# Returning Students Activity: Robot Repair Arcade

**Date:** August 1, 2026  
**Use during:** VS Code, Node.js, and TypeScript setup time  
**Goal:** Strengthen July skills without moving ahead of the class

## Your Mission

The Robot Repair Arcade has five broken training stations. Repair the code,
test it carefully, and customize the arcade using only TypeScript ideas you
have already learned.

This is a practice lane, not the next lesson. Stop and rejoin the whole class
when the teacher says, **"All coders together."**

## Learning Boundary

You may use:

- `console.log`
- `let` and `const`
- `string`, `number`, and `boolean`
- Type annotations
- Template literals
- Math operators: `+`, `-`, `*`, `/`, and `%`
- Comparisons such as `===`, `!==`, `>`, `<`, `>=`, and `<=`
- One `if / else` decision at a time

Do not use today:

- `else if`
- Functions
- Arrays or objects
- Loops
- `switch`
- New libraries, extensions, or packages
- AI-generated replacement code

The challenge comes from predicting, debugging, testing, and explaining—not
from learning syntax before the rest of the class.

## Ready Check

Only enter the arcade if both commands work:

```text
node --version
tsc --version
```

If either command fails, join the teacher's setup lane. That is the correct
activity for you.

If both commands work:

1. Create a folder named `2026-08-01-robot-arcade`.
2. Open it in VS Code.
3. Create `robot-arcade.ts`.
4. After every change, save, compile, and run:

```text
tsc robot-arcade.ts
node robot-arcade.js
```

## Station 1: Build Your Robot Badge

Type this program:

```ts
const playerName: string = "Nova";
const robotName: string = "R0-B1";
let energy: number = 40;
const missionReady: boolean = true;

console.log(`${playerName} controls ${robotName}.`);
console.log(`Energy: ${energy}`);
console.log(`Mission ready: ${missionReady}`);
```

Before running it, predict all three output lines.

Then customize the player name, robot name, energy, and boolean. Run it again
and confirm that the output matches your prediction.

Checkpoint: identify one `string`, one `number`, one `boolean`, one `const`,
and one `let` in your program.

## Station 2: Recharge the Robot

Replace your file with:

```ts
let energy: number = 35;
const batteryPack: number = 20;

energy = energy + batteryPack;

console.log(`New energy: ${energy}`);
console.log(energy >= 50);
console.log(energy % 2 === 0);
```

Predict before running:

1. What is the new energy?
2. Does `energy >= 50` print `true` or `false`?
3. Does `energy % 2 === 0` print `true` or `false`?

Change only the two starting numbers and make:

- The final energy lower than `50`
- The final energy an odd number
- The final energy exactly `50`

Checkpoint: explain what `% 2 === 0` is checking.

## Station 3: Repair the Type Errors

The arcade computer says this program should print:

```text
R0-B1 has 50 battery.
Online: true
```

However, the program has three mistakes:

```ts
const robotName: string = 404;
const battery: number = 20;
battery = battery + 30;
let online: boolean = "true";

console.log(`${robotName} has ${battery} battery.`);
console.log(`Online: ${online}`);
```

Repair it without removing the type annotations.

For each repair, be ready to explain:

- What TypeScript expected
- What it received
- Why `let` or `const` was the correct choice

Checkpoint: the repaired program compiles and prints the two expected lines.

## Station 4: Program the Energy Gate

Type this two-path decision:

```ts
let energy: number = 50;

if (energy >= 50) {
  console.log("Energy gate opened!");
} else {
  console.log("Recharge before entering.");
}
```

Predict, compile, and run with:

- `49`
- `50`
- `100`

Then try this separate two-path decision:

```ts
const hasArcadePass: boolean = true;

if (hasArcadePass) {
  console.log("Welcome to the bonus room!");
} else {
  console.log("Find an arcade pass first.");
}
```

Run it once with `true` and once with `false`.

Checkpoint: explain why exactly one branch runs each time.

## Station 5: AI Logic Bug Hunt

An AI assistant produced code that compiles, but the messages are backward:

```ts
let coins: number = 3;

if (coins > 0) {
  console.log("Your pockets are empty.");
} else {
  console.log(`You have ${coins} coin(s)!`);
}
```

Complete the bug hunt:

1. Predict the output for `3`.
2. Run the program and compare the result with your prediction.
3. Repair the logic using the same `if / else` structure.
4. Test the repair with `0` and `3`.
5. Explain why "it compiled" did not mean "it was correct."

Checkpoint: both test values produce sensible messages.

## Final Remix: Design Your Own Arcade Machine

Choose one theme:

- Space rescue
- Dragon training
- Sports scoreboard
- Pet-care robot
- Treasure vault

Build a small program using only concepts from the Learning Boundary. It must
contain:

- One typed `string`
- One typed `number` that changes
- One typed `boolean`
- One math operator
- One comparison
- One `if / else`
- One template literal
- Two test runs with different results

Do not add `else if`. Save that discovery for the whole-class lesson.

## Share When the Class Rejoins

Be ready to share one of these—not all three:

- A TypeScript error you repaired
- A prediction that your test confirmed
- A program that compiled but still had incorrect logic

## Finished Early?

Improve the same program without adding syntax:

- Rename variables so their purpose is clearer.
- Make the printed messages more fun.
- Predict and record two more test values.
- Break one type on purpose, read the error, and repair it.
- Explain your program line by line to another returning student.

Do not begin `else if` early. Everyone will learn it together.
