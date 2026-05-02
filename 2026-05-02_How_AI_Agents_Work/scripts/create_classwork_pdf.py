"""
Classwork PDF Generator - May 2, 2026
How AI Agents Actually Work - Agent Trace Lab

Students label the Think/Act/Observe steps in a real agent run,
and compare a chatbot vs. an agent on the same task.

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
    # Agent-themed accents
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
    CONTENT_BOTTOM = FOOTER_HEIGHT + 0.3 * inch


# =============================================================================
# PDF BUILDER
# =============================================================================

class ClassworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Classwork: Agent Trace Lab")
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
                    "CLASSWORK: Agent Trace Lab")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "How AI Agents Actually Work — Inside the Loop")
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

    def checkbox(self, label, field_name, indent=0):
        c = self.c
        c.acroForm.checkbox(
            name=field_name,
            x=Layout.MARGIN + indent, y=self.y - 0.02 * inch,
            size=12,
            borderColor=Colors.MEDIUM_BLUE,
            fillColor=Colors.WHITE,
        )
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN + indent + 0.3 * inch, self.y, label)
        self.y -= 0.27 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # -------------------------------------------------------------------------
    # Build
    # -------------------------------------------------------------------------

    def build(self):
        # === PAGE 1: Setup + Recap (15 points) ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.section_header("SECTION 1: Recap — The Agent Loop (15 points)",
                           Colors.AGENT_PURPLE)

        self.info_box(
            "Quick Recap from Last Week",
            "An AI agent follows a loop: THINK (plan) -> ACT (use a tool) -> "
            "OBSERVE (look at the result) -> REPEAT until the task is done.",
            Colors.LIGHT_PURPLE, 0.7 * inch
        )

        self.text("Q1: In your own words, what is the AGENT LOOP? (2 sentences)",
                 bold=True)
        self.multiline_field("", "loop_def", 0.55 * inch)

        self.text("Q2: Name the 4 core components of an AI agent we learned:",
                 bold=True)
        self.text_field("1.", "comp_1", 0.3 * inch, 4.5 * inch)
        self.text_field("2.", "comp_2", 0.3 * inch, 4.5 * inch)
        self.text_field("3.", "comp_3", 0.3 * inch, 4.5 * inch)
        self.text_field("4.", "comp_4", 0.3 * inch, 4.5 * inch)

        self._draw_footer()

        # === PAGE 2: Agent Skill Identifier (25 points) ===
        self.new_page()

        self.section_header("SECTION 2: Spot the Agent Skills (25 points)",
                           Colors.THINK_BLUE)

        self.info_box(
            "Your Job",
            "For each task below, check ALL the agent skills it would need. "
            "More than one can apply.",
            Colors.SKY_BLUE, 0.55 * inch
        )

        # Task 1
        self.text('Task A: "Find the cheapest flight from SFO to Tokyo next month '
                 'and email it to my dad."', bold=True, size=10)
        self.space(0.05 * inch)
        self.checkbox("Web search (find flight prices)", "a_search", 0.3 * inch)
        self.checkbox("Tool use (send an email)", "a_email", 0.3 * inch)
        self.checkbox("Planning (multiple steps in order)", "a_plan", 0.3 * inch)
        self.checkbox("Memory (remember dad's email address)", "a_memory", 0.3 * inch)
        self.space(0.1 * inch)

        # Task 2
        self.text('Task B: "What is the capital of France?"', bold=True, size=10)
        self.space(0.05 * inch)
        self.checkbox("Web search", "b_search", 0.3 * inch)
        self.checkbox("Tool use", "b_tool", 0.3 * inch)
        self.checkbox("Planning", "b_plan", 0.3 * inch)
        self.checkbox("None — a chatbot can answer this", "b_none", 0.3 * inch)
        self.space(0.1 * inch)

        # Task 3
        self.text('Task C: "Build me a working calculator app and show it to me."',
                 bold=True, size=10)
        self.space(0.05 * inch)
        self.checkbox("Code execution (run code)", "c_code", 0.3 * inch)
        self.checkbox("Planning (design then build)", "c_plan", 0.3 * inch)
        self.checkbox("Observation (test and fix bugs)", "c_observe", 0.3 * inch)
        self.checkbox("Web search", "c_search", 0.3 * inch)
        self.space(0.1 * inch)

        # Task 4
        self.text('Task D: "Research 3 colleges, compare their tuition and weather, '
                 'and write me a summary."', bold=True, size=10)
        self.space(0.05 * inch)
        self.checkbox("Web search", "d_search", 0.3 * inch)
        self.checkbox("Planning (3 schools, then compare, then summarize)",
                     "d_plan", 0.3 * inch)
        self.checkbox("Memory (hold info from all 3 while comparing)",
                     "d_memory", 0.3 * inch)
        self.checkbox("Image generation", "d_image", 0.3 * inch)

        self._draw_footer()

        # === PAGE 3: Annotate the Trace (35 points) ===
        self.new_page()

        self.section_header("SECTION 3: Annotate the Trace (35 points)",
                           Colors.ACT_ORANGE)

        self.info_box(
            "Run This With Your AI",
            "Open your AI agent (Gemini, ChatGPT, or Claude). Paste the prompt "
            "below. Watch what it does step by step — many agents show their "
            "thinking. Then label each step you see.",
            Colors.LIGHT_GREEN, 0.85 * inch
        )

        self.text("Prompt to use (copy exactly):", bold=True)
        self.space(0.05 * inch)

        # Prompt box
        c = self.c
        c.setFillColor(Colors.LIGHT_GRAY)
        c.setStrokeColor(Colors.MEDIUM_BLUE)
        c.roundRect(Layout.MARGIN, self.y - 0.95 * inch,
                   Layout.CONTENT_WIDTH, 0.95 * inch, 5, fill=True, stroke=True)
        c.setFillColor(Colors.DARK_BLUE)
        c.setFont("Courier-Bold", 9)
        c.drawString(Layout.MARGIN + 0.15 * inch, self.y - 0.2 * inch,
                    'I want to plan a 1-day visit to a national park near me.')
        c.drawString(Layout.MARGIN + 0.15 * inch, self.y - 0.36 * inch,
                    'Find the closest one, check the weather forecast for')
        c.drawString(Layout.MARGIN + 0.15 * inch, self.y - 0.52 * inch,
                    'this Saturday, suggest 3 things to do, and write me a')
        c.drawString(Layout.MARGIN + 0.15 * inch, self.y - 0.68 * inch,
                    'short packing list. Show your steps as you go.')
        self.y -= 1.1 * inch

        self.text("Step 1 — What was the AI's FIRST thought / plan? (THINK)",
                 bold=True, size=10)
        self.multiline_field("", "trace_think1", 0.45 * inch)

        self.text("Step 2 — What ACTION / tool did it use first? (ACT)",
                 bold=True, size=10)
        self.multiline_field("", "trace_act1", 0.45 * inch)

        self.text("Step 3 — What did it OBSERVE / find from that action?",
                 bold=True, size=10)
        self.multiline_field("", "trace_observe1", 0.45 * inch)

        self.text("Step 4 — How many times did it loop (think/act/observe) total?",
                 bold=True, size=10)
        self.text_field("Number of loops:", "trace_loops", 1.3 * inch, 1 * inch)

        self._draw_footer()

        # === PAGE 4: Same Task, Two Ways + Bonus (25 + 10 points) ===
        self.new_page()

        self.section_header("SECTION 4: Same Task, Two Ways (25 points)",
                           Colors.OBSERVE_GREEN)

        self.info_box(
            "Compare a Chatbot vs. an Agent",
            "Pick ANY AI tool and ask it the SAME question two ways: once "
            "asking for just an answer, once asking it to use tools and search "
            "the web. Notice the difference.",
            Colors.LIGHT_GREEN, 0.85 * inch
        )

        self.text_field("AI tool you used:", "compare_tool", 1.5 * inch, 3 * inch)

        self.space(0.05 * inch)

        self.text("Question (same for both): What is the most popular video game right now?",
                 bold=True, size=9)
        self.space(0.1 * inch)

        self.text("Way 1 — Just answer (no tools):", bold=True)
        self.multiline_field("AI's answer:", "way1_answer", 0.5 * inch)

        self.text("Way 2 — Use the web to check what is popular RIGHT NOW:",
                 bold=True)
        self.multiline_field("AI's answer:", "way2_answer", 0.5 * inch)

        self.text("Q: Which answer was more accurate / current? Why do you think so?",
                 bold=True)
        self.multiline_field("", "compare_why", 0.45 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: Break the Agent (+10 points)", Colors.AMBER)

        self.text("Try to give the agent a task it CAN'T do. Describe what happened.",
                 bold=True, size=9)
        self.multiline_field("", "bonus_break", 0.55 * inch)

        self._draw_footer()

        self.c.save()
        print(f"[SUCCESS] Classwork PDF created: {self.output_path}")
        return self.output_path


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir,
                               "2026-05-02_Classwork_Agent_Trace.pdf")
    pdf = ClassworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
