"""
Classwork PDF Generator - April 11, 2026
Prompt Engineering & Using AI Tools

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
        self.c.setTitle("Classwork: Prompt Engineering & Using AI Tools")
        self.page_num = 0
        self.total_pages = 6
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
                    "CLASSWORK: Prompt Engineering")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Learning to Talk to AI Effectively")
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
            name=field_name, x=field_x, y=self.y - 4,
            width=actual_width, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
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
            name=field_name, x=Layout.MARGIN,
            y=self.y - height + 0.08 * inch,
            width=Layout.CONTENT_WIDTH, height=height,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
            textColor=black, fontSize=10, borderWidth=1, maxlen=0,
            fieldFlags='multiline',
        )
        self.y -= height + 0.08 * inch

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
                x=Layout.MARGIN + 0.2 * inch, y=self.y - 2,
                size=11, borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.WHITE,
            )
            c.setFont("Helvetica", 10)
            c.setFillColor(Colors.DARK_GRAY)
            c.drawString(Layout.MARGIN + 0.2 * inch + 15, self.y, f"{letter_char}) {option}")
            self.y -= 0.2 * inch
        self.y -= 0.08 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # =========================================================================
    # BUILD METHOD
    # =========================================================================

    def build(self):
        # =================================================================
        # PAGE 1: Student Info + Key Terms Reference
        # =================================================================
        self.new_page()

        self.section_header("STUDENT INFORMATION", Colors.MEDIUM_BLUE)
        self.text_field("Name:", "student_name")
        self.text_field("Date:", "student_date")

        self.info_box(
            "Your Mission Today:",
            "You are a Prompt Engineer! Your job is to learn how to write effective prompts "
            "that get the best possible responses from AI tools. Use what you learned last week "
            "about LLMs and transformers to understand WHY these techniques work.",
            color=Colors.LIGHT_GREEN,
            height=0.75 * inch,
        )

        self.section_header("KEY TERMS REFERENCE", Colors.AI_PURPLE)

        terms = [
            ("Prompt:", "The text instruction you give to an AI to get a response"),
            ("Hallucination:", "When AI generates false or made-up information confidently"),
            ("Zero-Shot:", "Asking AI to do something with no examples"),
            ("Few-Shot:", "Giving AI a few examples before asking it to do something"),
            ("Chain-of-Thought:", "Asking AI to explain its reasoning step by step"),
            ("RTCF Framework:", "Role, Task, Context, Format -- a structure for writing good prompts"),
            ("Token:", "The smallest unit of text AI processes (like a word or word piece)"),
            ("Context Window:", "The maximum amount of text AI can process at once"),
        ]

        for term_name, term_def in terms:
            c = self.c
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(Layout.MARGIN, self.y, term_name)
            c.setFont("Helvetica", 9)
            term_width = stringWidth(term_name, "Helvetica-Bold", 9)
            c.drawString(Layout.MARGIN + term_width + 4, self.y, term_def)
            self.y -= 0.22 * inch

        self._draw_footer()

        # =================================================================
        # PAGE 2: Part 1 - Matching & True/False (25 points)
        # =================================================================
        self.new_page()

        self.section_header("PART 1: Matching -- AI & Prompting Terms (10 points)", Colors.AI_PURPLE)

        self.text("Match each term (1-7) with the correct definition letter (A-G).", size=9)
        self.space(0.05 * inch)

        definitions = [
            "A. The text input you give to an AI to get a response",
            "B. When AI confidently generates false information",
            "C. Asking AI to do a task with no examples given",
            "D. Providing a few examples before asking AI to complete a task",
            "E. Asking AI to show its reasoning step by step",
            "F. A framework: Role, Task, Context, Format",
            "G. The maximum amount of text an AI can process at once",
        ]

        for defn in definitions:
            self.text(defn, size=9, indent=0.1 * inch)

        self.space(0.08 * inch)

        match_terms = [
            "1. Prompt",
            "2. Hallucination",
            "3. Zero-Shot",
            "4. Few-Shot",
            "5. Chain-of-Thought",
            "6. RTCF Framework",
            "7. Context Window",
        ]

        for i, term in enumerate(match_terms):
            self.text_field(term, f"match_{i+1}",
                          label_width=2.2 * inch, field_width=0.5 * inch)

        self.section_header("PART 1 continued: True or False (15 points)", Colors.TEAL)

        tf_statements = [
            "1. A more specific prompt usually gives a better AI response.",
            "2. AI truly understands the meaning of what it writes.",
            "3. Hallucinations happen when AI makes up information that sounds real.",
            "4. You should always trust AI responses without checking them.",
            "5. Adding \"think step by step\" can improve AI accuracy.",
            "6. AI has access to real-time information from the internet.",
            "7. The RTCF framework stands for Role, Task, Context, Format.",
            "8. It is okay to share your home address with an AI chatbot.",
            "9. Few-shot prompting gives the AI examples before asking it to do something.",
            "10. AI can be biased based on its training data.",
        ]

        for i, stmt in enumerate(tf_statements):
            c = self.c
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 9)
            # Draw small text field first, then statement
            field_x = Layout.MARGIN
            c.acroForm.textfield(
                name=f"tf_{i+1}", x=field_x, y=self.y - 4,
                width=0.3 * inch, height=0.2 * inch,
                borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.LIGHT_GRAY,
                textColor=black, fontSize=9, borderWidth=1, maxlen=0,
            )
            c.drawString(Layout.MARGIN + 0.4 * inch, self.y, stmt)
            self.y -= 0.26 * inch

        self._draw_footer()

        # =================================================================
        # PAGE 3: Part 2 - Good vs Bad Prompts (20 points)
        # =================================================================
        self.new_page()

        self.section_header("PART 2: Identify Good vs Bad Prompts (10 points)", Colors.PROMPT_GREEN)

        self.text("For each pair, circle which prompt is BETTER and explain why.", size=9)
        self.space(0.05 * inch)

        self.text("Pair 1:", bold=True)
        self.text("Prompt A: \"Write about history\"", bold=True, indent=0.15 * inch)
        self.text("Prompt B: \"Write a 3-paragraph summary of the causes of", bold=True, indent=0.15 * inch)
        self.text("World War I for a 9th grade history class\"", bold=True, indent=0.15 * inch)
        self.text_field("Which is better? (A or B):", "pair1_choice",
                       label_width=2.2 * inch, field_width=0.5 * inch)
        self.multiline_field("Why?", "pair1_why", height=0.45 * inch)

        self.text("Pair 2:", bold=True)
        self.text("Prompt A: \"You are a math tutor. Solve 2x + 5 = 15.", bold=True, indent=0.15 * inch)
        self.text("Show each step and explain your reasoning.\"", bold=True, indent=0.15 * inch)
        self.text("Prompt B: \"Solve this math problem\"", bold=True, indent=0.15 * inch)
        self.text_field("Which is better? (A or B):", "pair2_choice",
                       label_width=2.2 * inch, field_width=0.5 * inch)
        self.multiline_field("Why?", "pair2_why", height=0.45 * inch)

        self.section_header("PART 2 continued: Rewrite These Prompts (10 points)", Colors.ORANGE)

        self.text("Make each vague prompt better using the RTCF framework.", bold=True)
        self.space(0.05 * inch)

        self.text("Q1: \"Help me with science\"", bold=False)
        self.multiline_field("Your improved prompt:", "rewrite_1", height=0.55 * inch)

        self.text("Q2: \"Write a story\"", bold=False)
        self.multiline_field("Your improved prompt:", "rewrite_2", height=0.55 * inch)

        self.text("Q3: \"Explain coding\"", bold=False)
        self.multiline_field("Your improved prompt:", "rewrite_3", height=0.55 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 4: Part 3 - Build Your Own Prompts (25 points)
        # =================================================================
        self.new_page()

        self.section_header("PART 3: Build Your Own Prompts Using RTCF (25 points)", Colors.AI_PURPLE)

        self.info_box(
            "Instructions:",
            "For each scenario, write a complete prompt using the RTCF framework. "
            "Label each part (Role, Task, Context, Format).",
            color=Colors.LIGHT_PURPLE,
            height=0.55 * inch,
        )

        self.text("Scenario 1: You want AI to help you study for a biology test about cells.", bold=True)
        self.space(0.05 * inch)
        self.text_field("Role:", "s1_role", label_width=0.8 * inch)
        self.text_field("Task:", "s1_task", label_width=0.8 * inch)
        self.text_field("Context:", "s1_context", label_width=0.8 * inch)
        self.text_field("Format:", "s1_format", label_width=0.8 * inch)
        self.multiline_field("Complete prompt:", "s1_complete", height=0.5 * inch)

        self.space(0.1 * inch)

        self.text("Scenario 2: You want AI to help you write a thank-you email to your teacher.", bold=True)
        self.space(0.05 * inch)
        self.text_field("Role:", "s2_role", label_width=0.8 * inch)
        self.text_field("Task:", "s2_task", label_width=0.8 * inch)
        self.text_field("Context:", "s2_context", label_width=0.8 * inch)
        self.text_field("Format:", "s2_format", label_width=0.8 * inch)
        self.multiline_field("Complete prompt:", "s2_complete", height=0.5 * inch)

        self._draw_footer()

        # =================================================================
        # PAGE 5: Part 4 - Spot the Hallucination + AI Safety (20 points)
        # =================================================================
        self.new_page()

        self.section_header("PART 4: Spot the Problem (10 points)", Colors.RED)

        self.text("Read each AI response and identify what might be wrong.", bold=True)
        self.space(0.05 * inch)

        self.text("Q1: AI Response: \"The Great Wall of China was built in 1842 by Emperor", bold=True)
        self.text("Napoleon as a trade route between China and France.\"", bold=True, indent=0.35 * inch)
        self.multiline_field("What's wrong with this response?", "spot1", height=0.45 * inch)

        self.text("Q2: AI Response: \"Python was created by Steve Jobs in 2015 as a", bold=True)
        self.text("replacement for JavaScript.\"", bold=True, indent=0.35 * inch)
        self.multiline_field("What's wrong with this response?", "spot2", height=0.45 * inch)

        self.text("Q3: A student asks AI to do their entire homework and submits the AI's", bold=True)
        self.text("answer as their own work. What's wrong with this?", bold=True, indent=0.35 * inch)
        self.multiline_field("Your answer:", "spot3", height=0.45 * inch)

        self.section_header("PART 4 continued: AI Safety Multiple Choice (10 points)", Colors.PROMPT_GREEN)

        self.multiple_choice(
            "Which of these is SAFE to share with an AI chatbot?",
            ["Your home address", "A math problem you need help with",
             "Your password", "Your Social Security number"],
            "safety_q1", q_num=1,
        )

        self.multiple_choice(
            "What should you do after getting important information from AI?",
            ["Trust it completely", "Share it on social media",
             "Fact-check it with a reliable source", "Ignore it"],
            "safety_q2", q_num=2,
        )

        self.multiple_choice(
            "When is it okay to use AI for schoolwork?",
            ["To copy answers word-for-word",
             "To help you understand a concept you're stuck on",
             "To write your entire essay for you",
             "To take a test for you"],
            "safety_q3", q_num=3,
        )

        self._draw_footer()

        # =================================================================
        # PAGE 6: Reflection + Bonus
        # =================================================================
        self.new_page()

        self.section_header("REFLECTION (10 points)", Colors.MEDIUM_BLUE)

        self.text("What is the most important thing you learned about prompting today?", bold=True)
        self.multiline_field("", "reflect_1", height=0.6 * inch)

        self.text("Write one prompt you could use AI for in your daily life (school, hobbies, etc.).", bold=True)
        self.multiline_field("", "reflect_2", height=0.6 * inch)

        self.text("On a scale of 1-5, how confident do you feel writing good AI prompts?", bold=True)
        self.text_field("Rating (1-5):", "reflect_rating",
                       label_width=1.2 * inch, field_width=0.5 * inch)
        self.multiline_field("Explain your rating:", "reflect_explain", height=0.45 * inch)

        self.section_header("BONUS: Ultimate Prompt Challenge (+10 points)", Colors.ORANGE)

        self.info_box(
            "Challenge:",
            "Write the BEST possible prompt you can for this task: You want AI to help you plan "
            "a birthday party for your friend. Use everything you learned today (RTCF, be specific, "
            "set the format). The more detailed and well-structured your prompt, the more bonus points!",
            color=Colors.SKY_BLUE,
            height=0.85 * inch,
        )

        self.multiline_field("Your ultimate prompt:", "bonus_prompt", height=1.0 * inch)

        self._draw_footer()

        # Save the PDF
        self.c.save()
        print(f"Created: {self.output_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-04-11_Classwork_Prompt_Engineering.pdf")
    pdf = ClassworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
