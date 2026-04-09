# Kids Computer Science

Weekly computer science education program for students ages 10-18. Classes run every Saturday, 9 AM - 1 PM Pacific, taught live and remotely.

## Curriculum

| Phase | Months | Topics |
|-------|--------|--------|
| Networking & Cloud | Jan - Mar | PC hardware, networking, cloud, data centers, Linux, CLI, cybersecurity |
| Artificial Intelligence | Apr - Jun | What AI is, prompting, AI tools, simple AI projects, ethics |
| Programming | Jul - Dec | Python fundamentals, logic, projects, VS Code, GitHub |

## Repository Structure

```
KidsComputerScience/
├── CLAUDE.md                        # Detailed project instructions
├── CODEX.md                         # Quick-reference for Codex workflows
├── tools/                           # Shared utility scripts
│   ├── create_theme.py              # Standard presentation theme
│   ├── read_pptx.py                 # PowerPoint text extractor
│   ├── read_docx.py                 # Word document text extractor
│   ├── read_pdf.py                  # PDF text extractor
│   ├── test_pdf_fields.py           # PDF form field validator
│   └── test_pptx_layout.py          # PowerPoint layout validator
├── theme/                           # Theme demo files
├── Marketing/                       # Promotional materials
└── YYYY-MM-DD_Topic_Name/           # Lesson folders (one per week)
    ├── scripts/                     # Python generators for this lesson
    │   ├── create_presentation.py
    │   ├── create_classwork_pdf.py
    │   ├── create_homework_pdf.py
    │   └── create_kahoot_excel.py
    ├── *.pptx                       # Presentations
    ├── *.pdf                        # Fillable classwork/homework
    ├── *.xlsx                       # Kahoot import files
    └── *.md                         # Activities, notes
```

## Tools

All lesson materials are generated programmatically with Python scripts.

**Setup:**
```bash
pip install python-pptx python-docx openpyxl reportlab pypdf
```

**Generate a presentation:**
```bash
cd 2026-04-11_Prompt_Engineering_and_Using_AI_Tools/scripts
python create_presentation.py
```

**Validate layouts after generating:**
```bash
python tools/test_pptx_layout.py path/to/file.pptx
python tools/test_pdf_fields.py path/to/file.pdf
```

**Extract content for review:**
```bash
python tools/read_pptx.py path/to/file.pptx
python tools/read_docx.py path/to/file.docx
python tools/read_pdf.py path/to/file.pdf
```

## Presentation Theme

Lessons use a shared theme (`tools/create_theme.py`) with dark blue title bars, orange accent lines, and colorful rounded boxes on white backgrounds. Lesson scripts import it with:

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from create_theme import *
```

Run `python tools/create_theme.py` to generate the theme demo at `theme/EverestIT_Theme_Demo.pptx`.

## Class Materials

Each lesson includes:
- **Presentation** (.pptx) — one core idea per slide, visual-first
- **Classwork** (.pdf) — fillable, 100 points + 10 bonus
- **Homework** (.pdf) — fillable, 100 points + 5-10 bonus
- **Kahoot quiz** (.xlsx) — ~12 reinforcement questions
- **Class activity** (.md) — guided hands-on exercise

Every lesson includes at least one connection to AI, regardless of the current curriculum phase.
