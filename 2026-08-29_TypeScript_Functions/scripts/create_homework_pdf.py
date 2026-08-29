"""Create the fillable August 29 TypeScript functions homework PDF."""

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
        "Homework: TypeScript Functions",
        "August 29, 2026 homework",
    )

    pdf.start_page(
        "Homework: TypeScript Functions",
        "100 points + 5 bonus | Due before class on September 5, 2026",
    )
    add_student_header(pdf, "hw")
    pdf.section(532, "Part 1 - Match the Vocabulary", "15 points", BLUE)
    pdf.wrapped(
        48,
        500,
        "Match these terms: Function, Definition, Call, Parameter, Argument, and Return.",
        size=9.2,
    )
    meanings = [
        "A. A value sent into one function call",
        "B. A reusable named job",
        "C. A value sent back to the calling code",
        "D. Code that describes the function and its body",
        "E. A command that runs a function",
        "F. A named input in the function definition",
    ]
    for index, meaning in enumerate(meanings):
        pdf.text(58, 465 - index * 22, meaning, size=8.7)
    pdf.text(48, 320, "Write the six matching letters in term order:", bold=True)
    pdf.field("hw_vocabulary_matches", 48, 275, 522, 30)
    pdf.text(48, 255, "Explain parameter versus argument in your own words:", bold=True)
    pdf.field("hw_parameter_argument", 48, 165, 522, 70, multiline=True)
    pdf.note(
        48,
        145,
        522,
        64,
        "Tool options",
        "Predict first. Check in VS Code. If it fails, use typescriptlang.org/play.",
        fill=PALE_GREEN,
    )

    pdf.start_page("Predict the Output", "Part 2 | 20 points")
    pdf.section(646, "Part 2A - Count the Calls", "8 points", CYAN)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function beep() {",
            '  console.log("Beep!");',
            "}",
            "beep();",
            "beep();",
        ],
        font_size=8.7,
    )
    pdf.text(48, 510, "Write the output, count the calls, and predict the no-call version:", bold=True)
    pdf.field("hw_output_a", 48, 385, 522, 105, multiline=True, font_size=8)
    pdf.section(345, "Part 2B - Trace the Parameter", "12 points", PURPLE)
    pdf.code_box(
        48,
        308,
        522,
        [
            "function showDouble(number: number) {",
            "  console.log(number * 2);",
            "}",
            "showDouble(4);",
            "showDouble(7);",
            "showDouble(10);",
        ],
        font_size=8.4,
    )
    pdf.text(48, 205, "Write the output and the parameter value during each call:", bold=True)
    pdf.field("hw_output_b", 48, 95, 522, 90, multiline=True, font_size=8)

    pdf.start_page("Parameters and Arguments", "Part 3 | 20 points")
    pdf.section(646, "Part 3 - Match Inputs by Position", "20 points", PURPLE)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function describePet(name: string, age: number) {",
            "  console.log(`${name} is ${age} years old.`);",
            "}",
            'describePet("Pixel", 3);',
        ],
        font_size=8.5,
    )
    pdf.text(48, 520, "1-3. Name both parameters, their types, and their matching arguments:", bold=True)
    pdf.field("hw_pet_parts", 48, 410, 522, 90, multiline=True, font_size=8)
    pdf.text(48, 390, "4. Write two new valid calls and predict one output:", bold=True)
    pdf.field("hw_pet_calls", 48, 285, 522, 85, multiline=True, font_size=8)
    pdf.text(48, 265, "5-6. Explain both broken calls:", bold=True)
    pdf.code_box(
        48,
        240,
        522,
        ['describePet(3, "Pixel");', 'describePet("Pixel");'],
        font_size=8.5,
    )
    pdf.field("hw_pet_bugs", 48, 85, 522, 105, multiline=True, font_size=8)

    pdf.start_page("Finish the Functions", "Part 4 | 20 points")
    pdf.section(646, "Part 4A - Complete a Greeting", "6 points", GREEN)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function greetStudent(____: string) {",
            "  console.log(`Hello, ${____}!`);",
            "}",
            'greetStudent("Ari");',
        ],
        font_size=8.5,
    )
    pdf.field("hw_finish_a", 48, 470, 522, 75, multiline=True, font_size=8)
    pdf.section(430, "Part 4B - Complete a Decision", "6 points", ORANGE)
    pdf.code_box(
        48,
        393,
        522,
        [
            "function checkTemperature(temperature: ____) {",
            "  if (temperature >= 80) {",
            '    console.log("Hot");',
            "  } ____ {",
            '    console.log("Mild");',
            "  }",
            "}",
            "checkTemperature(____); // choose Mild",
        ],
        font_size=7.9,
        leading=9,
    )
    pdf.field("hw_finish_b", 48, 240, 522, 65, multiline=True, font_size=8)
    pdf.section(200, "Part 4C - Design Two Inputs", "8 points", BLUE)
    pdf.wrapped(
        48,
        170,
        "Write showProduct(item: string, price: number). Print one sentence and call it twice with valid arguments.",
        size=8.8,
    )
    pdf.field("hw_finish_c", 48, 65, 522, 80, multiline=True, font_size=8)

    pdf.start_page("Find and Repair the Bugs", "Part 5A | 15 points total")
    pdf.section(646, "Bug A - Missing Argument", "5 points", RED)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function welcome(name: string) {",
            "  console.log(`Welcome, ${name}!`);",
            "}",
            "welcome();",
        ],
        font_size=8.5,
    )
    pdf.text(48, 520, "Explain, repair, and predict:", bold=True)
    pdf.field("hw_bug_a", 48, 410, 522, 90, multiline=True, font_size=8)
    pdf.section(370, "Bug B - Wrong Argument Type", "5 points", RED)
    pdf.code_box(
        48,
        333,
        522,
        [
            "function showLevel(level: number) {",
            "  console.log(`Level ${level}`);",
            "}",
            'showLevel("five");',
        ],
        font_size=8.5,
    )
    pdf.text(48, 248, "Explain, repair, and predict:", bold=True)
    pdf.field("hw_bug_b", 48, 105, 522, 123, multiline=True, font_size=8)

    pdf.start_page("Repair One More Bug", "Part 5B | 5 points")
    pdf.section(646, "Bug C - Defined but Never Called", "5 points", RED)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function announceWinner(winner: string) {",
            "  console.log(`${winner} wins!`);",
            "}",
        ],
        font_size=8.6,
    )
    pdf.text(48, 530, "Explain why there is no output:", bold=True)
    pdf.field("hw_bug_c_explain", 48, 440, 522, 70, multiline=True)
    pdf.text(48, 420, "Add a valid call and predict the repaired output:", bold=True)
    pdf.field("hw_bug_c_repair", 48, 300, 522, 100, multiline=True, font_size=8)
    pdf.note(
        48,
        270,
        522,
        78,
        "Debugging checklist",
        "Find the call. Count the arguments. Match each argument type and position to its parameter.",
    )

    pdf.start_page("AI Review Reflection", "Part 6 | 10 points")
    pdf.section(646, "Part 6 - One Reusable Review Rule", "10 points", PURPLE)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function reviewLabel(label: string) {",
            '  if (label === "unknown") {',
            '    console.log("Human review needed.");',
            "  } else {",
            "    console.log(`${label}: accepted for now.`);",
            "  }",
            "}",
            'reviewLabel("tree");',
            'reviewLabel("unknown");',
        ],
        font_size=7.8,
        leading=10,
    )
    pdf.text(48, 470, "Predict both outputs; identify the parameter and both arguments:", bold=True)
    pdf.field("hw_ai_parts", 48, 335, 522, 115, multiline=True, font_size=8)
    pdf.text(48, 315, "Why is accepted for now more accurate than guaranteed correct?", bold=True)
    pdf.field("hw_ai_accuracy", 48, 225, 522, 70, multiline=True)
    pdf.text(48, 205, "What should a person inspect when the helper flags unknown?", bold=True)
    pdf.field("hw_ai_human", 48, 120, 522, 65, multiline=True)
    pdf.submission_bar("Core homework total: 100 points")

    pdf.start_page("Bonus: Return a Boolean", "+5 bonus points")
    pdf.section(646, "Bonus - Complete isPassing", "+5 points", CYAN)
    pdf.code_box(
        48,
        605,
        522,
        [
            "function isPassing(score: number): boolean {",
            "  if (score >= 70) {",
            "    return ____;",
            "  } else {",
            "    return ____;",
            "  }",
            "}",
        ],
        font_size=8.4,
    )
    pdf.text(48, 490, "Fill both blanks and predict isPassing(92) and isPassing(61):", bold=True)
    pdf.field("hw_bonus_complete", 48, 370, 522, 100, multiline=True, font_size=8)
    pdf.text(48, 350, "Why does this function return a value instead of only printing one?", bold=True)
    pdf.field("hw_bonus_explain", 48, 240, 522, 90, multiline=True)
    pdf.note(
        48,
        210,
        522,
        70,
        "Return reminder",
        "The parameter type describes what goes in. The return type describes what comes back.",
        fill=PALE_GREEN,
    )
    pdf.submission_bar(
        "Send ONLY to Ishwari ma'am + Khushi ma'am (assistant teachers) - not Teams."
    )
    pdf.save()


def main():
    lesson_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(
        lesson_dir, "2026-08-29_Homework_TypeScript_Functions.pdf"
    )
    create_homework(output_path)
    print(f"Created {output_path}")


if __name__ == "__main__":
    main()
