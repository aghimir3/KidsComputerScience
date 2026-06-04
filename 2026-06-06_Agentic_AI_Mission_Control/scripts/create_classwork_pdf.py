"""
Classwork PDF Generator - June 6, 2026
Agentic AI Mission Control

Students supervise an AI app-builder using a job brief, permissions,
small changes, and a test checklist.

Usage:
    py create_classwork_pdf.py

Dependencies:
    pip install reportlab
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth


class Colors:
    DARK_BLUE = HexColor("#1E3A5F")
    MEDIUM_BLUE = HexColor("#3467A6")
    SKY_BLUE = HexColor("#ADD8E6")
    ORANGE = HexColor("#FF9933")
    GREEN = HexColor("#4CAF50")
    LIGHT_GREEN = HexColor("#C8E6C9")
    PURPLE = HexColor("#673AB7")
    LIGHT_PURPLE = HexColor("#EDE7F6")
    RED = HexColor("#D32F2F")
    LIGHT_RED = HexColor("#FFCDD2")
    TEAL = HexColor("#00897B")
    LIGHT_TEAL = HexColor("#B2DFDB")
    AMBER = HexColor("#FFB300")
    LIGHT_AMBER = HexColor("#FFECB3")
    LIGHT_GRAY = HexColor("#F5F5F5")
    DARK_GRAY = HexColor("#424242")
    WHITE = HexColor("#FFFFFF")


class Layout:
    WIDTH, HEIGHT = letter
    MARGIN = 0.5 * inch
    CONTENT_WIDTH = WIDTH - (2 * MARGIN)
    HEADER_HEIGHT = 1.0 * inch
    FOOTER_HEIGHT = 0.65 * inch
    CONTENT_TOP = HEIGHT - HEADER_HEIGHT - 0.3 * inch


class ClassworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Classwork: Agentic AI Mission Control")
        self.page_num = 0
        self.total_pages = 4
        self.y = Layout.CONTENT_TOP

    def new_page(self):
        if self.page_num > 0:
            self._draw_footer()
            self.c.showPage()
        self.page_num += 1
        self._draw_header()
        self.y = Layout.CONTENT_TOP

    def finish(self):
        self._draw_footer()
        self.c.save()

    def _draw_header(self):
        c = self.c
        c.setFillColor(Colors.DARK_BLUE)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT,
               Layout.WIDTH, Layout.HEADER_HEIGHT, fill=True, stroke=False)
        c.setFillColor(Colors.ORANGE)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT - 4,
               Layout.WIDTH, 4, fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 17)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.52 * inch,
                     "CLASSWORK: Agentic AI Mission Control")
        c.setFont("Helvetica", 9)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.78 * inch,
                     "From vibe coding to supervised AI agents")
        c.setFont("Helvetica", 9)
        c.setFillColor(Colors.WHITE)
        c.drawRightString(Layout.WIDTH - Layout.MARGIN,
                          Layout.HEIGHT - 0.52 * inch,
                          f"Page {self.page_num} of {self.total_pages}")

    def _draw_footer(self):
        c = self.c
        c.setFillColor(Colors.DARK_BLUE)
        c.rect(0, 0, Layout.WIDTH, Layout.FOOTER_HEIGHT,
               fill=True, stroke=False)
        c.setFillColor(Colors.ORANGE)
        c.rect(0, Layout.FOOTER_HEIGHT, Layout.WIDTH, 3,
               fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(Layout.MARGIN, 0.4 * inch, "SUBMISSION:")
        c.setFont("Helvetica", 9)
        c.drawString(1.4 * inch, 0.4 * inch,
                     "1. Microsoft Teams   2. Copy to Ishwari Raut ma'am")
        c.drawString(Layout.MARGIN, 0.2 * inch,
                     "Due: End of class  |  Total Points: 100 (+10 bonus)")

    def _wrap_lines(self, text, font="Helvetica", size=9, max_width=None):
        if max_width is None:
            max_width = Layout.CONTENT_WIDTH - 0.35 * inch
        lines = []
        for raw_line in text.splitlines():
            words = raw_line.split()
            if not words:
                lines.append("")
                continue
            current = ""
            for word in words:
                test = f"{current} {word}".strip()
                if stringWidth(test, font, size) <= max_width:
                    current = test
                else:
                    lines.append(current)
                    current = word
            if current:
                lines.append(current)
        return lines

    def section_header(self, title, color):
        c = self.c
        c.setFillColor(color)
        c.roundRect(Layout.MARGIN, self.y - 0.28 * inch,
                    Layout.CONTENT_WIDTH, 0.38 * inch, 5,
                    fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(Layout.MARGIN + 0.15 * inch,
                     self.y - 0.16 * inch, title)
        self.y -= 0.52 * inch

    def info_box(self, title, content, color, height=0.75 * inch):
        c = self.c
        c.setFillColor(color)
        c.setStrokeColor(Colors.MEDIUM_BLUE)
        c.roundRect(Layout.MARGIN, self.y - height,
                    Layout.CONTENT_WIDTH, height, 7,
                    fill=True, stroke=True)
        c.setFillColor(Colors.DARK_BLUE)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(Layout.MARGIN + 0.15 * inch,
                     self.y - 0.18 * inch, title)
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 9)
        text_y = self.y - 0.36 * inch
        for line in self._wrap_lines(content)[:5]:
            c.drawString(Layout.MARGIN + 0.15 * inch, text_y, line)
            text_y -= 0.14 * inch
        self.y -= height + 0.14 * inch

    def text(self, content, bold=False, size=10, indent=0):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        c.drawString(Layout.MARGIN + indent, self.y, content)
        self.y -= (size + 6)

    def wrapped_text(self, content, size=9, indent=0, line_gap=0.14 * inch):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", size)
        max_width = Layout.CONTENT_WIDTH - indent
        for line in self._wrap_lines(content, size=size, max_width=max_width):
            c.drawString(Layout.MARGIN + indent, self.y, line)
            self.y -= line_gap

    def text_field(self, label, field_name, label_width=1.3 * inch,
                   field_width=None, height=0.25 * inch):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN, self.y, label)
        field_x = Layout.MARGIN + label_width
        actual_width = field_width or (Layout.WIDTH - Layout.MARGIN - field_x)
        c.acroForm.textfield(
            name=field_name, x=field_x, y=self.y - 5,
            width=actual_width, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
        )
        self.y -= 0.34 * inch

    def multiline_field(self, label, field_name, height=0.52 * inch):
        c = self.c
        if label:
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 10)
            c.drawString(Layout.MARGIN, self.y, label)
            self.y -= 0.2 * inch
        c.acroForm.textfield(
            name=field_name, x=Layout.MARGIN, y=self.y - height,
            width=Layout.CONTENT_WIDTH, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=9, borderWidth=1, maxlen=0,
            fieldFlags="multiline",
        )
        self.y -= height + 0.1 * inch

    def checkbox(self, label, field_name, indent=0):
        c = self.c
        c.acroForm.checkbox(
            name=field_name,
            x=Layout.MARGIN + indent,
            y=self.y - 0.02 * inch,
            size=12,
            borderColor=Colors.MEDIUM_BLUE,
            fillColor=Colors.WHITE,
        )
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 9)
        c.drawString(Layout.MARGIN + indent + 0.27 * inch, self.y, label)
        self.y -= 0.24 * inch


def build_pdf(output_path):
    pdf = ClassworkPDF(output_path)

    # Page 1
    pdf.new_page()
    pdf.text_field("Name:", "student_name", label_width=0.75 * inch,
                   field_width=3.0 * inch)
    pdf.text_field("Date:", "date", label_width=0.75 * inch,
                   field_width=2.0 * inch)
    pdf.info_box(
        "Today's Mission",
        "You will use an AI app-builder like Gemini Canvas, but you are the supervisor. "
        "Before prompting, define the goal, safety rules, and tests. Then make small "
        "changes, observe what happened, and refine.",
        Colors.LIGHT_TEAL,
        height=0.86 * inch,
    )
    pdf.section_header("Part A - Choose Your Starting App (10 points)", Colors.TEAL)
    pdf.checkbox("I am using my May 30 app/game.", "start_may30")
    pdf.checkbox("I am building a fresh Gemini Canvas app.", "start_fresh")
    pdf.checkbox("I am using the teacher starter quiz prompt.", "start_teacher")
    pdf.multiline_field("What app or game are you improving today?",
                        "starting_app", height=0.45 * inch)

    pdf.section_header("Part B - Agent Job Brief (30 points)", Colors.PURPLE)
    pdf.multiline_field("Goal: What should the AI help you accomplish?",
                        "brief_goal", height=0.45 * inch)
    pdf.multiline_field("Success Criteria: How will you know it worked?",
                        "brief_success", height=0.58 * inch)
    pdf.multiline_field("Allowed Tools: What can the AI use?",
                        "brief_allowed", height=0.42 * inch)
    pdf.multiline_field("Not Allowed: What should the AI never do?",
                        "brief_not_allowed", height=0.42 * inch)
    pdf.multiline_field("Approval Required: What must the AI ask before doing?",
                        "brief_approval", height=0.42 * inch)

    # Page 2
    pdf.new_page()
    pdf.section_header("Part C - Ask for a Plan First (15 points)", Colors.MEDIUM_BLUE)
    pdf.info_box(
        "Prompt Tip",
        "A supervised agent should plan before it changes things. Ask for a short plan, "
        "read it, and approve or revise it.",
        Colors.SKY_BLUE,
        height=0.68 * inch,
    )
    pdf.multiline_field("Write your plan-first prompt:",
                        "plan_prompt", height=0.58 * inch)
    pdf.multiline_field("What plan did the AI suggest?",
                        "plan_result", height=0.65 * inch)
    pdf.multiline_field("Did you approve the plan or change it? Why?",
                        "plan_approval", height=0.48 * inch)

    pdf.section_header("Part D - Two Small Improvements (25 points)", Colors.GREEN)
    pdf.multiline_field("Improvement 1 prompt:",
                        "improvement_1_prompt", height=0.48 * inch)
    pdf.multiline_field("What changed after improvement 1?",
                        "improvement_1_result", height=0.42 * inch)
    pdf.multiline_field("Improvement 2 prompt:",
                        "improvement_2_prompt", height=0.48 * inch)
    pdf.multiline_field("What changed after improvement 2?",
                        "improvement_2_result", height=0.42 * inch)
    pdf.info_box(
        "Good Supervisor Move",
        "Use prompts like: Make only one change. Keep the existing score working. "
        "Do not replace the whole app. Explain what you changed.",
        Colors.LIGHT_GREEN,
        height=0.72 * inch,
    )

    # Page 3
    pdf.new_page()
    pdf.section_header("Part E - Bug Fix Mission (15 points)", Colors.ORANGE)
    pdf.multiline_field("What bug or confusing behavior did you notice?",
                        "bug_description", height=0.45 * inch)
    pdf.multiline_field("Bug-fix prompt:",
                        "bug_prompt", height=0.58 * inch)
    pdf.multiline_field("What happened after the AI tried to fix it?",
                        "bug_result", height=0.45 * inch)

    pdf.section_header("Part F - Test Checklist (15 points)", Colors.AMBER)
    pdf.wrapped_text("Check each test you actually performed. Add one custom test of your own.")
    pdf.checkbox("I opened Preview and used the app like a student would.", "test_preview")
    pdf.checkbox("I clicked every button or answer choice.", "test_clicks")
    pdf.checkbox("I checked whether the score or result changed correctly.", "test_score")
    pdf.checkbox("I tested the restart/reset behavior.", "test_restart")
    pdf.checkbox("I checked that the text is readable.", "test_readable")
    pdf.multiline_field("My custom test:",
                        "test_custom", height=0.34 * inch)
    pdf.multiline_field("What did your tests prove? What still needs work?",
                        "test_notes", height=0.72 * inch)

    # Page 4
    pdf.new_page()
    pdf.section_header("Part G - Future Agent Tools Reflection (15 points)", Colors.RED)
    pdf.info_box(
        "Important",
        "Tool-using agents can connect AI to real tools such as files, browser "
        "control, commands, messages, and skills. More power means more safety rules.",
        Colors.LIGHT_RED,
        height=0.78 * inch,
    )
    pdf.multiline_field("If a future agent worked on your app, what tools would it need?",
                        "future_agent_tools", height=0.5 * inch)
    pdf.multiline_field("What should require your approval before the agent does it?",
                        "future_agent_approval", height=0.5 * inch)
    pdf.multiline_field("What should the agent never do in a class project?",
                        "future_agent_never", height=0.48 * inch)

    pdf.section_header("Part H - Share and Reflect (10 points)", Colors.MEDIUM_BLUE)
    pdf.multiline_field("What are you most proud of from today's build?",
                        "proud", height=0.42 * inch)
    pdf.multiline_field("What did testing help you catch or confirm?",
                        "testing_reflection", height=0.42 * inch)
    pdf.multiline_field("In one sentence, explain supervised agentic AI.",
                        "one_sentence", height=0.38 * inch)

    pdf.section_header("Bonus - Better Supervisor Prompt (+10 points)", Colors.PURPLE)
    pdf.multiline_field("Write one excellent prompt that includes goal, limits, and testing:",
                        "bonus_prompt", height=0.58 * inch)

    pdf.finish()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(
        parent_dir,
        "2026-06-06_Classwork_Agentic_AI_Mission_Control.pdf",
    )
    build_pdf(output_path)
    print(f"[SUCCESS] Classwork PDF created: {output_path}")


if __name__ == "__main__":
    main()
