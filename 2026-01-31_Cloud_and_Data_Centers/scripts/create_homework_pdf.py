"""
Fillable PDF Homework Generator
Topic: The Cloud & Data Centers
Date: January 31, 2026

Creates interactive PDF documents with form fields, checkboxes, and text areas.

Usage:
    python create_homework_pdf.py

Dependencies:
    pip install reportlab
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth


# ============================================================================
# COLOR PALETTE
# ============================================================================
COLORS = {
    'dark_blue': HexColor('#1E3A5F'),
    'medium_blue': HexColor('#3467A6'),
    'light_blue': HexColor('#64B5ED'),
    'sky_blue': HexColor('#ADD8E6'),
    'cloud_blue': HexColor('#87CEFA'),
    'orange': HexColor('#FF9933'),
    'green': HexColor('#4CAF50'),
    'light_green': HexColor('#C8E6C9'),
    'purple': HexColor('#9C27B0'),
    'light_purple': HexColor('#E1BEE7'),
    'red': HexColor('#F44336'),
    'light_gray': HexColor('#F5F5F5'),
    'dark_gray': HexColor('#424242'),
    'white': HexColor('#FFFFFF'),
    'data_center_gray': HexColor('#607D8B'),
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
    """Draw a multi-line text area."""
    width, _ = letter

    # Label
    if label:
        c.setFillColor(COLORS['dark_gray'])
        c.setFont("Helvetica", 11)
        c.drawString(0.5*inch, y, label)
        y -= 0.2*inch

    # Text area
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

    # Content (simple word wrap)
    c.setFont("Helvetica", 10)
    c.setFillColor(COLORS['dark_gray'])

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
    """Draw a matching exercise."""
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
# HOMEWORK CONTENT - JANUARY 31, 2026
# ============================================================================

def create_homework_jan31():
    """Create the homework PDF for January 31, 2026."""

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-01-31_Homework_Cloud_Explorer.pdf")

    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # ========== PAGE 1 ==========
    draw_header(c, "HOMEWORK: Cloud Explorer", "The Cloud & Data Centers", 1, 5)

    y = height - 1.3*inch

    # Student info section
    y = draw_section_header(c, y, "Student Information", COLORS['dark_blue'])
    y -= 0.1*inch
    y = draw_text_field(c, y, "Name:", "student_name", label_width=0.6*inch, extend_to_margin=True)
    y -= 0.05*inch
    y = draw_text_field(c, y, "Date:", "date", field_width=2*inch, label_width=0.6*inch)

    y -= 0.2*inch

    # Intro box
    y = draw_fun_box(c, y, "Your Mission",
        "Now that you know about the cloud and data centers, it's time to dig deeper! "
        "Complete these challenges to become a true cloud expert.",
        COLORS['cloud_blue'], 0.85*inch)

    y -= 0.1*inch

    # Part 1: What Would Happen If...?
    y = draw_section_header(c, y, "PART 1: What Would Happen If...? (15 points)", COLORS['green'])
    y -= 0.05*inch

    y = draw_text(c, y, "For each scenario, explain what would happen and WHY:", "Helvetica-Bold", 10)
    y -= 0.1*inch

    y = draw_text(c, y, "1. Google's data centers all went offline for a day. What couldn't you use?", "Helvetica", 10, indent=0.1*inch)
    y = draw_multiline_field(c, y, "", "scenario1", 1.0*inch)

    y = draw_text(c, y, "2. You save a file to Google Drive but then lose your phone. Can you still access it?", "Helvetica", 10, indent=0.1*inch)
    y = draw_multiline_field(c, y, "", "scenario2", 1.0*inch)

    y = draw_text(c, y, "3. Your internet goes out but you have music downloaded on Spotify. Can you listen?", "Helvetica", 10, indent=0.1*inch)
    y = draw_multiline_field(c, y, "", "scenario3", 1.0*inch)

    c.showPage()

    # ========== PAGE 2 ==========
    draw_header(c, "HOMEWORK: Cloud Explorer", "The Cloud & Data Centers", 2, 5)

    y = height - 1.3*inch

    # Part 2: Matching
    y = draw_section_header(c, y, "PART 2: Match the Service to Its Cloud Type (15 points)", COLORS['purple'])
    y -= 0.05*inch

    y = draw_text(c, y, "Write the letter (A-E) for each service:", "Helvetica", 10)
    y -= 0.15*inch

    left_items = ["Google Drive", "Netflix streaming", "Zoom video calls", "iCloud Photos", "Online multiplayer games"]
    right_items = ["Cloud Storage", "Cloud Compute", "Cloud Networking", "Cloud Backup", "Cloud Gaming"]

    y = draw_matching_exercise(c, y, left_items, right_items, "matching")

    y -= 0.2*inch

    # Part 3: Data Center Facts
    y = draw_section_header(c, y, "PART 3: Data Center Research (15 points)", COLORS['data_center_gray'])
    y -= 0.05*inch

    y = draw_text(c, y, "Research one of the Big Three providers and answer:", "Helvetica-Bold", 10)
    y -= 0.1*inch

    y = draw_checkbox(c, y, "AWS (Amazon)", "provider_aws")
    y = draw_checkbox(c, y, "Microsoft Azure", "provider_azure")
    y = draw_checkbox(c, y, "Google Cloud", "provider_google")

    y -= 0.1*inch

    y = draw_text_field(c, y, "How many data centers do they have?", "dc_count", label_width=2.7*inch, extend_to_margin=True)
    y = draw_text_field(c, y, "Name one country where they have data centers:", "dc_country", label_width=3*inch, extend_to_margin=True)
    y = draw_text(c, y, "What is one interesting fact you learned about their data centers?", "Helvetica", 10)
    y = draw_multiline_field(c, y, "", "dc_fact", 0.9*inch)

    c.showPage()

    # ========== PAGE 3 ==========
    draw_header(c, "HOMEWORK: Cloud Explorer", "The Cloud & Data Centers", 3, 5)

    y = height - 1.3*inch

    # Part 4: True or False
    y = draw_section_header(c, y, "PART 4: True or False - Explain Your Answer (15 points)", COLORS['medium_blue'])
    y -= 0.1*inch

    y = draw_text(c, y, "Check T (True) or F (False), then explain WHY:", "Helvetica", 10)
    y -= 0.15*inch

    tf_questions = [
        "The cloud is actual clouds in the sky that store our data.",
        "Data centers need cooling because servers generate lots of heat.",
        "You need internet to access files stored in the cloud.",
        "AI chatbots like ChatGPT can run entirely on your smartphone without the cloud.",
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
        y = draw_multiline_field(c, y, "", f"tf{i+1}_why", 0.7*inch)
        y -= 0.05*inch

    y -= 0.1*inch

    # Part 5: Creative
    y = draw_section_header(c, y, "PART 5: Explain It! (25 points)", COLORS['green'])
    y -= 0.1*inch

    y = draw_fun_box(c, y, "Creative Challenge",
        "Imagine explaining 'the cloud' to a younger sibling or grandparent who has never heard of it. "
        "Use simple words and a real-world comparison they would understand!",
        COLORS['light_green'], 0.8*inch)

    y -= 0.1*inch
    y = draw_text(c, y, "My explanation of the cloud:", "Helvetica-Bold", 10)
    y = draw_multiline_field(c, y, "", "creative_explanation", 1.5*inch)

    c.showPage()

    # ========== PAGE 4 ==========
    draw_header(c, "HOMEWORK: Cloud Explorer", "The Cloud & Data Centers", 4, 5)

    y = height - 1.3*inch

    # Part 5.5: AI + Cloud
    y = draw_section_header(c, y, "PART 5.5: AI + Cloud Connection (10 points)", COLORS['light_purple'])
    y -= 0.05*inch

    y = draw_fun_box(c, y, "Did You Know?",
        "AI chatbots like ChatGPT, Gemini, Claude, and Grok all run on cloud servers! "
        "They need massive computing power that only data centers can provide.",
        COLORS['light_purple'], 0.75*inch)

    y -= 0.1*inch

    y = draw_text(c, y, "Match each AI chatbot to its cloud provider:", "Helvetica-Bold", 10)
    y -= 0.1*inch

    ai_left = ["ChatGPT (OpenAI)", "Gemini", "Claude (Anthropic)", "Grok (xAI)"]
    ai_right = ["Microsoft Azure", "Google Cloud", "AWS + Google", "xAI's servers"]

    y = draw_matching_exercise(c, y, ai_left, ai_right, "ai_matching")

    y -= 0.1*inch

    y = draw_text(c, y, "Why can't AI like ChatGPT run on just your phone or laptop?", "Helvetica", 10)
    y = draw_multiline_field(c, y, "", "ai_why_cloud", 0.9*inch)

    c.showPage()

    # ========== PAGE 5 ==========
    draw_header(c, "HOMEWORK: Cloud Explorer", "The Cloud & Data Centers", 5, 5)

    y = height - 1.3*inch

    # Continue Part 6 (was Part 5)
    y = draw_section_header(c, y, "PART 6: Explain It! (20 points)", COLORS['green'])
    y -= 0.05*inch

    y = draw_text(c, y, "In my explanation:", "Helvetica-Bold", 10)
    y -= 0.1*inch
    analogy_label_width = 2.2*inch
    y = draw_text_field(c, y, "The CLOUD is like:", "analogy_cloud", label_width=analogy_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "A DATA CENTER is like:", "analogy_datacenter", label_width=analogy_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "SERVERS are like:", "analogy_servers", label_width=analogy_label_width, extend_to_margin=True)
    y = draw_text_field(c, y, "YOUR DEVICE is like:", "analogy_device", label_width=analogy_label_width, extend_to_margin=True)

    y -= 0.25*inch

    # Part 7: Reflection
    y = draw_section_header(c, y, "PART 7: Reflection (10 points)", COLORS['purple'])
    y -= 0.1*inch

    y = draw_text(c, y, "What's ONE thing about cloud computing that you'll think about", "Helvetica", 10)
    y = draw_text(c, y, "differently now when you use the internet?", "Helvetica", 10)
    y = draw_multiline_field(c, y, "", "reflection", 1.0*inch)

    y -= 0.15*inch

    # Bonus section
    y = draw_section_header(c, y, "BONUS: Cloud Outage Research (+5 points)", COLORS['orange'])
    y -= 0.1*inch

    y = draw_text(c, y, "Research a real cloud outage (AWS, Google, or Azure) and answer:", "Helvetica", 10)
    y -= 0.1*inch

    y = draw_text_field(c, y, "When did it happen?", "bonus_when", label_width=1.5*inch, extend_to_margin=True)
    y = draw_text(c, y, "What services were affected? (websites, apps, etc.)", "Helvetica", 10)
    y = draw_multiline_field(c, y, "", "bonus_affected", 0.5*inch)
    y = draw_text(c, y, "What did you learn from this?", "Helvetica", 10)
    y = draw_multiline_field(c, y, "", "bonus_learned", 0.5*inch)

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
    create_homework_jan31()
