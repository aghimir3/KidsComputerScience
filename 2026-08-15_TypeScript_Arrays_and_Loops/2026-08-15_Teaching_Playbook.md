# August 15 Teaching Playbook: TypeScript Arrays and Loops

## Teaching Purpose

This lesson connects two ideas students already know:

- A variable stores a value.
- A loop repeats code.

The one new idea is that an array stores an ordered list of related values.
Students should leave with one dependable pattern:

```ts
const items: string[] = ["first", "second", "third"];

for (let i = 0; i < items.length; i++) {
  console.log(items[i]);
}
```

Depth matters more than reaching every example.

## What Students Already Know

Students have previously used:

- `let` and `const`
- `string`, `number`, and `boolean`
- Math and comparison operators
- Template literals
- `if`, `else if`, and `else`
- `for` and `while` loops
- Accumulators
- VS Code and Code Runner

Do not reteach all of these. Briefly recall them when they become useful.

## New Vocabulary

| Word | Student-friendly meaning |
|---|---|
| Array | One variable that stores an ordered list of values |
| Item | One value inside an array |
| Index | The numbered address of an item |
| Length | The number of items in an array |
| Zero-based | The first index is `0`, not `1` |

## Explanation Sequence

### 1. Begin with the problem

Three separate names require three variables and three print statements. Ask
students what would happen with 100 names. Then replace the separate variables
with one array.

### 2. Separate index from position

Students naturally call `players[1]` the first item because they see the number
one. Use precise language:

- Human position: first item
- Array index: `0`

Avoid saying only "the first one" when demonstrating code.

### 3. Connect `.length` to the loop boundary

Do not teach `.length` as an isolated fact. Show why it lets the same loop work
when the array gains or loses items.

```ts
for (let i = 0; i < players.length; i++) {
  console.log(players[i]);
}
```

The array has three items, so its length is `3`. Its valid indexes are `0`,
`1`, and `2`. When `i` becomes `3`, the condition is false and the loop stops.

### 4. Reuse old ideas inside the loop

Once students can print every item, add an `if` statement or accumulator. This
shows that arrays do not replace previous skills; they provide values for those
skills to process.

## Common Misconceptions

### "Index 1 means the first item"

Response: Point to the index row and ask which address is directly under the
first value. Have the student predict before running.

### "Length is the last index"

Response: Write both facts side by side:

```text
length = 3
last index = 2
```

Then state: last index equals `length - 1`.

### "The loop should use <= so it includes everything"

Response: Trace the final round. For a length of `3`, `i <= 3` permits index
`3`, which does not exist.

### "const means no array item can change"

Response: Keep this brief. `const` prevents assigning a different array to the
variable. It does not freeze each item. Demonstrate one direct index change and
move on.

### "undefined is another value we stored"

Response: Explain that it appears here because the program asked for an index
outside the list. Repair the boundary rather than exploring the full type.

## Questions That Reveal Understanding

Use these instead of asking only "Does that make sense?"

- If an array has six items, what is its length?
- If an array has six items, what is its last valid index?
- What value does `i` have during the first loop round?
- Why can `i` serve as an array index?
- What changes if we add another item to the array?
- Why is `.length` safer than typing a fixed number into the loop condition?
- What output would prove that our loop went one step too far?

## Live-Coding Habits

- Type one small change at a time.
- Ask for a prediction before each Run.
- Keep arrays to three to five values during explanations.
- Use names and values that fit on one line.
- Trace at least one complete loop on screen.
- Deliberately show one out-of-range index and repair it.
- Save before running so Code Runner uses the latest version.
- Keep the terminal visible when discussing output.

## Guided Project Checkpoints

### Checkpoint 1: The data exists

```ts
const labels: string[] = ["cat", "unknown", "dog", "unknown", "bird"];
```

Expected understanding: one typed array contains five strings.

### Checkpoint 2: Every item is visited

```ts
for (let i = 0; i < labels.length; i++) {
  console.log(labels[i]);
}
```

Expected understanding: the counter becomes the current index.

### Checkpoint 3: One item is inspected

```ts
const label: string = labels[i];

if (label === "unknown") {
  console.log("Needs human review");
}
```

Expected understanding: the decision runs once for each array item.

### Checkpoint 4: Results are counted

```ts
let reviewCount: number = 0;
```

Expected understanding: the accumulator starts outside the loop so it keeps
its value across all rounds.

## AI Discussion Guide

Keep the connection concrete and age-appropriate:

1. An AI model may learn from many labeled examples.
2. A label describes what an example is supposed to contain.
3. Some labels may be missing, uncertain, or incorrect.
4. A program can flag obvious problems such as `"unknown"`.
5. A human must still investigate and decide what is correct.

Avoid implying that a five-item TypeScript array trains a model. The activity
is a small simulation of reviewing data before or after AI processing.

## Expected Project Output

```text
Example 1: cat
Example 2 needs human review.
Example 3: dog
Example 4 needs human review.
Example 5: bird
2 examples need human review.
```

## Support Ladder

Give the smallest useful hint first:

1. Ask the student to point to the current index.
2. Ask what `items.length` equals.
3. Ask whether the condition is still true.
4. Show the index-and-value table.
5. Provide one missing line, not the complete program.
6. Pair the student with a classmate for a verbal trace.

## Fast Finisher Limits

Students may:

- Add more items of the same type.
- Change labels and messages.
- Count another familiar category.
- Use an existing `else if` ladder inside the loop.
- Create a trace table for their customized array.

Students may not add functions, objects, nested arrays, new array methods,
randomness, or input. Extra depth should reinforce the shared lesson rather
than create a separate advanced track.

## End-of-Class Evidence

Before students leave, verify that each student can show or explain:

- One typed array.
- One correct index lookup.
- One use of `.length`.
- One loop using `i < items.length`.
- The final AI review count.
- Why human review still matters.