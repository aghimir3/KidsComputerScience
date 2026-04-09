"""
Homework PDF Generator - April 11, 2026
Prompt Engineering & Using AI Tools

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
        self.c.setTitle("Homework: Prompt Engineering & Using AI Tools")
        self.page_num = 0
        self.total_pages = 5
        self.y = Layout.CONTENT_TOP

    # -------------------------------------------------------------------------
    # Core Drawing
    # -------------------------------------------------------------------------

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
                    "HOMEWORK: Prompt Engineering & AI Tools")

        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Practice what you learned and explore AI on your own!")

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

    # -------------------------------------------------------------------------
    # Section Helpers
    # -------------------------------------------------------------------------

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

        text_y = self.y - 0.38 * inch
        for line in lines[:4]:
            c.drawString(Layout.MARGIN + 0.15 * inch, text_y, line)
            text_y -= 0.16 * inch

        self.y -= height + 0.1 * inch

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
            name=field_name,
            x=field_x,
            y=self.y - 4,
            width=actual_width,
            height=height,
            borderColor=Colors.MEDIUM_BLUE,
            fillColor=Colors.LIGHT_GRAY,
            textColor=black,
            fontSize=10,
            borderWidth=1,
            maxlen=0,
        )

        self.y -= 0.38 * inch

    def multiline_field(self, label, field_name, height=0.5 * inch):
        c = self.c

        if label:
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 10)
            c.drawString(Layout.MARGIN, self.y, label)
            self.y -= 0.18 * inch

        c.acroForm.textfield(
            name=field_name,
            x=Layout.MARGIN,
            y=self.y - height + 0.08 * inch,
            width=Layout.CONTENT_WIDTH,
            height=height,
            borderColor=Colors.MEDIUM_BLUE,
            fillColor=Colors.LIGHT_GRAY,
            textColor=black,
            fontSize=10,
            borderWidth=1,
            maxlen=0,
            fieldFlags='multiline',
        )

        self.y -= height + 0.08 * inch

    def checkbox(self, label, field_name, x_offset=0):
        c = self.c

        c.acroForm.checkbox(
            name=field_name,
            x=Layout.MARGIN + x_offset,
            y=self.y - 2,
            size=13,
            borderColor=Colors.MEDIUM_BLUE,
            fillColor=Colors.WHITE,
            buttonStyle='check',
        )

        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN + x_offset + 18, self.y, label)

        self.y -= 0.23 * inch

    def multiple_choice(self, question, options, field_name, q_num=None):
        c = self.c

        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica-Bold", 10)
        q_text = f"Q{q_num}: {question}" if q_num else question
        c.drawString(Layout.MARGIN, self.y, q_text)
        self.y -= 0.22 * inch

        for i, option in enumerate(options):
            letter_char = chr(65 + i)

            c.acroForm.checkbox(
                name=f"{field_name}_{letter_char}",
                x=Layout.MARGIN + 0.2 * inch,
                y=self.y - 2,
                size=11,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.WHITE,
            )

            c.setFont("Helvetica", 10)
            c.setFillColor(Colors.DARK_GRAY)
            c.drawString(Layout.MARGIN + 0.2 * inch + 15, self.y, f"{letter_char}) {option}")
            self.y -= 0.2 * inch

        self.y -= 0.08 * inch

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

        self.section_header("SECTION 1: Matching (15 points)", Colors.AI_PURPLE)

        self.text("Match each term with its definition. Write the letter in the box.", bold=True)
        self.space(0.08 * inch)

        # Definitions
        self.text("A. The text instruction you give to an AI to get a response", size=9)
        self.text("B. When AI confidently presents false information as fact", size=9)
        self.text("C. A prompting technique where you provide examples first", size=9)
        self.text("D. Asking AI to explain its thinking step by step", size=9)
        self.text("E. The framework: Role, Task, Context, Format", size=9)
        self.text("F. The smallest unit of text that AI processes", size=9)
        self.text("G. AI reflecting unfair patterns from its training data", size=9)

        self.space(0.1 * inch)

        # Match terms
        self.text_field("1. Prompt:", "match_1", 2.2 * inch, 0.5 * inch)
        self.text_field("2. Hallucination:", "match_2", 2.2 * inch, 0.5 * inch)
        self.text_field("3. Few-Shot Prompting:", "match_3", 2.2 * inch, 0.5 * inch)
        self.text_field("4. Chain-of-Thought:", "match_4", 2.2 * inch, 0.5 * inch)
        self.text_field("5. RTCF Framework:", "match_5", 2.2 * inch, 0.5 * inch)
        self.text_field("6. Token:", "match_6", 2.2 * inch, 0.5 * inch)
        self.text_field("7. Bias:", "match_7", 2.2 * inch, 0.5 * inch)

        # === PAGE 2: True/False + Short Answer ===
        self.new_page()

        self.section_header("SECTION 2: True or False (15 points)", Colors.TEAL)

        self.text("Write T for True or F for False in each box.", bold=True)
        self.space(0.08 * inch)

        tf_questions = [
            ('Adding "think step by step" to a prompt is called chain-of-thought prompting.', "tf_1"),
            ("AI chatbots have access to live internet data at all times.", "tf_2"),
            ("The 'Role' in RTCF tells the AI who it should pretend to be.", "tf_3"),
            ("It is safe to share your passwords with AI chatbots.", "tf_4"),
            ("A vague prompt will usually give you a vague answer.", "tf_5"),
            ("AI can never be wrong because it was trained on lots of data.", "tf_6"),
            ("Few-shot prompting means giving AI examples before your question.", "tf_7"),
            ("You should tell your teacher when you use AI to help with schoolwork.", "tf_8"),
        ]

        for i, (question, field_name) in enumerate(tf_questions):
            c = self.c
            # Draw the small text field first
            c.acroForm.textfield(
                name=field_name,
                x=Layout.MARGIN,
                y=self.y - 4,
                width=0.3 * inch,
                height=0.22 * inch,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.LIGHT_GRAY,
                textColor=black,
                fontSize=10,
                borderWidth=1,
                maxlen=0,
            )
            # Draw the question text next to it
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 9)
            c.drawString(Layout.MARGIN + 0.4 * inch, self.y, f"{i + 1}. {question}")
            self.y -= 0.32 * inch

        self.space(0.1 * inch)

        self.section_header("SECTION 3: Short Answer (25 points)", Colors.PROMPT_GREEN)

        self.text("Answer each question in 1-3 sentences.", bold=True)
        self.space(0.05 * inch)

        self.text("Q1: What is the difference between a vague prompt and a specific prompt? Give an example of each.", bold=True)
        self.multiline_field("", "sa_q1", 0.55 * inch)

        self.text("Q2: Explain the RTCF framework in your own words. What does each letter stand for?", bold=True)
        self.multiline_field("", "sa_q2", 0.55 * inch)

        self.text("Q3: What is an AI hallucination? Why is it important to know about this?", bold=True)
        self.multiline_field("", "sa_q3", 0.55 * inch)

        self.text("Q4: Name two things you should NEVER share with an AI chatbot and explain why.", bold=True)
        self.multiline_field("", "sa_q4", 0.55 * inch)

        # === PAGE 3: Prompt Improvement (20 points) ===
        self.new_page()

        self.section_header("SECTION 4: Improve These Prompts (20 points)", Colors.ORANGE)

        self.info_box(
            "Instructions",
            "Each prompt below is vague or poorly written. Rewrite it to be much better using the RTCF framework or prompting techniques you learned.",
            Colors.LIGHT_GRAY, 0.6 * inch
        )

        self.space(0.05 * inch)

        self.text('Q1: Original prompt: "Tell me about space"', bold=True)
        self.multiline_field("Your improved prompt:", "improve_q1", 0.55 * inch)

        self.text('Q2: Original prompt: "Write me a poem"', bold=True)
        self.multiline_field("Your improved prompt:", "improve_q2", 0.55 * inch)

        self.text('Q3: Original prompt: "Help me study"', bold=True)
        self.multiline_field("Your improved prompt:", "improve_q3", 0.55 * inch)

        self.text('Q4: Original prompt: "Explain math"', bold=True)
        self.multiline_field("Your improved prompt:", "improve_q4", 0.55 * inch)

        # === PAGE 4: Hands-On Challenge + AI Safety (15 points) ===
        self.new_page()

        self.section_header("SECTION 5: Hands-On AI Challenge (10 points)", Colors.AI_PURPLE)

        self.info_box(
            "Try It Yourself!",
            "Try using an AI tool (ChatGPT, Claude, Gemini, or Copilot) to complete this task. If you don't have access, write what prompt you WOULD use and what you'd expect the AI to say.",
            Colors.LIGHT_PURPLE, 0.7 * inch
        )

        self.text("Task: Ask AI to explain a topic you're learning in another class right now.", bold=True)
        self.space(0.05 * inch)

        self.text_field("AI tool you used:", "challenge_tool", 1.4 * inch)
        self.text_field("Subject/topic:", "challenge_topic", 1.2 * inch)
        self.multiline_field("The prompt you wrote:", "challenge_prompt", 0.5 * inch)
        self.multiline_field("How was the AI's response? Was it helpful? Anything wrong?", "challenge_response", 0.5 * inch)

        self.space(0.1 * inch)

        self.section_header("SECTION 5 (continued): AI Safety Scenarios (5 points)", Colors.RED)

        self.text("Read each scenario and explain what the student should do differently.", bold=True)
        self.space(0.05 * inch)

        self.text("Q1: A student copies an entire AI-generated essay and turns it in as their own work.", bold=True)
        self.multiline_field("", "safety_q1", 0.45 * inch)

        self.text("Q2: A student shares their home address and phone number with a chatbot to get local recommendations.", bold=True)
        self.multiline_field("", "safety_q2", 0.45 * inch)

        # === PAGE 5: Reflection + Bonus ===
        self.new_page()

        self.section_header("SECTION 6: Reflection (10 points)", Colors.PURPLE)

        self.text("Q1: What was the most interesting thing you learned about prompt engineering?", bold=True)
        self.multiline_field("", "reflect_q1", 0.5 * inch)

        self.text("Q2: How could you use AI tools to help you in school or in a hobby?", bold=True)
        self.multiline_field("", "reflect_q2", 0.5 * inch)

        self.text("Q3: Rate your confidence with AI prompting before and after this lesson (1-5):", bold=True)
        self.text_field("Before this lesson:", "confidence_before", 1.4 * inch, 1 * inch)
        self.text_field("After this lesson:", "confidence_after", 1.3 * inch, 1 * inch)

        self.space(0.15 * inch)

        self.section_header("BONUS: Teach Someone About Prompting (+5 points)", Colors.ORANGE)

        self.text("Teach a family member or friend one prompting tip from this week.", bold=True)
        self.space(0.05 * inch)

        self.text_field("Who did you teach?", "bonus_who", 1.5 * inch, 2.5 * inch)
        self.text_field("What tip did you share?", "bonus_tip", 1.5 * inch)
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
    output_path = os.path.join(parent_dir, "2026-04-11_Homework_Prompt_Engineering.pdf")
    pdf = HomeworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
