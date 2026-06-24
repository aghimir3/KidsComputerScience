"""
Kahoot Quiz Generator - June 27, 2026
Your Own AI Assistant (OpenClaw) - LAST DAY of the AI unit

Usage:
    python create_kahoot_excel.py

Dependencies:
    pip install openpyxl
"""

import os
from openpyxl import Workbook

# =============================================================================
# KAHOOT QUESTIONS (15 total)
# Format: (Question, Answer 1, Answer 2, Answer 3, Answer 4, Time limit, Correct)
# Correct Answer = 1, 2, 3, or 4
# =============================================================================

QUESTIONS = [
    (
        "What is OpenClaw?",
        "A video game",
        "A free, open-source AI assistant you run on your own computer",
        "A web browser",
        "A type of password",
        20,
        2,
    ),
    (
        "Where does OpenClaw actually run?",
        "Only in the cloud",
        "On a school server",
        "On your own computer (local-first)",
        "Inside a web page",
        20,
        3,
    ),
    (
        "In class, how do you talk to your OpenClaw assistant?",
        "By typing in the terminal with 'openclaw chat'",
        "By sending it a letter",
        "By calling it on the phone",
        "You can't talk to it",
        20,
        1,
    ),
    (
        "What is the Gateway in OpenClaw?",
        "A door on a website",
        "The always-on 'brain' that keeps your assistant running",
        "A type of password",
        "A video filter",
        20,
        2,
    ),
    (
        "What does OpenRouter do for us?",
        "Slows down the internet",
        "Gives you one API key to reach many AI models",
        "Builds websites",
        "Deletes your files",
        20,
        2,
    ),
    (
        "Which AI model are we using today through OpenRouter?",
        "DeepSeek V4 Flash",
        "A toaster",
        "Dial-up",
        "No model at all",
        20,
        1,
    ),
    (
        "Your API key is most like a...",
        "Public poster",
        "Password you keep secret",
        "Phone number to share",
        "Sticker",
        20,
        2,
    ),
    (
        "What should you do before the assistant runs a command on your computer?",
        "Ignore it",
        "Unplug the computer",
        "Read it and approve it",
        "Close your eyes",
        20,
        3,
    ),
    (
        "What is 'ask' mode?",
        "The assistant asks permission before it does actions",
        "A way to ask for more battery",
        "A mode that turns off the screen",
        "A quiz game",
        20,
        1,
    ),
    (
        "How is an AI assistant different from a simple chatbot?",
        "It can only say hello",
        "It can take real actions (files, commands), not just chat",
        "It costs more money",
        "There is no difference",
        20,
        2,
    ),
    (
        "What is the 'heartbeat' in OpenClaw?",
        "A timer that lets the assistant act on its own (we keep it OFF in class)",
        "The sound the computer makes",
        "A health app",
        "The power button",
        20,
        1,
    ),
    (
        "How does OpenClaw remember you, even after a restart?",
        "It can't remember anything",
        "It saves notes in memory files on your computer",
        "It memorizes everything forever with no files",
        "It asks a friend",
        20,
        2,
    ),
    (
        "What is the SAFEST habit with your assistant?",
        "Share your API key with everyone",
        "Approve every command without reading it",
        "Never share your API key, and read before you approve",
        "Post your key online",
        20,
        3,
    ),
    (
        "From our whole unit, what is an AI agent really?",
        "A robot toy",
        "An LLM in a loop that uses tools and memory",
        "A single web page",
        "A type of keyboard",
        20,
        2,
    ),
    (
        "Why keep OpenClaw on 'localhost' with the gateway in the foreground during class?",
        "To make it slower",
        "To keep it on your own computer and stop it when class ends",
        "To share it with the whole internet",
        "There is no reason",
        20,
        2,
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
    output_path = os.path.join(parent_dir, "2026-06-27_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")
    print(f"[INFO] {len(QUESTIONS)} questions written.")


if __name__ == "__main__":
    main()
