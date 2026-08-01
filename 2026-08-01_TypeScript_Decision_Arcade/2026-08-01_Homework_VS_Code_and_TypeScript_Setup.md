# Homework: Install Your TypeScript Coding Workspace

**Assigned:** August 1, 2026  
**Due:** August 8, 2026  
**Points:** 100 points + 5 bonus points

## Homework Goal

Install Visual Studio Code, Node.js LTS, and TypeScript once so future class
folders can use the same local coding tools.

Choose the detailed guide for your computer:

- Windows: `2026-08-01_Windows_Setup_Guide.md`
- macOS: `2026-08-01_macOS_Setup_Guide.md`

Use only the official links in the guide. Never download from a search ad or an
unofficial website.

## Help Is Available

If a step is blocked:

1. Stop instead of changing random permissions.
2. Copy or screenshot the exact error.
3. Continue any written questions you can complete.
4. Bring the error to the **Hangout Session channel from 4:30-5:30 PM Pacific**,
   as scheduled in Microsoft Teams.

An installation restriction is not a failure. Clear evidence of the attempted
step and exact error earns process credit while you get help.

Never share an administrator password with a teacher, classmate, screenshot,
chat, or assignment.

## Part 1 - Choose a Safe Setup Path (10 points)

Record:

- Your operating system: Windows or macOS
- The setup guide you selected
- Why official download pages are safer than random download sites
- What you will do if the computer asks for a password or blocks a step

## Part 2 - Install Visual Studio Code (20 points)

Follow the operating-system guide.

### Windows goal

- Install the recommended **User Installer** from the official VS Code page.
- Open Visual Studio Code.
- Open the integrated terminal.
- Use **Command Prompt** for this homework.

### macOS goal

- Download VS Code from the official macOS page.
- Open the `.dmg`.
- Drag Visual Studio Code to Applications.
- Open VS Code from Applications.
- Open the integrated `zsh` terminal.

Record:

- Did VS Code open successfully?
- If not, what exact message appeared?
- One part of the VS Code window you can identify

## Part 3 - Install Node.js LTS (20 points)

1. Open https://nodejs.org/en/download/.
2. Choose the release marked **LTS**, not **Current**.
3. Use the normal installer for your operating system.
4. Finish the installation.
5. Close every VS Code window and reopen VS Code.
6. Open a new terminal.

Run:

```text
node --version
npm --version
```

Record both version outputs or the exact error.

Explain the job of:

- Node.js
- npm

## Part 4 - Install TypeScript Globally (20 points)

In the VS Code terminal, run:

```text
npm install -g typescript
```

Then verify:

```text
tsc --version
```

Record the TypeScript version or the exact error.

Explain what **global** means for our beginner class workflow.

Windows students: if PowerShell shows a script-policy error, switch the VS Code
terminal profile to **Command Prompt**. Do not change Windows security policy.

macOS students: if npm reports `EACCES` or a permission error, stop and use the
help steps in the macOS guide. Never reveal a password.

## Part 5 - Create, Compile, and Run a Local File (20 points)

1. Create a folder named `KidsComputerScience`.
2. Create `2026-08-01-homework-setup` inside it.
3. Open the dated folder in VS Code.
4. Trust the folder only because you created it.
5. Create `local-ready.ts`.
6. Type:

```ts
const coderName: string = "Coder";
let score: number = 82;

if (score >= 90) {
  console.log(`${coderName}: Legend rank!`);
} else if (score >= 70) {
  console.log(`${coderName}: Hero rank!`);
} else if (score >= 50) {
  console.log(`${coderName}: Explorer rank!`);
} else {
  console.log(`${coderName}: Keep training!`);
}
```

Save the file, then run:

```text
tsc local-ready.ts
node local-ready.js
```

Record:

- The compiler command
- The generated filename
- The run command
- The terminal output

## Part 6 - Evidence and Reflection (10 points)

Provide safe evidence of your progress:

- The three version outputs, or exact errors
- Your `local-ready.ts` code
- The terminal output, if the program ran

Answer:

1. Which tool is the editor?
2. Which tool checks and compiles TypeScript?
3. Which tool runs the generated JavaScript?
4. Which step would you bring to the Hangout Session if you needed help?

Do not include passwords, private folder names, email addresses, or other
personal information in screenshots.

## Bonus - Personalize the First Local Program (5 points)

Change the coder name and rank messages. Test two scores that reach different
branches. Record both outputs.

## Submission

Submit the completed homework to:

1. Microsoft Teams
2. Ishwari Raut ma'am

Submit the completed PDF or written response plus your `.ts` file or safe
screenshots. If setup is blocked, submit the exact error and your planned next
step, then use the Hangout Session for help.
