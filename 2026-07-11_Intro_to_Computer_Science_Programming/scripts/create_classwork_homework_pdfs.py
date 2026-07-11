"""Create fillable July 11 classwork and homework PDFs."""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


WIDTH, HEIGHT = letter
NAVY = colors.HexColor("#2D323C")
YELLOW = colors.HexColor("#FFDB5D")
PINK = colors.HexColor("#E81981")
GREEN = colors.HexColor("#94EE6B")
LIGHT = colors.HexColor("#F4F6F8")
GRAY = colors.HexColor("#5A616C")


class FillableLessonPDF:
    def __init__(self, output_path, title):
        self.c = canvas.Canvas(output_path, pagesize=letter)
        self.c.setTitle(title)
        self.page = 0

    def start_page(self, title, subtitle=""):
        if self.page:
            self.c.showPage()
        self.page += 1
        self.c.setFillColor(NAVY)
        self.c.rect(0, HEIGHT - 92, WIDTH, 92, fill=1, stroke=0)
        self.c.setFillColor(YELLOW)
        self.c.rect(0, HEIGHT - 96, WIDTH, 4, fill=1, stroke=0)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 21)
        self.c.drawString(40, HEIGHT - 47, title)
        if subtitle:
            self.c.setFont("Helvetica", 10)
            self.c.drawString(40, HEIGHT - 68, subtitle)

    def footer(self):
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica", 8)
        self.c.drawString(40, 24, "Kids Computer Science - July 11, 2026")
        self.c.drawRightString(WIDTH - 40, 24, f"Page {self.page}")

    def section(self, y, title, points, color=PINK):
        self.c.setFillColor(color)
        self.c.roundRect(40, y - 6, WIDTH - 80, 30, 5, fill=1, stroke=0)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 13)
        self.c.drawString(52, y + 4, title)
        self.c.drawRightString(WIDTH - 52, y + 4, points)

    def text(self, x, y, value, size=10, bold=False, color=NAVY):
        self.c.setFillColor(color)
        self.c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        self.c.drawString(x, y, value)

    def wrapped(self, x, y, value, width_chars=82, leading=14, size=10):
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
            self.text(x, y, line, size=size)
            y -= leading
        return y

    def field(self, name, x, y, w, h=22, multiline=False):
        flags = 4096 if multiline else 0
        self.c.acroForm.textfield(
            name=name,
            x=x,
            y=y,
            width=w,
            height=h,
            borderStyle="inset",
            borderColor=colors.HexColor("#AAB1BA"),
            fillColor=colors.white,
            textColor=NAVY,
            forceBorder=True,
            fontName="Helvetica",
            fontSize=10,
            fieldFlags=flags,
            maxlen=0,
        )

    def checkbox(self, name, x, y, label):
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
        self.text(x + 20, y + 2, label, size=10)

    def save(self):
        self.footer()
        self.c.save()


def student_header(pdf, prefix):
    pdf.text(40, 662, "Student name", bold=True)
    pdf.field(f"{prefix}_student_name", 125, 650, 255)
    pdf.text(400, 662, "Date", bold=True)
    pdf.field(f"{prefix}_date", 435, 650, 135)


def create_classwork(output_path):
    pdf = FillableLessonPDF(output_path, "Classwork: Programming Launch")
    pdf.start_page(
        "Classwork: Programming Launch",
        "100 points + 10 bonus points | Welcome, Teams, Code Crew, and Code.org",
    )
    student_header(pdf, "cw")

    pdf.section(604, "Part 1 - Meet the Class", "20 points")
    y = pdf.wrapped(
        48,
        574,
        "Participate in the class icebreaker. Share only what feels comfortable. A location means city/state or country, never a street address.",
    )
    pdf.checkbox("cw_intro_done", 52, y - 8, "I participated or respectfully chose to pass.")

    pdf.section(494, "Part 2 - Find Your Way in Teams", "20 points", GREEN)
    pdf.text(48, 463, "Write what you use each space for.", size=10)
    channels = ["Calendar", "Announcements", "Classwork", "Homework", "Hangout Session"]
    y = 430
    for index, channel in enumerate(channels):
        pdf.text(52, y + 7, channel, bold=True)
        pdf.field(f"cw_team_{index}", 165, y - 2, 405, 24)
        y -= 45

    pdf.text(48, 188, "When is the Hangout Session?", bold=True)
    pdf.field("cw_hangout_time", 225, 176, 345)
    pdf.text(48, 145, "Privacy check: What should you never share in class chat?", bold=True)
    pdf.field("cw_privacy", 48, 98, 522, 36, multiline=True)
    pdf.footer()

    pdf.start_page("Programming Launch", "Classwork continued")
    pdf.section(646, "Part 3 - Code Crew Breakout", "20 points")
    pdf.text(48, 613, "Which role did you try? Check all that apply.")
    pdf.checkbox("cw_role_captain", 52, 582, "Captain")
    pdf.checkbox("cw_role_coach", 180, 582, "Coach")
    pdf.checkbox("cw_role_reporter", 300, 582, "Reporter")
    pdf.text(48, 540, "How did you help your crew?", bold=True)
    pdf.field("cw_crew_help", 48, 480, 522, 48, multiline=True)

    pdf.section(431, "Part 4 - Create in Code.org", "30 points", YELLOW)
    pdf.checkbox("cw_music_open", 52, 392, "Opened Music Lab")
    pdf.checkbox("cw_music_intro", 52, 360, "Completed introductory challenges")
    pdf.checkbox("cw_music_sounds", 52, 328, "Used at least two sounds")
    pdf.checkbox("cw_music_ai", 52, 296, "Tried AI-generated drums when available")
    pdf.text(48, 250, "What changed when you moved or changed a block?", bold=True)
    pdf.field("cw_block_change", 48, 174, 522, 62, multiline=True)
    pdf.text(48, 140, "What did the AI feature add to your project?", bold=True)
    pdf.field("cw_ai_change", 48, 70, 522, 56, multiline=True)
    pdf.footer()

    pdf.start_page("Programming Launch", "Reflection and bonus")
    pdf.section(646, "Part 5 - Reflection", "10 points")
    pdf.text(48, 610, "What did you learn about programming or teamwork today?", bold=True)
    pdf.field("cw_reflection", 48, 440, 522, 150, multiline=True)

    pdf.section(385, "Bonus - Imagine the Next Feature", "+10 points", GREEN)
    pdf.wrapped(
        48,
        352,
        "Describe one feature you would add to Music Lab. Explain how AI could help with it.",
    )
    pdf.field("cw_bonus", 48, 174, 522, 150, multiline=True)

    pdf.c.setFillColor(LIGHT)
    pdf.c.roundRect(40, 72, WIDTH - 80, 74, 6, fill=1, stroke=0)
    pdf.text(52, 124, "Submit your classwork to:", bold=True)
    pdf.text(52, 104, "1. Microsoft Teams")
    pdf.text(52, 87, "2. Ishwari Raut ma'am")
    pdf.save()


def create_homework(output_path):
    pdf = FillableLessonPDF(output_path, "Homework: Music Lab Remix Challenge")
    pdf.start_page(
        "Homework: Music Lab Remix Challenge",
        "100 points + 5 bonus points | Complete the project in Code.org",
    )
    student_header(pdf, "hw")

    pdf.section(604, "Open the Assignment", "Code.org")
    pdf.text(48, 568, "Class section code", bold=True)
    pdf.field("hw_section_code", 165, 556, 160)
    pdf.text(342, 568, "Due date", bold=True)
    pdf.field("hw_due_date", 408, 556, 162)
    pdf.text(48, 522, "Activity: https://code.org/en-US/hour-of-code/music", size=9)

    pdf.section(475, "Your Remix Mission", "100 points", GREEN)
    missions = [
        ("hw_finish", "Finish the guided Music Lab levels - 30 points"),
        ("hw_three_sounds", "Use at least three sounds - 20 points"),
        ("hw_ai_drums", "Add an AI-generated drum beat - 20 points"),
        ("hw_changes", "Make at least two creative changes - 20 points"),
        ("hw_title_test", "Give it a school-appropriate title and test it - 10 points"),
    ]
    y = 433
    for name, label in missions:
        pdf.checkbox(name, 52, y, label)
        y -= 43

    pdf.section(190, "Bonus Challenge", "+5 points", YELLOW)
    pdf.wrapped(
        48,
        157,
        "Add one extra feature beyond the required steps, such as another sound, a new section, a function, or a surprising change.",
    )
    pdf.field("hw_bonus_feature", 48, 70, 522, 56, multiline=True)
    pdf.footer()

    pdf.start_page("Music Lab Remix Challenge", "Submission and reflection")
    pdf.section(646, "Project Evidence", "Required")
    pdf.text(48, 610, "Project title", bold=True)
    pdf.field("hw_project_title", 135, 598, 435)
    pdf.text(48, 565, "Project link, if sharing is available", bold=True)
    pdf.field("hw_project_link", 48, 525, 522, 28)
    pdf.checkbox("hw_screenshot", 52, 486, "I submitted a screenshot if a project link was unavailable.")

    pdf.section(437, "Reflection", "Required", PINK)
    pdf.text(48, 402, "What is your favorite part of your remix, and why?", bold=True)
    pdf.field("hw_reflection", 48, 245, 522, 140, multiline=True)

    pdf.c.setFillColor(LIGHT)
    pdf.c.roundRect(40, 100, WIDTH - 80, 112, 6, fill=1, stroke=0)
    pdf.text(52, 188, "Submit your homework to:", bold=True)
    pdf.text(52, 168, "1. Microsoft Teams")
    pdf.text(52, 151, "2. Ishwari Raut ma'am")
    pdf.text(52, 126, "Need help? Join the Hangout Session channel from 4:30-5:30 PM Pacific.", size=9)
    pdf.text(52, 111, "Never include private information in a project title or submission.", size=9)
    pdf.save()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lesson_dir = os.path.dirname(script_dir)
    create_classwork(os.path.join(lesson_dir, "2026-07-11_Classwork_Programming_Launch.pdf"))
    create_homework(os.path.join(lesson_dir, "2026-07-11_Homework_Music_Lab_Remix_Challenge.pdf"))
    print("Created July 11 classwork and homework PDFs")


if __name__ == "__main__":
    main()
