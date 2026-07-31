# Homework: TypeScript Decision Ladders

**Assigned:** August 1, 2026  
**Due:** August 8, 2026  
**Points:** 100 points + 5 bonus points

## Before You Begin

Use your local VS Code setup if it works. If installation is still blocked,
complete the same coding work at https://www.typescriptlang.org/play and attend
the 4:30-5:30 PM Pacific Hangout Session for help.

You should be able to complete every written question without live help.

## Part 1 - Setup Check (20 points)

Run these commands:

```text
node --version
npm --version
tsc --version
```

Record each version. If a command fails, record the exact error and the step you
will try next.

Explain the job of each tool:

- Visual Studio Code:
- TypeScript compiler (`tsc`):
- Node.js (`node`):

## Part 2 - Put the Workflow in Order (20 points)

Number these steps from 1 to 5:

- Run `node decisions.js`.
- Save `decisions.ts`.
- Read the terminal output.
- Run `tsc decisions.ts`.
- Type or change the TypeScript code.

Then complete the sentence:

```text
decisions.ts -> ______ -> decisions.js -> ______ -> output
```

## Part 3 - Predict the Branch (25 points)

Use this decision ladder:

```ts
let temperature: number = 72;

if (temperature >= 90) {
  console.log("Very hot");
} else if (temperature >= 70) {
  console.log("Warm");
} else if (temperature >= 50) {
  console.log("Cool");
} else {
  console.log("Cold");
}
```

Predict the output for each value without running it first:

- `95`:
- `90`:
- `72`:
- `70`:
- `50`:
- `49`:

Why are `90`, `70`, `50`, and `49` useful boundary tests?

## Part 4 - Build Your Own Program (25 points)

Create a new file named `homework-decisions.ts`. Build a program with:

- One typed variable
- One `if`
- At least two `else if` branches
- One final `else`
- A different message in every branch
- At least four test values

Ideas:

- Weather clothing adviser
- Game difficulty selector
- Reading-goal badge
- Character energy level
- Choose-your-own-adventure result

Write your final code and record four test values with their outputs.

If working locally, compile and run with:

```text
tsc homework-decisions.ts
node homework-decisions.js
```

## Part 5 - AI Reflection (10 points)

An AI assistant gives you code that compiles and runs. Does that prove the
logic is correct? Explain why or why not, and name two test values you would use
before trusting the result.

## Bonus - Improve the User Experience (5 points)

Use a template literal to include the tested value in the output message.

Example:

```ts
console.log(`A score of ${score} earns Hero rank!`);
```

## Submission

Submit your homework to:

1. Microsoft Teams
2. Ishwari Raut ma'am

Submit the completed homework plus your `.ts` code or a screenshot of the
Playground. Do not include passwords or private information.

