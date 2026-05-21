# AGENTS.md — Kids Computer Science Class

This project supports a **live, weekly Kids Computer Science education program**. All materials directly impact students and should be treated as **production teaching content**.

---

## Role

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

## Git Conventions

### Commit Messages

All commit messages **must** follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <description>

[optional body]
```

**Types:**
| Type | Use When |
|------|----------|
| `feat` | Adding new lesson materials, scripts, or tools |
| `fix` | Correcting errors in existing materials |
| `docs` | Updating documentation (AGENTS.md, README, etc.) |
| `chore` | Maintenance tasks, dependency updates |
| `refactor` | Restructuring without changing behavior |

**Scope** is the lesson date or tool name: `2026-05-23`, `theme`, `tools`

**Examples:**
```
feat(2026-05-23): add AI Image & Multimodal Models lesson materials
fix(2026-05-16): correct Kahoot question 12 answer index
docs: update AGENTS.md with new tool instructions
chore(tools): add test_pptx_layout.py validator
```

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

All other time is dynamically adjusted. Sessions typically include:

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

## Current Phase

**April 2026** → Focus on **Artificial Intelligence**

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

Every lesson — regardless of the current curriculum phase — should include at least one connection to **Artificial Intelligence**.

When creating materials:
- **Presentations:** Include at least one slide connecting the lesson topic to AI
- **Classwork/Homework:** Include at least one question that ties the topic to AI
- **Kahoot:** Include at least one AI-related question
- **Class Activity:** Include a discussion point or demo that connects AI to the lesson

Examples of AI connections by phase:
- **Networking & Cloud:** AI models train on GPU clusters in cloud data centers
- **Cybersecurity:** AI is used for both attacks (deepfakes) and defense (spam filters, threat detection)
- **Programming:** AI coding assistants (Claude Code, GitHub Copilot); AI models are built with Python

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
python tools/read_pptx.py path/to/file.pptx       # Read specific file
python tools/read_pptx.py --all                    # Read ALL .pptx in current folder
python tools/read_pptx.py                          # Interactive mode
```

---

### tools/read_docx.py — Word Document Reader

Extracts text content from `.docx` files.

```bash
python tools/read_docx.py path/to/file.docx
python tools/read_docx.py --all
```

**Requires:** `python-docx`

---

### tools/read_pdf.py — PDF Reader

Extracts text content from `.pdf` files.

```bash
python tools/read_pdf.py path/to/file.pdf
python tools/read_pdf.py --all
```

**Requires:** `pypdf`

---

### scripts/create_presentation.py — PowerPoint Generator

Creates presentations using the standard theme from `tools/create_theme.py`.

```bash
# Run from inside a lesson folder
python scripts/create_presentation.py
```

**How to import theme in lesson scripts:**
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from create_theme import *
```

#### PowerPoint Formatting Best Practices (python-pptx)

**Slide Dimensions (16:9 Widescreen):**
- Width: 13.33 inches / Height: 7.5 inches
- Safe content area: y = 1.5 to y = 7.0

**Element Positioning Math:**
```
Bottom of element = y_position + height
```

**Multi-Row Layouts:**
```python
y = start_y + (row_index * row_spacing)
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

---

### scripts/create_kahoot_excel.py — Kahoot Quiz Generator

Creates Excel files in the official Kahoot import format.

```bash
python scripts/create_kahoot_excel.py
```

**Format:** Question | Answer 1-4 | Time limit | Correct answer

---

### scripts/create_homework_pdf.py — Fillable PDF Homework Generator

Creates interactive PDF documents with form fields, checkboxes, and text areas.

```bash
python scripts/create_homework_pdf.py
```

**IMPORTANT — No Character Limits on Form Fields:**
> Always set `maxlen=0` on all `acroForm.textfield()` calls. Reportlab defaults `maxlen` to 100.

```python
# GOOD — unlimited text
c.acroForm.textfield(name=field_name, ..., maxlen=0)
```

**IMPORTANT — Always Set PDF Title Metadata:**
> Always call `c.setTitle()` right after creating the canvas.

```python
c = canvas.Canvas(output_path, pagesize=letter)
c.setTitle("Classwork: Cybersecurity Detective")
```

**Requires:** `reportlab`

---

### scripts/create_classwork_pdf.py — Fillable PDF Classwork Generator

Same as homework generator but uses a class-based `ClassworkPDF` builder.

**Requires:** `reportlab`

---

### tools/test_pdf_fields.py — PDF Form Field Validator

```bash
python tools/test_pdf_fields.py <pdf_file>   # Test specific file
python tools/test_pdf_fields.py --all        # Test all PDFs in folder
```

**Use after:** Creating new PDFs to ensure no fields are cut off.

---

### tools/test_pptx_layout.py — PowerPoint Layout Validator

```bash
python tools/test_pptx_layout.py <pptx_file>   # Test specific file
python tools/test_pptx_layout.py --all          # Test all .pptx in folder
```

**Use after:** Generating or modifying presentations.

---

### tools/create_theme.py — Standard Presentation Theme

**Color palette:** `COLORS` dict with `dark_blue`, `medium_blue`, `light_blue`, `sky_blue`, `orange`, `green`, `red`, `purple`, `teal`, `violet`, `amber`, `pink`, `coral`, `white`, `light_gray`, `dark_gray`, `black`.

**Key functions:**
- `add_title_bar(slide, text, subtitle)` — Dark blue title bar with orange accent line
- `add_styled_textbox(slide, ...)` — Consistent text styling
- `add_rounded_box(slide, ...)` — Rounded rectangle with optional text/border
- `add_circle(slide, ...)` — Circle with optional centered text
- `add_arrow(slide, ...)` — Directional arrow shape
- `add_agenda_item(slide, num, text, y, color)` — Agenda items
- `add_takeaway_bar(slide, text, color)` — Bottom bar for key messages
- `create_title_slide(prs, title, subtitle, date, tagline)` — Title slide template
- `create_questions_slide(prs, prompt_text)` — Questions slide template

---

### Dependencies

```bash
pip install python-pptx python-docx openpyxl reportlab pypdf
```

---

## File & Folder Organization

### Folder Structure

```
KidsComputerScience/
├── AGENTS.md                           # Project instructions (this file)
├── CLAUDE.md                           # Points to AGENTS.md (Claude Code / Claude)
├── .github/
│   └── copilot-instructions.md         # Points to AGENTS.md (VS Code Copilot)
├── tools/                              # Reusable utility scripts
│   ├── read_pptx.py
│   ├── read_docx.py
│   ├── read_pdf.py
│   ├── test_pdf_fields.py
│   ├── test_pptx_layout.py
│   └── create_theme.py
├── theme/
│   └── EverestIT_Theme_Demo.pptx
└── YYYY-MM-DD_Topic_Name/              # Class session folders
    ├── scripts/
    │   ├── create_presentation.py
    │   ├── create_classwork_pdf.py
    │   ├── create_homework_pdf.py
    │   └── create_kahoot_excel.py
    ├── *.pptx
    ├── *.pdf
    └── ...
```

### File Naming Convention

```
YYYY-MM-DD_Topic_Name.pptx              # Main presentation
YYYY-MM-DD_Kahoot_Questions.md          # Kahoot question reference
YYYY-MM-DD_Kahoot_Import.xlsx           # Kahoot import file
YYYY-MM-DD_Class_Activity.md            # In-class guided activities
YYYY-MM-DD_Classwork_*.pdf              # Fillable PDF classwork
YYYY-MM-DD_Homework_*.pdf               # Fillable PDF homework
Classwork_Teams_Post.txt                # Teams posting instructions
Homework_Teams_Post.txt                 # Teams posting instructions
*_content.txt                           # Extracted text (auto-generated, do not commit)
```

---

## Lesson Planning Workflow

When asked to help plan a new lesson:

**Finding previous lessons:** Lesson folders are date-stamped (`YYYY-MM-DD_Topic_Name`), so "last class" or "previous lesson" means the folder with the most recent date.

1. **Review previous lesson(s)** — Use `tools/read_pptx.py` or read existing materials
2. **Check the curriculum phase** — Ensure the new topic fits the current phase
3. **Suggest next lesson topics** — Natural progression from previous content
4. **Propose lesson structure** — Objectives, vocabulary, activities, Kahoot, homework
