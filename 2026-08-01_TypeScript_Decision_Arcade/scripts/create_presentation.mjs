import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const starterPath = process.argv[2];
const outputPath = process.argv[3];
const qaDir = process.argv[4];

if (!starterPath || !outputPath || !qaDir) {
  throw new Error(
    "Usage: node create_presentation.mjs <template-starter.pptx> <output.pptx> <qa-dir>",
  );
}

const presentation = await PresentationFile.importPptx(
  await FileBlob.load(starterPath),
);

function shapeByName(slide, name) {
  const shape = slide.shapes.items.find((item) => item.name === name);
  if (!shape) throw new Error(`Missing inherited shape: ${name}`);
  return shape;
}

function setText(slideNumber, name, value) {
  shapeByName(presentation.slides.items[slideNumber - 1], name).text = value;
}

function addNotes(slideNumber, text, sources = []) {
  const slide = presentation.slides.items[slideNumber - 1];
  let notes = text.trim();
  if (sources.length) {
    notes += `\n\n[Sources]\n${sources.map((url) => `- ${url}`).join("\n")}\n[/Sources]`;
  }
  slide.speakerNotes.textFrame.setText(notes);
  slide.speakerNotes.setVisible(true);
}

function setCards(slideNumber, title, subtitle, cards) {
  const names = [
    ["TextBox 8", "TextBox 9", "TextBox 10", "TextBox 11"],
    ["TextBox 14", "TextBox 15", "TextBox 16", "TextBox 17"],
    ["TextBox 20", "TextBox 21", "TextBox 22", "TextBox 23"],
    ["TextBox 26", "TextBox 27", "TextBox 28", "TextBox 29"],
  ];
  setText(slideNumber, "TextBox 4", title);
  setText(slideNumber, "TextBox 5", subtitle);
  for (let i = 0; i < 4; i += 1) {
    for (let j = 0; j < 4; j += 1) setText(slideNumber, names[i][j], cards[i][j]);
  }
}

function setSix(slideNumber, title, subtitle, items, takeaway) {
  setText(slideNumber, "TextBox 4", title);
  setText(slideNumber, "TextBox 5", subtitle);
  for (let i = 0; i < 6; i += 1) {
    setText(slideNumber, `Rounded Rectangle ${i + 6}`, items[i]);
  }
  setText(slideNumber, "Rounded Rectangle 12", takeaway);
}

function setJourney(slideNumber, title, items) {
  setText(slideNumber, "TextBox 4", title);
  const names = ["TextBox 6", "TextBox 8", "TextBox 10", "TextBox 12", "TextBox 14", "TextBox 16"];
  for (let i = 0; i < 6; i += 1) setText(slideNumber, names[i], items[i]);
}

function setComparison(slideNumber, title, subtitle, stats, left, right) {
  setText(slideNumber, "TextBox 4", title);
  setText(slideNumber, "TextBox 5", subtitle);
  const statNames = [
    ["TextBox 7", "TextBox 8"],
    ["TextBox 10", "TextBox 11"],
    ["TextBox 13", "TextBox 14"],
    ["TextBox 16", "TextBox 17"],
  ];
  for (let i = 0; i < 4; i += 1) {
    setText(slideNumber, statNames[i][0], stats[i][0]);
    setText(slideNumber, statNames[i][1], stats[i][1]);
  }
  const leftNames = ["TextBox 19", "TextBox 20", "TextBox 21", "TextBox 22", "TextBox 23"];
  const rightNames = ["TextBox 25", "TextBox 26", "TextBox 27", "TextBox 28", "TextBox 29"];
  for (let i = 0; i < 5; i += 1) {
    setText(slideNumber, leftNames[i], left[i]);
    setText(slideNumber, rightNames[i], right[i]);
  }
}

setText(1, "TextBox 15", "TypeScript Decision Arcade");
setText(1, "TextBox 16", "Playground missions + else if");
setText(1, "TextBox 18", "August 1, 2026  |  Kids Computer Science");
addNotes(1, "Welcome students to the Decision Arcade. Classroom coding stays in the browser today so time is spent practicing decisions. The only new syntax is else if.");

setJourney(2, "Today you become a decision-game designer", [
  "Open the Playground",
  "Recharge July skills",
  "Learn else if",
  "Trace top to bottom",
  "Beat boundary bosses",
  "Debug an AI draft",
]);
addNotes(2, "Preview the six outcomes. Tell students that they already know most of the ingredients. Today connects familiar yes-or-no decisions into one multi-path ladder.");

setCards(3, "Your July toolkit is ready", "Everything here has already been practiced", [
  ["STORE", "let and const", "Give values clear names", "Some values can change"],
  ["LABEL", "string, number, boolean", "Types describe values", "Read TypeScript clues"],
  ["CALCULATE", "+  -  *  /  %", "Build expressions", "Comparisons make booleans"],
  ["CHOOSE", "if asks a question", "else is the fallback", "console.log shows the result"],
]);
addNotes(3, "Ask for one example from each card. Keep the recap active: students should name the type, calculate the value, and predict a branch before the teacher reveals it.");

setCards(4, "The Playground keeps us coding", "Our class loop is Type → Run → Read", [
  ["OPEN", "typescriptlang.org/play", "Use the official site", "No classroom install"],
  ["TYPE", "Code goes in the editor", "Keep examples short", "Follow the teacher"],
  ["RUN", "Predict before clicking", "Run after each change", "Errors are clues"],
  ["READ", "Find the output", "Compare with prediction", "Explain the chosen path"],
]);
addNotes(4, "Open the Playground with students. Type a tiny console.log example, ask for a prediction, click Run, and locate the output together.", [
  "https://www.typescriptlang.org/play/",
]);

setSix(5, "Prediction is your superpower", "Do the thinking before the computer answers", [
  "Read the code",
  "Find the values",
  "Do the math",
  "Check booleans",
  "Choose a branch",
  "Then click Run",
], "Predict → Run → Compare → Explain");
addNotes(5, "Model the prediction routine. Pause before every Run click and have students state both the output and the reason. This prevents the Playground from becoming a guessing button.");

setCards(6, "Quick recap challenge", "Predict each output before the Playground runs", [
  ["TEXT", "const hero: string =", '"Pixel";', "What prints?"],
  ["NUMBER", "let energy = 40", "energy = energy + 15", "What is energy now?"],
  ["BOOLEAN", "energy >= 50", "A yes-or-no result", "true or false?"],
  ["DECISION", "if fuel >= 50", "Launch or refuel", "Which path runs?"],
]);
addNotes(6, "Use const hero = Pixel, energy 40 plus 15, energy >= 50, and a fuel if/else example. Students should answer before the teacher runs the code.");

setCards(7, "NEW CONCEPT: Add paths with else if", "One connected ladder can choose among several outcomes", [
  ["IF", "Ask the first question", "score >= 90", "True? Run and stop"],
  ["ELSE IF", "Ask the next question", "score >= 70", "Only after false"],
  ["ELSE IF", "Ask one more question", "score >= 50", "After earlier false"],
  ["ELSE", "Catch everything else", "No condition needed", "One path wins"],
]);
addNotes(7, "This is the dedicated new-concept slide. Build the need first: if/else gives two paths, while a game rank needs several. Say else if as two words and emphasize that it remains one connected ladder.");

setCards(8, "The ladder checks from top to bottom", "Trace score 82 — do not run yet", [
  ["1. START", "score = 82", "Begin at the top", "Never jump ahead"],
  ["2. CHECK 90", "82 >= 90 is false", "Move down", "Nothing prints yet"],
  ["3. CHECK 70", "82 >= 70 is true", "Print Hero", "First true branch"],
  ["4. STOP", "Ignore lower branches", "One result", "Hero wins"],
]);
addNotes(8, "Trace score 82 aloud. Use thumbs down for false and thumbs up for true. Once 82 reaches the 70 branch, cover the lower cards to show that checking stops.");

setSix(9, "First true branch wins", "A connected ladder chooses exactly one result", [
  ">= 90?\nfalse",
  "Move down",
  ">= 70?\ntrue",
  "Run Hero",
  "Stop ladder",
  "Skip the rest",
], "Top to bottom → first true → run → stop");
addNotes(9, "Repeat the stopping rule with scores 95, 82, 55, and 20. Contrast the connected ladder with separate if statements without teaching a new pattern.");

setJourney(10, "Build the Rank Engine together", [
  "Create the score variable",
  "Add the highest if rule",
  "Add the 70 else if",
  "Add the 50 else if",
  "Add the final else",
  "Test several values",
]);
addNotes(10, "Live-code one step at a time. After every addition, ask what the new line means and what the current program would do. Students follow in the Playground.");

setCards(11, "Rank Engine: one connected ladder", "Change only score, then predict before Run", [
  ["START", "const score: number = 82;", "", "Predict before Run"],
  ["FIRST CHECK", "if (score >= 90) {", "  console.log(\"Legendary\");", "} else if (score >= 70) {"],
  ["MORE PATHS", "  console.log(\"Hero\");", "} else if (score >= 50) {", "  console.log(\"Explorer\");"],
  ["FALLBACK", "} else {", "  console.log(\"Rookie\");", "}"],
]);
addNotes(11, "Type the code slowly. Keep every bracket visible. Ask students to find the if, each else if, and the fallback. Avoid functions, arrays, loops, input, randomness, and compound conditions.");

setSix(12, "Boundary Boss Battle", "Test the edge and the number just below it", [
  "90 → Legendary",
  "89 → Hero",
  "70 → Hero",
  "69 → Explorer",
  "50 → Explorer",
  "49 → Rookie",
], "Boundaries reveal whether the written rule matches the game rule");
addNotes(12, "Students predict each output before Run. Ask why 90 and 89 form a useful pair, then repeat for 70/69 and 50/49.");

setCards(13, "Mission 1: Galactic Gatekeeper", "Build a fuel-status game in the Playground", [
  ["RULES", "80+ Warp speed!", "50+ Cruise mode", "20+ Emergency reserve"],
  ["START", "const fuel: number = 72;", "Build one ladder", "Predict first"],
  ["TEST", "80 and 79", "50 and 49", "20 and 19"],
  ["TEAM", "Navigator reads", "Coder types; Tester checks", "Reporter explains"],
]);
addNotes(13, "Assign team roles. The Tester owns the six boundary values even though only three roles fit on the card. Ask why the thresholds are ordered from highest to lowest.");

setCards(14, "Mission 2: Dragon Training Arena", "Turn training points into a rider rank", [
  ["MASTER", "90 or more", "Master Dragon Rider", "Highest rule first"],
  ["SKILLED", "70 or more", "Skilled Flyer", "Second question"],
  ["CADET", "40 or more", "Training Cadet", "Third question"],
  ["NEST", "Anything lower", "Practice in the nest", "Final else"],
]);
addNotes(14, "Teams rotate roles after one successful test. If a group is stuck, ask for the value variable, the highest outcome, the first condition, and the final fallback.");

setCards(15, "Mission 3: Design your own tiny game", "Creativity changes the theme, not the course concepts", [
  ["CHOOSE", "Name a game theme", "Use one number", "Write four outcomes"],
  ["BUILD", "One if", "At least two else if", "One final else"],
  ["TEST", "Try four values", "Include a boundary", "Record each output"],
  ["EXPLAIN", "Trace from the top", "Name the first true", "Say why it stops"],
]);
addNotes(15, "Offer themes such as superheroes, space badges, pet care, weather outfits, or robot battery. Keep the scope to today's syntax and previously learned types, values, comparisons, and output.");

setComparison(16, "AI draft: order changes the answer", "Code can run and still make the wrong decision", [
  ["95", "test score"],
  ["1st", "true branch"],
  [">= 50", "too broad first"],
  ["Explorer", "wrong result"],
], [
  "WRONG ORDER",
  "if (score >= 50)",
  "else if (score >= 70)",
  "else if (score >= 90)",
  "95 stops at Explorer",
], [
  "CORRECT ORDER",
  "if (score >= 90)",
  "else if (score >= 70)",
  "else if (score >= 50)",
  "95 reaches Legendary",
]);
addNotes(16, "Frame this as an AI Bug Bounty. Students predict before running, find the mismatch between rules and output, and repair the order. Emphasize that the programmer remains responsible for testing AI suggestions.");

setComparison(17, "Homework builds your local workspace", "Choose one guide; ask for help instead of guessing", [
  ["Windows", "User guide"],
  ["macOS", "Mac guide"],
  ["3 tools", "VS Code + Node + TS"],
  ["4:30", "Hangout help"],
], [
  "DO",
  "Use the official links",
  "Choose Node.js LTS",
  "Record every version",
  "Save exact error messages",
], [
  "STOP AND ASK",
  "Never share a password",
  "Avoid download advertisements",
  "Do not guess security fixes",
  "Bring errors to Hangout",
]);
addNotes(17, "Explain that setup is homework, not classroom time. Students choose the attached Windows or macOS guide, install VS Code, Node.js LTS, and TypeScript globally, then compile and run local-ready.ts. The assistant-teacher Hangout Session is 4:30–5:30 PM Pacific as scheduled in Teams.", [
  "https://code.visualstudio.com/docs/setup/windows",
  "https://code.visualstudio.com/docs/setup/mac",
  "https://nodejs.org/en/download/",
  "https://www.typescriptlang.org/download/",
]);

setText(18, "TextBox 14", "✓");
setText(18, "TextBox 15", "Arcade cleared!");
setText(18, "TextBox 17", "Homework: build your local VS Code + TypeScript workspace.");
setText(18, "Rounded Rectangle 18", "Use one guide • Ask for help");
addNotes(18, "Celebrate students' decision games. Remind them to submit classwork to Microsoft Teams and Ishwari Raut ma'am, then complete the setup homework with the matching operating-system guide. Setup help is available in Hangout.");

await fs.mkdir(path.dirname(outputPath), { recursive: true });
await fs.mkdir(path.join(qaDir, "slides"), { recursive: true });
await fs.mkdir(path.join(qaDir, "layout"), { recursive: true });

for (const [index, slide] of presentation.slides.items.entries()) {
  const stem = `slide-${String(index + 1).padStart(2, "0")}`;
  const png = await presentation.export({ slide, format: "png", scale: 1 });
  await fs.writeFile(path.join(qaDir, "slides", `${stem}.png`), new Uint8Array(await png.arrayBuffer()));
  const layout = await slide.export({ format: "layout" });
  await fs.writeFile(path.join(qaDir, "layout", `${stem}.layout.json`), await layout.text());
}

const montage = await presentation.export({ format: "webp", montage: true, scale: 1 });
await fs.writeFile(path.join(qaDir, "deck-montage.webp"), new Uint8Array(await montage.arrayBuffer()));

const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(outputPath);
await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });

console.log(`Created ${outputPath}`);
