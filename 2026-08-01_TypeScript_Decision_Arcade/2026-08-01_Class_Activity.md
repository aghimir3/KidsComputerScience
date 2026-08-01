# Instructor-Run Class Activity: TypeScript Decisions

**Date:** August 1, 2026

**Tool:** https://www.typescriptlang.org/play/

**New concept:** `else if`

**Format:** Instructor live-codes; students follow along

## How to Run This Activity

You drive the entire activity from your shared TypeScript Playground. Students
keep their own Playground open and type the same code as you.

This is not a team activity. Students do not need roles, separate missions, or
long discussions. Keep the flow moving:

1. Explain what you are about to type.
2. Type one small section while students follow.
3. Ask one short reinforcing question.
4. Run the code yourself.
5. Briefly explain the output.
6. Move to the next change.

Students may answer aloud or in chat. Accept short answers and continue once
the main idea is clear.

Use only concepts the class already knows, plus today's `else if`:

- `console.log`
- `let` and `const`
- `string`, `number`, and `boolean`
- Math and comparison operators
- `if`, `else if`, and `else`

Do not introduce functions, arrays, objects, loops, `switch`, logical
operators, user input, randomness, or libraries.

## Demo 1: Quick July Recap

### Say

> Let us warm up with values, types, one calculation, and two booleans.

### Type

```ts
const player: string = "Nova";
let coins: number = 7;
const hasKey: boolean = true;

coins = coins + 3;

console.log(`${player} has ${coins} coins.`);
console.log(coins >= 10);
console.log(hasKey);
```

### Ask while typing

- Which variable is allowed to change?
  **Expected:** `coins`, because it uses `let`.
- What value will `coins` contain after the calculation?
  **Expected:** `10`.
- What type of answer does `coins >= 10` produce?
  **Expected:** A boolean.

### Run and reinforce

Point out that the output contains one string followed by two boolean values.

## Demo 2: Review `if` and `else`

### Say

> We already know how a program chooses between two paths. The condition is a
> yes-or-no question.

### Replace the editor with

```ts
let fuel: number = 60;

if (fuel >= 50) {
  console.log("Launch approved!");
} else {
  console.log("Refuel first.");
}
```

### Ask before Run

- Is `fuel >= 50` true or false when fuel is `60`?
  **Expected:** True.
- Which message should print?
  **Expected:** `Launch approved!`

Run the program. Then change only the value to `49` and run it again.

### Ask after the second Run

- What is the job of `else`?
  **Expected:** It catches the values that did not pass the `if` condition.

## Demo 3: Build an `else if` Ladder

### Say

> `if` and `else` give us two paths. `else if` lets us ask another question
> when the earlier question was false.

Start with:

```ts
let score: number = 82;
```

Build the ladder one branch at a time. Pause briefly after each addition so
students can catch up.

### Add the first condition

```ts
if (score >= 90) {
  console.log("Legendary");
}
```

Ask: “Is 82 at least 90?”
**Expected:** No, so nothing prints yet.

### Add the first `else if`

```ts
if (score >= 90) {
  console.log("Legendary");
} else if (score >= 70) {
  console.log("Hero");
}
```

Ask: “Why does the computer check 70?”
**Expected:** The 90 condition was false.

### Add another `else if`

```ts
if (score >= 90) {
  console.log("Legendary");
} else if (score >= 70) {
  console.log("Hero");
} else if (score >= 50) {
  console.log("Explorer");
}
```

Ask: “Will the computer check 50 for score 82?”
**Expected:** No. The 70 branch is already true, so the ladder stops.

### Add the final fallback

```ts
if (score >= 90) {
  console.log("Legendary");
} else if (score >= 70) {
  console.log("Hero");
} else if (score >= 50) {
  console.log("Explorer");
} else {
  console.log("Keep training");
}
```

Ask: “Which scores reach the final `else`?”
**Expected:** Scores lower than 50.

### Reinforce before moving on

> The ladder checks from top to bottom. The first true branch runs, and then
> the ladder stops.

## Demo 4: Show Why Boundaries Matter

Keep the completed rank ladder on screen. Change only `score`, one value at a
time:

```text
95, 90, 89, 70, 69, 50, 49
```

Before each Run, state the value and give students a moment to predict. You
still control every edit and Run click.

Use these reinforcing questions:

- Why do 90 and 89 produce different results?
  **Expected:** 90 passes the first condition; 89 does not.
- Why do we test the exact boundary and the number just below it?
  **Expected:** The pair helps reveal mistakes in the threshold.
- How many branches print during one Run?
  **Expected:** One.

Main message:

> Boundary tests help prove that the code matches the written rules.

## Demo 5: Galactic Gatekeeper

### Say

> Now I will use the same decision pattern with a different theme. Watch how
> the structure stays the same while the values and messages change.

### Type

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

### Ask while demonstrating

- Why is the 90 condition above the 60 condition?
  **Expected:** The computer checks from the top, so the highest threshold
  must come first.
- Which route should fuel 68 choose?
  **Expected:** Moon Route.
- What happens when fuel is 29?
  **Expected:** The final `else` prints the recharge message.

Run `68`, `90`, `89`, `60`, `59`, `30`, and `29`. Students follow the value
changes on their own screens.

## Demo 6: AI Logic Bug

### Say

> An AI coding assistant can produce code that runs but still makes the wrong
> decision. We must test the logic ourselves.

### Type the AI draft

```ts
let score: number = 95;

if (score >= 50) {
  console.log("Explorer");
} else if (score >= 70) {
  console.log("Hero");
} else if (score >= 90) {
  console.log("Legendary");
} else {
  console.log("Keep training");
}
```

### Ask before Run

- What will the code actually print for 95?
  **Expected:** Explorer.
- What should it print according to the rank rules?
  **Expected:** Legendary.
- Why does the code stop too early?
  **Expected:** `score >= 50` is already true, so the first branch runs.

Run the incorrect version. Then move the thresholds into this order:

```text
90, 70, 50
```

Run it again and emphasize:

> “The program ran” and “the program is correct” are not the same claim.

## Optional Demo: Dragon Training Arena

Use this only if the main demos finish early. You still type and run the whole
program while students follow.

- `80` or more energy: `Sky Flame`
- `50` or more energy: `Fireball`
- `20` or more energy: `Smoke Puff`
- Lower than `20`: `Nap Time`

Use a typed number named `dragonEnergy` and the same `if` / `else if` / `else`
structure.

Ask:

- Which threshold belongs first?
- Which values would be useful boundary tests?
- What is the job of the final `else`?

Do not add new syntax. The point is repetition with a different theme.

## Closing Reinforcement

Ask these three questions without turning them into a long discussion:

1. In what direction does an `else if` ladder check?
   **Expected:** Top to bottom.
2. What happens after the first true condition?
   **Expected:** That branch runs and the ladder stops.
3. Why should we test AI-generated code?
   **Expected:** Code can run while still containing incorrect logic.
