"""
Kahoot Quiz Generator - April 11, 2026
Prompt Engineering & Using AI Tools

Usage:
    python create_kahoot_excel.py
"""

import os
from openpyxl import Workbook

# =============================================================================
# KAHOOT QUESTIONS (12 total)
# Format: (Question, Answer 1, Answer 2, Answer 3, Answer 4, Time limit, Correct Answer)
# Correct Answer = 1,2,3,4
# =============================================================================

QUESTIONS = [
    (
        "What is a 'prompt' in AI?",
        "A type of AI model",
        "The text instruction you give to an AI",
        "An AI's memory",
        "A programming language",
        20,
        2,
    ),
    (
        "What does the 'R' in the RTCF framework stand for?",
        "Response",
        "Result",
        "Role",
        "Repeat",
        20,
        3,
    ),
    (
        "Which prompt is MORE specific and better?",
        "'Tell me about dogs'",
        "'Write a short paragraph about why golden retrievers are great family pets'",
        "'Dogs please'",
        "'Information about animals'",
        30,
        2,
    ),
    (
        "What is an AI 'hallucination'?",
        "When AI shuts down unexpectedly",
        "When AI generates false information confidently",
        "When AI asks you a question",
        "When AI runs out of memory",
        20,
        2,
    ),
    (
        "What does 'chain-of-thought' prompting mean?",
        "Asking AI to write a story",
        "Connecting multiple AI tools together",
        "Asking AI to explain its reasoning step by step",
        "Typing really fast",
        20,
        3,
    ),
    (
        "Which of these is SAFE to share with an AI chatbot?",
        "Your home address",
        "Your password",
        "A math problem you need help with",
        "Your Social Security number",
        20,
        3,
    ),
    (
        "What is 'few-shot' prompting?",
        "Using AI for only a few minutes",
        "Giving the AI a few examples before your question",
        "Asking the AI a few questions",
        "Using a few different AI tools",
        20,
        2,
    ),
    (
        "What should you ALWAYS do after getting important information from AI?",
        "Share it on social media immediately",
        "Trust it completely -- AI is always right",
        "Fact-check it with a reliable source",
        "Delete it and try again",
        20,
        3,
    ),
    (
        "Which prompt uses the RTCF framework correctly?",
        "'Help me with homework'",
        "'You are a tutor. Explain photosynthesis to an 8th grader. Use 3 bullets.'",
        "'Photosynthesis'",
        "'I need to learn'",
        30,
        2,
    ),
    (
        "What does the 'F' in RTCF stand for?",
        "Function",
        "Fast",
        "Format",
        "Feedback",
        20,
        3,
    ),
    (
        "A student copies an entire AI essay and turns it in as their own. This is...",
        "A great study strategy",
        "Totally fine if the AI wrote it well",
        "Academic dishonesty -- not okay!",
        "The best way to learn",
        20,
        3,
    ),
    (
        "Adding 'think step by step' to a math prompt usually makes AI...",
        "Slower but less accurate",
        "More accurate because it shows its work",
        "Confused and unable to answer",
        "Give shorter answers",
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
    output_path = os.path.join(parent_dir, "2026-04-11_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")

if __name__ == "__main__":
    main()
