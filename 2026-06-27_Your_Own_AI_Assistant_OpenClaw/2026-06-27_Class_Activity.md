# Class Activity — Your Own AI Assistant (OpenClaw)
**Date:** Saturday, 2026-06-27 · 9:00 AM – 1:00 PM Pacific
**The LAST class of the AI unit — let's end with a bang! 🦞**

Today every student installs and runs a **real, full-power AI assistant** (OpenClaw) on their own laptop, connects it to a real model (**DeepSeek V4 Flash** via **OpenRouter**), and talks to it right in the terminal. We finish by celebrating how far the class has come this AI unit.

---

## Goals for the day

By the end, students can:
- Explain what a personal AI assistant is and how it's different from a chatbot
- Install OpenClaw and connect it to OpenRouter
- Chat with their assistant from the terminal (`openclaw chat`)
- Use it **safely**: approve every action, keep the key secret, stay on localhost
- Connect today's tool to the big picture of the whole AI unit

---

## Before class (teacher)

- Read and follow **`2026-06-27_OpenClaw_Setup_Guide.md`** end-to-end on a test laptop.
- Preload ~**$10** on OpenRouter and create **one API key per group**. Share keys privately.
- Ask students to **pre-install Node.js 22.19+ and run `npm install -g openclaw` before class** if possible — it saves lots of setup time.
- Decide groups (3–4 students). Each group needs at least one Mac/Windows laptop that can install software.

---

## Sample timeline (flex as needed)

| Time | Activity |
|------|----------|
| 9:00 – 9:15 | **Opening + recap of the journey.** It's the last AI class — recap what an agent is (an LLM in a loop with tools + memory). |
| 9:15 – 9:40 | **Concept intro (slides).** Chatbot vs assistant, the 4 ingredients, the CLI, the Gateway, OpenRouter, API-key safety, execution approval. |
| 9:40 – 10:15 | **Setup walkthrough (everyone together).** Node → OpenClaw → onboard with OpenRouter → set DeepSeek → start the gateway → first `openclaw chat`. |
| 10:15 – 10:30 | **Mission A + B** (first contact + watch it act). |
| 10:30 – 11:00 | **BREAK** (fixed) |
| 11:00 – 11:30 | **Typing Practice** (fixed) |
| 11:30 – 12:15 | **Missions C–F** (personality, memory, interview, quick quests). |
| 12:15 – 12:35 | **Celebration: "How far you've come"** recap + group share-outs. |
| 12:35 – 12:50 | **Kahoot** (15 questions). |
| 12:50 – 1:00 | **Homework explanation + goodbye.** What's next: Python programming starts in July! |

> **Roles:** Each group picks a **Driver** (shares screen / types). **Rotate the Driver every mission** so everyone gets a turn.

---

## Guided setup (teacher-led, ~35 min)

Do this together, step by step, pausing so groups can catch up. Full details are in the setup guide.

1. **Check Node:** `node --version` (need 22.19+; install Node 24 if older).
2. **Install OpenClaw:** `npm install -g openclaw`, then `openclaw --version`.
3. **Onboard:** `openclaw onboard` → choose **OpenRouter** → paste the **group's class key** → **Skip** messaging channels.
4. **Pick the model:** `openclaw models set openrouter/deepseek/deepseek-v4-flash`.
5. **Start the Gateway (Terminal 1):** `openclaw gateway` — leave it running.
6. **Chat (Terminal 2):** `openclaw chat` → say hello.
7. **Practice approval:** ask it to make a file; show the **[approve] / [deny]** prompt and read it together before approving.

> **Checkpoint:** Every group should get a reply in `openclaw chat` before moving on. Help groups who are stuck — pair laptops if needed.

---

## Live group activity — "Interview Your Assistant" (~10 min)

Have each group ask their assistant these questions out loud and compare answers:

- *"In two sentences, what are you and what can you help me with?"*
- *"How do you remember things about me between conversations?"*
- *"What is an API key, and why should I keep it secret?"*
- *"Before you run a command on my computer, what do you do first?"*

Then discuss as a class: **the assistant can describe its own model, memory, and safety rules — because those were built into it.** Asking the agent is a real way developers learn a new tool!

---

## AI discussion point (whole class)

> **"Should everyone have a personal AI assistant that can use their files, run commands, and message them? What's amazing about it — and what could go wrong?"**

Guide students toward:
- **Amazing:** it can actually *do* things, remember you, and work across your apps.
- **Risks:** it has real power on your computer, so you must approve actions, keep keys secret, and not run code you don't understand. (This is exactly why OpenClaw asks before acting.)

---

## 🎉 Celebration: How Far You've Come (~20 min)

It's the last day of the AI unit — take time to celebrate!

**1. Walk the timeline together** (put it on screen):
- Intro to AI Agents → How Agents Work → LLM Internals → Building with AI → Mission Control → Using Tools, MCP, Skills & Memory → **Building Your Own Tools** → **Running a Real Assistant (today!)**

**2. Group share-outs.** Each group shares:
- The **coolest thing** their assistant did today.
- One thing they **understand now** that they didn't 3 months ago.
- What they would **build or automate** if they had an assistant at home.

**3. "I can now..." round.** Go around the room; each student finishes the sentence *"I can now ___"* (e.g., "explain what an AI agent is," "run a real AI assistant," "build my own tool").

**4. Certificates / shout-outs (optional).** Recognize each student for completing the AI unit. A simple "AI Explorer — Completed the AI Unit" certificate or a class shout-out works great.

**5. What's next.** In July we begin **Python programming** — and now you understand the AI tools that are built *with* Python. You're not just using AI; you're on your way to building it.

---

## Materials checklist

- [ ] `2026-06-27_OpenClaw_Setup_Guide.md` shared with students
- [ ] OpenRouter keys created (one per group) and shared privately
- [ ] `2026-06-27_Your_AI_Assistant_OpenClaw.pptx` ready to present
- [ ] `2026-06-27_Classwork_Your_AI_Assistant.pdf` printed/shared
- [ ] `2026-06-27_Homework_Your_AI_Assistant.pdf` shared
- [ ] `2026-06-27_Kahoot_Import.xlsx` uploaded to Kahoot
- [ ] (Optional) completion certificates ready

---

## Submission reminder

All classwork and homework is submitted to:
1. **Microsoft Teams** (primary)
2. **Ishwari Raut ma'am** (copy)
