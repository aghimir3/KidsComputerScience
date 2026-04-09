"""
Classwork PDF Generator - February 7, 2026
Internet Pathfinder: How the Internet Connects Everything

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
    LIGHT_GRAY = HexColor('#F5F5F5')
    DARK_GRAY = HexColor('#424242')
    WHITE = HexColor('#FFFFFF')
    OCEAN_BLUE = HexColor('#006699')
    CABLE_BLUE = HexColor('#0078D4')


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
        self.page_num = 0
        self.total_pages = 6
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
                    "CLASSWORK: Internet Pathfinder")

        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Mission: Track how the internet connects the world")

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
            letter = chr(65 + i)

            c.acroForm.checkbox(
                name=f"{field_name}_{letter}",
                x=Layout.MARGIN + 0.2 * inch,
                y=self.y - 2,
                size=11,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.WHITE,
            )

            c.setFont("Helvetica", 10)
            c.setFillColor(Colors.DARK_GRAY)
            c.drawString(Layout.MARGIN + 0.2 * inch + 15, self.y, f"{letter}) {option}")
            self.y -= 0.2 * inch

        self.y -= 0.08 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # -------------------------------------------------------------------------
    # Build
    # -------------------------------------------------------------------------

    def build(self):
        # === PAGE 1: Student Info + Review ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.1 * inch)

        self.info_box(
            "Your Mission Today",
            "You are an Internet Pathfinder! You will trace how data travels from your device to the world using ISPs, backbones, and cables.",
            Colors.LIGHT_BLUE, 0.7 * inch
        )

        self.space(0.1 * inch)

        self.section_header("QUICK REVIEW: Cloud & Data Centers (10 points)", Colors.ORANGE)

        self.multiple_choice("The cloud is...", [
            "Magic computers in the sky",
            "Servers in data centers",
            "A type of browser",
            "A phone app"
        ], "review_q1", 1)

        self.multiple_choice("A data center is...", [
            "A building full of servers",
            "A USB drive",
            "A Wi-Fi password",
            "A game server only"
        ], "review_q2", 2)

        self.multiple_choice("Your device sends requests to a...", [
            "Client",
            "Server",
            "Router brand",
            "Cable"
        ], "review_q3", 3)

        # === PAGE 2: ISPs ===
        self.new_page()

        self.section_header("PART 1: ISPs (20 points)", Colors.GREEN)

        self.text("Q1: What does ISP stand for?", bold=True)
        self.text_field("Answer:", "isp_full", 0.8 * inch)

        self.space(0.1 * inch)

        self.text("Q2: Write two ISP names you know (USA):", bold=True)
        self.text_field("ISP 1:", "isp_1", 0.6 * inch)
        self.text_field("ISP 2:", "isp_2", 0.6 * inch)

        self.space(0.1 * inch)

        self.text("Q3: Which part is usually the FIRST hop?", bold=True)
        self.multiple_choice("", [
            "Data center",
            "Your ISP",
            "An undersea cable",
            "A CDN cache"
        ], "isp_first_hop")

        self.space(0.1 * inch)

        self.text("Q4: Why do we need ISPs?", bold=True)
        self.multiline_field("", "isp_reason", 0.6 * inch)

        # === PAGE 3: Backbones and Cables ===
        self.new_page()

        self.section_header("PART 2: Backbones & Cables (20 points)", Colors.CABLE_BLUE)

        self.text("Q5: Complete the sentence:", bold=True)
        self.text("Internet backbones are super-fast __________ highways.")
        self.text_field("Word:", "backbone_word", 0.7 * inch, 1.5 * inch)

        self.space(0.1 * inch)

        self.text("Q6: What do undersea cables connect?", bold=True)
        self.multiple_choice("", [
            "Cities to neighborhoods",
            "Continents to continents",
            "Phones to routers",
            "Games to consoles"
        ], "cables_connect")

        self.space(0.1 * inch)

        self.text("Q7: Why are undersea cables important?", bold=True)
        self.multiline_field("", "cables_important", 0.6 * inch)

        self.space(0.1 * inch)

        self.text("Q8: What is a cable landing point?", bold=True)
        self.multiline_field("", "landing_point", 0.6 * inch)

        # === PAGE 4: IXPs and CDNs ===
        self.new_page()

        self.section_header("PART 3: IXPs & CDNs (20 points)", Colors.ORANGE)

        self.info_box(
            "CDN Examples",
            "CDNs speed up YouTube, Netflix, TikTok, Spotify, game updates, and school websites by storing copies nearby.",
            Colors.LIGHT_GRAY, 0.6 * inch
        )

        self.text("Q9: Match each term to its meaning:", bold=True)
        self.space(0.05 * inch)

        terms = [
            ("IXP", "ixp_meaning"),
            ("CDN", "cdn_meaning"),
            ("ISP", "isp_meaning"),
        ]

        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(Colors.DARK_GRAY)
        self.c.drawString(Layout.MARGIN + 3.9 * inch, self.y + 0.15 * inch,
                         "Options: Content Delivery Network, Meeting place for networks, Your internet provider")
        self.y -= 0.1 * inch

        for term, field_name in terms:
            self.text(f"{term}:", indent=0.2 * inch)
            self.text_field("Meaning:", field_name, 1.0 * inch, 3.5 * inch)

        self.space(0.05 * inch)

        self.text("Q10: CDN or Not? Check the correct box.", bold=True)
        self.space(0.05 * inch)

        scenarios = [
            ("A nearby server stores a copy of a video", "cdn_yes1", "cdn_no1"),
            ("A cable under the ocean connects two countries", "cdn_yes2", "cdn_no2"),
            ("Images load fast because they are stored near your city", "cdn_yes3", "cdn_no3"),
        ]

        for text, yes_name, no_name in scenarios:
            self.c.setFont("Helvetica", 9)
            self.c.setFillColor(Colors.DARK_GRAY)
            self.c.drawString(Layout.MARGIN, self.y, text)

            self.c.acroForm.checkbox(
                name=yes_name,
                x=Layout.MARGIN + 4.2 * inch,
                y=self.y - 2,
                size=11,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.WHITE,
            )
            self.c.drawString(Layout.MARGIN + 4.2 * inch + 15, self.y, "CDN")

            self.c.acroForm.checkbox(
                name=no_name,
                x=Layout.MARGIN + 5.2 * inch,
                y=self.y - 2,
                size=11,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.WHITE,
            )
            self.c.drawString(Layout.MARGIN + 5.2 * inch + 15, self.y, "Not CDN")

            self.y -= 0.28 * inch

        # === PAGE 5: Latency and Speed ===
        self.new_page()

        self.section_header("PART 4: Speed & Latency (20 points)", Colors.PURPLE)

        self.text("Q11: What does latency mean?", bold=True)
        self.multiline_field("", "latency_meaning", 0.6 * inch)

        self.space(0.1 * inch)

        self.text("Q12: Which is usually faster?", bold=True)
        self.multiple_choice("", [
            "A nearby server",
            "A server across the ocean",
            "They are always the same",
            "It depends only on your phone"
        ], "latency_fast")

        self.space(0.1 * inch)

        self.text("Q13: List two reasons the internet can feel slow:", bold=True)
        self.text_field("1.", "slow_reason_1", 0.3 * inch)
        self.text_field("2.", "slow_reason_2", 0.3 * inch)

        self.space(0.1 * inch)

        self.text("Q14: Which part helps speed up videos?", bold=True)
        self.multiple_choice("", [
            "CDN",
            "Undersea cable",
            "Laptop battery",
            "Keyboard"
        ], "cdn_speed")

        self.space(0.05 * inch)

        self.text("Q15: Why does AI need fast physical internet?", bold=True)
        self.multiple_choice("", [
            "AI runs in faraway data centers and needs quick connections",
            "AI only works without cables",
            "AI lives inside phones",
            "AI does not need the internet"
        ], "ai_physical")

        # === PAGE 6: Map Explorer + Bonus ===
        self.new_page()

        self.section_header("PART 5: Map Explorer (10 points)", Colors.OCEAN_BLUE)

        self.info_box(
            "Map Task",
            "Go to submarinecablemap.com and click on any cable. Write the cable name and the two places it connects.",
            Colors.LIGHT_GRAY, 0.6 * inch
        )

        self.text_field("Cable name:", "cable_name", 1.0 * inch)
        self.text_field("Place 1:", "cable_place_1", 0.7 * inch)
        self.text_field("Place 2:", "cable_place_2", 0.7 * inch)

        self.space(0.1 * inch)

        self.section_header("REFLECTION (10 points)", Colors.MEDIUM_BLUE)
        self.text("What surprised you most about how the internet connects the world?", bold=True)
        self.multiline_field("", "reflection", 0.7 * inch)

        self.section_header("BONUS: Internet Path (+10 points)", Colors.ORANGE)
        self.text("Draw or describe the path from your device to a video website.", bold=True)
        self.multiline_field("", "bonus_path", 0.8 * inch)

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
    output_path = os.path.join(parent_dir, "2026-02-07_Classwork_Internet_Pathfinder.pdf")

    pdf = ClassworkPDF(output_path)
    pdf.build()

    return output_path


if __name__ == "__main__":
    main()
