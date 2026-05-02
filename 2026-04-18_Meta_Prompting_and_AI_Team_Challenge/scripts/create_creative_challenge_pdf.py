"""
Creative Challenge Activity PDF - April 18, 2026
Meta Prompting & AI Team Challenge

Group activity: Use meta prompting to create something creative with AI.

Usage:
    python create_creative_challenge_pdf.py

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


class CreativeChallengePDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Activity: Creative Challenge -- Build Something with AI")
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
        c.setFillColor(Colors.META_GOLD)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT,
               Layout.WIDTH, Layout.HEADER_HEIGHT, fill=True, stroke=False)
        c.setFillColor(Colors.ORANGE)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT - 4,
               Layout.WIDTH, 4, fill=True, stroke=False)
        c.setFillColor(Colors.DARK_BLUE)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                    "ACTIVITY: Creative Challenge")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.DARK_GRAY)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Use meta prompting to create something amazing with AI!")
        c.setFillColor(Colors.DARK_BLUE)
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
                    "Due: End of class  |  Activity 2 of 2")

    def section_header(self, title, color=None):
        if color is None:
            color = Colors.META_GOLD
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

    def checkbox(self, label, field_name, x_offset=0):
        c = self.c
        c.acroForm.checkbox(
            name=field_name, x=Layout.MARGIN + x_offset, y=self.y - 2,
            size=13, borderColor=Colors.MEDIUM_BLUE,
            fillColor=Colors.WHITE, buttonStyle='check',
        )
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN + x_offset + 18, self.y, label)
        self.y -= 0.25 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # =========================================================================
    # BUILD
    # =========================================================================

    def build(self):
        # =================================================================
        # PAGE 1: Team Info + Project Choice + Planning
        # =================================================================
        self.new_page()

        self.section_header("TEAM INFORMATION", Colors.DARK_BLUE)
        self.text_field("Team Name:", "team_name")
        self.text_field("AI tool used:", "tool_used", 1.2 * inch, 3.0 * inch)

        self.info_box(
            "Your Mission:",
            "Use meta prompting and iteration to create something creative with AI. "
            "Pick ONE project type below, then use at least 2 rounds of meta prompting "
            "to make your final result as good as possible. You'll present this to the class!",
            color=Colors.LIGHT_GREEN,
            height=0.75 * inch,
        )

        self.section_header("DIVIDE YOUR ROLES", Colors.TEAL)

        self.info_box(
            "How to divide roles:",
            "Each person picks ONE role. If your team has 3 people, the Prompt Writer "
            "also generates ideas. If you have 2 people, split into Writer + Editor and "
            "Researcher + Note Taker. Swap roles halfway through if you want!",
            color=Colors.LIGHT_PURPLE,
            height=0.7 * inch,
        )

        roles = [
            ("Prompt Writer:", "Shares screen, types and refines prompts"),
            ("Editor:", "Reviews AI output and suggests improvements"),
            ("Researcher:", "Fact-checks AI content and finds reference material"),
            ("Note Taker:", "Fills out this worksheet and documents the process"),
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
        self.text_field("Editor:", "role_editor", 1.4 * inch, 2.5 * inch)
        self.text_field("Researcher:", "role_researcher", 1.4 * inch, 2.5 * inch)
        self.text_field("Note Taker:", "role_notetaker", 1.4 * inch, 2.5 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 2: Project Choice + First Prompt
        # =================================================================
        self.new_page()

        self.section_header("CHOOSE YOUR PROJECT (check one)", Colors.AI_PURPLE)

        self.checkbox("Write a short story or poem", "choice_story")
        self.checkbox("Create a quiz for younger kids", "choice_quiz")
        self.checkbox("Design a lesson plan on any topic", "choice_lesson")
        self.checkbox("Build a \"how-to\" guide for a hobby or skill", "choice_howto")
        self.checkbox("Other (describe below)", "choice_other")

        self.text_field("Project description:", "project_desc", 1.5 * inch)

        self.space(0.1 * inch)

        self.section_header("STEP 1: YOUR FIRST PROMPT", Colors.RED)

        self.text("Write your first attempt at a prompt (before meta prompting):", bold=True)
        self.multiline_field("", "prompt_v1", height=0.6 * inch)

        self.multiline_field("What was the result like? What was good/bad?", "eval_v1", height=0.5 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 2: Meta Prompting + Iteration
        # =================================================================
        self.new_page()

        self.section_header("STEP 2: META PROMPT -- ASK AI TO IMPROVE", Colors.META_GOLD)

        self.text("Ask AI to improve your prompt. Write what you asked:", bold=True)
        self.multiline_field("Your meta prompt:", "meta_prompt", height=0.6 * inch)

        self.multiline_field("The improved prompt AI gave you:", "prompt_v2", height=0.6 * inch)

        self.space(0.1 * inch)

        self.section_header("STEP 3: FINAL ITERATION", Colors.PROMPT_GREEN)

        self.text("Run the improved prompt. Did you make any more changes?", bold=True)
        self.multiline_field("Your final prompt:", "prompt_final", height=0.6 * inch)

        self.multiline_field("How is the final result different from your first attempt?", "eval_final", height=0.6 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 3: Final Product + Reflection
        # =================================================================
        self.new_page()

        self.section_header("YOUR CREATIVE PROJECT -- FINAL RESULT", Colors.AI_PURPLE)

        self.text("Paste or summarize your final creative project below:", bold=True)
        self.multiline_field("", "final_product", height=2.5 * inch)

        self.space(0.1 * inch)

        self.section_header("TEAM REFLECTION", Colors.MEDIUM_BLUE)

        self.text("How many times did you iterate on your prompt?", bold=True)
        self.text_field("Number of iterations:", "num_iterations", 1.7 * inch, 0.5 * inch)

        self.text("What meta prompting technique helped the most?", bold=True)
        self.multiline_field("", "reflect_technique", height=0.5 * inch)

        self.text("What would you do differently next time?", bold=True)
        self.multiline_field("", "reflect_next_time", height=0.5 * inch)

        self.text("Rate your team's final project (1-5):", bold=True)
        self.text_field("Rating:", "self_rating", 0.7 * inch, 0.5 * inch)

        self._draw_footer()

        self.c.save()
        print(f"[SUCCESS] Creative Challenge PDF created: {self.output_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-04-18_Activity_Creative_Challenge.pdf")
    pdf = CreativeChallengePDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
