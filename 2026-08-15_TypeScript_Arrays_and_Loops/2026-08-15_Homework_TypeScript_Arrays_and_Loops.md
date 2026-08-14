# Homework: TypeScript Arrays and Loops

**Assigned:** August 15, 2026

**Due:** Before class on August 22, 2026

**Points:** 100 points + 5 bonus points

## Directions

No computer is required. Predict and explain the code on paper or in the
fillable PDF. You may run the examples afterward to check your thinking.

Use only arrays, indexes, `.length`, loops, decisions, and accumulators from
class. Do not use functions, objects, or new array methods.

## Part 1 - Match the Vocabulary (15 points)

Write the correct letter beside each term.

**Meanings**

- A. One variable that stores an ordered list of values
- B. One value inside an array
- C. The numbered address of an array item
- D. The number of items in an array
- E. A first index of `0` instead of `1`
- F. Asking for an index that is not inside the array

**Terms**

1. Array
2. Item
3. Index
4. Length
5. Zero-based
6. Out-of-range index

Then write one sentence explaining the difference between an item's position
in everyday speech and its index in TypeScript.

## Part 2 - Index and Length Practice (20 points)

Use this array for every question:

```ts
const snacks: string[] = ["apple", "popcorn", "yogurt", "pretzels"];
```

Answer:

1. What is `snacks.length`?
2. What is the first valid index?
3. What is the final valid index?
4. What value is stored at `snacks[0]`?
5. What value is stored at `snacks[2]`?
6. Write the code that prints `"pretzels"` using an index.
7. Write the code that finds the final item using `snacks.length`.
8. Write one line that changes `"popcorn"` to `"carrots"`.
9. What happens if the program asks for `snacks[4]`?
10. Explain why the length and final index are different.

## Part 3 - Predict the Output (20 points)

Write exactly what each program prints.

### Program A

```ts
const levels: number[] = [2, 4, 6];
console.log(levels[1]);
console.log(levels.length);
```

### Program B

```ts
const pets: string[] = ["cat", "dog", "fish"];

for (let i = 0; i < pets.length; i++) {
  console.log(`${i}: ${pets[i]}`);
}
```

### Program C

```ts
const numbers: number[] = [3, 5, 7];
let total: number = 0;

for (let i = 0; i < numbers.length; i++) {
  total = total + numbers[i];
}

console.log(total);
```

### Program D

```ts
const temperatures: number[] = [72, 85, 68];

for (let i = 0; i < temperatures.length; i++) {
  if (temperatures[i] >= 80) {
    console.log("Hot");
  } else {
    console.log("Mild");
  }
}
```

## Part 4 - Spot and Repair the Bugs (20 points)

Each program contains one important problem.

### Bug A

```ts
const games: string[] = ["Chess", "Soccer", "Tag"];

for (let i = 0; i <= games.length; i++) {
  console.log(games[i]);
}
```

Explain what goes wrong and rewrite the loop condition.

### Bug B

```ts
const points: number[] = [10, 20, 30];

for (let i = 0; i < points.length; i++) {
  let total: number = 0;
  total = total + points[i];
}

console.log(total);
```

Explain why the accumulator is in the wrong place and rewrite the program with
`total` in the correct scope.

## Part 5 - Design a List Program (15 points)

Design a small program using only concepts taught in class.

Your design must include:

- One typed array containing at least four values
- A correct loop using `.length`
- An index lookup inside the loop
- A template literal that prints the current item
- One sentence describing the expected output

Write the complete code. It is okay to write it on paper without running it.

## Part 6 - AI Data Reflection (10 points)

Imagine an AI image project has this list of labels:

```ts
const labels: string[] = ["tree", "unknown", "car", "tree", "unknown"];
```

Answer:

1. How many labels are stored?
2. Which indexes contain `"unknown"`?
3. Why should uncertain labels be flagged instead of silently trusted?
4. What can a loop do consistently that would be boring to repeat by hand?
5. What decision still requires a person after the program flags a label?

## Bonus - Extend and Predict (5 points)

Add one more label to the AI data array. Write the new array, its new length,
its final valid index, and the output line your added item should produce in a
correct loop.

## Submission

Submit your completed homework to:

1. Microsoft Teams
2. Ishwari Raut ma'am

Submit the completed PDF or clear written responses. If you include a code
screenshot, do not show passwords, private folders, or personal information.