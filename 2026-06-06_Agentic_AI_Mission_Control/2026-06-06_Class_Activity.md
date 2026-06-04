# Class Activity - June 6, 2026
## Agentic AI Mission Control: From Vibe Coding to Supervised Agents

---

## Overview

**Theme:** From Vibe Coding to Agentic Coding  
**Format:** Teacher-led demo, practical student build, debug gallery  
**Tools Needed:** Gemini Canvas or another AI app-builder

Students already learned how Gemini Canvas and Lovable can turn prompts into apps. Today they learn how to supervise an agent-like workflow: give a goal, define success, choose tools, set safety limits, test the result, and refine.

Do not introduce a specific agent platform yet. Keep the focus on safe workflow habits.

---

## Learning Goals

By the end of class, students should be able to:

1. Explain why an AI agent needs a clear goal and success criteria.
2. Name common tools an agent might use: browser, files, code, search, messages.
3. Identify actions that should require human approval.
4. Use a test checklist before deciding an AI-built app is finished.
5. Explain why tool-using agents need safety rules before autonomy.

---

## Timing

| Time | Activity |
|------|----------|
| 9:00-9:20 | Recap May 30: vibe coding, HTML/CSS/JS, build-test-refine |
| 9:20-9:45 | Mini-lesson: chatbot vs app-builder vs agentic workflow |
| 9:45-10:15 | Teacher demo: Agent Mission Control on a small app |
| 10:15-10:30 | Safety discussion: tools, permissions, approval |
| 10:30-11:00 | Break |
| 11:00-11:30 | Typing Practice |
| 11:30-12:20 | Student classwork: supervised app improvement |
| 12:20-12:45 | Share/debug gallery |
| 12:45-1:00 | Kahoot + homework explanation |

---

## Teacher Demo: Agent Mission Control

### Setup

Open Gemini Canvas and create or reuse a simple app. Recommended starter prompt:

```text
Build a simple quiz game for kids with 5 computer science questions,
a score counter, a restart button, and a colorful classroom theme.
Use HTML, CSS, and JavaScript.
```

After the first build, explain that the AI has made a starting version, but the human is now the supervisor.

### Demo Step 1 - Write the Job Brief

Show this template on screen:

```text
Goal:
Improve the quiz game so it is easier and more fun to use.

Success Criteria:
- The quiz has 5 questions.
- The score updates correctly.
- The restart button works.
- The design is readable.
- A student can finish the quiz without help.

Allowed Tools:
Gemini Canvas preview, code editor, browser preview.

Not Allowed:
Do not delete the whole app. Do not add logins or collect personal info.

Approval Required:
Ask before changing the whole theme or replacing the game idea.

Test Checklist:
Click every answer, finish the quiz, check the score, restart, test again.
```

### Demo Step 2 - Ask for a Plan First

Prompt:

```text
Act like an AI coding agent, but do not change the app yet.
Read my goal and success criteria.
Make a short plan for improving the quiz game.
Then wait for my approval.
```

Talking points:

- Agents should plan before acting.
- The human should read the plan.
- If the plan is too big or unsafe, the human should stop it.

### Demo Step 3 - Improve One Thing at a Time

Prompt:

```text
Make only one change: improve the quiz design so the question,
answers, score, and restart button are easy to read.
Do not change the questions yet.
```

Test the app in Preview. Narrate:

- "I am observing the result."
- "Now I test, not just look."
- "If something broke, I refine."

### Demo Step 4 - Add a Feature

Prompt:

```text
Add a progress label that says Question 1 of 5, Question 2 of 5,
and so on. Keep the existing score and restart button working.
```

Test again.

### Demo Step 5 - Fix a Bug

If a real bug appears, use it. If not, use this safe simulated bug prompt:

```text
Review this quiz game like a careful tester.
Find one small bug or confusing behavior.
Explain it in one sentence, then fix only that issue.
```

Talking points:

- Debugging is part of the loop.
- A good supervisor asks for small changes.
- Testing tells us whether the agent really succeeded.

---

## Safety Discussion

Ask students:

> "If an agent can use tools, which tools feel safe? Which tools feel risky?"

Write answers in three columns:

| Usually Safe | Needs Care | Approval Required |
|--------------|------------|-------------------|
| Read a web page | Edit a file | Delete files |
| Preview an app | Search the web | Send a message/email |
| Explain code | Run code | Spend money or buy things |
| Make a checklist | Change settings | Share private information |

Key line:

> "More tools means more power, but also more responsibility."

Future agent tools connection:

- Tool-using agents can connect an LLM to real tools.
- Tools can include files, browser control, commands, messages, and skills.
- That is why permissions, approvals, and a safe workspace matter.
- Students are not installing a new agent platform today; June 6 is the safety and workflow foundation.

---

## Student Classwork

Students may start from:

1. Their May 30 app or game.
2. A fresh Gemini Canvas app.
3. The teacher starter quiz prompt.

They must:

1. Fill out an agent job brief.
2. Make two improvements.
3. Fix one bug or confusing behavior.
4. Test using a checklist.
5. Reflect on what a future tool-using agent would need permission to do.

Encourage small prompts:

- "Make only one change..."
- "Do not delete..."
- "Keep the existing behavior..."
- "Explain what you changed..."
- "Give me a test checklist..."

---

## Share/Debug Gallery

Each volunteer shares for about 60 seconds:

1. What app they improved.
2. One prompt they used.
3. One test they ran.
4. One thing they would require approval for if this were a tool-using agent.

Teacher listens for:

- Clear success criteria.
- Real testing, not just visual inspection.
- Permission awareness.
- Small, controlled changes.

---

## Backup Plan

If AI tools are slow:

1. Run the demo from a prepared screenshot or prior Canvas app.
2. Students complete the job brief and test checklist on the PDF.
3. Students write the three prompts they would use.
4. Discuss which actions need approval.

If students cannot sign in:

1. Pair them with someone who has access.
2. Let them complete the supervisor role: goal, permissions, testing, reflection.
3. They can still receive full credit if their planning and testing work is complete.

---

## Homework Bridge

End class with:

> "Today you supervised an AI app-builder. Later, we may use agents that can touch real files and tools. Before we give an agent that much power, we need to know how to write clear goals, permissions, approval rules, and tests."
