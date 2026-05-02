"""
Classwork PDF Generator - April 18, 2026
Meta Prompting & AI Team Challenge (Group Worksheet)

Usage:
    python create_classwork_pdf.py

Dependencies:
    pip install reportlab
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
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
    LIGHT_RED = HexColor('#FFCDD2')
    LIGHT_GRAY = HexColor('#F5F5F5')
    DARK_GRAY = HexColor('#424242')
    WHITE = HexColor('#FFFFFF')
    # Theme-specific
    AI_PURPLE = HexColor('#673AB7')
    PROMPT_GREEN = HexColor('#388E3C')
    DEEP_PURPLE = HexColor('#4A148C')
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
    CONTENT_BOTTOM = FOOTER_HEIGHT + 0.3 * inch


class ClassworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Classwork: Meta Prompting & AI Team Challenge")
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
        c.setFillColor(Colors.DARK_BLUE)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT,
               Layout.WIDTH, Layout.HEADER_HEIGHT, fill=True, stroke=False)
        c.setFillColor(Colors.ORANGE)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT - 4,
               Layout.WIDTH, 4, fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                    "CLASSWORK: AI Team Challenge")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Meta Prompting & Hands-On Group Projects")
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
                    "Due: End of class  |  Total Points: 100 (+10 bonus)")

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
                   field_width=None, height=0.25 * inch):
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
            name=field_name, x=field_x, y=self.y - 5,
            width=actual_width, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
        )
        self.y -= 0.35 * inch

    def multiline_field(self, label, field_name, height=0.5 * inch):
        c = self.c
        if label:
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 10)
            c.drawString(Layout.MARGIN, self.y, label)
            self.y -= 0.2 * inch
        c.acroForm.textfield(
            name=field_name, x=Layout.MARGIN,
            y=self.y - height,
            width=Layout.CONTENT_WIDTH, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
            fieldFlags='multiline',
        )
        self.y -= height + 0.1 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # =========================================================================
    # BUILD METHOD
    # =========================================================================

    def build(self):
        # =================================================================
        # PAGE 1: Team Info + Challenge Overview
        # =================================================================
        self.new_page()

        self.section_header("TEAM INFORMATION", Colors.TEAM_CYAN)
        self.text_field("Team Name:", "team_name")
        self.text_field("Member 1:", "member_1")
        self.text_field("Member 2:", "member_2")
        self.text_field("Member 3:", "member_3")
        self.text_field("Member 4:", "member_4")
        self.text_field("Date:", "team_date")

        self.info_box(
            "Your Mission Today:",
            "Work as a team to complete AI challenges using meta prompting! "
            "Use AI tools (ChatGPT, Gemini, Grok) to create amazing content, "
            "then present your best work to the class. Document everything -- "
            "your prompts, improvements, and results.",
            color=Colors.LIGHT_GREEN,
            height=0.75 * inch,
        )

        self.section_header("TEAM ROLES -- Study Guide Battle", Colors.AI_PURPLE)

        self.info_box(
            "How to divide roles:",
            "Each person picks ONE role below. If your team has 3 people, one person "
            "does both Fact Checker and Idea Generator. If you have 2 people, split into "
            "Writer + Note Taker and Checker + Ideas. Everyone should suggest prompt improvements!",
            color=Colors.LIGHT_PURPLE,
            height=0.7 * inch,
        )

        roles = [
            ("Prompt Writer:", "Shares screen and types prompts into the AI tool"),
            ("Fact Checker:", "Looks up AI claims online to verify they are true"),
            ("Note Taker:", "Fills out this worksheet -- documents prompts, changes, and results"),
            ("Idea Generator:", "Suggests ways to improve prompts and thinks of creative approaches"),
        ]
        for role_name, role_desc in roles:
            c = self.c
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(Layout.MARGIN, self.y, role_name)
            c.setFont("Helvetica", 9)
            role_width = stringWidth(role_name, "Helvetica-Bold", 9)
            c.drawString(Layout.MARGIN + role_width + 4, self.y, role_desc)
            self.y -= 0.22 * inch

        self.space(0.05 * inch)

        self.text_field("Prompt Writer:", "role_writer", 1.4 * inch, 2.5 * inch)
        self.text_field("Fact Checker:", "role_checker", 1.4 * inch, 2.5 * inch)
        self.text_field("Note Taker:", "role_notetaker", 1.4 * inch, 2.5 * inch)
        self.text_field("Idea Generator:", "role_ideas", 1.4 * inch, 2.5 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 2: Round 1 - Prompt Journal (document 3 iterations)
        # =================================================================
        self.new_page()

        self.section_header("ROUND 1: Study Guide Battle -- Prompt Journal (35 points)", Colors.META_GOLD)

        self.text_field("Topic chosen:", "r1_topic", 1.2 * inch)
        self.text_field("AI tool used:", "r1_tool", 1.2 * inch)

        self.space(0.05 * inch)

        self.text("ITERATION 1: Your first prompt", bold=True)
        self.multiline_field("Prompt you typed:", "r1_prompt_1", height=0.5 * inch)
        self.multiline_field("What was good/bad about the response?", "r1_eval_1", height=0.4 * inch)

        self.space(0.05 * inch)

        self.text("ITERATION 2: Use meta prompting to improve", bold=True)
        self.text("(Ask AI: \"How can I improve this prompt?\" or \"Rewrite this prompt using RTCF\")", size=9)
        self.multiline_field("Your improved prompt:", "r1_prompt_2", height=0.5 * inch)
        self.multiline_field("How did the response improve?", "r1_eval_2", height=0.4 * inch)

        self.space(0.05 * inch)

        self.text("ITERATION 3: Final refinement", bold=True)
        self.multiline_field("Your final prompt:", "r1_prompt_3", height=0.5 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 3: Round 1 - Final Study Guide + Fact Check
        # =================================================================
        self.new_page()

        self.section_header("ROUND 1: Study Guide Results & Fact-Check (25 points)", Colors.PROMPT_GREEN)

        self.text("Paste or summarize the best parts of your AI-generated study guide:", bold=True)
        self.multiline_field("", "r1_study_guide", height=2.0 * inch)

        self.space(0.1 * inch)

        self.section_header("FACT-CHECK LOG", Colors.RED)

        self.text("Claim 1 from AI:", bold=True)
        self.multiline_field("What AI said:", "fc_claim_1", height=0.4 * inch)
        self.text_field("True or False?", "fc_verdict_1", 1.2 * inch, 0.6 * inch)
        self.text_field("How you checked:", "fc_source_1", 1.4 * inch)

        self.space(0.1 * inch)

        self.text("Claim 2 from AI:", bold=True)
        self.multiline_field("What AI said:", "fc_claim_2", height=0.4 * inch)
        self.text_field("True or False?", "fc_verdict_2", 1.2 * inch, 0.6 * inch)
        self.text_field("How you checked:", "fc_source_2", 1.4 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 4: Team Reflection + Bonus
        # =================================================================
        self.new_page()

        self.section_header("TEAM REFLECTION (30 points)", Colors.MEDIUM_BLUE)

        self.text("What meta prompting technique was most useful for your team?", bold=True)
        self.multiline_field("", "reflect_meta", height=0.55 * inch)

        self.text("What was the biggest difference between your first prompt and your last?", bold=True)
        self.multiline_field("", "reflect_improvement", height=0.55 * inch)

        self.text("Did any AI response surprise you? What was it?", bold=True)
        self.multiline_field("", "reflect_surprise", height=0.55 * inch)

        self.text("How did your team work together? What would you do differently?", bold=True)
        self.multiline_field("", "reflect_teamwork", height=0.55 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: Meta Prompting Chain (+10 points)", Colors.ORANGE)

        self.info_box(
            "Challenge:",
            "Create a 3-step meta prompting chain: (1) Ask AI what to ask, (2) Use its suggestion "
            "to write a prompt, (3) Ask AI to improve that prompt. Document all 3 steps below.",
            color=Colors.SKY_BLUE,
            height=0.6 * inch,
        )

        self.multiline_field("Step 1 - What you asked AI:", "bonus_step1", height=0.4 * inch)
        self.multiline_field("Step 2 - The prompt you wrote:", "bonus_step2", height=0.4 * inch)
        self.multiline_field("Step 3 - AI's improved version:", "bonus_step3", height=0.4 * inch)

        self._draw_footer()

        # Save the PDF
        self.c.save()
        print(f"[SUCCESS] Classwork PDF created: {self.output_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-04-18_Classwork_AI_Team_Challenge.pdf")
    pdf = ClassworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
