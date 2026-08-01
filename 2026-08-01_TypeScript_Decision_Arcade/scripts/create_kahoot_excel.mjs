import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputPath = process.argv[2];
const qaDir = process.argv[3];
if (!outputPath || !qaDir) {
  throw new Error("Usage: node create_kahoot_excel.mjs <output.xlsx> <qa-dir>");
}

const rows = [
  ["Which tool did we use to run TypeScript during class?", "TypeScript Playground", "Microsoft Word", "File Explorer", "Calculator", 20, 1],
  ["Which declaration correctly stores a number?", "const score: string = 82;", "const score: number = 82;", "const score: boolean = 82;", "const score = \"number\";", 20, 2],
  ["What type of value does score >= 70 produce?", "string", "number", "boolean", "console", 20, 3],
  ["What does an if / else statement choose between?", "Two possible branches", "Two variable names", "Two TypeScript files", "Two web browsers", 20, 1],
  ["When is an else if condition checked?", "Before the if condition", "After an earlier condition is false", "Only after the final else", "Every time a variable is created", 20, 2],
  ["In what order does an else if ladder check conditions?", "Bottom to top", "Random order", "Top to bottom", "Alphabetical order", 20, 3],
  ["What happens when the ladder finds its first true condition?", "That branch runs and the ladder stops", "Every remaining branch runs", "The program deletes the variable", "The ladder starts again at the top", 20, 1],
  ["What rank does score 82 receive: 90+ Legendary, 70+ Hero, 50+ Explorer?", "Legendary", "Hero", "Explorer", "Rookie", 20, 2],
  ["Why should we test an exact boundary such as 70?", "To check whether the rule includes that value", "To make the code use more memory", "To rename the Playground", "To turn a number into text", 20, 1],
  ["What rank does exactly 70 receive: 90+ Legendary, 70+ Hero, 50+ Explorer?", "Legendary", "Hero", "Explorer", "Rookie", 20, 2],
  ["What is the job of the final else?", "Handle values not matched earlier", "Check the highest condition again", "Create a number variable", "Always run before if", 20, 1],
  ["An AI draft checks score >= 50 before score >= 90. What will it label 95?", "Legendary", "Hero", "Explorer", "Rookie", 20, 3],
  ["If code runs without an error, what is still possible?", "Its decision logic may still be wrong", "Every output must be correct", "It cannot contain comparisons", "It automatically installs VS Code", 20, 1],
  ["Which plan matches this lesson?", "Playground in class; local setup for homework", "Local setup in class; no homework", "Word in class; Playground for homework", "No coding in class or at home", 20, 1],
  ["Where can students get help with setup problems?", "Hangout, 4:30–5:30 PM Pacific", "Share a password in chat", "Download from advertisements", "Change security settings alone", 20, 1],
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

const fullRange = `A1:G${rows.length + 1}`;
sheet.getRange(fullRange).values = [headers, ...rows];
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
sheet.getRange(fullRange).format.borders = {
  insideHorizontal: { style: "thin", color: "#CAD7E5" },
  bottom: { style: "thin", color: "#CAD7E5" },
};
sheet.getRange(`A2:A${rows.length + 1}`).format.fill = "#EAF5FB";
sheet.getRange(`G2:G${rows.length + 1}`).format.fill = "#EAF8F2";
sheet.getRange(`G2:G${rows.length + 1}`).format.font = { bold: true, color: "#007A50" };
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
  range: `Kahoot Questions!${fullRange}`,
  include: "values,formulas",
  tableMaxRows: rows.length + 1,
  tableMaxCols: 7,
});
await fs.writeFile(path.join(qaDir, "kahoot.inspect.ndjson"), inspect.ndjson);

const preview = await workbook.render({
  sheetName: "Kahoot Questions",
  range: fullRange,
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
