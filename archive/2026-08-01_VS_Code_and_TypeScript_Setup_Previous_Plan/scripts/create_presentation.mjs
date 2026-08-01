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

setText(1, "TextBox 15", "Build Your Coding Workspace");
setText(1, "TextBox 16", "VS Code + Node.js + TypeScript");
setText(1, "TextBox 18", "August 1, 2026  |  Kids Computer Science");
addNotes(1, "Welcome students. Today we move from browser-based experiments to a real coding workspace. The goal is confidence, not speed.");

setJourney(2, "Today ends with a real local program", [
  "Install VS Code",
  "Install Node.js LTS",
  "Install TypeScript once",
  "Prove every tool works",
  "Compile and run a file",
  "Test a decision ladder",
]);
addNotes(2, "Preview the mission. Setup is the required win. The decision ladder is the extension if setup finishes in time.");

setCards(3, "You already know the code", "A quick two-week recap", [
  ["PRINT & STORE", "console.log(...) shows output", "let and const store values", "Some values can change"],
  ["TYPE SAFETY", "string, number, boolean", "TypeScript spots mismatches", "Read the red message"],
  ["COMPARE", "+  -  *  /  %", "===  >  <  >=  <=", "Comparisons make booleans"],
  ["DECIDE", "if chooses a true path", "else is the fallback", "Exactly one path runs"],
]);
addNotes(3, "Ask students for one example from each card. Keep this recap under fifteen minutes unless the class needs more practice.");

setCards(4, "From Playground to your computer", "The code stays familiar; the workflow changes", [
  ["PLAYGROUND", "A website handles the tools", "Great for quick experiments", "Nothing to install"],
  ["LOCAL WORKSPACE", "Files live on your computer", "VS Code saves the files", "The terminal runs commands"],
  ["TYPESCRIPT FILE", "Humans edit the .ts file", "The compiler creates .js", "The language stays the same"],
  ["SAFE SETUP", "Use official downloads", "Trust folders you created", "Ask before admin access"],
]);
addNotes(4, "Build the mental model before installing anything. A local workspace gives students ownership of their files and prepares them for later projects.");

setSix(5, "Three tools make one workflow", "Each tool has one beginner-friendly job", [
  "VS Code\nWRITE",
  "Node.js\nRUN",
  "TypeScript\nCHECK",
  "Save the .ts file",
  "Compile with tsc",
  "Run with node",
], "Install once. Reuse every Saturday.");
addNotes(5, "Point from left to right: write in VS Code, check and compile with TypeScript, then run the generated JavaScript with Node.js.", [
  "https://code.visualstudio.com/docs",
  "https://nodejs.org/en/download/",
  "https://www.typescriptlang.org/download/",
]);

setCards(6, "Windows: install the workspace", "Follow the teacher and stop at each green check", [
  ["VS CODE", "Choose User Installer", "Use the official Microsoft page", "Accept the normal defaults"],
  ["NODE.JS", "Choose the LTS version", "Run the Windows .msi", "Restart VS Code afterward"],
  ["TERMINAL", "Open Command Prompt in VS Code", "Avoid script-policy errors", "Do not change security settings"],
  ["CHECK", "node --version", "npm --version", "Then install TypeScript"],
]);
addNotes(6, "Demonstrate the User Installer and Node.js LTS. Use the Command Prompt terminal for class so PowerShell policy messages do not become a distraction.", [
  "https://code.visualstudio.com/docs/setup/windows",
  "https://nodejs.org/en/download/",
]);

setCards(7, "macOS: install the workspace", "Follow the teacher and stop at each green check", [
  ["VS CODE", "Download the Universal build", "Drag it to Applications", "Open it once"],
  ["NODE.JS", "Choose the LTS version", "Run the macOS installer", "Restart VS Code afterward"],
  ["TERMINAL", "Open the zsh terminal", "Commands run in the folder", "Never share a password"],
  ["CHECK", "node --version", "npm --version", "Then install TypeScript"],
]);
addNotes(7, "Demonstrate dragging VS Code to Applications and installing Node.js LTS. If macOS asks for a computer password, the student should ask a parent or teacher.", [
  "https://code.visualstudio.com/docs/setup/mac",
  "https://nodejs.org/en/download/",
]);

setCards(8, "Install TypeScript once", "Global means the tsc command works in future folders", [
  ["RUN ONCE", "npm install -g typescript", "Teacher leads the command", "Wait until it finishes"],
  ["WHY GLOBAL", "No repeated installs", "Use the same tsc command", "Future folders are ready"],
  ["VERIFY", "Run tsc --version", "Expect a Version message", "Stop if command is missing"],
  ["SAFETY", "Use the official npm package", "Do not add extra extensions", "Ask before using sudo"],
]);
addNotes(8, "This is the one-time global installation. On macOS, use sudo only if npm reports a permissions error and an adult approves. Students never read passwords aloud or share them.", [
  "https://www.typescriptlang.org/download/",
]);

setSix(9, "Green Check setup milestones", "Do not race ahead of the class", [
  "VS Code opens",
  "node --version",
  "npm --version",
  "tsc --version",
  "Class folder open",
  "decisions.ts saved",
], "Stop at the first red check and ask for help.");
addNotes(9, "Pause after each milestone and use reactions or the chat for green checks. Pair students so one reads the screen while the other confirms the step.");

setJourney(10, "Create one class workspace", [
  "Choose File > Open Folder",
  "Open KidsComputerScience",
  "Create 2026-08-01-decisions",
  "Trust the folder you created",
  "Create decisions.ts",
  "Open Terminal > New Terminal",
]);
addNotes(10, "Model the exact folder and file names. Show that the terminal prompt should point to the class folder before students type a command.");

setCards(11, "Write your first local decision ladder", "Save this as decisions.ts", [
  ["START", "let score: number = 82;", "", "Save decisions.ts"],
  ["FIRST TEST", "if (score >= 90) {", "  console.log(\"Legend\");", "} else if (score >= 70) {"],
  ["MORE PATHS", "  console.log(\"Hero\");", "} else if (score >= 50) {", "  console.log(\"Explorer\");"],
  ["FALLBACK", "} else {", "  console.log(\"Keep training\");", "}"],
]);
addNotes(11, "Type slowly and have students follow. Explain only the structure: one value, ordered tests, and one fallback. Do not introduce functions, arrays, or loops.");

setSix(12, "Save, compile, and run", "The terminal turns your file into visible output", [
  "Save decisions.ts",
  "tsc decisions.ts",
  "TypeScript checks",
  "decisions.js appears",
  "node decisions.js",
  "Output appears",
], ".ts  →  tsc  →  .js  →  Node  →  output");
addNotes(12, "Repeat this workflow aloud twice. A successful compile can be quiet. The generated decisions.js file is expected and should not be edited today.");

setCards(13, "Read the local workflow", "Know which file you edit and which command you run", [
  ["SOURCE FILE", "decisions.ts", "Humans edit this file", "Save before compiling"],
  ["GENERATED FILE", "decisions.js", "tsc creates this file", "Do not edit it today"],
  ["TERMINAL", "node decisions.js", "The program prints Hero", "No browser is needed"],
  ["EXPERIMENT", "Try 95, 70, and 49", "Compile after each edit", "Name the path that ran"],
]);
addNotes(13, "Ask: Which file do we edit? Which file does Node run? Let students answer before changing the score and recompiling.");

setCards(14, "Recap: if and else", "A two-way decision chooses one path", [
  ["QUESTION", "Is the condition true?", "The answer is a boolean", "true or false"],
  ["IF", "Runs when the test is true", "The first path", "Uses curly braces"],
  ["ELSE", "Runs when the test is false", "The fallback path", "No new condition"],
  ["ONE RESULT", "Only one path runs", "Trace the condition first", "Then predict the output"],
]);
addNotes(14, "Use a familiar example such as age or temperature. Ask students to predict before running the program.");

setCards(15, "Add more paths with else if", "Tests run from top to bottom", [
  ["IF", "Test the highest rule first", "score >= 90", "Stop if it is true"],
  ["ELSE IF", "Try the next rule", "score >= 70", "Only if the first was false"],
  ["ELSE IF", "Try one more rule", "score >= 50", "Only if earlier tests failed"],
  ["ELSE", "Catch every other value", "No condition is needed", "Exactly one path wins"],
]);
addNotes(15, "Walk down the ladder with scores 95, 82, 50, and 49. Emphasize that the first true branch wins.");

setComparison(16, "Condition order changes the answer", "A broad rule placed first can hide a stricter rule", [
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
  "95 reaches Legend",
]);
addNotes(16, "Trace the wrong ladder first. The program compiles, yet the logic is wrong. Reorder conditions from most specific or highest threshold to broadest or lowest threshold.");

setComparison(17, "AI logic bug hunt", "AI can suggest code; humans still test the decisions", [
  ["AI draft", "code source"],
  ["4 tests", "95  90  70  49"],
  ["1 bug", "wrong order"],
  ["Human", "verifies"],
], [
  "DO",
  "Predict before running",
  "Test boundary values",
  "Trace the first true rule",
  "Reorder highest first",
], [
  "DON'T",
  "Assume compile means correct",
  "Test only one value",
  "Accept AI code blindly",
  "Skip boundary values",
]);
addNotes(17, "Display the buggy ladder from classwork. Students predict four outputs, run the tests, and explain the repair. Connect this to responsible use of AI coding assistants.");

setText(18, "TextBox 14", "✓");
setText(18, "TextBox 15", "Workspace ready!");
setText(18, "TextBox 17", "Save your folder and show one successful program run.");
setText(18, "Rounded Rectangle 18", "Submit classwork in Teams");
addNotes(18, "Celebrate every successful checkpoint. Remind students to submit in Microsoft Teams and copy Ishwari Raut ma'am. Students using the Playground fallback receive equal credit.");

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
