"""
Classwork PDF Generator - January 25, 2026
Internet Investigator: Analyze Your Digital World

Creates a fillable PDF classwork with proper page layout management.
Each major section gets adequate space - no content gets cut off.

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
    """Consistent color palette for the document."""
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


class Layout:
    """Page layout constants."""
    WIDTH, HEIGHT = letter
    MARGIN = 0.5 * inch
    CONTENT_WIDTH = WIDTH - (2 * MARGIN)
    HEADER_HEIGHT = 1.0 * inch
    FOOTER_HEIGHT = 0.65 * inch
    CONTENT_TOP = HEIGHT - HEADER_HEIGHT - 0.3 * inch
    CONTENT_BOTTOM = FOOTER_HEIGHT + 0.3 * inch


# =============================================================================
# PDF BUILDER CLASS
# =============================================================================

class ClassworkPDF:
    """Builds the Internet Investigator classwork PDF."""

    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.page_num = 0
        self.total_pages = 8
        self.y = Layout.CONTENT_TOP

    # -------------------------------------------------------------------------
    # Core Drawing Methods
    # -------------------------------------------------------------------------

    def new_page(self):
        """Start a new page."""
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1
        self._draw_header()
        self.y = Layout.CONTENT_TOP

    def _draw_header(self):
        """Draw page header."""
        c = self.c

        # Header background
        c.setFillColor(Colors.DARK_BLUE)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT,
               Layout.WIDTH, Layout.HEADER_HEIGHT, fill=True, stroke=False)

        # Orange accent
        c.setFillColor(Colors.ORANGE)
        c.rect(0, Layout.HEIGHT - Layout.HEADER_HEIGHT - 4,
               Layout.WIDTH, 4, fill=True, stroke=False)

        # Title
        c.setFillColor(Colors.WHITE)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                    "CLASSWORK: Internet Investigator")

        # Subtitle
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Mission: Analyze Your Digital World")

        # Page number
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.WHITE)
        c.drawRightString(Layout.WIDTH - Layout.MARGIN, Layout.HEIGHT - 0.55 * inch,
                         f"Page {self.page_num} of {self.total_pages}")

    def _draw_footer(self):
        """Draw footer on current page."""
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
    # Section Drawing Methods
    # -------------------------------------------------------------------------

    def section_header(self, title, color=None):
        """Draw a colored section header."""
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
        """Draw an information box with title and wrapped content."""
        if color is None:
            color = Colors.SKY_BLUE

        c = self.c

        # Background
        c.setFillColor(color)
        c.setStrokeColor(Colors.MEDIUM_BLUE)
        c.roundRect(Layout.MARGIN, self.y - height,
                   Layout.CONTENT_WIDTH, height, 8, fill=True, stroke=True)

        # Title
        c.setFillColor(Colors.DARK_BLUE)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(Layout.MARGIN + 0.15 * inch, self.y - 0.2 * inch, title)

        # Content (simple word wrap)
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
        """Draw a line of text."""
        c = self.c
        c.setFillColor(Colors.DARK_GRAY)
        font = "Helvetica-Bold" if bold else "Helvetica"
        c.setFont(font, size)
        c.drawString(Layout.MARGIN + indent, self.y, content)
        self.y -= (size + 6)

    def text_field(self, label, field_name, label_width=1.3 * inch,
                   field_width=None, height=0.25 * inch):
        """Draw a text input field with label."""
        c = self.c

        # Label
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(Layout.MARGIN, self.y, label)

        # Field position and width
        field_x = Layout.MARGIN + label_width
        if field_width is None:
            actual_width = Layout.WIDTH - Layout.MARGIN - field_x
        else:
            actual_width = field_width

        # Text field
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
        )

        self.y -= 0.38 * inch

    def multiline_field(self, label, field_name, height=0.5 * inch):
        """Draw a multiline text area."""
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
            fieldFlags='multiline',
        )

        self.y -= height + 0.08 * inch

    def checkbox(self, label, field_name, x_offset=0):
        """Draw a checkbox with label."""
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
        """Draw a multiple choice question."""
        c = self.c

        # Question text
        c.setFillColor(Colors.DARK_GRAY)
        c.setFont("Helvetica-Bold", 10)
        q_text = f"Q{q_num}: {question}" if q_num else question
        c.drawString(Layout.MARGIN, self.y, q_text)
        self.y -= 0.22 * inch

        # Options with checkboxes
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

    def matching_exercise(self, terms, choices, field_name):
        """Draw a matching exercise."""
        c = self.c

        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(Colors.DARK_GRAY)
        c.drawString(Layout.MARGIN, self.y, "TERM")
        c.drawString(Layout.MARGIN + 1.5 * inch, self.y, "YOUR ANSWER")
        c.drawString(Layout.MARGIN + 3.2 * inch, self.y, "CHOICES")
        self.y -= 0.08 * inch

        c.setStrokeColor(Colors.MEDIUM_BLUE)
        c.line(Layout.MARGIN, self.y, Layout.WIDTH - Layout.MARGIN, self.y)
        self.y -= 0.22 * inch

        for i, term in enumerate(terms):
            c.setFont("Helvetica", 10)
            c.setFillColor(Colors.DARK_GRAY)
            c.drawString(Layout.MARGIN, self.y, f"{i+1}. {term}")

            c.acroForm.textfield(
                name=f"{field_name}_{i}",
                x=Layout.MARGIN + 1.5 * inch,
                y=self.y - 4,
                width=1.2 * inch,
                height=0.2 * inch,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.LIGHT_GRAY,
                textColor=black,
                fontSize=10,
                borderWidth=1,
            )

            if i < len(choices):
                c.drawString(Layout.MARGIN + 3.2 * inch, self.y, f"{chr(65+i)}) {choices[i]}")

            self.y -= 0.28 * inch

    def case_file(self, case_num, prefix):
        """Draw a complete case file section."""
        label_w = 1.3 * inch

        # Website name and URL
        self.text_field("Website Name:", f"{prefix}_name", label_w)
        self.text_field("Full URL:", f"{prefix}_url", label_w)

        self.y -= 0.1 * inch

        # Part A: URL Breakdown
        self.c.setFillColor(Colors.MEDIUM_BLUE)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "PART A: URL Breakdown")
        self.y -= 0.22 * inch

        url_label = 1.1 * inch
        self.text_field("Protocol:", f"{prefix}_protocol", url_label, 2 * inch)
        self.text_field("Subdomain:", f"{prefix}_subdomain", url_label, 2 * inch)
        self.text_field("Domain:", f"{prefix}_domain", url_label, 2 * inch)
        self.text_field("TLD:", f"{prefix}_tld", url_label, 1.5 * inch)
        self.text_field("Path:", f"{prefix}_path", url_label)

        self.y -= 0.1 * inch

        # Part B: Security Check
        self.c.setFillColor(Colors.GREEN)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "PART B: Security Check")
        self.y -= 0.22 * inch

        sec_label = 1.4 * inch
        self.text_field("Lock icon? (Yes/No):", f"{prefix}_lock", sec_label, 1 * inch)
        self.text_field("HTTP or HTTPS?:", f"{prefix}_secure", sec_label, 1.2 * inch)
        self.text("Would you enter a password here? Why?", size=10)
        self.multiline_field("", f"{prefix}_password_why", 0.45 * inch)

        self.y -= 0.1 * inch

        # Part C: Tracert
        self.c.setFillColor(Colors.PURPLE)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "PART C: Tracert Investigation")
        self.y -= 0.18 * inch

        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(Colors.DARK_GRAY)
        self.c.drawString(Layout.MARGIN + 0.1 * inch, self.y,
                         "Windows: tracert [website]  |  Mac: traceroute [website]")
        self.y -= 0.22 * inch

        trace_label = 1.1 * inch
        self.text_field("Total hops:", f"{prefix}_hops", trace_label, 1 * inch)
        self.text_field("Fastest hop:", f"{prefix}_fastest", trace_label, 2.5 * inch)
        self.text_field("Slowest hop:", f"{prefix}_slowest", trace_label, 2.5 * inch)

    def space(self, amount=0.15 * inch):
        """Add vertical space."""
        self.y -= amount

    # -------------------------------------------------------------------------
    # Build Document
    # -------------------------------------------------------------------------

    def build(self):
        """Build the complete document."""

        # === PAGE 1: Title & Review Questions 1-3 ===
        self.new_page()

        # Student info
        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.1 * inch)

        # Mission box
        self.info_box(
            "Your Mission Today",
            "You're an Internet Investigator! Analyze websites you actually use, "
            "trace how data travels across the internet, and uncover the secrets of how the web works.",
            Colors.SKY_BLUE, 0.7 * inch
        )

        self.space(0.1 * inch)

        # Review section
        self.section_header("LAST WEEK REVIEW (10 points)", Colors.ORANGE)

        self.multiple_choice("What is an IP Address?", [
            "A website name like google.com",
            "A unique number that identifies your computer",
            "Your Wi-Fi password",
            "A type of cable"
        ], "review_q1", 1)

        self.multiple_choice("What does DNS do?", [
            "Speeds up your internet",
            "Blocks viruses",
            "Translates website names into IP addresses",
            "Connects your Wi-Fi"
        ], "review_q2", 2)

        self.multiple_choice("What is a Gateway?", [
            "A website you visit often",
            "The 'front door' connecting your network to the internet",
            "A type of computer virus",
            "Your computer's password"
        ], "review_q3", 3)

        # === PAGE 2: Review Q4-Q5 & Mission ===
        self.new_page()

        # Q4
        self.c.setFillColor(Colors.DARK_GRAY)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "Q4: What command shows YOUR computer's IP address? (3 pts)")
        self.y -= 0.28 * inch

        self.text_field("Windows command:", "review_q4_win", 1.5 * inch, 2.5 * inch)
        self.text_field("Mac command:", "review_q4_mac", 1.5 * inch, 2.5 * inch)

        self.space(0.15 * inch)

        # Q5 Matching
        self.c.setFillColor(Colors.DARK_GRAY)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "Q5: Match the term to the analogy (3 pts)")
        self.y -= 0.18 * inch

        self.matching_exercise(
            ["IP Address", "Router", "Packets"],
            ["Traffic police directing cars", "Your home address", "Puzzle pieces sent through mail"],
            "review_match"
        )

        # === PAGE 3: Your Mission & Case File #1 ===
        self.new_page()

        # Mission instruction
        self.section_header("YOUR MISSION", Colors.GREEN)

        self.info_box(
            "Pick 3 Websites YOU Actually Use",
            "Choose from: YouTube, TikTok, Instagram, Discord, Snapchat, Google Classroom, "
            "Khan Academy, Quizlet, Steam, Roblox, Twitch, Spotify - or any website you love!",
            Colors.LIGHT_GREEN, 0.7 * inch
        )

        self.space(0.15 * inch)

        self.section_header("CASE FILE #1 (20 points)", Colors.PURPLE)
        self.case_file(1, "case1")

        # === PAGE 4: Case File #2 ===
        self.new_page()

        self.section_header("CASE FILE #2 (20 points)", Colors.PURPLE)
        self.case_file(2, "case2")

        # === PAGE 5: Case File #3 ===
        self.new_page()

        self.section_header("CASE FILE #3 (20 points)", Colors.PURPLE)
        self.case_file(3, "case3")

        # === PAGE 6: Investigation Summary ===
        self.new_page()

        self.section_header("INVESTIGATION SUMMARY (20 points)", Colors.MEDIUM_BLUE)

        # Q1
        self.c.setFillColor(Colors.DARK_GRAY)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "Q1: When you visited these websites, your computer was the:")
        self.y -= 0.22 * inch

        self.c.acroForm.checkbox(
            name="summary_client", x=Layout.MARGIN + 0.2 * inch, y=self.y - 2, size=11,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.WHITE
        )
        self.c.setFont("Helvetica", 10)
        self.c.drawString(Layout.MARGIN + 0.2 * inch + 15, self.y, "A) CLIENT")

        self.c.acroForm.checkbox(
            name="summary_server", x=Layout.MARGIN + 2 * inch, y=self.y - 2, size=11,
            borderColor=Colors.MEDIUM_BLUE, fillColor=Colors.WHITE
        )
        self.c.drawString(Layout.MARGIN + 2 * inch + 15, self.y, "B) SERVER")
        self.y -= 0.25 * inch

        self.text("Why?", bold=True)
        self.multiline_field("", "summary_q1_why", 0.45 * inch)

        self.space(0.1 * inch)

        # Q2
        self.text("Q2: Which website had the FEWEST hops?", bold=True)
        self.text_field("Website:", "summary_q2_site", 0.9 * inch)
        self.text("Why is fewer hops usually better?")
        self.multiline_field("", "summary_q2_why", 0.45 * inch)

        self.space(0.1 * inch)

        # Q3
        self.text("Q3: Did all 3 websites use HTTPS?", bold=True)
        self.text_field("Yes/No:", "summary_q3_https", 0.8 * inch, 1 * inch)
        self.text("What should you NEVER enter on a site without HTTPS?")
        self.multiline_field("", "summary_q3_never", 0.45 * inch)

        self.space(0.1 * inch)

        # Q4 and Q5
        self.multiple_choice("HTTPS uses which port?", [
            "Port 80",
            "Port 443"
        ], "summary_q4", 4)

        self.multiple_choice("What happens FIRST when you type a website in your browser?", [
            "The server sends you the webpage",
            "Your browser displays the content",
            "DNS translates the domain to an IP address",
            "You click a link"
        ], "summary_q5", 5)

        # === PAGE 7: Creative Challenge & Reflection ===
        self.new_page()

        self.section_header("CREATIVE CHALLENGE (5 points)", Colors.GREEN)

        self.info_box(
            "Design Your Own Website!",
            "Create a website for something you love - a game, hobby, band, or anything cool! "
            "Think about what your server would need to store.",
            Colors.LIGHT_GREEN, 0.55 * inch
        )

        self.space(0.1 * inch)

        self.text_field("Your website name:", "creative_name", 1.5 * inch)

        self.space(0.05 * inch)

        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(Colors.DARK_GRAY)
        self.c.drawString(Layout.MARGIN, self.y, "Your URL:  https://_______._______._____/_______")
        self.y -= 0.1 * inch
        self.c.setFont("Helvetica", 8)
        self.c.drawString(Layout.MARGIN + 1.5 * inch, self.y, "(subdomain)  (domain)  (TLD)    (path)")
        self.y -= 0.22 * inch

        url_label = 1 * inch
        self.text_field("Subdomain:", "creative_subdomain", url_label, 2 * inch)
        self.text_field("Domain:", "creative_domain", url_label, 2 * inch)
        self.text_field("Path:", "creative_path", url_label, 2 * inch)

        self.space(0.1 * inch)

        self.text("What would your server store? (check all that apply)", bold=True)
        self.space(0.05 * inch)

        self.checkbox("Images/photos", "creative_images")
        self.checkbox("Videos", "creative_videos")
        self.checkbox("User accounts", "creative_accounts")
        self.checkbox("Game data", "creative_games")
        self.checkbox("Music", "creative_music")
        self.text_field("Other:", "creative_other", 0.6 * inch)

        self.space(0.05 * inch)
        self.text("Would it NEED HTTPS? Why?", bold=True)
        self.multiline_field("", "creative_https_why", 0.5 * inch)

        self.space(0.15 * inch)

        # Reflection
        self.section_header("REFLECTION (5 points)", Colors.PURPLE)

        self.text("One thing I learned today:", bold=True)
        self.multiline_field("", "reflection_learned", 0.5 * inch)

        self.text("One thing I'm still curious about:", bold=True)
        self.multiline_field("", "reflection_curious", 0.5 * inch)

        # === PAGE 8: Bonus & Help ===
        self.new_page()

        self.section_header("BONUS: Request Counter (+10 points)", Colors.ORANGE)

        self.info_box(
            "Developer Tools Challenge",
            "Open Developer Tools > Network tab > Refresh the page to see all the requests! "
            "Windows: Press F12  |  Mac: Press Cmd + Option + I",
            Colors.SKY_BLUE, 0.55 * inch
        )

        self.space(0.1 * inch)

        bonus_label = 1.3 * inch

        self.text("Website 1:", bold=True, size=10)
        self.text_field("# of requests:", "bonus_w1_requests", bonus_label, 1.5 * inch)
        self.text_field("Biggest file type:", "bonus_w1_filetype", bonus_label, 2 * inch)

        self.text("Website 2:", bold=True, size=10)
        self.text_field("# of requests:", "bonus_w2_requests", bonus_label, 1.5 * inch)
        self.text_field("Biggest file type:", "bonus_w2_filetype", bonus_label, 2 * inch)

        self.text("Website 3:", bold=True, size=10)
        self.text_field("# of requests:", "bonus_w3_requests", bonus_label, 1.5 * inch)
        self.text_field("Biggest file type:", "bonus_w3_filetype", bonus_label, 2 * inch)

        self.space(0.1 * inch)
        self.text_field("Which site had the MOST requests?", "bonus_most", 2.5 * inch)
        self.text("Why do you think?")
        self.multiline_field("", "bonus_why", 0.45 * inch)

        self.space(0.25 * inch)

        # Help section
        self.section_header("NEED HELP?", Colors.DARK_BLUE)

        c = self.c
        c.setFillColor(Colors.DARK_GRAY)

        help_items = [
            ("OPEN COMMAND LINE:", "Windows: Win+R, type 'cmd'  |  Mac: Cmd+Space, type 'Terminal'"),
            ("RUN TRACE:", "Windows: tracert google.com  |  Mac: traceroute google.com"),
            ("DEV TOOLS:", "Windows: F12  |  Mac: Cmd+Option+I"),
            ("CAN'T RUN TRACERT?", "Use: https://www.traceroute-online.com/"),
        ]

        for label, value in help_items:
            c.setFont("Helvetica-Bold", 9)
            c.drawString(Layout.MARGIN, self.y, label)
            c.setFont("Helvetica", 9)
            c.drawString(Layout.MARGIN + 1.5 * inch, self.y, value)
            self.y -= 0.2 * inch

        # Final footer
        self._draw_footer()

        # Save
        self.c.save()
        print(f"[SUCCESS] Classwork PDF created: {self.output_path}")
        return self.output_path


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Generate the classwork PDF."""

    # Output folder
    output_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Clients_Servers_How_Websites_Work_2026-01-25"
    )

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, "2026-01-25_Classwork_Internet_Investigator.pdf")

    # Build PDF
    pdf = ClassworkPDF(output_path)
    pdf.build()

    return output_path


if __name__ == "__main__":
    main()
