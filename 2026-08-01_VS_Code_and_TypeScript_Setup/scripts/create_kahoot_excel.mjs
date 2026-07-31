import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputPath = process.argv[2];
const qaDir = process.argv[3];
if (!outputPath || !qaDir) {
  throw new Error("Usage: node create_kahoot_excel.mjs <output.xlsx> <qa-dir>");
}

const rows = [
  ["Which tool do we use to write and save our code?", "Node.js", "Visual Studio Code", "npm", "TypeScript Playground only", 20, 2],
  ["What is Node.js doing in today's workflow?", "Drawing the slide deck", "Installing Windows", "Running the JavaScript file", "Replacing VS Code", 20, 3],
  ["What does the tsc command do?", "Checks and compiles TypeScript", "Opens Microsoft Teams", "Deletes JavaScript", "Changes the computer password", 20, 1],
  ["What does a global TypeScript installation mean for our class?", "Only one file can use it", "It works only in the Playground", "It must be installed every Saturday", "The tsc command can be used in future folders", 20, 4],
  ["Which command checks whether Node.js is installed?", "node --version", "tsc --version", "code --version", "run node", 20, 1],
  ["Which file should a student edit?", "decisions.exe", "decisions.zip", "decisions.ts", "decisions.png", 20, 3],
  ["What file is created after compiling decisions.ts?", "decisions.js", "decisions.pdf", "decisions.pptx", "decisions.node", 20, 1],
  ["Which order is correct?", "Run JavaScript, save TypeScript, then compile", "Compile, delete the file, then write code", "Save TypeScript, compile it, then run JavaScript", "Run Node, install VS Code, then save", 20, 3],
  ["When does the code inside an if branch run?", "When its condition is true", "Every time, even when false", "Only after the final else", "Only in the browser", 20, 1],
  ["When is an else if condition checked?", "Before the first if", "After an earlier condition was false", "Only when every condition is true", "After the program closes", 20, 2],
  ["What is the job of the final else?", "Repeat the first branch", "Install TypeScript", "Run when no earlier condition was true", "Compare two numbers", 20, 3],
  ["How many branches run in one if / else if / else ladder?", "Every branch", "Exactly one branch", "No branches", "Always two branches", 20, 2],
  ["Why should score conditions usually go from highest to lowest?", "The first true branch wins", "Node requires alphabetical order", "TypeScript cannot read small numbers", "It makes the file download faster", 20, 1],
  ["An AI-written program compiles and runs. What should a human do next?", "Trust it immediately", "Delete every condition", "Test several values and verify the logic", "Submit it without reading", 20, 3],
  ["When should you trust a VS Code workspace?", "Whenever a stranger sends it", "When you created the folder or verified its source", "Every time VS Code asks", "Only after disabling security", 20, 2],
];

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("Kahoot Questions");
sheet.showGridLines = false;
sheet.freezePanes.freezeRows(1);

const headers = [
  "Question",
  "Answer 1",
  "Answer 2",
  "Answer 3",
  "Answer 4",
  "Time limit",
  "Correct answer",
];

sheet.getRange(`A1:G${rows.length + 1}`).values = [headers, ...rows];
sheet.getRange("A1:G1").format = {
  fill: "#061229",
  font: { bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center",
  verticalAlignment: "center",
};
sheet.getRange(`A2:G${rows.length + 1}`).format = {
  fill: "#F4F8FC",
  font: { color: "#152238" },
  verticalAlignment: "center",
  wrapText: true,
};
sheet.getRange(`A1:G${rows.length + 1}`).format.borders = {
  insideHorizontal: { style: "thin", color: "#CAD7E5" },
  bottom: { style: "thin", color: "#CAD7E5" },
};
sheet.getRange(`A1:A${rows.length + 1}`).format.columnWidth = 48;
sheet.getRange(`B1:E${rows.length + 1}`).format.columnWidth = 30;
sheet.getRange(`F1:G${rows.length + 1}`).format.columnWidth = 15;
sheet.getRange("A1:G1").format.rowHeight = 32;
sheet.getRange(`A2:G${rows.length + 1}`).format.rowHeight = 46;
sheet.getRange(`F2:G${rows.length + 1}`).format.horizontalAlignment = "center";

await fs.mkdir(path.dirname(outputPath), { recursive: true });
await fs.mkdir(qaDir, { recursive: true });

const inspect = await workbook.inspect({
  kind: "table",
  range: `Kahoot Questions!A1:G${rows.length + 1}`,
  include: "values,formulas",
  tableMaxRows: rows.length + 1,
  tableMaxCols: 7,
});
await fs.writeFile(path.join(qaDir, "kahoot.inspect.ndjson"), inspect.ndjson);

const preview = await workbook.render({
  sheetName: "Kahoot Questions",
  range: `A1:G${rows.length + 1}`,
  scale: 1,
  format: "png",
});
await fs.writeFile(
  path.join(qaDir, "kahoot-preview.png"),
  new Uint8Array(await preview.arrayBuffer()),
);

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});
await fs.writeFile(path.join(qaDir, "kahoot-errors.ndjson"), errors.ndjson);

const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(outputPath);
await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });
