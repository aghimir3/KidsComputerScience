# August 29, 2026 - TypeScript Functions Teaching Playbook

## Purpose

This playbook supports live instruction for students ages 10-18. It prioritizes
understanding over coverage. The core success condition is that students can
define, call, and explain a named function with one typed parameter.

## The One Idea to Protect

> A function is a reusable named job.

Every example should strengthen that sentence. Syntax is secondary to the
mental model.

## Success Levels

### Core success

Students can:

- Find a function definition.
- Find a function call.
- Explain that defining does not run the body.
- Write and call a function with one typed parameter.
- Predict two calls with different arguments.

### Strong success

Students can also:

- Use two typed parameters in the correct order.
- Put an `if/else` inside a function.
- Call a function from an array loop.

### Extension success

Students can also:

- Explain input type versus return type.
- Return one `boolean`, `number`, or `string` value.
- Store or test the returned value.

Do not treat the extension as required for students who are still building the
core model.

## Vocabulary and Teacher Language

| Word | Student-friendly meaning | Sentence to repeat |
|---|---|---|
| Function | A reusable named job | "Define once, call many times." |
| Definition | The code that describes the job | "The definition teaches; it does not run yet." |
| Call | A command that runs the function | "Parentheses after the name make the call." |
| Parameter | A named input box in the definition | "The parameter receives a value." |
| Argument | A value sent by one call | "This call sends this argument." |
| Return | A value sent back to the caller | "Return sends a result back." |

Do not describe both parameters and arguments as "the value in parentheses."
That shortcut creates confusion later. Keep definition language and call
language distinct.

## Board Plan

Keep this visible:

```ts
function greetPlayer(name: string) {
  console.log(`Welcome, ${name}!`);
}

greetPlayer("Maya");
```

Label it with arrows:

```text
greetPlayer  -> function name
name         -> parameter
string       -> parameter type
"Maya"       -> argument
greetPlayer("Maya") -> call
```

Underneath, write:

```text
definition != call
parameter != argument
```

Explain that `!=` means "is not the same as" only if students already know
that operator. Otherwise use plain words.

## Live-Coding Routine

Use this cycle for every example:

1. **Question:** What job should the program perform?
2. **Define:** Type only the function definition.
3. **Predict:** Ask whether anything runs yet.
4. **Call:** Add one function call.
5. **Trace:** Write the current parameter value beside the code.
6. **Run:** Compare output with the prediction.
7. **Change:** Call it with a different argument.
8. **Explain:** Ask what stayed the same and what changed.

This routine prevents students from treating a function as a block to copy
without understanding.

## High-Value Questions

Ask questions that reveal the mental model:

- "If I delete every call, what output remains?"
- "How many calls do you see?"
- "How many times will the body run?"
- "What value does `name` hold during the second call?"
- "Which part is reusable?"
- "Which part changes from call to call?"
- "Why does TypeScript reject this argument?"
- "Could this function be called from inside a loop?"

Avoid questions answered only by reading punctuation, such as "What symbol
comes next?" unless a student is fixing one specific syntax error.

## Misconceptions and Responses

### "Writing the function runs it"

Response:

1. Run a file containing only the definition.
2. Observe no output.
3. Add one call and run again.
4. Add a second call and count two outputs.

### "Parameter and argument mean the same thing"

Response:

Draw a labeled box inside the definition and a value traveling from the call.
Say, "The box is the parameter. The traveling value is the argument."

### "The function remembers the last argument"

Response:

Trace three calls in separate rows. Show that each call starts a new run of the
body with its own current parameter value.

### "Arguments can go in any order"

Response:

Number parameters and arguments from left to right. Match first to first and
second to second. Use one `string` and one `number` so TypeScript makes the
mistake visible.

### "Printing and returning are the same"

Response:

Only address this after the readiness gate. Show that `console.log` displays a
message, while `return` lets another line store or test the result.

## Error-Reading Protocol

When TypeScript reports an error:

1. Read the first useful line together.
2. Locate the function call named in the message.
3. Count arguments and parameters.
4. Match each argument type to its parameter type.
5. Change one thing, then run again.

Do not immediately type the repair for the student. Ask which contract the call
failed to follow.

## AI Label Review Helper

### Why this project works

It reuses labels from the previous two lessons, so students can focus on
functions instead of learning a new problem domain. It also demonstrates that
one named rule can be applied consistently across many values.

### Core version

```ts
function reviewLabel(label: string) {
  if (label === "unknown") {
    console.log("Human review needed.");
  } else {
    console.log(`${label}: label accepted for now.`);
  }
}

const labels: string[] = ["cat", "unknown", "tree", "unknown"];

for (let i = 0; i < labels.length; i++) {
  reviewLabel(labels[i]);
}
```

### Discussion prompts

- What job has been given the name `reviewLabel`?
- Which value is the argument on each loop round?
- Does the function know whether a label is truly correct?
- What evidence would a human need to inspect?
- Why is "accepted for now" more accurate than "guaranteed correct"?

### Extension version

```ts
function needsReview(label: string): boolean {
  if (label === "unknown") {
    return true;
  } else {
    return false;
  }
}
```

Keep the explicit `if/else` for this first return example. The shorter
`return label === "unknown"` form is elegant but hides the new return path.

## Assistant-Teacher Look-Fors

Watch for students who:

- Define functions but never call them.
- Put quotation marks around a parameter name inside the body.
- Omit an argument or send the wrong type.
- Reverse two arguments.
- Place a call inside the function body by accident.
- Add a semicolon between the function header and body.
- Try to use a parameter outside the function.
- Copy the complete project without predicting any output.

Ask one diagnostic question before offering a correction.

## Fast-Finisher Path

Keep extensions inside the day's concept:

1. Add another valid label and predict the output.
2. Write `isPassing(score: number): boolean`.
3. Write `getDouble(number: number): number`.
4. Use an array loop to call one function for every item.
5. Explain the input and output contract in plain language.

Do not move fast finishers into arrow functions, callbacks, or array methods.

## Exit Evidence

Before students leave, collect three short responses:

1. A function is...
2. A parameter is..., while an argument is...
3. One reason to use a function is...

Use these responses to decide whether September 5 should deepen return values
or begin a small function-based project.

## Answer Expectations for the Core Examples

- A definition without a call prints nothing.
- Two calls run the body twice.
- `greetPlayer("Maya")` gives the parameter `name` the value `"Maya"`.
- `reportScore("Maya", 92)` matches `string` first and `number` second.
- `checkScore(80)` takes the passing branch because the comparison uses `>=`.
- The AI helper receives four arguments and flags two `"unknown"` labels.
- A human must inspect the original example before changing a label.
