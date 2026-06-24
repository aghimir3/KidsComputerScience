# AI Agents — opencode Setup Guide

A step-by-step guide to getting **opencode** running with **OpenRouter** and **DeepSeek V4 Flash**, then adding an **MCP server** and a **skill**. Works on Mac and Windows.

> **Teacher note:** opencode's desktop app is in **beta**, so menus and button labels may shift between versions. If a screen doesn't match this guide exactly, look for the closest matching option — the steps are the same idea. It's worth doing a full dry-run yourself before class. Exact menu names below are written generically on purpose.

---

## What each student needs

- A Mac or Windows computer where they can install an app (the desktop app does **not** run on Chromebooks).
- The **class OpenRouter API key** (you provide this — see the "For the teacher" section).
- Internet access.

---

## Part 1 — Install the opencode desktop app

**Mac**

1. Go to **opencode.ai/download**.
2. Download the **macOS** version (pick **Apple Silicon** for M1/M2/M3/M4 Macs, or **Intel** for older Macs).
3. Open the downloaded file and drag opencode into your Applications folder.
4. Launch it. If macOS warns about an app from the internet, open **System Settings → Privacy & Security** and click **Open Anyway**.

> Tip: if you use Homebrew, you can instead run `brew install --cask opencode-desktop`.

**Windows**

1. Go to **opencode.ai/download**.
2. Download the **Windows (x64)** installer.
3. Run the installer and follow the prompts.
4. Launch opencode from the Start menu. If Windows SmartScreen warns you, click **More info → Run anyway**.

---

## Part 2 — Connect OpenRouter + pick the model

1. Open opencode. Look for **Settings**, **Providers**, or a **/connect** option.
2. Choose **OpenRouter** as the provider.
3. Paste the **class API key** when prompted. (Keep this key private — never share or post it.)
4. Set the model to:

   ```
   deepseek/deepseek-v4-flash
   ```

5. Send a quick test message like `say hello in one word` to confirm it answers.

> **If DeepSeek feels slow or stalls on small steps:** that's a known quirk of V4 Flash on rapid tool-calling tasks. Add a backup model in settings and switch to it if needed — a good free fallback is a `:free` model such as `meta-llama/llama-3.3-70b:free`.

---

## Part 3 — Make a workspace folder

Agents work best in their own empty folder so they don't touch anything important.

1. On the Desktop, create a new folder called `agent-class`.
2. In opencode, **open** that folder as the working directory (look for **Open Folder** or **Open Project**).
3. Everything the agent creates will land here.

---

## Part 4 — Add an MCP server (Mission C)

MCP servers give the agent new tools. opencode reads them from a config file called **`opencode.json`**.

1. In your `agent-class` folder, create a file named `opencode.json`.
2. Paste in this starter (it adds a safe **filesystem** MCP server scoped to this folder):

   ```json
   {
     "$schema": "https://opencode.ai/config.json",
     "mcp": {
       "filesystem": {
         "type": "local",
         "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "."]
       }
     }
   }
   ```

3. Save the file and **restart opencode** (or reload the project) so it picks up the new server.
4. The agent now has the filesystem MCP's tools. Try a task that uses them, e.g. *"List every file in this folder and summarize what each one does."*

> **Want a "wow" web power instead?** Swap the block for a fetch server:
> ```json
> "fetch": {
>   "type": "local",
>   "command": ["npx", "-y", "@modelcontextprotocol/server-fetch"]
> }
> ```
> Then ask: *"Fetch example.com and tell me what the page is about."*
>
> **Teacher: please pre-test whichever MCP server you choose** and confirm `npx`/Node is available, since the first run downloads the server. Pick ONE server for the class so everyone's screen matches.

---

## Part 5 — Add a Skill (Mission D)

A skill is a small instruction file the agent can reuse. In opencode, skills live in a **`skills/`** folder inside your project (or `.opencode/skills/`).

1. In `agent-class`, create a folder called `skills`.
2. Inside it, create a folder for your skill, e.g. `quiz-maker`.
3. Inside that, create a file named `SKILL.md` with this shape:

   ```markdown
   ---
   name: quiz-maker
   description: Use this when the user asks for a quiz on a topic.
   ---

   # Steps
   1. Ask the user for the topic if they didn't give one.
   2. Write 5 multiple-choice questions about the topic.
   3. Save them as quiz.html with a clean, colorful layout.
   4. Add an answer key at the bottom.
   ```

4. Save it and reload the project.
5. Test it: *"Use your quiz-maker skill to make a quiz about space."* The agent should follow your steps.

> Students will write their **own** skill in Mission D — this `quiz-maker` is just the worked example so they see the format.

---

## Quick troubleshooting

| Problem | Try this |
|---|---|
| App won't open (Mac) | System Settings → Privacy & Security → **Open Anyway** |
| App won't open (Windows) | SmartScreen → **More info → Run anyway** |
| "Invalid API key" | Re-paste the key; check for extra spaces |
| Model errors or very slow | Switch to the backup `:free` model |
| MCP server not showing up | Restart opencode; confirm `opencode.json` is valid JSON |
| `npx` not found | Install Node.js (v18+) from nodejs.org, then restart |
| Agent stuck in a loop | Stop it, give a clearer mission with a finish line |

---

## For the teacher — before class

- **Get the OpenRouter key to students safely.** Share it through your class platform's private channel, not a public post. Consider one shared class key or a few keys rotated across groups (free models allow ~20 requests/min, ~200/day — plan groups around that).
- **Pre-test the whole flow** on both a Mac and a Windows machine if you can: install → connect → one mission → add the MCP server → add the skill.
- **Pick ONE MCP server** for the class so every group's screen matches the slides and classwork.
- **Confirm Node.js (v18+) is installed** on student machines if your chosen MCP server uses `npx` (most do). You can have students install it ahead of time from nodejs.org.
- **Decide your Mission C "new task"** — the thing the agent can't do until the MCP server is added — and tell students at that point in the lesson.
- **Remind students** that the API key is like a password: never share, post, or paste it anywhere public.
