"""
Kahoot Quiz Generator - June 6, 2026
Agentic AI Mission Control

Usage:
    py create_kahoot_excel.py
"""

import os
from openpyxl import Workbook


QUESTIONS = [
    (
        "What is the main difference between vibe coding and agentic coding?",
        "Vibe coding uses computers, agentic coding does not",
        "Agentic coding includes goals, tools, testing, and supervision",
        "Vibe coding is always wrong",
        "Agentic coding means the human does nothing",
        25,
        2,
    ),
    (
        "Why should an agent have success criteria before it starts?",
        "So it can type faster",
        "So we know how to check whether the task is actually done",
        "So it can avoid using tools",
        "So the app looks more colorful",
        25,
        2,
    ),
    (
        "Which item belongs in the Allowed Tools part of an agent job brief?",
        "Delete anything you want",
        "Browser preview and code editor",
        "Never test the app",
        "Guess if you are unsure",
        20,
        2,
    ),
    (
        "Which action should usually require human approval?",
        "Reading a test checklist",
        "Explaining what HTML means",
        "Deleting files or sending messages",
        "Changing a button color in a toy app",
        25,
        3,
    ),
    (
        "In plan -> act -> observe -> test -> refine, what does observe mean?",
        "Look at the result of what the AI just changed",
        "Ignore the app and keep prompting",
        "Let the AI do anything",
        "Close the browser",
        20,
        1,
    ),
    (
        "Why is 'Make only one change' a useful instruction?",
        "It makes the AI stop working forever",
        "It helps you test what changed and catch mistakes",
        "It prevents the app from having colors",
        "It only works in Python",
        25,
        2,
    ),
    (
        "What is a test checklist for?",
        "Proving the AI is always perfect",
        "Checking the app works before calling it finished",
        "Replacing the need to preview the app",
        "Making the assignment longer for no reason",
        20,
        2,
    ),
    (
        "Which is the best example of a clear success criterion?",
        "Make it cool",
        "Make it better",
        "The restart button resets the score to 0",
        "Do computer stuff",
        20,
        3,
    ),
    (
        "What can happen if an AI agent has powerful tools but weak rules?",
        "It can make risky changes without asking",
        "It becomes unable to answer questions",
        "It can only write poems",
        "It stops needing the internet",
        25,
        1,
    ),
    (
        "Why are tool-using AI agents important to understand safely?",
        "They can connect AI to real files, browsers, commands, and messages",
        "They only make drawings",
        "They never use permissions",
        "They are just normal calculators",
        25,
        1,
    ),
    (
        "Which prompt is safest for improving an app?",
        "Delete the app and rebuild everything however you want",
        "Make only the score easier to read; keep everything else working",
        "Change everything until you think it is done",
        "Add logins and collect student emails",
        25,
        2,
    ),
    (
        "If AI says a bug is fixed but the app still fails, what should you do?",
        "Trust it because AI is always correct",
        "Test again, describe the failure, and refine the prompt",
        "Submit without checking",
        "Delete your classwork",
        25,
        2,
    ),
    (
        "Which tool would an agent most likely use to check how a web app looks?",
        "Browser or preview",
        "Calendar",
        "Email",
        "Camera roll",
        20,
        1,
    ),
    (
        "What is the human's job in supervised agentic AI?",
        "Let the agent do everything without checking",
        "Set goals, approve risky actions, test results, and refine",
        "Memorize all JavaScript first",
        "Avoid using prompts",
        25,
        2,
    ),
    (
        "Which belongs in the Not Allowed part of a job brief for class?",
        "Do not collect personal information",
        "Use the preview tab",
        "Make the text easier to read",
        "Explain what changed",
        20,
        1,
    ),
]


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Kahoot Questions"
    ws.append([
        "Question",
        "Answer 1",
        "Answer 2",
        "Answer 3",
        "Answer 4",
        "Time limit",
        "Correct answer",
    ])

    for question in QUESTIONS:
        ws.append(list(question))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-06-06_Kahoot_Import.xlsx")
    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")


if __name__ == "__main__":
    main()
