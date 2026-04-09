"""
Homework PDF Generator - March 21, 2026
Cybersecurity & Staying Safe Online

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


# =============================================================================
# PDF BUILDER
# =============================================================================

class HomeworkPDF:
    def __init__(self, output_path):
        self.output_path = output_path
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Homework: Cybersecurity & Staying Safe Online")
        self.page_num = 0
        self.total_pages = 6
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
                    "HOMEWORK: Cybersecurity & Staying Safe Online")

        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Review what you learned and apply it at home!")

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
        # === PAGE 1: Matching + True/False ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.section_header("SECTION 1: Matching (15 points)", Colors.SHIELD_BLUE)

        self.text("Match each term with its definition. Write the letter in the box.", bold=True)
        self.space(0.05 * inch)

        self.text("A. A second verification step beyond your password", size=9)
        self.text("B. Fake emails, texts, or websites designed to steal your information", size=9)
        self.text("C. Harmful software like viruses, ransomware, and spyware", size=9)
        self.text("D. Tricking people into giving up confidential information", size=9)
        self.text("E. Protecting computers, networks, and data from threats", size=9)
        self.text("F. The trail of data you leave behind on the internet", size=9)

        self.space(0.05 * inch)

        matches = [
            ("1. Cybersecurity", "match_1"),
            ("2. Phishing", "match_2"),
            ("3. Malware", "match_3"),
            ("4. Social Engineering", "match_4"),
            ("5. Two-Factor Authentication (2FA)", "match_5"),
            ("6. Digital Footprint", "match_6"),
        ]

        for label, field_name in matches:
            self.text_field(label, field_name, 2.5 * inch, 0.5 * inch)

        # === PAGE 2: True/False + Short Answer ===
        self.new_page()

        self.section_header("SECTION 2: True or False (15 points)", Colors.DANGER_RED)

        self.text("Write T for True or F for False in each box.", bold=True)
        self.space(0.05 * inch)

        tf_statements = [
            ("1.", "A strong password should be at least 12 characters long.", "tf_1"),
            ("2.", "It is safe to use the same password for all your accounts.", "tf_2"),
            ("3.", "Phishing emails often create a sense of urgency or fear.", "tf_3"),
            ("4.", "HTTPS means a website is encrypted and more secure.", "tf_4"),
            ("5.", "If a friend sends you a link, it is always safe to click.", "tf_5"),
            ("6.", "Two-Factor Authentication adds a second layer of security.", "tf_6"),
            ("7.", "A company will sometimes ask for your password by email.", "tf_7"),
            ("8.", "Your digital footprint can be seen by colleges and employers.", "tf_8"),
            ("9.", "Social engineering targets computers, not people.", "tf_9"),
            ("10.", "Keeping your software updated helps protect against security threats.", "tf_10"),
        ]

        for num, statement, field_name in tf_statements:
            c = self.c
            c.acroForm.textfield(
                name=field_name,
                x=Layout.MARGIN,
                y=self.y - 4,
                width=0.3 * inch,
                height=0.2 * inch,
                borderColor=Colors.MEDIUM_BLUE,
                fillColor=Colors.LIGHT_GRAY,
                textColor=black,
                fontSize=10,
                borderWidth=1,
                maxlen=0,
            )
            c.setFillColor(Colors.DARK_GRAY)
            c.setFont("Helvetica", 9)
            c.drawString(Layout.MARGIN + 0.4 * inch, self.y, f"{num} {statement}")
            self.y -= 0.28 * inch

        # === PAGE 3: Short Answer ===
        self.new_page()

        self.section_header("SECTION 3: Short Answer (25 points)", Colors.SAFE_GREEN)

        self.text("Answer each question in 1-3 sentences.", bold=True)
        self.space(0.05 * inch)

        self.text("Q1: What is the difference between a password and a passphrase?", bold=True)
        self.text("Give an example of each.")
        self.multiline_field("", "sa_1", 0.55 * inch)

        self.text("Q2: Name three red flags that help you identify a phishing email.", bold=True)
        self.multiline_field("", "sa_2", 0.55 * inch)

        self.text("Q3: Explain what social engineering is in your own words.", bold=True)
        self.text("Give one example of how it might happen to a teenager.")
        self.multiline_field("", "sa_3", 0.55 * inch)

        self.text("Q4: Why is it important to use a different password for each account?", bold=True)
        self.text("What could happen if you reuse the same password everywhere?")
        self.multiline_field("", "sa_4", 0.55 * inch)

        self.text("Q5: What is a digital footprint, and why should you care about yours?", bold=True)
        self.multiline_field("", "sa_5", 0.55 * inch)

        # === PAGE 4: Scenarios + Hands-On ===
        self.new_page()

        self.section_header("SECTION 4: Scenario Questions (20 points)", Colors.ORANGE)

        self.text("Read each scenario and answer the question.", bold=True)
        self.space(0.05 * inch)

        self.text("Q1: You get a text saying your bank account is frozen. It asks you to", bold=True)
        self.text("call a number and provide your Social Security number. What do you do?")
        self.multiline_field("", "scenario_1", 0.5 * inch)

        self.text("Q2: A website asks you to enter your email and password. The URL bar", bold=True)
        self.text("shows http:// (not https://) and the domain is faceb00k-login.com.", bold=True)
        self.text("What should you do?")
        self.multiline_field("", "scenario_2", 0.5 * inch)

        self.text("Q3: Your friend tells you they use '123456' as their password because", bold=True)
        self.text("it is easy to remember. What would you say to convince them to change it?")
        self.multiline_field("", "scenario_3", 0.5 * inch)

        self.text("Q4: You post a photo on social media that shows your school name", bold=True)
        self.text("on your uniform and your street sign in the background. Why could")
        self.text("this be a problem?")
        self.multiline_field("", "scenario_4", 0.5 * inch)

        # === PAGE 5: AI & Cybersecurity ===
        self.new_page()

        self.section_header("SECTION 5: AI & Cybersecurity (10 points)", Colors.SHIELD_BLUE)

        self.info_box(
            "AI Changes Everything",
            "Artificial Intelligence is making cybersecurity both harder AND easier. AI can create more convincing scams, but it also powers the tools that protect us. Next month we start our AI unit -- this is a preview!",
            Colors.LIGHT_BLUE, 0.7 * inch
        )

        self.space(0.1 * inch)

        self.text("Q1: AI can now clone someone's voice from just a few seconds of", bold=True)
        self.text("audio. How could a scammer use this to trick a family member?")
        self.multiline_field("", "ai_q1", 0.55 * inch)

        self.text("Q2: Old phishing emails often had spelling mistakes and bad grammar.", bold=True)
        self.text("Now AI tools like ChatGPT can write perfect emails. What other red")
        self.text("flags (besides spelling) can you still use to spot a phishing email?")
        self.multiline_field("", "ai_q2", 0.55 * inch)

        self.text("Q3: A 'deepfake' is an AI-generated video that makes it look like a", bold=True)
        self.text("real person is saying something they never said. Why is this dangerous?")
        self.multiline_field("", "ai_q3", 0.55 * inch)

        self.text("Q4: AI is also used to PROTECT us. Name one way AI helps keep", bold=True)
        self.text("you safe online (think about email, banking, or social media).")
        self.multiline_field("", "ai_q4", 0.55 * inch)

        # === PAGE 6: Hands-On + Reflection + Bonus ===
        self.new_page()

        self.section_header("SECTION 5: Hands-On Challenge (15 points)", Colors.TEAL)

        self.info_box(
            "Instructions",
            "Complete these tasks at home and write down what you did. Ask a parent or guardian for help if needed.",
            Colors.LIGHT_GREEN, 0.55 * inch
        )

        self.space(0.1 * inch)

        self.text("Task 1: Check if any of your accounts have 2FA turned on.", bold=True)
        self.text("If not, turn it on for at least ONE account (email, gaming, social media).")
        self.text_field("Account you checked:", "hands_account", 1.5 * inch)
        self.text_field("2FA on? (Yes/No):", "hands_2fa_status", 1.4 * inch, 2 * inch)
        self.text_field("Did you turn it on?:", "hands_2fa_action", 1.5 * inch, 2 * inch)

        self.space(0.08 * inch)

        self.text("Task 2: Create a strong passphrase for a NEW account (or practice).", bold=True)
        self.text_field("Your passphrase:", "hands_passphrase", 1.3 * inch)
        self.text("(Do NOT write a passphrase you actually use! Make a practice one.)", size=8)

        self.space(0.1 * inch)

        self.section_header("SECTION 6: Reflection (10 points)", Colors.PURPLE)

        self.text("Q1: What is the most surprising thing you learned about cybersecurity?", bold=True)
        self.multiline_field("", "reflect_1", 0.5 * inch)

        self.text("Q2: Rate your cybersecurity habits BEFORE and AFTER this lesson (1-5):", bold=True)
        self.text_field("Before this lesson:", "reflect_before", 1.4 * inch, 1 * inch)
        self.text_field("After this lesson:", "reflect_after", 1.3 * inch, 1 * inch)

        self.space(0.1 * inch)

        self.section_header("BONUS: Teach Someone Else (+5 points)", Colors.ORANGE)

        self.text("Teach a family member ONE cybersecurity tip from this week.", bold=True)
        self.text_field("Who did you teach?", "bonus_who", 1.5 * inch, 2.5 * inch)
        self.text_field("What tip?", "bonus_tip", 0.8 * inch)
        self.text_field("Their reaction?", "bonus_reaction", 1.1 * inch)

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
    output_path = os.path.join(parent_dir, "2026-03-21_Homework_Cybersecurity_Safe_Online.pdf")

    pdf = HomeworkPDF(output_path)
    pdf.build()

    return output_path


if __name__ == "__main__":
    main()
