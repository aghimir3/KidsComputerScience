"""
Kahoot Quiz Generator - February 28, 2026
Windows & Mac Command Line: Everything Connects

Usage:
    python create_kahoot_excel.py
"""

import os
from openpyxl import Workbook

# =============================================================================
# KAHOOT QUESTIONS (19 total)
# Format: (Question, Answer 1, Answer 2, Answer 3, Answer 4, Time limit, Correct Answer)
# Correct Answer = 1,2,3,4
# =============================================================================

QUESTIONS = [
    (
        "What is the Windows equivalent of the Linux command 'ls'?",
        "list",
        "dir",
        "show",
        "files",
        20,
        2,
    ),
    (
        "What is the Windows equivalent of the Linux command 'cat'?",
        "read",
        "view",
        "type",
        "open",
        20,
        3,
    ),
    (
        "What is the Windows equivalent of the Linux command 'rm'?",
        "erase",
        "del",
        "remove",
        "trash",
        20,
        2,
    ),
    (
        "What is the Windows equivalent of the Linux command 'cp'?",
        "duplicate",
        "clone",
        "paste",
        "copy",
        20,
        4,
    ),
    (
        "What is the Windows command to move a file?",
        "mv",
        "shift",
        "move",
        "transfer",
        20,
        3,
    ),
    (
        "What is the Windows command to clear the screen?",
        "clear",
        "cls",
        "wipe",
        "reset",
        20,
        2,
    ),
    (
        "What is the Windows command to rename a file?",
        "mv",
        "rename",
        "name",
        "ren",
        20,
        4,
    ),
    (
        "On Windows, how do you see your current directory?",
        "Type 'pwd'",
        "Type 'ls'",
        "Type 'cd' with no arguments",
        "Type 'where'",
        20,
        3,
    ),
    (
        "Which symbol does Windows use in file paths?",
        "Forward slash /",
        "Backslash \\",
        "Dash -",
        "Colon :",
        20,
        2,
    ),
    (
        "True or False: On Windows, 'MyFile.txt' and 'myfile.txt' are the same file.",
        "True -- Windows ignores case",
        "False -- Windows cares about case",
        "Only on old Windows versions",
        "Only for .txt files",
        20,
        1,
    ),
    (
        "True or False: Mac Terminal commands are basically the same as Linux.",
        "False -- they are completely different",
        "Only for networking commands",
        "True -- both are Unix-based",
        "Only for file commands",
        20,
        3,
    ),
    (
        "Why are Mac Terminal and Linux commands so similar?",
        "Both are made by Microsoft",
        "Both use the same keyboard",
        "Both cost the same",
        "Both are based on Unix",
        20,
        4,
    ),
    (
        "How do you create an empty file on Windows CMD (no 'touch' command)?",
        "touch file.txt",
        "echo. > file.txt",
        "create file.txt",
        "new file.txt",
        20,
        2,
    ),
    (
        "What keyboard shortcut opens Task Manager on Windows?",
        "Ctrl + Alt + T",
        "Cmd + Space",
        "Alt + F4",
        "Ctrl + Shift + Esc",
        20,
        4,
    ),
    (
        "What does the 'systeminfo' command show on Windows?",
        "A list of all files",
        "Your computer's details (name, OS, RAM)",
        "Your internet speed",
        "A list of installed games",
        20,
        2,
    ),
    (
        "Which command works the SAME on Linux, Windows, AND Mac?",
        "dir",
        "type",
        "mkdir",
        "del",
        20,
        3,
    ),
    (
        "What does 'cd ..' do on ALL operating systems?",
        "Lists files",
        "Deletes a folder",
        "Creates a file",
        "Goes up one directory level",
        20,
        4,
    ),
    (
        "AI tools like Claude Code run inside the terminal. Why is the command line important for AI?",
        "It's not -- AI only uses websites",
        "AI models train on Linux servers controlled through terminals",
        "The command line makes your internet faster",
        "AI was invented before websites existed",
        20,
        2,
    ),
    (
        "What is the main idea of today's lesson?",
        "Windows is better than Linux",
        "Mac is the only OS worth learning",
        "Same concepts, different syntax across OSes",
        "You should never use the command line",
        20,
        3,
    ),
]

# =============================================================================
# EXCEL GENERATOR
# =============================================================================

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

    for q in QUESTIONS:
        ws.append(list(q))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-02-28_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")

if __name__ == "__main__":
    main()
