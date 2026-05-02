"""
AI Showdown Activity PDF - April 18, 2026
Meta Prompting & AI Team Challenge

Group activity: Compare the same prompt across ChatGPT, Gemini, and Grok.

Usage:
    python create_ai_showdown_pdf.py

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
    LIGHT_PURPLE = HexColor('#E1BEE7')
    RED = HexColor('#F44336')
    LIGHT_GRAY = HexColor('#F5F5F5')
    DARK_GRAY = HexColor('#424242')
    WHITE = HexColor('#FFFFFF')
    AI_PURPLE = HexColor('#673AB7')
    PROMPT_GREEN = HexColor('#388E3C')
    TEAL = HexColor('#00897B')
    META_GOLD = HexColor('#FFB300')
    TEAM_CYAN = HexColor('#00ACC1')


class Layout:
    WIDTH, HEIGHT = letter
    MARGIN = 0.5 * inch
    CONTENT_WIDTH = WIDTH - (2 * MARGIN)
    HEADER_HEIGHT = 1.0 * inch
    FOOTER_HEIGHT = 0.65 * inch
    CONTENT_TOP = HEIGHT - HEADER_HEIGHT - 0.3 * inch


class ShowdownPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Activity: AI Showdown -- Compare AI Tools")
        self.page_num = 0
        self.total_pages = 4
        self.y = Layout.CONTENT_TOP

    def new_page(self):
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1
        self._draw_header()
        self.y = Layout.CONTENT_TOP

    def _draw_header(self):
        c = self.c
        c.setFillColor(Colors.TEAM_CYAN)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT,
               Layout.WIDTH, Layout.HEADER_HEIGHT, fill=True, stroke=False)
        c.setFillColor(Colors.ORANGE)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT - 4,
               Layout.WIDTH, 4, fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                    "ACTIVITY: AI Showdown")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Compare the same prompt across ChatGPT, Gemini, and Grok!")
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica", 10)
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
                    "Due: End of class  |  Activity 1 of 2")

    def section_header(self, title, color=None):
        if color is None:
            color = Colors.TEAM_CYAN
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
        c.drawString(Layout.MARGIN + 0.15 * inch, self.y - 0.18 * inch, title)
        c.setFont("Helvetica", 9)
        c.setFillColor(Colors.DARK_GRAY)
        words = content.split()
        lines = []
        current_line = ""
        max_width = Layout.CONTENT_WIDTH - 0.4 * inch
        for word in words:
            test_line = current_line + " " + word if current_line else word
            if stringWidth(test_line, "Helvetica", 9) < max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        text_y = self.y - 0.35 * inch
        box_bottom = self.y - height + 0.05 * inch
        for line in lines[:5]:
            if text_y < box_bottom:
                break
            c.drawString(Layout.MARGIN + 0.15 * inch, text_y, line)
            text_y -= 0.14 * inch
        self.y -= height + 0.12 * inch

    def text(self, content, bold=False, size=10, indent=0):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        font = "Helvetica-Bold" if bold else "Helvetica"
        c.setFont(font, size)
        c.drawString(Layout.MARGIN + indent, self.y, content)
        self.y -= (size + 6)

    def text_field(self, label, field_name, label_width=1.3 * inch,
                   field_width=None, height=0.28 * inch):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN, self.y, label)
        field_x = Layout.MARGIN + label_width
        if field_width is None:
            actual_width = Layout.WIDTH - Layout.MARGIN - field_x
        else:
            actual_width = field_width
        c.acroForm.textfield(
            name=field_name, x=field_x, y=self.y - 6,
            width=actual_width, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
        )
        self.y -= 0.4 * inch

    def multiline_field(self, label, field_name, height=0.5 * inch):
        c = self.c
        if label:
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 10)
            c.drawString(Layout.MARGIN, self.y, label)
            self.y -= 0.22 * inch
        c.acroForm.textfield(
            name=field_name, x=Layout.MARGIN,
            y=self.y - height,
            width=Layout.CONTENT_WIDTH, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
            fieldFlags='multiline',
        )
        self.y -= height + 0.12 * inch

    def _draw_ratings(self, prefix):
        """Draw Accuracy, Detail, Style ratings on a single row."""
        c = self.c
        labels = [
            ("Accuracy (1-5):", f"{prefix}_accuracy"),
            ("Detail (1-5):", f"{prefix}_detail"),
            ("Style (1-5):", f"{prefix}_style"),
        ]
        col_width = Layout.CONTENT_WIDTH / 3
        for i, (label, field_name) in enumerate(labels):
            x = Layout.MARGIN + i * col_width
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 10)
            c.drawString(x, self.y, label)
            label_w = stringWidth(label, "Helvetica", 10) + 6
            c.acroForm.textfield(
                name=field_name, x=x + label_w, y=self.y - 6,
                width=0.6 * inch, height=0.28 * inch,
                borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
                textColor=black, fontSize=10, borderWidth=1, maxlen=0,
            )
        self.y -= 0.4 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # =========================================================================
    # BUILD
    # =========================================================================

    def build(self):
        # =================================================================
        # PAGE 1: Team Info + Instructions + Shared Prompt
        # =================================================================
        self.new_page()

        self.section_header("TEAM INFORMATION", Colors.DARK_BLUE)
        self.text_field("Team Name:", "team_name")
        self.text_field("Date:", "team_date")

        self.info_box(
            "How It Works:",
            "Everyone in your group uses the SAME prompt on a DIFFERENT AI tool. "
            "Compare the results side by side. Rate each tool from 1-5 on accuracy, "
            "detail, and style. Then decide as a group: which AI did the best job?",
            color=Colors.LIGHT_GREEN,
            height=0.75 * inch,
        )

        self.section_header("DIVIDE YOUR ROLES", Colors.AI_PURPLE)

        self.info_box(
            "How to divide roles:",
            "Each person picks a different AI tool to test. One person also writes "
            "down the team's shared prompt. If you have 2 people, skip one tool. "
            "If you have 4, two people can test the same tool and compare notes.",
            color=Colors.LIGHT_PURPLE,
            height=0.7 * inch,
        )

        self.text_field("ChatGPT tester:", "role_chatgpt", 1.5 * inch, 2.5 * inch)
        self.text_field("Gemini tester:", "role_gemini", 1.5 * inch, 2.5 * inch)
        self.text_field("Grok tester:", "role_grok", 1.5 * inch, 2.5 * inch)
        self.text_field("Prompt writer:", "role_prompt_writer", 1.5 * inch, 2.5 * inch)

        self.section_header("THE SHARED PROMPT", Colors.TEAM_CYAN)

        self.multiline_field("Write the prompt your team will use on all 3 tools:", "showdown_prompt", height=0.8 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 2: Tools 1 and 2
        # =================================================================
        self.new_page()

        self.section_header("TOOL 1: ChatGPT (chat.openai.com)", Colors.PROMPT_GREEN)

        self.text_field("Tester name:", "tool1_tester", 1.2 * inch, 3.0 * inch)
        self.multiline_field("Summarize the response:", "tool1_summary", height=0.65 * inch)
        self._draw_ratings("tool1")
        self.multiline_field("What did it do well? What did it miss?", "tool1_notes", height=0.45 * inch)

        self.space(0.15 * inch)

        self.section_header("TOOL 2: Gemini (gemini.google.com)", Colors.MEDIUM_BLUE)

        self.text_field("Tester name:", "tool2_tester", 1.2 * inch, 3.0 * inch)
        self.multiline_field("Summarize the response:", "tool2_summary", height=0.65 * inch)
        self._draw_ratings("tool2")
        self.multiline_field("What did it do well? What did it miss?", "tool2_notes", height=0.45 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 3: Tool 3 + Verdict
        # =================================================================
        self.new_page()

        self.section_header("TOOL 3: Grok (grok.com)", Colors.DARK_GRAY)

        self.text_field("Tester name:", "tool3_tester", 1.2 * inch, 3.0 * inch)
        self.multiline_field("Summarize the response:", "tool3_summary", height=0.65 * inch)
        self._draw_ratings("tool3")
        self.multiline_field("What did it do well? What did it miss?", "tool3_notes", height=0.45 * inch)

        self.space(0.15 * inch)

        self.section_header("THE VERDICT", Colors.META_GOLD)

        self.text_field("Which tool gave the BEST response?", "winner", 2.8 * inch)
        self.multiline_field("Why was it the best? What made it stand out?", "winner_why", height=0.55 * inch)

        self.space(0.1 * inch)

        self.text_field("Which tool gave the WORST response?", "worst", 2.8 * inch)
        self.multiline_field("What was wrong with it?", "worst_why", height=0.55 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 4: Reflection
        # =================================================================
        self.new_page()

        self.section_header("TEAM REFLECTION", Colors.MEDIUM_BLUE)

        self.text("Were you surprised by any of the results? What surprised you?", bold=True)
        self.space(0.05 * inch)
        self.multiline_field("", "reflect_surprise", height=0.7 * inch)

        self.text("Did all 3 tools give the same information, or were there differences?", bold=True)
        self.space(0.05 * inch)
        self.multiline_field("", "reflect_differences", height=0.7 * inch)

        self.text("Would you change the prompt to get better results? How?", bold=True)
        self.space(0.05 * inch)
        self.multiline_field("", "reflect_improve", height=0.7 * inch)

        self._draw_footer()

        self.c.save()
        print(f"[SUCCESS] AI Showdown PDF created: {self.output_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-04-18_Activity_AI_Showdown.pdf")
    pdf = ShowdownPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
