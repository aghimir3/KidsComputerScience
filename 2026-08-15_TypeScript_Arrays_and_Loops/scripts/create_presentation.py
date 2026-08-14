"""Create the August 15 TypeScript Arrays and Loops presentation."""

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
    """Add one non-overlapping textbox containing one paragraph per line."""
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
    """Use the shared title bar without its overlapping subtitle placement."""
    add_title_bar(slide, title)
    if kicker:
        add_styled_textbox(
            slide, Inches(0.65), Inches(1.5), Inches(12.0), Inches(0.42),
            kicker, font_size=16, font_color=COLORS["medium_blue"], bold=True,
        )


def add_card(slide, x, y, w, h, color, title, lines,
             title_color=None, body_color=None, title_size=18, body_size=15):
    add_rounded_box(slide, Inches(x), Inches(y), Inches(w), Inches(h), color)
    add_styled_textbox(
        slide, Inches(x + 0.22), Inches(y + 0.18), Inches(w - 0.44), Inches(0.42),
        title, font_size=title_size, font_color=title_color or COLORS["white"],
        bold=True, alignment=PP_ALIGN.CENTER,
    )
    add_lines(
        slide, x + 0.22, y + 0.78, w - 0.44, h - 0.96, lines,
        font_size=body_size, color=body_color or COLORS["white"],
        alignment=PP_ALIGN.CENTER,
    )


def add_code_panel(slide, x, y, w, h, lines, font_size=17):
    panel = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
    )
    set_shape_fill(panel, CODE_BG)
    panel.line.fill.background()
    return add_lines(
        slide, x + 0.24, y + 0.2, w - 0.48, h - 0.35, lines,
        font_size=font_size, color=CODE_TEXT, font_name="Consolas",
        line_spacing=1.0,
    )


def add_array_cells(slide, values, start_x, value_y, cell_w=2.35,
                    value_color=None):
    if value_color is None:
        value_color = COLORS["medium_blue"]
    for index, value in enumerate(values):
        x = start_x + index * (cell_w + 0.14)
        add_rounded_box(
            slide, Inches(x), Inches(value_y), Inches(cell_w), Inches(1.0),
            value_color, text=value, text_size=18,
        )
        add_rounded_box(
            slide, Inches(x + 0.55), Inches(value_y + 1.18), Inches(cell_w - 1.1),
            Inches(0.62), COLORS["orange"], text=str(index), text_size=18,
        )


def build(prs):
    slide = new_slide(prs)
    add_full_bg(slide, COLORS["dark_blue"])
    add_rounded_box(
        slide, Inches(1.15), Inches(1.55), Inches(11.03), Inches(2.7),
        COLORS["light_blue"],
    )
    add_styled_textbox(
        slide, Inches(0.8), Inches(1.95), Inches(11.73), Inches(0.8),
        "TypeScript Arrays and Loops", font_size=42,
        font_color=COLORS["dark_blue"], bold=True, alignment=PP_ALIGN.CENTER,
        font_name="Segoe UI Semibold",
    )
    add_styled_textbox(
        slide, Inches(1.0), Inches(3.08), Inches(11.33), Inches(0.55),
        "Store a list. Visit every item. Find what needs attention.",
        font_size=21, font_color=COLORS["dark_blue"], alignment=PP_ALIGN.CENTER,
    )
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(3.0), Inches(5.1), Inches(7.33), Inches(0.06)
    )
    set_shape_fill(accent, COLORS["orange"])
    accent.line.fill.background()
    add_styled_textbox(
        slide, Inches(1.0), Inches(5.45), Inches(11.33), Inches(0.45),
        "Kids Computer Science | Programming", font_size=17,
        font_color=COLORS["sky_blue"], alignment=PP_ALIGN.CENTER,
    )
    add_styled_textbox(
        slide, Inches(1.0), Inches(6.45), Inches(11.33), Inches(0.4),
        "Saturday, August 15, 2026", font_size=18,
        font_color=COLORS["sky_blue"], alignment=PP_ALIGN.CENTER,
    )

    slide = new_slide(prs)
    add_slide_title(slide, "From One Value to a Whole List", "Connect today's idea to skills you already know")
    add_card(slide, 0.65, 2.1, 3.75, 3.35, COLORS["medium_blue"], "VARIABLE",
             ["Stores one value", "const player = \"Maya\""], body_size=16)
    add_card(slide, 4.79, 2.1, 3.75, 3.35, COLORS["green"], "LOOP",
             ["Repeats one block", "i changes each round"], body_size=16)
    add_card(slide, 8.93, 2.1, 3.75, 3.35, COLORS["purple"], "ARRAY",
             ["Stores an ordered list", "One new idea today"], body_size=16)
    add_takeaway_bar(slide, "An array gives a familiar loop a list of values to visit.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Why Use an Array?", "One list replaces repeated variables")
    add_card(slide, 0.65, 2.05, 5.85, 3.65, COLORS["light_gray"], "REPEATED VARIABLES",
             ["const player1 = \"Maya\";", "const player2 = \"Leo\";",
              "const player3 = \"Zara\";", "Three names, three variables"],
             title_color=COLORS["dark_blue"], body_color=COLORS["dark_gray"], body_size=15)
    add_card(slide, 6.83, 2.05, 5.85, 3.65, COLORS["teal"], "ONE TYPED ARRAY",
             ["const players: string[] =", "  [\"Maya\", \"Leo\", \"Zara\"];",
              "Three names, one variable"], body_size=15)
    add_takeaway_bar(slide, "Use an array when related values belong together in order.", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, "Anatomy of a Typed Array", "Read each part from left to right")
    add_code_panel(slide, 1.0, 2.15, 11.33, 1.35,
                   ['const players: string[] = ["Maya", "Leo", "Zara"];'], 20)
    facts = [
        ("players", "Variable name", COLORS["medium_blue"]),
        ("string[]", "Only strings", COLORS["purple"]),
        ("[ ... ]", "Creates the list", COLORS["teal"]),
        ("commas", "Separate items", COLORS["orange"]),
    ]
    for index, (title, body, color) in enumerate(facts):
        add_card(slide, 0.65 + index * 3.08, 4.05, 2.78, 1.75, color,
                 title, [body], title_size=17, body_size=14)
    add_takeaway_bar(slide, "The item type appears before the square brackets.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Indexes Are Numbered Addresses", "Array counting begins at zero")
    add_array_cells(slide, ["Maya", "Leo", "Zara"], 2.75, 2.25, 2.35)
    add_styled_textbox(
        slide, Inches(1.0), Inches(4.45), Inches(11.33), Inches(0.45),
        "players[0]       players[1]       players[2]",
        font_size=21, font_color=COLORS["dark_blue"], bold=True,
        alignment=PP_ALIGN.CENTER, font_name="Consolas",
    )
    add_takeaway_bar(slide, "Three items use indexes 0, 1, and 2.", COLORS["teal"])

    slide = new_slide(prs)
    add_slide_title(slide, "Human Position vs. Array Index", "Use precise language when predicting")
    positions = [
        ("FIRST ITEM", "Index 0", "Maya", COLORS["medium_blue"]),
        ("SECOND ITEM", "Index 1", "Leo", COLORS["green"]),
        ("THIRD ITEM", "Index 2", "Zara", COLORS["purple"]),
    ]
    for index, (title, index_text, value, color) in enumerate(positions):
        add_card(slide, 0.75 + index * 4.17, 2.15, 3.75, 3.35, color, title,
                 [index_text, value], title_size=17, body_size=19)
    add_takeaway_bar(slide, "Position starts with first; index starts with zero.", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, ".length Counts the Items", "Length and last index are not the same number")
    add_code_panel(slide, 0.75, 2.05, 6.1, 2.5,
                   ['const players: string[] =', '  ["Maya", "Leo", "Zara"];',
                    '', 'console.log(players.length);'], 18)
    add_card(slide, 7.2, 2.05, 2.45, 2.5, COLORS["green"], "LENGTH", ["3 items"], body_size=19)
    add_card(slide, 9.95, 2.05, 2.7, 2.5, COLORS["orange"], "LAST INDEX", ["3 - 1 = 2"], body_size=19)
    add_styled_textbox(
        slide, Inches(1.0), Inches(5.05), Inches(11.33), Inches(0.55),
        "Final item: players[players.length - 1]",
        font_size=22, font_color=COLORS["dark_blue"], bold=True,
        alignment=PP_ALIGN.CENTER, font_name="Consolas",
    )
    add_takeaway_bar(slide, "Last valid index = length - 1", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Change One Item by Index", "The array stays; one value is replaced")
    add_card(slide, 0.8, 2.1, 4.8, 3.15, COLORS["medium_blue"], "BEFORE",
             ["scores", "[70, 82, 91]"], body_size=20)
    add_arrow(slide, Inches(5.92), Inches(3.15), Inches(1.45), Inches(0.75), COLORS["orange"])
    add_card(slide, 7.7, 2.1, 4.8, 3.15, COLORS["green"], "AFTER scores[1] = 88",
             ["scores", "[70, 88, 91]"], body_size=20)
    add_takeaway_bar(slide, "Index 1 means the second item.", COLORS["teal"])

    slide = new_slide(prs)
    add_slide_title(slide, "One Loop Visits Every Item", "The counter also becomes the current index")
    add_code_panel(slide, 0.65, 2.05, 7.0, 3.6,
                   ['const players: string[] =', '  ["Maya", "Leo", "Zara"];', '',
                    'for (let i = 0;', '     i < players.length; i++) {',
                    '  console.log(players[i]);', '}'], 17)
    add_card(slide, 8.0, 2.05, 4.65, 3.6, COLORS["purple"], "TWO JOBS FOR i",
             ["Counts each round", "Selects the current item", "Stops at the length"], body_size=16)
    add_takeaway_bar(slide, "Start at 0 and continue while i is less than the length.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Trace the Array Loop", "Watch the check before every round")
    columns = [0.55, 2.15, 4.25, 7.55, 10.1]
    widths = [1.35, 1.85, 3.05, 2.3, 2.65]
    add_table_row(slide, 2.0, ["Round", "i", "i < 3?", "Item", "Output"], widths, columns,
                  COLORS["dark_blue"], font_size=14, row_height=0.62)
    rows = [
        (["1", "0", "true", "players[0]", "Maya"], COLORS["medium_blue"]),
        (["2", "1", "true", "players[1]", "Leo"], COLORS["teal"]),
        (["3", "2", "true", "players[2]", "Zara"], COLORS["purple"]),
        (["Stop", "3", "false", "none", "nothing"], COLORS["orange"]),
    ]
    for index, (values, color) in enumerate(rows):
        add_table_row(slide, 2.78 + index * 0.76, values, widths, columns, color,
                      font_size=14, row_height=0.62)
    add_takeaway_bar(slide, "When i becomes 3, the check is false before another item is read.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "The Off-by-One Boundary Bug", "One extra equals sign asks for an item that does not exist")
    add_card(slide, 0.65, 2.05, 5.85, 3.75, COLORS["red"], "BUG: i <= items.length",
             ["Tries indexes 0, 1, 2, 3", "Index 3 is outside", "Prints undefined"], body_size=16)
    add_card(slide, 6.83, 2.05, 5.85, 3.75, COLORS["green"], "FIX: i < items.length",
             ["Tries indexes 0, 1, 2", "Every valid item once", "Stops before index 3"], body_size=16)
    add_takeaway_bar(slide, "For array indexes, less than is the reliable boundary.", COLORS["orange"])

    slide = new_slide(prs)
    add_slide_title(slide, "Make a Decision for Each Item", "Old if/else skills work inside the array loop")
    add_code_panel(slide, 0.7, 2.0, 8.0, 3.95,
                   ['const scores: number[] = [95, 68, 82];', '',
                    'for (let i = 0; i < scores.length; i++) {',
                    '  if (scores[i] >= 70) {',
                    '    console.log(`${scores[i]}: passed`);',
                    '  } else {',
                    '    console.log(`${scores[i]}: practice`);',
                    '  }', '}'], 15)
    add_card(slide, 9.05, 2.0, 3.6, 3.95, COLORS["teal"], "PREDICT",
             ["95: passed", "68: practice", "82: passed"], body_size=16)
    add_takeaway_bar(slide, "The same decision runs once for every score.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Accumulate Across the Array", "Keep the total outside the loop")
    add_code_panel(slide, 0.75, 2.05, 7.2, 3.7,
                   ['const numbers: number[] = [3, 5, 7];',
                    'let total: number = 0;', '',
                    'for (let i = 0; i < numbers.length; i++) {',
                    '  total = total + numbers[i];', '}', '',
                    'console.log(total);'], 16)
    add_card(slide, 8.3, 2.05, 4.35, 3.7, COLORS["orange"], "WATCH TOTAL GROW",
             ["0 + 3 = 3", "3 + 5 = 8", "8 + 7 = 15", "Final output: 15"], body_size=16)
    add_takeaway_bar(slide, "An accumulator remembers work from earlier rounds.", COLORS["teal"])

    slide = new_slide(prs)
    add_slide_title(slide, "AI Uses Collections of Examples", "Our program simulates one small data-review task")
    add_array_cells(slide, ["cat", "unknown", "dog", "unknown", "bird"], 0.45, 2.1, 2.25, COLORS["medium_blue"])
    add_arrow(slide, Inches(5.95), Inches(4.35), Inches(1.45), Inches(0.72), COLORS["orange"], "down")
    add_card(slide, 2.1, 5.1, 4.15, 1.0, COLORS["green"], "KNOWN LABEL",
             ["Continue"], title_size=15, body_size=12)
    add_card(slide, 7.08, 5.1, 4.15, 1.0, COLORS["purple"], "UNKNOWN LABEL",
             ["Human review"], title_size=15, body_size=12)
    add_takeaway_bar(slide, "Automatic checks can flag uncertainty; people decide what is correct.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Build the AI Data Checker", "Combine arrays, loops, decisions, and an accumulator")
    stages = [
        ("1. STORE", ["Create labels: string[]"], COLORS["medium_blue"]),
        ("2. VISIT", ["Loop to labels.length"], COLORS["teal"]),
        ("3. CHECK", ["Find \"unknown\""], COLORS["purple"]),
        ("4. COUNT", ["Report human reviews"], COLORS["orange"]),
    ]
    for index, (title, lines, color) in enumerate(stages):
        x = 0.75 + (index % 2) * 6.2
        y = 2.0 + (index // 2) * 2.0
        add_card(slide, x, y, 5.75, 1.65, color, title, lines, title_size=17, body_size=15)
    add_takeaway_bar(slide, "Build and test one checkpoint at a time.", COLORS["green"])

    slide = new_slide(prs)
    add_slide_title(slide, "The Completed Checker", "Predict the two review examples before Run")
    add_code_panel(slide, 0.65, 1.85, 8.7, 4.3,
                   ['const labels: string[] =', '  ["cat", "unknown", "dog", "unknown", "bird"];',
                    'let reviewCount: number = 0;', '',
                    'for (let i = 0; i < labels.length; i++) {',
                    '  const label: string = labels[i];',
                    '  if (label === "unknown") {',
                    '    console.log(`Example ${i + 1} needs review.`);',
                    '    reviewCount++;', '  }', '}',
                    'console.log(`${reviewCount} need review.`);'], 13)
    add_card(slide, 9.7, 1.85, 2.95, 4.3, COLORS["green"], "EXPECTED",
             ["Examples 2 and 4", "need review", "Final count: 2"], title_size=17, body_size=15)
    add_takeaway_bar(slide, "The program flags possible problems; a human investigates them.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_slide_title(slide, "Common Array Mistakes", "Predict, trace, and repair")
    mistakes = [
        ("START AT 1", ["Skips index 0"], COLORS["red"]),
        ("USE <= LENGTH", ["Tries one extra index"], COLORS["orange"]),
        ("MIX ITEM TYPES", ["Breaks the typed list"], COLORS["purple"]),
        ("RESET TOTAL", ["Loses earlier rounds"], COLORS["medium_blue"]),
    ]
    for index, (title, lines, color) in enumerate(mistakes):
        x = 0.7 + (index % 2) * 6.25
        y = 2.0 + (index // 2) * 1.95
        add_card(slide, x, y, 5.75, 1.55, color, title, lines, title_size=16, body_size=14)
    add_takeaway_bar(slide, "Trace the first index, the final index, and the stop check.", COLORS["teal"])

    slide = new_slide(prs)
    add_slide_title(slide, "Today's Classwork Missions", "Complete the core path before the bonus")
    missions = [
        ("Loop readiness", COLORS["medium_blue"]),
        ("Build typed arrays", COLORS["teal"]),
        ("Index and length lab", COLORS["purple"]),
        ("Trace an array loop", COLORS["green"]),
        ("AI data checker", COLORS["orange"]),
        ("Repair the boundary bug", COLORS["red"]),
    ]
    for index, (text, color) in enumerate(missions):
        add_agenda_item(slide, index + 1, text, 2.0 + index * 0.65, color)
    add_takeaway_bar(slide, "Predict first. Run second. Explain what happened.", COLORS["dark_blue"])

    slide = new_slide(prs)
    add_full_bg(slide, COLORS["dark_blue"])
    add_styled_textbox(
        slide, Inches(0.75), Inches(0.75), Inches(11.83), Inches(0.7),
        "Arrays + Loops: The Reliable Pattern", font_size=34,
        font_color=COLORS["white"], bold=True, alignment=PP_ALIGN.CENTER,
        font_name="Segoe UI Semibold",
    )
    recap = [
        ("1", "Store related values in one typed array"),
        ("2", "Start the array index at 0"),
        ("3", "Use .length to count the items"),
        ("4", "Loop while i < items.length"),
        ("5", "Read the current item with items[i]"),
        ("6", "Test AI-related data; keep humans responsible"),
    ]
    for index, (number, text) in enumerate(recap):
        y = 1.75 + index * 0.77
        add_circle(slide, Inches(1.0), Inches(y), Inches(0.52),
                   [COLORS["light_blue"], COLORS["teal"], COLORS["purple"],
                    COLORS["green"], COLORS["orange"], COLORS["pink"]][index],
                   text=number, text_size=17)
        add_styled_textbox(
            slide, Inches(1.85), Inches(y + 0.04), Inches(10.4), Inches(0.48),
            text, font_size=19, font_color=COLORS["white"],
        )

    slide = new_slide(prs)
    add_full_bg(slide, COLORS["dark_blue"])
    add_styled_textbox(
        slide, Inches(0), Inches(1.25), Inches(13.33), Inches(1.1),
        "Questions?", font_size=54, font_color=COLORS["white"], bold=True,
        alignment=PP_ALIGN.CENTER, font_name="Segoe UI Semibold",
    )
    add_styled_textbox(
        slide, Inches(1.0), Inches(2.85), Inches(11.33), Inches(0.7),
        "Then: Kahoot and the homework walkthrough", font_size=24,
        font_color=COLORS["sky_blue"], alignment=PP_ALIGN.CENTER,
    )
    add_rounded_box(
        slide, Inches(3.1), Inches(4.35), Inches(7.13), Inches(1.0),
        COLORS["orange"], text="First index?  Last index?  Stop condition?",
        text_size=20, text_color=COLORS["dark_blue"],
    )


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)
    build(prs)

    lesson_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(
        lesson_dir, "2026-08-15_TypeScript_Arrays_and_Loops.pptx"
    )
    prs.core_properties.title = "TypeScript Arrays and Loops"
    prs.core_properties.subject = "Kids Computer Science - August 15, 2026"
    prs.core_properties.author = "Kids Computer Science"
    prs.save(output_path)
    print(f"Created {output_path}")
    print(f"Slides: {len(prs.slides)}")


if __name__ == "__main__":
    main()