"""
Challenge Classwork PDF Generator - May 23, 2026
AI Image & Multimodal Models — AI Image for a Purpose

For fast finishers: Design real-world deliverables (poster, logo,
book cover, social media graphic) using AI image generation.

Usage:
    py create_challenge_classwork_pdf.py

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
    CREATIVE_PINK = HexColor('#EC407A')
    LIGHT_PINK = HexColor('#F8BBD0')
    PROMPT_GOLD = HexColor('#FFB300')
    LIGHT_GOLD = HexColor('#FFF8E1')
    TEAL = HexColor('#009688')
    LIGHT_TEAL = HexColor('#B2DFDB')
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

class ChallengePDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Challenge Classwork: AI Image for a Purpose")
        self.page_num = 0
        self.total_pages = 3
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
        c.setFillColor(Colors.CREATIVE_PINK)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT - 4,
               Layout.WIDTH, 4, fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                    "CHALLENGE: AI Image for a Purpose")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Design Real-World Deliverables Using AI Image Generation")
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.WHITE)
        c.drawRightString(Layout.WIDTH - Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                         f"Page {self.page_num} of {self.total_pages}")

    def _draw_footer(self):
        c = self.c
        c.setFillColor(Colors.DARK_BLUE)
        c.rect(0, 0, Layout.WIDTH, Layout.FOOTER_HEIGHT, fill=True, stroke=False)
        c.setFillColor(Colors.CREATIVE_PINK)
        c.rect(0, Layout.FOOTER_HEIGHT, Layout.WIDTH, 3, fill=True, stroke=False)
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(Layout.MARGIN, 0.4 * inch, "SUBMISSION:")
        c.setFont("Helvetica", 9)
        c.drawString(1.4 * inch, 0.4 * inch,
                    "Submit to Ishwari Raut ma'am")
        c.drawString(Layout.MARGIN, 0.2 * inch,
                    "Challenge Classwork  |  Total Points: 100 (+10 bonus)")

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

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # -------------------------------------------------------------------------
    # Build
    # -------------------------------------------------------------------------

    def build(self):
        # === PAGE 1: Setup + Event Poster (30 points) ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.info_box(
            "Challenge: You're a Designer!",
            "You've been hired as a designer for a brand new company or event. "
            "Your job: create 4 real-world deliverables using only AI image tools. "
            "First, invent your company/event, then design for it!",
            Colors.LIGHT_PINK, 0.7 * inch
        )

        self.text_field("Your company/event name:", "brand_name", 2.2 * inch)
        self.text_field("What does it do? (1 sentence)", "brand_desc", 2.6 * inch)

        self.space(0.1 * inch)

        self.section_header("DELIVERABLE 1: Event Poster (30 points)",
                           Colors.CREATIVE_PINK)

        self.text("Create a poster that advertises your company/event.", bold=True, size=9)
        self.text("Think about: What's the mood? Who is the audience? What style fits?", size=9)
        self.space(0.05 * inch)

        self.multiline_field("Your prompt (include subject, style, mood, colors):",
                           "poster_prompt", 0.5 * inch)
        self.text_field("Art style chosen:", "poster_style", 1.5 * inch, 3 * inch)
        self.text_field("Rate the result (1-5):", "poster_rate", 1.8 * inch, 0.7 * inch)
        self.multiline_field("What worked? What would you change?",
                           "poster_reflect", 0.4 * inch)

        self._draw_footer()

        # === PAGE 2: Logo + Book/Album Cover (40 points) ===
        self.new_page()

        self.section_header("DELIVERABLE 2: Logo Design (20 points)",
                           Colors.PROMPT_GOLD)

        self.text("Create a logo for your company/event. Logos should be:", bold=True, size=9)
        self.text("simple, memorable, and work at small sizes. Try: 'minimalist logo, flat design'", size=9)
        self.space(0.05 * inch)

        self.multiline_field("Your prompt:", "logo_prompt", 0.45 * inch)
        self.text_field("Rate the result (1-5):", "logo_rate", 1.8 * inch, 0.7 * inch)
        self.multiline_field("Did it look like a real logo? Why or why not?",
                           "logo_reflect", 0.4 * inch)

        self.space(0.1 * inch)

        self.section_header("DELIVERABLE 3: Book or Album Cover (20 points)",
                           Colors.TEAL)

        self.text("Design a cover for a book or music album related to your brand.", bold=True, size=9)
        self.text("Think about: genre, target audience, visual storytelling, typography style.", size=9)
        self.space(0.05 * inch)

        self.text_field("Book or Album title:", "cover_title", 1.8 * inch)
        self.multiline_field("Your prompt:", "cover_prompt", 0.45 * inch)
        self.text_field("Rate the result (1-5):", "cover_rate", 1.8 * inch, 0.7 * inch)
        self.multiline_field("How does the image tell a story about your brand?",
                           "cover_reflect", 0.4 * inch)

        self._draw_footer()

        # === PAGE 3: Social Media + Reflection + Bonus ===
        self.new_page()

        self.section_header("DELIVERABLE 4: Social Media Post (10 points)",
                           Colors.PURPLE)

        self.text("Create an eye-catching image for Instagram/TikTok promoting your brand.", bold=True, size=9)
        self.text("Social media images need to: grab attention instantly, be colorful, tell a story fast.", size=9)
        self.space(0.05 * inch)

        self.multiline_field("Your prompt:", "social_prompt", 0.45 * inch)
        self.text_field("Platform (Instagram/TikTok/YouTube):", "social_platform", 3.0 * inch, 2.5 * inch)
        self.text_field("Rate the result (1-5):", "social_rate", 1.8 * inch, 0.7 * inch)

        self.space(0.1 * inch)

        self.section_header("REFLECTION: Designer Review (10 points)",
                           Colors.MEDIUM_BLUE)

        self.text("Q1: Which deliverable turned out best? What made that prompt work?", bold=True, size=9)
        self.multiline_field("", "reflect_best", 0.4 * inch)

        self.text("Q2: What's hard about designing with AI vs. doing it yourself?", bold=True, size=9)
        self.multiline_field("", "reflect_hard", 0.4 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: Client Presentation (+10 points)",
                           Colors.AMBER)

        self.text("Write a 2-3 sentence 'pitch' explaining your brand and how AI helped", bold=True, size=9)
        self.text("you create the visuals. Pretend you're presenting to the client!", size=9)
        self.multiline_field("", "bonus_pitch", 0.5 * inch)

        self._draw_footer()

        self.c.save()
        print(f"[SUCCESS] Challenge Classwork PDF created: {self.output_path}")
        return self.output_path


# =============================================================================
# MAIN
# =============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir,
                               "2026-05-23_Challenge_AI_Image_for_a_Purpose.pdf")
    pdf = ChallengePDF(output_path)
    pdf.build()
    return output_path


if __name__ == "__main__":
    main()
