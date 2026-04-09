"""
Kahoot Quiz Generator - February 7, 2026
Internet Backbones, ISPs, and How the Internet Connects Everything

Usage:
    python create_kahoot_excel.py
"""

import os
import openpyxl
from openpyxl import Workbook

# =============================================================================
# KAHOOT QUESTIONS (20 total)
# Format: (Question, Answer 1, Answer 2, Answer 3, Answer 4, Time limit, Correct Answer)
# Correct Answer = 1,2,3,4
# =============================================================================

QUESTIONS = [
    (
        "What does ISP stand for?",
        "Internet Service Provider",
        "Internet Safety Program",
        "Internal Server Protocol",
        "Instant Streaming Platform",
        20,
        1,
    ),
    (
        "Which company is an example of an ISP?",
        "Comcast",
        "YouTube",
        "Minecraft",
        "Google Docs",
        20,
        1,
    ),
    (
        "What does an ISP do for your home?",
        "Connects you to the internet",
        "Stores your photos",
        "Builds your computer",
        "Makes video games",
        20,
        1,
    ),
    (
        "What is the internet backbone?",
        "Super-fast fiber highways that carry data",
        "A password manager",
        "A phone app",
        "A type of cloud storage",
        20,
        1,
    ),
    (
        "Fiber optic cables send data using...",
        "Light",
        "Water",
        "Batteries",
        "Magnets",
        20,
        1,
    ),
    (
        "Most of the world's internet traffic travels through...",
        "Cables under the ocean",
        "Satellites only",
        "Wi-Fi towers only",
        "Bluetooth signals",
        20,
        1,
    ),
    (
        "Undersea cables connect...",
        "Continents",
        "Only nearby houses",
        "Only cell phones",
        "Only satellites",
        20,
        1,
    ),
    (
        "Why are many cable landing points near big cities?",
        "Lots of people and networks are there",
        "The water is warmer",
        "Cities have more clouds",
        "It is illegal elsewhere",
        20,
        1,
    ),
    (
        "What is an Internet Exchange Point (IXP)?",
        "A meeting place where networks swap traffic",
        "A new video game",
        "A type of router",
        "A phone tower",
        20,
        1,
    ),
    (
        "IXPs make the internet...",
        "Faster and cheaper",
        "Slower and more expensive",
        "Only for videos",
        "Only for emails",
        20,
        1,
    ),
    (
        "What does CDN stand for?",
        "Content Delivery Network",
        "Computer Data Notebook",
        "Cloud Download Network",
        "Central Device Number",
        20,
        1,
    ),
    (
        "What is the main job of a CDN?",
        "Store copies of content close to users",
        "Fix broken computers",
        "Create passwords",
        "Build new phones",
        20,
        1,
    ),
    (
        "Why do CDNs make videos load faster?",
        "They keep content nearby",
        "They make the screen bigger",
        "They turn off Wi-Fi",
        "They delete ads",
        20,
        1,
    ),
    (
        "Latency means...",
        "Delay before data arrives",
        "The size of a file",
        "A type of cable",
        "A website address",
        20,
        1,
    ),
    (
        "Which usually lowers latency?",
        "A closer server",
        "More distance",
        "Turning off the router",
        "Using older cables",
        20,
        1,
    ),
    (
        "Which is NOT a common cause of slow internet?",
        "Too much sunlight",
        "Busy Wi-Fi",
        "Long distance",
        "Server overload",
        20,
        1,
    ),
    (
        "Which is a good example of CDN content?",
        "Videos, images, and game updates",
        "Only text messages",
        "Printer ink",
        "Battery power",
        20,
        1,
    ),
    (
        "What is the first network your data usually enters?",
        "Your ISP",
        "An undersea cable",
        "A data center in another country",
        "A video game server",
        20,
        1,
    ),
    (
        "Which path is MOST accurate?",
        "Device -> Router -> ISP -> Backbone -> Server",
        "Device -> Satellite -> Printer -> Server",
        "Device -> Bluetooth -> TV -> Server",
        "Device -> USB Cable -> Server",
        20,
        1,
    ),
    (
        "Why does AI need the physical internet?",
        "AI runs in data centers and needs fast connections",
        "AI works without cables",
        "AI lives only in phones",
        "AI does not use the internet",
        20,
        1,
    ),
]

# =============================================================================
# EXCEL GENERATOR
# =============================================================================

def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Kahoot Questions"

    # Header row (Kahoot import format)
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
    output_path = os.path.join(parent_dir, "2026-02-07_Kahoot_Import.xlsx")

    wb.save(output_path)
    print(f"[SUCCESS] Kahoot import file created: {output_path}")

if __name__ == "__main__":
    main()
