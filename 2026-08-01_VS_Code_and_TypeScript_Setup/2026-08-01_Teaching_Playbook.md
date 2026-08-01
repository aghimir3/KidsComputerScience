# Teaching Playbook: Build Your Coding Workspace

**Class date:** Saturday, August 1, 2026  
**Class time:** 9:00 AM-1:00 PM Pacific  
**Main outcome:** Every student finishes with either a working local TypeScript
workspace or an equal-credit Playground path  
**New programming idea:** `else if`, only after the environment is ready

This playbook is a live-teaching guide. The times outside the fixed break and
typing blocks are flexible. Slow down when students need it and skip optional
practice before rushing the class.

## The Lesson in One Sentence

> We will install our coding tools once, use them to run a real TypeScript file,
> recap `if / else`, and then learn how `else if` adds more possible paths.

## Success Priorities

Use this order when deciding what to keep or shorten:

1. Students feel safe asking for setup help.
2. Every student reaches a working local setup or the Playground fallback.
3. Every student sees the save, compile, and run workflow.
4. The class recaps `if / else` together.
5. The class learns that an `else if` ladder checks from top to bottom and stops
   at the first true branch.
6. Extra testing, the AI bug hunt, and Kahoot expand only when time allows.

## Content Boundary

Teach today:

- VS Code as the editor
- Node.js as the JavaScript runner
- TypeScript and `tsc` as the checker/compiler
- Global TypeScript installation for reuse across class folders
- The `.ts -> tsc -> .js -> node -> output` workflow
- A recap of variables, types, comparisons, `if`, and `else`
- `else if` and the first-true-branch rule
- Predicting output and testing boundary values
- Verifying AI-written code

Do not introduce:

- Git or GitHub
- VS Code extensions or Copilot
- `npm init` or project-local packages
- Functions
- Arrays or objects
- Loops
- `switch`
- Logical operators such as `&&` or `||`
- Nested decisions

## Files to Open Before Students Arrive

Keep these ready in separate windows or tabs:

1. `2026-08-01_VS_Code_and_TypeScript_Setup.pptx`
2. `2026-08-01_Windows_Setup_Guide.md`
3. `2026-08-01_macOS_Setup_Guide.md`
4. `2026-08-01_Classwork_VS_Code_and_TypeScript_Setup.pdf`
5. `2026-08-01_Returning_Students_Activity.md`
6. `2026-08-01_Kahoot_Questions.md`
7. The official VS Code, Node.js, and TypeScript download pages
8. The TypeScript Playground as the fallback

Also prepare one empty demonstration folder named
`2026-08-01-decisions-demo`.

## Screen-Sharing Setup

- Share only the application window students need to see.
- Increase VS Code and terminal text size before class.
- Keep the Explorer, editor, and terminal visible at the same time.
- Hide personal folders, account names, notifications, and saved passwords.
- When demonstrating a command, type it slowly instead of pasting it.
- Leave successful version outputs visible long enough for students to compare.

## Assistant-Teacher Roles

If multiple assistants are available, assign:

- **Windows lane:** User Installer, Node.js LTS, Command Prompt, and version
  checks
- **macOS lane:** Applications folder, Node.js LTS, zsh, and permission issues
- **Returning-student lane:** Robot Repair Arcade check-ins without introducing
  new syntax
- **Blocker recorder:** student name, operating system, exact error, and the
  next safe step for the Hangout Session

No teacher or assistant should ask a student to reveal a password.

## Class Signals

Tell students to use these reactions or chat messages:

- `GREEN 1`: VS Code opens
- `GREEN 2`: `node --version` and `npm --version` work
- `GREEN 3`: `tsc --version` works
- `GREEN 4`: the class folder and `decisions.ts` are open
- `GREEN 5`: `decisions.js` appears
- `GREEN 6`: the program prints in the terminal
- `HELP + operating system`: a student is blocked

Use one class-wide phrase to reunite everyone:

> All coders together. Save your work and return to the presentation.

## Flexible Class Map

| Target window | Teaching block | Required result |
|---|---|---|
| 9:00-9:15 | Welcome, goal, and short recap | Students understand the three-tool workflow. |
| 9:15-10:25 | Guided environment setup | Students reach local Green Check 3 or the fallback. |
| 10:25-10:30 | Setup status and save point | Blocked devices are recorded. |
| 10:30-11:00 | **Break** | Fixed block. |
| 11:00-11:30 | **Typing practice** | Fixed block. |
| 11:30-12:05 | Workspace, first file, compile, and run | Students reach Green Check 6. |
| 12:05-12:35 | `if / else` recap and `else if` | Students trace a decision ladder. |
| 12:35-12:50 | Testing and AI logic bug hunt | Students prove that compiling is not the same as correctness. |
| 12:50-1:00 | Kahoot or recap, homework, and submission | Students know what to submit and where. |

Only the break and typing blocks are fixed. Adjust the other windows to student
understanding.

---

# Live Teaching Guide

## 1. Welcome and Set the Goal

**Use slides 1-2.**

Say:

> Until now, a website handled our coding tools for us. Today we build our own
> workspace. We install the tools once, and then we can reuse them every week.

Ask:

- What did `console.log` do in our earlier classes?
- What kind of value is `"momo"`?
- What kind of value is `42`?
- What are the two paths in an `if / else`?

Set the expectation:

> Setup problems are normal. A blocked installation is not a failed class. We
> will record the error, use the Playground, and give equal credit.

## 2. Give the Three-Tool Mental Model

**Use slides 4-5.**

Keep this visible:

```text
VS Code -> write and save
TypeScript -> check and compile
Node.js -> run the JavaScript
```

Then show the full file workflow:

```text
decisions.ts -> tsc -> decisions.js -> node -> output
```

Say:

> VS Code does not run TypeScript by itself. It is our editor. The `tsc` command
> checks the TypeScript file and creates JavaScript. Node runs that JavaScript.

Quick check:

- Which tool do we type code in?
- Which tool creates the `.js` file?
- Which tool runs the `.js` file?

Do not continue until students can match the three tools to their jobs.

## 3. Sort Students Into the Correct Lane

Ask everyone who already has VS Code to open its terminal and run:

```text
node --version
tsc --version
```

Use the results:

- **Both commands work:** post Robot Repair Arcade and move the student to the
  returning-student lane.
- **VS Code works but either command fails:** the student stays in the setup
  lane.
- **VS Code is missing:** the student begins with the operating-system guide.
- **Installation is blocked:** record the error and open the Playground.

Tell returning students:

> This is deeper practice with July ideas. Do not use `else if` yet. Save your
> work and rejoin us when you hear “All coders together.”

## 4. Install VS Code

**Use slide 6 for Windows and slide 7 for macOS.**

### Windows teaching path

1. Open the official Windows setup page.
2. Choose the **User Installer**.
3. Run the installer and keep the normal options.
4. Open VS Code.
5. Open **Terminal > New Terminal**.
6. Change the terminal profile to **Command Prompt** when necessary.

Say:

> We are using Command Prompt so a PowerShell script-policy message does not
> distract us. We are not changing the computer's security policy.

### macOS teaching path

1. Open the official macOS setup page.
2. Download the Universal build.
3. Drag Visual Studio Code into Applications.
4. Open VS Code from Applications.
5. Open **Terminal > New Terminal** and point out `zsh`.

Say:

> If the computer asks for an administrator password, keep it private. A
> teacher never needs to see or hear it.

Pause for `GREEN 1`.

## 5. Install Node.js LTS

Keep Windows and macOS instructions separate, but use the same teaching words:

> Choose the version marked LTS. LTS is the stable version intended for longer
> support. We are not choosing Current today.

After installation:

1. Close every VS Code window.
2. Reopen VS Code.
3. Open a new terminal.
4. Run each command separately:

```text
node --version
npm --version
```

Tell students that their exact version numbers may differ. The success signal
is that both commands print a version instead of an error.

Pause for `GREEN 2`.

## 6. Install TypeScript Globally

**Use slide 8.**

Say:

> We are installing TypeScript globally once. For our class, global means the
> `tsc` command will be available when we open future lesson folders. We will
> not repeat the installation every Saturday.

Type:

```text
npm install -g typescript
```

Wait for the command to finish, then type:

```text
tsc --version
```

Pause for `GREEN 3`.

If macOS reports `EACCES`, stop. Do not ask for the password. Use the
Playground fallback unless a parent or teacher has approved the documented
`sudo` path.

## 7. Take the Setup Save Point

**Use slide 9.**

Ask students to report their highest Green Check. Record anyone below Green
Check 3.

Say:

> Save or screenshot the exact error. Do not keep changing random settings. We
> now have enough information to help you safely.

Move blocked students to the Playground before the break. Their coding work
earns equal credit.

## 8. Break and Typing Practice

- **10:30-11:00 AM:** break
- **11:00-11:30 AM:** typing practice

Do not use these fixed blocks for extended installation troubleshooting.
Assistant teachers may record issues, but students should still receive the
scheduled break and typing practice.

## 9. Reunite the Class

At the end of typing practice, say:

> All coders together. Save your work and return to the presentation.

Returning students stop Robot Repair Arcade here. Everyone begins the new
workspace and the new content together.

## 10. Create the Class Workspace

**Use slide 10.**

Demonstrate one step, then wait for students to copy it:

1. Choose **File > Open Folder**.
2. Open or create `KidsComputerScience`.
3. Create `2026-08-01-decisions` inside it.
4. Trust the folder only because the student created it.
5. Create `decisions.ts`.
6. Open **Terminal > New Terminal**.

Ask students to point to the folder name in the Explorer and in the terminal.

Pause for `GREEN 4`.

## 11. Write the First Local Program

**Use slide 11.**

Type slowly:

```ts
let score: number = 82;

if (score >= 70) {
  console.log("Hero rank!");
} else {
  console.log("Keep training!");
}
```

Before running it, ask:

- What type is `score`?
- Is `82 >= 70` true or false?
- Which message should print?

Have students save the file.

## 12. Compile and Run

**Use slides 12-13.**

Type:

```text
tsc decisions.ts
```

Explain:

> A successful compile may say nothing. Quiet can mean success. Look in the
> Explorer for `decisions.js`.

Pause for `GREEN 5`, then type:

```text
node decisions.js
```

Pause for `GREEN 6`.

Ask:

- Which file do humans edit today?
- Which file did `tsc` create?
- Which file did Node run?

Change `score` to `50`. Require the full cycle again:

1. Save `decisions.ts`.
2. Run `tsc decisions.ts`.
3. Run `node decisions.js`.
4. Read the new output.

## 13. Recap `if / else`

**Use slide 14.**

Say:

> An `if / else` has two paths. The condition is a true-or-false question.
> Exactly one path runs.

Use two quick examples without adding syntax:

- `score = 82`
- `score = 50`

Ask students to point to the path before running the program.

## 14. Introduce `else if`

**Use slide 15.**

Say:

> Sometimes two paths are not enough. `else if` lets us ask another question
> only when the earlier question was false.

Build one branch at a time:

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

After each branch, read it aloud in plain language.

Use this tracing routine for every test value:

1. Start at the top.
2. Read the condition.
3. Decide true or false.
4. If true, run that branch and stop.
5. If false, move to the next condition.
6. Use `else` only if every earlier test was false.

Test in this order:

```text
95, 90, 82, 70, 50, 49
```

Students must predict before each run.

## 15. Prove That Order Matters

**Use slide 16.**

Show the wrong order:

```ts
if (score >= 50) {
  console.log("Explorer rank!");
} else if (score >= 70) {
  console.log("Hero rank!");
} else if (score >= 90) {
  console.log("Legend rank!");
} else {
  console.log("Keep training!");
}
```

Set `score` to `95` and ask:

- Is `95 >= 50` true?
- What does the program do after finding the first true branch?
- Will it ever reach `score >= 90`?

State the rule:

> For score thresholds, test from highest to lowest because the first true
> branch wins.

## 16. Run the AI Logic Bug Hunt

**Use slide 17 and Part 6 of the classwork.**

Say:

> Imagine an AI assistant wrote the wrong-order version. TypeScript accepts the
> syntax and Node runs the file. Does that prove the answer is correct?

Have students:

1. Predict the output for `95`.
2. Run the code.
3. Trace the first true branch.
4. Reorder the conditions.
5. Test `95`, `90`, `70`, and `49`.

Main takeaway:

> Compiling proves the code follows the language rules. Testing helps prove the
> program follows the human rules.

## 17. Use the Classwork Adaptively

The classwork totals **100 points + 10 bonus points**:

- Parts 1-2: setup and global TypeScript installation, 40 points
- Part 3: workspace, 15 points
- Part 4: compile and run, 20 points
- Part 5: decision ladder, 15 points
- Part 6: AI logic bug hunt, 10 points
- Bonus: new tested branch, 10 points

Do not force every student to finish every section live. A student using the
Playground can earn the same points with equivalent evidence.

## 18. Kahoot or Verbal Recap

If time allows, run the 15-question Kahoot at 20 seconds per question.

If time is short, ask these five verbal questions instead:

1. What does VS Code do?
2. What does `tsc` do?
3. What does Node.js do?
4. When is an `else if` checked?
5. Why do high score conditions go before lower conditions?

## 19. Explain Homework and Submission

The homework is **100 points + 5 bonus points** and is due August 8, 2026.

Show students where they will:

- Record the three tool versions
- Put the save, compile, and run workflow in order
- Predict decision-ladder outputs
- Build one decision program
- Explain why humans must verify AI-written code

Say:

> Submit to Microsoft Teams and copy Ishwari Raut ma'am. Include your completed
> homework and your `.ts` file or a Playground screenshot. Never include a
> password or private folder information.

## 20. Close the Class

**Use slide 18.**

Ask for one-word or one-sentence responses:

- One Green Check you earned
- One error you learned to read
- One value that tested a different branch

Closing script:

> Today you built a reusable coding workspace. You can write TypeScript, ask
> the compiler to check it, and run the JavaScript with Node. You also learned
> that decision order matters and that humans must test code—even when AI wrote
> it and the computer accepts it.

---

# Troubleshooting Guide

## VS Code Does Not Open

1. Confirm the student used the official installer.
2. Ask the student to close the installer and try opening the application.
3. If the device blocks installation, record the message.
4. Move the student to the Playground.

## `node` or `npm` Is Not Recognized

1. Confirm Node.js LTS finished installing.
2. Close every VS Code window.
3. Reopen VS Code and create a new terminal.
4. Run the version command again.
5. If it still fails, record the exact message and use the Playground.

## Windows Shows a PowerShell Script-Policy Error

1. Open the terminal dropdown.
2. Choose **Select Default Profile > Command Prompt**.
3. Open a new terminal.
4. Retry the command.

Do not change the execution policy during class.

## macOS Shows `EACCES` During Global Installation

1. Stop and read the exact error.
2. Do not ask for the administrator password.
3. Use the Playground unless the documented `sudo` fallback has adult
   approval.
4. Record the device for the Hangout Session.

## `tsc --version` Is Missing

1. Confirm `npm install -g typescript` finished.
2. Close and reopen the terminal.
3. Close and reopen VS Code if necessary.
4. Retry `tsc --version` once.
5. Record the error and use the Playground if it remains blocked.

## `tsc decisions.ts` Prints Nothing

Say:

> No error message can mean the compile succeeded.

Look for `decisions.js` in the Explorer.

## `decisions.js` Does Not Appear

Check:

- Was `decisions.ts` saved?
- Is the terminal inside the correct folder?
- Is the filename exactly `decisions.ts`?
- Did TypeScript print an error that needs to be repaired?

## Node Cannot Find the File

Check:

- Does the Explorer show `decisions.js`?
- Is the terminal inside the same folder?
- Is the command exactly `node decisions.js`?

## The Program Shows Old Output

Repeat the full cycle:

1. Save the `.ts` file.
2. Compile it again.
3. Run the `.js` file again.

## The Program Compiles but Prints the Wrong Rank

Trace conditions from the top. Circle the first true condition. Reorder score
thresholds from highest to lowest.

## One Student Needs Extended Help

After one focused troubleshooting attempt:

1. Record the exact error.
2. Move the student to the Playground.
3. Continue the whole-class lesson.
4. Invite the student to the 4:30-5:30 PM Pacific Hangout Session.

---

# Pacing Decisions

## If Setup Takes Most of the Class

Keep:

1. A working local setup or Playground fallback
2. One `decisions.ts` file
3. One successful compile and run
4. A teacher demonstration of the `else if` ladder
5. Clear homework instructions

Move independent decision-ladder practice and the AI bug hunt to homework.

## If the Class Is On Track

Complete the setup, first run, decision ladder, four boundary tests, and AI bug
hunt. Use a short verbal recap instead of Kahoot if needed.

## If the Class Finishes Early

Stay within the lesson boundary:

- Test more values
- Explain why each branch wins
- Improve variable names and messages
- Add the classwork bonus branch
- Let students compare predictions with results

Do not move to functions, arrays, loops, or other future concepts.

## If Returning Students Finish Robot Repair Arcade Early

Ask them to:

- Add more tests to the same program
- Break and repair one familiar type
- Explain code line by line
- Improve messages using template literals

Do not give them future syntax. They begin `else if` with the whole class.

---

# Teacher Reminders

- Say "first true branch wins" repeatedly.
- Ask for a prediction before pressing Enter.
- Praise careful testing and clear explanations, not speed.
- Treat the Playground as an equal-credit path.
- Never request or display a student's password.
- Do not change Windows security settings during class.
- Do not spend a long time silently troubleshooting one computer.
- Keep the `.ts` file and generated `.js` file visually distinct.
- Remind students to save before compiling.
- Keep AI framed as a drafting assistant whose work still needs human testing.

## Final Teacher Checklist

- [ ] Every student reached a local setup or the fallback.
- [ ] Returning students rejoined before `else if`.
- [ ] Students saw `.ts -> tsc -> .js -> node -> output`.
- [ ] Students traced at least one `if / else`.
- [ ] Students learned the first-true-branch rule.
- [ ] At least one AI connection was discussed.
- [ ] Classwork submission locations were stated.
- [ ] Homework submission locations and due date were stated.
- [ ] Blocked devices were recorded for the Hangout Session.
