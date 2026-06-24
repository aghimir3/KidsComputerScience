"""
Classwork PDF Generator - June 27, 2026
Your Own AI Assistant (OpenClaw) - LAST DAY of the AI unit

Usage:
    python create_classwork_pdf.py

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
    TEAL = HexColor('#00897B')
    SAFE_GREEN = HexColor('#388E3C')


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

class ClassworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Classwork: Your Own AI Assistant (OpenClaw)")
        self.page_num = 0
        self.total_pages = 4
        self.y = Layout.CONTENT_TOP

    # ----- core drawing -----
    def new_page(self):
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1
        self._draw_header()
        self._draw_footer()
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
        c.setFont("Helvetica-Bold", 17)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                     "CLASSWORK: Your Own AI Assistant")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                     "Run a real AI with OpenClaw + OpenRouter  \u00b7  Last day of the AI unit!")
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

    # ----- section helpers -----
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
        lines, current = [], ""
        max_width = Layout.CONTENT_WIDTH - 0.4 * inch
        for word in words:
            test = current + " " + word if current else word
            if stringWidth(test, "Helvetica", 9) < max_width:
                current = test
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        text_y = self.y - 0.38 * inch
        for line in lines[:4]:
            c.drawString(Layout.MARGIN + 0.15 * inch, text_y, line)
            text_y -= 0.16 * inch
        self.y -= height + 0.1 * inch

    def text(self, content, bold=False, size=10, indent=0):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        c.drawString(Layout.MARGIN + indent, self.y, content)
        self.y -= (size + 6)

    def prompt_box(self, prompt, height=0.34 * inch):
        """A monospace 'type this' box."""
        c = self.c
        c.setFillColor(Colors.LIGHT_GRAY)
        c.setStrokeColor(Colors.TEAL)
        c.roundRect(Layout.MARGIN + 0.1 * inch, self.y - height,
                    Layout.CONTENT_WIDTH - 0.2 * inch, height, 5, fill=True, stroke=True)
        c.setFillColor(Colors.DARK_BLUE)
        c.setFont("Courier-Bold", 9)
        c.drawString(Layout.MARGIN + 0.28 * inch, self.y - height + 0.12 * inch, prompt)
        self.y -= height + 0.1 * inch

    def text_field(self, label, field_name, label_width=1.3 * inch,
                   field_width=None, height=0.25 * inch):
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN, self.y, label)
        field_x = Layout.MARGIN + label_width
        actual_width = (Layout.WIDTH - Layout.MARGIN - field_x) if field_width is None else field_width
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
            name=field_name, x=Layout.MARGIN, y=self.y - height + 0.08 * inch,
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
            size=13, borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.WHITE,
            buttonStyle='check',
        )
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN + x_offset + 18, self.y, label)
        self.y -= 0.23 * inch

    def multiple_choice(self, question, options, field_name, q_num=None):
        c = self.c
        if question:
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
                size=11, borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.WHITE,
            )
            c.setFont("Helvetica", 10)
            c.setFillColor(Colors.DARK_GRAY)
            c.drawString(Layout.MARGIN + 0.2 * inch + 15, self.y, f"{letter_char}) {option}")
            self.y -= 0.2 * inch
        self.y -= 0.08 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # ----- build -----
    def build(self):
        # === PAGE 1: Setup check + Mission A ===
        self.new_page()
        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)
        self.text_field("Group:", "group_name", 0.7 * inch, 3 * inch)

        self.info_box(
            "Your Mission Today",
            "Today you run a REAL AI assistant on your own computer with OpenClaw! Give it missions, watch it work, teach it about you, and keep it SAFE. Pick a Driver and switch each mission.",
            Colors.LIGHT_BLUE, 0.72 * inch
        )

        self.section_header("Setup Check (5 points)", Colors.SAFE_GREEN)
        self.text("Tick these off as a group before Mission A:", bold=True)
        self.checkbox("Node.js is installed (node --version shows 22 or higher)", "set_node")
        self.checkbox("OpenClaw is installed (openclaw --version works)", "set_install")
        self.checkbox("Onboarded with OpenRouter using the class key", "set_key")
        self.checkbox("Model set to DeepSeek V4 Flash", "set_model")
        self.checkbox("Gateway is running in one terminal (openclaw gateway)", "set_gateway")
        self.checkbox("You got a reply in 'openclaw chat'", "set_chat")

        self.space(0.05 * inch)
        self.section_header("Mission A - First Contact (15 points)", Colors.MEDIUM_BLUE)
        self.text("In 'openclaw chat', type this to your assistant:", bold=True)
        self.prompt_box("Introduce yourself in two sentences. What can you help me with?")
        self.multiline_field("What did your assistant say?", "a_intro", 0.55 * inch)
        self.text_field("Does it have a name or model? (ask if not):", "a_name", 3.4 * inch)

        # === PAGE 2: Mission B + Mission C ===
        self.new_page()
        self.section_header("Mission B - Watch It Act (20 points)", Colors.MEDIUM_BLUE)
        self.text("Now give it a real task. Type this:", bold=True)
        self.prompt_box("Make a file called space.txt with one cool fact about space.")
        self.text("Watch closely: it will ASK permission before it does anything.", bold=True)
        self.multiple_choice("When it asked to run a command, did you...",
                             ["Approve (after reading it)", "Deny"], "b_choice")
        self.text_field("What command did it ask to run?", "b_cmd", 3.0 * inch)
        self.multiline_field("Did the file get made? What was inside it?", "b_result", 0.5 * inch)
        self.info_box(
            "Concept: 'ask' mode",
            "Your assistant didn't just talk -- it ACTED on your computer. And it asked first! That 'approve / deny' step is called ask mode. Always read the command before you approve.",
            Colors.LIGHT_GREEN, 0.66 * inch
        )

        self.section_header("Mission C - Give It a Personality (15 points)", Colors.PURPLE)
        self.text("Make your assistant your own. Pick a name and a vibe, then type:", bold=True)
        self.prompt_box("From now on your name is Nova, a cheerful helper. Re-introduce yourself.")
        self.text_field("What did you name your assistant?", "c_name", 3.2 * inch)
        self.multiline_field("How did its replies change after you gave it a personality?",
                             "c_change", 0.5 * inch)

        # === PAGE 3: Mission D + Mission E ===
        self.new_page()
        self.section_header("Mission D - Make It Remember (15 points)", Colors.TEAL)
        self.text("Tell your assistant a fact about your group:", bold=True)
        self.prompt_box("Remember: my team is the Sharks and our favorite game is Minecraft.")
        self.text("Then, in the SAME chat, ask:", bold=True)
        self.prompt_box("What is my team's name and our favorite game?")
        self.multiline_field("Did it remember? What did it say?", "d_recall", 0.5 * inch)
        self.text("Bonus: ask it to SAVE that to its memory so it knows next time, too!", bold=True)
        self.text_field("Did it save your fact to memory? (yes/no):", "d_saved", 3.2 * inch)

        self.section_header("Mission E - Interview Your Assistant (15 points)", Colors.GREEN)
        self.text("Ask your assistant how it works. Write its answers in your own words.", bold=True)
        self.prompt_box("In 2-3 sentences, how do you remember things about me?")
        self.multiline_field("Memory - in your own words:", "e_memory", 0.45 * inch)
        self.prompt_box("What is an API key, and why should I keep it secret?")
        self.multiline_field("API key - in your own words:", "e_key", 0.45 * inch)
        self.prompt_box("Before running a command on my computer, what do you do first?")
        self.text_field("It said it first:", "e_approve", 3.6 * inch)

        # === PAGE 4: Mission F + Reflection + Bonus ===
        self.new_page()
        self.section_header("Mission F - Quick Quests (10 points)", Colors.ORANGE)
        self.text("Do as many as you can. Check the box when your group finishes one!", bold=True)
        self.checkbox("Ask it to make jokes.txt with 3 kid-friendly jokes", "f_jokes")
        self.checkbox("Ask it to write a 4-line poem about robots and save it", "f_poem")
        self.checkbox("Ask it to make a weekend to-do list file", "f_todo")
        self.checkbox("Ask it to make a study plan for your favorite subject", "f_study")
        self.checkbox("Ask it to list every file in your folder", "f_list")
        self.multiline_field("Which quest was your favorite, and what did it make?",
                             "f_fav", 0.5 * inch)

        self.section_header("Reflection (5 points)", Colors.MEDIUM_BLUE)
        self.text("What was the coolest thing your assistant did today? Why?", bold=True)
        self.multiline_field("", "r_cool", 0.5 * inch)

        self.section_header("BONUS: Design Your Dream Assistant (+10 points)", Colors.ORANGE)
        self.info_box(
            "Bonus Challenge",
            "If you had an AI assistant at home, what would it do for you? Design it below -- and remember one safety rule, since assistants are powerful!",
            Colors.LIGHT_GRAY, 0.6 * inch
        )
        self.text_field("Assistant's name:", "bonus_name", 1.5 * inch)
        self.text_field("One job it does for you:", "bonus_job", 2.0 * inch)
        self.text_field("One safety rule it follows:", "bonus_rule", 2.2 * inch)

        self.c.save()
        print(f"[SUCCESS] Classwork PDF created: {self.output_path}")
        return self.output_path


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-06-27_Classwork_Your_AI_Assistant.pdf")
    pdf = ClassworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
