# Classwork: VS Code and TypeScript Setup

**Date:** August 1, 2026  
**Points:** 100 points + 10 bonus points

## Important

Follow the teacher one checkpoint at a time. If your computer blocks an
installation, record the exact error and use the TypeScript Playground backup.
You can earn full credit through the backup path.

Never share a password, home address, phone number, or other private
information in this assignment.

## Part 1 - Open the Coding Tools (20 points)

Complete the steps for your operating system.

- Open Visual Studio Code.
- Open the integrated terminal.
- Windows: use Command Prompt.
- macOS: use the normal `zsh` terminal.
- Run `node --version` and `npm --version`.

Record the two outputs:

- Node version:
- npm version:

If a command did not work, copy the exact error or explain it in your own
words.

## Part 2 - Install TypeScript Once (20 points)

Follow the teacher before running:

```text
npm install -g typescript
```

Then run:

```text
tsc --version
```

Record the TypeScript version or the exact error.

In one sentence, explain what **global** means in this lesson.

## Part 3 - Create a Workspace (15 points)

1. Create or open a folder named `KidsComputerScience`.
2. Create `2026-08-01-decisions` inside it.
3. Open the dated folder in VS Code.
4. Create and save `decisions.ts`.

Write the folder and file names exactly as they appear in the VS Code Explorer.

Why is it safe to trust this workspace?

## Part 4 - Compile and Run (20 points)

Type this starter into `decisions.ts`:

```ts
let score: number = 82;

if (score >= 70) {
  console.log("Hero rank!");
} else {
  console.log("Keep training!");
}
```

Save the file, then run:

```text
tsc decisions.ts
node decisions.js
```

Answer:

1. Which command checks and compiles the TypeScript file?
2. Which new file appeared?
3. Which command ran the new file?
4. What printed in the terminal?

## Part 5 - Build a Decision Ladder (15 points)

Upgrade the program so it has four possible outcomes:

- `90` or more: `Legend rank!`
- `70` or more: `Hero rank!`
- `50` or more: `Explorer rank!`
- Anything lower: `Keep training!`

Write your completed code. Then compile and run after each score change.

Record the output for:

- Score `95`:
- Score `70`:
- Score `49`:

Explain why the conditions should go from the highest score to the lowest.

## Part 6 - AI Logic Bug Hunt (10 points)

An AI assistant wrote:

```ts
let score: number = 95;

if (score >= 50) {
  console.log("Explorer rank!");
} else if (score >= 90) {
  console.log("Legend rank!");
} else {
  console.log("Keep training!");
}
```

Answer:

1. What does the program print for `95`?
2. Why does the program stop at the wrong branch?
3. Rewrite the conditions in the correct order.
4. Why must humans test AI-written code even when it compiles?

## Bonus - Add and Test a New Branch (10 points)

Add a fifth outcome of your own. State the condition, message, and at least two
test values that prove it works.

## Submission

Submit your completed classwork to:

1. Microsoft Teams
2. Ishwari Raut ma'am

Include the completed PDF or markdown response and one screenshot showing your
code and terminal output. If you used the Playground backup, submit a
Playground screenshot instead. Do not include passwords or private folders in
the screenshot.

