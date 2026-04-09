"""
Classwork PDF Generator - February 28, 2026
Command Line Translator: Windows & Mac Edition

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
    TERMINAL_GREEN = HexColor('#00C853')
    WINDOWS_BLUE = HexColor('#0078D7')
    MAC_GRAY = HexColor('#8E8E93')


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
                    "CLASSWORK: Command Line Translator")

        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Translate your Linux skills to Windows and Mac")

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
        # === PAGE 1: Student Info + Quick Translation ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.info_box(
            "Your Mission Today",
            "You are a Command Line Translator! Take the Linux commands you learned and translate them to work on YOUR computer (Windows or Mac).",
            Colors.LIGHT_BLUE, 0.7 * inch
        )

        self.space(0.15 * inch)

        self.text_field("My operating system:", "my_os", 1.7 * inch, 2.5 * inch)

        self.space(0.05 * inch)

        self.section_header("PART 1: Quick Translation (15 points)", Colors.ORANGE)

        self.text("Fill in the Windows CMD equivalent for each Linux command:", bold=True)
        self.space(0.1 * inch)

        translations = [
            ("Linux: ls", "trans_ls"),
            ("Linux: cat file.txt", "trans_cat"),
            ("Linux: rm file.txt", "trans_rm"),
            ("Linux: cp file.txt backup.txt", "trans_cp"),
            ("Linux: clear", "trans_clear"),
        ]

        for label, field_name in translations:
            self.text(label, bold=True, size=10, indent=0.1 * inch)
            self.text_field("Windows CMD:", field_name, 1.2 * inch, 3 * inch)

        # === PAGE 2: Translation Table Exercise ===
        self.new_page()

        self.section_header("PART 2: Complete the Translation Table (20 points)", Colors.TERMINAL_GREEN)

        self.text("Fill in the missing commands. Some cells are done for you!", bold=True)
        self.space(0.1 * inch)

        # Row 1: ls
        self.text("1. List files:", bold=True, indent=0.1 * inch)
        self.text("   Linux: ls", indent=0.1 * inch)
        self.text_field("   Windows CMD:", "table_ls_win", 1.3 * inch, 2.5 * inch)
        self.text("   Mac Terminal: ls", indent=0.1 * inch)
        self.space(0.05 * inch)

        # Row 2: touch
        self.text("2. Create empty file:", bold=True, indent=0.1 * inch)
        self.text("   Linux: touch file.txt", indent=0.1 * inch)
        self.text_field("   Windows CMD:", "table_touch_win", 1.3 * inch, 2.5 * inch)
        self.text_field("   Mac Terminal:", "table_touch_mac", 1.3 * inch, 2.5 * inch)
        self.space(0.05 * inch)

        # Row 3: cat
        self.text("3. View file contents:", bold=True, indent=0.1 * inch)
        self.text("   Linux: cat notes.txt", indent=0.1 * inch)
        self.text_field("   Windows CMD:", "table_cat_win", 1.3 * inch, 2.5 * inch)
        self.text_field("   Mac Terminal:", "table_cat_mac", 1.3 * inch, 2.5 * inch)
        self.space(0.05 * inch)

        # Row 4: move (given Windows)
        self.text("4. Move a file:", bold=True, indent=0.1 * inch)
        self.text_field("   Linux:", "table_mv_linux", 1.3 * inch, 2.5 * inch)
        self.text("   Windows CMD: move file.txt folder\\", indent=0.1 * inch)
        self.text_field("   Mac Terminal:", "table_mv_mac", 1.3 * inch, 2.5 * inch)

        # === PAGE 3: Hands-On Part 1 ===
        self.new_page()

        self.section_header("PART 3: Hands-On -- Try It on YOUR Computer! (25 points)", Colors.WINDOWS_BLUE)

        self.info_box(
            "Instructions",
            "Open Command Prompt (Windows) or Terminal (Mac) on your computer. Run each task and write what happened. Tip: On Windows, ping runs forever -- press Ctrl+C to stop it.",
            Colors.LIGHT_BLUE, 0.8 * inch
        )

        self.space(0.15 * inch)

        self.text("Task 1: List all files in your current directory.", bold=True)
        self.text_field("Command you typed:", "hands1_cmd", 1.6 * inch)
        self.multiline_field("What did you see?", "hands1_output", 0.5 * inch)

        self.text("Task 2: Create a new folder called 'cs_class'.", bold=True)
        self.text_field("Command you typed:", "hands2_cmd", 1.6 * inch)
        self.text_field("Did it work? (Yes/No):", "hands2_result", 1.8 * inch, 1.5 * inch)

        self.text("Task 3: Navigate into the 'cs_class' folder.", bold=True)
        self.text_field("Command you typed:", "hands3_cmd", 1.6 * inch)

        self.text("Task 4: Create a file called 'hello.txt' inside cs_class.", bold=True)
        self.text_field("Command you typed:", "hands4_cmd", 1.6 * inch)

        self.text("Task 5: Write 'I love computer science!' into hello.txt.", bold=True)
        self.text_field("Command you typed:", "hands5_cmd", 1.6 * inch)

        # === PAGE 4: Hands-On Part 2 + File Paths ===
        self.new_page()

        self.section_header("PART 3 (continued): More Hands-On Tasks", Colors.WINDOWS_BLUE)

        self.text("Task 6: View the contents of hello.txt.", bold=True)
        self.text_field("Command you typed:", "hands6_cmd", 1.6 * inch)
        self.text_field("What did it show?:", "hands6_output", 1.6 * inch)

        self.text("Task 7: Copy hello.txt to a new file called backup.txt.", bold=True)
        self.text_field("Command you typed:", "hands7_cmd", 1.6 * inch)

        self.text("Task 8: List the files to confirm both exist.", bold=True)
        self.text_field("Command you typed:", "hands8_cmd", 1.6 * inch)
        self.text_field("Files you see:", "hands8_files", 1.2 * inch)

        self.space(0.15 * inch)

        self.section_header("PART 4: File Paths (15 points)", Colors.PURPLE)

        self.multiple_choice(
            "What symbol does Windows use between folder names?",
            ["Forward slash /", "Backslash \\", "Dash -", "Period ."],
            "path_q1", 1
        )

        self.multiple_choice(
            "On Windows, file paths start with a...",
            ["Forward slash /", "Drive letter like C:\\", "Tilde ~", "Nothing"],
            "path_q2", 2
        )

        self.multiple_choice(
            "True or False: On Windows, MyFile.txt and myfile.txt are the SAME file.",
            ["True -- Windows ignores case", "False -- Windows cares about case"],
            "path_q3", 3
        )

        # === PAGE 5: Networking Revisited ===
        self.new_page()

        self.section_header("PART 5: Networking Commands Revisited (15 points)", Colors.GREEN)

        self.info_box(
            "Remember These?",
            "You used ipconfig, ping, tracert, and nslookup back in January! Now you understand they work on all operating systems. Windows uses 'ipconfig', Mac/Linux use 'ifconfig'.",
            Colors.LIGHT_GREEN, 0.8 * inch
        )

        self.space(0.15 * inch)

        self.text("Task 9: Run ipconfig (Windows) or ifconfig (Mac).", bold=True)
        self.text_field("Your IPv4 address:", "net_ip", 1.5 * inch)
        self.text_field("Default gateway:", "net_gateway", 1.3 * inch)

        self.space(0.15 * inch)

        self.text("Task 10: Run 'ping google.com' (press Ctrl+C to stop after a few replies).", bold=True)
        self.text_field("Average response time:", "net_ping", 1.8 * inch, 2 * inch)

        self.space(0.15 * inch)

        self.text("Task 11: What is the Windows command for tracing a route?", bold=True)
        self.text_field("Command:", "net_tracert", 1.0 * inch, 2 * inch)

        self.space(0.1 * inch)

        self.text("Task 12: What is the Mac/Linux command for tracing a route?", bold=True)
        self.text_field("Command:", "net_traceroute", 1.0 * inch, 2 * inch)

        self.space(0.15 * inch)

        self.text("Task 13: Which networking command is the SAME on all three OSes?", bold=True)
        self.multiple_choice("", [
            "ping",
            "ipconfig",
            "tracert",
            "ifconfig"
        ], "net_same")

        # === PAGE 6: Reflection + Bonus ===
        self.new_page()

        self.section_header("REFLECTION (10 points)", Colors.MEDIUM_BLUE)

        self.text("What is the biggest difference you noticed between using commands on your", bold=True)
        self.text("computer vs. using them on DistroSea Linux?")
        self.multiline_field("", "reflection", 0.8 * inch)

        self.space(0.1 * inch)

        self.text("Which do you prefer: Linux terminal or your computer's command line? Why?", bold=True)
        self.multiline_field("", "preference", 0.6 * inch)

        self.space(0.1 * inch)

        self.text("AI tools like Claude Code and Codex run inside the terminal.", bold=True)
        self.text("Why do you think AI developers chose the command line for their tools?")
        self.multiline_field("", "ai_reflection", 0.6 * inch)

        self.space(0.15 * inch)

        self.section_header("BONUS: Power User Challenge (+10 points)", Colors.ORANGE)

        self.info_box(
            "Bonus Task",
            "Run 'systeminfo' (Windows) or 'sw_vers' (Mac) on your computer. Write down three interesting facts about your system!",
            Colors.LIGHT_GRAY, 0.65 * inch
        )

        self.space(0.15 * inch)

        self.text_field("Fact 1:", "bonus_fact1", 0.6 * inch)
        self.text_field("Fact 2:", "bonus_fact2", 0.6 * inch)
        self.text_field("Fact 3:", "bonus_fact3", 0.6 * inch)

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
    output_path = os.path.join(parent_dir, "2026-02-28_Classwork_Command_Line_Translator.pdf")

    pdf = ClassworkPDF(output_path)
    pdf.build()

    return output_path


if __name__ == "__main__":
    main()
