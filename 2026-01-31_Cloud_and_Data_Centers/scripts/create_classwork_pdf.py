"""
Classwork PDF Generator - January 31, 2026
Cloud Detective: Explore Your Digital World

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
    CLOUD_BLUE = HexColor('#87CEFA')
    ORANGE = HexColor('#FF9933')
    GREEN = HexColor('#4CAF50')
    LIGHT_GREEN = HexColor('#C8E6C9')
    PURPLE = HexColor('#9C27B0')
    LIGHT_PURPLE = HexColor('#E1BEE7')
    RED = HexColor('#F44336')
    LIGHT_GRAY = HexColor('#F5F5F5')
    DARK_GRAY = HexColor('#424242')
    WHITE = HexColor('#FFFFFF')
    DATA_CENTER_GRAY = HexColor('#607D8B')


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
    """Builds the Cloud Detective classwork PDF."""

    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.page_num = 0
        self.total_pages = 7
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
                    "CLASSWORK: Cloud Detective")

        # Subtitle
        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Mission: Explore Your Digital Cloud World")

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

    def space(self, amount=0.15 * inch):
        """Add vertical space."""
        self.y -= amount

    # -------------------------------------------------------------------------
    # Build Document
    # -------------------------------------------------------------------------

    def build(self):
        """Build the complete document."""

        # === PAGE 1: Title & Review ===
        self.new_page()

        # Student info
        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.1 * inch)

        # Mission box
        self.info_box(
            "Your Mission Today",
            "You're a Cloud Detective! Today you'll explore where your data actually lives, "
            "discover real data centers around the world, and understand how cloud services power your digital life.",
            Colors.CLOUD_BLUE, 0.7 * inch
        )

        self.space(0.1 * inch)

        # Review section
        self.section_header("QUICK REVIEW: Last Week (10 points)", Colors.ORANGE)

        self.multiple_choice("What is a SERVER?", [
            "Your personal laptop",
            "A computer that stores and serves data to clients",
            "A type of Wi-Fi router",
            "A gaming console"
        ], "review_q1", 1)

        self.multiple_choice("When you visit youtube.com, your device is the...", [
            "Server",
            "Data Center",
            "Client",
            "Cloud"
        ], "review_q2", 2)

        self.multiple_choice("What does DNS do?", [
            "Blocks viruses",
            "Makes internet faster",
            "Translates domain names to IP addresses",
            "Stores your passwords"
        ], "review_q3", 3)

        # === PAGE 2: Cloud Basics ===
        self.new_page()

        self.section_header("PART 1: What is the Cloud? (15 points)", Colors.CLOUD_BLUE)

        self.text("Q1: Complete the famous saying about the cloud:", bold=True)
        self.text('"There is no cloud, it\'s just _______________________"')
        self.text_field("Your answer:", "cloud_saying", 1.1 * inch)

        self.space(0.1 * inch)

        self.text("Q2: What is 'the cloud' REALLY?", bold=True)
        self.multiple_choice("", [
            "Actual clouds in the sky that store data",
            "A wireless internet connection",
            "Servers stored in data centers around the world",
            "A type of computer software"
        ], "cloud_definition")

        self.space(0.1 * inch)

        self.text("Q3: Name 3 cloud services YOU use:", bold=True)
        self.text_field("1.", "cloud_service_1", 0.3 * inch)
        self.text_field("2.", "cloud_service_2", 0.3 * inch)
        self.text_field("3.", "cloud_service_3", 0.3 * inch)

        self.space(0.15 * inch)

        self.section_header("PART 2: Data Center Investigation (15 points)", Colors.DATA_CENTER_GRAY)

        self.info_box(
            "Data Center Research",
            "Go to: google.com/about/datacenters/locations/ and explore the interactive map. "
            "Click on different locations to learn about Google's data centers.",
            Colors.LIGHT_GRAY, 0.6 * inch
        )

        self.text("Q4: How many continents have Google data centers?", bold=True)
        self.text_field("Number:", "dc_continents", 0.8 * inch, 1 * inch)

        # === PAGE 3: Data Center Investigation continued ===
        self.new_page()

        self.text("Q5: Name 2 locations where Google has data centers:", bold=True)
        self.text_field("Location 1:", "dc_location_1", 1 * inch)
        self.text_field("Location 2:", "dc_location_2", 1 * inch)

        self.space(0.1 * inch)

        self.text("Q6: Why do data centers need massive cooling systems?", bold=True)
        self.multiline_field("", "dc_cooling", 0.5 * inch)

        self.space(0.1 * inch)

        self.text("Q7: Why are many data centers built near water sources?", bold=True)
        self.multiline_field("", "dc_water", 0.5 * inch)

        self.space(0.15 * inch)

        self.section_header("PART 3: The Big Three Providers (15 points)", Colors.ORANGE)

        self.text("Research the three biggest cloud providers and fill in the blanks:", bold=True)
        self.space(0.1 * inch)

        # AWS
        self.c.setFillColor(Colors.ORANGE)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "Amazon Web Services (AWS)")
        self.y -= 0.2 * inch
        self.text_field("Famous company that uses AWS:", "aws_customer", 2.3 * inch)

        self.space(0.05 * inch)

        # Azure
        self.c.setFillColor(HexColor('#0078D4'))
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "Microsoft Azure")
        self.y -= 0.2 * inch
        self.text_field("Famous company that uses Azure:", "azure_customer", 2.3 * inch)

        self.space(0.05 * inch)

        # Google Cloud
        self.c.setFillColor(HexColor('#4285F4'))
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(Layout.MARGIN, self.y, "Google Cloud")
        self.y -= 0.2 * inch
        self.text_field("Famous company that uses GCP:", "gcp_customer", 2.5 * inch)

        self.space(0.1 * inch)

        self.text("Q8: Which is the BIGGEST cloud provider in the world?", bold=True)
        self.text_field("Answer:", "biggest_provider", 0.7 * inch)

        # === PAGE 4: Cloud Services ===
        self.new_page()

        self.section_header("PART 4: Cloud Services You Use (15 points)", Colors.GREEN)

        self.text("Q9: For each app, identify what cloud service it uses:", bold=True)
        self.space(0.1 * inch)

        apps = [
            ("YouTube", "youtube_stores"),
            ("Google Drive", "drive_stores"),
            ("Spotify", "spotify_stores"),
            ("Fortnite/Roblox", "game_stores"),
        ]

        for app_name, field_name in apps:
            self.text(f"{app_name} - What does it store in the cloud?")
            self.text_field("Stores:", field_name, 0.6 * inch)

        self.space(0.1 * inch)

        self.text("Q10: Cloud or Local? Check the correct box:", bold=True)
        self.space(0.1 * inch)

        scenarios = [
            ("Watching a downloaded movie offline", "scenario1"),
            ("Sending a message on Discord", "scenario2"),
            ("Using the calculator app", "scenario3"),
            ("Saving a file to Google Drive", "scenario4"),
        ]

        for scenario, field_name in scenarios:
            self.c.setFont("Helvetica", 9)
            self.c.setFillColor(Colors.DARK_GRAY)
            self.c.drawString(Layout.MARGIN, self.y, scenario)

            self.c.acroForm.checkbox(
                name=f"{field_name}_cloud",
                x=Layout.MARGIN + 4.2 * inch,
                y=self.y - 2,
                size=11,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.WHITE,
            )
            self.c.drawString(Layout.MARGIN + 4.2 * inch + 15, self.y, "Cloud")

            self.c.acroForm.checkbox(
                name=f"{field_name}_local",
                x=Layout.MARGIN + 5.2 * inch,
                y=self.y - 2,
                size=11,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.WHITE,
            )
            self.c.drawString(Layout.MARGIN + 5.2 * inch + 15, self.y, "Local")

            self.y -= 0.28 * inch

        # === PAGE 5: AI + Cloud ===
        self.new_page()

        self.section_header("PART 5: AI + Cloud (10 points)", Colors.PURPLE)

        self.info_box(
            "AI Needs the Cloud!",
            "Chatbots like ChatGPT, Gemini, Claude, and Grok need massive computing power. "
            "They can't run on your phone or laptop - they run on thousands of servers in data centers!",
            Colors.LIGHT_PURPLE, 0.65 * inch
        )

        self.space(0.1 * inch)

        self.text("Q14: Match the AI chatbot to its cloud provider:", bold=True)
        self.space(0.1 * inch)

        ai_matches = [
            ("ChatGPT (OpenAI)", "ai_match_chatgpt"),
            ("Gemini", "ai_match_gemini"),
            ("Claude (Anthropic)", "ai_match_claude"),
            ("Grok (xAI)", "ai_match_grok"),
        ]

        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(Colors.DARK_GRAY)
        self.c.drawString(Layout.MARGIN + 4 * inch, self.y + 0.15 * inch,
                         "Options: Microsoft Azure, Google Cloud,")
        self.c.drawString(Layout.MARGIN + 4 * inch, self.y,
                         "AWS, xAI's own servers")
        self.y -= 0.15 * inch

        for ai_name, field_name in ai_matches:
            self.text(f"{ai_name}:", indent=0.2 * inch)
            self.text_field("Cloud Provider:", field_name, 1.2 * inch, 2.5 * inch)

        self.space(0.1 * inch)

        self.text("Q15: Why can't ChatGPT run on just your phone?", bold=True)
        self.multiline_field("", "ai_why_cloud", 0.5 * inch)

        self.space(0.1 * inch)

        self.text("Q16: What do AI models need lots of to learn (train)?", bold=True)
        self.multiple_choice("", [
            "Water and food",
            "Data and computing power",
            "Sunlight and electricity",
            "Batteries and cables"
        ], "ai_training")

        # === PAGE 6: Safety & Reflection ===
        self.new_page()

        self.section_header("PART 6: Cloud Safety (10 points)", Colors.GREEN)

        self.text("Q11: What are 2 ways to keep your cloud accounts safe?", bold=True)
        self.text_field("1.", "safety_tip_1", 0.3 * inch)
        self.text_field("2.", "safety_tip_2", 0.3 * inch)

        self.space(0.1 * inch)

        self.text("Q12: What is 2FA (Two-Factor Authentication)?", bold=True)
        self.multiline_field("", "tfa_definition", 0.5 * inch)

        self.space(0.1 * inch)

        self.text("Q13: Why should you think before uploading to the cloud?", bold=True)
        self.multiline_field("", "upload_caution", 0.5 * inch)

        self.space(0.15 * inch)

        self.section_header("REFLECTION (10 points)", Colors.MEDIUM_BLUE)

        self.text("What surprised you most about 'the cloud' today?", bold=True)
        self.multiline_field("", "reflection_surprise", 0.5 * inch)

        self.text("What will you think about differently when using cloud services?", bold=True)
        self.multiline_field("", "reflection_change", 0.5 * inch)

        # === PAGE 7: Bonus ===
        self.new_page()

        self.section_header("BONUS: Cloud Speed Test (+10 points)", Colors.ORANGE)

        self.info_box(
            "Speed Test Challenge",
            "Upload a small file (photo or document) to your cloud storage (Google Drive, iCloud, OneDrive). "
            "Time how long it takes. Then check if you can see it on another device or browser.",
            Colors.SKY_BLUE, 0.65 * inch
        )

        self.text_field("Cloud service used:", "bonus_service", 1.5 * inch)
        self.text_field("File size (approx):", "bonus_filesize", 1.3 * inch, 2 * inch)
        self.text_field("Upload time:", "bonus_time", 1.1 * inch, 2 * inch)

        self.space(0.1 * inch)

        self.text("Could you see the file on another device?", bold=True)
        self.checkbox("Yes, immediately", "bonus_immediate")
        self.checkbox("Yes, after a few seconds", "bonus_delayed")
        self.checkbox("No, I couldn't access it", "bonus_no")

        self.space(0.1 * inch)

        self.text("Where did your file travel to? (Think about it!)", bold=True)
        self.multiline_field("", "bonus_travel", 0.5 * inch)

        self.space(0.25 * inch)

        # Help section
        self.section_header("NEED HELP?", Colors.DARK_BLUE)

        c = self.c
        c.setFillColor(Colors.DARK_GRAY)

        help_items = [
            ("DATA CENTER MAP:", "google.com/about/datacenters/locations/"),
            ("CLOUD PROVIDERS:", "AWS = Amazon | Azure = Microsoft | GCP = Google"),
            ("CLOUD STORAGE:", "Google Drive, iCloud, OneDrive, Dropbox"),
        ]

        for label, value in help_items:
            c.setFont("Helvetica-Bold", 9)
            c.drawString(Layout.MARGIN, self.y, label)
            c.setFont("Helvetica", 9)
            c.drawString(Layout.MARGIN + 1.4 * inch, self.y, value)
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

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-01-31_Classwork_Cloud_Detective.pdf")

    # Build PDF
    pdf = ClassworkPDF(output_path)
    pdf.build()

    return output_path


if __name__ == "__main__":
    main()
