# Classwork: TypeScript Arrays and Loops

**Date:** August 15, 2026

**Points:** 100 points + 10 bonus points

**Tool:** VS Code with Node.js 24 or newer

## Important

Predict before pressing **Run**. Type each program yourself, save the file, and
compare the output with your prediction.

If VS Code is unavailable, use https://www.typescriptlang.org/play/ or work with
a partner. Do not include private information in code or screenshots.

## Part 1 - Loop Readiness Check (10 points)

Read this loop without running it:

```ts
for (let i = 0; i < 4; i++) {
  console.log(i);
}
```

Answer:

1. What value does `i` start with?
2. What four values print?
3. What check becomes false and stops the loop?
4. Why does `4` not print?

Then run the code and record whether your prediction matched.

## Part 2 - Build Typed Arrays (15 points)

Create both arrays:

```ts
const players: string[] = ["Maya", "Leo", "Zara"];
const scores: number[] = [78, 91, 84];
```

Answer:

1. What does `string[]` tell TypeScript?
2. What does `number[]` tell TypeScript?
3. How many variables store all six values?
4. Add one more player and one more score using the same array syntax.
5. Predict what happens if you place `"high"` inside `scores`.

Run `console.log(players)` and `console.log(scores)` to check both arrays.

## Part 3 - Index and Length Lab (20 points)

Use this array:

```ts
const colors: string[] = ["red", "green", "blue", "gold"];
```

Complete the table before running any code:

| Question | Prediction | Actual result |
|---|---|---|
| `colors[0]` | | |
| `colors[1]` | | |
| `colors[3]` | | |
| `colors.length` | | |
| `colors[colors.length - 1]` | | |

Then answer:

1. Why is the first item at index `0`?
2. What is the final valid index?
3. Why is the final index one less than the length?
4. Change `"green"` to `"lime"` using one index assignment.
5. What appears if you print `colors[4]`, and why?

## Part 4 - Trace an Array Loop (20 points)

Predict every round:

```ts
const planets: string[] = ["Mercury", "Venus", "Earth"];

for (let i = 0; i < planets.length; i++) {
  console.log(`Index ${i}: ${planets[i]}`);
}
```

Complete the trace:

| Round | `i` | Is `i < planets.length` true? | Output |
|---|---:|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| Stop check | | | |

Explain:

1. What are the two jobs of `i` in this program?
2. Why does the condition use `.length` instead of the number `3`?
3. What would need to change if a fourth planet were added?

Run the program after completing the trace.

## Part 5 - AI Training Data Checker (25 points)

AI systems often use collections of labeled examples. A human should review
labels that are missing or uncertain.

Build this program one section at a time:

```ts
const labels: string[] = ["cat", "unknown", "dog", "unknown", "bird"];
let reviewCount: number = 0;

for (let i = 0; i < labels.length; i++) {
  const label: string = labels[i];

  if (label === "unknown") {
    console.log(`Example ${i + 1} needs human review.`);
    reviewCount++;
  } else {
    console.log(`Example ${i + 1}: ${label}`);
  }
}

console.log(`${reviewCount} examples need human review.`);
```

Before running, predict:

- The five example lines
- The final review count
- Which array indexes contain `"unknown"`
- Which human-friendly example numbers need review

After running, answer:

1. Why is `reviewCount` created before the loop?
2. Why does the output use `i + 1` but the array lookup uses `i`?
3. Is this program an AI model? Explain what small AI-related job it simulates.
4. Why should a human inspect uncertain or automatically generated labels?

## Part 6 - Repair the Boundary Bug (10 points)

An AI coding assistant suggested this loop:

```ts
const missions: string[] = ["Map", "Build", "Test"];

for (let i = 0; i <= missions.length; i++) {
  console.log(missions[i]);
}
```

Answer:

1. What four indexes does the loop try?
2. Which index is outside the array?
3. What unexpected output appears?
4. Repair the condition by changing one character.
5. Why must a human test AI-generated code even when it runs?

## Bonus - Add Another Review Rule (10 points)

Customize the AI Training Data Checker without using new syntax:

- Use at least seven labels.
- Keep at least one `"unknown"` label.
- Add a second familiar category that should receive a special message.
- Count or clearly identify every item needing review.
- Provide a trace for two different rounds.
- Explain why your loop still stops at the correct boundary.

## Submission

Submit your completed classwork to:

1. Microsoft Teams
2. Ishwari Raut ma'am

Include the completed PDF or written responses plus your final code or a clear
screenshot of the code and terminal output. Do not include passwords, private
folders, or other personal information.