"""
Homework PDF Generator - May 23, 2026
AI Image & Multimodal Models — Image Explorer

Individual homework: students explore image generation at home,
experiment with prompts, test multimodal understanding, and reflect
on ethics.

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


# =============================================================================
# PDF BUILDER
# =============================================================================

class HomeworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Homework: AI Image Explorer")
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
                    "HOMEWORK: AI Image Explorer")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "AI Image & Multimodal Models — Explore, Create, and Think Critically")
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
        # === PAGE 1: Student Info + Vocabulary Match (20 points) ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "hw_name", 0.55 * inch)
        self.text_field("Date:", "hw_date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.section_header("SECTION 1: Vocabulary Match (20 points)",
                           Colors.IMAGE_PURPLE)

        self.text("Match each term with its definition. Write the letter in the box.",
                 bold=True)
        self.space(0.08 * inch)

        self.text("A. AI model that creates pictures from text descriptions", size=9)
        self.text("B. The process of removing noise step by step to create an image", size=9)
        self.text("C. AI that works with multiple types of data (text + image + audio)", size=9)
        self.text("D. AI-generated fake image or video of a real person", size=9)
        self.text("E. The text description you give to an image generator", size=9)
        self.text("F. How AI starts with random static and sculpts it into a picture", size=9)
        self.text("G. Applying one artistic style to another image", size=9)
        self.text("H. AI that can look at a photo and answer questions about it", size=9)

        self.space(0.08 * inch)

        self.text_field("1. Text-to-Image:", "match_1", 1.8 * inch, 0.5 * inch)
        self.text_field("2. Diffusion:", "match_2", 1.8 * inch, 0.5 * inch)
        self.text_field("3. Multimodal:", "match_3", 1.8 * inch, 0.5 * inch)
        self.text_field("4. Deepfake:", "match_4", 1.8 * inch, 0.5 * inch)
        self.text_field("5. Image Prompt:", "match_5", 1.8 * inch, 0.5 * inch)
        self.text_field("6. Noise-to-Image:", "match_6", 1.8 * inch, 0.5 * inch)
        self.text_field("7. Style Transfer:", "match_7", 1.8 * inch, 0.5 * inch)
        self.text_field("8. Vision AI:", "match_8", 1.8 * inch, 0.5 * inch)

        self._draw_footer()

        # === PAGE 2: True/False + Short Answer (30 points) ===
        self.new_page()

        self.section_header("SECTION 2: True or False (10 points)",
                           Colors.DIFFUSION_BLUE)

        self.text("Write T (True) or F (False) in each box.", bold=True)
        self.space(0.05 * inch)

        self.text_field("1. AI image models copy real photos from the internet.",
                       "tf_1", 5.5 * inch, 0.4 * inch)
        self.text_field("2. Diffusion works by removing noise step by step.",
                       "tf_2", 5.5 * inch, 0.4 * inch)
        self.text_field("3. A more detailed prompt usually gives a better image.",
                       "tf_3", 5.5 * inch, 0.4 * inch)
        self.text_field("4. Multimodal AI can only understand text, not images.",
                       "tf_4", 5.5 * inch, 0.4 * inch)
        self.text_field("5. It is always okay to make AI images of real people.",
                       "tf_5", 5.5 * inch, 0.4 * inch)
        self.text_field("6. AI-generated images can have mistakes like extra fingers.",
                       "tf_6", 5.5 * inch, 0.4 * inch)
        self.text_field("7. DALL-E, Midjourney, and Stable Diffusion are text-to-image models.",
                       "tf_7", 5.5 * inch, 0.4 * inch)
        self.text_field("8. You should always trust photos you see online.",
                       "tf_8", 5.5 * inch, 0.4 * inch)

        self.space(0.1 * inch)

        self.section_header("SECTION 3: Short Answer (20 points)",
                           Colors.MULTIMODAL_TEAL)

        self.text("Answer each question in 2-3 sentences.", bold=True)
        self.space(0.05 * inch)

        self.text("1. Explain how diffusion creates an image. Use an analogy", bold=True, size=9)
        self.text("   (like sculpting, cleaning fog, or developing a photo).", size=9)
        self.multiline_field("", "sa_1", 0.55 * inch)

        self.text("2. What is the difference between a text-to-image model and a", bold=True, size=9)
        self.text("   multimodal model? Give an example of each.", size=9)
        self.multiline_field("", "sa_2", 0.55 * inch)

        self.text("3. How is prompting for images different from prompting for text?", bold=True, size=9)
        self.text("   What details should you include in an image prompt?", size=9)
        self.multiline_field("", "sa_3", 0.55 * inch)

        self._draw_footer()

        # === PAGE 3: Applied Scenarios (30 points) ===
        self.new_page()

        self.section_header("SECTION 4: Applied Scenarios (30 points)",
                           Colors.PROMPT_GOLD)

        self.text("Scenario A: Prompt Improvement", bold=True)
        self.text("Your friend typed: 'make a cat picture'. Rewrite this as a GREAT", size=9)
        self.text("image prompt that includes subject, style, lighting, and mood.", size=9)
        self.multiline_field("Your improved prompt:", "scenario_a", 0.55 * inch)

        self.text("Scenario B: Real vs. Fake", bold=True)
        self.text("You see a news photo of a celebrity doing something shocking.", size=9)
        self.text("List 3 steps you would take to check if it's real or AI-generated.", size=9)
        self.multiline_field("", "scenario_b", 0.55 * inch)

        self.text("Scenario C: Right Tool for the Job", bold=True)
        self.text("For each task, write whether you need: text-to-image, multimodal, or a text LLM.", size=9)
        self.space(0.05 * inch)
        self.text_field("Create a poster for a school event:", "task_1", 3.0 * inch, 2.5 * inch)
        self.text_field("Ask AI to describe what's in a photo:", "task_2", 3.0 * inch, 2.5 * inch)
        self.text_field("Write an essay about climate change:", "task_3", 3.0 * inch, 2.5 * inch)
        self.text_field("Turn a sketch into a realistic image:", "task_4", 3.0 * inch, 2.5 * inch)

        self.space(0.05 * inch)

        self.text("Scenario D: Ethical Dilemma", bold=True)
        self.text("A friend wants to create a funny AI image of their teacher.", size=9)
        self.text("Is this okay? What would you tell them? (3 sentences)", size=9)
        self.multiline_field("", "scenario_d", 0.55 * inch)

        self._draw_footer()

        # === PAGE 4: Creative Challenge + Bonus (20 + 10 points) ===
        self.new_page()

        self.section_header("SECTION 5: Creative Challenge (20 points)",
                           Colors.CREATIVE_PINK)

        self.info_box(
            "Your Mission: Build a Prompt Collection",
            "Create 3 image prompts for different purposes. For each one, write "
            "the prompt, say what style and mood you chose, then actually try it "
            "on an AI tool and describe the result.",
            Colors.LIGHT_PURPLE, 0.7 * inch
        )

        self.text("Prompt 1 — For a school project or presentation:", bold=True, size=9)
        self.text_field("Prompt:", "creative_p1", 0.7 * inch)
        self.text_field("Style/Mood:", "creative_s1", 1.0 * inch, 3 * inch)
        self.multiline_field("Result (describe or rate 1-5):", "creative_r1", 0.35 * inch)

        self.text("Prompt 2 — Pure creativity (fantasy, sci-fi, anything!):", bold=True, size=9)
        self.text_field("Prompt:", "creative_p2", 0.7 * inch)
        self.text_field("Style/Mood:", "creative_s2", 1.0 * inch, 3 * inch)
        self.multiline_field("Result:", "creative_r2", 0.35 * inch)

        self.text("Prompt 3 — A real-world use (logo, room design, outfit idea):", bold=True, size=9)
        self.text_field("Prompt:", "creative_p3", 0.7 * inch)
        self.text_field("Style/Mood:", "creative_s3", 1.0 * inch, 3 * inch)
        self.multiline_field("Result:", "creative_r3", 0.35 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: AI Art Gallery (+10 points)", Colors.AMBER)

        self.text("Pick your BEST generated image from this homework. Describe it and", bold=True, size=9)
        self.text("explain what made the prompt work so well. What would you change?", size=9)
        self.multiline_field("", "bonus_gallery", 0.5 * inch)

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
                               "2026-05-23_Homework_AI_Image_Explorer.pdf")
    pdf = HomeworkPDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
