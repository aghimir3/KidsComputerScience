# VS Code Setup Guide — Running TypeScript with Code Runner

Follow these steps once. After that, running your code is a single click.

> **Why this guide exists:** Code Runner's factory setting tries to run TypeScript with a tool called `ts-node`, which isn't installed. So clicking **Run Code** fails with something like `'ts-node' is not recognized`. Step 4 fixes that permanently.

---

## What you need

- A Mac or Windows computer where you can install apps
- About 10 minutes

---

## Step 1 — Install VS Code

1. Go to **code.visualstudio.com**
2. Click the big download button (it detects your computer automatically)
3. Run the installer and accept the defaults
4. Open VS Code when it finishes

---

## Step 2 — Install Node.js

Node is the program that actually *runs* your TypeScript file.

1. Go to **nodejs.org**
2. Download the **LTS** version (must be **Node 24 or newer**)
3. Run the installer and accept the defaults
   - **Windows:** if you see a checkbox about "Add to PATH," leave it checked
4. **Restart your computer** (this matters — VS Code won't find Node until you do)

**Check it worked:** open VS Code, go to **Terminal → New Terminal**, type this and press Enter:

```
node --version
```

You should see something like `v24.x.x`. If you see an error, Node didn't install correctly — redo this step.

---

## Step 3 — Install the Code Runner extension

1. In VS Code, click the **Extensions** icon in the left sidebar (four squares)
2. Search for **Code Runner**
3. Click **Install** on the one by *Jun Han*

---

## Step 4 — Fix the TypeScript setting ⭐ (the important one)

1. Open the Command Palette: **Ctrl + Shift + P** (Windows) or **Cmd + Shift + P** (Mac)
2. Type `settings json` and choose **Preferences: Open User Settings (JSON)**
3. A file called `settings.json` opens. Add the two settings below **inside** the outer curly braces `{ }`:

```json
{
    "code-runner.executorMap": {
        "typescript": "node $fullFileName"
    },
    "code-runner.runInTerminal": true
}
```

4. **Save the file** (Ctrl+S / Cmd+S)

**If your settings.json already had things in it,** just add the two settings and make sure there's a comma between each entry. For example:

```json
{
    "editor.fontSize": 14,
    "code-runner.executorMap": {
        "typescript": "node $fullFileName"
    },
    "code-runner.runInTerminal": true
}
```

### What these two settings do

| Setting | Why it matters |
|---|---|
| `"typescript": "node $fullFileName"` | Tells Code Runner to run your `.ts` file with Node instead of the missing `ts-node`. Node 24 understands TypeScript on its own. |
| `"runInTerminal": true` | Runs your program in the real Terminal instead of the read-only Output box — this is what makes **Ctrl + C** work to stop a runaway loop. |

---

## Step 5 — Test it

1. Make a new folder for class, and inside it a new file called **`loops.ts`**
2. Type this in:

```typescript
console.log("VS Code works!")
```

3. Right-click anywhere in the file and choose **Run Code** (or press **Ctrl+Alt+N** / **Cmd+Alt+N**)
4. You should see `VS Code works!` appear in the Terminal at the bottom

If you see that message, you're ready for class!

---

## Stopping a program that won't stop

You'll write an infinite loop on purpose in class. To stop it:

- Click inside the **Terminal** panel at the bottom
- Press **Ctrl + C**

That's the universal "stop this program" command on every computer.

> If you skipped `"runInTerminal": true`, your code runs in the Output panel where Ctrl+C does nothing. Use **Ctrl+Alt+M** to stop it there, or go back and add that setting.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `'ts-node' is not recognized` | Step 4 wasn't saved. Reopen settings.json and check the `executorMap` line. |
| `'node' is not recognized` | Node isn't installed or you didn't restart. Redo Step 2, then restart. |
| Nothing happens when I click Run Code | Make sure your file is saved and ends in `.ts` |
| Red squiggles but the code still runs | That's normal! VS Code checks types; Node just runs the file. Fix the squiggle anyway — it's usually a real bug. |
| Ctrl + C doesn't stop my loop | Click *inside* the Terminal first, then press it. Or add `"runInTerminal": true`. |
| Output shows an old result | Save the file (Ctrl+S) before running. |

---

## If you can't install software on your computer

Some school or family computers block installs. You're not stuck:

- **Pair up.** Work with a groupmate who has it working — you plan the loops and read the code out, they type. Switch roles halfway.
- **Use the online playground.** Go to **typescriptlang.org/play** — every loop from today works there exactly the same. You just won't have the VS Code terminal.

---

## For the teacher — before class

- **Do this setup yourself first**, ideally on both a Mac and a Windows machine. Step 4 is the one that bites.
- **Send Steps 1–2 home ahead of time** so installs aren't eating class minutes. The restart after installing Node is the most-skipped step.
- **Verify Node 24+**, not just "Node installed." Older versions can't run `.ts` files directly and Step 4 will fail.
- **Plan B if a machine has an older Node:** install the runner globally with `npm install -g ts-node`, then leave Code Runner's default setting alone.
- **Demo Ctrl + C before the infinite-loop mission** so nobody panics when their screen fills up.
