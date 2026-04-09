"""
Fillable PDF Homework Generator
Creates interactive PDF documents with form fields, checkboxes, and text areas.

Usage:
    python create_homework_pdf.py

Dependencies:
    pip install reportlab
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, gray
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase.pdfmetrics import stringWidth


# ============================================================================
# COLOR PALETTE
# ============================================================================
COLORS = {
    'dark_blue': HexColor('#1E3A5F'),
    'medium_blue': HexColor('#3467A6'),
    'light_blue': HexColor('#64B5ED'),
    'sky_blue': HexColor('#ADD8E6'),
    'orange': HexColor('#FF9933'),
    'green': HexColor('#4CAF50'),
    'light_green': HexColor('#C8E6C9'),
    'purple': HexColor('#9C27B0'),
    'light_purple': HexColor('#E1BEE7'),
    'red': HexColor('#F44336'),
    'light_gray': HexColor('#F5F5F5'),
    'dark_gray': HexColor('#424242'),
    'white': HexColor('#FFFFFF'),
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def draw_header(c, title, subtitle=None, page_num=None, total_pages=None):
    """Draw a styled header at the top of the page."""
    width, height = letter

    # Header background
    c.setFillColor(COLORS['dark_blue'])
    c.rect(0, height - 1*inch, width, 1*inch, fill=True, stroke=False)

    # Orange accent line
    c.setFillColor(COLORS['orange'])
    c.rect(0, height - 1*inch - 4, width, 4, fill=True, stroke=False)

    # Title
    c.setFillColor(COLORS['white'])
    c.setFont("Helvetica-Bold", 20)
    c.drawString(0.5*inch, height - 0.6*inch, title)

    # Subtitle
    if subtitle:
        c.setFont("Helvetica", 11)
        c.setFillColor(COLORS['sky_blue'])
        c.drawString(0.5*inch, height - 0.85*inch, subtitle)

    # Page number
    if page_num and total_pages:
        c.setFont("Helvetica", 10)
        c.setFillColor(COLORS['white'])
        c.drawRightString(width - 0.5*inch, height - 0.6*inch, f"Page {page_num} of {total_pages}")


def draw_section_header(c, y, title, color=None):
    """Draw a section header with colored background."""
    width, _ = letter
    if color is None:
        color = COLORS['medium_blue']

    # Background
    c.setFillColor(color)
    c.roundRect(0.5*inch, y - 0.3*inch, width - 1*inch, 0.4*inch, 5, fill=True, stroke=False)

    # Text
    c.setFillColor(COLORS['white'])
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.7*inch, y - 0.18*inch, title)

    return y - 0.5*inch


def draw_text(c, y, text, font="Helvetica", size=11, color=None, indent=0):
    """Draw text at position."""
    if color is None:
        color = COLORS['dark_gray']
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawString(0.5*inch + indent, y, text)
    return y - (size + 4)


def draw_text_field(c, y, label, field_name, field_width=4*inch, height=0.25*inch, label_width=None, extend_to_margin=False):
    """Draw a text input field with label."""
    page_width, _ = letter

    # Label
    c.setFillColor(COLORS['dark_gray'])
    c.setFont("Helvetica", 11)
    c.drawString(0.5*inch, y, label)

    # Calculate field position
    if label_width is not None:
        field_x = 0.5*inch + label_width
    else:
        field_x = 0.5*inch + stringWidth(label, "Helvetica", 11) + 10

    # Calculate field width
    if extend_to_margin:
        actual_width = page_width - field_x - 0.5*inch
    else:
        actual_width = field_width

    # Text field
    c.acroForm.textfield(
        name=field_name,
        x=field_x,
        y=y - 5,
        width=actual_width,
        height=height,
        borderColor=COLORS['medium_blue'],
        fillColor=COLORS['light_gray'],
        textColor=black,
        fontSize=10,
        borderWidth=1,
    )

    return y - 0.4*inch


def draw_multiline_field(c, y, label, field_name, height=0.6*inch):
    """Draw a multi-line text area with proper multiline support."""
    width, _ = letter

    # Label (only if provided)
    if label:
        c.setFillColor(COLORS['dark_gray'])
        c.setFont("Helvetica", 11)
        c.drawString(0.5*inch, y, label)
        y -= 0.2*inch

    # Text area with multiline flag enabled
    c.acroForm.textfield(
        name=field_name,
        x=0.5*inch,
        y=y - height + 0.1*inch,
        width=width - 1*inch,
        height=height,
        borderColor=COLORS['medium_blue'],
        fillColor=COLORS['light_gray'],
        textColor=black,
        fontSize=11,
        borderWidth=1,
        fieldFlags='multiline',
    )

    return y - height - 0.1*inch


def draw_checkbox(c, y, label, field_name, checked=False):
    """Draw a checkbox with label."""
    c.acroForm.checkbox(
        name=field_name,
        x=0.5*inch,
        y=y - 2,
        size=14,
        borderColor=COLORS['medium_blue'],
        fillColor=COLORS['white'],
        buttonStyle='check',
        checked=checked,
    )

    c.setFillColor(COLORS['dark_gray'])
    c.setFont("Helvetica", 11)
    c.drawString(0.5*inch + 20, y, label)

    return y - 0.25*inch


def draw_fun_box(c, y, title, content, color=None, height=1.2*inch):
    """Draw a colored info/fun fact box."""
    width, _ = letter
    if color is None:
        color = COLORS['light_blue']

    # Background
    c.setFillColor(color)
    c.setStrokeColor(COLORS['medium_blue'])
    c.roundRect(0.5*inch, y - height, width - 1*inch, height, 10, fill=True, stroke=True)

    # Title
    c.setFillColor(COLORS['dark_blue'])
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.7*inch, y - 0.25*inch, title)

    # Content (simple text wrapping)
    c.setFont("Helvetica", 10)
    c.setFillColor(COLORS['dark_gray'])

    # Basic word wrap
    words = content.split()
    lines = []
    current_line = ""
    max_width = width - 1.4*inch

    for word in words:
        test_line = current_line + " " + word if current_line else word
        if stringWidth(test_line, "Helvetica", 10) < max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    text_y = y - 0.45*inch
    for line in lines[:4]:
        c.drawString(0.7*inch, text_y, line)
        text_y -= 0.18*inch

    return y - height - 0.15*inch


def draw_matching_exercise(c, y, left_items, right_items, group_name):
    """Draw a matching exercise with dropdowns."""
    width, _ = letter

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(COLORS['dark_gray'])
    c.drawString(0.5*inch, y, "TERM")
    c.drawString(3*inch, y, "YOUR ANSWER")
    c.drawString(5*inch, y, "CHOICES")
    y -= 0.1*inch

    # Draw line
    c.setStrokeColor(COLORS['medium_blue'])
    c.line(0.5*inch, y, width - 0.5*inch, y)
    y -= 0.25*inch

    for i, term in enumerate(left_items):
        c.setFont("Helvetica", 10)
        c.setFillColor(COLORS['dark_gray'])
        c.drawString(0.5*inch, y, f"{i+1}. {term}")

        c.acroForm.textfield(
            name=f"{group_name}_{i}",
            x=3*inch,
            y=y - 5,
            width=1.5*inch,
            height=0.22*inch,
            borderColor=COLORS['medium_blue'],
            fillColor=COLORS['light_gray'],
            textColor=black,
            fontSize=10,
            borderWidth=1,
        )

        if i < len(right_items):
            c.setFont("Helvetica", 10)
            c.drawString(5*inch, y, f"{chr(65+i)}) {right_items[i]}")

        y -= 0.3*inch

    return y


# ============================================================================
# HOMEWORK CONTENT - JANUARY 25, 2026
# ============================================================================

def create_homework_jan25():
    """Create the homework PDF for January 25, 2026."""

    output_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Clients_Servers_How_Websites_Work_2026-01-25"
    )

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, "2026-01-25_Homework_Web_Explorer.pdf")

    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # ========== PAGE 1 ==========
    draw_header(c, "HOMEWORK: Web Explorer Challenge", "Clients, Servers & How Websites Work", 1, 4)

    y = height - 1.3*inch

    # Student info section
    y = draw_section_header(c, y, "Student Information", COLORS['dark_blue'])
    y -= 0.1*inch
    y = draw_text_field(c, y, "Name:", "student_name", label_width=0.6*inch, extend_to_margin=True)
    y -= 0.05*inch
    y = draw_text_field(c, y, "Date:", "date", field_width=2*inch, label_width=0.6*inch)

    y -= 0.3*inch

    # Fun intro box
    y = draw_fun_box(c, y, "Your Mission",
        "You've learned how websites work in class. Now it's time to explore the web like a pro! "
        "Complete these challenges to prove you understand how your computer talks to servers around the world.",
        COLORS['sky_blue'], 0.9*inch)

    y -= 0.1*inch

    # Part 1: Real-World Scenarios
    y = draw_section_header(c, y, "PART 1: What Would Happen If...? (20 points)", COLORS['green'])
    y -= 0.05*inch

    y = draw_text(c, y, "For each scenario, explain what would happen and WHY:", "Helvetica-Bold", 10)
    y -= 0.1*inch

    y = draw_text(c, y, "1. You type 'youtube.com' but DNS servers are down worldwide. What happens?", "Helvetica", 10, indent=0.1*inch)
    y = draw_multiline_field(c, y, "", "scenario1", 0.75*inch)

    y = draw_text(c, y, "2. A hacker intercepts data between you and a website using HTTP (not HTTPS). What could they see?", "Helvetica", 10, indent=0.1*inch)
    y = draw_multiline_field(c, y, "", "scenario2", 0.75*inch)

    y = draw_text(c, y, "3. Netflix's servers crash. Can you still watch shows you already downloaded? Why or why not?", "Helvetica", 10, indent=0.1*inch)
    y = draw_multiline_field(c, y, "", "scenario3", 0.75*inch)

    c.showPage()

    # ========== PAGE 2 ==========
    draw_header(c, "HOMEWORK: Web Explorer Challenge", "Clients, Servers & How Websites Work", 2, 4)

    y = height - 1.3*inch

    # Part 2: Matching
    y = draw_section_header(c, y, "PART 2: Match the Service to What It Does (15 points)", COLORS['purple'])
    y -= 0.05*inch

    y = draw_text(c, y, "Write the letter (A-E) next to each service:", "Helvetica", 10)
    y -= 0.15*inch

    left_items = ["Google.com", "Your laptop at home", "Your Wi-Fi router", "Cloudflare DNS (1.1.1.1)", "A YouTube video file"]
    right_items = ["Acts as a CLIENT", "Acts as a SERVER", "Acts as a GATEWAY", "Translates names to IPs", "Stored on a SERVER"]

    y = draw_matching_exercise(c, y, left_items, right_items, "matching")

    y -= 0.2*inch

    # Part 3: Decode the URL
    y = draw_section_header(c, y, "PART 3: Decode This URL (15 points)", COLORS['orange'])
    y -= 0.05*inch

    # URL box
    c.setFillColor(COLORS['light_gray'])
    c.setStrokeColor(COLORS['dark_gray'])
    c.roundRect(0.5*inch, y - 0.4*inch, width - 1*inch, 0.4*inch, 5, fill=True, stroke=True)
    c.setFillColor(COLORS['dark_blue'])
    c.setFont("Courier-Bold", 11)
    c.drawString(0.7*inch, y - 0.28*inch, "https://classroom.google.com/u/0/c/abc123/a/homework")
    y -= 0.6*inch

    y = draw_text(c, y, "Identify each part of the URL above:", "Helvetica", 10)
    y -= 0.1*inch

    url_label_width = 1.1*inch
    y = draw_text_field(c, y, "Protocol:", "url_protocol", label_width=url_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "Subdomain:", "url_subdomain", label_width=url_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "Domain:", "url_domain", label_width=url_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "TLD:", "url_tld", label_width=url_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "Path:", "url_path", label_width=url_label_width, extend_to_margin=True)

    y -= 0.1*inch
    y = draw_text(c, y, "What port is your browser using to connect?", "Helvetica", 10)
    y = draw_text_field(c, y, "Port:", "url_port", field_width=1.5*inch, label_width=url_label_width)

    c.showPage()

    # ========== PAGE 3 ==========
    draw_header(c, "HOMEWORK: Web Explorer Challenge", "Clients, Servers & How Websites Work", 3, 4)

    y = height - 1.3*inch

    # Part 4: True or False
    y = draw_section_header(c, y, "PART 4: True or False - Explain Your Answer (15 points)", COLORS['medium_blue'])
    y -= 0.1*inch

    y = draw_text(c, y, "Check T (True) or F (False), then explain WHY:", "Helvetica", 10)
    y -= 0.15*inch

    tf_questions = [
        "A server can also be a client at the same time.",
        "HTTPS encrypts your data so only you and the server can read it.",
        "Port 80 is more secure than port 443.",
    ]

    for i, q in enumerate(tf_questions):
        y = draw_text(c, y, f"{i+1}. {q}", "Helvetica", 10, indent=0.1*inch)

        c.acroForm.checkbox(name=f"tf{i+1}_true", x=0.7*inch, y=y-2, size=12,
                           borderColor=COLORS['medium_blue'], fillColor=COLORS['white'])
        c.drawString(0.7*inch + 16, y, "T")

        c.acroForm.checkbox(name=f"tf{i+1}_false", x=1.1*inch, y=y-2, size=12,
                           borderColor=COLORS['medium_blue'], fillColor=COLORS['white'])
        c.drawString(1.1*inch + 16, y, "F")

        y -= 0.25*inch
        y = draw_text(c, y, "Why?", "Helvetica", 10)
        y = draw_multiline_field(c, y, "", f"tf{i+1}_why", 0.6*inch)
        y -= 0.1*inch

    y -= 0.15*inch

    # Part 5: Creative Challenge
    y = draw_section_header(c, y, "PART 5: Teach It! (25 points)", COLORS['green'])
    y -= 0.1*inch

    y = draw_fun_box(c, y, "Creative Challenge",
        "Imagine you need to explain to a 10-year-old how visiting a website works. "
        "Use a real-world analogy (like ordering pizza, sending mail, or going to a library). "
        "Be creative and make it fun!",
        COLORS['light_green'], 0.85*inch)

    y -= 0.1*inch
    y = draw_text(c, y, "My analogy for how websites work:", "Helvetica-Bold", 10)
    y = draw_multiline_field(c, y, "", "creative_analogy", 1.2*inch)

    c.showPage()

    # ========== PAGE 4 ==========
    draw_header(c, "HOMEWORK: Web Explorer Challenge", "Clients, Servers & How Websites Work", 4, 4)

    y = height - 1.3*inch

    # Continue Part 5
    y = draw_text(c, y, "In my analogy:", "Helvetica-Bold", 10)
    y -= 0.1*inch
    analogy_label_width = 1.8*inch
    y = draw_text_field(c, y, "The CLIENT is like:", "analogy_client", label_width=analogy_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "The SERVER is like:", "analogy_server", label_width=analogy_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "DNS is like:", "analogy_dns", label_width=analogy_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "The REQUEST is like:", "analogy_request", label_width=analogy_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "The RESPONSE is like:", "analogy_response", label_width=analogy_label_width, extend_to_margin=True)

    y -= 0.3*inch

    # Part 6: Reflection
    y = draw_section_header(c, y, "PART 6: Reflection (10 points)", COLORS['purple'])
    y -= 0.1*inch

    y = draw_text(c, y, "What's ONE thing from today's class that you'll think about differently", "Helvetica", 10)
    y = draw_text(c, y, "when you use the internet now?", "Helvetica", 10)
    y = draw_multiline_field(c, y, "", "reflection", 0.8*inch)

    y -= 0.2*inch

    # Bonus section
    y = draw_section_header(c, y, "BONUS: Did You Know? (+5 points)", COLORS['orange'])
    y -= 0.1*inch

    y = draw_text(c, y, "Research ONE of these and write 2-3 sentences about what you learned:", "Helvetica", 10)
    y -= 0.15*inch

    y = draw_checkbox(c, y, "What is a CDN (Content Delivery Network)?", "bonus_choice1")
    y = draw_checkbox(c, y, "What is the difference between IPv4 and IPv6?", "bonus_choice2")
    y = draw_checkbox(c, y, "What does a load balancer do?", "bonus_choice3")

    y -= 0.05*inch
    y = draw_multiline_field(c, y, "", "bonus_answer", 1*inch)

    # Footer with submission info
    c.setFillColor(COLORS['dark_blue'])
    c.rect(0, 0, width, 0.65*inch, fill=True, stroke=False)

    c.setFillColor(COLORS['orange'])
    c.rect(0, 0.65*inch, width, 3, fill=True, stroke=False)

    c.setFillColor(COLORS['white'])
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.5*inch, 0.4*inch, "SUBMISSION:")
    c.setFont("Helvetica", 9)
    c.drawString(1.4*inch, 0.4*inch, "1. Microsoft Teams   2. Copy to Ishwari Raut ma'am")
    c.drawString(0.5*inch, 0.2*inch, "Due: Before next class  |  Total Points: 100 (+5 bonus)")

    c.save()
    print(f"[SUCCESS] Homework PDF created: {output_path}")
    return output_path


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    create_homework_jan25()
