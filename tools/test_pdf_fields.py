"""
PDF Form Field Validator
Tests whether form fields in a PDF are properly positioned within page boundaries,
checks for spacing/padding issues between consecutive fields, and lints Python
generator scripts for missing spacing after info_box() calls.

Usage:
    python test_pdf_fields.py <pdf_file>
    python test_pdf_fields.py --all          # Test all PDFs in current folder
    python test_pdf_fields.py --lint         # Lint Python scripts for spacing issues
    python test_pdf_fields.py                # Interactive mode

Dependencies:
    pip install pypdf
"""

import os
import re
import sys
from pypdf import PdfReader


# Page margins (in points, 1 inch = 72 points)
MARGIN_TOP = 72  # 1 inch from top
MARGIN_BOTTOM = 50  # Allow for footer
MARGIN_LEFT = 36  # 0.5 inch
MARGIN_RIGHT = 36  # 0.5 inch

# Spacing thresholds (in points)
MIN_FIELD_GAP = 5  # Minimum gap between consecutive fields (points)
TIGHT_SPACING_THRESHOLD = 8  # Warn if gap is less than this


class FieldValidator:
    """Validates form field positions in a PDF."""

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.reader = PdfReader(pdf_path)
        self.issues = []
        self.warnings = []
        self.field_count = 0

    def validate(self):
        """Validate all form fields in the PDF."""
        print(f"\n{'='*60}")
        print(f"VALIDATING: {os.path.basename(self.pdf_path)}")
        print(f"{'='*60}")

        # Get form fields
        if "/AcroForm" not in self.reader.trailer["/Root"]:
            print("  [INFO] No form fields found in this PDF.")
            return True

        fields = self.reader.get_fields()
        if not fields:
            print("  [INFO] No form fields found in this PDF.")
            return True

        self.field_count = len(fields)
        print(f"  Found {self.field_count} form fields across {len(self.reader.pages)} pages.\n")

        # Collect all field rects per page for spacing checks
        page_fields = {}  # page_num -> [(field_name, y1, y2, x1, x2)]

        # Check each field for boundary issues and collect positions
        for field_name, field_data in fields.items():
            self._check_field(field_name, field_data, page_fields)

        # Check spacing between fields on each page
        self._check_field_spacing(page_fields)

        # Report results
        self._report()

        return len(self.issues) == 0

    def _check_field(self, field_name, field_data, page_fields):
        """Check a single field for positioning issues."""

        # Get field rectangle (position)
        if "/Rect" not in field_data:
            # Try to get from widget annotation
            if "/Kids" in field_data:
                for kid in field_data["/Kids"]:
                    kid_obj = kid.get_object()
                    if "/Rect" in kid_obj:
                        page_num = self._find_page_number(kid_obj.get("/P"))
                        self._validate_rect(field_name, kid_obj["/Rect"], kid_obj.get("/P"))
                        self._collect_field_pos(field_name, kid_obj["/Rect"], page_num, page_fields)
            return

        rect = field_data["/Rect"]
        page_ref = field_data.get("/P")
        page_num = self._find_page_number(page_ref)

        self._validate_rect(field_name, rect, page_ref)
        self._collect_field_pos(field_name, rect, page_num, page_fields)

    def _find_page_number(self, page_ref):
        """Find the page number for a page reference."""
        if page_ref is None:
            return 0

        try:
            page_obj = page_ref.get_object()
            for i, page in enumerate(self.reader.pages):
                if page.get_object() == page_obj:
                    return i + 1
        except:
            pass
        return 0

    def _collect_field_pos(self, field_name, rect, page_num, page_fields):
        """Collect field position for spacing analysis."""
        try:
            x1 = float(rect[0])
            y1 = float(rect[1])
            x2 = float(rect[2])
            y2 = float(rect[3])
        except (TypeError, ValueError, IndexError):
            return

        if page_num not in page_fields:
            page_fields[page_num] = []
        page_fields[page_num].append((field_name, y1, y2, x1, x2))

    def _validate_rect(self, field_name, rect, page_ref):
        """Validate field rectangle against page boundaries."""

        # rect format: [x1, y1, x2, y2] (lower-left and upper-right corners)
        try:
            x1 = float(rect[0])
            y1 = float(rect[1])
            x2 = float(rect[2])
            y2 = float(rect[3])
        except (TypeError, ValueError, IndexError) as e:
            self.warnings.append(f"  [{field_name}] Could not parse rect: {rect}")
            return

        # Get page dimensions (default to letter size: 612 x 792 points)
        page_width = 612
        page_height = 792

        if page_ref:
            try:
                page_obj = page_ref.get_object()
                if "/MediaBox" in page_obj:
                    media_box = page_obj["/MediaBox"]
                    page_width = float(media_box[2])
                    page_height = float(media_box[3])
            except:
                pass

        # Calculate field dimensions
        field_width = abs(x2 - x1)
        field_height = abs(y2 - y1)

        # Check for issues
        issues_found = []

        # Check left boundary
        if x1 < MARGIN_LEFT:
            issues_found.append(f"extends past left margin (x1={x1:.1f}, margin={MARGIN_LEFT})")

        # Check right boundary
        if x2 > page_width - MARGIN_RIGHT:
            issues_found.append(f"extends past right margin (x2={x2:.1f}, max={page_width - MARGIN_RIGHT:.1f})")

        # Check bottom boundary (most common issue)
        if y1 < MARGIN_BOTTOM:
            issues_found.append(f"CUT OFF at bottom (y1={y1:.1f}, margin={MARGIN_BOTTOM})")

        # Check top boundary
        if y2 > page_height - MARGIN_TOP:
            issues_found.append(f"extends past top margin (y2={y2:.1f}, max={page_height - MARGIN_TOP:.1f})")

        # Check for zero/negative dimensions
        if field_width <= 0 or field_height <= 0:
            issues_found.append(f"invalid dimensions (width={field_width:.1f}, height={field_height:.1f})")

        # Check for extremely small fields
        if field_width < 10 or field_height < 8:
            self.warnings.append(f"  [{field_name}] Very small field (width={field_width:.1f}, height={field_height:.1f})")

        # Record issues
        if issues_found:
            self.issues.append({
                "field": field_name,
                "rect": [x1, y1, x2, y2],
                "issues": issues_found
            })

    def _check_field_spacing(self, page_fields):
        """Check spacing between consecutive fields on each page."""

        for page_num in sorted(page_fields.keys()):
            fields = page_fields[page_num]

            if len(fields) < 2:
                continue

            # Sort fields by vertical position (top to bottom = high y to low y)
            # y2 is the top of the field, y1 is the bottom
            sorted_fields = sorted(fields, key=lambda f: -f[2])  # sort by y2 descending

            for i in range(len(sorted_fields) - 1):
                name_above = sorted_fields[i][0]
                y1_above = sorted_fields[i][1]  # bottom of upper field

                name_below = sorted_fields[i + 1][0]
                y2_below = sorted_fields[i + 1][2]  # top of lower field

                gap = y1_above - y2_below

                # Overlapping fields
                if gap < 0:
                    self.issues.append({
                        "field": f"{name_above} / {name_below}",
                        "rect": [],
                        "issues": [
                            f"OVERLAP on page {page_num}: fields overlap by {abs(gap):.1f}pt"
                        ]
                    })
                # Too close together
                elif gap < MIN_FIELD_GAP:
                    self.issues.append({
                        "field": f"{name_above} / {name_below}",
                        "rect": [],
                        "issues": [
                            f"CRAMPED on page {page_num}: only {gap:.1f}pt gap (min {MIN_FIELD_GAP}pt)"
                        ]
                    })
                # Tight but not critical
                elif gap < TIGHT_SPACING_THRESHOLD:
                    self.warnings.append(
                        f"  [page {page_num}] Tight spacing between '{name_above}' and '{name_below}': {gap:.1f}pt gap"
                    )

    def _report(self):
        """Print validation report."""

        if self.issues:
            print("  ISSUES FOUND:")
            print("  " + "-" * 50)
            for issue in self.issues:
                print(f"  FIELD: {issue['field']}")
                if issue['rect']:
                    print(f"    Position: ({issue['rect'][0]:.1f}, {issue['rect'][1]:.1f}) to ({issue['rect'][2]:.1f}, {issue['rect'][3]:.1f})")
                for problem in issue["issues"]:
                    print(f"    - {problem}")
                print()
        else:
            print("  [PASS] All fields are properly positioned within page boundaries.")

        if self.warnings:
            print("\n  WARNINGS:")
            for warning in self.warnings:
                print(warning)

        print(f"\n  SUMMARY: {self.field_count} fields checked, {len(self.issues)} issues, {len(self.warnings)} warnings")


# =============================================================================
# SCRIPT LINTER — catches missing spacing after info_box() calls
# =============================================================================

class ScriptLinter:
    """Lints Python PDF generator scripts for common spacing issues."""

    def __init__(self):
        self.issues = []

    def lint_file(self, filepath):
        """Lint a single Python file for spacing issues."""
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        file_issues = []

        i = 0
        while i < len(lines):
            stripped = lines[i].strip()

            # Detect info_box() CALLS (not method definitions)
            if ('info_box(' in stripped or '.info_box(' in stripped) \
                    and 'def ' not in stripped:
                # Find where this call ends (track parentheses)
                call_start = i
                paren_depth = 0
                call_end = i

                for j in range(i, len(lines)):
                    paren_depth += lines[j].count('(') - lines[j].count(')')
                    if paren_depth <= 0:
                        call_end = j
                        break

                # Find the next non-blank line after the call
                next_line_idx = call_end + 1
                while next_line_idx < len(lines) and lines[next_line_idx].strip() == '':
                    next_line_idx += 1

                if next_line_idx < len(lines):
                    next_stripped = lines[next_line_idx].strip()

                    # These are OK without extra spacing:
                    # - self.space() — explicit spacing
                    # - self.section_header() — has built-in 0.55" spacing
                    # - comments / page breaks
                    safe_patterns = (
                        'self.space(',
                        'self.section_header(',
                        '# ===',
                        'self._draw_footer(',
                        'self.new_page(',
                        'self.c.',
                    )

                    if not any(next_stripped.startswith(p) for p in safe_patterns):
                        file_issues.append({
                            'line': call_start + 1,
                            'next_line': next_line_idx + 1,
                            'next_content': next_stripped[:60],
                        })

                i = call_end + 1
            else:
                i += 1

        if file_issues:
            self.issues.append({
                'file': filepath,
                'problems': file_issues,
            })

        return len(file_issues) == 0

    def lint_folder(self, folder):
        """Find and lint all create_*.py scripts in folder and subfolders."""
        scripts = []

        for root, dirs, files in os.walk(folder):
            for f in files:
                if f.startswith('create_') and f.endswith('.py') and 'pdf' in f.lower():
                    scripts.append(os.path.join(root, f))

        if not scripts:
            print("  [INFO] No PDF generator scripts found.")
            return True

        print(f"\n{'='*60}")
        print("LINTING PDF GENERATOR SCRIPTS")
        print(f"{'='*60}")
        print(f"  Found {len(scripts)} script(s) to check.\n")

        for script in sorted(scripts):
            self.lint_file(script)

        self._report()
        return len(self.issues) == 0

    def _report(self):
        """Print lint results."""
        if self.issues:
            print("  SPACING ISSUES FOUND:")
            print("  " + "-" * 50)
            for file_issue in self.issues:
                rel_path = os.path.basename(os.path.dirname(os.path.dirname(file_issue['file'])))
                script_name = os.path.basename(file_issue['file'])
                print(f"  FILE: {rel_path}/scripts/{script_name}")
                for problem in file_issue['problems']:
                    print(f"    Line {problem['line']}: info_box() not followed by self.space()")
                    print(f"      Next line {problem['next_line']}: {problem['next_content']}")
                print()
        else:
            print("  [PASS] All info_box() calls have proper spacing after them.")

        total = sum(len(f['problems']) for f in self.issues)
        print(f"\n  SUMMARY: {total} missing spacing issue(s) found")


def find_pdfs(folder):
    """Find all PDF files in a folder."""
    pdfs = []
    for f in os.listdir(folder):
        if f.lower().endswith('.pdf') and not f.startswith('~$'):
            pdfs.append(os.path.join(folder, f))

    # Also check subfolders
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isdir(item_path):
            for f in os.listdir(item_path):
                if f.lower().endswith('.pdf') and not f.startswith('~$'):
                    pdfs.append(os.path.join(item_path, f))

    return sorted(pdfs)


def main():
    """Main entry point."""
    # tools/ lives one level below the project root
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.dirname(tools_dir)

    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == '--lint':
            # Lint Python scripts only
            linter = ScriptLinter()
            linter.lint_folder(folder)

        elif arg == '--all':
            # Test all PDFs
            pdfs = find_pdfs(folder)
            if not pdfs:
                print("No PDF files found.")
                return

            print(f"\nTesting {len(pdfs)} PDF file(s)...\n")

            results = []
            for pdf_path in pdfs:
                validator = FieldValidator(pdf_path)
                passed = validator.validate()
                results.append((os.path.basename(pdf_path), passed, len(validator.issues)))

            # Also run script linter
            linter = ScriptLinter()
            lint_passed = linter.lint_folder(folder)

            # Summary
            print("\n" + "=" * 60)
            print("OVERALL SUMMARY")
            print("=" * 60)
            for name, passed, issue_count in results:
                status = "PASS" if passed else f"FAIL ({issue_count} issues)"
                print(f"  [{status}] {name}")

            lint_status = "PASS" if lint_passed else "FAIL"
            print(f"  [{lint_status}] Script spacing lint")

            total_passed = sum(1 for _, p, _ in results if p)
            print(f"\n  Total: {total_passed}/{len(results)} PDFs passed validation.")

        elif arg in ('--help', '-h'):
            print(__doc__)

        else:
            # Test specific file
            pdf_path = arg if os.path.isabs(arg) else os.path.join(folder, arg)
            if not pdf_path.lower().endswith('.pdf'):
                pdf_path += '.pdf'

            if not os.path.exists(pdf_path):
                print(f"File not found: {pdf_path}")
                return

            validator = FieldValidator(pdf_path)
            validator.validate()

    else:
        # Interactive mode
        pdfs = find_pdfs(folder)

        if not pdfs:
            print("No PDF files found in this folder or subfolders.")
            return

        print("\nAvailable PDF files:\n")
        for i, pdf in enumerate(pdfs, 1):
            # Show relative path
            rel_path = os.path.relpath(pdf, folder)
            print(f"  {i}. {rel_path}")

        print(f"\n  A. Test ALL files")
        print(f"  Q. Quit\n")

        choice = input("Enter number or letter: ").strip()

        if choice.upper() == 'Q':
            return
        elif choice.upper() == 'A':
            for pdf_path in pdfs:
                validator = FieldValidator(pdf_path)
                validator.validate()
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(pdfs):
                    validator = FieldValidator(pdfs[idx])
                    validator.validate()
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input.")


if __name__ == "__main__":
    main()
