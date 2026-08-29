# Classwork: TypeScript Functions

**Date:** August 29, 2026
**Points:** 100 points + 10 bonus points
**Tool:** VS Code first; TypeScript Playground as a backup

## Goal

Learn to define a reusable function, call it, and send typed values into its
parameters. Predict before you run each program.

## Setup

### Option 1: VS Code (use this first)

You should already have VS Code and TypeScript set up. Create a folder named
`august-29-functions`. Open it in VS Code, then create `functions.ts`.

Test the file:

```ts
console.log("Functions class ready!");
```

### Option 2: TypeScript website (backup)

If VS Code or TypeScript does not work on your computer, do not stop the
classwork. Go to https://www.typescriptlang.org/play/, clear the sample code,
and type the same programs there. Click **Run** to test each program.

## Part 1: Definition or Call? - 10 points

Study this program:

```ts
function celebrate() {
  console.log("Mission complete!");
}

celebrate();
celebrate();
```

1. Copy the complete function definition.
2. Copy one function call.
3. How many times will `Mission complete!` print?
4. What would print if both calls were deleted?
5. Explain the difference between defining and calling a function.

## Part 2: Define Once, Call Many Times - 15 points

Type this function:

```ts
function showWarmUp() {
  console.log("Open your file.");
  console.log("Read the goal.");
  console.log("Predict before running.");
}
```

1. Predict what prints before adding a call.
2. Call `showWarmUp` once and record the output.
3. Call it two more times.
4. How many times did the function body run in total?
5. Why is the function easier to reuse than copying all three output lines?

## Part 3: Parameters and Arguments - 20 points

Type and run:

```ts
function greetPlayer(name: string) {
  console.log(`Welcome, ${name}!`);
}

greetPlayer("Maya");
greetPlayer("Leo");
```

1. What is the function's name?
2. What is the parameter's name and type?
3. What argument is sent by the first call?
4. What value does `name` hold during the second call?
5. Write a third call using your name.
6. Predict what TypeScript reports for `greetPlayer(42)` and explain why.

Now type:

```ts
function reportScore(player: string, score: number) {
  console.log(`${player} scored ${score} points.`);
}

reportScore("Zara", 95);
```

7. Match each argument to its parameter.
8. Write a second valid call.
9. Explain why `reportScore(95, "Zara")` does not follow the function's
   contract.

## Part 4: Put a Decision Inside a Function - 20 points

Type this program:

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
checkScore(80);
```

1. Predict the three output lines.
2. Run the program and compare the result with your prediction.
3. Why does `80` pass?
4. What old programming idea is reused inside the new function?
5. Add a call that takes the `else` branch.
6. Change the passing boundary to `70`, then predict all four calls again.

## Part 5: AI Label Review Helper - 25 points

This program applies one review rule to several possible AI labels. It is a
rule-based helper, not an AI model.

### Step A: Define the reusable rule

```ts
function reviewLabel(label: string) {
  if (label === "unknown") {
    console.log("Human review needed.");
  } else {
    console.log(`${label}: label accepted for now.`);
  }
}
```

1. What prints before the function is called? Explain.

### Step B: Send three arguments

```ts
reviewLabel("cat");
reviewLabel("unknown");
reviewLabel("tree");
```

2. Predict and record all three output lines.
3. Which argument causes a human-review message?

### Step C: Reuse the function in a loop

```ts
const labels: string[] = ["cat", "unknown", "tree", "unknown"];

for (let i = 0; i < labels.length; i++) {
  reviewLabel(labels[i]);
}
```

4. How many times is `reviewLabel` called?
5. What is the argument during each loop round?
6. Predict all output lines.
7. Add one known label and one `"unknown"` label. Predict the new output.
8. Why must a person inspect the original example before changing its label?

## Part 6: Repair the Function Bugs - 10 points

Each program has a different problem. Explain and repair both.

### Bug A: Never called

```ts
function showReady() {
  console.log("Ready!");
}
```

### Bug B: Arguments in the wrong order

```ts
function showItem(item: string, quantity: number) {
  console.log(`${quantity} ${item}`);
}

showItem(3, "notebooks");
```

For each bug:

1. Explain why the program does not behave as intended.
2. Write the smallest correct change.
3. Predict the repaired output.

## Bonus: Return a Result - 10 bonus points

Complete this only after the teacher introduces return values.

```ts
function needsReview(label: string): boolean {
  if (label === "unknown") {
    return true;
  } else {
    return false;
  }
}
```

1. Predict `needsReview("unknown")` and `needsReview("cat")`.
2. Store one returned result in a typed variable and print it.
3. Explain the difference between printing and returning.
4. Write `isPassing(score: number): boolean` using a passing score of `70`.

## Submit

Send your completed classwork to both assistant teachers:

1. Ishwari Raut ma'am
2. Khushi ma'am

You may also post it in Microsoft Teams as a reply to the classwork post.
