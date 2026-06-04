"""
Homework PDF Generator - June 6, 2026
Agent-Ready Workflow

Students design a safe agent workflow without installing a new platform.

Usage:
    py create_homework_pdf.py

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


class HomeworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Homework: Agent-Ready Workflow")
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
        c.setFont("Helvetica-Bold", 16)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.52 * inch,
                     "HOMEWORK: Agent-Ready Workflow")
        c.setFont("Helvetica", 9)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.78 * inch,
                     "Design a safe agent workflow - no install required")
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
                     "Due: Next class  |  Total Points: 100 (+5 bonus)")

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

    def wrapped_text(self, content, size=9, indent=0):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", size)
        for line in self._wrap_lines(content, size=size,
                                     max_width=Layout.CONTENT_WIDTH - indent):
            c.drawString(Layout.MARGIN + indent, self.y, line)
            self.y -= 0.14 * inch

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
    pdf = HomeworkPDF(output_path)

    # Page 1
    pdf.new_page()
    pdf.text_field("Name:", "student_name", label_width=0.75 * inch,
                   field_width=3.0 * inch)
    pdf.text_field("Date:", "date", label_width=0.75 * inch,
                   field_width=2.0 * inch)
    pdf.info_box(
        "No Install Required",
        "You are designing an agent-ready workflow, not installing a new platform. "
        "The goal is to show that you know how to give an agent safe instructions, "
        "tool limits, approval rules, and tests.",
        Colors.LIGHT_TEAL,
        height=0.84 * inch,
    )

    pdf.section_header("Part 1 - Pick a Safe Agent Task (15 points)", Colors.TEAL)
    pdf.wrapped_text("Choose a task that is useful but safe for a beginner agent.")
    pdf.checkbox("Study helper or flashcard maker", "task_study")
    pdf.checkbox("App/game tester", "task_tester")
    pdf.checkbox("Research organizer", "task_research")
    pdf.checkbox("Schedule or checklist helper", "task_schedule")
    pdf.checkbox("Other safe task", "task_other")
    pdf.multiline_field("Describe your chosen task in one or two sentences:",
                        "task_description", height=0.48 * inch)

    pdf.section_header("Part 2 - Goal and Success Criteria (25 points)", Colors.PURPLE)
    pdf.multiline_field("Goal: What should the agent accomplish?",
                        "goal", height=0.48 * inch)
    pdf.multiline_field("Success Criteria: List 3-5 ways to know the task worked.",
                        "success_criteria", height=0.82 * inch)

    # Page 2
    pdf.new_page()
    pdf.section_header("Part 3 - Tools and Permissions (25 points)", Colors.MEDIUM_BLUE)
    pdf.info_box(
        "Think Like a Supervisor",
        "A tool is something the agent can use to take action. Pick only the tools "
        "your task truly needs. Extra tools create extra risk.",
        Colors.SKY_BLUE,
        height=0.72 * inch,
    )
    pdf.text("Which tools should your agent be allowed to use?", bold=True)
    pdf.checkbox("Web search", "tool_web")
    pdf.checkbox("Browser or app preview", "tool_browser")
    pdf.checkbox("Read files", "tool_read_files")
    pdf.checkbox("Write or edit files", "tool_write_files")
    pdf.checkbox("Run code or commands", "tool_commands")
    pdf.checkbox("Send messages or emails", "tool_messages")
    pdf.checkbox("Use memory from previous sessions", "tool_memory")
    pdf.multiline_field("Explain why each selected tool is needed:",
                        "tool_reasoning", height=0.72 * inch)

    pdf.section_header("Part 4 - Not Allowed (15 points)", Colors.RED)
    pdf.multiline_field("What should your agent never do?",
                        "not_allowed", height=0.68 * inch)
    pdf.wrapped_text("Examples: delete files, share personal info, spend money, message people, change settings.")

    # Page 3
    pdf.new_page()
    pdf.section_header("Part 5 - Human Approval Rules (20 points)", Colors.ORANGE)
    pdf.wrapped_text("List actions that must stop and ask you before continuing.")
    pdf.checkbox("Before deleting or replacing files", "approve_delete")
    pdf.checkbox("Before sending a message or email", "approve_send")
    pdf.checkbox("Before running a command", "approve_command")
    pdf.checkbox("Before using personal information", "approve_personal")
    pdf.checkbox("Before changing the whole project idea", "approve_big_change")
    pdf.multiline_field("Write your approval rule in your own words:",
                        "approval_rule", height=0.58 * inch)

    pdf.section_header("Part 6 - Test Plan (15 points)", Colors.GREEN)
    pdf.multiline_field("How will you test whether the agent succeeded?",
                        "test_plan", height=0.72 * inch)
    pdf.multiline_field("What would count as failure?",
                        "failure_definition", height=0.45 * inch)
    pdf.multiline_field("If it fails, what should the agent do next?",
                        "failure_recovery", height=0.45 * inch)

    # Page 4
    pdf.new_page()
    pdf.section_header("Part 7 - Example Prompt (10 points)", Colors.AMBER)
    pdf.info_box(
        "Prompt Recipe",
        "Write a prompt that includes the goal, success criteria, allowed tools, "
        "not allowed actions, approval rules, and test plan.",
        Colors.LIGHT_AMBER,
        height=0.7 * inch,
    )
    pdf.multiline_field("Write the exact prompt you would give your agent:",
                        "agent_prompt", height=1.0 * inch)

    pdf.section_header("Part 8 - Reflection (10 points)", Colors.MEDIUM_BLUE)
    pdf.multiline_field("Why is human supervision important for agentic AI?",
                        "supervision_reflection", height=0.5 * inch)
    pdf.multiline_field("What is one agent safety rule you understand better now?",
                        "agent_safety", height=0.5 * inch)

    pdf.section_header("Bonus - Safer Workflow Upgrade (+5 points)", Colors.PURPLE)
    pdf.multiline_field("Add one extra guardrail that would make your agent safer:",
                        "bonus_guardrail", height=0.5 * inch)

    pdf.finish()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(
        parent_dir,
        "2026-06-06_Homework_Agent_Ready_Workflow.pdf",
    )
    build_pdf(output_path)
    print(f"[SUCCESS] Homework PDF created: {output_path}")


if __name__ == "__main__":
    main()
