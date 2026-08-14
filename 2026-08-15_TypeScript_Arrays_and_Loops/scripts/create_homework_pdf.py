"""Create the fillable August 15 arrays and loops homework PDF."""

import os

from pdf_theme import (
    BLUE,
    CYAN,
    GREEN,
    ORANGE,
    PALE_GREEN,
    PURPLE,
    RED,
    FillableLessonPDF,
    add_student_header,
)


def create_homework(output_path):
    pdf = FillableLessonPDF(
        output_path,
        "Homework: TypeScript Arrays and Loops",
        "August 15, 2026 homework",
    )

    pdf.start_page(
        "Homework: TypeScript Arrays and Loops",
        "100 points + 5 bonus | Due before class on August 22, 2026",
    )
    add_student_header(pdf, "hw")
    pdf.section(532, "Part 1 - Match the Vocabulary", "15 points", BLUE)
    pdf.wrapped(
        48,
        500,
        "Match: Array, Item, Index, Length, Zero-based, and Out-of-range index.",
        size=9.2,
    )
    meanings = [
        "A. One variable that stores an ordered list",
        "B. One value inside an array",
        "C. The numbered address of an item",
        "D. The number of items in an array",
        "E. A first index of 0 instead of 1",
        "F. An index that is not inside the array",
    ]
    for index, meaning in enumerate(meanings):
        pdf.text(58, 470 - index * 22, meaning, size=8.8)
    pdf.text(48, 330, "Write the six matching letters in term order:", bold=True)
    pdf.field("hw_vocabulary_matches", 48, 285, 522, 30)
    pdf.text(48, 265, "Explain the difference between everyday position and array index:", bold=True)
    pdf.field("hw_position_vs_index", 48, 180, 522, 65, multiline=True)
    pdf.note(
        48,
        150,
        522,
        72,
        "No computer required",
        "Predict and explain first. You may run examples later to check your thinking.",
        fill=PALE_GREEN,
    )

    pdf.start_page("Index and Length Practice", "Homework continued")
    pdf.section(646, "Part 2 - Index and Length Practice", "20 points", CYAN)
    pdf.code_box(
        48,
        605,
        522,
        ['const snacks: string[] = ["apple", "popcorn", "yogurt", "pretzels"];'],
        font_size=8.4,
    )
    pdf.text(48, 565, "Answer questions 1-9 with values or TypeScript lines:", bold=True)
    pdf.wrapped(
        48,
        544,
        "Length; first index; last index; snacks[0]; snacks[2]; print pretzels; find the final item; change popcorn to carrots; explain snacks[4].",
        size=8.6,
    )
    pdf.field("hw_index_answers", 48, 350, 522, 170, multiline=True, font_size=8)
    pdf.text(48, 330, "10. Explain why the length and final index are different:", bold=True)
    pdf.field("hw_length_explanation", 48, 220, 522, 90, multiline=True)
    pdf.note(
        48,
        185,
        522,
        78,
        "Check your model",
        "Four items have length 4. Their valid indexes are 0, 1, 2, and 3.",
    )

    pdf.start_page("Predict the Output: A and B", "Part 3 | 20 points total")
    pdf.section(646, "Part 3A - Read Two Indexes", "", PURPLE)
    pdf.code_box(
        48,
        605,
        522,
        [
            "const levels: number[] = [2, 4, 6];",
            "console.log(levels[1]);",
            "console.log(levels.length);",
        ],
        font_size=8.8,
    )
    pdf.text(48, 545, "Write the exact two output lines:", bold=True)
    pdf.field("hw_output_a", 48, 480, 522, 50, multiline=True)
    pdf.section(435, "Part 3B - Trace Every Pet", "", GREEN)
    pdf.code_box(
        48,
        397,
        522,
        [
            'const pets: string[] = ["cat", "dog", "fish"];',
            "for (let i = 0; i < pets.length; i++) {",
            "  console.log(`${i}: ${pets[i]}`);",
            "}",
        ],
        font_size=8.5,
    )
    pdf.text(48, 320, "Write the exact three output lines:", bold=True)
    pdf.field("hw_output_b", 48, 215, 522, 85, multiline=True)
    pdf.text(48, 190, "Why does the first line begin with index 0?", bold=True)
    pdf.field("hw_output_b_reason", 48, 115, 522, 55, multiline=True)

    pdf.start_page("Predict the Output: C and D", "Part 3 continued")
    pdf.section(646, "Part 3C - Add an Array", "", ORANGE)
    pdf.code_box(
        48,
        605,
        522,
        [
            "const numbers: number[] = [3, 5, 7];",
            "let total: number = 0;",
            "for (let i = 0; i < numbers.length; i++) {",
            "  total = total + numbers[i];",
            "}",
            "console.log(total);",
        ],
        font_size=8.2,
    )
    pdf.text(48, 500, "Show how total changes, then write the final output:", bold=True)
    pdf.field("hw_output_c", 48, 405, 522, 75, multiline=True)
    pdf.section(365, "Part 3D - Decide for Each Temperature", "", RED)
    pdf.code_box(
        48,
        327,
        522,
        [
            "const temperatures: number[] = [72, 85, 68];",
            "for (let i = 0; i < temperatures.length; i++) {",
            "  if (temperatures[i] >= 80) {",
            '    console.log("Hot");',
            "  } else {",
            '    console.log("Mild");',
            "  }",
            "}",
        ],
        font_size=7.9,
        leading=9,
    )
    pdf.text(48, 215, "Write the exact three output lines:", bold=True)
    pdf.field("hw_output_d", 48, 105, 522, 85, multiline=True)

    pdf.start_page("Spot and Repair the Bugs", "Part 4 | 20 points")
    pdf.section(646, "Bug A - One Index Too Far", "10 points", RED)
    pdf.code_box(
        48,
        605,
        522,
        [
            'const games: string[] = ["Chess", "Soccer", "Tag"];',
            "for (let i = 0; i <= games.length; i++) {",
            "  console.log(games[i]);",
            "}",
        ],
        font_size=8.2,
    )
    pdf.text(48, 530, "Explain the problem and rewrite the condition:", bold=True)
    pdf.field("hw_bug_a", 48, 430, 522, 80, multiline=True)
    pdf.section(390, "Bug B - Accumulator in the Wrong Place", "10 points", ORANGE)
    pdf.code_box(
        48,
        352,
        522,
        [
            "const points: number[] = [10, 20, 30];",
            "for (let i = 0; i < points.length; i++) {",
            "  let total: number = 0;",
            "  total = total + points[i];",
            "}",
            "console.log(total);",
        ],
        font_size=8.0,
        leading=10,
    )
    pdf.text(48, 250, "Explain the scope problem and rewrite the complete program:", bold=True)
    pdf.field("hw_bug_b", 48, 85, 522, 145, multiline=True, font_size=8)

    pdf.start_page("Design a List Program", "Part 5 | 15 points")
    pdf.section(646, "Part 5 - Design a List Program", "15 points", GREEN)
    pdf.wrapped(
        48,
        614,
        "Create one typed array with at least four values, loop to .length, read items[i], and print the current item with a template literal.",
    )
    pdf.text(48, 565, "Program theme and one-sentence goal:", bold=True)
    pdf.field("hw_design_goal", 48, 505, 522, 45, multiline=True)
    pdf.text(48, 485, "Write the complete TypeScript program:", bold=True)
    pdf.field("hw_design_code", 48, 220, 522, 245, multiline=True, font_size=8)
    pdf.text(48, 200, "Describe the expected output:", bold=True)
    pdf.field("hw_design_output", 48, 110, 522, 70, multiline=True)

    pdf.start_page("AI Reflection, Bonus, and Submit", "Homework conclusion")
    pdf.section(646, "Part 6 - AI Data Reflection", "10 points", PURPLE)
    pdf.code_box(
        48,
        605,
        522,
        ['const labels: string[] = ["tree", "unknown", "car", "tree", "unknown"];'],
        font_size=8.2,
    )
    pdf.text(48, 565, "Answer all five questions:", bold=True)
    pdf.wrapped(
        48,
        544,
        "Find the length and unknown indexes. Explain why uncertainty is flagged, what a loop repeats consistently, and what decision still needs a person.",
        size=8.6,
    )
    pdf.field("hw_ai_reflection", 48, 330, 522, 190, multiline=True, font_size=8)
    pdf.section(290, "Bonus - Extend and Predict", "+5 points", CYAN)
    pdf.wrapped(
        48,
        258,
        "Add one label. Give the new array, length, final index, and expected output for the added item.",
    )
    pdf.field("hw_bonus_extend", 48, 120, 522, 110, multiline=True, font_size=8)
    pdf.submission_bar("Submit to Microsoft Teams AND Ishwari Raut ma'am.")
    pdf.save()


def main():
    lesson_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(
        lesson_dir, "2026-08-15_Homework_TypeScript_Arrays_and_Loops.pdf"
    )
    create_homework(output_path)
    print(f"Created {output_path}")


if __name__ == "__main__":
    main()