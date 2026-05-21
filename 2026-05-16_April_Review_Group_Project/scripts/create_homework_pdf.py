"""
Homework PDF Generator - May 16, 2026
April & May Review — Individual Reinforcement

Cumulative review homework covering GenAI basics, prompting/RTCF,
meta prompting, AI agents, agent loop, LLM internals, and AI safety.
Mix of matching, T/F, multiple choice, short answer, applied scenarios,
and a creative challenge.

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
    REVIEW_INDIGO = HexColor('#3F51B5')


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
        self.c.setTitle("Homework: April & May AI Review")
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
                    "HOMEWORK: April & May AI Review")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Everything We Learned: GenAI, Prompting, Agents, and LLM Internals")
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
                    "Due: Next class  |  Total Points: 100 (+10 bonus)")

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
        for line in lines[:6]:
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
        # === PAGE 1: Student Info + Matching (20 points) ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "hw_name", 0.55 * inch)
        self.text_field("Date:", "hw_date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.section_header("SECTION 1: Vocabulary Match (20 points)",
                           Colors.REVIEW_INDIGO)

        self.text("Match each term with its definition. Write the letter in the box.",
                 bold=True)
        self.space(0.08 * inch)

        self.text("A. Small chunks of text (words, word-pieces, punctuation) that an LLM reads",
                 size=9)
        self.text("B. A framework for writing good prompts: Role, Task, Context, Format",
                 size=9)
        self.text("C. When AI confidently presents false information as fact",
                 size=9)
        self.text("D. The cycle an agent follows: Think -> Act -> Observe -> Repeat",
                 size=9)
        self.text("E. Using AI to help you write or improve your prompts",
                 size=9)
        self.text("F. A setting that controls how creative vs. predictable AI answers are",
                 size=9)
        self.text("G. The amount of text the AI can hold in memory at once",
                 size=9)
        self.text("H. Functions an agent can call (web search, run code, send email)",
                 size=9)
        self.text("I. Hidden instructions that tell the AI how to behave",
                 size=9)
        self.text("J. A mechanism that helps the model focus on important earlier tokens",
                 size=9)

        self.space(0.08 * inch)

        self.text_field("1. Tokens:", "match_1", 1.8 * inch, 0.5 * inch)
        self.text_field("2. RTCF:", "match_2", 1.8 * inch, 0.5 * inch)
        self.text_field("3. Hallucination:", "match_3", 1.8 * inch, 0.5 * inch)
        self.text_field("4. Agent Loop:", "match_4", 1.8 * inch, 0.5 * inch)
        self.text_field("5. Meta Prompting:", "match_5", 1.8 * inch, 0.5 * inch)
        self.text_field("6. Temperature:", "match_6", 1.8 * inch, 0.5 * inch)
        self.text_field("7. Context Window:", "match_7", 1.8 * inch, 0.5 * inch)
        self.text_field("8. Tools:", "match_8", 1.8 * inch, 0.5 * inch)
        self.text_field("9. System Prompt:", "match_9", 1.8 * inch, 0.5 * inch)
        self.text_field("10. Attention:", "match_10", 1.8 * inch, 0.5 * inch)

        self._draw_footer()

        # === PAGE 2: True/False + Multiple Choice (25 points) ===
        self.new_page()

        self.section_header("SECTION 2: True or False (10 points)",
                           Colors.THINK_BLUE)

        self.text("Write T (True) or F (False) in each box.", bold=True)
        self.space(0.05 * inch)

        self.text_field("1. The Transformer architecture was introduced in 2017.",
                       "tf_1", 5.5 * inch, 0.4 * inch)
        self.text_field("2. A token is always exactly one full word.",
                       "tf_2", 5.5 * inch, 0.4 * inch)
        self.text_field("3. An AI agent can plan steps and use tools; a chatbot cannot.",
                       "tf_3", 5.5 * inch, 0.4 * inch)
        self.text_field("4. AGI (Artificial General Intelligence) exists today.",
                       "tf_4", 5.5 * inch, 0.4 * inch)
        self.text_field("5. Higher temperature makes AI answers more creative but less predictable.",
                       "tf_5", 5.5 * inch, 0.4 * inch)
        self.text_field("6. You should share your passwords with AI chatbots.",
                       "tf_6", 5.5 * inch, 0.4 * inch)
        self.text_field("7. Chain-of-thought prompting asks the AI to think step by step.",
                       "tf_7", 5.5 * inch, 0.4 * inch)
        self.text_field("8. LLMs truly understand language the same way humans do.",
                       "tf_8", 5.5 * inch, 0.4 * inch)
        self.text_field("9. RLHF uses human feedback to improve AI outputs.",
                       "tf_9", 5.5 * inch, 0.4 * inch)
        self.text_field("10. When an agent uses a tool, it sends a network request.",
                       "tf_10", 5.5 * inch, 0.4 * inch)

        self.space(0.1 * inch)

        self.section_header("SECTION 3: Multiple Choice (15 points)",
                           Colors.AGENT_PURPLE)

        self.text("Write the letter (A, B, C, or D) in the answer box.", bold=True)
        self.space(0.05 * inch)

        self.text("1. What is the core process LLMs use to generate text?", bold=True, size=9)
        self.text("   A) Database lookup  B) Next-token prediction  C) Internet search  D) Random selection", size=9)
        self.text_field("Answer:", "mc_1", 0.7 * inch, 0.5 * inch)

        self.text("2. What does the 'R' in RTCF stand for?", bold=True, size=9)
        self.text("   A) Read  B) Role  C) Run  D) Repeat", size=9)
        self.text_field("Answer:", "mc_2", 0.7 * inch, 0.5 * inch)

        self.text("3. Which task NEEDS an AI agent, not just a chatbot?", bold=True, size=9)
        self.text("   A) Define 'happy'  B) Tell a joke  C) Search, compare, and email a summary  D) Solve 2+2", size=9)
        self.text_field("Answer:", "mc_3", 0.7 * inch, 0.5 * inch)

        self._draw_footer()

        # === PAGE 3: Multiple Choice cont. + Short Answer (continued + 20 points) ===
        self.new_page()

        self.section_header("SECTION 3: Multiple Choice (continued)",
                           Colors.AGENT_PURPLE)

        self.text("4. In the agent loop, what comes after 'Act'?", bold=True, size=9)
        self.text("   A) Think  B) Observe  C) Loop  D) Goal", size=9)
        self.text_field("Answer:", "mc_4", 0.7 * inch, 0.5 * inch)

        self.text("5. What is 'attention' in a Transformer?", bold=True, size=9)
        self.text("   A) AI liking your question  B) Focusing on important earlier tokens  C) A timer  D) Watching you", size=9)
        self.text_field("Answer:", "mc_5", 0.7 * inch, 0.5 * inch)

        self.space(0.1 * inch)

        self.section_header("SECTION 4: Short Answer (20 points)",
                           Colors.OBSERVE_GREEN)

        self.text("Answer each question in 2-3 sentences.", bold=True)
        self.space(0.05 * inch)

        self.text("1. Explain in your own words how an LLM generates text.",
                 bold=True, size=9)
        self.text("   Use the words 'token', 'predict', and 'context' in your answer.",
                 size=9)
        self.multiline_field("", "sa_1", 0.6 * inch)

        self.text("2. What is the difference between an AI chatbot and an AI agent?",
                 bold=True, size=9)
        self.text("   Give an example task for each.",
                 size=9)
        self.multiline_field("", "sa_2", 0.6 * inch)

        self.text("3. Explain what meta prompting is and why it is useful.",
                 bold=True, size=9)
        self.multiline_field("", "sa_3", 0.6 * inch)

        self.text("4. Why can LLMs hallucinate? What should you do before trusting",
                 bold=True, size=9)
        self.text("   an important AI answer?",
                 bold=True, size=9)
        self.multiline_field("", "sa_4", 0.6 * inch)

        self._draw_footer()

        # === PAGE 4: Applied Scenarios (25 points) ===
        self.new_page()

        self.section_header("SECTION 5: Applied Scenarios (25 points)",
                           Colors.ACT_ORANGE)

        self.info_box(
            "Real-World Thinking",
            "Read each scenario and apply what you have learned about AI, "
            "prompting, agents, and safety to answer the questions.",
            Colors.SKY_BLUE, 0.55 * inch
        )

        self.text("Scenario A:", bold=True)
        self.text("Your friend wants to use AI to write a history report about the moon landing.", size=9)
        self.text("They type: 'Tell me about the moon.' The AI gives a long, unfocused answer.", size=9)
        self.space(0.05 * inch)
        self.text("Rewrite their prompt using RTCF to get a better result:", bold=True, size=9)
        self.multiline_field("", "scenario_a", 0.6 * inch)

        self.text("Scenario B:", bold=True)
        self.text("A student asks ChatGPT: 'Who won the NBA finals last night?'", size=9)
        self.text("The AI gives a confident answer, but the finals haven't happened yet.", size=9)
        self.space(0.05 * inch)
        self.text("What went wrong? What AI concept explains this? (2-3 sentences)", bold=True, size=9)
        self.multiline_field("", "scenario_b", 0.6 * inch)

        self.text("Scenario C:", bold=True)
        self.text("You want an AI to: research the 3 best laptops under $500, compare them,", size=9)
        self.text("and email a summary to your parent.", size=9)
        self.space(0.05 * inch)
        self.text("Does this need a chatbot or an agent? List the agent components needed:", bold=True, size=9)
        self.multiline_field("", "scenario_c", 0.65 * inch)

        self.text("Scenario D:", bold=True)
        self.text("You are designing an AI study buddy. Would you set temperature to low or high", size=9)
        self.text("for math help? What about for brainstorming creative story ideas? Why?", size=9)
        self.multiline_field("", "scenario_d", 0.55 * inch)

        self._draw_footer()

        # === PAGE 5: Reflection + Bonus (10 + 10 points) ===
        self.new_page()

        self.section_header("SECTION 6: Reflection (10 points)",
                           Colors.PURPLE)

        self.text("1. What is the most important thing you learned about AI this semester?",
                 bold=True, size=9)
        self.multiline_field("", "reflect_1", 0.55 * inch)

        self.text("2. Name one way AI could help you in your daily life, and one risk",
                 bold=True, size=9)
        self.text("   you would need to watch out for.",
                 size=9)
        self.multiline_field("", "reflect_2", 0.55 * inch)

        self.text("3. If you could build any AI agent, what would it do? Describe its", bold=True, size=9)
        self.text("   tools, system prompt, and one step of its Think->Act->Observe loop.",
                 size=9)
        self.multiline_field("", "reflect_3", 0.65 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: AI Concept Map (+10 points)", Colors.AMBER)

        self.info_box(
            "Creative Challenge",
            "On a separate sheet (or in the box below), draw or describe a concept map "
            "connecting at least 8 of these terms: LLM, Transformer, tokens, "
            "next-token prediction, attention, temperature, hallucination, RTCF, "
            "meta prompting, AI agent, tools, memory, Think/Act/Observe, "
            "context window, system prompt. Show how the concepts relate to each other.",
            Colors.LIGHT_PURPLE, 0.85 * inch
        )

        self.text("Describe your concept map or attach a photo of your drawing:", bold=True, size=9)
        self.multiline_field("", "bonus_concept_map", 0.8 * inch)

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
                               "2026-05-16_Homework_April_Review.pdf")
    pdf = HomeworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
