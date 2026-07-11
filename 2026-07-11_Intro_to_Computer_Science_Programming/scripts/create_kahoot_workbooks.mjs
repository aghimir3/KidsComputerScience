import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = process.argv[2];
const previewDir = process.argv[3];
if (!outputDir || !previewDir) {
  throw new Error("Usage: node create_kahoot_workbooks.mjs <output-dir> <preview-dir>");
}

const FUN = [
  ["Which planet do we live on?", "Mars", "Earth", "Venus", "Jupiter", 20, 2],
  ["What is 5 + 7?", "10", "11", "12", "13", 20, 3],
  ["Which animal is known for black and white stripes?", "Zebra", "Giraffe", "Elephant", "Dolphin", 20, 1],
  ["Which device can move the pointer on a computer?", "Speaker", "Printer", "Mouse", "Microphone", 20, 3],
  ["What color can you make by mixing blue and yellow?", "Purple", "Orange", "Pink", "Green", 20, 4],
  ["How many minutes are in one hour?", "30", "45", "60", "100", 20, 3],
  ["Which is the largest planet in our solar system?", "Earth", "Saturn", "Mars", "Jupiter", 20, 4],
  ["What number comes next: 2, 4, 6, 8, ___?", "9", "10", "11", "12", 20, 2],
  ["Which game is famous for blocks, crafting, and Creepers?", "Minecraft", "Rocket League", "Tetris", "Mario Kart", 20, 1],
  ["Which keyboard key usually starts a new line?", "Shift", "Tab", "Enter", "Spacebar", 20, 3],
  ["What does WWW stand for?", "World Wide Web", "Web World Window", "Worldwide Wireless", "Wide Web Workspace", 20, 1],
  ["Which is a renewable source of energy?", "Coal", "Sunlight", "Gasoline", "Natural gas", 20, 2],
  ["What is frozen water called?", "Steam", "Rain", "Ice", "Fog", 20, 3],
  ["Which tool can create text from a written prompt?", "Calculator", "Stopwatch", "File explorer", "AI assistant", 20, 4],
  ["What matters most in today's practice Kahoot?", "Getting every answer perfect", "Learning the game and having fun", "Finishing before everyone else", "Memorizing your final score", 20, 2],
];

const CLOSING = [
  ["When is our regular Saturday class?", "8 AM-10 AM Pacific", "9 AM-1 PM Pacific", "1 PM-4 PM Pacific", "4:30 PM-5:30 PM Pacific", 20, 2],
  ["Where can you find the Saturday class meeting?", "Teams Calendar", "Calculator", "File Explorer", "Code.org Music Lab", 20, 1],
  ["Which Teams channel contains important teacher updates?", "Homework", "Hangout Session", "Announcements", "Classwork", 20, 3],
  ["Which Teams channel should you check for after-class assignments?", "Announcements", "Homework", "Classwork", "Hangout Session", 20, 2],
  ["Where do you join an assistant-teacher help session?", "Homework channel", "Calendar settings", "Announcements channel", "Hangout Session channel", 20, 4],
  ["When is the assistant-teacher hangout session?", "4:30 PM-5:30 PM Pacific", "9 AM-10 AM Pacific", "10:30 AM-11 AM Pacific", "11 AM-11:30 AM Pacific", 20, 1],
  ["What is a sequence in programming?", "A computer password", "Steps arranged in an order", "A type of keyboard", "A Teams channel", 20, 2],
  ["What does debugging mean?", "Turning off the internet", "Decorating a program", "Finding and fixing a problem", "Deleting every block", 20, 3],
  ["How did AI appear in Music Lab today?", "It generated drum beats", "It graded the Kahoot", "It opened Teams", "It typed student names", 20, 1],
  ["Which programming language do we begin next week?", "Python", "Java", "C++", "TypeScript", 20, 4],
];

async function buildWorkbook(filename, title, rows) {
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
    fill: "#4F2683",
    font: { bold: true, color: "#FFFFFF" },
    horizontalAlignment: "center",
    verticalAlignment: "center",
  };
  sheet.getRange(`A2:G${rows.length + 1}`).format = {
    fill: "#F7F4FB",
    font: { color: "#242830" },
    verticalAlignment: "center",
    wrapText: true,
  };
  sheet.getRange(`A1:G${rows.length + 1}`).format.borders = {
    insideHorizontal: { style: "thin", color: "#D8D1E4" },
    bottom: { style: "thin", color: "#D8D1E4" },
  };
  sheet.getRange(`A1:A${rows.length + 1}`).format.columnWidth = 46;
  sheet.getRange(`B1:E${rows.length + 1}`).format.columnWidth = 28;
  sheet.getRange(`F1:G${rows.length + 1}`).format.columnWidth = 14;
  sheet.getRange("A1:G1").format.rowHeight = 30;
  sheet.getRange(`A2:G${rows.length + 1}`).format.rowHeight = 42;
  sheet.getRange(`F2:G${rows.length + 1}`).format.horizontalAlignment = "center";

  const preview = await workbook.render({
    sheetName: "Kahoot Questions",
    range: `A1:G${rows.length + 1}`,
    scale: 1,
    format: "png",
  });
  await fs.writeFile(
    path.join(previewDir, `${filename}.png`),
    new Uint8Array(await preview.arrayBuffer()),
  );

  const inspect = await workbook.inspect({
    kind: "table",
    range: `Kahoot Questions!A1:G${rows.length + 1}`,
    include: "values,formulas",
    tableMaxRows: rows.length + 1,
    tableMaxCols: 7,
  });
  await fs.writeFile(path.join(previewDir, `${filename}.inspect.ndjson`), inspect.ndjson);

  const outputPath = path.join(outputDir, `${filename}.xlsx`);
  const xlsx = await SpreadsheetFile.exportXlsx(workbook);
  await xlsx.save(outputPath);
  await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });
  console.log(`Created ${title}`);
}

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });
await buildWorkbook("2026-07-11_Fun_Kahoot_Import", "Fun Practice Kahoot", FUN);
await buildWorkbook("2026-07-11_Closing_Kahoot_Import", "Closing Kahoot", CLOSING);
