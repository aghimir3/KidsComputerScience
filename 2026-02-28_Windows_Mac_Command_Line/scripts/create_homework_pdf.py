"""
Homework PDF Generator - February 28, 2026
Command Line Polyglot: Linux, Windows & Mac

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
    TERMINAL_GREEN = HexColor('#00C853')
    WINDOWS_BLUE = HexColor('#0078D7')


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
                    "HOMEWORK: Command Line Polyglot")

        c.setFont("Helvetica", 10)
        c.setFillColor(Colors.SKY_BLUE)
        c.drawString(Layout.MARGIN, Layout.HEIGHT - 0.8 * inch,
                    "Prove you can speak Linux, Windows, AND Mac!")

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
        # === PAGE 1: Student Info + Command Translation ===
        self.new_page()

        self.section_header("Student Information", Colors.DARK_BLUE)
        self.text_field("Name:", "student_name", 0.55 * inch)
        self.text_field("Date:", "date", 0.55 * inch, 2 * inch)

        self.space(0.05 * inch)

        self.info_box(
            "What is a Polyglot?",
            "A 'polyglot' is someone who speaks multiple languages. In this homework, you will prove you can speak three command line languages: Linux, Windows CMD, and Mac Terminal!",
            Colors.LIGHT_BLUE, 0.7 * inch
        )

        self.section_header("PART 1: Command Translation (25 points)", Colors.ORANGE)

        self.text("For each task, write the command for ALL THREE operating systems.", bold=True)
        self.space(0.05 * inch)

        tasks = [
            ("1", "List all files in the current folder"),
            ("2", "View the contents of a file called notes.txt"),
            ("3", "Delete a file called old_data.txt"),
            ("4", "Copy report.txt to report_backup.txt"),
            ("5", "Rename essay.txt to final_essay.txt"),
        ]

        for num, task in tasks:
            self.text(f"Q{num}: {task}", bold=True)
            self.text_field("Linux:", f"hw_q{num}_linux", 0.55 * inch, 3 * inch)
            self.text_field("Windows:", f"hw_q{num}_win", 0.75 * inch, 3 * inch)
            self.text_field("Mac:", f"hw_q{num}_mac", 0.5 * inch, 3 * inch)

        # === PAGE 2: Predict the Output ===
        self.new_page()

        self.section_header("PART 2: Predict the Output (25 points)", Colors.TERMINAL_GREEN)

        self.text("Q6: A student types these WINDOWS commands. What will 'dir' show?", bold=True)
        self.text("    mkdir projects", size=10, indent=0.2 * inch)
        self.text("    cd projects", size=10, indent=0.2 * inch)
        self.text("    echo. > app.txt", size=10, indent=0.2 * inch)
        self.text("    echo. > readme.txt", size=10, indent=0.2 * inch)
        self.text("    del app.txt", size=10, indent=0.2 * inch)
        self.text("    dir", size=10, indent=0.2 * inch)
        self.text_field("What files does dir show?", "hw_predict1", 2.2 * inch)

        self.space(0.1 * inch)

        self.text("Q7: A student types these MAC commands. What will 'cat journal.txt' show?", bold=True)
        self.text('    echo "Day 1: Learned Linux" > journal.txt', size=10, indent=0.2 * inch)
        self.text('    echo "Day 2: Learned Windows" >> journal.txt', size=10, indent=0.2 * inch)
        self.text("    cat journal.txt", size=10, indent=0.2 * inch)
        self.multiline_field("Output:", "hw_predict2", 0.5 * inch)

        self.space(0.05 * inch)

        self.multiple_choice(
            "A student runs 'ren report.txt summary.txt' on Windows. What happened?",
            ["Copied the file", "Deleted the file", "Renamed the file", "Created a new folder"],
            "hw_predict3", 8
        )

        self.multiple_choice(
            "On Windows, a student types 'cd' with no arguments. What will it show?",
            ["A list of files", "The current directory path", "An error", "Nothing"],
            "hw_predict4", 9
        )

        self.multiple_choice(
            "On Mac, would 'rm MyFile.txt' and 'rm myfile.txt' delete the SAME file?",
            ["True -- Mac ignores case", "False -- Mac is case-sensitive"],
            "hw_predict5", 10
        )

        # === PAGE 3: Try It At Home ===
        self.new_page()

        self.section_header("PART 3: Try It At Home (25 points)", Colors.WINDOWS_BLUE)

        self.info_box(
            "Instructions",
            "Open Command Prompt (Windows) or Terminal (Mac) on your home computer. Complete these tasks and write down what you did. On Windows, use 'ping -n 4 google.com' to send only 4 pings.",
            Colors.LIGHT_BLUE, 0.8 * inch
        )

        self.space(0.15 * inch)

        self.text("Q11: Find your current directory (where you are right now).", bold=True)
        self.text_field("Command you used:", "hw_try1_cmd", 1.6 * inch)
        self.text_field("Your current directory:", "hw_try1_result", 1.7 * inch)

        self.space(0.1 * inch)

        self.text("Q12: Create a folder called 'homework_week3', navigate into it,", bold=True)
        self.text("and create a file called 'my_notes.txt'. Write 'Command line is fun!' into it.")
        self.multiline_field("Commands you used (list them all):", "hw_try2_cmds", 0.7 * inch)

        self.space(0.1 * inch)

        self.text("Q13: Run a networking command: ping google.com", bold=True)
        self.text_field("Response time (ms):", "hw_try3_ping", 1.6 * inch, 2 * inch)
        self.multiline_field("What does this tell you about your internet connection?", "hw_try3_explain", 0.6 * inch)

        # === PAGE 4: Reflection + Bonus ===
        self.new_page()

        self.section_header("PART 4: Reflection (25 points)", Colors.PURPLE)

        self.text("Q14: Which OS command line do you find easier -- Windows or Mac/Linux? Why?", bold=True)
        self.multiline_field("", "hw_reflect1", 0.55 * inch)

        self.space(0.08 * inch)

        self.text("Q15: A friend says: 'I only need to learn Linux commands because they are", bold=True)
        self.text("the most popular.' Do you agree or disagree? Explain using what you learned.")
        self.multiline_field("", "hw_reflect2", 0.55 * inch)

        self.space(0.08 * inch)

        self.text("Q16: In your own words, explain what 'the concepts are the same, only the", bold=True)
        self.text("syntax changes' means for command lines.")
        self.multiline_field("", "hw_reflect3", 0.55 * inch)

        self.space(0.08 * inch)

        self.text("Q17: Real AI tools like Claude Code and OpenAI Codex run inside the", bold=True)
        self.text("terminal -- the same terminal you are learning! Why do you think knowing")
        self.text("command line skills matters if you want to work with AI someday?")
        self.multiline_field("", "hw_reflect_ai", 0.55 * inch)

        self.space(0.15 * inch)

        self.section_header("BONUS: Command Line Detective (+5 points)", Colors.ORANGE)

        self.info_box(
            "Bonus Task",
            "Run 'systeminfo' (Windows) or 'system_profiler SPHardwareDataType' (Mac) on your computer.",
            Colors.LIGHT_GRAY, 0.55 * inch
        )

        self.space(0.15 * inch)

        self.text_field("Your CPU:", "bonus_cpu", 0.8 * inch)
        self.text_field("Your RAM:", "bonus_ram", 0.8 * inch)

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
    output_path = os.path.join(parent_dir, "2026-02-28_Homework_Command_Line_Polyglot.pdf")

    pdf = HomeworkPDF(output_path)
    pdf.build()

    return output_path


if __name__ == "__main__":
    main()
