"""
Homework PDF Generator - February 7, 2026
Internet Connection Detective

Usage:
    python create_homework_pdf.py

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
    LIGHT_GRAY = HexColor('#F5F5F5')
    DARK_GRAY = HexColor('#424242')
    WHITE = HexColor('#FFFFFF')
    OCEAN_BLUE = HexColor('#006699')


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
                    "HOMEWORK: Internet Connection Detective")

        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Track how your internet connects to the world")

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

    # -------------------------------------------------------------------------
    # Helpers
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
        # === PAGE 1: Student Info + Overview ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.1 * inch)

        self.info_box(
            "Homework Goal",
            "Find clues about your own internet connection and explain how data travels to the world.",
            Colors.LIGHT_BLUE, 0.7 * inch
        )

        self.section_header("PART 1: Your Home Internet (25 points)", Colors.GREEN)

        self.text("Q1: Who is your home internet provider (ISP)?", bold=True)
        self.text_field("Provider:", "hw_isp_name", 0.8 * inch)
        self.text("(If unsure, ask a parent/guardian or check a bill/app.)", size=9)

        self.space(0.1 * inch)

        self.text("Q2: Is your home internet connected by...", bold=True)
        self.checkbox("Cable", "hw_conn_cable")
        self.checkbox("Fiber", "hw_conn_fiber")
        self.checkbox("DSL", "hw_conn_dsl")
        self.checkbox("Fixed Wireless", "hw_conn_wireless")
        self.checkbox("Not sure", "hw_conn_unknown")

        self.space(0.1 * inch)

        self.text("Q3: Imagine your ISP went offline for a whole day.", bold=True)
        self.text("What would stop working at your house?", size=10)
        self.multiline_field("", "hw_isp_offline", 0.6 * inch)

        # === PAGE 2: Real-World Research ===
        self.new_page()

        self.section_header("PART 2: Undersea Cable Research (25 points)", Colors.OCEAN_BLUE)

        self.info_box(
            "Research Task",
            "Go to submarinecablemap.com, pick one cable, and answer the questions below.",
            Colors.LIGHT_GRAY, 0.55 * inch
        )

        self.text("Q4: What is the name of the cable you picked?", bold=True)
        self.text_field("Cable name:", "hw_cable_name", 1.0 * inch)

        self.space(0.05 * inch)

        self.text("Q5: What two places does it connect?", bold=True)
        self.text_field("Place 1:", "hw_cable_p1", 0.7 * inch)
        self.text_field("Place 2:", "hw_cable_p2", 0.7 * inch)

        self.space(0.05 * inch)

        self.text("Q6: Why is this cable important? What would happen", bold=True)
        self.text("if it broke? (Think about what countries or services it connects.)")
        self.multiline_field("", "hw_cable_importance", 0.7 * inch)

        self.space(0.05 * inch)

        self.text("Q7: Trace the journey when you ask ChatGPT a question.", bold=True)
        self.text("Describe the path from your device to the AI and back. Use words")
        self.text("like ISP, backbone, data center, and undersea cable.")
        self.multiline_field("", "hw_chatgpt_trace", 0.8 * inch)

        # === PAGE 3: Speed Scenarios ===
        self.new_page()

        self.section_header("PART 3: Speed & Latency Scenarios (25 points)", Colors.PURPLE)

        self.text("Q8: Your favorite online game is lagging badly.", bold=True)
        self.text("Using what you know about ISPs, backbones, and CDNs,")
        self.text("what could be causing the lag?")
        self.multiline_field("", "hw_lag_causes", 0.7 * inch)

        self.space(0.1 * inch)

        self.text("Q9: A friend says: 'The internet is the same speed", bold=True)
        self.text("everywhere in the world.' Do you agree or disagree?")
        self.text("Explain why using what you learned about distance and latency.")
        self.multiline_field("", "hw_speed_debate", 0.7 * inch)

        self.space(0.1 * inch)

        self.text("Q10: Why does Netflix put servers in many different", bold=True)
        self.text("cities instead of just one big data center?")
        self.multiline_field("", "hw_netflix_cdn", 0.6 * inch)

        # === PAGE 4: Reflection + Bonus ===
        self.new_page()

        self.section_header("PART 4: Reflection (25 points)", Colors.MEDIUM_BLUE)
        self.text("Q11: What surprised you most about how the internet works?", bold=True)
        self.multiline_field("", "hw_reflection", 0.7 * inch)

        self.space(0.1 * inch)

        self.text("Q12: If the internet went down, what would you miss most?", bold=True)
        self.multiline_field("", "hw_miss", 0.7 * inch)

        self.section_header("BONUS: Speed Test (+5 points)", Colors.ORANGE)
        self.info_box(
            "Optional Bonus",
            "Run a speed test on your device (with parent/guardian permission). Write down your download and upload speeds.",
            Colors.LIGHT_GRAY, 0.6 * inch
        )

        self.text_field("Download speed:", "bonus_download", 1.3 * inch)
        self.text_field("Upload speed:", "bonus_upload", 1.2 * inch)
        self.text_field("Ping/latency:", "bonus_ping", 1.2 * inch)

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
    output_path = os.path.join(parent_dir, "2026-02-07_Homework_Internet_Connection_Detective.pdf")

    pdf = HomeworkPDF(output_path)
    pdf.build()

    return output_path


if __name__ == "__main__":
    main()
