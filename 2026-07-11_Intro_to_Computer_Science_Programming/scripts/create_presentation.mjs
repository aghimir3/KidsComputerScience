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
  if (!shape) throw new Error(`Missing inherited shape ${name}`);
  return shape;
}

function setText(slide, name, newText) {
  shapeByName(slide, name).text = newText;
}

function setShapeTop(slide, name, top) {
  const shape = shapeByName(slide, name);
  shape.position = {
    left: shape.position.left,
    top,
    width: shape.position.width,
    height: shape.position.height,
  };
}

function addSlideHeading(slideNumber, heading) {
  const slide = presentation.slides.items[slideNumber - 1];
  const headingBox = slide.shapes.add({
    geometry: "textbox",
    name: `slide-heading-${slideNumber}`,
    position: { left: 58, top: 23, width: 720, height: 28 },
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  headingBox.text = heading;
  headingBox.text.style = {
    fontSize: 18,
    bold: true,
    color: "#FFFFFF",
    typeface: "Source Code Pro",
    alignment: "left",
  };
}

function adjustDescriptionSpacing(slide) {
  setShapeTop(slide, "Google Shape;304;p30", 188);
  setShapeTop(slide, "Google Shape;302;p30", 300);
  setShapeTop(slide, "Google Shape;307;p30", 411);
}

function setContentSlide(slideNumber, headings, descriptions) {
  const slide = presentation.slides.items[slideNumber - 1];
  const pairs = [
    ["Google Shape;303;p30", `{${headings[0]}}`],
    ["Google Shape;304;p30", descriptions[0]],
    ["Google Shape;305;p30", `{${headings[1]}}`],
    ["Google Shape;302;p30", descriptions[1]],
    ["Google Shape;306;p30", `{${headings[2]}}`],
    ["Google Shape;307;p30", descriptions[2]],
  ];
  for (const [name, newText] of pairs) {
    setText(slide, name, newText);
  }
  adjustDescriptionSpacing(slide);
}

function setTransitionSlide(slideNumber, title, subtitle) {
  const slide = presentation.slides.items[slideNumber - 1];
  setText(slide, "Google Shape;214;p24", title);
  setText(slide, "Google Shape;215;p24", subtitle);
}

const titleSlide = presentation.slides.items[0];
setText(
  titleSlide,
  "Google Shape;214;p24",
  "Programming Adventure Begins",
);
setText(
  titleSlide,
  "Google Shape;215;p24",
  "July 11, 2026",
);

setText(
  presentation.slides.items[3],
  "Google Shape;248;p27",
  "Lead Software engineer at Flagship Financial Group\nAvid learner\nMasters in Software Engineering\nFOSS contributor - Bitcoin, Large Language Models, OpenAI",
);

setContentSlide(
  6,
  ["Meet", "Explore", "Create"],
  ["Learn who is here", "Teams, Kahoot, and breakout rooms", "Make music with code"],
);
addSlideHeading(6, "Today's mission");
setContentSlide(
  7,
  ["Say your name", "Share favorites", "Listen kindly"],
  ["City/state or country only", "Grade, subject, and hobby", "Passing is always okay"],
);
addSlideHeading(7, "Introduce yourself");
setContentSlide(
  8,
  ["Code.org", "TypeScript", "Projects"],
  ["Visual blocks make ideas move", "Writing code starts next week", "Build games, apps, and tools"],
);
addSlideHeading(8, "Programming starts with ideas");
setContentSlide(
  9,
  ["Class: 9-1", "Break: 10:30", "Typing: 11:00"],
  ["Saturdays, Pacific Time", "Rest and recharge", "Practice accuracy and speed"],
);
addSlideHeading(9, "Our Saturday class routine");
setContentSlide(
  10,
  ["Calendar", "Join the Team", "Ask for help"],
  ["Find the Saturday meeting", "Open Kids Computer Science", "Use chat or raise your hand"],
);
addSlideHeading(10, "Find class in Microsoft Teams");
setContentSlide(
  11,
  ["Updates", "Assignments", "Hangout"],
  ["Important teacher updates", "Find and submit assignments", "Join extra help after class"],
);
addSlideHeading(11, "Know the Teams channels");
setContentSlide(
  12,
  ["4:30-5:30", "Questions", "Join Hangout"],
  ["Pacific Time", "Homework, classwork, or setup", "Assistant teachers are ready to help"],
);
addSlideHeading(12, "Use hangout for extra help");
addSlideHeading(13, "Class habits that help everyone");
adjustDescriptionSpacing(presentation.slides.items[12]);

setTransitionSlide(14, "Kahoot time!", "15 fun questions. Learn the game.");
setTransitionSlide(15, "Break time", "Return at 11:00 AM Pacific.");
setTransitionSlide(16, "Typing practice", "Accuracy first. Speed comes later.");

setContentSlide(
  17,
  ["Captain", "Coach", "Reporter"],
  ["Keeps the crew on the mission", "Helps when someone gets stuck", "Shares one discovery"],
);
addSlideHeading(17, "Breakout room jobs");
setContentSlide(
  18,
  ["Own project", "Explain", "Everyone"],
  ["Work on your computer", "Help by asking questions", "A crew succeeds together"],
);
addSlideHeading(18, "How to work as a code crew");
setContentSlide(
  19,
  ["Music Lab", "Build a mix", "Try AI drums"],
  ["Use the link in Teams", "Combine at least two sounds", "Notice what changes"],
);
addSlideHeading(19, "Code.org Music Lab");
setContentSlide(
  20,
  ["Sequence", "Event", "Debug"],
  ["Steps run in an order", "An action starts something", "Find and fix a problem"],
);
addSlideHeading(20, "Programming words we will use");
setContentSlide(
  21,
  ["AI suggests", "You choose", "Humans lead"],
  ["Music Lab can generate beats", "Keep, change, or remix", "Creativity and judgment stay yours"],
);
addSlideHeading(21, "AI can help, but you decide");
setContentSlide(
  22,
  ["One discovery", "One project", "One shout-out"],
  ["What did your crew learn?", "Show a favorite moment", "Thank someone who helped"],
);
addSlideHeading(22, "Share what your crew made");

setTransitionSlide(23, "Final Kahoot", "Show what you learned today.");

setContentSlide(
  24,
  ["Finish levels", "Remix it", "Submit"],
  ["Complete the guided levels", "3 sounds, AI drums, 2 changes", "Link or screenshot in Teams"],
);
addSlideHeading(24, "Homework: Music Lab remix");
setContentSlide(
  25,
  ["TypeScript", "Write code", "Build together"],
  ["Our programming language", "Start with small, clear steps", "Questions are always welcome"],
);
addSlideHeading(25, "Next week we start TypeScript");
setTransitionSlide(26, "Great first day!", "See you next Saturday.");

await fs.mkdir(path.dirname(outputPath), { recursive: true });
await fs.mkdir(path.join(qaDir, "slides"), { recursive: true });
await fs.mkdir(path.join(qaDir, "layout"), { recursive: true });

for (const [index, slide] of presentation.slides.items.entries()) {
  const stem = `slide-${String(index + 1).padStart(2, "0")}`;
  const png = await presentation.export({ slide, format: "png", scale: 1 });
  await fs.writeFile(
    path.join(qaDir, "slides", `${stem}.png`),
    new Uint8Array(await png.arrayBuffer()),
  );
  const layout = await slide.export({ format: "layout" });
  await fs.writeFile(
    path.join(qaDir, "layout", `${stem}.layout.json`),
    await layout.text(),
  );
}

const montage = await presentation.export({
  format: "webp",
  montage: true,
  scale: 1,
});
await fs.writeFile(
  path.join(qaDir, "deck-montage.webp"),
  new Uint8Array(await montage.arrayBuffer()),
);

const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(outputPath);
await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });

console.log(`Created ${outputPath}`);
