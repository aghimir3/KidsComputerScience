"""Create an advanced August 1 fillable classwork PDF for fast finishers."""

import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


WIDTH, HEIGHT = letter
NAVY = colors.HexColor("#061229")
CYAN = colors.HexColor("#00CFE8")
PURPLE = colors.HexColor("#7C4DFF")
GREEN = colors.HexColor("#00B876")
ORANGE = colors.HexColor("#F28C00")
MAGENTA = colors.HexColor("#D92C88")
LIGHT = colors.HexColor("#F4F8FC")
PALE_BLUE = colors.HexColor("#EAF5FB")
PALE_GREEN = colors.HexColor("#EAF8F2")
GRAY = colors.HexColor("#526173")
BORDER = colors.HexColor("#AABBCB")


class AdvancedPDF:
    def __init__(self, output_path):
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle("Advanced Classwork: TypeScript Decision Arcade")
        self.page = 0

    def start_page(self, title, subtitle):
        if self.page:
            self.footer()
            self.c.showPage()
        self.page += 1
        self.c.setFillColor(NAVY)
        self.c.rect(0, HEIGHT - 92, WIDTH, 92, fill=1, stroke=0)
        self.c.setFillColor(CYAN)
        self.c.rect(0, HEIGHT - 96, WIDTH, 4, fill=1, stroke=0)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 19)
        self.c.drawString(40, HEIGHT - 46, title)
        self.c.setFont("Helvetica", 9.5)
        self.c.drawString(40, HEIGHT - 68, subtitle)

    def footer(self):
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica", 8)
        self.c.drawString(40, 24, "Kids Computer Science | Advanced August 1 classwork")
        self.c.drawRightString(WIDTH - 40, 24, f"Page {self.page}")

    def text(self, x, y, value, size=9.5, bold=False, color=NAVY, font=None):
        self.c.setFillColor(color)
        self.c.setFont(font or ("Helvetica-Bold" if bold else "Helvetica"), size)
        self.c.drawString(x, y, value)

    def wrapped(self, x, y, value, width_chars=86, leading=12, size=9.2, bold=False):
        words = value.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > width_chars and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))
        for line in lines:
            self.text(x, y, line, size=size, bold=bold)
            y -= leading
        return y

    def section(self, y, title, points, color):
        self.c.setFillColor(color)
        self.c.roundRect(40, y - 6, WIDTH - 80, 29, 5, fill=1, stroke=0)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(52, y + 4, title)
        self.c.drawRightString(WIDTH - 52, y + 4, points)

    def field(self, name, x, y, w, h=22, multiline=False, font_size=8.5):
        self.c.acroForm.textfield(
            name=name,
            x=x,
            y=y,
            width=w,
            height=h,
            borderStyle="inset",
            borderColor=BORDER,
            fillColor=colors.white,
            textColor=NAVY,
            forceBorder=True,
            fontName="Helvetica",
            fontSize=font_size,
            fieldFlags=4096 if multiline else 0,
            maxlen=0,
        )

    def checkbox(self, name, x, y, label):
        self.c.acroForm.checkbox(
            name=name,
            x=x,
            y=y,
            size=12,
            buttonStyle="check",
            borderColor=NAVY,
            fillColor=colors.white,
            textColor=GREEN,
            forceBorder=True,
        )
        self.text(x + 18, y + 2, label, size=8.8)

    def code_box(self, x, y, w, lines, font_size=7.8, leading=9.8):
        height = 17 + len(lines) * leading
        self.c.setFillColor(PALE_BLUE)
        self.c.setStrokeColor(CYAN)
        self.c.roundRect(x, y - height, w, height, 5, fill=1, stroke=1)
        current_y = y - 15
        for line in lines:
            self.text(x + 9, current_y, line, size=font_size, color=NAVY, font="Courier")
            current_y -= leading
        return y - height

    def note_box(self, x, y, w, h, title, body):
        self.c.setFillColor(PALE_GREEN)
        self.c.setStrokeColor(BORDER)
        self.c.roundRect(x, y - h, w, h, 5, fill=1, stroke=1)
        self.text(x + 10, y - 18, title, bold=True, color=GREEN)
        self.wrapped(x + 10, y - 35, body, width_chars=79, leading=11, size=8.5)

    def save(self):
        self.footer()
        self.c.save()


def student_header(pdf):
    pdf.text(40, 662, "Student name", bold=True)
    pdf.field("adv_student_name", 125, 650, 255)
    pdf.text(400, 662, "Date", bold=True)
    pdf.field("adv_date", 435, 650, 135)


def create_advanced_classwork(output_path):
    pdf = AdvancedPDF(output_path)
    pdf.start_page(
        "Advanced Classwork: Decision Arcade",
        "For fast finishers | 100 points + 10 bonus | No new syntax beyond today's lesson",
    )
    student_header(pdf)

    pdf.section(604, "Part 1 - Silent Trace Challenge", "20 points", CYAN)
    pdf.wrapped(
        48,
        574,
        "Do not run the code yet. Trace it by hand. Write the one message that prints for each score.",
    )
    pdf.code_box(
        48,
        542,
        522,
        [
            "let score: number = 76;",
            "",
            "if (score >= 95) {",
            '  console.log("Mythic");',
            "} else if (score >= 85) {",
            '  console.log("Elite");',
            "} else if (score >= 75) {",
            '  console.log("Veteran");',
            "} else if (score >= 60) {",
            '  console.log("Rising");',
            "} else {",
            '  console.log("Training");',
            "}",
        ],
    )
    values = [("96", "trace_96"), ("95", "trace_95"), ("94", "trace_94"),
              ("85", "trace_85"), ("84", "trace_84"), ("76", "trace_76"),
              ("75", "trace_75"), ("74", "trace_74"), ("60", "trace_60"),
              ("59", "trace_59")]
    y = 374
    for index, (value, name) in enumerate(values):
        x = 48 + (index % 2) * 262
        if index and index % 2 == 0:
            y -= 42
        pdf.text(x, y + 8, f"score = {value}", bold=True)
        pdf.field(name, x + 78, y - 4, 166)
    pdf.text(48, 170, "For score 76, explain every condition checked until the ladder stops:", bold=True)
    pdf.field("trace_76_explanation", 48, 74, 522, 78, multiline=True)

    pdf.start_page("Logic Repair Lab", "Advanced classwork continued")
    pdf.section(646, "Part 2 - The Code Runs, But the Game Is Wrong", "20 points", MAGENTA)
    pdf.wrapped(
        48,
        615,
        "A student wanted four robot battery states. The rules are below, but the ladder is in a bad order.",
    )
    pdf.text(48, 583, "Rules: 90+ Overcharged, 70+ Ready, 35+ Low Power, lower than 35 Shutdown", bold=True)
    bottom = pdf.code_box(
        48,
        556,
        522,
        [
            "let battery: number = 92;",
            "",
            "if (battery >= 35) {",
            '  console.log("Low Power");',
            "} else if (battery >= 70) {",
            '  console.log("Ready");',
            "} else if (battery >= 90) {",
            '  console.log("Overcharged");',
            "} else {",
            '  console.log("Shutdown");',
            "}",
        ],
    )
    pdf.text(48, bottom - 22, "What does it print for 92?", bold=True)
    pdf.field("repair_prints_92", 205, bottom - 34, 365)
    pdf.text(48, bottom - 62, "What should it print for 92?", bold=True)
    pdf.field("repair_should_92", 205, bottom - 74, 365)
    pdf.text(48, bottom - 102, "Which condition catches 92 too early?", bold=True)
    pdf.field("repair_early_condition", 250, bottom - 114, 320)
    pdf.text(48, bottom - 146, "Rewrite the ladder in the correct order:", bold=True)
    pdf.field("repair_fixed_code", 48, 86, 522, 160, multiline=True, font_size=8)
    pdf.note_box(
        48,
        70,
        522,
        36,
        "Constraint",
        "Use only the same if / else if / else structure. Do not add loops, functions, arrays, or input.",
    )

    pdf.start_page("Boundary Test Designer", "Advanced classwork continued")
    pdf.section(646, "Part 3 - Prove the Repair Works", "20 points", ORANGE)
    pdf.wrapped(
        48,
        615,
        "Choose test values that prove each rule works. Include each exact boundary and the number just below it.",
    )
    rows = [
        ("Overcharged boundary", "test_over_boundary", "test_over_output"),
        ("Just below Overcharged", "test_under_over", "test_under_over_output"),
        ("Ready boundary", "test_ready_boundary", "test_ready_output"),
        ("Just below Ready", "test_under_ready", "test_under_ready_output"),
        ("Low Power boundary", "test_low_boundary", "test_low_output"),
        ("Just below Low Power", "test_under_low", "test_under_low_output"),
        ("One extra high value", "test_extra_high", "test_extra_high_output"),
        ("One extra low value", "test_extra_low", "test_extra_low_output"),
    ]
    y = 560
    pdf.text(48, y + 24, "Test purpose", bold=True)
    pdf.text(244, y + 24, "Value", bold=True)
    pdf.text(340, y + 24, "Expected output", bold=True)
    for label, value_name, output_name in rows:
        pdf.text(48, y, label)
        pdf.field(value_name, 244, y - 10, 76)
        pdf.field(output_name, 340, y - 10, 230)
        y -= 42
    pdf.text(48, 166, "Which two tests are the most important, and why?", bold=True)
    pdf.field("most_important_tests", 48, 78, 522, 72, multiline=True)

    pdf.start_page("Build a Harder Decision Game", "Advanced classwork continued")
    pdf.section(646, "Part 4 - Design With Overlapping Conditions", "25 points", GREEN)
    pdf.wrapped(
        48,
        615,
        "Create a game ladder where lower conditions would accidentally catch higher values if ordered badly.",
    )
    pdf.text(48, 575, "Theme", bold=True)
    pdf.field("design_theme", 98, 563, 472)
    pdf.text(48, 532, "Write your rules in English before coding:", bold=True)
    pdf.field("design_rules", 48, 436, 522, 78, multiline=True)
    pdf.text(48, 405, "Write your TypeScript ladder:", bold=True)
    pdf.field("design_code", 48, 185, 522, 202, multiline=True, font_size=8)
    pdf.text(48, 155, "Explain why your order goes from highest to lowest:", bold=True)
    pdf.field("design_order_reason", 48, 79, 522, 60, multiline=True)

    pdf.start_page("Expert Debug Reflection", "Advanced classwork conclusion")
    pdf.section(646, "Part 5 - Debug Without Guessing", "15 points", PURPLE)
    pdf.wrapped(
        48,
        615,
        "Answer like a careful programmer. The goal is evidence, not speed.",
    )
    pdf.text(48, 574, "1. A program compiles. What still might be wrong?", bold=True)
    pdf.field("reflect_compile_wrong", 48, 508, 522, 50, multiline=True)
    pdf.text(48, 472, "2. How can boundary values reveal an incorrect condition?", bold=True)
    pdf.field("reflect_boundary", 48, 406, 522, 50, multiline=True)
    pdf.text(48, 370, "3. Why should humans test AI-written decision code?", bold=True)
    pdf.field("reflect_ai", 48, 304, 522, 50, multiline=True)
    pdf.section(258, "Bonus - Create a Bug on Purpose", "+10 points", ORANGE)
    pdf.wrapped(
        48,
        228,
        "Make a wrong-order version of your own ladder. Predict the wrong output, then explain the fix.",
    )
    pdf.field("bonus_intentional_bug", 48, 88, 522, 122, multiline=True, font_size=8)
    pdf.c.setFillColor(LIGHT)
    pdf.c.roundRect(40, 45, WIDTH - 80, 24, 4, fill=1, stroke=0)
    pdf.text(52, 53, "Submit to Microsoft Teams AND Ishwari Raut ma'am if your teacher asks for this extension.", bold=True, size=8.4)
    pdf.save()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lesson_dir = os.path.dirname(script_dir)
    create_advanced_classwork(
        os.path.join(lesson_dir, "2026-08-01_Advanced_Classwork_Decision_Arcade.pdf")
    )
    print("Created advanced August 1 classwork PDF")


if __name__ == "__main__":
    main()
