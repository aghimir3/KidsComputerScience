"""
Kahoot Quiz Generator - April 18, 2026
Meta Prompting & AI Team Challenge

Usage:
    python create_kahoot_excel.py
"""

import os
from openpyxl import Workbook

# =============================================================================
# KAHOOT QUESTIONS (16 total)
# Format: (Question, Answer 1, Answer 2, Answer 3, Answer 4, Time limit, Correct Answer)
# Correct Answer = 1,2,3,4
# =============================================================================

QUESTIONS = [
    # Week 1 concepts (4 questions)
    (
        "What does LLM stand for?",
        "Large Language Model",
        "Long Learning Machine",
        "Local Logic Module",
        "Language Learning Method",
        20,
        1,
    ),
    (
        "What year was the Transformer architecture invented?",
        "2012",
        "2015",
        "2017",
        "2020",
        20,
        3,
    ),
    (
        "What is an AI agent?",
        "A human who works with AI",
        "AI that can plan, use tools, and take actions",
        "A type of programming language",
        "A robot that looks like a human",
        20,
        2,
    ),
    (
        "How do LLMs generate text?",
        "They copy from the internet",
        "They predict the most likely next word",
        "They read your mind",
        "They use a dictionary to find answers",
        20,
        2,
    ),
    # Week 2 concepts (5 questions)
    (
        "What does RTCF stand for?",
        "Read, Type, Check, Finish",
        "Role, Task, Context, Format",
        "Response, Time, Code, Function",
        "Repeat, Test, Create, Fix",
        20,
        2,
    ),
    (
        "What is an AI hallucination?",
        "When AI shuts down unexpectedly",
        "When AI starts talking to itself",
        "When AI generates false info confidently",
        "When AI runs out of memory",
        20,
        3,
    ),
    (
        "What prompting technique asks AI to 'think step by step'?",
        "Zero-shot",
        "Few-shot",
        "Meta prompting",
        "Chain-of-thought",
        20,
        4,
    ),
    (
        "Which is SAFE to share with an AI chatbot?",
        "Your home address",
        "Your password",
        "A homework question you need help with",
        "Your Social Security number",
        20,
        3,
    ),
    (
        "What is 'few-shot' prompting?",
        "Using AI for only a few minutes",
        "Giving AI a few examples before your question",
        "Asking the AI a few questions",
        "Using a few different AI tools",
        20,
        2,
    ),
    # Week 3 concepts (7 questions)
    (
        "What is meta prompting?",
        "Prompting without a keyboard",
        "Using AI to help you write better prompts",
        "A type of coding language",
        "Asking AI to delete your prompts",
        20,
        2,
    ),
    (
        "Which is a meta prompting technique?",
        "Asking AI to shut down",
        "Asking AI to improve your prompt",
        "Typing your prompt in ALL CAPS",
        "Sending the same prompt 10 times",
        20,
        2,
    ),
    (
        "Which meta prompting technique asks: 'What should I ask you about this topic?'",
        "Ask AI to write your prompt",
        "Ask AI to improve your prompt",
        "Ask AI what questions to ask",
        "Ask AI to fact-check itself",
        25,
        3,
    ),
    (
        "Why is iterating on prompts important?",
        "AI only works on the 3rd try",
        "It wastes time on purpose",
        "Each version usually gets better results",
        "Teachers require exactly 3 attempts",
        20,
        3,
    ),
    (
        "When comparing AI tools (ChatGPT, Gemini, Grok), what should you notice?",
        "They all give identical answers",
        "Only one tool ever gives correct answers",
        "Different tools may give different results",
        "Free tools never give good answers",
        25,
        3,
    ),
    (
        "What's the BEST first step when you're stuck on what to ask AI?",
        "Give up and Google it instead",
        "Type random words and hope for the best",
        "Use meta prompting to ask AI for help",
        "Copy someone else's prompt",
        25,
        3,
    ),
    (
        "You want to study for a biology test. What's a good meta prompt?",
        "'Help me study'",
        "'Write the best prompt to help me study for my 8th grade biology test on cells'",
        "'Biology'",
        "'Do my homework for me'",
        30,
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
    output_path = os.path.join(parent_dir, "2026-04-18_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")

if __name__ == "__main__":
    main()
