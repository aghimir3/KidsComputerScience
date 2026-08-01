"""Create static Windows and macOS setup-guide PDFs for the August 1 homework."""

import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


WIDTH, HEIGHT = letter
LEFT = 42
RIGHT = WIDTH - 42
CONTENT_WIDTH = RIGHT - LEFT
BOTTOM = 48

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
WHITE = colors.white


def wrap_lines(text, font_name, font_size, max_width):
    """Wrap text using actual font metrics."""
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split()
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if stringWidth(candidate, font_name, font_size) <= max_width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


class SetupGuidePDF:
    def __init__(self, output_path, document_title, platform):
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle(document_title)
        self.document_title = document_title
        self.platform = platform
        self.page = 0
        self.y = 0
        self.start_page()

    def start_page(self):
        if self.page:
            self.footer()
            self.c.showPage()
        self.page += 1
        self.c.setFillColor(NAVY)
        self.c.rect(0, HEIGHT - 86, WIDTH, 86, fill=1, stroke=0)
        self.c.setFillColor(CYAN)
        self.c.rect(0, HEIGHT - 90, WIDTH, 4, fill=1, stroke=0)
        self.c.setFillColor(WHITE)
        self.c.setFont("Helvetica-Bold", 19)
        title = self.document_title if self.page == 1 else f"{self.platform} Setup Guide - continued"
        self.c.drawString(LEFT, HEIGHT - 42, title)
        self.c.setFont("Helvetica", 9.5)
        subtitle = "VS Code + Node.js LTS + global TypeScript"
        self.c.drawString(LEFT, HEIGHT - 63, subtitle)
        self.y = HEIGHT - 122

    def footer(self):
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica", 8)
        self.c.drawString(LEFT, 24, "Kids Computer Science | August 1, 2026 homework")
        self.c.drawRightString(RIGHT, 24, f"Page {self.page}")

    def ensure(self, needed):
        if self.y - needed < BOTTOM:
            self.start_page()

    def draw_wrapped(self, text, x=LEFT, width=CONTENT_WIDTH, font="Helvetica", size=9.4,
                     leading=12.5, color=NAVY, before=0, after=8):
        lines = wrap_lines(text, font, size, width)
        needed = before + max(1, len(lines)) * leading + after
        self.ensure(needed)
        self.y -= before
        self.c.setFillColor(color)
        self.c.setFont(font, size)
        for line in lines:
            self.c.drawString(x, self.y, line)
            self.y -= leading
        self.y -= after

    def section(self, title, color=PURPLE):
        self.ensure(44)
        self.c.setFillColor(color)
        self.c.roundRect(LEFT, self.y - 26, CONTENT_WIDTH, 28, 5, fill=1, stroke=0)
        self.c.setFillColor(WHITE)
        self.c.setFont("Helvetica-Bold", 11.5)
        self.c.drawString(LEFT + 11, self.y - 17, title)
        self.y -= 42

    def paragraph(self, text, bold=False, after=8):
        self.draw_wrapped(
            text,
            font="Helvetica-Bold" if bold else "Helvetica",
            size=9.4,
            leading=12.5,
            after=after,
        )

    def bullet(self, text, color=CYAN):
        lines = wrap_lines(text, "Helvetica", 9.3, CONTENT_WIDTH - 24)
        needed = len(lines) * 12 + 4
        self.ensure(needed)
        self.c.setFillColor(color)
        self.c.circle(LEFT + 5, self.y + 2, 2.6, fill=1, stroke=0)
        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica", 9.3)
        for index, line in enumerate(lines):
            self.c.drawString(LEFT + 16, self.y - index * 12, line)
        self.y -= len(lines) * 12 + 4

    def step(self, number, text):
        lines = wrap_lines(text, "Helvetica", 9.3, CONTENT_WIDTH - 34)
        needed = max(18, len(lines) * 12) + 5
        self.ensure(needed)
        self.c.setFillColor(PURPLE)
        self.c.circle(LEFT + 10, self.y + 1, 9, fill=1, stroke=0)
        self.c.setFillColor(WHITE)
        self.c.setFont("Helvetica-Bold", 8.3)
        self.c.drawCentredString(LEFT + 10, self.y - 2, str(number))
        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica", 9.3)
        for index, line in enumerate(lines):
            self.c.drawString(LEFT + 28, self.y - index * 12, line)
        self.y -= max(18, len(lines) * 12) + 5

    def code(self, lines):
        font_size = 8.7
        leading = 11.2
        box_height = 18 + len(lines) * leading
        self.ensure(box_height + 10)
        self.c.setFillColor(PALE_BLUE)
        self.c.setStrokeColor(CYAN)
        self.c.roundRect(LEFT, self.y - box_height, CONTENT_WIDTH, box_height, 5, fill=1, stroke=1)
        self.c.setFillColor(NAVY)
        self.c.setFont("Courier", font_size)
        line_y = self.y - 16
        for line in lines:
            self.c.drawString(LEFT + 10, line_y, line)
            line_y -= leading
        self.y -= box_height + 10

    def callout(self, title, text, fill=PALE_GREEN, accent=GREEN):
        title_font = "Helvetica-Bold"
        body_font = "Helvetica"
        body_lines = wrap_lines(text, body_font, 8.8, CONTENT_WIDTH - 24)
        box_height = 35 + len(body_lines) * 11.5
        self.ensure(box_height + 9)
        self.c.setFillColor(fill)
        self.c.setStrokeColor(BORDER)
        self.c.roundRect(LEFT, self.y - box_height, CONTENT_WIDTH, box_height, 5, fill=1, stroke=1)
        self.c.setFillColor(accent)
        self.c.setFont(title_font, 9.5)
        self.c.drawString(LEFT + 11, self.y - 17, title)
        self.c.setFillColor(NAVY)
        self.c.setFont(body_font, 8.8)
        line_y = self.y - 34
        for line in body_lines:
            self.c.drawString(LEFT + 11, line_y, line)
            line_y -= 11.5
        self.y -= box_height + 9

    def checklist(self, items):
        for item in items:
            self.ensure(20)
            self.c.setFillColor(WHITE)
            self.c.setStrokeColor(NAVY)
            self.c.rect(LEFT + 2, self.y - 5, 11, 11, fill=1, stroke=1)
            self.c.setFillColor(NAVY)
            self.c.setFont("Helvetica", 9.2)
            self.c.drawString(LEFT + 22, self.y - 3, item)
            self.y -= 20
        self.y -= 4

    def save(self):
        self.footer()
        self.c.save()


def add_common_intro(pdf, links, opening_bullets):
    pdf.paragraph(
        "Goal: Install VS Code, Node.js LTS, and TypeScript once, then compile and run a local TypeScript file.",
        bold=True,
    )
    pdf.section("Official Links", CYAN)
    for label, url in links:
        pdf.bullet(f"{label}: {url}")
    pdf.section("Before You Start", ORANGE)
    for item in opening_bullets:
        pdf.bullet(item, ORANGE)
    pdf.callout(
        "Need setup help?",
        "Join the assistant-teacher Hangout Session from 4:30-5:30 PM Pacific, as scheduled in the Microsoft Teams Hangout Session channel. Bring this guide, the step number, and the exact error message.",
    )


def add_local_program(pdf):
    pdf.section("Create and Run local-ready.ts", PURPLE)
    steps = [
        "In VS Code, choose File > Open Folder.",
        "Create or choose KidsComputerScience.",
        "Create 2026-08-01-homework-setup inside it and open that folder.",
        "If Workspace Trust appears, trust the folder only because you created it.",
        "Create local-ready.ts and type the program below.",
    ]
    for number, text in enumerate(steps, start=1):
        pdf.step(number, text)
    pdf.code([
        "const score: number = 82;",
        "",
        "if (score >= 90) {",
        '  console.log("Legendary");',
        "} else if (score >= 70) {",
        '  console.log("Hero");',
        "} else {",
        '  console.log("Keep training");',
        "}",
    ])
    pdf.paragraph("Save the file, then run these commands one at a time:", bold=True, after=5)
    pdf.code(["tsc local-ready.ts", "node local-ready.js"])
    pdf.callout(
        "Expected result",
        "The compiler creates local-ready.js. Node.js runs it, and the terminal prints Hero. Change score to 69, compile again, and confirm that Keep training prints.",
    )


def create_windows(output_path):
    pdf = SetupGuidePDF(output_path, "Windows Homework Setup Guide", "Windows")
    add_common_intro(
        pdf,
        [
            ("Visual Studio Code", "https://code.visualstudio.com/docs/setup/windows"),
            ("Node.js", "https://nodejs.org/en/download/"),
            ("TypeScript", "https://www.typescriptlang.org/download/"),
        ],
        [
            "Use a Windows account that is allowed to install applications.",
            "Download only from the official links in this guide.",
            "Never share an administrator password.",
            "If a step is blocked, save the exact error and bring it to the teaching team or Hangout Session.",
        ],
    )

    pdf.section("Step 1 - Install Visual Studio Code", CYAN)
    for number, text in enumerate([
        "Open the official Windows setup link above.",
        "Choose the User Installer. Microsoft recommends User setup for most people, and it normally does not require administrator permission.",
        "Open VSCodeUserSetup-{version}.exe.",
        "Accept the agreement, keep the normal setup choices, and finish the installation.",
        "Open VS Code and confirm that the Welcome screen appears.",
    ], start=1):
        pdf.step(number, text)
    pdf.callout("Checkpoint", "VS Code opens and shows the Welcome screen.")

    pdf.section("Step 2 - Install Node.js LTS", GREEN)
    for number, text in enumerate([
        "Open the official Node.js download link above.",
        "Choose the version marked LTS. Do not choose Current.",
        "Download and run the Windows installer for your computer.",
        "Keep the normal choices and finish the installation.",
        "Close every VS Code window, then reopen VS Code.",
    ], start=1):
        pdf.step(number, text)
    pdf.paragraph("Node.js runs JavaScript. Its installer also provides npm, which installs TypeScript.")

    pdf.section("Step 3 - Use Command Prompt in VS Code", PURPLE)
    for number, text in enumerate([
        "Choose Terminal > New Terminal.",
        "If the terminal says PowerShell, open the terminal dropdown.",
        "Choose Select Default Profile, then choose Command Prompt.",
        "Open a new terminal.",
    ], start=1):
        pdf.step(number, text)
    pdf.callout(
        "Important",
        "Use Command Prompt for this assignment. Do not change the Windows execution policy.",
        fill=LIGHT,
        accent=ORANGE,
    )

    pdf.section("Step 4 - Verify Node.js and npm", GREEN)
    pdf.paragraph("Run one command at a time:", bold=True, after=5)
    pdf.code(["node --version", "npm --version"])
    pdf.paragraph("Both commands should print a version number.")
    pdf.callout(
        "If a command is not recognized",
        "Close every VS Code window, reopen it, start a new Command Prompt terminal, and try again. If it still fails, save the exact error for Hangout.",
        fill=LIGHT,
        accent=MAGENTA,
    )

    pdf.section("Step 5 - Install TypeScript Globally", ORANGE)
    pdf.paragraph("Run this command once:", bold=True, after=5)
    pdf.code(["npm install -g typescript", "tsc --version"])
    pdf.paragraph(
        "The tsc command should print a TypeScript version. This global beginner setup makes tsc available in future lesson folders without another TypeScript installation."
    )

    add_local_program(pdf)

    pdf.section("Windows Troubleshooting", MAGENTA)
    troubleshooting = [
        "PowerShell says scripts are disabled: switch the terminal to Command Prompt. Do not change the security policy.",
        "node or npm is not recognized: confirm the Node.js LTS installer finished, close VS Code, and reopen it.",
        "tsc is not recognized: confirm the global install finished, open a new terminal, and run tsc --version again.",
        "tsc local-ready.ts prints nothing: that can mean it worked. Look for local-ready.js in the Explorer.",
        "Node cannot find local-ready.js: confirm the terminal is inside the homework folder and that local-ready.js exists.",
    ]
    for item in troubleshooting:
        pdf.bullet(item, MAGENTA)

    pdf.start_page()
    pdf.section("Final Green Checks", GREEN)
    pdf.checklist([
        "VS Code opens.",
        "The VS Code terminal is Command Prompt.",
        "node --version works.",
        "npm --version works.",
        "tsc --version works.",
        "local-ready.ts compiles into local-ready.js.",
        "node local-ready.js prints a message.",
    ])
    pdf.callout(
        "Submission reminder",
        "Complete the attached homework PDF and submit it to both Microsoft Teams and Ishwari Raut ma'am. If a box remains unchecked, bring the exact error to Hangout.",
    )
    pdf.save()


def create_macos(output_path):
    pdf = SetupGuidePDF(output_path, "macOS Homework Setup Guide", "macOS")
    add_common_intro(
        pdf,
        [
            ("Visual Studio Code", "https://code.visualstudio.com/docs/setup/mac"),
            ("Node.js", "https://nodejs.org/en/download/"),
            ("TypeScript", "https://www.typescriptlang.org/download/"),
        ],
        [
            "Download only from the official links in this guide.",
            "Never say, display, screenshot, or send the computer administrator password.",
            "If a step is blocked, save the exact error and bring it to the teaching team or Hangout Session.",
        ],
    )

    pdf.section("Step 1 - Install Visual Studio Code", CYAN)
    for number, text in enumerate([
        "Open the official macOS setup link above.",
        "Download Visual Studio Code for macOS. The Universal build supports both Apple silicon and Intel-based Macs.",
        "Open the downloaded .dmg file.",
        "Drag Visual Studio Code.app into Applications.",
        "Open VS Code from Applications and confirm that the Welcome screen appears.",
    ], start=1):
        pdf.step(number, text)
    pdf.callout("Checkpoint", "VS Code opens from Applications and shows the Welcome screen.")

    pdf.section("Step 2 - Install Node.js LTS", GREEN)
    for number, text in enumerate([
        "Open the official Node.js download link above.",
        "Choose the version marked LTS. Do not choose Current.",
        "Download and open the normal macOS installer.",
        "Keep the normal choices and finish the installation.",
        "Close every VS Code window, then reopen VS Code.",
    ], start=1):
        pdf.step(number, text)
    pdf.paragraph("Node.js runs JavaScript. Its installer also provides npm, which installs TypeScript.")

    pdf.section("Step 3 - Open the VS Code Terminal", PURPLE)
    pdf.paragraph("Choose Terminal > New Terminal. The normal macOS shell should say zsh.")
    pdf.paragraph("Run one command at a time:", bold=True, after=5)
    pdf.code(["node --version", "npm --version"])
    pdf.paragraph("Both commands should print a version number.")
    pdf.callout(
        "If a command is not found",
        "Close every VS Code window, reopen it, start a new terminal, and try again. If it still fails, save the exact error for Hangout.",
        fill=LIGHT,
        accent=MAGENTA,
    )

    pdf.section("Step 4 - Install TypeScript Globally", ORANGE)
    pdf.paragraph("Try these commands first:", bold=True, after=5)
    pdf.code(["npm install -g typescript", "tsc --version"])
    pdf.paragraph(
        "The tsc command should print a TypeScript version. This global beginner setup makes tsc available in future lesson folders without another TypeScript installation."
    )
    pdf.callout(
        "If macOS reports EACCES or a permission error",
        "Stop and save the exact error. Do not repeatedly change permissions. Use sudo npm install -g typescript only when the teaching team directs you. Never say, display, screenshot, or send the computer administrator password. If unsure, bring the error to Hangout.",
        fill=LIGHT,
        accent=ORANGE,
    )

    add_local_program(pdf)

    pdf.section("macOS Troubleshooting", MAGENTA)
    troubleshooting = [
        "node or npm is not found: confirm the Node.js LTS installer finished, close VS Code, and reopen it.",
        "The global install reports a permission error: stop, record the exact error, and use the teaching-team help path above.",
        "tsc is not found: confirm the global install finished, open a new terminal, and run tsc --version again.",
        "tsc local-ready.ts prints nothing: that can mean it worked. Look for local-ready.js in the Explorer.",
        "Node cannot find local-ready.js: confirm the terminal is inside the homework folder and that local-ready.js exists.",
    ]
    for item in troubleshooting:
        pdf.bullet(item, MAGENTA)

    pdf.start_page()
    pdf.section("Final Green Checks", GREEN)
    pdf.checklist([
        "VS Code opens from Applications.",
        "The VS Code terminal uses zsh.",
        "node --version works.",
        "npm --version works.",
        "tsc --version works.",
        "local-ready.ts compiles into local-ready.js.",
        "node local-ready.js prints a message.",
    ])
    pdf.callout(
        "Submission reminder",
        "Complete the attached homework PDF and submit it to both Microsoft Teams and Ishwari Raut ma'am. If a box remains unchecked, bring the exact error to Hangout.",
    )
    pdf.save()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lesson_dir = os.path.dirname(script_dir)
    create_windows(os.path.join(lesson_dir, "2026-08-01_Windows_Setup_Guide.pdf"))
    create_macos(os.path.join(lesson_dir, "2026-08-01_macOS_Setup_Guide.pdf"))
    print("Created Windows and macOS setup guide PDFs")


if __name__ == "__main__":
    main()
