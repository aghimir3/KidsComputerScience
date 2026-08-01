# August 1, 2026 - Teacher Run of Show

## Class Goal

By the end of class, students should be able to open a local TypeScript
workspace in VS Code, verify Node.js and TypeScript, compile a `.ts` file with
`tsc`, run the generated `.js` file with Node, and test an `if / else if / else`
decision ladder.

Environment setup is the primary goal. Decision-ladder practice expands only
as time permits.

## Before Class

- Open the presentation and both setup guides.
- Download the current official VS Code and Node.js LTS installers for teacher
  demonstration. Never redistribute old installers through Teams.
- Keep these official pages ready:
  - Windows VS Code: https://code.visualstudio.com/docs/setup/windows
  - macOS VS Code: https://code.visualstudio.com/docs/setup/mac
  - Node.js LTS: https://nodejs.org/en/download/
  - TypeScript: https://www.typescriptlang.org/download/
  - Playground backup: https://www.typescriptlang.org/play
- Test all commands on one Windows computer and one Mac if available.
- Ask assistant teachers to take ownership of one operating-system group.
- Post the Windows and macOS guides before class begins.
- Homework due date: **Saturday, August 8, 2026**.

## Do Not Add Today

- Git or GitHub
- VS Code extensions
- Copilot sign-in
- `npm init` or a project-local TypeScript package
- Functions, arrays, loops, `switch`, or nested decisions

Students are installing TypeScript globally for the simplified class workflow.

## Returning Student Lane

Students whose local workspace already passes both `node --version` and
`tsc --version` may complete **Robot Repair Arcade** while the teacher supports
new installations.

- Post `2026-08-01_Returning_Students_Activity.md` separately.
- Keep returning students within July concepts: variables, types, template
  literals, operators, comparisons, and `if / else`.
- Do not let this lane preview `else if`, functions, arrays, loops, or other new
  syntax.
- Ask students to predict, test boundary values, repair type errors, and explain
  their reasoning. The depth comes from debugging, not new content.
- Bring everyone back together before the whole-class decision-ladder lesson.
- Returning students begin `else if` at the same time as everyone else.

## Flexible Schedule

| Time | Activity | Teacher focus |
|---|---|---|
| 9:00-9:15 | Welcome and goal | Explain editor, compiler, and runner. |
| 9:15-9:40 | Install VS Code | Split Windows/macOS guidance as needed. |
| 9:40-10:10 | Install Node.js LTS | Verify `node` and `npm`. |
| 10:10-10:25 | Install TypeScript globally | Run and verify `tsc`. |
| 10:25-10:30 | Green Check pause | Record blocked devices. |
| 10:30-11:00 | Break | Fixed block. |
| 11:00-11:30 | Typing practice | Fixed block. |
| 11:30-11:50 | Create workspace and file | Open folder and create `decisions.ts`. |
| 11:50-12:10 | Compile and run | Use `tsc`, then `node`. |
| 12:10-12:35 | Decision-ladder practice | Test several scores and boundaries. |
| 12:35-12:50 | AI logic bug hunt | Running code can still be wrong. |
| 12:50-1:00 | Submission and homework | Save evidence and explain next steps. |

## Opening Mental Model

Use this language:

> VS Code is where we write and save code. TypeScript checks our `.ts` file and
> turns it into JavaScript. Node.js runs the JavaScript on our computer.

Keep the workflow visible:

```text
decisions.ts -> tsc -> decisions.js -> node -> output
```

## Windows Follow-Along

1. Use the VS Code **User Installer**.
2. Install the Node.js version marked **LTS**.
3. Restart VS Code after Node installation.
4. Use **Command Prompt** in VS Code, not PowerShell.
5. Verify:

```text
node --version
npm --version
npm install -g typescript
tsc --version
```

If PowerShell shows a script-policy error, switch the terminal profile to
Command Prompt. Do not change the student's execution policy during class.

## macOS Follow-Along

1. Download the VS Code Universal `.dmg`.
2. Drag VS Code to Applications.
3. Install the Node.js version marked **LTS** using the `.pkg` installer.
4. Restart VS Code after Node installation.
5. Verify:

```text
node --version
npm --version
npm install -g typescript
tsc --version
```

If the global installation reports `EACCES` or another permission error, pause.
With teacher or parent approval, use:

```text
sudo npm install -g typescript
```

The teacher should explain that the administrator password remains private and
does not appear while typed. Never ask a student to reveal it.

## Green Check Management

Ask students to show a green reaction or type the checkpoint number in chat:

1. VS Code opens.
2. `node --version` and `npm --version` work.
3. `tsc --version` works.
4. The dated folder and `decisions.ts` are open.
5. `tsc decisions.ts` creates `decisions.js`.
6. `node decisions.js` prints an answer.

Move blocked students to the Playground after one focused troubleshooting
attempt. Record the error for the 4:30-5:30 PM Pacific Hangout Session.

## Coding Demo

Create `decisions.ts` and type the code instead of pasting it. Compile and run
after each meaningful change.

```ts
let score: number = 82;

if (score >= 90) {
  console.log("Legend rank!");
} else if (score >= 70) {
  console.log("Hero rank!");
} else if (score >= 50) {
  console.log("Explorer rank!");
} else {
  console.log("Keep training!");
}
```

Test `95`, `90`, `82`, `70`, `50`, and `49`. Ask students to predict before
each run.

## AI Connection

Show the AI-generated version with `score >= 50` before `score >= 90`.
Emphasize:

- TypeScript accepts it because the types and syntax are valid.
- Node runs it successfully.
- The logic is wrong because the first true branch wins.
- Testing several values reveals the problem.
- A human remains responsible for the result.

## Adaptive Pacing

- **Installations run long:** complete only one working local program; move the
  full decision ladder to homework.
- **Many devices are blocked:** switch the entire coding portion to the
  Playground while assistants record device-specific errors.
- **Most students finish early:** add a fourth rank and test boundary values.
- **Students are overwhelmed:** skip the AI bug hunt and use it as homework.
- **Students are confident:** let them invent a three-outcome program without
  adding new syntax.

## Closing Script

"Today you built a reusable coding workspace. You can write TypeScript, ask the
compiler to check it, and run the JavaScript with Node. Your next job is to
practice making careful decisions and testing every path."

## After Class

- Post the homework and both setup guides.
- Invite blocked students to the Hangout Session channel from 4:30-5:30 PM
  Pacific.
- Record common Windows and macOS issues for the next setup lesson.
- Do not collect screenshots that display private account names or passwords.
