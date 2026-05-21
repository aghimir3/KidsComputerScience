"""
Kahoot Quiz Generator - May 23, 2026
AI Image & Multimodal Models

Usage:
    py create_kahoot_excel.py
"""

import os
from openpyxl import Workbook

# =============================================================================
# KAHOOT QUESTIONS (15 total)
# Format: (Question, Answer 1, Answer 2, Answer 3, Answer 4, Time limit, Correct)
# Correct = 1, 2, 3, or 4
# =============================================================================

QUESTIONS = [
    (
        "What does a text-to-image model do?",
        "Converts pictures into text descriptions",
        "Creates images from text descriptions you type",
        "Searches Google Images for matching photos",
        "Scans physical drawings into digital files",
        20,
        2,
    ),
    (
        "Which of these is a text-to-image AI model?",
        "ChatGPT (text only mode)",
        "DALL-E 3",
        "Google Docs",
        "Microsoft Word",
        20,
        2,
    ),
    (
        "How does diffusion create an image?",
        "It copies images from the internet",
        "It takes a screenshot of a video",
        "It starts with random noise and removes it step by step",
        "It downloads photos from a database",
        25,
        3,
    ),
    (
        "What is 'multimodal' AI?",
        "AI that only works with text",
        "AI that can understand and generate multiple types of data (text, images, audio)",
        "AI that works on multiple computers at once",
        "AI that speaks multiple languages",
        25,
        2,
    ),
    (
        "Which is a BETTER image prompt?",
        "Make a dog",
        "A golden retriever in a sunflower field, watercolor style, warm sunset lighting",
        "Dog picture please",
        "Image of animal",
        20,
        2,
    ),
    (
        "What should you include in a great image prompt?",
        "Just the subject (e.g., 'cat')",
        "Subject, style, lighting, and mood",
        "Only the colors you want",
        "Your personal information",
        20,
        2,
    ),
    (
        "What is a deepfake?",
        "A very realistic photograph taken with an expensive camera",
        "AI-generated fake image or video of a real person",
        "A blurry photo that looks deep",
        "A type of social media filter",
        20,
        2,
    ),
    (
        "True or False: AI image models COPY real images from the internet.",
        "True — they just find and copy matching images",
        "False — they generate new images from learned patterns",
        "True — but they change the colors first",
        "False — they use a camera",
        25,
        2,
    ),
    (
        "What is one way to spot an AI-generated image?",
        "It's always black and white",
        "Look for weird hands, extra fingers, or garbled text",
        "AI images are always blurry",
        "AI images have a watermark that says 'AI' in the corner",
        20,
        2,
    ),
    (
        "What does GPT-4o's multimodal ability let you do?",
        "Only type text questions",
        "Upload a photo and ask questions about it",
        "Print images from your phone",
        "Video call with the AI",
        20,
        2,
    ),
    (
        "Why is it dangerous to create fake images of real people?",
        "It uses too much electricity",
        "It can harm their reputation, spread lies, or be used for bullying",
        "The images might be ugly",
        "It's not dangerous at all",
        25,
        2,
    ),
    (
        "A sculptor chipping away marble is an analogy for which AI process?",
        "Tokenization",
        "Diffusion (removing noise to reveal an image)",
        "Attention mechanism",
        "Next-token prediction",
        25,
        2,
    ),
    (
        "Which AI can LOOK at a photo and tell you what's in it?",
        "A text-only LLM",
        "A text-to-image model like DALL-E",
        "A multimodal AI like GPT-4o or Gemini",
        "A search engine",
        20,
        3,
    ),
    (
        "If you see a shocking news photo online, what should you do FIRST?",
        "Share it immediately before it gets deleted",
        "Check the source and try to verify if it's real",
        "Assume it's real because it looks convincing",
        "Delete it from your phone",
        25,
        2,
    ),
    (
        "How does prompting for images DIFFER from prompting for text?",
        "Image prompts don't need any detail",
        "Image prompts describe visual elements: style, lighting, mood, composition",
        "There is no difference at all",
        "Image prompts must be in a foreign language",
        20,
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
    output_path = os.path.join(parent_dir, "2026-05-23_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")
    print(f"Total questions: {len(QUESTIONS)}")


if __name__ == "__main__":
    main()
