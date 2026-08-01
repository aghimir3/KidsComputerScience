# Bonus Practice: Robot Repair Arcade

**Who should use this:** Returning students or anyone who finishes a class
mission early  
**Rule:** Practice more deeply without moving beyond the class

## Before the `else if` Lesson

Use only July concepts. Do not use `else if` until the teacher introduces it to
everyone.

### Repair 1: Type Trouble

This program should print `R0-B1 has 50 battery. Online: true`:

```ts
const robotName: string = 404;
const battery: number = 20;
battery = battery + 30;
let online: boolean = "true";

console.log(`${robotName} has ${battery} battery. Online: ${online}`);
```

Repair the three mistakes without removing the type annotations. Explain every
repair.

### Repair 2: Two-Path Energy Gate

```ts
let energy: number = 50;

if (energy >= 50) {
  console.log("Energy gate opened!");
} else {
  console.log("Recharge before entering.");
}
```

Predict and test `49`, `50`, and `100`. Explain why exactly one path runs.

## After the Teacher Introduces `else if`

Build the same Rank Engine as the class. Add more boundary tests, clearer
variable names, and more creative messages. Do not use functions, arrays,
loops, `switch`, logical operators, or any other future syntax.

## Finished Again?

- Predict two additional values before running.
- Break one familiar type on purpose and repair it.
- Explain every line to another student.
- Create a second theme using the same decision-ladder structure.

Depth, testing, and explanation are the challenge - not learning ahead.
