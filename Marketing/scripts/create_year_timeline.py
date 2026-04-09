"""
EverestITT — Full Year Timeline (One-Page PDF)
Professional, detailed, email-ready
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# ─── Colors ──────────────────────────────────────────────────────────────────

DARK_BLUE = HexColor("#1E3A5F")
MEDIUM_BLUE = HexColor("#3467A6")
LIGHT_BLUE = HexColor("#6495ED")
SKY_BLUE = HexColor("#C8DCF0")
ORANGE = HexColor("#FF9933")
LIGHT_ORANGE = HexColor("#FFF3E0")
AI_PURPLE = HexColor("#673AB7")
LIGHT_PURPLE = HexColor("#EDE7F6")
GREEN = HexColor("#2E7D32")
LIGHT_GREEN = HexColor("#E8F5E9")
GOLD = HexColor("#FFC107")
CORAL = HexColor("#FF6F61")
TEAL = HexColor("#009688")
WHITE = HexColor("#FFFFFF")
OFF_WHITE = HexColor("#F8F9FA")
LIGHT_GRAY = HexColor("#E0E0E0")
MEDIUM_GRAY = HexColor("#9E9E9E")
DARK_GRAY = HexColor("#373737")
CHARCOAL = HexColor("#212529")

PAGE_W, PAGE_H = letter  # 8.5 x 11 inches


# ─── Drawing Helpers ─────────────────────────────────────────────────────────

def draw_rounded_rect(c, x, y, w, h, fill_color, border_color=None, radius=6):
    c.saveState()
    if fill_color:
        c.setFillColor(fill_color)
    if border_color:
        c.setStrokeColor(border_color)
        c.setLineWidth(1.5)
    else:
        c.setStrokeColor(fill_color or WHITE)
        c.setLineWidth(0)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1 if border_color else 0)
    c.restoreState()


def draw_text(c, x, y, text, size=10, color=DARK_GRAY, bold=False, font="Helvetica", align="left", max_width=None):
    c.saveState()
    font_name = f"{font}-Bold" if bold else font
    c.setFont(font_name, size)
    c.setFillColor(color)
    if align == "center" and max_width:
        text_w = c.stringWidth(text, font_name, size)
        x = x + (max_width - text_w) / 2
    elif align == "right" and max_width:
        text_w = c.stringWidth(text, font_name, size)
        x = x + max_width - text_w
    c.drawString(x, y, text)
    c.restoreState()


def draw_circle(c, x, y, r, fill_color):
    c.saveState()
    c.setFillColor(fill_color)
    c.setStrokeColor(fill_color)
    c.circle(x, y, r, fill=1, stroke=0)
    c.restoreState()


def draw_line(c, x1, y1, x2, y2, color=LIGHT_GRAY, width=1):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, y1, x2, y2)
    c.restoreState()


# ─── Build the Timeline ─────────────────────────────────────────────────────

def create_timeline():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "EverestITT_Year_Timeline_2026.pdf")

    c = canvas.Canvas(output_path, pagesize=letter)
    c.setTitle("EverestITT Kids Computer Science — 2026 Year Plan")

    margin = 0.4 * inch
    content_w = PAGE_W - 2 * margin

    # ── Header Background ──
    header_h = 0.85 * inch
    draw_rounded_rect(c, 0, PAGE_H - header_h, PAGE_W, header_h, DARK_BLUE, radius=0)

    # Orange accent line
    draw_rounded_rect(c, 0, PAGE_H - header_h - 3, PAGE_W, 3, ORANGE, radius=0)

    # Title
    draw_text(c, margin + 0.1 * inch, PAGE_H - 0.35 * inch,
              "Kids Computer Science — 2026 Year Plan",
              size=18, color=WHITE, bold=True)

    # Subtitle + contact on same line
    draw_text(c, margin + 0.1 * inch, PAGE_H - 0.58 * inch,
              "Every Saturday  •  9 AM – 1 PM Pacific  •  Ages 10–18  •  Live & Interactive",
              size=8.5, color=SKY_BLUE)
    draw_text(c, margin + 0.1 * inch, PAGE_H - 0.58 * inch,
              "everestitt.com  •  626-419-6649",
              size=9, color=ORANGE, bold=True,
              align="right", max_width=content_w - 0.2 * inch)

    # ── Phase Data ──
    phases = [
        {
            "title": "PHASE 1: FOUNDATIONS",
            "months": "January – March",
            "color": MEDIUM_BLUE,
            "light_color": HexColor("#E3EDF7"),
            "border_color": MEDIUM_BLUE,
            "items": [
                {
                    "month": "JAN",
                    "month_color": MEDIUM_BLUE,
                    "topics": [
                        ("PC Hardware", "Computer components — CPU, RAM, storage, GPU, motherboard"),
                        ("Networking Basics", "IP addresses, DNS, HTTP, how data travels across the internet"),
                        ("Clients & Servers", "How websites work — requests, responses, and web browsers"),
                    ]
                },
                {
                    "month": "FEB",
                    "month_color": MEDIUM_BLUE,
                    "topics": [
                        ("Cloud & Data Centers", "What the cloud really is — servers, storage, and services"),
                        ("Internet Infrastructure", "ISPs, internet backbone, undersea cables, how it all connects"),
                        ("Linux & Command Line", "Introduction to Linux, terminal commands, file navigation"),
                    ]
                },
                {
                    "month": "MAR",
                    "month_color": MEDIUM_BLUE,
                    "topics": [
                        ("Windows & Mac CLI", "Command Prompt, PowerShell, and Terminal basics"),
                        ("Cloud Collaboration", "OneDrive, Google Drive, sharing, co-authoring documents"),
                        ("Cybersecurity", "Passwords, phishing, 2FA, staying safe online, AI in security"),
                    ]
                },
            ]
        },
        {
            "title": "PHASE 2: ARTIFICIAL INTELLIGENCE",
            "months": "April – June",
            "color": AI_PURPLE,
            "light_color": LIGHT_PURPLE,
            "border_color": AI_PURPLE,
            "highlight": True,
            "items": [
                {
                    "month": "APR",
                    "month_color": AI_PURPLE,
                    "topics": [
                        ("What AI Really Is", "Large Language Models, neural networks, training data — demystified"),
                        ("Prompt Engineering", "Writing effective prompts — the #1 skill for using AI professionally"),
                        ("AI Tools: ChatGPT", "Hands-on with ChatGPT — real projects, not just chatting"),
                    ]
                },
                {
                    "month": "MAY",
                    "month_color": AI_PURPLE,
                    "topics": [
                        ("Claude Code & OpenClaw", "Building with professional AI tools used in the industry"),
                        ("AI Agents", "How autonomous AI agents work — and how to create your own"),
                        ("AI-Powered Projects", "Students build real projects using AI tools"),
                    ]
                },
                {
                    "month": "JUN",
                    "month_color": AI_PURPLE,
                    "topics": [
                        ("Ethics & Safety", "Bias, deepfakes, misinformation — using AI responsibly"),
                        ("AI in Every Career", "How AI is transforming medicine, law, business, and more"),
                        ("AI Capstone Project", "Students present their AI-powered creations"),
                    ]
                },
            ]
        },
        {
            "title": "PHASE 3: PROGRAMMING",
            "months": "July – December",
            "color": GREEN,
            "light_color": LIGHT_GREEN,
            "border_color": GREEN,
            "items": [
                {
                    "month": "JUL",
                    "month_color": GREEN,
                    "topics": [
                        ("Programming Basics", "Variables, data types, input/output, first programs"),
                        ("Developer Tools", "Code editor setup, GitHub, version control basics"),
                    ]
                },
                {
                    "month": "AUG",
                    "month_color": GREEN,
                    "topics": [
                        ("Conditionals & Logic", "If/else, comparison operators, boolean logic"),
                        ("Loops", "For loops, while loops, iteration, pattern problems"),
                    ]
                },
                {
                    "month": "SEP",
                    "month_color": GREEN,
                    "topics": [
                        ("Functions", "Writing reusable code, parameters, return values"),
                        ("Problem Solving", "Breaking down problems, debugging, computational thinking"),
                    ]
                },
                {
                    "month": "OCT",
                    "month_color": TEAL,
                    "topics": [
                        ("Data Structures", "Lists, dictionaries, tuples — organizing data"),
                        ("File Handling", "Reading and writing files, working with data"),
                    ]
                },
                {
                    "month": "NOV",
                    "month_color": TEAL,
                    "topics": [
                        ("Algorithms", "Sorting, searching, efficiency basics"),
                        ("APIs & Libraries", "Using code libraries, calling web APIs, building tools"),
                    ]
                },
                {
                    "month": "DEC",
                    "month_color": TEAL,
                    "topics": [
                        ("Final Capstone Project", "Students design, build, and present a complete software application"),
                        ("Year in Review", "Portfolio showcase — everything they've accomplished"),
                    ]
                },
            ]
        },
    ]

    # ── Draw Phases ──
    y_cursor = PAGE_H - header_h - 0.22 * inch

    for phase in phases:
        is_highlight = phase.get("highlight", False)

        # Phase header bar
        phase_bar_h = 0.26 * inch
        draw_rounded_rect(c, margin, y_cursor - phase_bar_h,
                          content_w, phase_bar_h, phase["color"], radius=4)
        draw_text(c, margin + 0.12 * inch, y_cursor - phase_bar_h + 0.07 * inch,
                  phase["title"], size=9, color=WHITE, bold=True)
        draw_text(c, margin + 0.12 * inch, y_cursor - phase_bar_h + 0.07 * inch,
                  phase["months"], size=8, color=WHITE, bold=False,
                  align="right", max_width=content_w - 0.24 * inch)

        if is_highlight:
            # Gold "ENROLLING NOW" badge
            badge_w = 1.05 * inch
            badge_x = margin + content_w - badge_w - 1.3 * inch
            draw_rounded_rect(c, badge_x, y_cursor - phase_bar_h + 0.04 * inch,
                              badge_w, 0.18 * inch, GOLD, radius=3)
            draw_text(c, badge_x + 0.06 * inch, y_cursor - phase_bar_h + 0.08 * inch,
                      "★ ENROLLING NOW", size=6.5, color=CHARCOAL, bold=True)

        y_cursor -= phase_bar_h + 0.05 * inch

        # Month rows
        for month_data in phase["items"]:
            month = month_data["month"]
            topics = month_data["topics"]
            month_color = month_data["month_color"]

            # Calculate row height: each topic gets 2 lines (name + description)
            topic_block_h = 0.24 * inch
            row_padding = 0.1 * inch
            row_h = len(topics) * topic_block_h + row_padding

            # Light background for the row
            draw_rounded_rect(c, margin, y_cursor - row_h,
                              content_w, row_h, phase["light_color"],
                              border_color=LIGHT_GRAY, radius=3)

            # Month badge — vertically centered in the row
            badge_w = 0.5 * inch
            badge_h = 0.24 * inch
            badge_y = y_cursor - (row_h / 2) - (badge_h / 2)
            draw_rounded_rect(c, margin + 0.1 * inch, badge_y,
                              badge_w, badge_h, month_color, radius=4)
            draw_text(c, margin + 0.1 * inch, badge_y + 0.07 * inch,
                      month, size=8, color=WHITE, bold=True,
                      align="center", max_width=badge_w)

            # Topics — two lines each: bold name, then gray description
            topic_x = margin + 0.72 * inch
            topic_start_y = y_cursor - 0.1 * inch

            for j, (topic_name, topic_desc) in enumerate(topics):
                ty = topic_start_y - j * topic_block_h

                # Dot
                draw_circle(c, topic_x + 0.04 * inch, ty + 0.02 * inch, 2, month_color)

                # Topic name (bold, line 1)
                draw_text(c, topic_x + 0.16 * inch, ty,
                          topic_name, size=7.5, color=DARK_GRAY, bold=True)

                # Topic description (gray, line 2)
                draw_text(c, topic_x + 0.16 * inch, ty - 0.11 * inch,
                          topic_desc, size=6.5, color=MEDIUM_GRAY)

            y_cursor -= row_h + 0.03 * inch

        # Gap between phases
        y_cursor -= 0.05 * inch

    # ── Bottom Section ──
    # Hangout sessions bar
    hangout_h = 0.26 * inch
    draw_rounded_rect(c, margin, y_cursor - hangout_h,
                      content_w, hangout_h, ORANGE, radius=4)
    draw_text(c, margin + 0.12 * inch, y_cursor - hangout_h + 0.07 * inch,
              "DAILY HANGOUT SESSIONS", size=8, color=WHITE, bold=True)
    draw_text(c, margin + 0.12 * inch, y_cursor - hangout_h + 0.07 * inch,
              "Monday – Friday  •  4:30 – 5:30 PM Pacific  •  Homework help, Q&A, parent communication",
              size=7, color=WHITE, align="right", max_width=content_w - 0.24 * inch)

    y_cursor -= hangout_h + 0.1 * inch

    # Footer
    draw_line(c, margin, y_cursor, PAGE_W - margin, y_cursor, LIGHT_GRAY, 0.5)
    y_cursor -= 0.14 * inch

    draw_text(c, margin, y_cursor,
              "EverestITT — Empowering Future Innovators Through Technology",
              size=7, color=MEDIUM_GRAY)
    draw_text(c, margin, y_cursor,
              "everestitt.com  •  626-419-6649  •  Contact: Pratikshya maam (Program Manager)",
              size=7, color=MEDIUM_GRAY, align="right", max_width=content_w)

    c.save()
    print(f"[SUCCESS] Timeline PDF created: {output_path}")


if __name__ == "__main__":
    create_timeline()
