# Class Activity — Same Task, Three Ways

**Date:** May 2, 2026
**Lesson:** How AI Agents Actually Work
**Block:** ~30 minutes (10:00 - 10:30 AM, before break)

---

## Goal

Students see the *same* prompt run three different ways — chatbot, assistant with memory, and a full agent with tools — and watch the outputs diverge. By the end they should be able to explain *why* the agent answer is different, in their own words.

---

## What you'll need

- One screen to share with the class
- Three browser tabs open to:
  1. **Chatbot mode** — a basic LLM chat with no tools (e.g., ChatGPT free *with web search disabled*, or any local/offline LLM)
  2. **Assistant with memory** — same model with conversation memory but no tools (or a chatbot that remembers across messages)
  3. **Full agent** — Gemini with Search/Canvas, ChatGPT with tools, or Claude with web search enabled
- A way to show the chat side by side, or one at a time with a quick recap after each

---

## The single prompt (use the SAME wording in all three tabs)

```
What is the most popular video game right now,
how many people are playing it this week,
and write me a 4-line poem about it?
```

This prompt is deliberately chosen because it requires:
- **Live data** (chatbot can't get it)
- **A creative output** (all three can do this)
- **Two distinct "things"** (tests planning)

---

## Run it three ways — what to point out

### 1. Chatbot (no tools, no web)

**What students will see:**
- It will guess based on training data — likely an outdated answer (e.g., names a game from 1-2 years ago).
- It will write the poem fine.
- It will sound *confident* even when wrong.

**Talking points:**
- "Notice how confident it sounds? That's a hallucination risk."
- "It can't *know* what's popular this week — its training stopped months ago."
- Connect back to 4/25: this is the world without an agent loop.

### 2. Assistant with memory (still no tools)

**What students will see:**
- Same problem as #1 — still no live info.
- BUT if you ask a follow-up like *"actually, change the poem to be funny"*, it remembers the original game.

**Talking points:**
- "Memory ≠ tools. It can remember, but still can't look anything up."
- This is the in-between step in the chatbot → assistant → agent evolution.

### 3. Full agent (web search + reasoning visible)

**What students will see:**
- The agent *thinks out loud* — "I should search for current popular games..."
- It uses a **tool** (web search) — students can see the search query and results scroll by.
- It returns up-to-date numbers with sources.
- Then plans the poem.

**Talking points:**
- "Watch the THINK / ACT / OBSERVE happen in real time."
- "Every search you saw is a network request — same idea as when you load a website."
- This is the AI connection back to networking (Jan-Mar phase).

---

## Quick discussion (5 min)

After all three runs, ask:

1. **Which answer was MOST accurate? Why?** *(Looking for: agent, because it had the right tool — web search.)*
2. **Which answer was FASTEST? Why?** *(Looking for: chatbot, because no extra steps. Tradeoff: speed vs. accuracy.)*
3. **If your task is "write me a poem about my dog" — which one do you pick? What about "find me a flight"?** *(Looking for: match the task to the right tool.)*

---

## Backup plan if internet/AI is slow

If the demo doesn't go smoothly, you can:
- Show pre-recorded screenshots of each (save before class)
- Or just walk through it on the whiteboard:
  - Draw three columns: Chatbot / Assistant / Agent
  - Write the same prompt at the top
  - Fill in expected answers and key differences
- The lesson works either way; the goal is the *contrast*, not a flawless live run

---

## Connection back to homework

Tell students at the end of this activity:
> "For homework you'll DESIGN your own agent — pick a task in your own life that needs an agent, not a chatbot. We just saw the difference. Now you build one."

This sets up the "Build Your Workflow" homework directly.

---

## Challenge Question (after the activity)

After you've finished the three demos, the discussion, and the homework framing, pose this to the class. Give them ~30 seconds to think silently, then 3-5 minutes to discuss as a group. There is no single right answer.

> **"An AI agent is asked: *'Find me a flight to New York under $200 and book it.'* It searches, finds the cheapest flight at $250 — and books it anyway. Where in the Think → Act → Observe → Repeat loop did the agent go wrong, and what would you change to fix it?"**

**What to listen for** *(any of these is a great answer — multiple are correct):*
- The **OBSERVE** step failed — the agent saw the $250 price but didn't compare it to the $200 limit
- The **THINK/PLAN** step was missing a "should I stop and ask?" decision before the ACT step
- The agent needed a **CONFIRMATION** tool ("ask the user before booking") that it didn't have
- The agent did what was *literally* asked, not what was *intended* — this is a real failure mode of agents today
- Bonus answer: "agents need guardrails / limits" — perfect setup for the future ethics lesson

**Why this question is challenging:**
- It forces students to map a *failure* onto the loop they just learned (most examples in class were successes)
- It connects directly to the homework: when they design their own agent, they have to think about what could go wrong
- It quietly introduces the idea of agent safety without making it the topic of the lesson

**Optional follow-up if discussion is strong:**
> "Now: what if instead of booking a flight, the agent was told to *delete files older than 6 months* and it deleted your homework folder? Same kind of mistake — what's the fix?"
