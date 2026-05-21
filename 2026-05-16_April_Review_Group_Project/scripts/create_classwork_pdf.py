"""
Classwork PDF Generator - May 16, 2026
April Review — Group AI Presentation Project

Groups of 3 students create a presentation/story reviewing key AI concepts
from April-May. Each member has a role: AI Architect, Story Director,
Presenter/Designer.

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
    CONTENT_BOTTOM = FOOTER_HEIGHT + 0.3 * inch


# =============================================================================
# PDF BUILDER
# =============================================================================

class ClassworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Classwork: AI Review Group Project")
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
        c.setFont("Helvetica-Bold", 16)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                    "CLASSWORK: AI Review — Group Project")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "April Review — Build a Presentation Reviewing Everything We Learned")
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
        # === PAGE 1: Team Info + Mission + Roles ===
        self.new_page()

        self.section_header("Team Information", Colors.DARK_BLUE)
        self.text_field("Team Name:", "team_name", 1.0 * inch)
        self.text_field("Member 1:", "member_1", 1.0 * inch)
        self.text_field("Member 2:", "member_2", 1.0 * inch)
        self.text_field("Member 3:", "member_3", 1.0 * inch)
        self.text_field("Date:", "date", 1.0 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.section_header("Your Mission (Read Carefully!)", Colors.REVIEW_INDIGO)

        self.info_box(
            "The Challenge",
            "Your team will create a short presentation or story that reviews "
            "the key AI concepts we have learned since April. You will present "
            "it to the whole class at the end (~3-4 minutes). Your story should "
            "include an AI character or agent and show how it works.",
            Colors.LIGHT_PURPLE, 0.85 * inch
        )

        self.section_header("Roles — Assign One Per Person", Colors.AGENT_PURPLE)

        self.text("AI Architect — designs the AI character/agent", bold=True, size=10)
        self.text("  Pick the LLM, write a system prompt (use RTCF), choose a temperature,", size=9, indent=0.15 * inch)
        self.text("  list the tools and memory your agent needs.", size=9, indent=0.15 * inch)
        self.space(0.05 * inch)

        self.text("Story Director — writes the demo scenario or skit", bold=True, size=10)
        self.text("  Show the Think->Act->Observe loop in action, include a moment where", size=9, indent=0.15 * inch)
        self.text("  the AI hallucinates and the user catches it.", size=9, indent=0.15 * inch)
        self.space(0.05 * inch)

        self.text("Presenter/Designer — builds slides or visuals, leads delivery", bold=True, size=10)
        self.text("  Create slides or a poster, make sure key vocab is shown, and practice", size=9, indent=0.15 * inch)
        self.text("  the group's presentation.", size=9, indent=0.15 * inch)
        self.space(0.1 * inch)

        self.text_field("AI Architect:", "role_architect", 1.3 * inch, 3.5 * inch)
        self.text_field("Story Director:", "role_director", 1.3 * inch, 3.5 * inch)
        self.text_field("Presenter/Designer:", "role_presenter", 1.3 * inch, 3.5 * inch)

        self._draw_footer()

        # === PAGE 2: AI Architect Worksheet (35 points) ===
        self.new_page()

        self.section_header("AI ARCHITECT — Design Your Agent (35 points)",
                           Colors.THINK_BLUE)

        self.info_box(
            "Your Job",
            "Design the AI character that stars in your team's story. Fill in "
            "every detail below. Think about what you learned about LLMs, "
            "prompting (RTCF), agents, tools, and memory.",
            Colors.SKY_BLUE, 0.7 * inch
        )

        self.text_field("Agent Name:", "agent_name", 1.3 * inch, 4 * inch)

        self.text("Which LLM powers your agent? (pick one)", bold=True)
        self.space(0.05 * inch)
        self.checkbox("GPT (OpenAI)", "llm_gpt", 0.3 * inch)
        self.checkbox("Claude (Anthropic)", "llm_claude", 0.3 * inch)
        self.checkbox("Gemini (Google)", "llm_gemini", 0.3 * inch)
        self.checkbox("Other (name it below)", "llm_other", 0.3 * inch)
        self.text_field("Other LLM:", "llm_other_name", 1.0 * inch, 3 * inch)

        self.space(0.05 * inch)

        self.text("System Prompt — Write the hidden instructions using RTCF:", bold=True)
        self.text("  R = Role | T = Task | C = Context | F = Format", size=9, indent=0.15 * inch)
        self.multiline_field("", "system_prompt", 0.8 * inch)

        self.text("Temperature Setting (circle or write):", bold=True)
        self.text("  Low (0.0-0.3) = factual/safe | Medium (0.4-0.7) = balanced | High (0.8-1.0) = creative",
                 size=9, indent=0.15 * inch)
        self.text_field("Temperature:", "temperature", 1.1 * inch, 1.5 * inch)

        self.text("What TOOLS does your agent have? Check all that apply:", bold=True)
        self.space(0.05 * inch)
        self.checkbox("Web search", "tool_search", 0.3 * inch)
        self.checkbox("Code execution", "tool_code", 0.3 * inch)
        self.checkbox("Send email / message", "tool_email", 0.3 * inch)
        self.checkbox("Calendar / reminders", "tool_calendar", 0.3 * inch)
        self.checkbox("Image generation", "tool_image", 0.3 * inch)
        self.checkbox("File reader / writer", "tool_files", 0.3 * inch)
        self.text_field("Other tools:", "tools_other", 1.0 * inch, 4 * inch)

        self.text("What kind of MEMORY does your agent use?", bold=True)
        self.multiline_field("", "agent_memory", 0.45 * inch)

        self._draw_footer()

        # === PAGE 3: Story Director Worksheet (35 points) ===
        self.new_page()

        self.section_header("STORY DIRECTOR — Write the Scenario (35 points)",
                           Colors.ACT_ORANGE)

        self.info_box(
            "Your Job",
            "Write a short story or skit that shows the agent in action. "
            "It MUST include the Think->Act->Observe loop AND a moment "
            "where the AI hallucinates and the user catches it.",
            Colors.LIGHT_GREEN, 0.7 * inch
        )

        self.text("What task does the user give the agent?", bold=True)
        self.multiline_field("", "user_task", 0.5 * inch)

        self.text("Step 1 — THINK: What does the agent plan to do first?", bold=True)
        self.multiline_field("", "story_think", 0.45 * inch)

        self.text("Step 2 — ACT: What tool does it use and what does it do?", bold=True)
        self.multiline_field("", "story_act", 0.45 * inch)

        self.text("Step 3 — OBSERVE: What result does the agent see?", bold=True)
        self.multiline_field("", "story_observe", 0.45 * inch)

        self.text("Does the agent loop again? What happens next?", bold=True)
        self.multiline_field("", "story_loop", 0.45 * inch)

        self.space(0.05 * inch)

        self.text("HALLUCINATION MOMENT: Describe when the AI gets something wrong", bold=True)
        self.text("  and how the user catches it and corrects it.", size=9, indent=0.15 * inch)
        self.multiline_field("", "hallucination_moment", 0.55 * inch)

        self._draw_footer()

        # === PAGE 4: Presenter/Designer Worksheet (20 points) ===
        self.new_page()

        self.section_header("PRESENTER/DESIGNER — Build & Present (20 points)",
                           Colors.OBSERVE_GREEN)

        self.info_box(
            "Your Job",
            "Create visuals (slides, a poster, or a diagram) and lead the "
            "team's presentation. Make sure you include key vocabulary "
            "from our April-May lessons.",
            Colors.LIGHT_GREEN, 0.7 * inch
        )

        self.text("What format is your presentation? (slides, poster, skit, etc.)", bold=True)
        self.text_field("Format:", "pres_format", 0.7 * inch, 4 * inch)

        self.text("Which KEY VOCABULARY will you show on your visuals?", bold=True)
        self.text("Check at least 6:", size=9)
        self.space(0.05 * inch)
        self.checkbox("LLM / Large Language Model", "vocab_llm", 0.3 * inch)
        self.checkbox("Transformer", "vocab_transformer", 0.3 * inch)
        self.checkbox("Next-token prediction", "vocab_ntp", 0.3 * inch)
        self.checkbox("RTCF (Role/Task/Context/Format)", "vocab_rtcf", 0.3 * inch)
        self.checkbox("Meta prompting", "vocab_meta", 0.3 * inch)
        self.checkbox("Hallucination", "vocab_hallucination", 0.3 * inch)
        self.checkbox("AI Agent", "vocab_agent", 0.3 * inch)
        self.checkbox("Think -> Act -> Observe", "vocab_loop", 0.3 * inch)
        self.checkbox("Tools / Tool calls", "vocab_tools", 0.3 * inch)
        self.checkbox("Context window", "vocab_context", 0.3 * inch)
        self.checkbox("Temperature", "vocab_temp", 0.3 * inch)
        self.checkbox("Attention", "vocab_attention", 0.3 * inch)
        self.checkbox("Tokens", "vocab_tokens", 0.3 * inch)

        self.space(0.05 * inch)

        self.text("Outline your slides/visuals (what goes on each slide or section):", bold=True)
        self.multiline_field("", "pres_outline", 0.7 * inch)

        self.text("Presentation plan: Who says what? (practice notes)", bold=True)
        self.multiline_field("", "pres_plan", 0.6 * inch)

        self._draw_footer()

        # === PAGE 5: Team Review + Bonus (10 + 10 points) ===
        self.new_page()

        self.section_header("TEAM REVIEW — Put It All Together (10 points)",
                           Colors.PURPLE)

        self.text("Before you present, review as a team:", bold=True)
        self.space(0.05 * inch)

        self.checkbox("Our story includes the Think -> Act -> Observe loop", "check_loop", 0.2 * inch)
        self.checkbox("Our AI character has a system prompt written with RTCF", "check_rtcf", 0.2 * inch)
        self.checkbox("We included a hallucination moment and how to catch it", "check_hallucination", 0.2 * inch)
        self.checkbox("We mention at least 6 vocabulary terms from class", "check_vocab", 0.2 * inch)
        self.checkbox("Every team member has a speaking part", "check_speaking", 0.2 * inch)
        self.checkbox("We practiced and are ready to present (3-4 minutes)", "check_practice", 0.2 * inch)

        self.space(0.1 * inch)

        self.text("Team self-assessment: What is the BEST part of your project?", bold=True)
        self.multiline_field("", "team_best", 0.5 * inch)

        self.text("What would you improve if you had more time?", bold=True)
        self.multiline_field("", "team_improve", 0.5 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: Audience Feedback (+10 points)", Colors.AMBER)

        self.text("While watching other teams present, write feedback:", bold=True, size=9)
        self.space(0.05 * inch)

        self.text_field("Team presenting:", "feedback_team", 1.3 * inch, 3.5 * inch)
        self.text("One concept they explained really well:", bold=True, size=9)
        self.multiline_field("", "feedback_good", 0.4 * inch)
        self.text("One question you have about their presentation:", bold=True, size=9)
        self.multiline_field("", "feedback_question", 0.4 * inch)

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
                               "2026-05-16_Classwork_AI_Review_Group_Project.pdf")
    pdf = ClassworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
