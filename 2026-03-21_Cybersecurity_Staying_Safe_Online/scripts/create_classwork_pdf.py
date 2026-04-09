"""
Classwork PDF Generator - March 21, 2026
Cybersecurity Detective: Can You Spot the Scam?

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
    LIGHT_RED = HexColor('#FFCDD2')
    LIGHT_GRAY = HexColor('#F5F5F5')
    DARK_GRAY = HexColor('#424242')
    WHITE = HexColor('#FFFFFF')
    SHIELD_BLUE = HexColor('#1976D2')
    DANGER_RED = HexColor('#D32F2F')
    SAFE_GREEN = HexColor('#388E3C')
    TEAL = HexColor('#00897B')


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
        self.c.setTitle("Classwork: Cybersecurity Detective")
        self.page_num = 0
        self.total_pages = 8
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
                    "CLASSWORK: Cybersecurity Detective")

        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Can You Spot the Scam?")

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
            letter_char = chr(65 + i)

            c.acroForm.checkbox(
                name=f"{field_name}_{letter_char}",
                x=Layout.MARGIN + 0.2 * inch,
                y=self.y - 2,
                size=11,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.WHITE,
            )

            c.setFont("Helvetica", 10)
            c.setFillColor(Colors.DARK_GRAY)
            c.drawString(Layout.MARGIN + 0.2 * inch + 15, self.y, f"{letter_char}) {option}")
            self.y -= 0.2 * inch

        self.y -= 0.08 * inch

    def space(self, amount=0.15 * inch):
        self.y -= amount

    # -------------------------------------------------------------------------
    # Build
    # -------------------------------------------------------------------------

    def build(self):
        # === PAGE 1: Student Info + Key Terms ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.info_box(
            "Your Mission Today",
            "You are a Cybersecurity Detective! Your job is to identify online threats, spot phishing scams, evaluate password strength, and learn how to protect yourself online.",
            Colors.LIGHT_BLUE, 0.7 * inch
        )

        self.space(0.1 * inch)

        self.section_header("KEY TERMS REFERENCE", Colors.SHIELD_BLUE)

        terms = [
            ("Cybersecurity", "Protecting computers, networks, and data from threats"),
            ("Phishing", "Fake emails/texts/websites that trick you into sharing info"),
            ("Password", "A secret word or phrase that controls access to an account"),
            ("2FA", "Two-Factor Authentication -- a second verification step"),
            ("Social Engineering", "Tricking people into giving up confidential information"),
            ("Digital Footprint", "The trail of data you leave behind online"),
            ("Malware", "Malicious software: viruses, ransomware, spyware"),
            ("HTTPS", "Secure version of HTTP -- look for the padlock!"),
        ]

        for term, definition in terms:
            self.text(f"{term}: {definition}", size=9)

        # === PAGE 2: Password Analysis ===
        self.new_page()

        self.section_header("PART 1: Password Strength Analysis (20 points)", Colors.SAFE_GREEN)

        self.text("Rate each password from 1 (very weak) to 5 (very strong). Explain why.", bold=True)
        self.space(0.1 * inch)

        passwords = [
            ("1", "password123"),
            ("2", "MyDog$Name!2026"),
            ("3", "abc"),
            ("4", "PurpleTiger$Eats42Tacos!"),
            ("5", "john2010"),
        ]

        for num, pw in passwords:
            self.text(f"Q{num}: {pw}", bold=True)
            self.text_field("Rating (1-5):", f"pw_rate_{num}", 1.1 * inch, 1 * inch)
            self.multiline_field("Why?", f"pw_explain_{num}", 0.4 * inch)

        # === PAGE 3: Create Strong Passwords ===
        self.new_page()

        self.section_header("PART 1 (continued): Create Your Own Strong Passwords", Colors.SAFE_GREEN)

        self.text("Q6: Create a strong password using the passphrase method.", bold=True)
        self.text("Pick 3-4 random words and add numbers/symbols. Example: BlueFrog$Jumps99High!")
        self.text_field("Your passphrase:", "pw_create_1", 1.3 * inch)
        self.multiline_field("Why is this strong?", "pw_create_explain_1", 0.4 * inch)

        self.space(0.1 * inch)

        self.text("Q7: Your friend uses 'gaming123' for their Fortnite AND email.", bold=True)
        self.text("What advice would you give them? Write 2-3 sentences.")
        self.multiline_field("", "pw_advice", 0.6 * inch)

        self.space(0.15 * inch)

        self.section_header("PART 2: Spot the Phishing Scam! (25 points)", Colors.DANGER_RED)

        self.info_box(
            "Instructions",
            "Read each message below. Decide if it is REAL or a SCAM. Then list the red flags that helped you decide.",
            Colors.LIGHT_RED, 0.6 * inch
        )

        self.space(0.1 * inch)

        self.text("MESSAGE 1:", bold=True)
        self.text('"FROM: security@amaz0n-verify.com"', size=9, indent=0.2 * inch)
        self.text('"Subject: URGENT! Your account will be SUSPENDED in 24 hours!"', size=9, indent=0.2 * inch)
        self.text('"Click here immediately to verify your identity: http://amaz0n-login.sketchy.ru"', size=9, indent=0.2 * inch)

        self.multiple_choice("", ["REAL", "SCAM"], "phish_1")
        self.multiline_field("Red flags you noticed:", "phish_1_flags", 0.4 * inch)

        # === PAGE 4: More Phishing Examples ===
        self.new_page()

        self.section_header("PART 2 (continued): More Messages to Analyze", Colors.DANGER_RED)

        self.text("MESSAGE 2:", bold=True)
        self.text('"FROM: noreply@microsoft.com"', size=9, indent=0.2 * inch)
        self.text('"Subject: Your Microsoft 365 subscription renewal"', size=9, indent=0.2 * inch)
        self.text('"Hi Student, your M365 plan renews on April 1. No action needed."', size=9, indent=0.2 * inch)
        self.text('"View your subscription: https://account.microsoft.com"', size=9, indent=0.2 * inch)

        self.multiple_choice("", ["REAL", "SCAM"], "phish_2")
        self.multiline_field("Why did you choose this answer?", "phish_2_flags", 0.4 * inch)

        self.space(0.1 * inch)

        self.text("MESSAGE 3:", bold=True)
        self.text('"TEXT from unknown number: Congratulations!! You have won a FREE"', size=9, indent=0.2 * inch)
        self.text('"iPhone 16! Click this link to claim NOW before it expires:"', size=9, indent=0.2 * inch)
        self.text('"http://free-iphones-real.biz/claim?id=29381"', size=9, indent=0.2 * inch)

        self.multiple_choice("", ["REAL", "SCAM"], "phish_3")
        self.multiline_field("Red flags you noticed:", "phish_3_flags", 0.4 * inch)

        self.space(0.1 * inch)

        self.text("MESSAGE 4:", bold=True)
        self.text('"FROM: itsupport@yourschool.edu"', size=9, indent=0.2 * inch)
        self.text('"Subject: Password reset required"', size=9, indent=0.2 * inch)
        self.text('"Dear Student, please reply to this email with your current password"', size=9, indent=0.2 * inch)
        self.text('"so we can reset it for you. Thank you, IT Department"', size=9, indent=0.2 * inch)

        self.multiple_choice("", ["REAL", "SCAM"], "phish_4")
        self.multiline_field("Red flags you noticed:", "phish_4_flags", 0.4 * inch)

        # === PAGE 5: Social Engineering + 2FA ===
        self.new_page()

        self.section_header("PART 3: Social Engineering Scenarios (20 points)", Colors.ORANGE)

        self.text("Read each scenario and answer the question.", bold=True)
        self.space(0.1 * inch)

        self.text("Scenario 1: Someone calls you saying they are from Apple Support.", bold=True)
        self.text("They say your iCloud account has been hacked and they need your")
        self.text("password to 'secure it.' What should you do?")
        self.multiline_field("", "se_1", 0.5 * inch)

        self.text("Scenario 2: You find a USB drive in the school parking lot", bold=True)
        self.text("labeled 'Final Exam Answers.' What should you do?")
        self.multiline_field("", "se_2", 0.5 * inch)

        self.text("Scenario 3: A friend sends you a DM on Instagram: 'OMG look at this", bold=True)
        self.text("embarrassing photo of you! Click here!' But the link looks weird.")
        self.text("What should you do?")
        self.multiline_field("", "se_3", 0.5 * inch)

        # === PAGE 6: 2FA + Safe Browsing ===
        self.new_page()

        self.section_header("PART 4: Two-Factor Authentication (15 points)", Colors.TEAL)

        self.multiple_choice(
            "What does 2FA stand for?",
            ["Two-File Authentication", "Two-Factor Authentication",
             "Two-Finger Access", "Two-Firewall Activation"],
            "tfa_q1", 1
        )

        self.multiple_choice(
            "Which of these is an example of 2FA?",
            ["Using a longer password", "Logging in with password + a code from your phone",
             "Changing your password every month", "Using the same password on two sites"],
            "tfa_q2", 2
        )

        self.text("Q3: Name two of your accounts where you should turn on 2FA.", bold=True)
        self.text_field("Account 1:", "tfa_account1", 0.9 * inch, 3 * inch)
        self.text_field("Account 2:", "tfa_account2", 0.9 * inch, 3 * inch)

        self.text("Q4: Why is 2FA important even if you have a strong password?", bold=True)
        self.multiline_field("", "tfa_why", 0.5 * inch)

        self.space(0.1 * inch)

        self.section_header("PART 5: Safe Browsing Check (10 points)", Colors.PURPLE)

        self.multiple_choice(
            "Which URL is most likely safe?",
            ["http://free-games-download.biz", "https://www.google.com",
             "http://g00gle.com", "https://login-verify-paypal.ru"],
            "browse_q1", 1
        )

        self.text("Q2: What does the 'S' in HTTPS stand for, and why does it matter?", bold=True)
        self.multiline_field("", "browse_https", 0.45 * inch)

        # === PAGE 7: AI & Cybersecurity ===
        self.new_page()

        self.section_header("PART 6: AI & Cybersecurity (10 points)", Colors.SHIELD_BLUE)

        self.info_box(
            "AI and Security",
            "Artificial Intelligence is changing cybersecurity -- it is used by BOTH attackers and defenders. Understanding how AI affects security will be important as we start our AI unit next month!",
            Colors.LIGHT_BLUE, 0.7 * inch
        )

        self.space(0.1 * inch)

        self.text("Q1: AI can now write phishing emails with perfect grammar and no", bold=True)
        self.text("spelling mistakes. How does this make phishing HARDER to detect?")
        self.multiline_field("", "ai_phishing", 0.5 * inch)

        self.text("Q2: A 'deepfake' is an AI-generated video or audio that looks and", bold=True)
        self.text("sounds like a real person. Give an example of how this could be")
        self.text("used to scam someone.")
        self.multiline_field("", "ai_deepfake", 0.5 * inch)

        self.text("Q3: AI is also used for DEFENSE. Which of these are real ways AI", bold=True)
        self.text("helps protect us? (Check all that apply)")
        self.checkbox("Filtering spam and phishing emails from your inbox", "ai_def_spam")
        self.checkbox("Detecting unusual activity on your bank account", "ai_def_bank")
        self.checkbox("Making your password longer automatically", "ai_def_pw")
        self.checkbox("Monitoring networks for cyber attacks 24/7", "ai_def_monitor")

        self.space(0.1 * inch)

        self.text("Q4: Your grandma gets a phone call that sounds exactly like your", bold=True)
        self.text("voice saying you are in trouble and need money. But it is actually")
        self.text("an AI voice clone. What should she do to verify it is really you?")
        self.multiline_field("", "ai_voice_clone", 0.5 * inch)

        # === PAGE 8: Reflection + Bonus ===
        self.new_page()

        self.section_header("REFLECTION (10 points)", Colors.MEDIUM_BLUE)

        self.text("What is the most important cybersecurity tip you learned today? Why?", bold=True)
        self.multiline_field("", "reflection_1", 0.6 * inch)

        self.space(0.05 * inch)

        self.text("What is one thing you will change about how you use the internet", bold=True)
        self.text("after today's class?")
        self.multiline_field("", "reflection_2", 0.6 * inch)

        self.space(0.05 * inch)

        self.text("On a scale of 1-5, how confident do you feel about staying safe online?", bold=True)
        self.text_field("Rating (1-5):", "confidence_rating", 1.1 * inch, 1 * inch)
        self.multiline_field("Explain your rating:", "confidence_explain", 0.45 * inch)

        self.space(0.15 * inch)

        self.section_header("BONUS: Create a Cybersecurity Tip Poster (+10 points)", Colors.ORANGE)

        self.info_box(
            "Bonus Challenge",
            "Design a mini cybersecurity awareness poster! Write a catchy title, 3 safety tips, and a slogan that would convince other teenagers to take security seriously.",
            Colors.LIGHT_GRAY, 0.65 * inch
        )

        self.space(0.1 * inch)

        self.text_field("Poster Title:", "bonus_title", 1.0 * inch)
        self.text_field("Tip 1:", "bonus_tip1", 0.5 * inch)
        self.text_field("Tip 2:", "bonus_tip2", 0.5 * inch)
        self.text_field("Tip 3:", "bonus_tip3", 0.5 * inch)
        self.text_field("Slogan:", "bonus_slogan", 0.6 * inch)

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
    output_path = os.path.join(parent_dir, "2026-03-21_Classwork_Cybersecurity_Detective.pdf")

    pdf = ClassworkPDF(output_path)
    pdf.build()

    return output_path


if __name__ == "__main__":
    main()
