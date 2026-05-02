"""
Homework PDF Generator - May 2, 2026
How AI Agents Actually Work - Build Your Workflow

Students design a 5-step agent workflow for a real task in their life,
specifying the prompt and tool at each step.

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
    AGENT_PURPLE = HexColor('#673AB7')
    THINK_BLUE = HexColor('#1976D2')
    ACT_ORANGE = HexColor('#F57C00')
    OBSERVE_GREEN = HexColor('#388E3C')
    LOOP_TEAL = HexColor('#00897B')
    AMBER = HexColor('#FFB300')


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
        self.c.setTitle("Homework: Build Your Agent Workflow")
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
                    "HOMEWORK: Build Your Agent Workflow")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Design a real, multi-step AI agent for your own life")
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
        self.y -= height + 0.15 * inch

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

        self.section_header("SECTION 1: Vocabulary Match (15 points)",
                           Colors.AGENT_PURPLE)

        self.text("Match each term with its definition. Write the letter in the box.",
                 bold=True)
        self.space(0.08 * inch)

        self.text("A. Hidden instructions that tell the AI how to behave",
                 size=9)
        self.text("B. The amount of text the AI can hold in memory at once",
                 size=9)
        self.text("C. The cycle: Think -> Act -> Observe -> Repeat",
                 size=9)
        self.text("D. Functions an agent can call (web search, run code, send email)",
                 size=9)
        self.text("E. Sending a request over the network to another program",
                 size=9)
        self.text("F. The visible step-by-step thinking some agents show",
                 size=9)
        self.text("G. Human-level intelligence — does NOT exist yet",
                 size=9)

        self.space(0.1 * inch)

        self.text_field("1. Agent Loop:", "match_1", 2.0 * inch, 0.5 * inch)
        self.text_field("2. Context Window:", "match_2", 2.0 * inch, 0.5 * inch)
        self.text_field("3. System Prompt:", "match_3", 2.0 * inch, 0.5 * inch)
        self.text_field("4. Tools:", "match_4", 2.0 * inch, 0.5 * inch)
        self.text_field("5. Tool Call (network):", "match_5", 2.0 * inch, 0.5 * inch)
        self.text_field("6. Reasoning:", "match_6", 2.0 * inch, 0.5 * inch)
        self.text_field("7. AGI:", "match_7", 2.0 * inch, 0.5 * inch)

        self._draw_footer()

        # === PAGE 2: True / False + Short Answers (20 points) ===
        self.new_page()

        self.section_header("SECTION 2: True or False (10 points)",
                           Colors.THINK_BLUE)

        self.text("Write T (True) or F (False) in each box.", bold=True)
        self.space(0.05 * inch)

        self.text_field("1. An AI agent is just a chatbot with a different name.",
                       "tf_1", 5.5 * inch, 0.4 * inch)
        self.text_field("2. The context window has a limit; conversations can outgrow it.",
                       "tf_2", 5.5 * inch, 0.4 * inch)
        self.text_field("3. When an agent uses a tool, it sends a network request.",
                       "tf_3", 5.5 * inch, 0.4 * inch)
        self.text_field("4. AGI exists today and is the same as a chatbot.",
                       "tf_4", 5.5 * inch, 0.4 * inch)
        self.text_field("5. A system prompt is the same as the user's question.",
                       "tf_5", 5.5 * inch, 0.4 * inch)
        self.text_field("6. Agents can plan multiple steps before acting.",
                       "tf_6", 5.5 * inch, 0.4 * inch)
        self.text_field("7. Memory lets an agent refer back to earlier in the chat.",
                       "tf_7", 5.5 * inch, 0.4 * inch)
        self.text_field("8. You should always trust an agent's answer without checking.",
                       "tf_8", 5.5 * inch, 0.4 * inch)

        self.space(0.1 * inch)

        self.section_header("SECTION 3: Short Answer (10 points)",
                           Colors.OBSERVE_GREEN)

        self.text("Q1: Explain in your own words what a TOOL CALL is. (2 sentences)",
                 bold=True)
        self.multiline_field("", "sa_q1", 0.55 * inch)

        self.text("Q2: Why might a long conversation make an AI 'forget' early messages?",
                 bold=True)
        self.multiline_field("", "sa_q2", 0.55 * inch)

        self._draw_footer()

        # === PAGE 3: Build Your Workflow Part 1 (20 of 35 points) ===
        self.new_page()

        self.section_header("SECTION 4: Build Your Workflow (35 points)",
                           Colors.ACT_ORANGE)

        self.info_box(
            "Your Mission",
            "Design a real AI agent that helps with something in YOUR life. "
            "Pick a task that needs MULTIPLE steps - not just one question. "
            "Examples: study buddy, meal planner, vacation planner, club organizer.",
            Colors.LIGHT_GREEN, 0.85 * inch
        )

        self.text_field("Name your agent:", "agent_name", 1.6 * inch, 3.5 * inch)
        self.multiline_field("What does your agent do? (1-2 sentences)",
                            "agent_purpose", 0.45 * inch)

        self.text("Which TOOLS does your agent need? Check at least 2:",
                 bold=True)
        self.space(0.05 * inch)

        # Tool checkboxes - using text fields instead so all show consistently
        self.text("[  ] Web search    [  ] Code execution    [  ] Image generation",
                 size=10, indent=0.2 * inch)
        self.text("[  ] Send email    [  ] Calendar / reminders    [  ] File reader",
                 size=10, indent=0.2 * inch)
        self.text("[  ] Other (describe below)", size=10, indent=0.2 * inch)
        self.space(0.05 * inch)
        self.text_field("Other tools:", "agent_other_tools",
                       1.0 * inch, 4 * inch)

        self.space(0.05 * inch)

        self.multiline_field(
            "What is your agent's SYSTEM PROMPT? (1-2 sentences telling it how to behave)",
            "agent_system", 0.6 * inch
        )

        self._draw_footer()

        # === PAGE 4: Build Your Workflow Part 2 - The 5 Steps ===
        self.new_page()

        self.section_header("SECTION 4 (cont): Your Agent's 5-Step Workflow",
                           Colors.ACT_ORANGE)

        self.info_box(
            "Map It Out",
            "Write the EXACT steps your agent would follow. For each step, "
            "say what it would think, which tool it would use, and what it "
            "would do with the result.",
            Colors.SKY_BLUE, 0.7 * inch
        )

        self.text("Step 1:", bold=True)
        self.multiline_field("", "step1", 0.4 * inch)

        self.text("Step 2:", bold=True)
        self.multiline_field("", "step2", 0.4 * inch)

        self.text("Step 3:", bold=True)
        self.multiline_field("", "step3", 0.4 * inch)

        self.text("Step 4:", bold=True)
        self.multiline_field("", "step4", 0.4 * inch)

        self.text("Step 5:", bold=True)
        self.multiline_field("", "step5", 0.4 * inch)

        self._draw_footer()

        # === PAGE 5: Reflection + Bonus ===
        self.new_page()

        self.section_header("SECTION 5: Reflection (20 points)",
                           Colors.PURPLE)

        self.text("Q1: What is ONE thing your agent could get wrong, and how would",
                 bold=True)
        self.text("you check its work?", bold=True, indent=0.3 * inch)
        self.multiline_field("", "reflect_q1", 0.55 * inch)

        self.text("Q2: Could a regular chatbot do this task? Why or why not?",
                 bold=True)
        self.multiline_field("", "reflect_q2", 0.55 * inch)

        self.text("Q3: What is one ETHICAL concern your agent should respect?",
                 bold=True)
        self.text("(privacy, honesty, not deceiving people, etc.)",
                 size=9, indent=0.3 * inch)
        self.multiline_field("", "reflect_q3", 0.55 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: Try It With a Real Agent (+5 points)",
                           Colors.AMBER)

        self.text("Pick ONE step from your workflow and actually run it on a real",
                 bold=True, size=9)
        self.text("AI agent. Paste a screenshot or describe the result.",
                 bold=True, size=9, indent=0.3 * inch)
        self.space(0.05 * inch)

        self.text_field("Which step did you try?", "bonus_step",
                       1.7 * inch, 3 * inch)
        self.multiline_field("What happened? Did the agent do it correctly?",
                            "bonus_result", 0.55 * inch)

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
    output_path = os.path.join(parent_dir,
                               "2026-05-02_Homework_Build_Your_Workflow.pdf")
    pdf = HomeworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
