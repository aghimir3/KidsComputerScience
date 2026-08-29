# August 29, 2026 - Teacher Run of Show

## Class Goal

Students will learn one central programming idea: a function is a reusable
named job. They will define and call named functions, then use typed parameters
to send different values into the same instructions.

Returning a value is a readiness-gated extension. A class that finishes with
confident function calls and parameters has met the core goal.

## Learning Objectives

By the end of class, students should be able to:

- Explain why programmers place repeated instructions in a function.
- Distinguish a function definition from a function call.
- Define and call a named function.
- Identify a function name, parameter list, and body.
- Match arguments to typed parameters by position.
- Put a familiar `if/else` decision inside a function.
- Reuse a function while looping through an array.
- Explain why an AI review helper can flag uncertainty but cannot replace
  human judgment.
- If ready, explain that `return` sends one typed value back to the caller.

## Before Class

- Open the presentation, class activity, classwork PDF, and teaching playbook.
- Test VS Code, TypeScript, and Node.js 24 or newer on the demo computer.
- Create and run a `functions.ts` file before students arrive.
- Run every instructor demonstration and guided activity in VS Code.
- Keep https://www.typescriptlang.org/play/ available only as a fallback for
  an individual student whose local setup fails.
- Post the classwork PDF in Microsoft Teams.
- Prepare the Kahoot, but protect coding time if students need more practice.
- Ask assistant teachers to watch for missing calls, missing arguments, and
  reversed argument order.

## Content Boundary

The new core ideas are:

- Named function declarations
- Function calls
- Typed parameters
- Arguments matched by position

Use familiar `console.log`, template literals, `if/else`, arrays, and loops
inside functions.

Treat typed return values as an extension after the readiness gate.

Do not introduce:

- Arrow or anonymous functions
- Callbacks or higher-order functions
- Recursion
- Objects or classes
- Optional, default, or rest parameters
- Function overloading
- Deep scope rules or hoisting
- `forEach`, `map`, `filter`, packages, or user input

## Flexible Schedule

| Time | Activity | Teacher focus |
|---|---|---|
| 9:00-9:15 | Welcome and homework review | Ask students to explain one of the four array moves. |
| 9:15-9:30 | Setup and retrieval | Create `functions.ts`; identify repeated code. |
| 9:30-9:50 | Define versus call | Show that a definition alone produces no output. |
| 9:50-10:10 | One typed parameter | Trace one argument into the parameter box. |
| 10:10-10:30 | Two parameters and decisions | Match by position; reuse a familiar `if/else`. |
| 10:30-11:00 | Break | Fixed block. |
| 11:00-11:30 | Typing practice | Fixed block. |
| 11:30-11:40 | Retrieval restart | Rebuild a one-parameter function from memory. |
| 11:40-12:05 | Guided parameter missions | Predict, call, run, and repair. |
| 12:05-12:15 | Return readiness gate | Continue only if calls and parameters are secure. |
| 12:15-12:40 | AI Label Review Helper | Reuse one review rule across an array. |
| 12:40-12:52 | Kahoot or verbal recap | Reinforce definition, call, parameter, and argument. |
| 12:52-1:00 | Homework and exit check | Explain submission and collect one-sentence definitions. |

Only break and typing practice are fixed. Adjust every other block based on
student explanations, not on finishing every slide.

## Opening Script

> You already know how to write instructions, make decisions, repeat work, and
> process a list. Today you will learn how to give a useful group of
> instructions a name. Once a job has a name, your program can call that job
> whenever it needs it.

## Readiness Prompt

Show:

```ts
console.log("Welcome, Maya!");
console.log("Welcome, Leo!");
console.log("Welcome, Zara!");
```

Ask:

1. What repeats?
2. What changes?
3. What could go wrong if we copied this pattern 30 times?

Do not require students to invent function syntax yet. The goal is for them to
feel the problem before seeing the tool.

## Core Mental Model

Use this model throughout class:

```text
DEFINE THE JOB          CALL THE JOB          RUN THE BODY
function greet(...)     greet("Maya")         name = "Maya"
```

Say:

> The definition is the recipe. The call is the order to use that recipe now.
> The argument is the value sent with the order, and the parameter is the
> named box that receives it.

Avoid switching metaphors during the lesson. Use job, call, input box, and
result consistently.

## Guided Coding Sequence

Build in this order:

1. Define a no-parameter function.
2. Predict the output before calling it.
3. Call it once, then twice.
4. Add one `string` parameter.
5. Trace one argument into that parameter.
6. Call the function with three different arguments.
7. Add a second parameter of a different type.
8. Put a familiar `if/else` inside the function.
9. Call the function from an array loop.
10. Use a typed return value only after the readiness gate.

Never paste the finished AI project at once. Each addition should answer one
question the students can predict.

## Return-Value Readiness Gate

Ask four students, or four groups, to answer:

1. Where is the function definition?
2. Which line calls the function?
3. Which argument enters the parameter?
4. What changes between two calls?

Proceed to `return` only if most answers are clear and independent.

If not, repeat with:

```ts
function showDouble(number: number) {
  console.log(number * 2);
}

showDouble(4);
showDouble(7);
```

## AI Connection

Use this wording:

> AI systems can produce labels or predictions. A review function can apply
> one consistent rule to every result, such as flagging `unknown`. Consistency
> is useful, but the rule does not understand the image. A person still checks
> the evidence and decides what is correct.

Emphasize:

- The function is ordinary TypeScript, not an AI model.
- One named rule can be reused for many labels.
- A function can help organize a larger AI product.
- Automatic flags support human review; they do not guarantee truth.

## Checks for Understanding

Use these throughout class:

- "Has this function been defined, called, or both?"
- "What value is inside the parameter during this call?"
- "Which argument matches the second parameter?"
- "How many times will the function body run?"
- "What old skill is being reused inside the function?"
- "Does this function print a value or return a value?"

Require predictions before running code. A correct prediction with a clear
reason matters more than typing speed.

## Adaptive Pacing

- **A student's setup fails:** Continue teaching in VS Code and ask that
  student to use the TypeScript Playground for the same code.
- **Students expect a definition to run:** Add and remove the call several
  times while they predict the output.
- **Parameter and argument are mixed up:** Draw one labeled input box and send
  a sticky note value into it.
- **Two parameters are confusing:** Return to one parameter; do not force the
  second.
- **Students are on pace:** Complete the array-driven AI helper.
- **Students move quickly:** Add `needsReview(label: string): boolean`.
- **Activities run long:** Skip return values and Kahoot; keep guided coding
  and the closing check.

## Homework Transition

Say:

> Homework asks you to read, call, complete, and repair small functions. Start
> by locating the definition, parameters, and calls. Predict before checking
> anything in VS Code.

Homework is due before class on Saturday, September 5, 2026.

## Submission Reminder

Classwork must be sent to both assistant teachers:

1. Ishwari Raut ma'am
2. Khushi ma'am

Students may also post classwork in Microsoft Teams as a reply to the
classwork post.

Homework must be sent only to Ishwari Raut ma'am and Khushi ma'am. Do not
post homework in Microsoft Teams.

## Closing Script

> A function is a reusable named job. A definition describes the job, a call
> runs it, parameters name the inputs, and arguments provide the values. You
> can now organize old skills into code your program can reuse.
