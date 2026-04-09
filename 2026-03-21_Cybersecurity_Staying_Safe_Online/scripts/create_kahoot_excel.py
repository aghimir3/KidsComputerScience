"""
Kahoot Quiz Generator - March 21, 2026
Cybersecurity & Staying Safe Online

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
        "What does 'cybersecurity' mean?",
        "Making computers run faster",
        "Protecting computers, networks, and data from threats",
        "Building websites",
        "Installing antivirus software only",
        20,
        2,
    ),
    (
        "Which of these is a STRONG password?",
        "password123",
        "123456",
        "PurpleTiger$Eats42Tacos!",
        "fluffy",
        20,
        3,
    ),
    (
        "What is phishing?",
        "A type of outdoor sport",
        "A computer programming language",
        "Fake emails or messages that try to steal your information",
        "A way to speed up your internet",
        20,
        3,
    ),
    (
        "Which is a red flag in a suspicious email?",
        "It comes from a known company",
        "It creates urgency: 'Act NOW or your account is deleted!'",
        "It has your real name in it",
        "It has no links",
        20,
        2,
    ),
    (
        "What does 2FA stand for?",
        "Two-File Authentication",
        "Two-Finger Access",
        "Two-Firewall Activation",
        "Two-Factor Authentication",
        20,
        4,
    ),
    (
        "What does the 'S' in HTTPS stand for?",
        "Super",
        "Secure",
        "Server",
        "Speed",
        20,
        2,
    ),
    (
        "What is social engineering?",
        "Building social media apps",
        "Tricking people into giving up confidential information",
        "A type of computer virus",
        "Engineering robots to be social",
        20,
        2,
    ),
    (
        "A website URL is 'http://faceb00k-login.com'. Is this safe?",
        "Yes -- it looks like Facebook",
        "Yes -- it starts with http",
        "No -- the URL is suspicious (0's instead of o's, wrong domain)",
        "No -- Facebook doesn't have a login page",
        20,
        3,
    ),
    (
        "How long would it take to crack the password '123456'?",
        "10 years",
        "1 hour",
        "Instantly",
        "1 week",
        20,
        3,
    ),
    (
        "What is a 'digital footprint'?",
        "A footprint made by a robot",
        "The trail of data you leave behind on the internet",
        "A digital drawing of your foot",
        "Your computer's shoe size",
        20,
        2,
    ),
    (
        "You find a USB drive labeled 'Exam Answers' in the hallway. What should you do?",
        "Plug it in to see what's on it",
        "Give it to a friend",
        "Don't plug it in -- give it to a teacher or throw it away",
        "Post about it on social media",
        20,
        3,
    ),
    (
        "Why should you use a DIFFERENT password for each account?",
        "It's more fun that way",
        "If one account gets hacked, the others stay safe",
        "Websites require it by law",
        "It makes your computer faster",
        20,
        2,
    ),
    (
        "What is a 'deepfake'?",
        "A really deep website",
        "An AI-generated video or audio that looks/sounds like a real person",
        "A type of computer virus",
        "A fake password",
        20,
        2,
    ),
    (
        "How does AI make phishing emails MORE dangerous?",
        "AI sends more emails",
        "AI makes emails load faster",
        "AI writes emails with perfect grammar, making them harder to spot",
        "AI deletes your spam folder",
        20,
        3,
    ),
    (
        "Which of these is a REAL way AI helps protect you online?",
        "AI makes your Wi-Fi faster",
        "AI filters spam and phishing from your email inbox",
        "AI creates stronger passwords by itself",
        "AI turns off your computer when hackers attack",
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
    output_path = os.path.join(parent_dir, "2026-03-21_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")

if __name__ == "__main__":
    main()
