"""Create fillable August 1 classwork and setup-homework PDFs."""

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


class FillableLessonPDF:
    """Small themed builder shared by the two student forms."""

    def __init__(self, output_path, title, short_title):
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle(title)
        self.page = 0
        self.short_title = short_title

    def start_page(self, title, subtitle=""):
        if self.page:
            self.footer()
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
        self.c.drawString(40, 24, f"Kids Computer Science | {self.short_title}")
        self.c.drawRightString(WIDTH - 40, 24, f"Page {self.page}")

    def section(self, y, title, points="", color=PURPLE):
        self.c.setFillColor(color)
        self.c.roundRect(40, y - 6, WIDTH - 80, 29, 5, fill=1, stroke=0)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 12.2)
        self.c.drawString(52, y + 4, title)
        if points:
            self.c.drawRightString(WIDTH - 52, y + 4, points)

    def text(self, x, y, value, size=10, bold=False, color=NAVY, font=None):
        self.c.setFillColor(color)
        font_name = font or ("Helvetica-Bold" if bold else "Helvetica")
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

    def checkbox(self, name, x, y, label, size=9.3):
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

    def code_box(self, x, y, w, lines, font_size=8.5, leading=11):
        h = 18 + len(lines) * leading
        self.c.setFillColor(PALE_BLUE)
        self.c.setStrokeColor(CYAN)
        self.c.roundRect(x, y - h, w, h, 5, fill=1, stroke=1)
        current_y = y - 17
        for line in lines:
            self.text(x + 10, current_y, line, size=font_size, color=NAVY, font="Courier")
            current_y -= leading
        return y - h

    def note_box(self, x, y, w, h, title, body, fill=LIGHT):
        self.c.setFillColor(fill)
        self.c.setStrokeColor(BORDER)
        self.c.roundRect(x, y - h, w, h, 5, fill=1, stroke=1)
        self.text(x + 10, y - 18, title, size=9.5, bold=True, color=PURPLE)
        self.wrapped(x + 10, y - 35, body, width_chars=82, leading=12, size=8.7)

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
        "Classwork: TypeScript Decision Arcade",
        "August 1, 2026 classwork",
    )
    pdf.start_page(
        "Classwork: TypeScript Decision Arcade",
        "100 points + 10 bonus | Use typescriptlang.org/play during class",
    )
    student_header(pdf, "cw")

    pdf.section(604, "Part 1 — Predict Before Run", "15 points", CYAN)
    pdf.wrapped(
        48,
        574,
        "Read each line. Predict the output before you click Run in the TypeScript Playground.",
    )
    pdf.code_box(
        48,
        542,
        522,
        [
            'const player: string = "Nova";',
            "let energy: number = 40;",
            "energy = energy + 15;",
            "console.log(player);",
            "console.log(energy);",
            "console.log(energy >= 50);",
        ],
        font_size=8.8,
    )
    pdf.text(48, 440, "Line 1 output", bold=True)
    pdf.field("cw_predict_player", 142, 428, 155)
    pdf.text(318, 440, "Line 2 output", bold=True)
    pdf.field("cw_predict_energy", 412, 428, 158)
    pdf.text(48, 397, "Line 3 output", bold=True)
    pdf.field("cw_predict_boolean", 142, 385, 155)
    pdf.text(318, 397, "Did Run match?", bold=True)
    pdf.field("cw_prediction_match", 412, 385, 158)

    pdf.section(338, "Part 2 — Rebuild an if / else Gate", "15 points", GREEN)
    pdf.wrapped(
        48,
        306,
        "Fuel 50 or higher launches. A lower value must refuel. Complete the missing condition and messages.",
    )
    pdf.text(48, 264, "Condition inside if (...)", bold=True)
    pdf.field("cw_gate_condition", 192, 252, 378)
    pdf.text(48, 220, "True-branch message", bold=True)
    pdf.field("cw_gate_true", 192, 208, 378)
    pdf.text(48, 176, "Else-branch message", bold=True)
    pdf.field("cw_gate_false", 192, 164, 378)
    pdf.text(48, 128, "Test fuel = 50. What prints, and why?", bold=True)
    pdf.field("cw_gate_boundary", 48, 54, 522, 58, multiline=True)

    pdf.start_page("Rank Engine and Boundary Bosses", "Classwork continued")
    pdf.section(646, "Part 3 — Build the Rank Engine", "20 points", PURPLE)
    pdf.wrapped(
        48,
        615,
        "Use: 90+ Legendary, 70+ Hero, 50+ Explorer, and anything lower Rookie. Write one connected ladder.",
    )
    pdf.text(48, 572, "Your TypeScript code:", bold=True)
    pdf.field("cw_rank_code", 48, 340, 522, 215, multiline=True, font_size=8)

    pdf.section(300, "Part 4 — Boundary Boss Battle", "15 points", ORANGE)
    pdf.wrapped(
        48,
        270,
        "Predict first, then run each value. Record the output you actually see.",
    )
    tests = [("90", "cw_test_90"), ("89", "cw_test_89"), ("70", "cw_test_70"),
             ("69", "cw_test_69"), ("50", "cw_test_50"), ("49", "cw_test_49")]
    positions = [(48, 224), (240, 224), (432, 224), (48, 176), (240, 176), (432, 176)]
    for (value, name), (x, y) in zip(tests, positions):
        pdf.text(x, y + 10, f"Score {value}", bold=True)
        pdf.field(name, x, y - 18, 138)
    pdf.text(48, 116, "Why test a boundary and the number just below it?", bold=True)
    pdf.field("cw_boundary_reason", 48, 52, 522, 48, multiline=True)

    pdf.start_page("AI Bug Bounty", "Classwork continued")
    pdf.section(646, "Part 5 — Find and Repair the Logic Bug", "15 points", MAGENTA)
    pdf.wrapped(
        48,
        615,
        "An AI assistant suggested this code. It compiles, but its condition order causes a wrong answer.",
    )
    bottom = pdf.code_box(
        48,
        580,
        522,
        [
            "const score: number = 95;",
            "",
            "if (score >= 50) {",
            '  console.log("Explorer");',
            "} else if (score >= 70) {",
            '  console.log("Hero");',
            "} else if (score >= 90) {",
            '  console.log("Legendary");',
            "} else {",
            '  console.log("Rookie");',
            "}",
        ],
        font_size=8.1,
        leading=10,
    )
    pdf.text(48, bottom - 24, "1. What prints for 95?", bold=True)
    pdf.field("cw_ai_actual", 190, bottom - 36, 380)
    pdf.text(48, bottom - 66, "2. What should print?", bold=True)
    pdf.field("cw_ai_expected", 190, bottom - 78, 380)
    pdf.text(48, bottom - 108, "3. Why does the wrong branch win?", bold=True)
    pdf.field("cw_ai_reason", 48, bottom - 164, 522, 42, multiline=True)
    pdf.text(48, bottom - 194, "4. Rewrite only the three conditions in the correct order:", bold=True)
    pdf.field("cw_ai_fixed_order", 48, bottom - 264, 522, 55, multiline=True, font_size=8)
    pdf.text(48, bottom - 294, "5. Why must a human test AI-generated code?", bold=True)
    pdf.field("cw_ai_reflection", 48, 52, 522, 64, multiline=True)

    pdf.start_page("Design Your Decision Game", "Classwork conclusion and bonus")
    pdf.section(646, "Part 6 — Create a Tiny Game", "20 points", GREEN)
    pdf.wrapped(
        48,
        615,
        "Use one number variable, one if, at least two else if branches, one final else, and four different messages.",
    )
    pdf.text(48, 573, "Game theme or title", bold=True)
    pdf.field("cw_game_title", 175, 561, 395)
    pdf.text(48, 528, "Your TypeScript code:", bold=True)
    pdf.field("cw_game_code", 48, 300, 522, 210, multiline=True, font_size=8)
    pdf.text(48, 269, "Test value 1", bold=True)
    pdf.field("cw_game_test_1", 128, 257, 130)
    pdf.text(282, 269, "Output", bold=True)
    pdf.field("cw_game_output_1", 330, 257, 240)
    pdf.text(48, 226, "Boundary test", bold=True)
    pdf.field("cw_game_test_2", 128, 214, 130)
    pdf.text(282, 226, "Output", bold=True)
    pdf.field("cw_game_output_2", 330, 214, 240)

    pdf.section(170, "Bonus — Explain a Full Trace", "+10 points", ORANGE)
    pdf.wrapped(
        48,
        139,
        "Choose one value. Explain each false check, the first true check, and why the ladder stops.",
    )
    pdf.field("cw_bonus_trace", 48, 63, 522, 56, multiline=True)
    pdf.c.setFillColor(LIGHT)
    pdf.c.roundRect(40, 35, WIDTH - 80, 22, 4, fill=1, stroke=0)
    pdf.text(52, 42, "Submit to Microsoft Teams AND Ishwari Raut ma'am.", bold=True, size=8.8)
    pdf.save()


def create_homework(output_path):
    pdf = FillableLessonPDF(
        output_path,
        "Homework: VS Code and TypeScript Setup",
        "August 1, 2026 homework",
    )
    pdf.start_page(
        "Homework: Build Your Coding Workspace",
        "100 points + 5 bonus | Due before class on August 8, 2026",
    )
    student_header(pdf, "hw")

    pdf.section(604, "Part 1 — Choose the Safe Route", "10 points", CYAN)
    pdf.checkbox("hw_os_windows", 52, 565, "Windows — follow the attached Windows Setup Guide")
    pdf.checkbox("hw_os_macos", 52, 532, "macOS — follow the attached macOS Setup Guide")
    pdf.checkbox("hw_official_links", 52, 499, "I will use only the official links in my guide")
    pdf.checkbox("hw_password_safe", 52, 466, "I will never share my computer password")
    pdf.checkbox("hw_error_safe", 52, 433, "I will save exact errors instead of changing security settings by guessing")
    pdf.text(48, 392, "Computer or operating-system details", bold=True)
    pdf.field("hw_computer_details", 48, 350, 522, 28)

    pdf.section(308, "Part 2 — Install and Open VS Code", "20 points", PURPLE)
    pdf.checkbox("hw_vscode_official", 52, 269, "Downloaded Visual Studio Code from code.visualstudio.com")
    pdf.checkbox("hw_vscode_installed", 52, 236, "Installed it using the steps for my operating system")
    pdf.checkbox("hw_vscode_open", 52, 203, "Opened Visual Studio Code successfully")
    pdf.text(48, 161, "VS Code version or About information", bold=True)
    pdf.field("hw_vscode_version", 48, 120, 522, 28)
    pdf.text(48, 87, "What is VS Code's job?", bold=True)
    pdf.field("hw_vscode_job", 48, 50, 522, 25)

    pdf.start_page("Install Node.js LTS", "Homework continued | Use the official Node.js website")
    pdf.section(646, "Part 3 — Install Node.js LTS and npm", "20 points", GREEN)
    pdf.wrapped(
        48,
        615,
        "Open nodejs.org, choose the LTS release, finish the installer, then close and reopen the terminal before checking versions.",
    )
    pdf.checkbox("hw_node_lts", 52, 560, "I selected the LTS release, not Current")
    pdf.checkbox("hw_node_installed", 52, 527, "The Node.js installer completed")
    pdf.text(48, 480, "Run: node --version", bold=True)
    pdf.field("hw_node_version", 205, 468, 365)
    pdf.text(48, 436, "Run: npm --version", bold=True)
    pdf.field("hw_npm_version", 205, 424, 365)
    pdf.text(48, 386, "What is Node.js's job in our beginner workflow?", bold=True)
    pdf.field("hw_node_job", 48, 320, 522, 50, multiline=True)
    pdf.text(48, 284, "What is npm's job in this setup?", bold=True)
    pdf.field("hw_npm_job", 48, 218, 522, 50, multiline=True)
    pdf.text(48, 204, "If a command failed, copy the exact message:", bold=True)
    pdf.field("hw_node_error", 48, 116, 522, 72, multiline=True)
    pdf.note_box(
        48,
        100,
        522,
        50,
        "Help is available",
        "Bring the exact error to the 4:30–5:30 PM Pacific Hangout Session.",
        fill=PALE_GREEN,
    )

    pdf.start_page("Install TypeScript Once", "Homework continued | Global beginner setup")
    pdf.section(646, "Part 4 — Install TypeScript Globally", "20 points", ORANGE)
    pdf.wrapped(
        48,
        615,
        "Open a new terminal and run the command exactly. A global install makes the tsc command available for our small beginner exercises.",
    )
    bottom = pdf.code_box(
        48,
        568,
        522,
        ["npm install -g typescript", "tsc --version"],
        font_size=10,
        leading=15,
    )
    pdf.text(48, bottom - 30, "TypeScript version", bold=True)
    pdf.field("hw_tsc_version", 190, bottom - 42, 380)
    pdf.text(48, bottom - 76, "In this assignment, what does globally mean?", bold=True)
    pdf.field("hw_global_meaning", 48, bottom - 142, 522, 50, multiline=True)
    pdf.text(48, bottom - 178, "If the command failed, copy the exact message:", bold=True)
    pdf.field("hw_tsc_error", 48, bottom - 278, 522, 84, multiline=True)
    pdf.note_box(
        48,
        bottom - 298,
        522,
        96,
        "Permission safety",
        "Do not share a password or copy random permission fixes. macOS students with EACCES should record the error and ask an adult or Hangout helper. Use sudo only if the approved guide/helper directs you on your own computer.",
    )

    pdf.start_page("Compile and Run a Local File", "Homework continued | Follow the workflow in order")
    pdf.section(646, "Part 5 — Create local-ready.ts", "20 points", PURPLE)
    pdf.wrapped(
        48,
        615,
        "Create a folder you can find again, open it in VS Code, create local-ready.ts, and type the short program below.",
    )
    bottom = pdf.code_box(
        48,
        570,
        522,
        [
            "const score: number = 82;",
            "",
            "if (score >= 90) {",
            '  console.log("Legendary");',
            "} else if (score >= 70) {",
            '  console.log("Hero");',
            "} else {",
            '  console.log("Keep training");',
            "}",
        ],
        font_size=8.3,
        leading=10,
    )
    pdf.text(48, bottom - 26, "Folder name", bold=True)
    pdf.field("hw_folder_name", 140, bottom - 38, 430)
    pdf.text(48, bottom - 70, "Compile command", bold=True)
    pdf.field("hw_compile_command", 160, bottom - 82, 410)
    pdf.text(48, bottom - 114, "Generated JavaScript file", bold=True)
    pdf.field("hw_js_file", 205, bottom - 126, 365)
    pdf.text(48, bottom - 158, "Run command", bold=True)
    pdf.field("hw_run_command", 145, bottom - 170, 425)
    pdf.text(48, bottom - 202, "Terminal output", bold=True)
    pdf.field("hw_local_output", 145, bottom - 214, 425)
    pdf.text(48, bottom - 246, "Change score to 69. What prints?", bold=True)
    pdf.field("hw_local_boundary", 255, bottom - 258, 315)
    pdf.text(48, bottom - 290, "One problem you solved or one step that worked well:", bold=True)
    pdf.field("hw_local_reflection", 48, 54, 522, 64, multiline=True)

    pdf.start_page("Evidence, Reflection, and Submission", "Homework conclusion")
    pdf.section(646, "Part 6 — Evidence and Reflection", "10 points", MAGENTA)
    pdf.wrapped(
        48,
        615,
        "Attach screenshots or copy version outputs. Never include passwords, private folders, or personal information.",
    )
    pdf.text(48, 567, "Evidence attached or recorded", bold=True)
    pdf.checkbox("hw_evidence_vscode", 52, 531, "VS Code opened")
    pdf.checkbox("hw_evidence_versions", 52, 499, "Node.js, npm, and TypeScript versions")
    pdf.checkbox("hw_evidence_program", 52, 467, "local-ready.ts and its terminal output")
    pdf.text(48, 423, "Why will these local tools help in a future programming class?", bold=True)
    pdf.field("hw_tools_reflection", 48, 325, 522, 82, multiline=True)
    pdf.text(48, 287, "How can a programmer verify AI-generated TypeScript before trusting it?", bold=True)
    pdf.field("hw_ai_connection", 48, 207, 522, 64, multiline=True)

    pdf.section(166, "Bonus — Bring a Helpful Setup Note", "+5 points", GREEN)
    pdf.wrapped(
        48,
        136,
        "Write one setup tip or exact error-and-solution pair that could help another student.",
    )
    pdf.field("hw_bonus_tip", 48, 69, 522, 50, multiline=True)

    pdf.c.setFillColor(LIGHT)
    pdf.c.roundRect(40, 35, WIDTH - 80, 27, 4, fill=1, stroke=0)
    pdf.text(52, 44, "Submit to Microsoft Teams AND Ishwari Raut ma'am. Hangout: 4:30–5:30 PM Pacific.", bold=True, size=8.5)
    pdf.save()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lesson_dir = os.path.dirname(script_dir)
    create_classwork(
        os.path.join(lesson_dir, "2026-08-01_Classwork_TypeScript_Decision_Arcade.pdf")
    )
    create_homework(
        os.path.join(lesson_dir, "2026-08-01_Homework_VS_Code_and_TypeScript_Setup.pdf")
    )
    print("Created August 1 classwork and homework PDFs")


if __name__ == "__main__":
    main()
