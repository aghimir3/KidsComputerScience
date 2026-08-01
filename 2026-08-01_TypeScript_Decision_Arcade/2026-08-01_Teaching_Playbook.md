# Teaching Playbook — TypeScript Decision Arcade

**Class date:** August 1, 2026  
**Class time:** 9:00 AM–1:00 PM Pacific  
**Classroom coding tool:** [TypeScript Playground](https://www.typescriptlang.org/play/)  
**New concept:** `else if`  
**Homework:** Install VS Code, Node.js LTS, and TypeScript on Windows or macOS

---

## The teaching goal

By the end of class, students should be able to:

1. Open the TypeScript Playground and run a short program.
2. Recall variables, types, expressions, comparisons, `console.log`, `if`, and `else`.
3. Explain that an `else if` ladder checks conditions from top to bottom.
4. Predict which single branch will run.
5. Test exact boundary values such as 90, 89, 70, and 69.
6. Find and repair a condition-order bug in an AI-generated draft.

The confidence target is more important than the speed target. A student who can trace one ladder carefully has succeeded.

---

## Guardrails for this class

- Use the browser Playground for all classroom coding.
- Do not stop class for VS Code, Node.js, or TypeScript installation.
- Keep every example inside July's concepts plus today's single new idea: `else if`.
- Do not introduce functions, arrays, loops, input prompts, randomness, compound conditions, or advanced operators.
- Ask students to predict before clicking **Run**.
- Use several values, especially values exactly on and just below each boundary.
- Let returning students deepen the same concepts instead of moving ahead.

---

## Before students arrive

### Open these tabs

1. The August 1 slide deck.
2. `https://www.typescriptlang.org/play/`
3. The class activity.
4. The fillable classwork PDF.
5. The Kahoot game or question reference.
6. The homework PDF and both setup guides.

### Prepare the Playground

Delete the sample code and paste this tiny test:

```ts
const className: string = "Decision Arcade";
console.log(className);
```

Click **Run** once. Confirm that the output appears. Then clear the editor so students see a clean starting point.

### Prepare Teams

- Post the classwork materials in **Classwork**.
- Post the setup assignment and both operating-system guides in **Homework**.
- Keep the **Hangout Session** channel visible so students know where to find help.

### Screen-sharing check

- Increase browser zoom until code is readable.
- Make sure the editor and output panel are both visible.
- Turn off notifications.
- Keep the code line length short enough to fit on screen.

---

## 9:00–9:10 — Welcome and set the mission

### Say

> Today we are turning the browser into a decision-game arcade. We will reuse everything we learned in July and add one new move: `else if`. We are not installing anything during class. We will spend our class time coding together.

### Show

- Slide 1: TypeScript Decision Arcade
- Slide 2: Today's outcomes

### Check for readiness

Ask students to react with:

- ✅ if they can see your shared screen
- 🎮 if they are ready to build a decision game

### Important expectation

Tell students that the code may look longer today, but it is still made from familiar pieces. The new part is how several decisions connect.

---

## 9:10–9:20 — Open the Playground together

### Say

> The Playground is a safe browser workspace for practicing TypeScript. Code goes on the left. We click Run. Then we read the output. If we make a mistake, we can change the code and try again.

### Student steps

1. Open `https://www.typescriptlang.org/play/`.
2. Remove any sample code.
3. Type:

```ts
const playerName: string = "Nova";
console.log(playerName);
```

4. Predict the output.
5. Click **Run**.
6. Find `Nova` in the output.

### If the interface looks different

Do not spend time matching every button. Have the student locate only the editor, **Run**, and the output.

### Quick check

Ask: “What are the three actions in our coding loop?”

Expected response: **Type, Run, Read**.

---

## 9:20–9:40 — July recap through prediction

### Show

- Slide 3: July toolkit
- Slide 4: Playground workflow
- Slide 5: Prediction workflow
- Slide 6: Recap challenge

### Recap one idea at a time

#### Variables and types

Type:

```ts
const hero: string = "Pixel";
let energy: number = 40;
const doorOpen: boolean = false;
```

Ask:

- Which value is text?
- Which value is a number?
- Which value is true or false?
- Which variable may change?

#### Expressions

Add:

```ts
energy = energy + 15;
console.log(energy);
```

Ask students to calculate the output before running it.

#### Comparisons

Add:

```ts
console.log(energy >= 50);
```

Ask:

> Does a comparison produce a number, text, or a boolean?

Expected response: **boolean**.

#### `if` and `else`

Replace the editor with:

```ts
const fuel: number = 60;

if (fuel >= 50) {
  console.log("Launch approved!");
} else {
  console.log("Refuel first.");
}
```

Ask students to point to the branch they think will run. Then click **Run**.

### Teaching language

Use the phrase:

> A condition is a yes-or-no question. A branch is the path chosen by the answer.

### Returning-student option

Students who finish early may begin the first half of the Robot Repair Arcade. Ask them to explain type corrections and `if`/`else` predictions. They should return when the new-concept slide begins.

---

## 9:40–10:10 — Introduce `else if`

### Show

- Slide 7: New concept — `else if`
- Slide 8: Top-to-bottom checking
- Slide 9: First true branch wins

### Build the need before the syntax

Say:

> `if` and `else` are perfect for two paths. What if our game needs Legendary, Hero, Explorer, and Rookie? We need more than one question.

Write the outcomes on screen before showing code:

- 90 or more → Legendary
- 70 or more → Hero
- 50 or more → Explorer
- anything lower → Rookie

### Introduce the ladder

Type slowly:

```ts
const score: number = 82;

if (score >= 90) {
  console.log("Legendary");
} else if (score >= 70) {
  console.log("Hero");
} else if (score >= 50) {
  console.log("Explorer");
} else {
  console.log("Rookie");
}
```

### Exact talk track

> The computer starts at the top. It asks the first question. If that answer is false, it moves down. When it reaches the first true condition, it runs that branch and stops the ladder. The final `else` catches everything that did not match earlier.

### Trace score 82 aloud

1. Is 82 at least 90? **False. Move down.**
2. Is 82 at least 70? **True. Print Hero.**
3. Stop. Do not check the remaining branches.

### Body movement check

Have students use:

- thumbs down = false, move down
- thumbs up = true, run and stop

Trace scores 95, 82, 55, and 20 without running the code.

### Prevent the main misconception

Say:

> This is one connected ladder. It chooses one branch. It is not four separate `if` statements.

### Check for understanding

Ask:

- What direction does the computer check?
- What makes it stop?
- What is the job of the final `else`?

Expected responses:

- top to bottom
- the first true condition
- catch every remaining value

---

## 10:10–10:30 — Build the Rank Engine together

### Show

- Slide 10: Build steps
- Slide 11: Rank Engine code

### Live-coding routine

Use the same routine after every small addition:

1. Teacher types one part.
2. Students say what it means.
3. Students predict.
4. Everyone runs.
5. Everyone reads the output.

### Build in this order

1. Create `score` as a number.
2. Add the `if` condition for 90.
3. Add the first `else if` for 70.
4. Add the second `else if` for 50.
5. Add the final `else`.
6. Test several values.

### Boundary Boss tests

Ask students to fill this table before running each test:

| Score | Prediction |
|---:|---|
| 90 | Legendary |
| 89 | Hero |
| 70 | Hero |
| 69 | Explorer |
| 50 | Explorer |
| 49 | Rookie |

### Emphasize

> Exact boundaries are where many bugs hide. Test the boundary and the number just below it.

### Save progress

Students should copy their Rank Engine code into their classwork answer area or keep the Playground tab open through break.

---

## 10:30–11:00 — Break

Fixed break. Do not use this time for installation support.

Before releasing students, say:

> Keep your Playground tab open if possible. We will turn the ladder into game missions after typing practice.

---

## 11:00–11:30 — Typing practice

Fixed block.

Optional TypeScript vocabulary for a final two-minute typing burst:

- condition
- boolean
- branch
- predict
- boundary
- `else if`

Do not turn this into another programming lecture. Resume the lesson at 11:30.

---

## 11:30–11:45 — Boundary Boss Battle

### Show

- Slide 12: Boundary Boss Battle

### Pair routine

For each test value:

1. Partner A traces from the top.
2. Partner B records the result.
3. Both run the program.
4. Switch roles.

### Listen for complete explanations

A strong explanation sounds like:

> 69 fails the 90 condition and the 70 condition. It passes the 50 condition, so Explorer runs and the ladder stops.

If students state only the output, ask: “Which earlier conditions were false?”

---

## 11:45–12:05 — Mission 1: Galactic Gatekeeper

### Show

- Slide 13: Galactic Gatekeeper

### Rules

- 80 or more fuel → `Warp speed!`
- 50 or more fuel → `Cruise mode.`
- 20 or more fuel → `Emergency reserve.`
- anything lower → `Dock and refuel.`

### Starter

```ts
const fuel: number = 72;

// Build the decision ladder here.
```

### Required tests

80, 79, 50, 49, 20, and 19.

### Facilitation prompt

Ask: “Why are the conditions written from the largest threshold to the smallest?”

Expected idea: a broad lower condition placed first could catch a high value too early.

---

## 12:05–12:20 — Mission 2: Dragon Training Arena

### Show

- Slide 14: Dragon Training Arena

### Rules

- 90 or more → `Master Dragon Rider`
- 70 or more → `Skilled Flyer`
- 40 or more → `Training Cadet`
- anything lower → `Practice in the nest`

### Team roles

- **Navigator:** reads the mission rules.
- **Coder:** types while teammates explain.
- **Tester:** chooses boundary values.
- **Reporter:** explains one trace to the class.

Rotate roles when the team completes one successful test.

### If the group is stuck

Ask these questions in order:

1. What is the value variable?
2. What is the highest outcome?
3. What condition belongs first?
4. What should happen when that condition is false?
5. What should the final `else` catch?

---

## 12:20–12:35 — Mission 3: Create a tiny decision game

### Show

- Slide 15: Create your game

### Student choices

Students may design one of these:

- superhero training rank
- space explorer badge
- pet-care helper
- weather outfit guide using a number
- robot battery status

### Requirements

- one number variable with a type
- one `if`
- at least two `else if` branches
- one final `else`
- four different messages
- four test values, including a boundary

### Scope reminder

Students should not add input boxes, randomness, arrays, loops, or functions. The creative part is the theme, messages, thresholds, and test plan.

### Share-out

Invite two students to show:

1. one boundary they tested
2. the path the computer followed

---

## 12:35–12:48 — AI Bug Bounty

### Show

- Slide 16: AI draft — order changes the answer

### Frame the AI connection

Say:

> AI coding tools can suggest code quickly, but suggested code can compile and still make the wrong decision. A human programmer must test the logic.

### Buggy draft

```ts
const score: number = 95;

if (score >= 50) {
  console.log("Explorer");
} else if (score >= 70) {
  console.log("Hero");
} else if (score >= 90) {
  console.log("Legendary");
} else {
  console.log("Rookie");
}
```

### Ask before running

- What will this code print for 95?
- What should it print?
- Why are those answers different?

### Repair

Move the thresholds into descending order: 90, 70, 50.

### Key message

> “The code runs” and “the code is correct” are different claims.

### AI discussion point

Ask: “What evidence would help you decide whether AI-generated decision code is trustworthy?”

Expected ideas:

- trace it
- test boundaries
- compare the output with the written rules
- ask another person to review it

---

## 12:48–12:55 — Homework walkthrough

### Show

- Slide 17: Homework builds your local workspace

### Say

> Classroom coding was in the Playground. Your homework is to prepare the local tools we will use later: VS Code, Node.js LTS, and TypeScript. Choose the Windows guide or the macOS guide. You install these once; we are using a global TypeScript installation so you do not repeat that step for every beginner exercise.

### Explain the two routes

#### Windows

- VS Code **User Installer**
- Node.js **LTS**
- `npm install -g typescript`
- verify with `code --version`, `node --version`, `npm --version`, and `tsc --version`

#### macOS

- VS Code `.dmg`, then drag to Applications
- Node.js **LTS**
- `npm install -g typescript`
- verify with `node --version`, `npm --version`, and `tsc --version`

### Safety message

Say clearly:

> Use only the official links in the guide. Never post or share a password. If the computer asks for administrator approval or shows a permissions error, record what happened and get an adult or Hangout helper. Do not change security settings by guessing.

### Help route

> The assistant-teacher Hangout Session is 4:30–5:30 PM Pacific, as scheduled in the Microsoft Teams Hangout Session channel. Bring the guide, the exact step number, and the exact error message.

### Submission reminder

Students submit to:

1. Microsoft Teams
2. Ishwari Raut ma'am

---

## 12:55–1:00 — Kahoot and close

### Use the quiz adaptively

If there is time, run the full 15-question Kahoot. If class needs more practice, ask the following five essentials live and post the full quiz for later review:

1. In what order does an `else if` ladder check?
2. What happens after the first true condition?
3. What is the job of the final `else`?
4. Why test 90 and 89?
5. Why should humans test AI-generated code?

### Final recap

Ask students to finish this sentence in chat:

> An `else if` ladder...

A successful answer should include **top to bottom**, **first true**, or **one branch**.

### Close

> Today you turned yes-or-no questions into a multi-path game. Your next step is to prepare VS Code at home using the guide. If the setup fights back, save the error and bring it to Hangout—we solve setup problems together.

---

## Common misconceptions and responses

### “Every true condition will run.”

Response:

> In one connected `if` / `else if` / `else` ladder, the first true branch runs and the ladder stops.

Trace score 95 from the top and physically cover the remaining branches after the first match.

### “The order does not matter.”

Response:

> The computer checks from the top, so an earlier broad condition can steal a value from a later specific condition.

Use the AI Bug Bounty example with `score >= 50` placed first.

### “`else` needs a condition.”

Response:

> The final `else` means “anything not already handled,” so it does not need another question.

### “A boundary is close enough.”

Response:

> `>= 70` includes exactly 70. `> 70` does not. Test the exact boundary to see which rule you wrote.

Do not expand into every comparison operator unless the class needs that recap.

### “Red underlines mean I am bad at coding.”

Response:

> A red underline is a clue. Check braces, parentheses, spelling, and quotation marks one at a time.

### “The AI wrote it, so it must be right.”

Response:

> AI can create a useful draft. The programmer remains responsible for tracing the rules and testing the output.

---

## Debugging checklist for live support

When a program does not work, avoid rewriting it for the student. Ask them to check:

1. Does every opening `{` have a closing `}`?
2. Is every text message inside matching quotation marks?
3. Is the keyword written as two words: `else if`?
4. Is the comparison inside parentheses?
5. Are thresholds ordered from most specific/highest to lower?
6. Did the student click **Run** after changing the value?
7. Is the expected output based on the written rules?

---

## Adaptive pacing decisions

### If students need more support

- Use only the Rank Engine and Galactic Gatekeeper.
- Trace with thumbs up/down before typing.
- Keep the four outcomes visible.
- Complete the classwork together.
- Shorten the student-created game to one `if`, one `else if`, and one `else`.
- Do the five-question verbal close instead of the full live Kahoot.

### If students are on pace

- Complete both guided missions.
- Give time for a themed decision game.
- Run the AI Bug Bounty and full Kahoot.

### If students finish early

- Use the Robot Repair Arcade.
- Require more boundary tests.
- Ask for clearer output messages.
- Have students explain the trace to a partner.
- Do not introduce new syntax.

---

## Evidence of learning to collect

During class, look for:

- predictions made before Run
- correct tracing from the first condition downward
- one explanation of why a branch was skipped
- boundary tests at and just below a threshold
- a repair to the AI-generated wrong-order ladder
- a student-created ladder with four outcomes

After class, look for:

- completed classwork submitted in both required places
- setup homework showing VS Code, Node.js LTS, npm, and global TypeScript versions
- a local TypeScript file that compiles and runs
- a reflection or saved error report

---

## End-of-class teacher checklist

- [ ] Students know that classroom coding used the Playground.
- [ ] Students can explain top-to-bottom checking.
- [ ] Students can explain first true branch wins.
- [ ] Students tested at least one exact boundary.
- [ ] Students saw that AI-generated code still needs human testing.
- [ ] Homework includes both Windows and macOS guides.
- [ ] Students heard the Hangout Session time: 4:30–5:30 PM Pacific.
- [ ] Students know to submit to Microsoft Teams and Ishwari Raut ma'am.

