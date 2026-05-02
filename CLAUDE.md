# Claude.md — Kids Computer Science Class

This project supports a **live, weekly Kids Computer Science education program**. All materials directly impact students and should be treated as **production teaching content**.

---

## Your Role

You are a **patient teaching assistant**, not a production engineer. When working in this project:

- Optimize for **clarity and learning**
- Simplify whenever unsure
- Avoid introducing concepts before their scheduled phase
- Preserve curriculum progression across months
- Never impose rigid timelines on flexible content

---

## Audience

| Attribute | Details |
|-----------|---------|
| **Ages** | 10–18 (mostly 13–15, some younger and older) |
| **Experience** | Many true beginners; some limited prior exposure |
| **Format** | Remote, live instruction |

---

## Class Schedule

**Day:** Saturday
**Time:** 9:00 AM – 1:00 PM Pacific (4 hours total)

### Fixed Blocks (Non-Negotiable)

| Time | Activity |
|------|----------|
| 10:30 – 11:00 AM | Break |
| 11:00 – 11:30 AM | Typing Practice |

### Flexible Activities

All other time is dynamically adjusted. Sessions typically include some combination of:

- Opening check-in and recap
- Homework review and student walkthroughs
- Concept introduction
- Live demos or diagrams
- Guided hands-on activities
- Interactive recap or quiz (usually Kahoot)
- Tooling or setup walkthroughs
- Homework explanation

---

## Annual Curriculum Phases

Content must align with the **current phase**. Do not introduce concepts early.

### January → March: PC Hardware, Networking & Cloud

- PC components and how computers work
- Networking fundamentals (clients, servers, IP, DNS, HTTP)
- What "the cloud" is and why it exists
- Compute, storage, networking concepts
- How real apps and websites are hosted

### April → June: Artificial Intelligence

- What AI is (conceptual first)
- Prompting basics
- AI tools and safe usage
- Simple AI-powered projects
- Understanding limitations and ethics (age-appropriate)

### July → December: Programming

- Python fundamentals
- Logic and problem-solving
- Small projects and cumulative assignments
- Developer tools (VS Code, GitHub)
- Gradual progression, no rushing

> Programming supports other phases but becomes the **primary focus** July–December.

---

## Slide Decks

When creating or editing slides:

- **One core idea per slide** — avoid information overload
- Use **simple language** appropriate for teenagers
- Prefer **visuals and diagrams** over walls of text
- Build intuition before introducing formal definitions
- Include recap slides to reinforce key points
- Slides should support live teaching, not replace it

---

## Kahoot Quizzes

Most classes include a Kahoot quiz with **15 questions**.

### Question Guidelines

- Questions should **reinforce**, not trick
- Focus on:
  - Core concepts from the lesson
  - Vocabulary and definitions
  - Mental models and "why" understanding
- Use clear, unambiguous wording
- All answer choices should be plausible (no joke answers)
- Correct answers should feel obvious after the lesson

### Format

```
Q: [Question text]
A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]
Correct: [Letter]
```

---

## Code Style (When Applicable)

- Beginner-friendly only
- Plain Python preferred
- Avoid advanced abstractions
- Avoid clever shortcuts
- Comments should explain *why*, not just *what*
- Code must be readable by teenagers with no prior experience

---

## Homework Materials

- Homework is **cumulative** — builds on previous weeks
- Instructions in markdown (`.md`) with clear steps
- Python files should be short and focused
- Students must be able to complete work **without live help**
- Include examples where helpful

### Point Structure (Always Follow)

- **Classwork:** Always 100 points + 10 bonus points
- **Homework:** Always 100 points + 5 bonus points (or 10 bonus for longer assignments)

This keeps grading consistent and makes it easy for students to understand their scores.

### Submission Instructions (Always Include)

All classwork and homework must be submitted to:
1. **Microsoft Teams** (primary)
2. **Ishwari Raut ma'am** (copy)

---

## Teaching Philosophy

| Principle | Application |
|-----------|-------------|
| Adaptive pacing | Adjust to student understanding, not a clock |
| One idea at a time | Don't overload; depth over breadth |
| Intuition first | Build mental models before formal definitions |
| Repetition is intentional | Revisiting concepts is expected, not failure |
| Confidence over speed | Students should feel capable, not rushed |

### AI Connections (Always Include)

Every lesson — regardless of the current curriculum phase — should include at least one connection to **Artificial Intelligence**. AI is woven into every area of computer science, and students should start building that awareness early.

When creating materials:
- **Presentations:** Include at least one slide connecting the lesson topic to AI (e.g., how AI affects or is affected by the topic)
- **Classwork/Homework:** Include at least one question that ties the topic to AI
- **Kahoot:** Include at least one AI-related question
- **Class Activity:** Include a discussion point or demo that connects AI to the lesson

Examples of AI connections by phase:
- **Networking & Cloud:** AI models train on GPU clusters in cloud data centers; AI tools like Claude Code run in the terminal
- **Cybersecurity:** AI is used for both attacks (deepfakes, AI-generated phishing) and defense (spam filters, threat detection); AI tools require strong security practices
- **Programming:** AI coding assistants (Claude Code, GitHub Copilot); AI models are built with Python

The goal is to **build excitement** about the April AI phase while reinforcing that every topic they learn connects to AI in the real world.

---

## Python Tools Available

This project includes Python scripts to help create class materials. Always use these tools when available.

### Where Scripts Live

- **`tools/`** — Reusable utility scripts that work across all lessons (readers, validators). These live at the project root level.
- **`scripts/`** — Lesson-specific generator scripts (presentations, PDFs, Kahoot). These live inside each lesson folder (e.g., `2026-02-28_Topic/scripts/`). Each lesson gets its own copy so content can be customized independently.

When creating materials for a new lesson, always put generator scripts in `YYYY-MM-DD_Topic/scripts/`, not in the root `tools/` folder.

---

### tools/read_pptx.py — PowerPoint Reader

Extracts text content from `.pptx` files for easy reference.

```bash
# Read a specific file (prints to console + saves .txt)
python tools/read_pptx.py path/to/file.pptx

# Read ALL .pptx files in current folder
python tools/read_pptx.py --all

# Interactive mode (lists files, lets you choose)
python tools/read_pptx.py
```

**Output:** Creates `*_content.txt` files with slide-by-slide text extraction.

**Use this to:** Quickly reference previous lesson content without parsing binary files.

---

### tools/read_docx.py — Word Document Reader

Extracts text content from `.docx` files for easy reference.

```bash
# Read a specific file (prints to console + saves .txt)
python tools/read_docx.py path/to/file.docx

# Read ALL .docx files in current folder
python tools/read_docx.py --all

# Interactive mode (lists files, lets you choose)
python tools/read_docx.py
```

**Output:** Creates `*_content.txt` files with paragraph-by-paragraph text extraction. Marks headings and extracts tables.

**Use this to:** Quickly reference classwork/homework Word documents without opening them.

**Requires:** `python-docx` library

---

### tools/read_pdf.py — PDF Reader

Extracts text content from `.pdf` files for easy reference.

```bash
# Read a specific file (prints to console + saves .txt)
python tools/read_pdf.py path/to/file.pdf

# Read ALL .pdf files in current folder
python tools/read_pdf.py --all

# Interactive mode (lists files, lets you choose)
python tools/read_pdf.py
```

**Output:** Creates `*_content.txt` files with page-by-page text extraction. Also reports form fields if present.

**Use this to:** Quickly reference fillable PDF assignments without opening them.

**Requires:** `pypdf` library

---

### scripts/create_presentation.py — PowerPoint Generator

Creates beautifully designed PowerPoint presentations programmatically.

```bash
# Run from inside a lesson folder (e.g., 2026-01-25_Clients_Servers_How_Websites_Work/)
python scripts/create_presentation.py
```

**Features:**
- Modern color palette (blues, oranges, greens)
- Widescreen 16:9 format
- Consistent header bars with accent lines
- Rounded boxes, shapes, and visual diagrams
- One core idea per slide

**To modify:** Edit the slide creation functions and re-run the script.

#### PowerPoint Formatting Best Practices (python-pptx)

These guidelines prevent common layout issues like overlapping elements and cut-off text.

**Slide Dimensions (16:9 Widescreen):**
- Width: 13.33 inches
- Height: 7.5 inches
- Safe content area: y = 1.5 to y = 7.0 (leave room for header and footer)

**Element Positioning Math:**
```
Bottom of element = y_position + height
```
Always calculate where elements END, not just where they start.

**Multi-Row Layouts:**
```python
# Formula for row positioning
y = start_y + (row_index * row_spacing)

# Example: 3 rows starting at 1.7", with 1.5" spacing
# Row 0: y = 1.7
# Row 1: y = 3.2
# Row 2: y = 4.7
# If box height is 1.25", Row 2 ends at 5.95"
```

**Common Spacing Values:**
| Element Type | Recommended Height | Row Spacing |
|--------------|-------------------|-------------|
| Content boxes (2-3 lines) | 1.25 - 1.4 inches | 1.5 inches |
| Content boxes (4+ lines) | 2.2 - 2.5 inches | — |
| Summary boxes at bottom | 0.85 - 1.0 inches | — |
| Text items in a list | 0.4 - 0.45 inches | 0.4 - 0.45 inches |

**Preventing Overlap:**
1. Calculate the bottom position of all content rows
2. Place summary/footer boxes BELOW that (typically y = 6.3 - 6.5)
3. Leave 0.1 - 0.2 inch gap between elements

**Text in Rounded Boxes:**
- DON'T use the `text` parameter in `add_rounded_box()` for multi-line content
- DO use separate `add_styled_textbox()` calls overlaid on the box
- This gives precise control over text positioning

```python
# BAD - text may get cut off
add_rounded_box(slide, x, y, w, h, color, text="Long text here...")

# GOOD - full control over text position
add_rounded_box(slide, x, y, w, h, color)
add_styled_textbox(slide, x, y + 0.15, w, 0.5, "Title", bold=True)
add_styled_textbox(slide, x, y + 0.6, w, 0.8, "Description text")
```

**Box Height for Text Content:**
| Lines of Text | Minimum Box Height |
|---------------|-------------------|
| 1 line | 0.6 - 0.7 inches |
| 2 lines | 1.0 - 1.2 inches |
| 3-4 lines | 1.4 - 1.6 inches |
| 4+ lines (list) | 2.2 - 2.5 inches |

**Debugging Layout Issues:**
1. Print calculated y positions to console
2. Check that no element's bottom (y + height) exceeds 7.0
3. Verify gaps between elements are at least 0.1 inches
4. Regenerate and visually inspect after changes

---

### scripts/create_kahoot_excel.py — Kahoot Quiz Generator

Creates Excel files in the official Kahoot import format.

```bash
# Run from inside a lesson folder
python scripts/create_kahoot_excel.py
```

**Output:** `*_Kahoot_Import.xlsx` ready to upload to Kahoot.

**Format:** Question | Answer 1 | Answer 2 | Answer 3 | Answer 4 | Time limit | Correct answer

**To add questions:** Edit the `QUESTIONS` list in the script.

---

### scripts/create_homework_pdf.py — Fillable PDF Homework Generator

Creates interactive PDF documents with form fields, checkboxes, and text areas.

```bash
# Run from inside a lesson folder
python scripts/create_homework_pdf.py
```

**Output:** Fillable PDF homework documents (e.g., `*_Homework_Web_Explorer.pdf`)

**Features:**
- Styled headers with colored accent lines
- Section headers with colored backgrounds
- Text input fields for short answers
- Multi-line text areas for longer responses
- Checkboxes for True/False and selection questions
- Matching exercises with answer fields
- Fun fact and info boxes
- Professional color palette (blues, greens, purples, oranges)
- Submission instructions in footer

**Available helper functions:**
- `draw_header()` — Page header with title, subtitle, page numbers
- `draw_section_header()` — Colored section title bars
- `draw_text_field()` — Single-line text input with label
- `draw_multiline_field()` — Large text area for paragraphs
- `draw_checkbox()` — Checkbox with label
- `draw_radio_group()` — Multiple choice radio buttons
- `draw_fun_box()` — Colored info/highlight box
- `draw_matching_exercise()` — Term matching with answer fields

**To create new homework:** Copy the `create_homework_jan25()` function as a template and modify content.

**Requires:** `reportlab` library

**IMPORTANT — No Character Limits on Form Fields:**
> Always set `maxlen=0` on all `acroForm.textfield()` calls (both single-line and multiline). Reportlab defaults `maxlen` to 100, which silently caps student input at ~100 characters. Use `maxlen=0` to allow unlimited text.

```python
# GOOD — unlimited text
c.acroForm.textfield(name=field_name, ..., maxlen=0)

# BAD — reportlab defaults to maxlen=100, students get cut off
c.acroForm.textfield(name=field_name, ...)
```

**IMPORTANT — Always Set PDF Title Metadata:**
> Always call `c.setTitle()` right after creating the canvas so the PDF has a meaningful title in viewers/browsers instead of "untitled". Use a descriptive title matching the document's purpose.

```python
# GOOD — PDF shows a meaningful title in the viewer tab
c = canvas.Canvas(output_path, pagesize=letter)
c.setTitle("Classwork: Cybersecurity Detective")

# BAD — PDF shows "untitled" in the viewer tab
c = canvas.Canvas(output_path, pagesize=letter)
```

---

### scripts/create_classwork_pdf.py — Fillable PDF Classwork Generator

Creates interactive PDF classwork documents with form fields, checkboxes, and text areas. Uses a class-based architecture for better organization.

```bash
# Run from inside a lesson folder
python scripts/create_classwork_pdf.py
```

**Output:** Fillable PDF classwork documents (e.g., `*_Classwork_Internet_Investigator.pdf`)

**Features:**
- Class-based `ClassworkPDF` builder for clean code organization
- Design system with `Colors` and `Layout` classes
- All homework features plus case file sections
- Multiple choice questions with checkboxes
- Matching exercises
- Better page management with dedicated pages per section

**To create new classwork:** Modify the `build()` method in the `ClassworkPDF` class.

**Requires:** `reportlab` library

---

### tools/test_pdf_fields.py — PDF Form Field Validator

Validates that form fields in PDFs are properly positioned within page boundaries.

```bash
python tools/test_pdf_fields.py <pdf_file>   # Test specific file
python tools/test_pdf_fields.py --all        # Test all PDFs in folder
python tools/test_pdf_fields.py              # Interactive mode
```

**Features:**
- Checks all form fields against page margins
- Detects cut-off fields at page boundaries
- Reports field positions and issues
- Validates multiple PDFs at once

**Use this:** After creating new PDFs to ensure no fields are cut off.

**Requires:** `pypdf` library

---

### tools/create_theme.py — Standard Presentation Theme

Provides reusable helper functions for creating clean, colorful PowerPoint slides. Dark blue title bars, orange accent lines, colorful rounded boxes, white backgrounds.

```bash
# Generate the theme demo (saves to theme/ folder)
python tools/create_theme.py
```

**How to use in lesson scripts:**
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from create_theme import *
```

**Color palette:** `COLORS` dict with `dark_blue`, `medium_blue`, `light_blue`, `sky_blue`, `orange`, `green`, `red`, `purple`, `teal`, `violet`, `amber`, `pink`, `coral`, `white`, `light_gray`, `dark_gray`, `black`. Lesson scripts can add topic-specific colors (e.g., `COLORS["ai_purple"]`).

**Key functions:**
- `set_shape_fill(shape, color)` — Solid fill a shape
- `set_shape_line(shape, color, width_pt)` — Set shape border
- `add_styled_textbox(slide, ...)` — Text box with consistent styling
- `add_rounded_box(slide, ...)` — Rounded rectangle with optional text and border
- `add_circle(slide, ...)` — Circle with optional centered text
- `add_arrow(slide, ...)` — Directional arrow shape
- `add_table_row(slide, ...)` — Row of boxes that looks like a table row
- `add_title_bar(slide, text, subtitle)` — Dark blue title bar with orange accent line
- `add_agenda_item(slide, num, text, y, color)` — Colored circle + label for agendas
- `add_takeaway_bar(slide, text, color)` — Bottom bar for key messages
- `add_full_bg(slide, color)` — Full-slide solid background
- `create_title_slide(prs, title, subtitle, date, tagline)` — Standard title slide template
- `create_questions_slide(prs, prompt_text)` — Standard questions slide template

**Output:** `theme/EverestIT_Theme_Demo.pptx` — demo showing all available styles

**Requires:** `python-pptx`

---

### tools/test_pptx_layout.py — PowerPoint Layout Validator

Validates that shapes and text in PowerPoint files are properly positioned, not overlapping, and not overflowing.

```bash
python tools/test_pptx_layout.py <pptx_file>   # Test specific file
python tools/test_pptx_layout.py --all          # Test all .pptx files in folder
python tools/test_pptx_layout.py                # Interactive mode
```

**Features:**
- Checks shapes against slide boundaries (flags elements extending past edges)
- Detects text-on-text overlaps (major overlaps = errors, minor = warnings)
- Estimates text overflow (when text is too long for its container)
- Detects zero-size shapes
- Reports errors and warnings per slide

**Use this:** After generating or modifying presentations to catch layout issues.

**Requires:** `python-pptx` library

---

### Dependencies

All scripts require these Python packages:

```bash
pip install python-pptx python-docx openpyxl reportlab pypdf
```

---

## File & Folder Organization

### Folder Structure

```
EverestIT Claude/
├── CLAUDE.md                           # Project instructions
├── tools/                              # Reusable utility scripts
│   ├── read_pptx.py                    # PowerPoint text extractor
│   ├── read_docx.py                    # Word document text extractor
│   ├── read_pdf.py                     # PDF text extractor
│   ├── test_pdf_fields.py              # PDF form validator
│   ├── test_pptx_layout.py            # PowerPoint layout validator
│   └── create_theme.py                 # Standard presentation theme & helpers
├── theme/                              # Reusable theme assets
│   └── EverestIT_Theme_Demo.pptx       # Theme demo showing all styles
└── YYYY-MM-DD_Topic_Name/              # Class session folders (date-first for sorting)
    ├── scripts/                        # Class-specific Python generators
    │   ├── create_presentation.py
    │   ├── create_classwork_pdf.py
    │   ├── create_homework_pdf.py
    │   └── create_kahoot_excel.py
    ├── *.pptx                          # Presentations
    ├── *.pdf                           # Fillable assignments
    └── ...                             # Other class materials
```

Example: `2026-01-25_Clients_Servers_How_Websites_Work/`

### File Naming Convention

Inside each class folder:

```
YYYY-MM-DD_Topic_Name.pptx              # Main presentation
YYYY-MM-DD_Topic_Name_BEAUTIFUL.pptx    # Python-generated presentation
YYYY-MM-DD_Kahoot_Questions.md          # Kahoot question reference
YYYY-MM-DD_Kahoot_Import.xlsx           # Kahoot import file
YYYY-MM-DD_Class_Activity.md            # In-class guided activities
YYYY-MM-DD_Classwork_*.md               # Student assignments (Teams format)
YYYY-MM-DD_Classwork_*_Notepad.txt      # Student assignments (plain text)
YYYY-MM-DD_Classwork_*.pdf              # Fillable PDF classwork
YYYY-MM-DD_Homework_*.pdf               # Fillable PDF homework
Classwork_Teams_Post.txt                # Teams posting instructions
*_content.txt                           # Extracted PowerPoint text
```

---

## Lesson Planning Workflow

When asked to help plan a new lesson:

**Finding previous lessons:** Lesson folders are date-stamped (`YYYY-MM-DD_Topic_Name`), so "last class" or "previous lesson" means the folder with the most recent date. List the project folder to find it.

1. **Review previous lesson(s)** — Use `tools/read_pptx.py` or read existing materials to understand:
   - What concepts were already covered
   - What vocabulary students know
   - How content was structured and paced
   - Any homework that was assigned (students may have questions)

2. **Check the curriculum phase** — Ensure the new topic fits the current phase (see Annual Curriculum Phases above)

3. **Suggest next lesson topics** — Based on:
   - Natural progression from previous content
   - Building on concepts students already understand
   - Gaps that need filling before moving forward
   - Upcoming topics in the curriculum roadmap

4. **Propose lesson structure** — Include:
   - Learning objectives (what students will understand)
   - Key vocabulary to introduce
   - Suggested activities and demos
   - Kahoot quiz topics
   - Homework ideas that reinforce the lesson

**Example prompt:** "Look at last week's lesson and suggest what we should cover next Saturday."

---

## Current Phase

**April 2026** → Focus on **Artificial Intelligence**
