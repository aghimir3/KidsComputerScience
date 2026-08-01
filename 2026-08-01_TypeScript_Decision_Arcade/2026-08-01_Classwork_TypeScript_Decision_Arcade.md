# Classwork: TypeScript Decision Arcade

**Date:** August 1, 2026  
**Points:** 100 points + 10 bonus points  
**Tool:** https://www.typescriptlang.org/play/

## Important

Predict before pressing **Run**. Type the code yourself, test several values,
and explain why each branch runs.

Do not include private information in your code or screenshots.

## Part 1 - Prediction Power-Up (15 points)

Read this code without running it:

```ts
const player: string = "Nova";
let coins: number = 7;
const hasKey: boolean = true;

coins = coins + 3;

console.log(`${player} has ${coins} coins.`);
console.log(coins > 5);
console.log(coins % 2 === 0);
console.log(hasKey);
```

Write your prediction for all four output lines. Then run the program and
record whether your prediction matched.

Identify:

- One `string`
- One `number`
- One `boolean`
- The variable that changed

## Part 2 - Trace `if / else` (15 points)

Use this program:

```ts
let energy: number = 50;

if (energy >= 50) {
  console.log("Energy gate opened!");
} else {
  console.log("Recharge before entering.");
}
```

Predict the output for:

- `49`
- `50`
- `100`

Explain why exactly one branch runs for each value.

## Part 3 - Build a Rank Engine (20 points)

Type and run:

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

In your own words, explain:

1. When is the first `else if` checked?
2. What does "the first true branch wins" mean?
3. Why should the score conditions go from highest to lowest?

## Part 4 - Boundary Boss Battle (15 points)

Predict first, then test the Rank Engine with:

```text
95, 90, 89, 70, 69, 50, 49
```

Record the output for every value.

Answer:

- Which values are exact boundaries?
- Which values are just below a boundary?
- Why is testing only `82` not enough?

## Part 5 - AI Bug Bounty (15 points)

An AI assistant wrote:

```ts
let score: number = 95;

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

Answer:

1. What do you predict for `95`?
2. Which condition becomes true first?
3. Why does the program stop at the wrong rank?
4. Rewrite the conditions in the correct order.
5. Name three test values that help prove the repair works.
6. Why must humans test AI-written code even when it runs?

## Part 6 - Design Your Own Decision Game (20 points)

Choose a theme and create a decision ladder with:

- One typed number
- One `if`
- At least two `else if` branches
- One final `else`
- Conditions ordered from highest to lowest
- A different message in every branch
- At least six test values

Ideas:

- Superhero power meter
- Pet robot mood
- Treasure-vault security level
- Sports tournament rank
- Weather adventure
- Reading challenge badge

Write your final code and record the six test values with their outputs.

## Bonus - Become the Test Designer (10 points)

Add one more branch to your decision game without using any new syntax.

Provide:

- The new condition and message
- Two values that should reach the new branch
- One nearby value that should reach a different branch
- A short explanation of why the order is correct

## Submission

Submit your completed classwork to:

1. Microsoft Teams
2. Ishwari Raut ma'am

Include the completed PDF or written responses plus your final code or a clear
Playground screenshot. Do not include passwords or private information.
