# August 15, 2026 - Teacher Run of Show

## Class Goal

Students will learn one new programming concept: a typed array stores an
ordered list of related values. They will access items by zero-based index and
reuse last week's `for` loop to process every item.

## Learning Objectives

By the end of class, students should be able to:

- Create a `string[]` or `number[]` array.
- Explain that array indexes begin at `0`.
- Read and change one item using its index.
- Use `.length` to count array items.
- Trace `for (let i = 0; i < items.length; i++)`.
- Explain why `i <= items.length` goes one step too far.
- Combine an array, loop, decision, and accumulator.
- Explain why uncertain AI data labels need human review.

## Before Class

- Open the presentation, class activity, classwork PDF, and teacher playbook.
- Test VS Code, Code Runner, and Node.js 24 or newer on the demo computer.
- Create and run an `arrays.ts` file before students arrive.
- Post the classwork PDF in Microsoft Teams.
- Keep https://www.typescriptlang.org/play/ available as the fallback.
- Have students pair up if one computer cannot run TypeScript locally.
- Prepare the Kahoot, but use a verbal recap if students need more coding time.
- Ask assistant teachers to watch for `<=` in array loops and index confusion.

## Content Boundary

The only new programming concept is typed arrays.

Use:

- `string[]` and `number[]`
- Square-bracket indexes
- `.length`
- Direct assignment such as `scores[1] = 88`
- The familiar counter-based `for` loop

Do not introduce:

- Functions
- Objects
- Nested arrays
- `forEach`, `map`, `filter`, or other array methods
- `push`, `pop`, `shift`, or `unshift`
- `for...of`
- User input, randomness, libraries, or packages

## Flexible Schedule

| Time | Activity | Teacher focus |
|---|---|---|
| 9:00-9:15 | Welcome and homework review | Ask students to explain one loop rule from the August 8 homework. |
| 9:15-9:30 | VS Code check | Create `arrays.ts`; pair students or use the Playground if setup fails. |
| 9:30-9:50 | Loop readiness gate | Trace `i = 0; i < 4; i++` before introducing arrays. |
| 9:50-10:10 | Array mental model | Show one ordered row of values with index labels underneath. |
| 10:10-10:30 | Index and length practice | Predict `items[0]`, `items[2]`, and `items.length`. |
| 10:30-11:00 | Break | Fixed block. |
| 11:00-11:30 | Typing practice | Fixed block. |
| 11:30-11:50 | Loop through an array | Build the loop one piece at a time and trace every round. |
| 11:50-12:10 | Decisions and accumulators | Process scores and count matching items. |
| 12:10-12:40 | AI Training Data Checker | Build, predict, run, and customize the guided project. |
| 12:40-12:50 | Classwork completion | Students finish explanations and submit evidence. |
| 12:50-1:00 | Kahoot or verbal recap | Reinforce indexes, `.length`, and human review of AI data. |

Only break and typing practice are fixed. Slow down when students confuse an
item's human position with its array index.

## Opening Script

> Last week, a loop helped one block of code repeat. Today we give that loop a
> list to work through. An array stores the list, and the loop visits one item
> at a time.

## Loop Readiness Gate

Show:

```ts
for (let i = 0; i < 4; i++) {
  console.log(i);
}
```

Ask:

1. Where does `i` start?
2. What four values print?
3. Why does the loop stop before `4`?

If most students answer correctly, continue. If not, trace each round on the
screen and repeat with `i < 3`. The array lesson depends on this exact loop
idea, so this review is part of the lesson rather than lost time.

## Core Mental Model

Draw an ordered row:

| Index | 0 | 1 | 2 |
|---|---|---|---|
| Value | Maya | Leo | Zara |

Say:

> The value is the item we stored. The index is its numbered address. Arrays
> begin at index zero, so three items use indexes zero, one, and two.

Repeat throughout class:

> Length is the number of items. The last index is one less than the length.

## Guided Coding Sequence

Build in this order:

1. One `string[]` array.
2. Print the whole array.
3. Print individual indexes.
4. Print `.length`.
5. Change one item by index.
6. Loop through every item.
7. Put an `if` statement inside the loop.
8. Add an accumulator outside the loop.

Do not paste the finished project at once. Each step should answer one small
question before the next line is added.

## AI Connection

Use this wording:

> AI systems learn from collections of examples. Each example may have a label
> such as `cat` or `dog`. Real datasets can contain missing, uncertain, or wrong
> labels. Our program is not an AI model; it simulates a human review step that
> finds labels marked `unknown`.

Emphasize:

- A large collection can be represented as data that a program processes.
- Repetition helps inspect every example consistently.
- Automatic checks can find possible problems.
- A human remains responsible for deciding whether a label is correct.

## Adaptive Pacing

- **Setup takes too long:** pair students and use the TypeScript Playground.
- **Loops are shaky:** use only three-item arrays and trace on paper.
- **Indexes are confusing:** label physical cards `0`, `1`, and `2`.
- **Students are on pace:** complete the AI checker with five labels.
- **Students move quickly:** add more values and one additional familiar `if`
  branch; do not introduce new array methods.
- **Activities run long:** skip Kahoot and use the six closing questions from
  the class activity.

## Homework Transition

Say:

> Homework checks whether you can read arrays and loops without guessing. You
> can complete it on paper or in the fillable PDF. Predict first, then use VS
> Code only if you want to check your work.

Homework is due before class on Saturday, August 22, 2026.

## Submission Reminder

Classwork and homework must be submitted to:

1. Microsoft Teams
2. Ishwari Raut ma'am

## Closing Script

> An array keeps related values in order. An index chooses one item, `.length`
> counts all items, and a loop lets us visit the complete list without writing
> the same code again and again.