"""
Kahoot Quiz Generator - May 16, 2026
April Review — Cumulative Quiz (35 Questions)

Covers all April-May topics: GenAI basics, prompting/RTCF,
meta prompting, AI agents, agent loop, LLM internals, AI safety/ethics.

Usage:
    py create_kahoot_excel.py
"""

import os
from openpyxl import Workbook

# =============================================================================
# KAHOOT QUESTIONS (35 total — ~5 per major topic)
# Format: (Question, Answer 1, Answer 2, Answer 3, Answer 4, Time limit, Correct)
# Correct = 1, 2, 3, or 4
# Kahoot: question max ~120 chars, answer max ~75 chars
# =============================================================================

QUESTIONS = [
    # =========================================================================
    # TOPIC 1: Generative AI & LLM Basics (5 questions)
    # =========================================================================
    (
        "What does LLM stand for?",
        "Large Language Model",
        "Learning Logic Machine",
        "Live Learning Module",
        "Language Lookup Manager",
        20,
        1,
    ),
    (
        "What type of AI do we have TODAY — designed for specific tasks like chess or Siri?",
        "AGI (General AI)",
        "ASI (Super AI)",
        "ANI (Narrow AI)",
        "ABI (Broad AI)",
        20,
        3,
    ),
    (
        "What groundbreaking architecture was introduced in 2017 that powers modern LLMs?",
        "Neural Network",
        "Transformer",
        "Calculator",
        "Search Engine",
        20,
        2,
    ),
    (
        "How many parameters does GPT-3 have?",
        "1 million",
        "10 billion",
        "175 billion",
        "1 trillion",
        20,
        3,
    ),
    (
        "What is the CORE process LLMs use to generate text?",
        "Looking up answers in a database",
        "Next-token prediction",
        "Copying from the internet",
        "Random word selection",
        20,
        2,
    ),

    # =========================================================================
    # TOPIC 2: Prompting & RTCF (5 questions)
    # =========================================================================
    (
        "What does R.T.C.F. stand for in prompt engineering?",
        "Read, Type, Check, Finish",
        "Role, Task, Context, Format",
        "Run, Test, Code, Fix",
        "Research, Think, Create, Format",
        20,
        2,
    ),
    (
        "Which prompting technique asks the AI to 'think step by step'?",
        "Zero-shot",
        "Few-shot",
        "Chain-of-thought",
        "Meta prompting",
        20,
        3,
    ),
    (
        "In RTCF, what does the 'R' (Role) do?",
        "Tells the AI how long the answer should be",
        "Tells the AI WHO it should act as",
        "Tells the AI to repeat the question",
        "Tells the AI to restart",
        20,
        2,
    ),
    (
        "What is 'few-shot' prompting?",
        "Asking the AI only one question",
        "Giving the AI a few examples so it learns the pattern",
        "Shooting a basketball while prompting",
        "Deleting the AI's memory",
        20,
        2,
    ),
    (
        "Which prompt is BETTER?",
        "Tell me about dogs",
        "Write an essay",
        "Explain the top 3 dog breeds for families, including size and temperament",
        "Help me",
        25,
        3,
    ),

    # =========================================================================
    # TOPIC 3: Meta Prompting (5 questions)
    # =========================================================================
    (
        "What is META prompting?",
        "Deleting a prompt and starting over",
        "Using AI to help you write or improve your prompts",
        "Typing the longest prompt possible",
        "Asking the AI to ignore your prompt",
        20,
        2,
    ),
    (
        "What does 'iteration' mean when working with AI prompts?",
        "Asking the same question many times and hoping for luck",
        "Improving a prompt step by step based on the AI's response",
        "Giving up after the first try",
        "Copying someone else's prompt",
        25,
        2,
    ),
    (
        "Which is a good example of a meta prompt?",
        "What is 2 + 2?",
        "How can I improve this prompt to get a better study guide?",
        "Tell me a joke",
        "Write code",
        20,
        2,
    ),
    (
        "Why should you fact-check AI responses?",
        "AI always lies on purpose",
        "AI can hallucinate — give confident but wrong answers",
        "AI only works on weekends",
        "Fact-checking is not needed",
        20,
        2,
    ),
    (
        "When comparing AI tools like ChatGPT, Gemini, and Grok, what should you keep the same?",
        "The time of day you ask",
        "The exact prompt you use",
        "The color of your screen",
        "Nothing — just compare random results",
        20,
        2,
    ),

    # =========================================================================
    # TOPIC 4: AI Agents (5 questions)
    # =========================================================================
    (
        "What can an AI agent do that a regular chatbot CANNOT?",
        "Answer a single question",
        "Plan multiple steps and use tools to complete a task",
        "Speak in English",
        "Display text on screen",
        20,
        2,
    ),
    (
        "What are the 4 core components of an AI agent?",
        "Screen, keyboard, mouse, speaker",
        "LLM + tools + memory + planning",
        "Google + YouTube + email + camera",
        "CPU + RAM + disk + GPU",
        25,
        2,
    ),
    (
        "What is a 'system prompt'?",
        "The first thing the user types",
        "An error message from the AI",
        "Hidden instructions that tell the AI how to behave",
        "The AI's login password",
        20,
        3,
    ),
    (
        "Which task NEEDS an AI agent (not just a chatbot)?",
        "What is the capital of France?",
        "Tell me a joke",
        "Research 3 colleges, compare tuition, and email me a summary",
        "Define the word 'happy'",
        25,
        3,
    ),
    (
        "True or False: An AI agent is the same thing as AGI.",
        "True — they are the same thing",
        "False — agents use tools today; AGI doesn't exist yet",
        "True — but only paid versions",
        "False — AGI is just a faster chatbot",
        25,
        2,
    ),

    # =========================================================================
    # TOPIC 5: Agent Loop — Think / Act / Observe (5 questions)
    # =========================================================================
    (
        "What are the 3 steps of the agent loop?",
        "Read, Write, Delete",
        "Think, Act, Observe",
        "Ask, Wait, Repeat",
        "Copy, Paste, Save",
        20,
        2,
    ),
    (
        "In the agent loop, what does 'Observe' mean?",
        "The agent watches the user typing",
        "The agent looks at the result of the action it just took",
        "The agent shuts down",
        "The agent picks a new LLM",
        20,
        2,
    ),
    (
        "When an AI agent uses a tool like web search, what actually happens?",
        "The AI downloads the whole internet",
        "The AI sends a request to another program and waits for a result",
        "The AI guesses based on training data",
        "Nothing — it just pretends to search",
        25,
        2,
    ),
    (
        "Why might an AI agent loop (Think -> Act -> Observe) MULTIPLE times?",
        "It enjoys repeating itself",
        "The task needs several steps to complete",
        "It is broken and stuck",
        "The user pressed the repeat button",
        20,
        2,
    ),
    (
        "An agent has memory but NO tools. Which task can it still NOT do?",
        "Remember your name from earlier in the chat",
        "Look up today's weather from the internet",
        "Write a poem about your dog",
        "Answer trivia from its training data",
        25,
        2,
    ),

    # =========================================================================
    # TOPIC 6: LLM Internals (5 questions)
    # =========================================================================
    (
        "What is a 'token' in AI?",
        "A physical coin the AI collects",
        "A small chunk of text like a word, word-piece, or punctuation",
        "The AI's password",
        "A type of computer virus",
        20,
        2,
    ),
    (
        "What does 'temperature' control in an LLM?",
        "How fast the computer runs",
        "How creative vs. predictable the AI's answers are",
        "The color of the text",
        "How long the AI thinks",
        20,
        2,
    ),
    (
        "What is 'attention' in a Transformer model?",
        "How much the AI likes your question",
        "A mechanism that helps the model focus on important earlier tokens",
        "A timer that counts how long you wait",
        "The AI paying attention to your camera",
        20,
        2,
    ),
    (
        "What is a 'context window'?",
        "A pop-up ad on the screen",
        "The amount of text the AI can hold in memory during one conversation",
        "A window in the AI's office",
        "The AI's screen resolution",
        20,
        2,
    ),
    (
        "What is an AI 'hallucination'?",
        "When the AI sees pictures",
        "When the AI confidently makes up something that is not true",
        "When the AI runs out of battery",
        "When the AI has a dream",
        20,
        2,
    ),

    # =========================================================================
    # TOPIC 7: AI Safety & Ethics (5 questions)
    # =========================================================================
    (
        "What should you ALWAYS do before trusting an important AI answer?",
        "Ask the AI if it is sure",
        "Fact-check it using a reliable source",
        "Just trust it — AI is always right",
        "Delete the answer and ask again",
        20,
        2,
    ),
    (
        "Which of these is something you should NOT share with an AI chatbot?",
        "A homework question",
        "A coding problem",
        "Your home address and passwords",
        "A creative writing topic",
        20,
        3,
    ),
    (
        "What is RLHF?",
        "Really Large Helpful Files",
        "Reinforcement Learning from Human Feedback — humans rate AI outputs to improve them",
        "Remote Language Hardware Function",
        "Randomly Loaded Hidden Features",
        25,
        2,
    ),
    (
        "When you use AI to help with a school assignment, you should:",
        "Copy the AI's answer exactly and claim it as yours",
        "Never tell anyone you used AI",
        "Tell your teacher you used AI and explain how",
        "Only use AI if no one is watching",
        20,
        3,
    ),
    (
        "Why is it important that AI training data comes from many sources?",
        "To make the download bigger",
        "To help reduce bias and give more balanced answers",
        "Because one source would be too cheap",
        "Training data does not matter at all",
        25,
        2,
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

    for q in QUESTIONS:
        ws.append(list(q))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-05-16_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")
    print(f"Total questions: {len(QUESTIONS)}")


if __name__ == "__main__":
    main()
