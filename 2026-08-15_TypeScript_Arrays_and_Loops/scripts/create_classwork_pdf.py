"""Create the fillable August 15 arrays and loops classwork PDF."""

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


def create_classwork(output_path):
    pdf = FillableLessonPDF(
        output_path,
        "Classwork: TypeScript Arrays and Loops",
        "August 15, 2026 classwork",
    )

    pdf.start_page(
        "Classwork: TypeScript Arrays and Loops",
        "100 points + 10 bonus | Predict first, then run in VS Code",
    )
    add_student_header(pdf, "cw")
    pdf.section(532, "Part 1 - Loop Readiness Check", "10 points", BLUE)
    pdf.code_box(
        48,
        496,
        522,
        [
            "for (let i = 0; i < 4; i++) {",
            "  console.log(i);",
            "}",
        ],
        font_size=9.2,
    )
    pdf.text(48, 430, "Predict the starting value and all values that print:", bold=True)
    pdf.field("cw_loop_prediction", 48, 355, 522, 60, multiline=True)
    pdf.text(48, 340, "What check becomes false and stops the loop?", bold=True)
    pdf.field("cw_loop_stop", 48, 275, 522, 50, multiline=True)
    pdf.text(48, 260, "Why does 4 not print?", bold=True)
    pdf.field("cw_loop_boundary", 48, 195, 522, 50, multiline=True)
    pdf.text(48, 180, "Did the real output match your prediction?", bold=True)
    pdf.field("cw_loop_match", 48, 140, 522, 25)
    pdf.note(
        48,
        115,
        522,
        50,
        "Readiness rule",
        "If this trace is confusing, ask for help before moving to array indexes.",
        fill=PALE_GREEN,
    )

    pdf.start_page("Build Typed Arrays", "Classwork continued")
    pdf.section(646, "Part 2 - Build Typed Arrays", "15 points", CYAN)
    pdf.wrapped(
        48,
        614,
        "Create both arrays. Then explain what each type annotation allows inside the list.",
    )
    pdf.code_box(
        48,
        578,
        522,
        [
            'const players: string[] = ["Maya", "Leo", "Zara"];',
            "const scores: number[] = [78, 91, 84];",
        ],
        font_size=8.8,
    )
    pdf.text(48, 520, "What does string[] tell TypeScript?", bold=True)
    pdf.field("cw_string_array", 48, 455, 522, 45, multiline=True)
    pdf.text(48, 440, "What does number[] tell TypeScript?", bold=True)
    pdf.field("cw_number_array", 48, 375, 522, 45, multiline=True)
    pdf.text(48, 360, "How many variables store all six starting values?", bold=True)
    pdf.field("cw_array_variable_count", 48, 325, 522, 25)
    pdf.text(48, 310, "Rewrite both arrays after adding one matching item to each:", bold=True)
    pdf.field("cw_extended_arrays", 48, 210, 522, 85, multiline=True, font_size=8)
    pdf.text(48, 195, "Predict what TypeScript reports if scores contains the string high:", bold=True)
    pdf.field("cw_wrong_type", 48, 105, 522, 60, multiline=True)

    pdf.start_page("Index and Length Lab", "Classwork continued")
    pdf.section(646, "Part 3 - Index and Length Lab", "20 points", PURPLE)
    pdf.code_box(
        48,
        605,
        522,
        ['const colors: string[] = ["red", "green", "blue", "gold"];'],
        font_size=8.8,
    )
    pdf.text(48, 568, "Record a prediction and actual result for each expression:", bold=True)
    pdf.wrapped(
        48,
        548,
        "colors[0] | colors[1] | colors[3] | colors.length | colors[colors.length - 1]",
        size=8.8,
    )
    pdf.field("cw_index_table", 48, 410, 522, 130, multiline=True, font_size=8)
    pdf.text(48, 395, "Explain the first index, final index, and why length is different:", bold=True)
    pdf.field("cw_index_explanation", 48, 320, 522, 60, multiline=True)
    pdf.text(48, 305, "Write one line that changes green to lime:", bold=True)
    pdf.field("cw_change_item", 48, 260, 522, 28, font_size=8)
    pdf.text(48, 245, "What appears for colors[4], and why?", bold=True)
    pdf.field("cw_out_of_range", 48, 165, 522, 65, multiline=True)
    pdf.note(
        48,
        140,
        522,
        64,
        "Remember",
        "Length is the number of items. The final valid index is length - 1.",
    )

    pdf.start_page("Trace an Array Loop", "Classwork continued")
    pdf.section(646, "Part 4 - Trace an Array Loop", "20 points", GREEN)
    pdf.code_box(
        48,
        605,
        522,
        [
            'const planets: string[] = ["Mercury", "Venus", "Earth"];',
            "",
            "for (let i = 0; i < planets.length; i++) {",
            "  console.log(`Index ${i}: ${planets[i]}`);",
            "}",
        ],
        font_size=8.4,
    )
    pdf.text(48, 512, "Trace rounds 1, 2, 3, and the final stop check:", bold=True)
    pdf.field("cw_array_trace", 48, 350, 522, 140, multiline=True, font_size=8)
    pdf.text(48, 335, "What are the two jobs of i?", bold=True)
    pdf.field("cw_i_jobs", 48, 265, 522, 55, multiline=True)
    pdf.text(48, 250, "Why use planets.length instead of typing 3?", bold=True)
    pdf.field("cw_length_reason", 48, 180, 522, 55, multiline=True)
    pdf.text(48, 165, "What code changes if a fourth planet is added?", bold=True)
    pdf.field("cw_fourth_planet", 48, 110, 522, 40, multiline=True)

    pdf.start_page("AI Training Data Checker", "Classwork continued")
    pdf.section(646, "Part 5 - AI Training Data Checker", "25 points", ORANGE)
    pdf.wrapped(
        48,
        614,
        "This program flags uncertain labels for a person to inspect. It is a data-review simulation, not an AI model.",
    )
    pdf.code_box(
        48,
        574,
        522,
        [
            'const labels: string[] = ["cat", "unknown", "dog",',
            '  "unknown", "bird"];',
            "let reviewCount: number = 0;",
            "for (let i = 0; i < labels.length; i++) {",
            "  const label: string = labels[i];",
            '  if (label === "unknown") {',
            "    console.log(`Example ${i + 1} needs human review.`);",
            "    reviewCount++;",
            "  } else {",
            "    console.log(`Example ${i + 1}: ${label}`);",
            "  }",
            "}",
            "console.log(`${reviewCount} examples need human review.`);",
        ],
        font_size=7.2,
        leading=9,
    )
    pdf.text(48, 406, "Predict all output lines, review indexes, and the final count:", bold=True)
    pdf.field("cw_ai_predictions", 48, 310, 522, 80, multiline=True, font_size=8)
    pdf.text(48, 295, "Explain the accumulator, i + 1, the simulation, and human review:", bold=True)
    pdf.field("cw_ai_explanations", 48, 120, 522, 160, multiline=True, font_size=8)
    pdf.note(
        48,
        100,
        522,
        48,
        "Human responsibility",
        "A checker can flag uncertainty. A person still decides whether a label is correct.",
        fill=PALE_GREEN,
    )

    pdf.start_page("Repair, Bonus, and Submit", "Classwork conclusion")
    pdf.section(646, "Part 6 - Repair the Boundary Bug", "10 points", RED)
    pdf.code_box(
        48,
        605,
        522,
        [
            'const missions: string[] = ["Map", "Build", "Test"];',
            "for (let i = 0; i <= missions.length; i++) {",
            "  console.log(missions[i]);",
            "}",
        ],
        font_size=8.5,
    )
    pdf.text(48, 510, "Explain the attempted indexes, unexpected output, and one-character fix:", bold=True)
    pdf.field("cw_boundary_repair", 48, 355, 522, 120, multiline=True, font_size=8)
    pdf.section(320, "Bonus - Add Another Review Rule", "+10 points", PURPLE)
    pdf.wrapped(
        48,
        288,
        "Use seven labels, keep unknown, add a familiar second rule, and trace two rounds. Explain why the loop stops correctly.",
    )
    pdf.field("cw_bonus_rule", 48, 120, 522, 150, multiline=True, font_size=8)
    pdf.submission_bar("Submit to Microsoft Teams AND Ishwari Raut ma'am.")
    pdf.save()


def main():
    lesson_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(
        lesson_dir, "2026-08-15_Classwork_TypeScript_Arrays_and_Loops.pdf"
    )
    create_classwork(output_path)
    print(f"Created {output_path}")


if __name__ == "__main__":
    main()