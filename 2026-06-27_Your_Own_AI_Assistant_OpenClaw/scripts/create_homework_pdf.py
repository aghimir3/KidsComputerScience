"""
Homework PDF Generator - June 27, 2026
Your Own AI Assistant (OpenClaw) - LAST DAY of the AI unit

Usage:
    python create_homework_pdf.py

Dependencies:
    pip install reportlab
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth


# =============================================================================
# DESIGN SYSTEM
# =============================================================================

class Colors:
    DARK_BLUE = HexColor('#1E3A5F')
    MEDIUM_BLUE = HexColor('#3467A6')
    LIGHT_BLUE = HexColor('#64B5ED')
    SKY_BLUE = HexColor('#ADD8E6')
    ORANGE = HexColor('#FF9933')
    GREEN = HexColor('#4CAF50')
    LIGHT_GREEN = HexColor('#C8E6C9')
    PURPLE = HexColor('#9C27B0')
    LIGHT_GRAY = HexColor('#F5F5F5')
    DARK_GRAY = HexColor('#424242')
    WHITE = HexColor('#FFFFFF')
    TEAL = HexColor('#00897B')
    SAFE_GREEN = HexColor('#388E3C')


class Layout:
    WIDTH, HEIGHT = letter
    MARGIN = 0.5 * inch
    CONTENT_WIDTH = WIDTH - (2 * MARGIN)
    HEADER_HEIGHT = 1.0 * inch
    FOOTER_HEIGHT = 0.65 * inch
    CONTENT_TOP = HEIGHT - HEADER_HEIGHT - 0.3 * inch


# =============================================================================
# PDF BUILDER
# =============================================================================

class HomeworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Homework: Your Own AI Assistant (OpenClaw)")
        self.page_num = 0
        self.total_pages = 2
        self.y = Layout.CONTENT_TOP

    def new_page(self):
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1
        self._draw_header()
        self._draw_footer()
        self.y = Layout.CONTENT_TOP

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
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                     "HOMEWORK: Your Own AI Assistant")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                     "OpenClaw + OpenRouter  \u00b7  No computer needed!")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.WHITE)
        c.drawRightString(Layout.WIDTH - Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                          f"Page {self.page_num} of {self.total_pages}")

    def _draw_footer(self):
        c = self.c
        c.setFillColor(Colors.DARK_BLUE)
        c.rect(0, 0, Layout.WIDTH, Layout.FOOTER_HEIGHT, fill=True, stroke=False)
        c.setFillColor(Colors.ORANGE)
        c.rect(0, Layout.FOOTER_HEIGHT, Layout.WIDTH, 3, fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(Layout.MARGIN, 0.4 * inch, "SUBMISSION:")
        c.setFont("Helvetica", 9)
        c.drawString(1.4 * inch, 0.4 * inch,
                     "1. Microsoft Teams   2. Copy to Ishwari Raut ma'am")
        c.drawString(Layout.MARGIN, 0.2 * inch,
                     "Due: Next class  |  Total Points: 100 (+5 bonus)")

    # ----- helpers -----
    def section_header(self, title, color=None):
        if color is None:
            color = Colors.MEDIUM_BLUE
        c = self.c
        c.setFillColor(color)
        c.roundRect(Layout.MARGIN, self.y - 0.28 * inch,
                    Layout.CONTENT_WIDTH, 0.38 * inch, 5, fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(Layout.MARGIN + 0.15 * inch, self.y - 0.16 * inch, title)
        self.y -= 0.55 * inch

    def info_box(self, title, content, color=None, height=0.7 * inch):
        if color is None:
            color = Colors.SKY_BLUE
        c = self.c
        c.setFillColor(color)
        c.setStrokeColor(Colors.MEDIUM_BLUE)
        c.roundRect(Layout.MARGIN, self.y - height,
                    Layout.CONTENT_WIDTH, height, 8, fill=True, stroke=True)
        c.setFillColor(Colors.DARK_BLUE)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(Layout.MARGIN + 0.15 * inch, self.y - 0.2 * inch, title)
        c.setFont("Helvetica", 9)
        c.setFillColor(Colors.DARK_GRAY)
        words = content.split()
        lines, current = [], ""
        max_width = Layout.CONTENT_WIDTH - 0.4 * inch
        for word in words:
            test = current + " " + word if current else word
            if stringWidth(test, "Helvetica", 9) < max_width:
                current = test
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        text_y = self.y - 0.38 * inch
        for line in lines[:4]:
            c.drawString(Layout.MARGIN + 0.15 * inch, text_y, line)
            text_y -= 0.16 * inch
        self.y -= height + 0.1 * inch

    def text(self, content, bold=False, size=10, indent=0):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        c.drawString(Layout.MARGIN + indent, self.y, content)
        self.y -= (size + 6)

    def text_field(self, label, field_name, label_width=1.3 * inch,
                   field_width=None, height=0.25 * inch):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN, self.y, label)
        field_x = Layout.MARGIN + label_width
        actual_width = (Layout.WIDTH - Layout.MARGIN - field_x) if field_width is None else field_width
        c.acroForm.textfield(
            name=field_name, x=field_x, y=self.y - 4,
            width=actual_width, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
        )
        self.y -= 0.38 * inch

    def small_field(self, label, field_name, label_width=2.9 * inch):
        """Label with a short fill-in box on the same line (for matching / T-F)."""
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN + 0.1 * inch, self.y, label)
        c.acroForm.textfield(
            name=field_name, x=Layout.MARGIN + label_width, y=self.y - 4,
            width=0.5 * inch, height=0.22 * inch,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
        )
        self.y -= 0.3 * inch

    def multiline_field(self, label, field_name, height=0.5 * inch):
        c = self.c
        if label:
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 10)
            c.drawString(Layout.MARGIN, self.y, label)
            self.y -= 0.18 * inch
        c.acroForm.textfield(
            name=field_name, x=Layout.MARGIN, y=self.y - height + 0.08 * inch,
            width=Layout.CONTENT_WIDTH, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
            fieldFlags='multiline',
        )
        self.y -= height + 0.08 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # ----- build -----
    def build(self):
        # === PAGE 1: Matching + True/False ===
        self.new_page()
        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.info_box(
            "Last Day of the AI Unit!",
            "No computer needed. Show what you remember about your AI assistant, OpenClaw. Finish with a quick design challenge and a look back at everything you learned.",
            Colors.LIGHT_BLUE, 0.7 * inch
        )

        self.section_header("Part 1 - Matching (30 points)", Colors.SAFE_GREEN)
        self.text("Write the letter of the correct definition next to each term.", bold=True)
        self.space(0.05 * inch)
        self.text("A. The always-on \"brain\" that keeps your assistant running.", size=9)
        self.text("B. A service that gives you one key to reach many AI models.", size=9)
        self.text("C. A secret code, like a password, that lets you use a model.", size=9)
        self.text("D. When the assistant asks permission before it does an action.", size=9)
        self.text("E. A timer that lets the assistant act on its own.", size=9)
        self.text("F. An AI that can take real actions, not just chat.", size=9)
        self.space(0.08 * inch)
        self.small_field("AI assistant", "match_assistant")
        self.small_field("Gateway", "match_gateway")
        self.small_field("OpenRouter", "match_openrouter")
        self.small_field("API key", "match_apikey")
        self.small_field("Execution approval ('ask' mode)", "match_approval")
        self.small_field("Heartbeat", "match_heartbeat")

        self.space(0.05 * inch)
        self.section_header("Part 2 - True or False (25 points)", Colors.TEAL)
        self.text("Write T (true) or F (false) in each box.", bold=True)
        self.space(0.05 * inch)
        self.small_field("OpenClaw runs on your own computer.", "tf_local", 4.4 * inch)
        self.small_field("You should share your API key so friends can use it.", "tf_share", 4.4 * inch)
        self.small_field("In 'ask' mode, the assistant runs commands without asking.", "tf_ask", 4.4 * inch)
        self.small_field("The gateway is the always-on brain of the assistant.", "tf_gateway", 4.4 * inch)
        self.small_field("An assistant can remember you across restarts with memory files.", "tf_memory", 4.4 * inch)

        # === PAGE 2: Short answer + Design + Bonus ===
        self.new_page()
        self.section_header("Part 3 - Short Answer (30 points)", Colors.MEDIUM_BLUE)
        self.text("1. How is an AI assistant different from a simple chatbot?", bold=True)
        self.multiline_field("", "sa_assistant", 0.55 * inch)
        self.text("2. Why should you keep your API key secret?", bold=True)
        self.multiline_field("", "sa_key", 0.55 * inch)
        self.text("3. Why do we keep the heartbeat OFF and stop the gateway when class ends?", bold=True)
        self.multiline_field("", "sa_safety", 0.55 * inch)

        self.section_header("Part 4 - Design Your Own Assistant (15 points)", Colors.PURPLE)
        self.text("Invent an AI assistant and plan it out below.", bold=True)
        self.text_field("Assistant's name:", "design_name", 1.6 * inch)
        self.text_field("What job does it help with?", "design_job", 2.4 * inch)
        self.multiline_field("When should it STOP and ask your permission first?",
                             "design_approval", 0.5 * inch)

        self.section_header("BONUS - Looking Back (+5 points)", Colors.ORANGE)
        self.info_box(
            "You finished the AI unit!",
            "Look back at everything from this unit -- agents, the loop, tools, MCP, skills, memory, building your own tools, and running a real assistant.",
            Colors.LIGHT_GREEN, 0.6 * inch
        )
        self.text("Write 3 things you learned in the AI unit:", bold=True)
        self.text_field("1.", "bonus_1", 0.35 * inch)
        self.text_field("2.", "bonus_2", 0.35 * inch)
        self.text_field("3.", "bonus_3", 0.35 * inch)

        self.c.save()
        print(f"[SUCCESS] Homework PDF created: {self.output_path}")
        return self.output_path


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-06-27_Homework_Your_AI_Assistant.pdf")
    pdf = HomeworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
