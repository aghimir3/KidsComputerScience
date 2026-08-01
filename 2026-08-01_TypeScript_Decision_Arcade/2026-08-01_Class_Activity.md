# Live Class Activity: TypeScript Decisions

**Date:** August 1, 2026  
**Tool:** https://www.typescriptlang.org/play/  
**New concept:** `else if`

## How We Will Work

Everyone follows the teacher in the TypeScript Playground. We will complete one
small change at a time instead of copying a large finished program.

For every exercise:

1. Read the rule together.
2. Predict the output.
3. Type the next small piece.
4. Press **Run**.
5. Compare the output with the prediction.
6. Explain which branch ran and why.

Use only concepts the class already knows, plus today's `else if`:

- `console.log`
- `let` and `const`
- `string`, `number`, and `boolean`
- Math and comparison operators
- `if`, `else if`, and `else`

Do not add functions, arrays, objects, loops, `switch`, logical operators, user
input, randomness, or libraries.

## Live Exercise 1: Recharge July Skills

Type this together:

```ts
const player: string = "Nova";
let coins: number = 7;
const hasKey: boolean = true;

coins = coins + 3;

console.log(`${player} has ${coins} coins.`);
console.log(coins >= 10);
console.log(hasKey);
```

Before pressing **Run**, answer:

- Which value changed?
- What number will `coins` contain?
- Which two lines produce booleans?
- What will each line print?

Then run the program and compare the result with the class prediction.

## Live Exercise 2: Review Two Paths

Replace the editor with:

```ts
const fuel: number = 60;

if (fuel >= 50) {
  console.log("Launch approved!");
} else {
  console.log("Refuel first.");
}
```

Predict, run, and explain the result for:

- `fuel = 60`
- `fuel = 49`

Class discussion:

- What question does the condition ask?
- Which branch runs when the answer is true?
- What is the job of `else`?

## Live Exercise 3: Build a Multi-Path Rank Ladder

Start with only the value:

```ts
let score: number = 82;
```

Add one branch at a time with the teacher.

### Step 1: Highest Rank

```ts
if (score >= 90) {
  console.log("Legendary");
}
```

### Step 2: Add Another Question

```ts
if (score >= 90) {
  console.log("Legendary");
} else if (score >= 70) {
  console.log("Hero");
}
```

### Step 3: Add a Third Question

```ts
if (score >= 90) {
  console.log("Legendary");
} else if (score >= 70) {
  console.log("Hero");
} else if (score >= 50) {
  console.log("Explorer");
}
```

### Step 4: Add the Fallback

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

After every step, pause and ask:

- Where does the computer begin?
- When does it move down?
- What makes the ladder stop?
- What values will reach the final `else`?

## Live Exercise 4: Boundary Testing

Change only the value of `score`. Predict every result before pressing **Run**.

| Score | Class prediction | Actual output |
|---:|---|---|
| 95 |  |  |
| 90 |  |  |
| 89 |  |  |
| 70 |  |  |
| 69 |  |  |
| 50 |  |  |
| 49 |  |  |

Explain why these pairs are useful:

- `90` and `89`
- `70` and `69`
- `50` and `49`

Main idea:

> Test the exact boundary and the number just below it.

## Live Exercise 5: Galactic Gatekeeper

Build this second ladder together from a blank Playground:

- `90` or more fuel: `Hyper Jump unlocked!`
- `60` or more fuel: `Moon Route unlocked!`
- `30` or more fuel: `Training Orbit unlocked!`
- Lower than `30`: `Recharge before launch.`

Start with:

```ts
let fuel: number = 68;
```

The completed program must use:

- One `if`
- Two `else if` branches
- One final `else`
- Conditions ordered from highest to lowest

Predict and test:

```text
95, 90, 89, 60, 59, 30, 29
```

Explain why `89` takes the Moon Route instead of Hyper Jump.

## Live Exercise 6: Dragon Training Arena

Build another decision ladder as a class, but let students call out each next
line before the teacher types it.

- `80` or more energy: `Sky Flame`
- `50` or more energy: `Fireball`
- `20` or more energy: `Smoke Puff`
- Lower than `20`: `Nap Time`

Requirements:

- Use a typed number named `dragonEnergy`.
- Use one `if`, two `else if` branches, and one `else`.
- Print a different message in every branch.
- Keep conditions ordered from highest to lowest.
- Predict and test `80`, `79`, `50`, `49`, `20`, and `19`.

After each test, ask one student to name the first true branch and explain why
the earlier branches were false.

## Live Exercise 7: AI Bug Hunt

An AI assistant suggested this program:

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

Complete the bug hunt as one class:

1. Predict what the program will print for `95`.
2. Run it.
3. Identify the first true condition.
4. Compare the result with the intended rank rules.
5. Reorder the conditions from highest to lowest.
6. Test `95`, `90`, `70`, `50`, and `49` again.

AI connection:

> Code can compile and run while still containing incorrect logic. Humans must
> test AI-written code before trusting it.

## If Time Permits: Create a Class Theme

Choose one theme together:

- Superhero power meter
- Pet robot mood
- Treasure-vault security level
- Sports tournament rank
- Reading challenge badge

As a class, decide:

1. The number variable
2. Three boundary values
3. Four output messages
4. The correct top-to-bottom order
5. At least six useful test values

Keep the program within today's concepts. Returning students may suggest better
messages, boundary tests, and explanations, but they should not add future
course concepts.

## Final Explain-It Check

Every student should be able to complete this sentence:

> An `else if` ladder checks __________, runs __________, and then __________.

A strong answer includes:

- top to bottom
- the first true branch
- stops or skips the remaining branches
