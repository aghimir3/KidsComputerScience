"""Create the fillable August 29 TypeScript functions classwork PDF."""

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
        "Classwork: TypeScript Functions",
        "August 29, 2026 classwork",
    )

    pdf.start_page(
        "Classwork: TypeScript Functions",
        "100 points + 10 bonus | Define once, call many times",
    )
    add_student_header(pdf, "cw")
    pdf.section(532, "Part 1 - Definition or Call?", "10 points", BLUE)
    pdf.code_box(
        48,
        496,
        522,
        [
            "function celebrate() {",
            '  console.log("Mission complete!");',
            "}",
            "",
            "celebrate();",
            "celebrate();",
        ],
        font_size=8.8,
    )
    pdf.text(48, 398, "Identify the definition, one call, and the number of outputs:", bold=True)
    pdf.field("cw_definition_call", 48, 290, 522, 90, multiline=True, font_size=8)
    pdf.text(48, 270, "What would print if both calls were deleted? Why?", bold=True)
    pdf.field("cw_without_calls", 48, 190, 522, 60, multiline=True)
    pdf.text(48, 170, "Explain defining versus calling in your own words:", bold=True)
    pdf.field("cw_define_vs_call", 48, 90, 522, 60, multiline=True)
    pdf.note(
        48,
        78,
        522,
        42,
        "Core rule",
        "A definition describes the job. A call runs the job.",
        fill=PALE_GREEN,
    )

    pdf.start_page("Define Once, Call Many Times", "Part 2 | 15 points")
    pdf.section(646, "Part 2 - Reuse One Function", "15 points", CYAN)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function showWarmUp() {",
            '  console.log("Open your file.");',
            '  console.log("Read the goal.");',
            '  console.log("Predict before running.");',
            "}",
        ],
        font_size=8.5,
    )
    pdf.text(48, 510, "Predict the output before adding a call:", bold=True)
    pdf.field("cw_warmup_no_call", 48, 445, 522, 45, multiline=True)
    pdf.text(48, 425, "Write three calls, then record the complete output:", bold=True)
    pdf.field("cw_warmup_calls_output", 48, 245, 522, 160, multiline=True, font_size=8)
    pdf.text(48, 225, "How many times did the body run, and how do you know?", bold=True)
    pdf.field("cw_warmup_run_count", 48, 150, 522, 55, multiline=True)
    pdf.text(48, 130, "Why is this easier to reuse than copied output lines?", bold=True)
    pdf.field("cw_warmup_reuse", 48, 75, 522, 40, multiline=True)

    pdf.start_page("Parameters and Arguments", "Part 3 | 20 points")
    pdf.section(646, "Part 3A - One Typed Parameter", "12 points", PURPLE)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function greetPlayer(name: string) {",
            "  console.log(`Welcome, ${name}!`);",
            "}",
            'greetPlayer("Maya");',
            'greetPlayer("Leo");',
        ],
        font_size=8.4,
    )
    pdf.text(48, 510, "Name the function, parameter, type, and arguments. Predict both outputs:", bold=True)
    pdf.field("cw_one_parameter", 48, 380, 522, 110, multiline=True, font_size=8)
    pdf.text(48, 360, "Write a third call and explain why greetPlayer(42) is rejected:", bold=True)
    pdf.field("cw_one_parameter_call", 48, 285, 522, 55, multiline=True, font_size=8)
    pdf.section(245, "Part 3B - Two Typed Parameters", "8 points", GREEN)
    pdf.code_box(
        48,
        208,
        522,
        [
            "function reportScore(player: string, score: number) {",
            "  console.log(`${player} scored ${score} points.`);",
            "}",
            'reportScore("Zara", 95);',
        ],
        font_size=8.1,
    )
    pdf.text(48, 130, "Match by position, add one call, and repair reportScore(95, \"Zara\"):", bold=True)
    pdf.field("cw_two_parameters", 48, 65, 522, 50, multiline=True, font_size=8)

    pdf.start_page("A Decision Inside a Function", "Part 4 | 20 points")
    pdf.section(646, "Part 4 - Reuse a Familiar Decision", "20 points", GREEN)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function checkScore(score: number) {",
            "  if (score >= 80) {",
            "    console.log(`${score}: mission passed`);",
            "  } else {",
            "    console.log(`${score}: keep practicing`);",
            "  }",
            "}",
            "checkScore(92);",
            "checkScore(67);",
            "checkScore(80);",
        ],
        font_size=7.9,
        leading=10,
    )
    pdf.text(48, 474, "Predict the exact three output lines:", bold=True)
    pdf.field("cw_decision_output", 48, 365, 522, 90, multiline=True, font_size=8)
    pdf.text(48, 345, "Why does 80 pass? What old skill is reused inside the function?", bold=True)
    pdf.field("cw_decision_explain", 48, 260, 522, 65, multiline=True)
    pdf.text(48, 240, "Add an else-branch call. Change the boundary to 70 and predict again:", bold=True)
    pdf.field("cw_decision_change", 48, 95, 522, 125, multiline=True, font_size=8)

    pdf.start_page("AI Label Review Helper", "Part 5A | 25 points total")
    pdf.section(646, "Part 5A - Define and Call the Review Rule", "12 points", ORANGE)
    pdf.wrapped(
        48,
        614,
        "This is a rule-based review helper, not an AI model. A person remains responsible for checking the original example.",
    )
    pdf.code_box(
        48,
        568,
        522,
        [
            "function reviewLabel(label: string) {",
            '  if (label === "unknown") {',
            '    console.log("Human review needed.");',
            "  } else {",
            "    console.log(`${label}: label accepted for now.`);",
            "  }",
            "}",
            'reviewLabel("cat");',
            'reviewLabel("unknown");',
            'reviewLabel("tree");',
        ],
        font_size=7.8,
        leading=10,
    )
    pdf.text(48, 435, "Predict all three outputs and identify the review-triggering argument:", bold=True)
    pdf.field("cw_ai_calls", 48, 300, 522, 115, multiline=True, font_size=8)
    pdf.text(48, 280, "What prints before any call is added? Explain:", bold=True)
    pdf.field("cw_ai_no_call", 48, 205, 522, 55, multiline=True)
    pdf.text(48, 185, "Why say accepted for now instead of guaranteed correct?", bold=True)
    pdf.field("cw_ai_wording", 48, 90, 522, 75, multiline=True)

    pdf.start_page("Reuse the AI Helper in a Loop", "Part 5B | 13 points")
    pdf.section(646, "Part 5B - Call Once Per Array Item", "13 points", ORANGE)
    pdf.code_box(
        48,
        605,
        522,
        [
            'const labels: string[] = ["cat", "unknown", "tree", "unknown"];',
            "",
            "for (let i = 0; i < labels.length; i++) {",
            "  reviewLabel(labels[i]);",
            "}",
        ],
        font_size=8.2,
    )
    pdf.text(48, 510, "Trace each round: i, argument, and output:", bold=True)
    pdf.field("cw_ai_loop_trace", 48, 340, 522, 150, multiline=True, font_size=8)
    pdf.text(48, 320, "How many calls happen? Which arguments request review?", bold=True)
    pdf.field("cw_ai_loop_count", 48, 245, 522, 55, multiline=True)
    pdf.text(48, 225, "Add one known and one unknown label. Predict the added outputs:", bold=True)
    pdf.field("cw_ai_extend", 48, 140, 522, 65, multiline=True, font_size=8)
    pdf.text(48, 120, "What must a person inspect before changing a label?", bold=True)
    pdf.field("cw_ai_human", 48, 65, 522, 40, multiline=True)

    pdf.start_page("Repair the Function Bugs", "Part 6 | 10 points")
    pdf.section(646, "Bug A - Defined but Never Called", "5 points", RED)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function showReady() {",
            '  console.log("Ready!");',
            "}",
        ],
        font_size=8.7,
    )
    pdf.text(48, 535, "Explain the problem, add the smallest fix, and predict the output:", bold=True)
    pdf.field("cw_bug_a", 48, 430, 522, 85, multiline=True, font_size=8)
    pdf.section(390, "Bug B - Arguments in the Wrong Order", "5 points", RED)
    pdf.code_box(
        48,
        352,
        522,
        [
            "function showItem(item: string, quantity: number) {",
            "  console.log(`${quantity} ${item}`);",
            "}",
            'showItem(3, "notebooks");',
        ],
        font_size=8.1,
    )
    pdf.text(48, 270, "Explain the contract problem, repair the call, and predict the output:", bold=True)
    pdf.field("cw_bug_b", 48, 125, 522, 125, multiline=True, font_size=8)
    pdf.submission_bar("Core score: 100 points | Continue only if return was introduced.")

    pdf.start_page("Bonus: Return a Result", "+10 bonus points")
    pdf.section(646, "Bonus - A Typed Result Comes Back", "+10 points", PURPLE)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function needsReview(label: string): boolean {",
            '  if (label === "unknown") {',
            "    return true;",
            "  } else {",
            "    return false;",
            "  }",
            "}",
        ],
        font_size=8.3,
    )
    pdf.text(48, 490, "Predict the returned values for unknown and cat:", bold=True)
    pdf.field("cw_bonus_predictions", 48, 420, 522, 50, multiline=True)
    pdf.text(48, 400, "Store one result in a typed variable and print it:", bold=True)
    pdf.field("cw_bonus_store", 48, 320, 522, 60, multiline=True, font_size=8)
    pdf.text(48, 300, "Explain the difference between printing and returning:", bold=True)
    pdf.field("cw_bonus_print_return", 48, 220, 522, 60, multiline=True)
    pdf.text(48, 200, "Write isPassing(score: number): boolean using a boundary of 70:", bold=True)
    pdf.field("cw_bonus_is_passing", 48, 80, 522, 100, multiline=True, font_size=8)
    pdf.submission_bar("Submit to Microsoft Teams AND Ishwari Raut ma'am.")
    pdf.save()


def main():
    lesson_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(
        lesson_dir, "2026-08-29_Classwork_TypeScript_Functions.pdf"
    )
    create_classwork(output_path)
    print(f"Created {output_path}")


if __name__ == "__main__":
    main()
