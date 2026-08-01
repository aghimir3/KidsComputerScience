# August 1, 2026 - Teacher Run of Show

## Class Goal

Students will use the TypeScript Playground to recap July concepts, learn one
new idea - `else if` - and build, test, debug, and explain decision-based mini
games.

No student installs VS Code, Node.js, npm, or TypeScript during class. Detailed
Windows and macOS setup is the homework assignment.

## Learning Objectives

By the end of class, students should be able to:

- Recall `let`, `const`, types, operators, comparisons, `if`, and `else`
- Explain why an `else if` condition is checked only after earlier conditions
  are false
- Trace a decision ladder from top to bottom
- State that the first true branch wins
- Put score thresholds from highest to lowest
- Test boundary values and repair a logic bug
- Explain why AI-written code still needs human testing

## Before Class

- Open https://www.typescriptlang.org/play/ in a clean browser tab.
- Open the presentation, class activity, classwork PDF, and teaching playbook.
- Use the presentation only to introduce the concepts. Close it after Slide 8
  and use the class activity for all live coding.
- Post the classwork and Playground link in Microsoft Teams.
- Keep the Kahoot ready but treat it as optional if activities need more time.
- Post the homework with both operating-system setup guides.
- Remind assistant teachers that there is no installation support during class.
- Homework is due Saturday, August 8, 2026.

## Content Boundary

The only new programming concept is `else if`.

Do not introduce:

- Functions
- Arrays or objects
- Loops
- `switch`
- Logical operators such as `&&` or `||`
- User input, randomness, libraries, or packages
- VS Code extensions, Git, GitHub, or Copilot

## Flexible Schedule

| Time | Activity | Teacher focus |
|---|---|---|
| 9:00-9:20 | Welcome and July recap | Show Slides 1-2, then use Live Exercises 1-2. |
| 9:20-9:40 | Concept introduction | Show Slides 3-8 without turning them into coding worksheets. |
| 9:40-10:30 | Guided Rank Engine | Close the deck and use Live Exercise 3. |
| 10:30-11:00 | Break | Fixed block. |
| 11:00-11:30 | Typing practice | Fixed block. |
| 11:30-12:15 | Live decision exercises | Use Exercises 4-6 and adjust to student understanding. |
| 12:15-12:35 | AI Bug Hunt | Use Live Exercise 7; running code can still be logically wrong. |
| 12:35-12:50 | Class remix and share-out | Build one theme together if time permits. |
| 12:50-1:00 | Kahoot or verbal recap and homework | Explain setup homework and Hangout help. |

Only the break and typing blocks are fixed. Adjust all other activities to
student understanding.

## Opening Script

> Today we stay in the TypeScript Playground so every minute of class can go
> toward coding. We will recap the tools you already know, add one new decision
> idea, and turn it into mini games. Installing the local coding environment is
> this week's homework, with help available during the Hangout Session.

## Playground Check

Ask every student to:

1. Open https://www.typescriptlang.org/play/.
2. Confirm the language button says **TypeScript**.
3. Delete any sample code.
4. Type `console.log("Arcade ready!");`.
5. Press **Run** and find the output.

Students who finish early use the Bonus Practice activity. They must stay
within concepts already taught to the whole class.

## New Concept Script

Use this language:

> `if / else` gives us two paths. `else if` lets us ask another question when
> the earlier question was false. The program checks from top to bottom and
> stops at the first true branch.

Show the concept slides first. After Slide 8, close the deck and build this
together through Live Exercise 3:

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

Test `95`, `90`, `82`, `70`, `50`, and `49`. Require a prediction before every
run.

## AI Connection

Show the wrong-order version where `score >= 50` appears before
`score >= 90`.

Emphasize:

- TypeScript accepts the types and syntax.
- The Playground runs the program.
- The logic is still wrong because the first true branch wins.
- Boundary testing reveals the problem.
- A human remains responsible for checking AI-written code.

## Adaptive Pacing

- **Recap takes longer:** complete only the Rank Engine and one arcade mission.
- **Students struggle with `else if`:** trace values on paper before running.
- **Students are confident:** add more test values or improve messages without
  adding new syntax.
- **Activities run long:** use the five-question verbal recap instead of
  Kahoot.
- **Students finish early:** use Robot Repair Arcade and require explanations,
  not future concepts.

## Homework Transition

Say:

> Class coding is finished in the Playground today. Homework is to install VS
> Code, Node.js LTS, and TypeScript once on your own computer, then prove the
> setup works. Choose the Windows or macOS guide. If anything is blocked, save
> the exact error and bring it to the 4:30-5:30 PM Pacific Hangout Session for
> help. Never share a password.

## Submission Reminder

Classwork and homework must be submitted to:

1. Microsoft Teams
2. Ishwari Raut ma'am

## Closing Script

> A decision ladder is fair only when its rules are in the right order. Start
> at the top, stop at the first true branch, and test the boundaries. Next,
> your homework turns today's browser coding into a reusable local workspace.
