"""
Kahoot Quiz Generator - May 2, 2026
How AI Agents Actually Work - Inside the Loop

Usage:
    py create_kahoot_excel.py
"""

import os
from openpyxl import Workbook

# =============================================================================
# KAHOOT QUESTIONS (15 total)
# Format: (Question, Answer 1, Answer 2, Answer 3, Answer 4, Time limit, Correct)
# Correct = 1, 2, 3, or 4
# Kahoot: question max ~120 chars, answer max ~75 chars
# =============================================================================

QUESTIONS = [
    (
        "In the agent loop Think -> Act -> Observe -> Repeat, what does 'Observe' mean?",
        "The agent watches the user typing",
        "The agent looks at the result of the action it just took",
        "The agent saves the conversation to memory",
        "The agent picks which tool to use next",
        20,
        2,
    ),
    (
        "When an AI agent uses a tool like web search, what is actually happening?",
        "The AI is downloading the whole internet",
        "The AI sends a request to another program and waits for the result",
        "The AI is guessing based on its training data",
        "The agent stops working until you click search",
        25,
        2,
    ),
    (
        "What is a 'context window'?",
        "A pop-up that shows what the AI is doing",
        "The website where you chat with AI",
        "The amount of text the AI can remember in one conversation",
        "A type of AI tool for browsing the web",
        20,
        3,
    ),
    (
        "Why does a long conversation sometimes make the AI 'forget' earlier messages?",
        "The AI gets bored",
        "The conversation goes past the context window limit",
        "The AI deletes old messages on purpose",
        "The internet connection cuts off",
        25,
        2,
    ),
    (
        "What is a 'system prompt'?",
        "An error message",
        "Hidden instructions that tell the AI how to behave",
        "The first question you ask",
        "A prompt that shuts down the AI",
        20,
        2,
    ),
    (
        "What can an AI agent do that a chatbot cannot?",
        "Speak in different languages",
        "Plan multiple steps and use tools to complete a task",
        "Type faster",
        "Remember your name",
        20,
        2,
    ),
    (
        "'Find the next Warriors game and remind me to watch it' needs which agent skills?",
        "Just memory",
        "Web search + memory + planning",
        "Image generation",
        "None - a chatbot can do this",
        25,
        2,
    ),
    (
        "What does the AI's 'reasoning' or 'thinking' output usually show?",
        "Random text",
        "The steps the AI is planning before answering",
        "The AI's training data",
        "Other users' questions",
        20,
        2,
    ),
    (
        "When an AI agent uses a tool, behind the scenes it is really:",
        "Talking to itself",
        "Sending a request over the network to another program",
        "Pausing for the user",
        "Restarting its brain",
        25,
        2,
    ),
    (
        "Why do AI agents sometimes loop forever or get stuck?",
        "They get tired",
        "Their plan failed and they keep retrying without a new approach",
        "The internet is too fast",
        "They are always perfect",
        25,
        2,
    ),
    (
        "Which task is the BEST fit for an AI agent (not just a chatbot)?",
        "What is 7 times 8?",
        "Define photosynthesis",
        "Research 3 colleges, compare tuition, and email me a summary",
        "Tell me a joke",
        25,
        3,
    ),
    (
        "True or False: An AI agent is the same thing as AGI.",
        "True - they mean the same thing",
        "False - agents use tools today; AGI is human-level and doesn't exist yet",
        "True - but only the paid versions",
        "False - AGI is just a faster agent",
        25,
        2,
    ),
    (
        "What is an AI 'hallucination'?",
        "When the AI sees pictures or images",
        "When the AI confidently makes up an answer that isn't true",
        "When the AI runs out of memory",
        "When the AI uses too many tools at once",
        20,
        2,
    ),
    (
        "In the agent loop, what is the 'Act' step?",
        "The agent talks back to the user",
        "The agent uses a tool to do something (search, send email, run code)",
        "The agent thinks about its options",
        "The agent saves its memory",
        20,
        2,
    ),
    (
        "An assistant has MEMORY but no TOOLS. Which task can it still NOT do?",
        "Remember your name from earlier in the chat",
        "Look up today's weather",
        "Write a poem about your dog",
        "Answer trivia from its training data",
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
    output_path = os.path.join(parent_dir, "2026-05-02_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")


if __name__ == "__main__":
    main()
