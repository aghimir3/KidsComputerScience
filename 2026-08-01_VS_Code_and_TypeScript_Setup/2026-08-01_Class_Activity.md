# Class Activity: Green Check Setup and AI Logic Bug Hunt

**Date:** August 1, 2026  
**Format:** Whole-class teacher follow-along, then partner verification  
**Primary goal:** Every student leaves with a reusable local TypeScript setup  
**Backup:** TypeScript Playground for computers that block installation

## Student Mission

Today we are moving from a browser coding lab to a real coding workspace. Your
job is to earn as many Green Checks as your computer allows, help a partner
verify their checks, and then test a decision program.

Technical restrictions are not a failure. If an installation is blocked, save
the exact error and use the Playground backup for equal class credit.

## Partner Roles

- **Builder:** follows the teacher and works on their own computer.
- **Verifier:** reads the current checkpoint aloud and confirms the output.

Switch roles after each Green Check. Both students still complete the setup on
their own computers.

## Green Check 1: The Editor Opens

1. Open Visual Studio Code.
2. Find the Explorer on the left.
3. Find **Terminal > New Terminal**.
4. Windows students confirm the terminal is **Command Prompt**.
5. macOS students confirm the terminal uses `zsh`.

Partner check: point to the Explorer and terminal without clicking for your
partner.

## Green Check 2: Node and npm Work

Run:

```text
node --version
npm --version
```

Partner check: both commands print a version number.

## Green Check 3: TypeScript Works Everywhere

Follow the teacher before running the global installation:

```text
npm install -g typescript
```

Verify:

```text
tsc --version
```

Partner check: the terminal prints a TypeScript version number.

## Green Check 4: The Workspace Is Open

1. Create a `KidsComputerScience` folder.
2. Create `2026-08-01-decisions` inside it.
3. Open the dated folder in VS Code.
4. Trust the folder only because you created it yourself.
5. Create and save `decisions.ts`.

Partner check: the Explorer shows the dated folder and `decisions.ts`.

## Green Check 5: TypeScript Compiles

Add the starter program from the presentation or classwork sheet. Save it, then
run:

```text
tsc decisions.ts
```

Partner check: `decisions.js` appears in the Explorer.

Discuss:

- Which file do humans edit?
- Which tool checked and compiled it?
- Why did a `.js` file appear?

## Green Check 6: Node Runs the Program

Run:

```text
node decisions.js
```

Change the score in `decisions.ts`, save, compile again, and run again. Test at
least `95`, `70`, and `49`.

Partner check: different scores reach different branches.

## AI Logic Bug Hunt

An AI assistant suggested this program:

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

Before running it, predict the output for `95`.

Then answer:

1. Does the code compile?
2. Is the answer logically correct?
3. Which true branch is reached first?
4. How should the conditions be reordered?
5. Which test scores prove the repair works?

Main takeaway:

> AI-written code can run without errors and still be logically wrong. Humans
> must predict, test, and verify it.

## Share-Out

Be ready to complete one sentence:

- One Green Check I earned was ____.
- One setup problem I learned to diagnose was ____.
- One test value that revealed a logic bug was ____.

## Teacher and Assistant Notes

- Keep the entire class on the same checkpoint whenever possible.
- Do not troubleshoot one computer silently for a long period; move the student
  to the Playground backup and record the issue for the Hangout Session.
- Never request a student's administrator password.
- On Windows, switch from PowerShell to Command Prompt before changing any
  security setting.
- On macOS, use the `sudo` fallback only with teacher or parent approval.
- Do not install optional extensions during this lesson.

