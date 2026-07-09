# ✅ Pre-Class Test Checklist — OpenClaw on My Mac
**For:** Saturday, June 27 (last day of the AI unit)
**Goal:** Confirm the full student flow works on a Mac *before* class, and finish teacher prep (OpenRouter credit, keys, DeepSeek, heartbeat off).
**Note to self:** This is a personal scratch file — delete it when you're done. ⏱️ Plan ~30–40 min.

---

## A. Accounts & money — do this the day before
- [ ] Sign in (or sign up) at **openrouter.ai**
- [ ] Add about **$10 credit** to the account
- [ ] Create API key(s) at **openrouter.ai/keys** — one **per group** is ideal (name them like `kids-class-group1`)
- [ ] Copy each key somewhere safe (you'll paste during onboarding)
- [ ] *(Optional)* Set a **spend limit** on each key as a safety cap
- [ ] Decide how you'll share keys **privately** (e.g., Teams private message) — never in a public post

> 💡 With DeepSeek V4 Flash, $10 is plenty for a full class of hands-on chatting.

---

## B. Install prerequisites (Mac)
- [ ] Open **Terminal** (Applications → Utilities → Terminal)
- [ ] Check Node: `node --version`
  - Need **v22.19 or higher** (v24.x is ideal)
  - If missing/old: `brew install node` (or download LTS from nodejs.org)
  - Re-check: `node --version`
- [ ] Check npm: `npm --version` (any recent version is fine)

---

## C. Install OpenClaw
- [ ] `npm install -g openclaw`
  - If you see **EACCES / permission denied**: `sudo npm install -g openclaw`
- [ ] Confirm it installed: `openclaw --version` → shows a version like `v2026.6.x`

---

## D. Onboard + connect OpenRouter
- [ ] `openclaw onboard`
  - Choose provider: **OpenRouter**
  - Paste your **class API key**
  - Messaging channel: **Skip for now**
- [ ] Set the model: `openclaw models set openrouter/deepseek/deepseek-v4-flash`
- [ ] Verify auth + model:
  - `openclaw models status`
  - `openclaw models list --provider openrouter`

✅ **What good looks like:** no auth errors, and `deepseek-v4-flash` shows up as available.

---

## E. Safety config (protect the $10 + keep it local)
- [ ] **No heartbeat tasks.** Make sure this file does NOT exist (or is empty):
  - `cat ~/.openclaw/HEARTBEAT.md` → expect **"No such file or directory"** (good!)
  - If it exists with tasks: `rm ~/.openclaw/HEARTBEAT.md`
- [ ] **Stays local.** Don't expose port 18789 — the default localhost bind is what we want
- [ ] **Ask mode stays on** (the default). Do **not** switch to `auto`
- [ ] Peek at the config and confirm the key + model are set:
  - `cat ~/.openclaw/openclaw.json`

---

## F. Start it up (two terminals)
- [ ] **Terminal 1:** `openclaw gateway`
  - ✅ Look for: `Status: RUNNING` on `ws://localhost:18789`
  - Leave this window **open**
- [ ] **Terminal 2:** `openclaw chat`
  - Type: `Hello! Tell me what you can do.`
  - ✅ You should get a reply within a few seconds

---

## G. Dry-run the student missions (the most important part!)
Make a fresh, empty folder first so the agent has a safe sandbox:
```bash
mkdir ~/Desktop/openclaw-test && cd ~/Desktop/openclaw-test
openclaw chat
```
Then run each mission exactly as the students will:
- [ ] **A — First Contact:** `Introduce yourself in two sentences. What can you help me with?`
- [ ] **B — Watch It Act:** `Make a file called space.txt with one cool fact about space.`
  - ✅ Confirm it shows the **[approve] / [deny]** prompt → approve → then `cat space.txt`
- [ ] **C — Personality:** `From now on your name is Nova, a cheerful helper. Re-introduce yourself.`
- [ ] **D — Memory:** `Remember: my team is the Sharks and our favorite game is Minecraft.`
  - then ask: `What is my team's name and our favorite game?`
- [ ] **E — Interview:** ask the 3 questions (memory / API key / what it does before running a command)
- [ ] **F — Quick Quests:** `Make jokes.txt with 3 kid-friendly jokes`
- [ ] ⏱️ Note how long a typical reply takes (DeepSeek speed sanity check)

---

## H. Cost check (confirm the $10 is safe)
- [ ] After the dry-run, open the **OpenRouter dashboard → usage** → confirm only a few **cents** were used
- [ ] Leave the gateway running idle for ~5 min, then recheck usage is **flat** (proves heartbeat isn't spending)

---

## I. Shut down cleanly
- [ ] In the chat terminal: type `exit` (or Ctrl+C)
- [ ] In the gateway terminal: **Ctrl+C** to stop it
- [ ] *(Optional)* `openclaw gateway status` → confirms it's stopped
- [ ] ✅ Nothing should keep running after class

---

## 🧯 Troubleshooting quick hits
- `openclaw: command not found` → reinstall, then close & reopen Terminal
- **EACCES** on install → `sudo npm install -g openclaw`
- **Port 18789 in use** → `lsof -i :18789`, then stop that process
- **Invalid API key** → re-paste the key (watch for extra spaces); rerun `openclaw onboard`
- **Slow / stuck model** → have a backup ready: `openclaw models set openrouter/<provider>/<model>`
- **Chat hangs** → make sure the gateway terminal is still running + you have internet

---

## 📝 Notes to self (what worked / what to tell students)
- Reply speed felt: ____________________
- Anything confusing in onboarding: ____________________
- Backup model to use if DeepSeek is slow: ____________________
- Pre-install ask for students (Node + `npm install -g openclaw`): ____________________

---

## 🪟 If any students are on Windows
- Same flow, but install Node from **nodejs.org**, use **PowerShell**, and run it **as Administrator** if the global install fails.
- Reminder: OpenClaw does **not** run on Chromebooks.
