"""
PDF Reader Utility
Extracts text content from .pdf files for easy reference.

Usage:
    python read_pdf.py <filename.pdf>
    python read_pdf.py                     # Lists all .pdf files and lets you choose
    python read_pdf.py --all               # Reads all .pdf files in the folder

Output is saved to a .txt file with the same name.

Dependencies:
    pip install pypdf
"""

import os
import sys
from pypdf import PdfReader


def extract_text_from_pdf(filepath):
    """Extract all text content from a PDF file."""
    reader = PdfReader(filepath)
    output = []

    filename = os.path.basename(filepath)
    output.append("=" * 60)
    output.append(f"FILE: {filename}")
    output.append(f"PAGES: {len(reader.pages)}")
    output.append("=" * 60)
    output.append("")

    for i, page in enumerate(reader.pages, 1):
        output.append(f"{'='*20} PAGE {i} {'='*20}")
        text = page.extract_text()
        if text and text.strip():
            output.append(text.strip())
        else:
            output.append("[No extractable text on this page]")
        output.append("")

    # Report form fields if present
    fields = reader.get_fields()
    if fields:
        output.append("=" * 40)
        output.append(f"FORM FIELDS: {len(fields)}")
        output.append("=" * 40)
        for name, field in fields.items():
            field_type = field.get("/FT", "Unknown")
            value = field.get("/V", "")
            output.append(f"  {name} ({field_type}): {value}")

    return "\n".join(output)


def list_pdf_files(folder):
    """List all .pdf files in a folder."""
    files = []
    for f in os.listdir(folder):
        if f.lower().endswith('.pdf') and not f.startswith('~$'):
            files.append(f)
    return sorted(files)


def save_output(content, original_filepath):
    """Save extracted content to a text file."""
    base = os.path.splitext(original_filepath)[0]
    output_path = f"{base}_content.txt"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path


def main():
    folder = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == '--all':
            files = list_pdf_files(folder)
            if not files:
                print("No .pdf files found in this folder.")
                return

            print(f"Found {len(files)} PDF files.\n")

            for filename in files:
                filepath = os.path.join(folder, filename)
                print(f"Reading: {filename}...")

                try:
                    content = extract_text_from_pdf(filepath)
                    output_path = save_output(content, filepath)
                    print(f"  Saved to: {os.path.basename(output_path)}")
                except Exception as e:
                    print(f"  Error: {e}")

            print("\nDone!")

        elif arg in ('--help', '-h'):
            print(__doc__)

        else:
            # Read specific file
            if not arg.lower().endswith('.pdf'):
                arg += '.pdf'

            filepath = os.path.join(folder, arg) if not os.path.isabs(arg) else arg

            if not os.path.exists(filepath):
                print(f"File not found: {filepath}")
                return

            print(f"Reading: {arg}...")
            content = extract_text_from_pdf(filepath)

            # Print to console
            print("\n" + content)

            # Save to file
            output_path = save_output(content, filepath)
            print(f"\nSaved to: {output_path}")

    else:
        # Interactive mode
        files = list_pdf_files(folder)

        if not files:
            print("No .pdf files found in this folder.")
            return

        print("Available PDF files:\n")
        for i, f in enumerate(files, 1):
            print(f"  {i}. {f}")

        print(f"\n  A. Read ALL files")
        print(f"  Q. Quit\n")

        choice = input("Enter number or letter: ").strip()

        if choice.upper() == 'Q':
            return
        elif choice.upper() == 'A':
            for filename in files:
                filepath = os.path.join(folder, filename)
                print(f"\nReading: {filename}...")

                try:
                    content = extract_text_from_pdf(filepath)
                    output_path = save_output(content, filepath)
                    print(f"  Saved to: {os.path.basename(output_path)}")
                except Exception as e:
                    print(f"  Error: {e}")
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(files):
                    filename = files[idx]
                    filepath = os.path.join(folder, filename)

                    print(f"\nReading: {filename}...\n")
                    content = extract_text_from_pdf(filepath)

                    print(content)

                    output_path = save_output(content, filepath)
                    print(f"\nSaved to: {output_path}")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input.")


if __name__ == "__main__":
    main()
