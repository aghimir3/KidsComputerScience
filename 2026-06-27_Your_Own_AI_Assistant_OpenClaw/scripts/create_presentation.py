"""
PowerPoint Generator for: Your Own AI Assistant (OpenClaw)
Kids Computer Science Class - June 27, 2026  (LAST DAY of the AI unit)

Uses the shared EverestIT theme in tools/create_theme.py.

Run:
    python create_presentation.py

Dependencies:
    pip install python-pptx
"""

import sys
import os

# Import the shared class theme (colors, helpers, templates)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from create_theme import *  # noqa: F401,F403  (Presentation, Inches, Pt, COLORS, helpers, ...)

# Terminal text color (soft green for a "code" feel)
TERM_GREEN = RGBColor(0x9B, 0xE3, 0x8A)
TERM_BG = RGBColor(0x12, 0x1A, 0x24)


# ---------------------------------------------------------------------------
# Local helpers
# ---------------------------------------------------------------------------

def new_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def add_lines(slide, left, top, width, height, lines,
              font_size=16, color=None, bold=False,
              alignment=PP_ALIGN.LEFT, font_name="Segoe UI",
              line_spacing=1.1):
    """Add a textbox with multiple lines (one paragraph each)."""
    if color is None:
        color = COLORS["dark_gray"]
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.bold = bold
        p.font.name = font_name
        p.alignment = alignment
        p.line_spacing = line_spacing
    return tb


def card(slide, x, y, w, h, color, title, desc,
         title_color=None, desc_color=None, title_size=18, desc_size=13):
    """Colored rounded box with a bold title and a description (str or list)."""
    add_rounded_box(slide, Inches(x), Inches(y), Inches(w), Inches(h), color)
    add_styled_textbox(
        slide, Inches(x + 0.25), Inches(y + 0.18), Inches(w - 0.5), Inches(0.5),
        title, font_size=title_size, font_color=title_color or COLORS["white"],
        bold=True
    )
    if isinstance(desc, str):
        desc = [desc]
    add_lines(
        slide, Inches(x + 0.25), Inches(y + 0.78), Inches(w - 0.5), Inches(h - 0.95),
        desc, font_size=desc_size, color=desc_color or COLORS["white"]
    )


def terminal(slide, x, y, w, h, lines, font_size=15):
    """A dark 'terminal window' box with monospace-style green text."""
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    set_shape_fill(box, TERM_BG)
    box.line.fill.background()
    add_lines(slide, Inches(x + 0.25), Inches(y + 0.18), Inches(w - 0.5), Inches(h - 0.3),
              lines, font_size=font_size, color=TERM_GREEN,
              font_name="Consolas", line_spacing=1.15)


def flow_box(slide, x, y, w, h, color, label, label_size=15):
    add_rounded_box(slide, Inches(x), Inches(y), Inches(w), Inches(h), color)
    add_lines(slide, Inches(x + 0.15), Inches(y + 0.18), Inches(w - 0.3), Inches(h - 0.3),
              [label] if isinstance(label, str) else label,
              font_size=label_size, color=COLORS["white"], bold=True,
              alignment=PP_ALIGN.CENTER, line_spacing=1.05)


def big_arrow(slide, x, y, w=0.7, h=0.7):
    add_arrow(slide, Inches(x), Inches(y), Inches(w), Inches(h), COLORS["orange"], "right")


def custom_title_slide(prs):
    """Title slide with non-overlapping text boxes (clean validator pass)."""
    s = new_slide(prs)
    add_full_bg(s, COLORS["dark_blue"])
    add_rounded_box(s, Inches(1.2), Inches(1.8), Inches(10.93), Inches(2.7),
                    COLORS["light_blue"])
    add_styled_textbox(s, Inches(0.6), Inches(2.15), Inches(12.13), Inches(1.0),
                       "Meet Your Own AI Assistant", font_size=44,
                       font_color=COLORS["dark_blue"], bold=True,
                       alignment=PP_ALIGN.CENTER, font_name="Segoe UI Semibold")
    add_styled_textbox(s, Inches(0.8), Inches(3.3), Inches(11.73), Inches(0.8),
                       "OpenClaw + OpenRouter  \u00b7  Run a real AI on your own computer",
                       font_size=20, font_color=COLORS["dark_blue"],
                       alignment=PP_ALIGN.CENTER)
    accent = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(3.0), Inches(5.2),
                                Inches(7.33), Inches(0.06))
    set_shape_fill(accent, COLORS["orange"])
    accent.line.fill.background()
    add_styled_textbox(s, Inches(2.0), Inches(5.5), Inches(9.33), Inches(0.5),
                       "Last Day of the AI Unit  \u00b7  Kids Computer Science",
                       font_size=16, font_color=COLORS["sky_blue"],
                       alignment=PP_ALIGN.CENTER)
    add_styled_textbox(s, Inches(0.6), Inches(6.5), Inches(12.13), Inches(0.4),
                       "Saturday, June 27, 2026", font_size=18,
                       font_color=COLORS["sky_blue"], alignment=PP_ALIGN.CENTER)
    return s


# ---------------------------------------------------------------------------
# Build the deck
# ---------------------------------------------------------------------------

def build(prs):
    # 1. Title
    custom_title_slide(prs)

    # 2. The journey so far (recap)
    s = new_slide(prs)
    add_title_bar(s, "How Far You've Come", "The last stop on our AI journey")
    steps = [
        ("What AI agents are", COLORS["light_blue"]),
        ("How agents think (the loop)", COLORS["medium_blue"]),
        ("Tools, MCP, Skills & Memory", COLORS["purple"]),
        ("Building your own tools", COLORS["teal"]),
        ("Today: run a REAL assistant", COLORS["orange"]),
    ]
    for i, (text, color) in enumerate(steps):
        add_agenda_item(s, i + 1, text, 1.7 + i * 0.82, color)
    add_takeaway_bar(s, "Today you run a real AI assistant on your OWN computer.",
                     COLORS["dark_blue"])

    # 3. Big idea
    s = new_slide(prs)
    add_full_bg(s, COLORS["dark_blue"])
    add_lines(
        s, Inches(1.0), Inches(2.1), Inches(11.33), Inches(2.6),
        ["What if your computer had its own assistant —",
         "one you could talk to, that remembers you",
         "and can actually DO things?"],
        font_size=32, color=COLORS["white"], bold=True,
        alignment=PP_ALIGN.CENTER, line_spacing=1.15
    )
    add_styled_textbox(
        s, Inches(1.0), Inches(5.0), Inches(11.33), Inches(0.8),
        "Today, you build one.", font_size=26, font_color=COLORS["orange"],
        bold=True, alignment=PP_ALIGN.CENTER
    )

    # 4. Meet OpenClaw
    s = new_slide(prs)
    add_title_bar(s, "Meet OpenClaw \U0001F99E", "A free, open-source AI assistant")
    card(s, 0.6, 1.7, 5.85, 1.95, COLORS["medium_blue"],
         "Runs on YOUR computer", ["It lives on your laptop, not a website.",
                                    "Your stuff stays with you."])
    card(s, 6.85, 1.7, 5.85, 1.95, COLORS["green"],
         "Free & open-source", ["Anyone can use it and see how it works.",
                                "Its mascot is a lobster. \U0001F99E"])
    card(s, 0.6, 3.85, 5.85, 1.95, COLORS["purple"],
         "Remembers you", ["It keeps notes so it knows you",
                           "next time you chat."])
    card(s, 6.85, 3.85, 5.85, 1.95, COLORS["orange"],
         "You talk in the terminal", ["Type a message, it replies —",
                                      "and it can take real actions."])
    add_takeaway_bar(s, "A real assistant that runs on your computer and works for you.",
                     COLORS["teal"])

    # 4b. What it can do (everyday)
    s = new_slide(prs)
    add_title_bar(s, "What OpenClaw Can Do", "Your everyday helper")
    caps_xs = [0.6, 4.74, 8.88]
    caps_a = [
        (COLORS["medium_blue"], "\U0001F4AC Chat & answer", "Questions, ideas, explanations"),
        (COLORS["teal"], "\U0001F4C4 Files & code", "Read, write, and edit files"),
        (COLORS["purple"], "\u26A1 Run commands", "Do real tasks (with your OK)"),
        (COLORS["green"], "\U0001F310 Browse the web", "Look things up, read pages"),
        (COLORS["orange"], "\U0001F9E0 Remember you", "Notes that last across chats"),
        (COLORS["light_blue"], "\u23F0 Reminders & tasks", "Schedule things, daily briefings"),
    ]
    for i, (color, title, desc) in enumerate(caps_a):
        x = caps_xs[i % 3]
        y = 1.7 + (i // 3) * 2.15
        card(s, x, y, 3.85, 1.9, color, title, [desc], title_size=15, desc_size=12)
    add_takeaway_bar(s, "It's not just a chatbot \u2014 it can actually get things done.",
                     COLORS["dark_blue"])

    # 4c. What it can do (bigger powers)
    s = new_slide(prs)
    add_title_bar(s, "...And Its Bigger Powers", "Even if we don't try them all today")
    caps_b = [
        (COLORS["purple"], "\U0001F4F1 Message you", "WhatsApp, Telegram, Discord"),
        (COLORS["medium_blue"], "\U0001F4E7 Email helper", "Sort & summarize your inbox"),
        (COLORS["pink"], "\U0001F3A8 Create media", "Images, audio, even video"),
        (COLORS["teal"], "\U0001F50C Add new tools", "Plug in MCP tool packs"),
        (COLORS["green"], "\U0001F4DA Learn new skills", "Reusable how-tos to follow"),
        (COLORS["orange"], "\U0001F91D Work as a team", "Spin up helper agents"),
    ]
    for i, (color, title, desc) in enumerate(caps_b):
        x = caps_xs[i % 3]
        y = 1.7 + (i // 3) * 2.15
        card(s, x, y, 3.85, 1.9, color, title, [desc], title_size=15, desc_size=12)
    add_takeaway_bar(s, "We'll try just a few today \u2014 but this is the full scope.",
                     COLORS["teal"])

    # 5. Chatbot vs Assistant
    s = new_slide(prs)
    add_title_bar(s, "Chatbot vs. Assistant", "What makes an assistant special?")
    card(s, 0.6, 1.7, 5.85, 4.1, COLORS["light_gray"], "A simple chatbot",
         ["\u2022 Waits for you to type",
          "\u2022 Text in, text out",
          "\u2022 Forgets when you close it",
          "\u2022 Lives inside a website"],
         title_color=COLORS["dark_blue"], desc_color=COLORS["dark_gray"],
         desc_size=16)
    card(s, 6.85, 1.7, 5.85, 4.1, COLORS["green"], "An AI assistant",
         ["\u2022 Takes action and does tasks",
          "\u2022 Uses files, commands, the web",
          "\u2022 Remembers you over time",
          "\u2022 Runs on your own computer"],
         desc_size=16)
    add_takeaway_bar(s, "Same chat window \u2014 but an assistant can actually DO things.",
                     COLORS["dark_blue"])

    # 6. The 4 ingredients
    s = new_slide(prs)
    add_title_bar(s, "Every Agent = 4 Ingredients",
                  "You've seen these all unit \u2014 OpenClaw has all four, for real")
    ingredients = [
        (COLORS["medium_blue"], "Model", "The brain that thinks"),
        (COLORS["teal"], "Tools", "Hands to act in the world"),
        (COLORS["purple"], "Memory", "Notes so it remembers"),
        (COLORS["orange"], "A Loop", "Repeats until done"),
    ]
    xs = [0.5, 3.62, 6.74, 9.86]
    for x, (color, title, desc) in zip(xs, ingredients):
        card(s, x, 2.1, 2.95, 2.5, color, title, [desc], desc_size=14)
    add_takeaway_bar(s, "Model + Tools + Memory + a Loop = a real agent.",
                     COLORS["dark_blue"])

    # 7. The CLI
    s = new_slide(prs)
    add_title_bar(s, "How You'll Talk to It: the Terminal")
    add_styled_textbox(s, Inches(0.8), Inches(1.55), Inches(11.7), Inches(0.5),
                       "Type. Press Enter. It replies. Type 'exit' to leave.",
                       font_size=18, font_color=COLORS["dark_gray"])
    terminal(s, 0.8, 2.15, 11.7, 3.5, [
        "$ openclaw chat",
        "You: Introduce yourself in two sentences.",
        "",
        "Clawd: Hi! I'm your AI assistant. I can read and write",
        "       files, run commands, and remember you.",
        "       What would you like to build today?",
        "You: _",
    ], font_size=15)
    add_takeaway_bar(s, "No phone, no website \u2014 just you and your assistant in the terminal.",
                     COLORS["teal"])

    # 8. The Gateway
    s = new_slide(prs)
    add_title_bar(s, "The Gateway = the Always-On Brain")
    flow_box(s, 1.0, 2.4, 4.7, 2.0, COLORS["dark_blue"],
             ["Terminal 1", "openclaw gateway", "(the brain \u2014 leave it running)"])
    big_arrow(s, 6.1, 3.05)
    flow_box(s, 7.6, 2.4, 4.7, 2.0, COLORS["green"],
             ["Terminal 2", "openclaw chat", "(where you talk to it)"])
    add_takeaway_bar(s, "One window thinks. One window talks. Close them to stop everything.",
                     COLORS["dark_blue"])

    # 9. OpenRouter
    s = new_slide(prs)
    add_title_bar(s, "OpenRouter: One Key, Many Models")
    flow_box(s, 0.6, 2.5, 3.7, 1.8, COLORS["medium_blue"],
             ["Your OpenClaw", "assistant"])
    big_arrow(s, 4.5, 3.05)
    flow_box(s, 5.3, 2.5, 2.7, 1.8, COLORS["purple"], ["OpenRouter", "(one API key)"])
    big_arrow(s, 8.2, 3.05)
    flow_box(s, 9.0, 2.5, 3.7, 1.8, COLORS["teal"],
             ["Many AI models", "DeepSeek, and more"])
    add_styled_textbox(s, Inches(0.6), Inches(4.7), Inches(12.1), Inches(0.6),
                       "Today's model: DeepSeek V4 Flash \u2014 fast and low-cost.",
                       font_size=18, font_color=COLORS["dark_gray"], bold=True,
                       alignment=PP_ALIGN.CENTER)
    add_takeaway_bar(s, "One API key unlocks lots of different AI models.",
                     COLORS["orange"])

    # 10. API key secret
    s = new_slide(prs)
    add_title_bar(s, "Your API Key Is a Secret \U0001F511")
    add_styled_textbox(s, Inches(0.8), Inches(1.65), Inches(11.7), Inches(0.7),
                       "Treat your API key like a password.",
                       font_size=24, font_color=COLORS["dark_blue"], bold=True,
                       alignment=PP_ALIGN.CENTER)
    card(s, 0.8, 2.6, 5.75, 3.0, COLORS["green"], "\u2713 DO",
         ["\u2022 Keep it private",
          "\u2022 Only use the class key",
          "\u2022 Ask the teacher if unsure"], desc_size=16)
    card(s, 6.75, 2.6, 5.75, 3.0, COLORS["red"], "\u2717 DON'T",
         ["\u2022 Share or text it to friends",
          "\u2022 Post it online",
          "\u2022 Paste it anywhere public"], desc_size=16)
    add_takeaway_bar(s, "Never share it, post it, or paste it anywhere public.",
                     COLORS["dark_blue"])

    # 11. Safety rules
    s = new_slide(prs)
    add_title_bar(s, "Safety: Rules of the Road", "OpenClaw is powerful \u2014 use it carefully")
    card(s, 0.6, 1.7, 5.85, 4.1, COLORS["green"], "\u2713 Do",
         ["\u2022 Read what it wants before approving",
          "\u2022 Keep it on localhost (your computer)",
          "\u2022 Work in a fresh folder",
          "\u2022 Stop the gateway when you're done"], desc_size=15)
    card(s, 6.85, 1.7, 5.85, 4.1, COLORS["red"], "\u2717 Don't",
         ["\u2022 Never share your API key",
          "\u2022 Don't approve commands you don't get",
          "\u2022 Don't install random skills",
          "\u2022 Don't let it touch files you care about"], desc_size=15)
    add_takeaway_bar(s, "Read before you approve \u2014 you're always in control.",
                     COLORS["dark_blue"])

    # 12. Execution approval
    s = new_slide(prs)
    add_title_bar(s, "You Approve Every Action")
    add_styled_textbox(s, Inches(0.8), Inches(1.55), Inches(11.7), Inches(0.5),
                       "When it wants to DO something, it asks first. This is 'ask' mode (the default).",
                       font_size=17, font_color=COLORS["dark_gray"])
    terminal(s, 0.8, 2.2, 11.7, 2.7, [
        "Agent wants to execute:",
        "    $ echo \"hello\" > hello.txt",
        "",
        "    [ approve ]     [ deny ]",
    ], font_size=16)
    add_styled_textbox(s, Inches(0.8), Inches(5.1), Inches(11.7), Inches(0.6),
                       "Read it. If you understand it and it's safe \u2014 approve. If not \u2014 deny and ask.",
                       font_size=16, font_color=COLORS["dark_gray"], bold=True)
    add_takeaway_bar(s, "You are always in control of what your assistant does.",
                     COLORS["teal"])

    # 13. Memory
    s = new_slide(prs)
    add_title_bar(s, "It Remembers You")
    flow_box(s, 0.6, 2.5, 3.7, 1.8, COLORS["medium_blue"],
             ["You tell it a fact", "\"My team is the Sharks\""])
    big_arrow(s, 4.5, 3.05)
    flow_box(s, 5.3, 2.5, 2.7, 1.8, COLORS["purple"], ["It saves it", "to a memory file"])
    big_arrow(s, 8.2, 3.05)
    flow_box(s, 9.0, 2.5, 3.7, 1.8, COLORS["teal"],
             ["Next time", "it still knows you"])
    add_takeaway_bar(s, "Memory = notes the assistant keeps on your computer.",
                     COLORS["dark_blue"])

    # 14. Heartbeat
    s = new_slide(prs)
    add_title_bar(s, "The Heartbeat: Acting On Its Own")
    add_styled_textbox(s, Inches(0.8), Inches(1.6), Inches(11.7), Inches(0.6),
                       "A real assistant can check things and act on a timer \u2014 even without being asked.",
                       font_size=17, font_color=COLORS["dark_gray"])
    card(s, 0.8, 2.4, 5.75, 2.9, COLORS["medium_blue"], "Heartbeat ON",
         ["Proactive 24/7.", "Checks tasks every 30 min", "and acts on its own."], desc_size=15)
    card(s, 6.75, 2.4, 5.75, 2.9, COLORS["orange"], "Heartbeat OFF (class)",
         ["Acts only when you ask.", "Keeps things safe and", "saves our credits."], desc_size=15)
    add_takeaway_bar(s, "In class we keep the heartbeat OFF \u2014 it acts only when you chat.",
                     COLORS["dark_blue"])

    # 15. Today's missions
    s = new_slide(prs)
    add_title_bar(s, "Your Turn \u2014 Today's Missions", "Work in groups \u2014 rotate the Driver!")
    missions = [
        ("A", "First Contact \u2014 meet your assistant", COLORS["light_blue"]),
        ("B", "Watch It Act \u2014 approve a real task", COLORS["medium_blue"]),
        ("C", "Give It a Personality \u2014 name it", COLORS["purple"]),
        ("D", "Make It Remember \u2014 save a fact", COLORS["teal"]),
        ("E", "Interview It \u2014 ask how it works", COLORS["green"]),
        ("F", "Quick Quests \u2014 build & create", COLORS["orange"]),
    ]
    for i, (letter, text, color) in enumerate(missions):
        y = 1.7 + i * 0.72
        add_circle(s, Inches(1.0), Inches(y), Inches(0.5), color, text=letter, text_size=20)
        add_styled_textbox(s, Inches(1.9), Inches(y + 0.05), Inches(10.6), Inches(0.5),
                           text, font_size=19, font_color=COLORS["dark_gray"])

    # 16. Big picture / AI connection
    s = new_slide(prs)
    add_title_bar(s, "A New Way to Use Computers", "Where AI is going")
    add_lines(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(2.4),
              ["Instead of clicking through menus, people are starting to just",
               "ASK their computer to do things \u2014 and an assistant does them.",
               "",
               "These assistants are built from the same ideas you learned:",
               "LLMs, tools, memory, and loops."],
              font_size=19, color=COLORS["dark_gray"], line_spacing=1.2)
    add_takeaway_bar(s, "They're written in languages like Python \u2014 which we start in July!",
                     COLORS["teal"])

    # 17. Finale recap
    s = new_slide(prs)
    add_full_bg(s, COLORS["dark_blue"])
    add_styled_textbox(s, Inches(0.8), Inches(1.5), Inches(11.7), Inches(1.0),
                       "How Far You've Come \U0001F389", font_size=44,
                       font_color=COLORS["white"], bold=True, alignment=PP_ALIGN.CENTER)
    add_lines(s, Inches(1.2), Inches(3.0), Inches(10.9), Inches(2.6),
              ["From \"what is an AI agent?\"",
               "to running your very own assistant on your computer.",
               "",
               "You used it, you understood it, and you stayed safe doing it."],
              font_size=22, color=COLORS["sky_blue"], alignment=PP_ALIGN.CENTER,
              line_spacing=1.2)

    # 18. Celebration + what's next
    s = new_slide(prs)
    add_title_bar(s, "Congratulations! \U0001F389", "You finished the AI unit")
    card(s, 0.6, 1.7, 3.95, 2.5, COLORS["medium_blue"], "You can explain",
         ["what AI agents", "really are."], desc_size=15)
    card(s, 4.7, 1.7, 3.95, 2.5, COLORS["purple"], "You built",
         ["your own AI", "tools."], desc_size=15)
    card(s, 8.8, 1.7, 3.95, 2.5, COLORS["green"], "You ran",
         ["a real AI", "assistant."], desc_size=15)
    add_styled_textbox(s, Inches(0.8), Inches(4.5), Inches(11.7), Inches(1.0),
                       "Next: Python programming starts in July \u2014 now you'll learn to BUILD the tech you've been using.",
                       font_size=18, font_color=COLORS["dark_gray"], bold=True,
                       alignment=PP_ALIGN.CENTER)
    add_takeaway_bar(s, "You're not just using AI \u2014 you're on your way to building it.",
                     COLORS["orange"])

    # 19. Questions
    create_questions_slide(prs, "Ask away \u2014 then it's Kahoot time! \U0001F99E")


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    build(prs)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_path = os.path.join(parent_dir, "2026-06-27_Your_AI_Assistant_OpenClaw.pptx")
    prs.save(output_path)
    print(f"[SUCCESS] Presentation created: {output_path}")
    print(f"[INFO] {len(prs.slides._sldIdLst)} slides.")


if __name__ == "__main__":
    main()
