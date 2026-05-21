"""
Classwork PDF Generator - May 23, 2026
AI Image & Multimodal Models — Image Lab

Students generate images with AI, compare prompts, test multimodal
understanding, and evaluate AI-generated vs. real images.

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
    IMAGE_PURPLE = HexColor('#7E57C2')
    DIFFUSION_BLUE = HexColor('#2196F3')
    MULTIMODAL_TEAL = HexColor('#009688')
    ETHICS_RED = HexColor('#E53935')
    CREATIVE_PINK = HexColor('#EC407A')
    PROMPT_GOLD = HexColor('#FFB300')
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
        self.c.setTitle("Classwork: AI Image Lab")
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
                    "CLASSWORK: AI Image Lab")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "AI Image & Multimodal Models — Generate, Compare, and Evaluate")
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
        # === PAGE 1: Setup + Prompt Battle (30 points) ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.section_header("SECTION 1: Prompt Battle — Vague vs. Detailed (30 points)",
                           Colors.IMAGE_PURPLE)

        self.info_box(
            "Your Mission",
            "Generate the SAME image idea twice: once with a vague prompt and "
            "once with a detailed prompt. See how much better specific prompts work! "
            "Use ChatGPT (chat.openai.com), Gemini (gemini.google.com), or another tool.",
            Colors.LIGHT_PURPLE, 0.7 * inch
        )

        self.text_field("AI tool used:", "tool_used", 1.1 * inch, 3.5 * inch)

        self.space(0.05 * inch)
        self.text("Round 1: VAGUE prompt (keep it short and generic)", bold=True)
        self.text_field("Your vague prompt:", "vague_prompt", 1.5 * inch)
        self.multiline_field("Describe what the AI generated (or paste a screenshot later):",
                           "vague_result", 0.45 * inch)

        self.text("Round 2: DETAILED prompt (subject, style, lighting, mood)", bold=True)
        self.text_field("Your detailed prompt:", "detailed_prompt", 1.6 * inch)
        self.multiline_field("Describe what the AI generated:",
                           "detailed_result", 0.45 * inch)

        self.text("Which image was better? Why? (2 sentences)", bold=True, size=9)
        self.multiline_field("", "compare_prompts", 0.45 * inch)

        self._draw_footer()

        # === PAGE 2: Multimodal Challenge (30 points) ===
        self.new_page()

        self.section_header("SECTION 2: Multimodal Challenge (30 points)",
                           Colors.MULTIMODAL_TEAL)

        self.info_box(
            "What is Multimodal?",
            "Multimodal AI can understand BOTH text and images. You can upload "
            "a photo and ask it questions! Let's test this.",
            Colors.LIGHT_GREEN, 0.55 * inch
        )

        self.text("Task A: Upload any photo to ChatGPT or Gemini and ask a question.", bold=True)
        self.text("(Use a photo from your camera roll, a screenshot, or find one online)", size=9)
        self.space(0.05 * inch)

        self.text_field("What photo did you upload?", "photo_desc", 2.2 * inch)
        self.text_field("What question did you ask?", "photo_question", 2.2 * inch)
        self.multiline_field("What did the AI answer? Was it correct?",
                           "photo_answer", 0.5 * inch)

        self.space(0.05 * inch)

        self.text("Task B: Test the AI's limits — upload something tricky!", bold=True)
        self.text("(e.g., handwritten notes, a meme, a blurry photo, something in another language)", size=9)
        self.space(0.05 * inch)

        self.text_field("What tricky image did you use?", "tricky_desc", 2.5 * inch)
        self.multiline_field("How did the AI do? Did it understand correctly or get confused?",
                           "tricky_result", 0.5 * inch)

        self.space(0.05 * inch)

        self.text("Task C: What types of images do you think AI is BEST at understanding?", bold=True)
        self.text("What types would be HARDEST? (2-3 sentences)", size=9)
        self.multiline_field("", "multimodal_limits", 0.5 * inch)

        self._draw_footer()

        # === PAGE 3: Real vs. AI Detective (25 points) ===
        self.new_page()

        self.section_header("SECTION 3: Real vs. AI Detective (25 points)",
                           Colors.ETHICS_RED)

        self.info_box(
            "Can You Spot the Fake?",
            "AI-generated images are getting better every day. Go to "
            "whichfaceisreal.com and play 5 rounds. For each round, write "
            "which face you picked and whether you were right or wrong.",
            Colors.LIGHT_RED, 0.7 * inch
        )

        # Image evaluations
        for i in range(1, 6):
            self.text(f"Round {i}:", bold=True, size=10)
            self.text_field("Which did you pick? (Left/Right)", f"image_{i}_guess", 2.5 * inch, 2 * inch)
            self.text_field("Were you correct?", f"image_{i}_why", 1.5 * inch, 2.5 * inch)
            self.space(0.05 * inch)

        self.space(0.05 * inch)
        self.text("What clues help you tell the difference? List at least 3:", bold=True, size=9)
        self.multiline_field("", "detection_clues", 0.5 * inch)

        self._draw_footer()

        # === PAGE 4: Reflection + Ethics + Bonus (15 + 10 points) ===
        self.new_page()

        self.section_header("SECTION 4: Ethics & Reflection (15 points)",
                           Colors.PURPLE)

        self.text("Q1: Why is it dangerous to create fake images of real people?", bold=True, size=9)
        self.multiline_field("", "ethics_q1", 0.5 * inch)

        self.text("Q2: A classmate finds a shocking news photo online. How should", bold=True, size=9)
        self.text("they verify if it's real or AI-generated? (name 2 steps)", size=9, indent=0.3 * inch)
        self.multiline_field("", "ethics_q2", 0.5 * inch)

        self.text("Q3: Name one GOOD use and one BAD use of AI image generation.", bold=True, size=9)
        self.multiline_field("", "ethics_q3", 0.5 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: Creative Prompt Challenge (+10 points)",
                           Colors.AMBER)

        self.text("Write the most creative, detailed image prompt you can think of.", bold=True, size=9)
        self.text("Include: subject, setting, art style, lighting, mood, and one surprising element.", size=9)
        self.multiline_field("Your masterpiece prompt:", "bonus_prompt", 0.6 * inch)
        self.multiline_field("What did the AI create? Rate it 1-5 and explain:",
                           "bonus_result", 0.5 * inch)

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
                               "2026-05-23_Classwork_AI_Image_Lab.pdf")
    pdf = ClassworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
