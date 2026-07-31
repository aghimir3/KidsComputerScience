"""Create fillable August 1 classwork and homework PDFs."""

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
GRAY = colors.HexColor("#526173")
BORDER = colors.HexColor("#AABBCB")


class FillableLessonPDF:
    def __init__(self, output_path, title, short_title):
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle(title)
        self.page = 0
        self.short_title = short_title

    def start_page(self, title, subtitle=""):
        if self.page:
            self.c.showPage()
        self.page += 1
        self.c.setFillColor(NAVY)
        self.c.rect(0, HEIGHT - 92, WIDTH, 92, fill=1, stroke=0)
        self.c.setFillColor(CYAN)
        self.c.rect(0, HEIGHT - 96, WIDTH, 4, fill=1, stroke=0)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 20)
        self.c.drawString(40, HEIGHT - 46, title)
        if subtitle:
            self.c.setFont("Helvetica", 9.5)
            self.c.drawString(40, HEIGHT - 68, subtitle)

    def footer(self):
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica", 8)
        self.c.drawString(40, 24, f"Kids Computer Science - {self.short_title}")
        self.c.drawRightString(WIDTH - 40, 24, f"Page {self.page}")

    def section(self, y, title, points="", color=PURPLE):
        self.c.setFillColor(color)
        self.c.roundRect(40, y - 6, WIDTH - 80, 29, 5, fill=1, stroke=0)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 12.5)
        self.c.drawString(52, y + 4, title)
        if points:
            self.c.drawRightString(WIDTH - 52, y + 4, points)

    def text(self, x, y, value, size=10, bold=False, color=NAVY, font=None):
        self.c.setFillColor(color)
        if font:
            font_name = font
        else:
            font_name = "Helvetica-Bold" if bold else "Helvetica"
        self.c.setFont(font_name, size)
        self.c.drawString(x, y, value)

    def wrapped(self, x, y, value, width_chars=88, leading=13, size=9.5, bold=False):
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

    def field(self, name, x, y, w, h=22, multiline=False, font_size=9):
        flags = 4096 if multiline else 0
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
            fieldFlags=flags,
            maxlen=0,
        )

    def checkbox(self, name, x, y, label, size=9.5):
        self.c.acroForm.checkbox(
            name=name,
            x=x,
            y=y,
            size=13,
            buttonStyle="check",
            borderColor=NAVY,
            fillColor=colors.white,
            textColor=GREEN,
            forceBorder=True,
        )
        self.text(x + 20, y + 2, label, size=size)

    def code_box(self, x, y, w, lines, font_size=8.7, leading=12):
        h = 18 + len(lines) * leading
        self.c.setFillColor(PALE_BLUE)
        self.c.setStrokeColor(CYAN)
        self.c.roundRect(x, y - h, w, h, 5, fill=1, stroke=1)
        current_y = y - 17
        for line in lines:
            self.text(x + 10, current_y, line, size=font_size, color=NAVY, font="Courier")
            current_y -= leading
        return y - h

    def note_box(self, x, y, w, h, title, body):
        self.c.setFillColor(LIGHT)
        self.c.setStrokeColor(BORDER)
        self.c.roundRect(x, y - h, w, h, 5, fill=1, stroke=1)
        self.text(x + 10, y - 18, title, size=9.5, bold=True, color=PURPLE)
        self.wrapped(x + 10, y - 35, body, width_chars=82, leading=12, size=8.8)

    def save(self):
        self.footer()
        self.c.save()


def student_header(pdf, prefix):
    pdf.text(40, 662, "Student name", bold=True)
    pdf.field(f"{prefix}_student_name", 125, 650, 255)
    pdf.text(400, 662, "Date", bold=True)
    pdf.field(f"{prefix}_date", 435, 650, 135)


def create_classwork(output_path):
    pdf = FillableLessonPDF(
        output_path,
        "Classwork: VS Code and TypeScript Setup",
        "August 1, 2026",
    )
    pdf.start_page(
        "Classwork: VS Code and TypeScript Setup",
        "100 points + 10 bonus points | Install once, then write, compile, and run",
    )
    student_header(pdf, "cw")

    pdf.section(604, "Part 1 - Open the Coding Tools", "20 points", CYAN)
    pdf.wrapped(
        48,
        573,
        "Open VS Code and its terminal. Windows students use Command Prompt. macOS students use the normal zsh terminal.",
    )
    pdf.text(48, 525, "Run node --version. Record the output:", bold=True)
    pdf.field("cw_node_version", 280, 513, 290)
    pdf.text(48, 482, "Run npm --version. Record the output:", bold=True)
    pdf.field("cw_npm_version", 275, 470, 295)
    pdf.text(48, 438, "If a command failed, copy the exact error or explain it:", bold=True)
    pdf.field("cw_tool_error", 48, 360, 522, 62, multiline=True)

    pdf.section(320, "Part 2 - Install TypeScript Once", "20 points", GREEN)
    pdf.text(48, 287, "Follow the teacher, then run:", bold=True)
    bottom = pdf.code_box(48, 270, 522, ["npm install -g typescript", "tsc --version"], font_size=9.5)
    pdf.text(48, bottom - 25, "TypeScript version or exact error:", bold=True)
    pdf.field("cw_tsc_version", 235, bottom - 37, 335)
    pdf.text(48, bottom - 76, "What does global mean in this lesson?", bold=True)
    pdf.field("cw_global_meaning", 48, 68, 522, 66, multiline=True)
    pdf.footer()

    pdf.start_page("Workspace and First Run", "Classwork continued")
    pdf.section(646, "Part 3 - Create a Workspace", "15 points", PURPLE)
    checks = [
        ("cw_folder_root", "Created or opened KidsComputerScience"),
        ("cw_folder_date", "Created 2026-08-01-decisions inside it"),
        ("cw_folder_open", "Opened the dated folder in VS Code"),
        ("cw_file_saved", "Created and saved decisions.ts"),
    ]
    y = 606
    for name, label in checks:
        pdf.checkbox(name, 52, y, label)
        y -= 31
    pdf.text(48, 468, "Folder and file names shown in the Explorer:", bold=True)
    pdf.field("cw_workspace_names", 48, 424, 522, 31)
    pdf.text(48, 390, "Why is it safe to trust this workspace?", bold=True)
    pdf.field("cw_workspace_trust", 48, 328, 522, 48, multiline=True)

    pdf.section(286, "Part 4 - Compile and Run", "20 points", ORANGE)
    bottom = pdf.code_box(
        48,
        258,
        522,
        [
            'let score: number = 82;',
            '',
            'if (score >= 70) {',
            '  console.log("Hero rank!");',
            '} else {',
            '  console.log("Keep training!");',
            '}',
        ],
        font_size=8.4,
        leading=11,
    )
    pdf.text(48, bottom - 18, "1. Compiler command", bold=True)
    pdf.field("cw_compile_command", 48, bottom - 50, 242)
    pdf.text(318, bottom - 18, "2. New file", bold=True)
    pdf.field("cw_generated_file", 318, bottom - 50, 252)
    pdf.text(48, bottom - 78, "3. Run command", bold=True)
    pdf.field("cw_run_command", 48, bottom - 110, 242)
    pdf.text(318, bottom - 78, "4. Terminal output", bold=True)
    pdf.field("cw_first_output", 318, bottom - 110, 252)
    pdf.footer()

    pdf.start_page("Decision Ladder", "Classwork continued")
    pdf.section(646, "Part 5 - Build and Test Four Outcomes", "15 points", GREEN)
    pdf.wrapped(
        48,
        614,
        "Upgrade the program: 90 or more is Legend, 70 or more is Hero, 50 or more is Explorer, and anything lower says Keep training.",
    )
    pdf.text(48, 568, "Write your completed TypeScript code:", bold=True)
    pdf.field("cw_ladder_code", 48, 346, 522, 205, multiline=True, font_size=8)

    pdf.text(48, 318, "Score 95 output", bold=True)
    pdf.field("cw_test_95", 155, 306, 145)
    pdf.text(318, 318, "Score 70 output", bold=True)
    pdf.field("cw_test_70", 420, 306, 150)
    pdf.text(48, 274, "Score 49 output", bold=True)
    pdf.field("cw_test_49", 155, 262, 145)
    pdf.text(318, 274, "One extra test", bold=True)
    pdf.field("cw_test_extra", 410, 262, 160)

    pdf.text(48, 226, "Why should the score conditions go from highest to lowest?", bold=True)
    pdf.field("cw_order_reason", 48, 124, 522, 86, multiline=True)

    pdf.note_box(
        48,
        100,
        522,
        38,
        "Remember",
        "The program checks from top to bottom and stops at the first true branch.",
    )
    pdf.footer()

    pdf.start_page("AI Logic Bug Hunt", "Classwork conclusion and bonus")
    pdf.section(646, "Part 6 - AI Logic Bug Hunt", "10 points", MAGENTA)
    bottom = pdf.code_box(
        48,
        615,
        522,
        [
            'let score: number = 95;',
            'if (score >= 50) {',
            '  console.log("Explorer rank!");',
            '} else if (score >= 90) {',
            '  console.log("Legend rank!");',
            '} else {',
            '  console.log("Keep training!");',
            '}',
        ],
        font_size=8.2,
        leading=9,
    )
    pdf.text(48, bottom - 15, "1. What prints for 95?", bold=True)
    pdf.field("cw_ai_output", 175, bottom - 27, 395)
    pdf.text(48, bottom - 53, "2. Why does the program stop at the wrong branch?", bold=True)
    pdf.field("cw_ai_reason", 48, bottom - 98, 522, 34, multiline=True)
    pdf.text(48, bottom - 122, "3. Rewrite the conditions in the correct order:", bold=True)
    pdf.field("cw_ai_fix", 48, bottom - 184, 522, 48, multiline=True, font_size=8)
    pdf.text(48, bottom - 208, "4. Why must humans test AI-written code?", bold=True)
    pdf.field("cw_ai_reflection", 48, bottom - 250, 522, 32, multiline=True)

    bonus_y = bottom - 286
    pdf.section(bonus_y, "Bonus - Add and Test a New Branch", "+10 points", ORANGE)
    pdf.text(48, bonus_y - 34, "New condition and message:", bold=True)
    pdf.field("cw_bonus_branch", 200, bonus_y - 46, 370)
    pdf.text(48, bonus_y - 77, "Two test values and expected outputs:", bold=True)
    pdf.field("cw_bonus_tests", 48, bonus_y - 109, 522, 22, multiline=True)

    pdf.c.setFillColor(LIGHT)
    pdf.c.roundRect(40, 44, WIDTH - 80, 54, 5, fill=1, stroke=0)
    pdf.text(52, 80, "Submit to: 1. Microsoft Teams  2. Ishwari Raut ma'am", bold=True, size=9.5)
    pdf.text(52, 60, "Include code and terminal output. Playground evidence earns equal credit.", size=8.7)
    pdf.save()


def create_homework(output_path):
    pdf = FillableLessonPDF(
        output_path,
        "Homework: TypeScript Decision Ladders",
        "August 1, 2026",
    )
    pdf.start_page(
        "Homework: TypeScript Decision Ladders",
        "100 points + 5 bonus points | Due August 8, 2026",
    )
    student_header(pdf, "hw")

    pdf.section(604, "Part 1 - Setup Check", "20 points", CYAN)
    versions = [
        ("Node version", "hw_node_version"),
        ("npm version", "hw_npm_version"),
        ("TypeScript version", "hw_tsc_version"),
    ]
    y = 560
    for label, name in versions:
        pdf.text(48, y + 8, label, bold=True)
        pdf.field(name, 175, y - 4, 395)
        y -= 43
    pdf.text(48, 420, "If a command failed, record the error and your next step:", bold=True)
    pdf.field("hw_setup_error", 48, 344, 522, 61, multiline=True)

    pdf.text(48, 310, "Explain the job of each tool:", bold=True)
    pdf.text(48, 278, "Visual Studio Code")
    pdf.field("hw_job_vscode", 170, 266, 400)
    pdf.text(48, 235, "TypeScript compiler")
    pdf.field("hw_job_tsc", 170, 223, 400)
    pdf.text(48, 192, "Node.js")
    pdf.field("hw_job_node", 170, 180, 400)

    pdf.note_box(
        48,
        144,
        522,
        62,
        "Blocked setup?",
        "Use the TypeScript Playground and join the 4:30-5:30 PM Pacific Hangout Session for help. You can still earn full credit.",
    )
    pdf.footer()

    pdf.start_page("Workflow and Prediction", "Homework continued")
    pdf.section(646, "Part 2 - Put the Workflow in Order", "20 points", PURPLE)
    steps = [
        ("hw_order_run", "Run node decisions.js"),
        ("hw_order_save", "Save decisions.ts"),
        ("hw_order_read", "Read the terminal output"),
        ("hw_order_compile", "Run tsc decisions.ts"),
        ("hw_order_edit", "Type or change the TypeScript code"),
    ]
    y = 604
    for name, label in steps:
        pdf.field(name, 52, y - 5, 30, 22)
        pdf.text(95, y + 2, label)
        y -= 34
    pdf.text(48, 426, "Complete the workflow:", bold=True)
    pdf.text(48, 397, "decisions.ts ->", font="Courier", size=9.5)
    pdf.field("hw_flow_tsc", 145, 385, 95)
    pdf.text(250, 397, "-> decisions.js ->", font="Courier", size=9.5)
    pdf.field("hw_flow_node", 365, 385, 95)
    pdf.text(470, 397, "-> output", font="Courier", size=9.5)

    pdf.section(340, "Part 3 - Predict the Branch", "25 points", GREEN)
    bottom = pdf.code_box(
        48,
        312,
        522,
        [
            'if (temperature >= 90) console.log("Very hot");',
            'else if (temperature >= 70) console.log("Warm");',
            'else if (temperature >= 50) console.log("Cool");',
            'else console.log("Cold");',
        ],
        font_size=8.2,
        leading=11,
    )
    tests = [("95", "hw_temp_95"), ("90", "hw_temp_90"), ("72", "hw_temp_72"),
             ("70", "hw_temp_70"), ("50", "hw_temp_50"), ("49", "hw_temp_49")]
    positions = [(48, bottom - 33), (240, bottom - 33), (432, bottom - 33),
                 (48, bottom - 76), (240, bottom - 76), (432, bottom - 76)]
    for (value, name), (x, y_pos) in zip(tests, positions):
        pdf.text(x, y_pos + 8, value, bold=True)
        pdf.field(name, x + 28, y_pos - 4, 130)
    pdf.text(48, bottom - 112, "Why are 90, 70, 50, and 49 useful boundary tests?", bold=True)
    pdf.field("hw_boundary_reason", 48, 52, 522, 58, multiline=True)
    pdf.footer()

    pdf.start_page("Build Your Own Program", "Homework continued")
    pdf.section(646, "Part 4 - Build Your Own Program", "25 points", ORANGE)
    pdf.wrapped(
        48,
        614,
        "Create homework-decisions.ts with one typed variable, one if, at least two else if branches, one final else, and a different message in every branch.",
    )
    pdf.text(48, 566, "What does your program decide?", bold=True)
    pdf.field("hw_program_purpose", 240, 554, 330)
    pdf.text(48, 520, "Write your final TypeScript code:", bold=True)
    pdf.field("hw_program_code", 48, 270, 522, 232, multiline=True, font_size=8)

    pdf.text(48, 236, "Record four tests:", bold=True)
    y = 202
    for index in range(1, 5):
        pdf.text(52, y + 7, f"Test {index}", bold=True)
        pdf.field(f"hw_test_value_{index}", 105, y - 5, 115)
        pdf.text(232, y + 7, "Output")
        pdf.field(f"hw_test_output_{index}", 275, y - 5, 295)
        y -= 40
    pdf.footer()

    pdf.start_page("AI Reflection and Submission", "Homework conclusion")
    pdf.section(646, "Part 5 - AI Reflection", "10 points", MAGENTA)
    pdf.wrapped(
        48,
        614,
        "An AI assistant gives you code that compiles and runs. Does that prove the logic is correct? Explain why or why not, and name two test values you would use before trusting it.",
    )
    pdf.field("hw_ai_reflection", 48, 430, 522, 135, multiline=True)

    pdf.section(385, "Bonus - Improve the User Experience", "+5 points", GREEN)
    pdf.wrapped(
        48,
        352,
        "Use a template literal to include the tested value in the output message.",
    )
    bottom = pdf.code_box(
        48,
        320,
        522,
        ['console.log(`A score of ${score} earns Hero rank!`);'],
        font_size=8.8,
        leading=12,
    )
    pdf.text(48, bottom - 24, "Write your improved output line:", bold=True)
    pdf.field("hw_bonus_line", 48, bottom - 68, 522, 31, font_size=8)

    pdf.c.setFillColor(LIGHT)
    pdf.c.roundRect(40, 112, WIDTH - 80, 110, 6, fill=1, stroke=0)
    pdf.text(52, 194, "Submit your homework to:", bold=True)
    pdf.text(52, 173, "1. Microsoft Teams")
    pdf.text(52, 154, "2. Ishwari Raut ma'am")
    pdf.text(52, 132, "Submit the completed homework plus your .ts code or Playground screenshot.", size=8.7)
    pdf.text(52, 117, "Never include passwords or private information.", size=8.7)
    pdf.save()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lesson_dir = os.path.dirname(script_dir)
    create_classwork(
        os.path.join(
            lesson_dir,
            "2026-08-01_Classwork_VS_Code_and_TypeScript_Setup.pdf",
        )
    )
    create_homework(
        os.path.join(
            lesson_dir,
            "2026-08-01_Homework_TypeScript_Decision_Ladders.pdf",
        )
    )
    print("Created August 1 classwork and homework PDFs")


if __name__ == "__main__":
    main()
