import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const starterPptxPath = process.argv[2];
const outputPath = process.argv[3];
const qaDir = process.argv[4];

if (!starterPptxPath || !outputPath || !qaDir) {
  throw new Error(
    "Usage: node create_presentation.mjs <template-starter.pptx> <output.pptx> <qa-dir>",
  );
}

const presentation = await PresentationFile.importPptx(
  await FileBlob.load(starterPptxPath),
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

const conceptSource = "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#control-flow-analysis";
const playgroundSource = "https://www.typescriptlang.org/play/";

setText(1, "TextBox 15", "TypeScript Decisions");
setText(1, "TextBox 16", "if, else if, and else");
setText(1, "TextBox 18", "August 1, 2026  |  Kids Computer Science");
addNotes(1, "Introduce the topic only. Tell students that the slide deck explains the decision ladder, and all typing and testing will happen afterward through the class activity.");

setJourney(2, "One ladder can choose one path", [
  "Start with a value",
  "Ask the first condition",
  "Get true or false",
  "Move down after false",
  "Run the first true branch",
  "Use else as the fallback",
]);
addNotes(2, "Give the mental model before showing syntax. A connected decision ladder begins at the top, moves only after false, and selects one outcome.", [conceptSource]);

setCards(3, "else if adds another question", "Use it when a program needs more than two outcomes", [
  ["IF", "Ask first", "score >= 90", "True? Run this"],
  ["ELSE IF", "Ask next", "score >= 70", "Only after false"],
  ["ELSE IF", "Ask again", "score >= 50", "Only after false"],
  ["ELSE", "Final fallback", "No condition", "Catches the rest"],
]);
addNotes(3, "Connect this to the familiar if/else pair. Else if does not start a separate decision; it adds another question inside the same ladder.", [conceptSource]);

setCards(4, "One connected decision ladder", "The branches belong together", [
  ["VALUE", "const score: number = 82;", "One value enters", "Start at the top"],
  ["FIRST CHECK", "if (score >= 90) {", "  console.log(\"Legendary\");", "} else if (score >= 70) {"],
  ["NEXT CHECKS", "  console.log(\"Hero\");", "} else if (score >= 50) {", "  console.log(\"Explorer\");"],
  ["FALLBACK", "} else {", "  console.log(\"Rookie\");", "}"],
]);
addNotes(4, "Point out the repeated structure: condition in parentheses, braces around each branch, and one final else without a condition. Do not live-code yet.", [conceptSource]);

setCards(5, "The computer checks top to bottom", "Example: score = 82", [
  ["1. START", "score = 82", "Begin at the top", "One ladder"],
  ["2. CHECK 90", "82 >= 90 is false", "Move down", "Nothing runs"],
  ["3. CHECK 70", "82 >= 70 is true", "Run Hero", "First true branch"],
  ["4. STOP", "Skip lower branches", "One result", "Hero wins"],
]);
addNotes(5, "Trace the example once as an explanation. Emphasize that the computer stops after the first true branch, even if a lower condition would also be true.", [conceptSource]);

setComparison(6, "Order changes the result", "AI-generated code still needs human testing", [
  ["95", "score"],
  ["1st", "true branch"],
  [">= 50", "catches 95"],
  ["Explorer", "wrong result"],
], [
  "WRONG ORDER",
  "if (score >= 50)",
  "else if (score >= 70)",
  "else if (score >= 90)",
  "95 stops too early",
], [
  "CORRECT ORDER",
  "if (score >= 90)",
  "else if (score >= 70)",
  "else if (score >= 50)",
  "95 reaches Legendary",
]);
addNotes(6, "Explain the AI connection: code can have valid syntax and still contain incorrect logic. Humans must compare the condition order with the written rules and test the result.", [conceptSource]);

setSix(7, "Boundary values reveal mistakes", "Check the edge and the number just below it", [
  "90 → Legendary",
  "89 → Hero",
  "70 → Hero",
  "69 → Explorer",
  "50 → Explorer",
  "49 → Rookie",
], "Testing proves that the code matches the written rules");
addNotes(7, "Introduce boundary testing as a concept. Exact edges and the values immediately below them are especially useful because they show whether >= and the threshold order match the intended rules.", [conceptSource]);

setText(8, "TextBox 14", "</>");
setText(8, "TextBox 15", "Concepts ready");
setText(8, "TextBox 17", "Now we open the Playground and code together.");
setText(8, "Rounded Rectangle 18", "Follow the Class Activity");
addNotes(8, "End the slide portion here. Open the TypeScript Playground and use the class activity for every recap, guided exercise, test, and discussion.", [playgroundSource]);

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
