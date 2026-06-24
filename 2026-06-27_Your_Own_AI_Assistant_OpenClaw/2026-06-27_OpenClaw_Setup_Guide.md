# Your Own AI Assistant — OpenClaw + OpenRouter Setup Guide

A step-by-step guide to getting **OpenClaw** running on your own computer, connected to a real model (**DeepSeek V4 Flash**) through **OpenRouter**, so you can chat with your very own AI assistant right in the terminal. Works on **Mac and Windows**.

> **Teacher note:** OpenClaw moves fast and its menus can change between versions. If a screen doesn't match this guide exactly, look for the closest matching option — the *idea* of each step stays the same. Please do a full dry-run yourself before class (install → onboard → gateway → chat → one mission). This is the **last class of the AI unit**, so we want the setup to feel smooth and exciting.

---

## What each student needs

- A **Mac or Windows laptop** where they can install software. (OpenClaw does **not** run on Chromebooks.)
- **Node.js 22.19 or newer** (Node 24 recommended) — we install this in Part 1.
- The **class OpenRouter API key** (your teacher provides this — see the "For the teacher" section).
- Internet access.

> **Heads up:** OpenClaw is a *powerful* tool — it can read and write files and run real commands on your computer. That's what makes it amazing, but it's also why we use it **carefully**. Follow the safety steps and always read what the assistant wants to do before you approve it.

---

## Part 1 — Install Node.js

OpenClaw runs on Node.js. Let's make sure you have a new enough version.

1. Open your terminal:
   - **Mac:** open the **Terminal** app (Applications → Utilities → Terminal).
   - **Windows:** open **PowerShell** (Start menu → type "PowerShell").
2. Check if Node is already installed:

   ```bash
   node --version
   ```

3. If you see **v22.19** or higher (like `v24.x`), you're good — skip to Part 2.
4. If the number is lower, or you get an error, install Node 24:
   - **Mac (with Homebrew):** `brew install node`
   - **Windows:** download the **LTS** installer from [nodejs.org](https://nodejs.org) and run it.
   - Then close and reopen your terminal and check `node --version` again.

---

## Part 2 — Install OpenClaw

In your terminal, install OpenClaw globally:

```bash
npm install -g openclaw
```

> If macOS or Windows complains about permissions, try `sudo npm install -g openclaw` (Mac) or reopen PowerShell **as Administrator** (Windows).

Check it worked:

```bash
openclaw --version
```

You should see a version number like `v2026.6.x`.

---

## Part 3 — Onboard + connect OpenRouter

This is where we plug in the **class API key** and pick our model.

1. Start the setup wizard:

   ```bash
   openclaw onboard
   ```

2. When it asks **"Choose your LLM provider,"** pick **OpenRouter**.
3. Paste the **class OpenRouter API key** when prompted. *(Keep this key private — it's like a password. Never share it or post it anywhere.)*
4. When it asks about connecting a messaging channel (WhatsApp, Telegram, etc.), choose **Skip for now**. We'll chat from the terminal instead.
5. Set the model to **DeepSeek V4 Flash**:

   ```bash
   openclaw models set openrouter/deepseek/deepseek-v4-flash
   ```

> **Why DeepSeek V4 Flash?** It's fast and inexpensive, so one class key goes a long way. If a model ever feels stuck or slow, your teacher may give you a backup model to switch to.

---

## Part 4 — Start the Gateway (the assistant's brain)

The **Gateway** is the always-on "brain" that keeps your assistant running. Start it and **leave this terminal open**:

```bash
openclaw gateway
```

You should see something like:

```
🦞 OpenClaw Gateway
   WebSocket control plane: ws://localhost:18789
   Status: RUNNING
```

> **Leave this window alone** while you work — it's doing the thinking. Closing it stops the assistant (which is actually handy: when class ends, closing this window shuts everything down).
>
> **Port already in use?** If you see an error about port `18789`, ask your teacher — another program may be using it.

---

## Part 5 — Chat with your assistant

Open a **new** terminal window (keep the Gateway running in the first one). Then start chatting:

```bash
openclaw chat
```

Now type a message and press Enter, like:

```
Introduce yourself in two sentences. What can you help me with?
```

Type `exit` (or press Ctrl+C) to leave the chat.

You can also ask a single question without entering chat mode:

```bash
openclaw chat "Write a haiku about robots and save it to robot.txt"
```

### Execution approval — YOU are in control

When the assistant wants to **do** something on your computer (like create a file or run a command), it will **ask first**:

```
Agent wants to execute:
  $ echo "hello" > hello.txt
  [approve]   [deny]
```

This is called **`ask` mode**, and it's the default. **Always read what it wants to do before you approve it.** If you're not sure, choose **deny** and ask your teacher.

---

## Part 6 — Safety setup for class

OpenClaw is powerful, so we run it with training wheels on. Here's the safe setup we use in class:

| Setting | What we do | Why |
|---|---|---|
| **Permission mode** | Keep the default **`ask`** mode | You approve every action before it runs |
| **Gateway** | Run `openclaw gateway` in the foreground (no daemon) | When you close the window, it stops — nothing runs after class |
| **Network** | Keep it on **localhost** (the default) | Your assistant stays on your computer only |
| **Heartbeat** | Leave it **off** (don't create a `HEARTBEAT.md`) | The assistant won't act on its own or use credits after class |
| **Skills** | Don't install random skills from the internet | Some community skills can be unsafe |
| **Workspace** | Work in a fresh folder | The assistant won't touch anything important |

> **The golden rule:** read before you approve, and never share the API key.

---

## Quick troubleshooting

| Problem | Try this |
|---|---|
| `openclaw: command not found` | Re-run `npm install -g openclaw`; close and reopen the terminal |
| `node` version too old | Install Node 24 from nodejs.org, reopen terminal, check `node --version` |
| "Invalid API key" | Re-paste the class key; check for extra spaces; rerun `openclaw onboard` |
| Port `18789` already in use | Ask the teacher; another program may be using it |
| Chat hangs / no reply | Make sure the **Gateway** terminal is still running and you have internet |
| Model errors or very slow | Switch to the teacher's backup model with `openclaw models set ...` |
| Assistant won't run a command | That's `ask` mode — approve it when prompted (after reading it!) |
| Permission denied on install (Mac) | Try `sudo npm install -g openclaw` |

---

## For the teacher — before class

- **Preload credit + create the key.** Add about **$10 of credit** to your OpenRouter account and create an API key at [openrouter.ai/keys](https://openrouter.ai/keys). With **DeepSeek V4 Flash**, $10 is plenty for a full class of hands-on chatting.
- **Share the key safely.** Send it through your class platform's private channel — never a public post. Consider **one key per group/team** so groups don't all hit rate limits at the same moment (they all draw from the same $10 pool).
- **Keep the heartbeat OFF.** Do **not** create a `~/.openclaw/HEARTBEAT.md` with tasks. With no heartbeat tasks, the assistant only acts when a student talks to it — so credits aren't drained during the break or after class. (If you want extra insurance, set the heartbeat model to DeepSeek too.)
- **Pre-test the whole flow** on both a Mac and a Windows laptop if you can: install Node → install OpenClaw → onboard with the class key → set DeepSeek → start the gateway → `openclaw chat` → run one mission → approve one command.
- **Pre-install where possible.** If students can install Node.js and run `npm install -g openclaw` *before* class, you'll save a lot of setup time on the big day.
- **Remind students** the API key is like a password: never share, post, or paste it anywhere public. Keep all activity in `ask` mode so every action is approved.
- **Run the foreground gateway** (`openclaw gateway`, not `--install-daemon`) so closing the terminal cleanly stops everything when class ends.

---

*Last day of the AI unit — have fun, stay safe, and celebrate how far the class has come!* 🦞
