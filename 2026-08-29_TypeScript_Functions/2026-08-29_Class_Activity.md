# Instructor-Guided Class Activity: TypeScript Functions

**Date:** August 29, 2026

**Tool:** VS Code with Node.js 24 or newer

**New concept:** Named functions with typed parameters

**Optional extension:** Returning one typed value

**Format:** Instructor demonstrates; students predict, type, call, run, and
explain

## Class Goal

Students will learn that a function gives a name to a group of instructions.
They will define a function once, call it more than once, and use typed
parameters to change what the function does each time.

Use only familiar ideas plus today's function ideas:

- `const` and `let`
- `string`, `number`, and `boolean`
- `console.log`
- Template literals
- `if`, `else if`, and `else`
- Typed arrays and counter-based `for` loops
- Named function declarations
- Function calls
- Typed parameters and arguments
- A typed `return` value only after the readiness gate

Do not introduce arrow functions, anonymous functions, callbacks, recursion,
objects, optional or default parameters, rest parameters, overloading,
`forEach`, `map`, `filter`, packages, or user input.

## Before Students Begin

Ask students to create a folder named `august-29-functions`. Inside it, create
a file named `functions.ts`.

Run this setup check:

```ts
console.log("Functions class ready!");
```

If local TypeScript does not run, pair the student with a classmate or use
https://www.typescriptlang.org/play/. Protect teaching time instead of turning
the lesson into a long setup repair.

## Readiness Gate: Can We Recognize Repeated Work?

Show this code:

```ts
console.log("Mission ready, Maya!");
console.log("Mission ready, Leo!");
console.log("Mission ready, Zara!");
```

Ask:

- What part repeats?
  **Expected:** The message and `console.log` structure.
- What part changes?
  **Expected:** The player's name.
- If we needed 30 names, what would become annoying or risky?
  **Expected:** Repeating and editing many nearly identical lines.

Say:

> Today we will give repeated instructions a name. Then we can run those
> instructions with a short function call.

## Demo 1: Define Once, Call Many Times

### Type the definition

```ts
function showMissionBriefing() {
  console.log("Check your tools.");
  console.log("Read the mission.");
  console.log("Ask questions before starting.");
}
```

Ask before running:

- What will print?
  **Expected:** Nothing yet.
- Why?
  **Expected:** The instructions were defined, but the function was not
  called.

### Add the calls

```ts
showMissionBriefing();
showMissionBriefing();
```

Run the program. Count two complete briefings.

Repeat this sentence:

> A definition teaches the program what the function means. A call tells the
> program to run it now.

## Demo 2: Read the Parts of a Function

Use this small example:

```ts
function cheer() {
  console.log("You can solve this!");
}

cheer();
```

Identify:

| Part | Meaning |
|---|---|
| `function` | Starts a function declaration |
| `cheer` | The function's name |
| `()` | The input area; empty for now |
| `{ }` | The function body containing instructions |
| `cheer()` | A function call |

Ask students to point to the definition and then the call.

## Demo 3: One Typed Parameter

Replace three repeated greetings with one reusable function:

```ts
function greetPlayer(name: string) {
  console.log(`Welcome, ${name}!`);
}

greetPlayer("Maya");
greetPlayer("Leo");
greetPlayer("Zara");
```

### Mental model

Draw three boxes:

```text
CALL                  PARAMETER BOX             OUTPUT
greetPlayer("Maya") -> name receives "Maya" -> Welcome, Maya!
```

Explain:

- `name` is the **parameter** in the function definition.
- `"Maya"` is the **argument** sent by this call.
- `: string` is a promise about the kind of value the function accepts.
- Each call gets a fresh value for `name`.

Ask students to predict the output before each new call.

## Demo 4: Two Parameters

```ts
function reportScore(player: string, score: number) {
  console.log(`${player} scored ${score} points.`);
}

reportScore("Maya", 92);
reportScore("Leo", 78);
```

Ask:

- Which argument goes into `player`?
  **Expected:** The first argument.
- Which argument goes into `score`?
  **Expected:** The second argument.
- Why would `reportScore(92, "Maya")` be rejected?
  **Expected:** The arguments are in the wrong order and do not match the
  parameter types.

Use the sentence:

> Arguments match parameters by position: first to first, second to second.

## Demo 5: Put an Old Decision Inside a New Function

```ts
function checkScore(score: number) {
  if (score >= 80) {
    console.log(`${score}: mission passed`);
  } else {
    console.log(`${score}: keep practicing`);
  }
}

checkScore(92);
checkScore(67);
```

Point out that `if/else` did not change. The function gives the familiar
decision a name and lets different calls send different scores.

Ask students to add `checkScore(80)` and predict the boundary result.

## Guided Project: AI Label Review Helper

### Introduce the connection

Say:

> An AI system can produce a label such as `cat`, `tree`, or `unknown`. Our
> function will apply the same review rule every time. It can flag uncertainty,
> but a person must inspect the example and decide what is correct.

Clarify that this is a rule-based review helper, not an AI model.

### Stage 1: Define the review function

```ts
function reviewLabel(label: string) {
  if (label === "unknown") {
    console.log("Human review needed.");
  } else {
    console.log(`${label}: label accepted for now.`);
  }
}
```

Pause. Ask what will print before any call is added.

### Stage 2: Call it with different arguments

```ts
reviewLabel("cat");
reviewLabel("unknown");
reviewLabel("tree");
```

Students predict all three output lines before running.

### Stage 3: Reuse it inside an array loop

```ts
const labels: string[] = ["cat", "unknown", "tree", "unknown"];

for (let i = 0; i < labels.length; i++) {
  reviewLabel(labels[i]);
}
```

Ask:

- What value becomes the argument on each round?
  **Expected:** The current array item, `labels[i]`.
- How many calls happen?
  **Expected:** Four.
- Which two calls request human review?
  **Expected:** The calls receiving `"unknown"`.

## Return-Value Readiness Gate

Do not continue until most students can:

1. Point to a function definition.
2. Point to a function call.
3. Match one argument to one parameter.
4. Predict two calls with different arguments.

If those answers are shaky, repeat parameter practice and skip this section.
That is a successful class, not unfinished teaching.

If students are ready, show:

```ts
function needsReview(label: string): boolean {
  if (label === "unknown") {
    return true;
  } else {
    return false;
  }
}

const result: boolean = needsReview("unknown");
console.log(result);
```

Explain:

- The parameter type says what goes **in**.
- The return type says what comes **out**.
- `return` sends one value back to the calling line.
- Returning a value and printing a value are different jobs.

### Optional extension: Count returned results

```ts
const labels: string[] = ["cat", "unknown", "tree", "unknown"];
let reviewCount: number = 0;

for (let i = 0; i < labels.length; i++) {
  if (needsReview(labels[i])) {
    reviewCount = reviewCount + 1;
  }
}

console.log(`${reviewCount} labels need human review.`);
```

## Common Mistakes to Demonstrate Safely

### Defined but never called

```ts
function celebrate() {
  console.log("Great work!");
}
```

### Missing argument

```ts
function greetPlayer(name: string) {
  console.log(`Hi, ${name}!`);
}

greetPlayer();
```

### Wrong argument type

```ts
greetPlayer(42);
```

### Reversed argument order

```ts
function reportScore(player: string, score: number) {
  console.log(`${player}: ${score}`);
}

reportScore(92, "Maya");
```

For every error, ask students to identify the contract the call failed to
follow.

## Quick Closing Check

Ask students to answer without running code:

1. What is the difference between defining and calling a function?
2. What is a parameter?
3. What is an argument?
4. Why does the order of two arguments matter?
5. How did the AI helper reuse one rule?
6. What decision still belongs to a person?

## Adaptive Pacing

- **Setup is slow:** Pair students or use the TypeScript Playground.
- **Calls are confusing:** Use only a no-parameter function and physically
  point from each call back to the definition.
- **Parameters are confusing:** Use one parameter and trace its value in a box.
- **The class is on pace:** Complete the AI helper with the array loop.
- **Students move quickly:** Use the return-value extension.
- **Students finish the extension:** Ask them to write `isPassing` or
  `isEven`, then explain the input and output types.
- **Time runs short:** Keep named functions and one typed parameter; skip
  return values and Kahoot before skipping guided practice.

## Final Message

> A function is a reusable named job. Define it once, call it when needed, and
> use parameters to give each call the information it needs.
