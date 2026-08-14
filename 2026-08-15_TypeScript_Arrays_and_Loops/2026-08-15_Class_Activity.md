# Instructor-Guided Class Activity: TypeScript Arrays and Loops

**Date:** August 15, 2026

**Tool:** VS Code with Node.js 24 or newer

**New concept:** Typed arrays

**Format:** Instructor demonstrates; students predict, type, run, and explain

## Class Goal

Students will learn that an array stores an ordered list of related values.
They will access values by index and use one familiar `for` loop to process
every item in the list.

Use only concepts students already know, plus today's array ideas:

- `const` and `let`
- `string`, `number`, and `boolean`
- `console.log`
- Template literals
- `if`, `else if`, and `else`
- `for` loops and accumulators
- Typed arrays such as `string[]` and `number[]`
- Indexes, `.length`, and changing one item by index

Do not introduce functions, objects, nested arrays, `forEach`, `map`, `filter`,
`push`, user input, randomness, or packages.

## Before Students Begin

Ask students to create a folder named `august-15-arrays`. Inside it, create a
file named `arrays.ts`.

Run this setup check:

```ts
console.log("Arrays class ready!");
```

If local TypeScript does not run, pair the student with a classmate or use
https://www.typescriptlang.org/play/. Do not spend the full class repairing one
computer.

## Readiness Gate: Can We Still Trace a Loop?

### Type

```ts
for (let i = 0; i < 4; i++) {
  console.log(i);
}
```

### Ask before Run

- What value does `i` start with?
  **Expected:** `0`.
- What values will print?
  **Expected:** `0`, `1`, `2`, `3`.
- Why does `4` not print?
  **Expected:** `4 < 4` is false.

### Decide

If most students can trace the loop, continue to arrays. If several students
cannot, repeat the trace with `i < 3` and draw each round before continuing.
Do not rush into arrays until students can explain why the loop stops.

## Demo 1: Why Use an Array?

### Say

> We can store one value in one variable. What if the values belong together,
> like a team roster or a list of scores? An array keeps an ordered list in one
> variable.

### Show the repeated-variable version

```ts
const player1: string = "Maya";
const player2: string = "Leo";
const player3: string = "Zara";

console.log(player1);
console.log(player2);
console.log(player3);
```

### Replace it with one array

```ts
const players: string[] = ["Maya", "Leo", "Zara"];

console.log(players);
```

### Reinforce

- `string[]` means an array whose items must be strings.
- Square brackets around the values create the list.
- Commas separate the items.
- The order is preserved.

Ask: "How many variables hold all three names now?"
**Expected:** One variable, `players`.

## Demo 2: Indexes Start at Zero

### Type

```ts
const players: string[] = ["Maya", "Leo", "Zara"];

console.log(players[0]);
console.log(players[1]);
console.log(players[2]);
```

Draw this model:

| Index | 0 | 1 | 2 |
|---|---|---|---|
| Value | Maya | Leo | Zara |

### Ask before Run

- Which index stores `Maya`?
  **Expected:** `0`.
- What does `players[2]` mean?
  **Expected:** The item at index `2`, which is `Zara`.
- Is index `3` part of this three-item array?
  **Expected:** No. The final valid index is `2`.

### Test one mistake safely

```ts
console.log(players[3]);
```

Run it and identify `undefined` as "there is no item at that index." Do not
turn this into a deeper lesson about `undefined` types.

## Demo 3: `.length` Counts Items

### Type

```ts
const players: string[] = ["Maya", "Leo", "Zara"];

console.log(players.length);
console.log(players[players.length - 1]);
```

### Ask

- What does `.length` report?
  **Expected:** `3`.
- Why is the last index `length - 1`?
  **Expected:** Counting starts at index `0`.

Use this sentence repeatedly:

> Length is the number of items. The last index is one less than the length.

## Demo 4: Change One Item

### Type

```ts
const scores: number[] = [70, 82, 91];

scores[1] = 88;

console.log(scores);
```

### Ask

- Which score changed?
  **Expected:** The second score, at index `1`.
- Why can the contents change even though the array uses `const`?
  **Expected:** The variable still points to the same array; one item inside it
  changed.

Keep this explanation brief. The goal is using the array, not studying object
identity.

## Demo 5: Loop Through Every Item

### Start with the familiar loop shape

```ts
const players: string[] = ["Maya", "Leo", "Zara"];

for (let i = 0; i < players.length; i++) {
  console.log(players[i]);
}
```

### Trace together

| Round | `i` | Check | `players[i]` |
|---|---:|---|---|
| 1 | 0 | `0 < 3` is true | Maya |
| 2 | 1 | `1 < 3` is true | Leo |
| 3 | 2 | `2 < 3` is true | Zara |
| Stop | 3 | `3 < 3` is false | Nothing |

### Reinforce

The counter has two jobs:

1. It tracks the current round.
2. It becomes the index for the current array item.

Ask why the condition uses `<` instead of `<=`.
**Expected:** `players.length` is `3`, but index `3` does not exist.

## Demo 6: Combine Arrays, Loops, and Decisions

### Type

```ts
const scores: number[] = [95, 68, 82, 49];

for (let i = 0; i < scores.length; i++) {
  const score: number = scores[i];

  if (score >= 70) {
    console.log(`${score}: mission passed`);
  } else {
    console.log(`${score}: keep training`);
  }
}
```

### Ask before Run

- How many rounds will run?
  **Expected:** Four.
- Which scores pass?
  **Expected:** `95` and `82`.
- What is the job of `scores[i]`?
  **Expected:** It gets the current item.

## Guided Project: AI Training Data Checker

### Introduce the connection

> An AI system learns from many examples. Those examples are often stored in
> large collections. If a label is missing or uncertain, a human should review
> it instead of pretending it is correct.

Clarify that this program is not an AI model. It simulates one small job a
person might do while checking data used with AI.

### Stage 1: Store the labels

```ts
const labels: string[] = ["cat", "unknown", "dog", "unknown", "bird"];
```

Ask students to predict `labels.length` and the value at `labels[2]`.

### Stage 2: Visit every label

```ts
const labels: string[] = ["cat", "unknown", "dog", "unknown", "bird"];

for (let i = 0; i < labels.length; i++) {
  console.log(`Example ${i + 1}: ${labels[i]}`);
}
```

Explain that `i + 1` creates a human-friendly example number while `i` remains
the correct array index.

### Stage 3: Find labels needing review

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

### Predict before Run

- How many examples need review?
  **Expected:** Two.
- Which example numbers need review?
  **Expected:** Examples `2` and `4`.
- Why is `reviewCount` created before the loop?
  **Expected:** It must keep its total across every round.

### Student customization

Students may replace the five labels with their own five safe categories. They
must keep at least one `"unknown"` value so the review branch can be tested.

## AI Logic Check

Show this incorrect loop:

```ts
const labels: string[] = ["cat", "unknown", "dog"];

for (let i = 0; i <= labels.length; i++) {
  console.log(labels[i]);
}
```

Ask:

- What extra index does the loop try?
  **Expected:** Index `3`.
- What appears after `dog`?
  **Expected:** `undefined`.
- What one-character repair is needed?
  **Expected:** Change `<=` to `<`.
- Could AI-generated code contain this mistake even if it runs?
  **Expected:** Yes. A human must test the boundary and inspect the output.

## Closing Check

Ask students to answer aloud or in chat:

1. What does an array store?
   **Expected:** An ordered list of related values.
2. What is the first array index?
   **Expected:** `0`.
3. For four items, what is the final valid index?
   **Expected:** `3`.
4. What does `.length` report?
   **Expected:** The number of items.
5. Why does an array loop usually use `i < items.length`?
   **Expected:** The index equal to the length is outside the array.
6. Why might AI training data need human review?
   **Expected:** Labels can be missing, uncertain, or incorrect.

## Fast Finisher Boundary

Fast finishers may:

- Add more values of the same type to an existing array.
- Change the messages printed by the loop.
- Add another `if` or `else if` branch using concepts already taught.
- Trace the final program in a table.

They may not use functions, objects, nested arrays, or new array methods. The
goal is deeper practice with today's one array-and-loop pattern.