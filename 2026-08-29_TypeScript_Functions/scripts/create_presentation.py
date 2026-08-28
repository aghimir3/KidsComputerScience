"""Create the August 29 TypeScript Functions presentation."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
from create_theme import *  # noqa: F401,F403


CODE_BG = RGBColor(22, 31, 45)
CODE_TEXT = RGBColor(210, 238, 224)
PALE_BLUE = RGBColor(232, 244, 252)
PALE_GREEN = RGBColor(232, 247, 238)
PALE_ORANGE = RGBColor(255, 244, 225)
PALE_PURPLE = RGBColor(244, 235, 248)


def new_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def add_lines(slide, x, y, w, h, lines, font_size=18, color=None,
              bold=False, alignment=PP_ALIGN.LEFT, font_name="Segoe UI",
              line_spacing=1.05):
    """Add one textbox with one paragraph per supplied line."""
    if color is None:
        color = COLORS["dark_gray"]
    textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = textbox.text_frame
    frame.word_wrap = True
    frame.margin_left = Inches(0.04)
    frame.margin_right = Inches(0.04)
    frame.margin_top = Inches(0.03)
    frame.margin_bottom = Inches(0.03)
    for index, line in enumerate(lines):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.text = line
        paragraph.font.size = Pt(font_size)
        paragraph.font.color.rgb = color
        paragraph.font.bold = bold
        paragraph.font.name = font_name
        paragraph.alignment = alignment
        paragraph.line_spacing = line_spacing
        paragraph.space_after = Pt(2)
    return textbox


def add_slide_title(slide, title, kicker=None):
    add_title_bar(slide, title)
    if kicker:
        add_styled_textbox(
            slide,
            Inches(0.65),
            Inches(1.5),
            Inches(12.0),
            Inches(0.42),
            kicker,
            font_size=16,
            font_color=COLORS["medium_blue"],
            bold=True,
        )


def add_card(slide, x, y, w, h, color, title, lines,
             title_color=None, body_color=None, title_size=18, body_size=15):
    add_rounded_box(slide, Inches(x), Inches(y), Inches(w), Inches(h), color)
    add_styled_textbox(
        slide,
        Inches(x + 0.22),
        Inches(y + 0.16),
        Inches(w - 0.44),
        Inches(0.42),
        title,
        font_size=title_size,
        font_color=title_color or COLORS["white"],
        bold=True,
        alignment=PP_ALIGN.CENTER,
    )
    add_lines(
        slide,
        x + 0.22,
        y + 0.76,
        w - 0.44,
        h - 0.92,
        lines,
        font_size=body_size,
        color=body_color or COLORS["white"],
        alignment=PP_ALIGN.CENTER,
    )


def add_code_panel(slide, x, y, w, h, lines, font_size=17):
    panel = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x),
        Inches(y),
        Inches(w),
        Inches(h),
    )
    set_shape_fill(panel, CODE_BG)
    panel.line.fill.background()
    add_lines(
        slide,
        x + 0.24,
        y + 0.18,
        w - 0.48,
        h - 0.32,
        lines,
        font_size=font_size,
        color=CODE_TEXT,
        font_name="Consolas",
        line_spacing=1.0,
    )


def add_step(slide, number, title, body, x, y, color):
    add_circle(
        slide,
        Inches(x),
        Inches(y),
        Inches(0.62),
        color,
        text=str(number),
        text_size=18,
    )
    add_styled_textbox(
        slide,
        Inches(x + 0.82),
        Inches(y - 0.02),
        Inches(3.0),
        Inches(0.36),
        title,
        font_size=17,
        font_color=COLORS["dark_blue"],
        bold=True,
    )
    add_styled_textbox(
        slide,
        Inches(x + 0.82),
        Inches(y + 0.38),
        Inches(3.0),
        Inches(0.58),
        body,
        font_size=13,
        font_color=COLORS["dark_gray"],
    )


def build(prs):
    slide = new_slide(prs)
    add_full_bg(slide, COLORS["dark_blue"])
    add_rounded_box(
        slide,
        Inches(1.15),
        Inches(1.45),
        Inches(11.03),
        Inches(2.85),
        COLORS["light_blue"],
    )
    add_styled_textbox(
        slide,
        Inches(0.8),
        Inches(1.85),
        Inches(11.73),
        Inches(0.85),
        "TypeScript Functions",
        font_size=44,
        font_color=COLORS["dark_blue"],
        bold=True,
        alignment=PP_ALIGN.CENTER,
        font_name="Segoe UI Semibold",
    )
    add_styled_textbox(
        slide,
        Inches(1.0),
        Inches(3.0),
        Inches(11.33),
        Inches(0.55),
        "Define once. Call many times. Build bigger programs.",
        font_size=21,
        font_color=COLORS["dark_blue"],
        alignment=PP_ALIGN.CENTER,
    )
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(3.0),
        Inches(5.05),
        Inches(7.33),
        Inches(0.06),
    )
    set_shape_fill(accent, COLORS["orange"])
    accent.line.fill.background()
    add_styled_textbox(
        slide,
        Inches(1.0),
        Inches(5.42),
        Inches(11.33),
        Inches(0.45),
        "Kids Computer Science | Programming",
        font_size=17,
        font_color=COLORS["sky_blue"],
        alignment=PP_ALIGN.CENTER,
    )
    add_styled_textbox(
        slide,
        Inches(1.0),
        Inches(6.42),
        Inches(11.33),
        Inches(0.4),
        "Saturday, August 29, 2026",
        font_size=18,
        font_color=COLORS["sky_blue"],
        alignment=PP_ALIGN.CENTER,
    )

    slide = new_slide(prs)
    add_slide_title(slide, "Your Skills Are Ready", "A function organizes code you already understand")
    skills = [
        ("VALUES", ["strings", "numbers", "booleans"], COLORS["medium_blue"]),
        ("DECISIONS", ["if / else", "comparisons"], COLORS["green"]),
        ("REPETITION", ["for loops", "array loops"], COLORS["purple"]),
        ("FUNCTIONS", ["name a job", "reuse the job"], COLORS["orange"]),
    ]
    for index, (title, lines, color) in enumerate(skills):
        add_card(slide, 0.55 + index * 3.18, 2.15, 2.83, 3.25, color, title, lines)
    add_takeaway_bar(slide, "Today adds organization, not a completely new kind of thinking.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "The Repetition Problem", "Find what stays the same and what changes")
    add_code_panel(
        slide,
        0.7,
        2.0,
        7.0,
        3.7,
        [
            'console.log("Welcome, Maya!");',
            'console.log("Welcome, Leo!");',
            'console.log("Welcome, Zara!");',
            "",
            "What if there were 30 players?",
        ],
        18,
    )
    add_card(slide, 8.05, 2.0, 4.6, 1.6, COLORS["green"], "STAYS THE SAME", ["The welcome instructions"], body_size=15)
    add_card(slide, 8.05, 4.0, 4.6, 1.6, COLORS["orange"], "CHANGES", ["The player's name"], body_size=15)
    add_takeaway_bar(slide, "Repeated structure is a clue that one reusable job could help.", COLORS["teal"])

    slide = new_slide(prs)
    add_slide_title(slide, "A Function Names the Job", "Definition first, call second")
    add_code_panel(
        slide,
        0.7,
        2.0,
        7.2,
        3.7,
        [
            "function cheer() {",
            '  console.log("You can solve this!");',
            "}",
            "",
            "cheer();",
        ],
        19,
    )
    add_card(slide, 8.25, 2.0, 4.4, 1.6, COLORS["medium_blue"], "DEFINE", ["Teach the job"], body_size=16)
    add_arrow(slide, Inches(9.72), Inches(3.7), Inches(1.45), Inches(0.65), COLORS["orange"], "down")
    add_card(slide, 8.25, 4.55, 4.4, 1.15, COLORS["green"], "CALL", ["Run the job now"], body_size=14)
    add_takeaway_bar(slide, "Define once. Call whenever the job is needed.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Anatomy of a Function", "Read the declaration from left to right")
    add_code_panel(slide, 0.9, 2.05, 11.53, 1.35, ['function cheer() { console.log("Go!"); }'], 20)
    parts = [
        ("function", ["Starts the declaration"], COLORS["medium_blue"]),
        ("cheer", ["Names the job"], COLORS["purple"]),
        ("( )", ["Input area"], COLORS["teal"]),
        ("{ }", ["Holds instructions"], COLORS["orange"]),
    ]
    for index, (title, lines, color) in enumerate(parts):
        add_card(slide, 0.55 + index * 3.18, 4.0, 2.83, 1.75, color, title, lines, title_size=17, body_size=13)
    add_takeaway_bar(slide, "The function body is the code between the braces.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "A Definition Does Not Run", "Predict before the call appears")
    add_code_panel(
        slide,
        0.7,
        2.05,
        6.8,
        3.5,
        ["function celebrate() {", '  console.log("Great work!");', "}"],
        20,
    )
    add_card(slide, 7.85, 2.05, 4.8, 1.5, COLORS["red"], "CALLS", ["0"], body_size=22)
    add_card(slide, 7.85, 4.05, 4.8, 1.5, COLORS["light_gray"], "OUTPUT", ["Nothing yet"], title_color=COLORS["dark_blue"], body_color=COLORS["dark_gray"], body_size=18)
    add_takeaway_bar(slide, "The definition teaches the job; a call tells it to run.", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, "Count Calls, Count Runs", "Each call starts one complete run of the body")
    add_code_panel(slide, 0.7, 2.0, 5.0, 3.8, ["function beep() {", '  console.log("Beep!");', "}", "", "beep();", "beep();", "beep();"], 18)
    for index, color in enumerate([COLORS["medium_blue"], COLORS["teal"], COLORS["purple"]]):
        add_card(slide, 6.15, 2.0 + index * 1.28, 2.6, 1.0, color, f"CALL {index + 1}", ["beep()"], title_size=14, body_size=12)
        add_arrow(slide, Inches(8.95), Inches(2.2 + index * 1.28), Inches(1.0), Inches(0.48), COLORS["orange"])
        add_card(slide, 10.15, 2.0 + index * 1.28, 2.5, 1.0, COLORS["green"], "OUTPUT", ["Beep!"], title_size=14, body_size=12)
    add_takeaway_bar(slide, "Three calls mean three runs and three output lines.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "One Typed Parameter", "Give each call one piece of information")
    add_code_panel(slide, 0.65, 2.0, 7.2, 3.8, ["function greetPlayer(name: string) {", "  console.log(`Welcome, ${name}!`);", "}", "", 'greetPlayer("Maya");'], 18)
    add_card(slide, 8.2, 2.0, 4.45, 1.45, COLORS["purple"], "INPUT BOX", ["name: string"], body_size=18)
    add_arrow(slide, Inches(9.72), Inches(3.68), Inches(1.35), Inches(0.65), COLORS["orange"], "down")
    add_card(slide, 8.2, 4.55, 4.45, 1.25, COLORS["green"], "CURRENT VALUE", ['name = "Maya"'], body_size=16)
    add_takeaway_bar(slide, "The parameter names the input and promises its type.", COLORS["teal"])

    slide = new_slide(prs)
    add_slide_title(slide, "Parameter vs. Argument", "The box and the value have different names")
    add_card(slide, 0.8, 2.1, 4.6, 3.45, COLORS["purple"], "PARAMETER", ["In the definition", "name: string", "A named input box"], body_size=17)
    add_arrow(slide, Inches(5.75), Inches(3.3), Inches(1.8), Inches(0.8), COLORS["orange"])
    add_card(slide, 7.9, 2.1, 4.6, 3.45, COLORS["medium_blue"], "ARGUMENT", ["In the call", '"Maya"', "The value sent in"], body_size=17)
    add_takeaway_bar(slide, "The argument travels into the parameter when the call runs.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Trace Three Calls", "The parameter receives a fresh value each time")
    widths = [3.6, 3.6, 4.2]
    starts = [0.75, 4.58, 8.41]
    add_table_row(slide, 2.0, ["CALL", "name VALUE", "OUTPUT"], widths, starts, COLORS["dark_blue"], font_size=15, row_height=0.62)
    rows = [
        (['greetPlayer("Maya")', '"Maya"', "Welcome, Maya!"], COLORS["medium_blue"]),
        (['greetPlayer("Leo")', '"Leo"', "Welcome, Leo!"], COLORS["teal"]),
        (['greetPlayer("Zara")', '"Zara"', "Welcome, Zara!"], COLORS["purple"]),
    ]
    for index, (values, color) in enumerate(rows):
        add_table_row(slide, 2.85 + index * 0.92, values, widths, starts, color, font_size=14, row_height=0.72)
    add_styled_textbox(slide, Inches(1.0), Inches(5.85), Inches(11.33), Inches(0.4), "What stays the same? What changes?", font_size=20, font_color=COLORS["dark_blue"], bold=True, alignment=PP_ALIGN.CENTER)
    add_takeaway_bar(slide, "The body stays the same; the argument changes.", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, "Two Parameters", "Arguments match parameters by position")
    add_code_panel(slide, 0.65, 2.0, 7.3, 3.8, ["function reportScore(", "  player: string,", "  score: number", ") {", "  console.log(`${player}: ${score}`);", "}", 'reportScore("Zara", 95);'], 16)
    add_card(slide, 8.3, 2.0, 4.3, 1.45, COLORS["medium_blue"], "FIRST -> FIRST", ['"Zara" -> player'], body_size=16)
    add_card(slide, 8.3, 4.0, 4.3, 1.45, COLORS["green"], "SECOND -> SECOND", ["95 -> score"], body_size=16)
    add_takeaway_bar(slide, "Order is part of the function's contract.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "A Typed Function Has a Contract", "Count inputs, match types, preserve order")
    examples = [
        ("VALID", ['reportScore("Zara", 95)'], COLORS["green"]),
        ("WRONG ORDER", ['reportScore(95, "Zara")'], COLORS["red"]),
        ("MISSING INPUT", ['reportScore("Zara")'], COLORS["orange"]),
    ]
    for index, (title, lines, color) in enumerate(examples):
        add_card(slide, 0.75 + index * 4.2, 2.2, 3.75, 3.1, color, title, lines, body_size=15)
    add_takeaway_bar(slide, "TypeScript catches calls that break the contract.", COLORS["purple"])

    slide = new_slide(prs)
    add_slide_title(slide, "Reuse an Old Decision", "The if/else works exactly as it did before")
    add_code_panel(slide, 0.65, 2.0, 8.0, 3.95, ["function checkScore(score: number) {", "  if (score >= 80) {", "    console.log(`${score}: passed`);", "  } else {", "    console.log(`${score}: practice`);", "  }", "}", "checkScore(92);", "checkScore(67);"], 15)
    add_card(slide, 9.0, 2.0, 3.65, 1.65, COLORS["green"], "92", ["passed"], body_size=18)
    add_card(slide, 9.0, 4.15, 3.65, 1.65, COLORS["orange"], "67", ["practice"], body_size=18)
    add_takeaway_bar(slide, "A function can organize decisions you already know.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Functions Organize Old Skills", "One named job can contain familiar code")
    items = [
        ("VALUES", ["parameters"], COLORS["medium_blue"]),
        ("DECISIONS", ["if / else"], COLORS["green"]),
        ("LOOPS", ["repeat calls"], COLORS["purple"]),
        ("ARRAYS", ["send items"], COLORS["teal"]),
    ]
    for index, (title, lines, color) in enumerate(items):
        add_card(slide, 0.55 + index * 3.18, 2.05, 2.83, 2.0, color, title, lines, title_size=16, body_size=14)
    add_arrow(slide, Inches(5.72), Inches(4.38), Inches(1.85), Inches(0.72), COLORS["orange"], "down")
    add_card(slide, 3.75, 5.25, 5.83, 1.0, COLORS["dark_blue"], "ONE REUSABLE FUNCTION", ["A clear name for the complete job"], title_size=15, body_size=12)
    add_takeaway_bar(slide, "New structure, familiar instructions.", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, "AI Products Use Reusable Steps", "Our code handles one small review step")
    workflow = [
        ("1", "COLLECT", "Examples", COLORS["medium_blue"]),
        ("2", "PREDICT", "AI labels", COLORS["purple"]),
        ("3", "FLAG", "Review rule", COLORS["orange"]),
        ("4", "DECIDE", "Human checks", COLORS["green"]),
    ]
    for index, (number, title, body, color) in enumerate(workflow):
        x = 0.55 + index * 3.18
        add_circle(slide, Inches(x + 1.05), Inches(2.0), Inches(0.72), color, text=number, text_size=20)
        add_card(slide, x, 3.0, 2.83, 2.15, color, title, [body], title_size=16, body_size=15)
        if index < 3:
            add_arrow(slide, Inches(x + 2.78), Inches(2.23), Inches(0.72), Inches(0.38), COLORS["orange"])
    add_takeaway_bar(slide, "A reusable rule can flag uncertainty; a person decides what is correct.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Build the AI Label Review Helper", "Give one review rule a clear name")
    add_code_panel(slide, 0.65, 1.95, 8.25, 4.15, ["function reviewLabel(label: string) {", '  if (label === "unknown") {', '    console.log("Human review needed.");', "  } else {", "    console.log(`${label}: accepted for now.`);", "  }", "}"], 16)
    add_card(slide, 9.25, 1.95, 3.4, 1.65, COLORS["purple"], "INPUT", ["one label"], body_size=16)
    add_card(slide, 9.25, 4.15, 3.4, 1.95, COLORS["green"], "JOB", ["apply one rule", "print guidance"], body_size=15)
    add_takeaway_bar(slide, "The function flags a possible problem; it does not prove the label is wrong.", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, "Call It for Every Label", "The loop chooses each argument; the function does the job")
    add_code_panel(slide, 0.65, 1.9, 8.2, 4.25, ['const labels: string[] =', '  ["cat", "unknown", "tree", "unknown"];', "", "for (let i = 0; i < labels.length; i++) {", "  reviewLabel(labels[i]);", "}"], 16)
    add_card(slide, 9.2, 1.9, 3.45, 1.55, COLORS["medium_blue"], "LOOP", ["selects labels[i]"], body_size=14)
    add_arrow(slide, Inches(10.3), Inches(3.65), Inches(1.2), Inches(0.58), COLORS["orange"], "down")
    add_card(slide, 9.2, 4.45, 3.45, 1.7, COLORS["purple"], "FUNCTION", ["reviews that value"], body_size=14)
    add_takeaway_bar(slide, "Four array items create four function calls.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Return-Value Readiness Gate", "Continue only when the core model is secure")
    checks = [
        ("1", "Find the definition", COLORS["medium_blue"]),
        ("2", "Find the call", COLORS["teal"]),
        ("3", "Match argument to parameter", COLORS["purple"]),
        ("4", "Predict two calls", COLORS["green"]),
    ]
    for index, (number, text, color) in enumerate(checks):
        x = 0.7 + (index % 2) * 6.25
        y = 2.05 + (index // 2) * 1.75
        add_circle(slide, Inches(x), Inches(y), Inches(0.65), color, text=number, text_size=18)
        add_rounded_box(slide, Inches(x + 0.9), Inches(y - 0.02), Inches(4.8), Inches(0.72), PALE_BLUE, text=text, text_size=15, text_color=COLORS["dark_blue"])
    add_takeaway_bar(slide, "Confident calls and parameters are the core success for today.", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, "A Return Sends Back a Value", "Input goes in; one result comes out")
    add_code_panel(slide, 0.65, 1.95, 8.1, 4.15, ["function needsReview(", "  label: string", "): boolean {", '  if (label === "unknown") {', "    return true;", "  } else {", "    return false;", "  }", "}"], 15)
    add_card(slide, 9.1, 1.95, 3.55, 1.55, COLORS["purple"], "INPUT", ["label: string"], body_size=15)
    add_arrow(slide, Inches(10.25), Inches(3.7), Inches(1.2), Inches(0.58), COLORS["orange"], "down")
    add_card(slide, 9.1, 4.45, 3.55, 1.65, COLORS["green"], "RETURN", ["true or false"], body_size=16)
    add_takeaway_bar(slide, "The parameter type is what goes in; the return type is what comes back.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Printing Is Not Returning", "These two jobs have different destinations")
    add_card(slide, 0.8, 2.05, 5.65, 3.65, COLORS["medium_blue"], "console.log", ["Displays a message", "Useful for a person", "Does not send a result back"], body_size=16)
    add_card(slide, 6.88, 2.05, 5.65, 3.65, COLORS["green"], "return", ["Sends a value back", "Useful to other code", "Can be stored or tested"], body_size=16)
    add_takeaway_bar(slide, "Ask: should a person see it, or should the program use it?", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, "Common Function Bugs", "Find the broken contract")
    bugs = [
        ("NO CALL", ["Body never runs"], COLORS["red"]),
        ("MISSING ARGUMENT", ["Input box is empty"], COLORS["orange"]),
        ("WRONG TYPE", ["Value breaks the promise"], COLORS["purple"]),
        ("WRONG ORDER", ["Values enter wrong boxes"], COLORS["medium_blue"]),
    ]
    for index, (title, lines, color) in enumerate(bugs):
        x = 0.7 + (index % 2) * 6.25
        y = 2.0 + (index // 2) * 1.95
        add_card(slide, x, y, 5.75, 1.55, color, title, lines, title_size=16, body_size=14)
    add_takeaway_bar(slide, "Find the call, count inputs, then match type and position.", COLORS["teal"])

    slide = new_slide(prs)
    add_slide_title(slide, "Today's Classwork Missions", "Complete the core path before the return bonus")
    missions = [
        ("Definition or call?", COLORS["medium_blue"]),
        ("Define once, call many", COLORS["teal"]),
        ("Parameters and arguments", COLORS["purple"]),
        ("Decision inside a function", COLORS["green"]),
        ("AI label review helper", COLORS["orange"]),
        ("Repair function bugs", COLORS["red"]),
    ]
    for index, (text, color) in enumerate(missions):
        add_agenda_item(slide, index + 1, text, 2.0 + index * 0.65, color)
    add_takeaway_bar(slide, "Predict first. Call second. Run third. Explain last.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_full_bg(slide, COLORS["dark_blue"])
    add_styled_textbox(slide, Inches(0.75), Inches(0.65), Inches(11.83), Inches(0.7), "Functions: The Reliable Pattern", font_size=34, font_color=COLORS["white"], bold=True, alignment=PP_ALIGN.CENTER, font_name="Segoe UI Semibold")
    recap = [
        ("1", "Name one clear job"),
        ("2", "Define the function"),
        ("3", "Add typed parameters for changing inputs"),
        ("4", "Call it with matching arguments"),
        ("5", "Reuse familiar decisions, loops, and arrays"),
        ("6", "Keep people responsible for AI decisions"),
    ]
    colors = [COLORS["light_blue"], COLORS["teal"], COLORS["purple"], COLORS["green"], COLORS["orange"], COLORS["pink"]]
    for index, (number, text) in enumerate(recap):
        y = 1.62 + index * 0.78
        add_circle(slide, Inches(1.0), Inches(y), Inches(0.52), colors[index], text=number, text_size=17)
        add_styled_textbox(slide, Inches(1.85), Inches(y + 0.04), Inches(10.4), Inches(0.48), text, font_size=19, font_color=COLORS["white"])

    slide = new_slide(prs)
    add_full_bg(slide, COLORS["dark_blue"])
    add_styled_textbox(slide, Inches(0), Inches(1.2), Inches(13.33), Inches(1.1), "Questions?", font_size=54, font_color=COLORS["white"], bold=True, alignment=PP_ALIGN.CENTER, font_name="Segoe UI Semibold")
    add_styled_textbox(slide, Inches(1.0), Inches(2.8), Inches(11.33), Inches(0.7), "Then: Kahoot and the homework walkthrough", font_size=24, font_color=COLORS["sky_blue"], alignment=PP_ALIGN.CENTER)
    add_rounded_box(slide, Inches(2.55), Inches(4.25), Inches(8.23), Inches(1.1), COLORS["orange"], text="Definition?  Call?  Parameter?  Argument?", text_size=20, text_color=COLORS["dark_blue"])


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)
    build(prs)

    lesson_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(lesson_dir, "2026-08-29_TypeScript_Functions.pptx")
    prs.core_properties.title = "TypeScript Functions"
    prs.core_properties.subject = "Kids Computer Science - August 29, 2026"
    prs.core_properties.author = "Kids Computer Science"
    prs.save(output_path)
    print(f"Created {output_path}")
    print(f"Slides: {len(prs.slides)}")


if __name__ == "__main__":
    main()
