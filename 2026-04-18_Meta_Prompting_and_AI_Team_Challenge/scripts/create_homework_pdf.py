"""
Homework PDF Generator - April 18, 2026
Meta Prompting & AI Team Challenge

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
    LIGHT_PURPLE = HexColor('#E1BEE7')
    RED = HexColor('#F44336')
    LIGHT_RED = HexColor('#FFCDD2')
    LIGHT_GRAY = HexColor('#F5F5F5')
    DARK_GRAY = HexColor('#424242')
    WHITE = HexColor('#FFFFFF')
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


# =============================================================================
# PDF BUILDER
# =============================================================================

class HomeworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Homework: Meta Prompting & AI Explorer")
        self.page_num = 0
        self.total_pages = 5
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
                    "HOMEWORK: Meta Prompting & AI Explorer")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Practice meta prompting and explore AI tools on your own!")
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

    # -------------------------------------------------------------------------
    # Build
    # -------------------------------------------------------------------------

    def build(self):
        # === PAGE 1: Student Info + Matching (15 points) ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.section_header("SECTION 1: Vocabulary Review -- Matching (15 points)", Colors.AI_PURPLE)

        self.text("Match each term with its definition. Write the letter in the box.", bold=True)
        self.space(0.08 * inch)

        self.text("A. Using AI to help you write better prompts", size=9)
        self.text("B. When AI confidently presents false information as fact", size=9)
        self.text("C. A framework for writing good prompts: Role, Task, Context, Format", size=9)
        self.text("D. Asking AI to explain its thinking step by step", size=9)
        self.text("E. A prompting technique where you provide examples first", size=9)
        self.text("F. Improving a prompt multiple times to get better results", size=9)
        self.text("G. The smallest unit of text that AI processes", size=9)

        self.space(0.1 * inch)

        self.text_field("1. Meta Prompting:", "match_1", 2.2 * inch, 0.5 * inch)
        self.text_field("2. Hallucination:", "match_2", 2.2 * inch, 0.5 * inch)
        self.text_field("3. RTCF Framework:", "match_3", 2.2 * inch, 0.5 * inch)
        self.text_field("4. Chain-of-Thought:", "match_4", 2.2 * inch, 0.5 * inch)
        self.text_field("5. Few-Shot Prompting:", "match_5", 2.2 * inch, 0.5 * inch)
        self.text_field("6. Iteration:", "match_6", 2.2 * inch, 0.5 * inch)
        self.text_field("7. Token:", "match_7", 2.2 * inch, 0.5 * inch)

        self._draw_footer()

        # === PAGE 2: Short Answer (25 points) ===
        self.new_page()

        self.section_header("SECTION 2: Short Answer (25 points)", Colors.PROMPT_GREEN)

        self.text("Answer each question in 1-3 sentences.", bold=True)
        self.space(0.05 * inch)

        self.text("Q1: What is meta prompting? Explain it in your own words and give one example.", bold=True)
        self.multiline_field("", "sa_q1", 0.6 * inch)

        self.text("Q2: Name the 3 meta prompting techniques we learned. Which one do you think", bold=True)
        self.text("is the most useful and why?", bold=True, indent=0.35 * inch)
        self.multiline_field("", "sa_q2", 0.6 * inch)

        self.text("Q3: Why is it important to iterate on your prompts instead of just using", bold=True)
        self.text("the first one you write?", bold=True, indent=0.35 * inch)
        self.multiline_field("", "sa_q3", 0.6 * inch)

        self.text("Q4: What are two things you should always check after getting a response from AI?", bold=True)
        self.multiline_field("", "sa_q4", 0.6 * inch)

        self.text("Q5: Name the 3 free AI tools we learned about and their websites.", bold=True)
        self.multiline_field("", "sa_q5", 0.6 * inch)

        self._draw_footer()

        # === PAGE 3: Solo AI Challenge (30 points) ===
        self.new_page()

        self.section_header("SECTION 3: Solo AI Challenge (30 points)", Colors.META_GOLD)

        self.info_box(
            "Try It Yourself!",
            "Use an AI tool (ChatGPT at chat.openai.com, Gemini at gemini.google.com, "
            "or Grok at grok.com) to complete this challenge. Use meta prompting!",
            Colors.LIGHT_GREEN, 0.6 * inch
        )

        self.space(0.1 * inch)

        self.text("Task: Use AI to help you with something REAL -- a school subject, a hobby,", bold=True)
        self.text("or a skill you want to learn. Use meta prompting to get the best result.", bold=True)
        self.space(0.08 * inch)

        self.text_field("AI tool you used:", "challenge_tool", 1.5 * inch)
        self.text_field("Topic/subject:", "challenge_topic", 1.3 * inch)

        self.space(0.05 * inch)

        self.text("Step 1: Your first (rough) prompt:", bold=True)
        self.multiline_field("", "challenge_prompt1", height=0.45 * inch)

        self.text("Step 2: Your meta prompt (ask AI to improve your prompt):", bold=True)
        self.multiline_field("", "challenge_meta", height=0.45 * inch)

        self.text("Step 3: The improved prompt AI gave you:", bold=True)
        self.multiline_field("", "challenge_prompt2", height=0.45 * inch)

        self.text("Step 4: How was the final response? Was it better than your first attempt?", bold=True)
        self.multiline_field("", "challenge_result", height=0.5 * inch)

        self._draw_footer()

        # === PAGE 4: Compare AI Tools (20 points) ===
        self.new_page()

        self.section_header("SECTION 4: Compare AI Tools (20 points)", Colors.TEAM_CYAN)

        self.info_box(
            "AI Showdown at Home!",
            "Pick one prompt and try it on TWO different AI tools. Compare the results. "
            "Use the same exact prompt on both tools so it's a fair comparison.",
            Colors.SKY_BLUE, 0.6 * inch
        )

        self.space(0.1 * inch)

        self.multiline_field("The prompt you used (same for both tools):", "compare_prompt", height=0.5 * inch)

        self.space(0.05 * inch)

        self.text("Tool 1:", bold=True)
        self.text_field("Name:", "compare_tool1", 0.55 * inch, 2.5 * inch)
        self.multiline_field("Summary of its response:", "compare_response1", height=0.5 * inch)
        self.text_field("Accuracy (1-5):", "compare_acc1", 1.4 * inch, 0.5 * inch)
        self.text_field("Helpfulness (1-5):", "compare_help1", 1.5 * inch, 0.5 * inch)

        self.space(0.05 * inch)

        self.text("Tool 2:", bold=True)
        self.text_field("Name:", "compare_tool2", 0.55 * inch, 2.5 * inch)
        self.multiline_field("Summary of its response:", "compare_response2", height=0.5 * inch)
        self.text_field("Accuracy (1-5):", "compare_acc2", 1.4 * inch, 0.5 * inch)
        self.text_field("Helpfulness (1-5):", "compare_help2", 1.5 * inch, 0.5 * inch)

        self.space(0.05 * inch)

        self.text_field("Which tool did a better job?", "compare_winner", 2.3 * inch, 2.5 * inch)
        self.multiline_field("Why was it better?", "compare_why", height=0.4 * inch)

        self._draw_footer()

        # === PAGE 5: Reflection + Bonus ===
        self.new_page()

        self.section_header("SECTION 5: Reflection (10 points)", Colors.PURPLE)

        self.text("Q1: What is the most useful thing you learned about meta prompting?", bold=True)
        self.multiline_field("", "reflect_q1", 0.55 * inch)

        self.text("Q2: How has your prompting improved since Week 1? Give a specific example.", bold=True)
        self.multiline_field("", "reflect_q2", 0.55 * inch)

        self.text("Q3: Rate your confidence with AI prompting (1-5):", bold=True)
        self.text_field("Rating:", "confidence", 0.7 * inch, 0.5 * inch)
        self.multiline_field("Explain your rating:", "confidence_explain", height=0.45 * inch)

        self.space(0.15 * inch)

        self.section_header("BONUS: Teach a Meta Prompting Trick (+5 points)", Colors.ORANGE)

        self.text("Teach a family member or friend about meta prompting.", bold=True)
        self.text("Show them how to ask AI to improve a prompt!", size=9)
        self.space(0.08 * inch)

        self.text_field("Who did you teach?", "bonus_who", 1.5 * inch, 2.5 * inch)
        self.multiline_field("What did you show them?", "bonus_what", height=0.4 * inch)
        self.text_field("Their reaction?", "bonus_reaction", 1.1 * inch)

        self._draw_footer()

        self.c.save()
        print(f"[SUCCESS] Homework PDF created: {self.output_path}")
        return self.output_path


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-04-18_Homework_AI_Explorer.pdf")
    pdf = HomeworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
