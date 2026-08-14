"""Shared fillable-PDF components for the August 15 lesson."""

import textwrap

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


WIDTH, HEIGHT = letter
NAVY = colors.HexColor("#1E3A5F")
BLUE = colors.HexColor("#3467A6")
CYAN = colors.HexColor("#009688")
PURPLE = colors.HexColor("#7A3E9D")
GREEN = colors.HexColor("#2E7D32")
ORANGE = colors.HexColor("#F28C28")
RED = colors.HexColor("#C43D3D")
LIGHT = colors.HexColor("#F5F8FC")
PALE_BLUE = colors.HexColor("#E8F4FC")
PALE_GREEN = colors.HexColor("#E8F7EE")
GRAY = colors.HexColor("#526173")
BORDER = colors.HexColor("#AABBCB")


class FillableLessonPDF:
    """Create a themed, fillable student document."""

    def __init__(self, output_path, title, short_title):
        self.canvas = canvas.Canvas(output_path, pagesize=letter)
        self.canvas.setTitle(title)
        self.page = 0
        self.short_title = short_title

    def start_page(self, title, subtitle=""):
        if self.page:
            self.footer()
            self.canvas.showPage()
        self.page += 1
        self.canvas.setFillColor(NAVY)
        self.canvas.rect(0, HEIGHT - 92, WIDTH, 92, fill=1, stroke=0)
        self.canvas.setFillColor(ORANGE)
        self.canvas.rect(0, HEIGHT - 96, WIDTH, 4, fill=1, stroke=0)
        self.canvas.setFillColor(colors.white)
        self.canvas.setFont("Helvetica-Bold", 20)
        self.canvas.drawString(40, HEIGHT - 46, title)
        if subtitle:
            self.canvas.setFont("Helvetica", 9.5)
            self.canvas.drawString(40, HEIGHT - 68, subtitle)

    def footer(self):
        self.canvas.setFillColor(GRAY)
        self.canvas.setFont("Helvetica", 8)
        self.canvas.drawString(40, 24, f"Kids Computer Science | {self.short_title}")
        self.canvas.drawRightString(WIDTH - 40, 24, f"Page {self.page}")

    def section(self, y, title, points="", color=PURPLE):
        self.canvas.setFillColor(color)
        self.canvas.roundRect(40, y - 6, WIDTH - 80, 29, 5, fill=1, stroke=0)
        self.canvas.setFillColor(colors.white)
        self.canvas.setFont("Helvetica-Bold", 12)
        self.canvas.drawString(52, y + 4, title)
        if points:
            self.canvas.drawRightString(WIDTH - 52, y + 4, points)

    def text(self, x, y, value, size=10, bold=False, color=NAVY, font=None):
        self.canvas.setFillColor(color)
        font_name = font or ("Helvetica-Bold" if bold else "Helvetica")
        self.canvas.setFont(font_name, size)
        self.canvas.drawString(x, y, value)

    def wrapped(self, x, y, value, width_chars=88, leading=13, size=9.5,
                bold=False, color=NAVY):
        lines = textwrap.wrap(value, width=width_chars) or [""]
        for line in lines:
            self.text(x, y, line, size=size, bold=bold, color=color)
            y -= leading
        return y

    def field(self, name, x, y, width, height=24, multiline=False, font_size=9):
        flags = 4096 if multiline else 0
        self.canvas.acroForm.textfield(
            name=name,
            x=x,
            y=y,
            width=width,
            height=height,
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

    def code_box(self, x, top, width, lines, font_size=8.5, leading=11):
        height = 18 + len(lines) * leading
        self.canvas.setFillColor(PALE_BLUE)
        self.canvas.setStrokeColor(BLUE)
        self.canvas.roundRect(x, top - height, width, height, 5, fill=1, stroke=1)
        line_y = top - 17
        for line in lines:
            self.text(x + 10, line_y, line, size=font_size, color=NAVY, font="Courier")
            line_y -= leading
        return top - height

    def note(self, x, top, width, height, title, body, fill=LIGHT):
        self.canvas.setFillColor(fill)
        self.canvas.setStrokeColor(BORDER)
        self.canvas.roundRect(x, top - height, width, height, 5, fill=1, stroke=1)
        self.text(x + 10, top - 18, title, size=9.5, bold=True, color=PURPLE)
        self.wrapped(x + 10, top - 35, body, width_chars=82, leading=11, size=8.5)

    def submission_bar(self, text):
        self.canvas.setFillColor(LIGHT)
        self.canvas.roundRect(40, 35, WIDTH - 80, 25, 4, fill=1, stroke=0)
        self.text(52, 44, text, bold=True, size=8.4)

    def save(self):
        self.footer()
        self.canvas.save()


def add_student_header(pdf, prefix):
    pdf.text(40, 666, "Student name", bold=True)
    pdf.field(f"{prefix}_student_name", 40, 632, 530, 25)
    pdf.text(40, 608, "Date", bold=True)
    pdf.field(f"{prefix}_date", 40, 574, 530, 25)