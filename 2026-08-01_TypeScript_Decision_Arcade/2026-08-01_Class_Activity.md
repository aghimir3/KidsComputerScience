# Class Activity: TypeScript Decision Arcade

**Date:** August 1, 2026  
**Tool:** https://www.typescriptlang.org/play/  
**New concept:** `else if`

## Arcade Mission

Your team will build and test decision-powered mini games. Every round uses the
same six-step loop:

1. Read the rules.
2. Predict the output.
3. Type the code.
4. Press **Run**.
5. Compare the result with the prediction.
6. Repair or improve the program.

## Team Roles

- **Navigator:** reads the next rule and keeps the team on the current step.
- **Coder:** types while sharing their screen.
- **Tester:** chooses test values and records predictions.
- **Reporter:** explains which branch ran and why.

Rotate roles after each mission. Every student should type at least one mission
on their own computer.

## Arcade Rules

You may use only:

- `console.log`
- `let` and `const`
- `string`, `number`, and `boolean`
- Template literals
- Math and comparison operators
- `if`, `else if`, and `else`

Do not add functions, arrays, objects, loops, `switch`, logical operators, user
input, randomness, or libraries.

## Power-Up: Prediction Sprint

Predict all four lines before pressing **Run**:

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

Discuss:

- Which value changed?
- Which values stayed locked?
- Which two lines produce booleans?

## New Move: `else if`

`if / else` gives a program two paths. `else if` adds another question between
them.

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

The program checks from top to bottom. The first true branch runs, and then the
ladder stops.

## Mission 1: Galactic Gatekeeper

The space station assigns a travel route based on fuel:

- `90` or more: Hyper Jump
- `60` or more: Moon Route
- `30` or more: Training Orbit
- Lower than `30`: Recharge

Build the program:

```ts
let fuel: number = 68;

if (fuel >= 90) {
  console.log("Hyper Jump unlocked!");
} else if (fuel >= 60) {
  console.log("Moon Route unlocked!");
} else if (fuel >= 30) {
  console.log("Training Orbit unlocked!");
} else {
  console.log("Recharge before launch.");
}
```

Predict and test:

```text
95, 90, 89, 60, 59, 30, 29
```

Reporter question: Why does `89` take the Moon Route instead of Hyper Jump?

## Mission 2: Dragon Training Arena

Create a dragon-energy ladder:

- `80` or more: Sky Flame
- `50` or more: Fireball
- `20` or more: Smoke Puff
- Lower than `20`: Nap Time

Requirements:

- Use a typed number named `dragonEnergy`.
- Use one `if`, two `else if` branches, and one `else`.
- Print a different message in every branch.
- Predict and test `80`, `79`, `50`, `49`, `20`, and `19`.

Reporter question: Which test values sit directly on a boundary?

## Mission 3: AI Bug Bounty

An AI assistant wrote this score ladder:

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

Complete the bug bounty:

1. Predict the output for `95`.
2. Run the code.
3. Circle or name the first true condition.
4. Explain why the program never reaches Legend.
5. Reorder the conditions.
6. Test `95`, `90`, `70`, `50`, and `49`.

Main takeaway:

> Code can compile and run while still having incorrect logic. Humans must test
> AI-written code.

## Mission 4: Build Your Own Decision Game

Choose a theme:

- Superhero power meter
- Pet robot mood
- Treasure-vault security level
- Sports tournament rank
- Weather adventure
- Reading challenge badge

Your program must include:

- One typed number
- One `if`
- At least two `else if` branches
- One final `else`
- A different message in every branch
- Conditions ordered from highest to lowest
- At least six test values, including exact boundaries and values just below
  them

## Arcade Showcase

Each team shares:

1. The theme and rules
2. One boundary value
3. The first true branch for that value
4. One bug the team prevented or repaired

## AI Discussion

Discuss:

- What part of a decision game could an AI assistant draft quickly?
- What test values should a human still choose?
- Why is "the program ran" not enough evidence that the rules are correct?
