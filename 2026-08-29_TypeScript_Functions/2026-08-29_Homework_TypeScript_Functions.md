# Homework: TypeScript Functions

**Assigned:** August 29, 2026
**Due:** Before class on September 5, 2026
**Points:** 100 points + 5 bonus points

You can complete the core homework without a computer. Read each definition
and call carefully. Predict first, then use one of these options to check your
work:

## Tool Options

### Option 1: VS Code (use this first)

You should already have VS Code and TypeScript set up. Open your
`august-29-functions` folder and use `functions.ts` to test your answers.

### Option 2: TypeScript website (backup)

If VS Code or TypeScript does not work on your computer, go to
https://www.typescriptlang.org/play/, clear the sample code, and test the same
programs there. You do not need to repair VS Code before finishing the
homework.

## Part 1: Match the Vocabulary - 15 points

Match each term to its meaning.

Terms:

1. Function
2. Definition
3. Call
4. Parameter
5. Argument
6. Return

Meanings:

A. A value sent into one function call
B. A reusable named job
C. A value sent back to the calling code
D. Code that describes the function and its body
E. A command that runs a function
F. A named input in the function definition

Then explain this difference in your own words:

> A parameter is __________, while an argument is __________.

## Part 2: Predict the Output - 20 points

### Program A

```ts
function beep() {
  console.log("Beep!");
}

beep();
beep();
```

1. Write the exact output.
2. How many calls are present?
3. What would print if both calls were removed?

### Program B

```ts
function showDouble(number: number) {
  console.log(number * 2);
}

showDouble(4);
showDouble(7);
showDouble(10);
```

4. Write the exact output.
5. What value does `number` hold during the second call?
6. Which part stays the same during all three calls?

## Part 3: Parameters and Arguments - 20 points

Study this function:

```ts
function describePet(name: string, age: number) {
  console.log(`${name} is ${age} years old.`);
}
```

1. Name the two parameters in order.
2. Give the type of each parameter.
3. Match the arguments in `describePet("Pixel", 3)` to their parameters.
4. Write two new valid calls.
5. Explain what is wrong with `describePet(3, "Pixel")`.
6. Explain what is wrong with `describePet("Pixel")`.
7. Predict the output of one valid call you wrote.

## Part 4: Finish the Functions - 20 points

Fill every blank.

### A. Greeting function

```ts
function greetStudent(____: string) {
  console.log(`Hello, ${____}!`);
}

greetStudent("Ari");
```

### B. Temperature decision

```ts
function checkTemperature(temperature: ____) {
  if (temperature >= 80) {
    console.log("Hot");
  } ____ {
    console.log("Mild");
  }
}

checkTemperature(____);
```

Choose an argument that prints `Mild`.

### C. Two typed inputs

Write a complete function named `showProduct` that accepts:

- `item: string`
- `price: number`

It should print a message such as `Notebook costs 4 dollars.` Call it twice
with valid arguments.

## Part 5: Find and Repair the Bugs - 15 points

### Bug A

```ts
function welcome(name: string) {
  console.log(`Welcome, ${name}!`);
}

welcome();
```

### Bug B

```ts
function showLevel(level: number) {
  console.log(`Level ${level}`);
}

showLevel("five");
```

### Bug C

```ts
function announceWinner(winner: string) {
  console.log(`${winner} wins!`);
}
```

For each bug:

1. Explain the problem.
2. Write a repaired call or missing call.
3. Predict the repaired output.

## Part 6: AI Review Reflection - 10 points

Study this helper:

```ts
function reviewLabel(label: string) {
  if (label === "unknown") {
    console.log("Human review needed.");
  } else {
    console.log(`${label}: accepted for now.`);
  }
}

reviewLabel("tree");
reviewLabel("unknown");
```

1. Predict both output lines.
2. What is the parameter?
3. What are the two arguments?
4. Why is the phrase `accepted for now` more accurate than `guaranteed
   correct`?
5. What should a person inspect when the helper flags `unknown`?

## Bonus: Return a Boolean - 5 bonus points

Complete this only if return values were introduced in class.

```ts
function isPassing(score: number): boolean {
  if (score >= 70) {
    return ____;
  } else {
    return ____;
  }
}
```

Predict the returned values for `isPassing(92)` and `isPassing(61)`. Then
explain why this function returns a value instead of only printing one.

## Submit

Send your completed homework only to the assistant teachers:

1. Ishwari Raut ma'am
2. Khushi ma'am

Do not post homework in Microsoft Teams.
