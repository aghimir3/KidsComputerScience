# Windows Setup Guide: VS Code, Node.js, and TypeScript

**Class date:** August 1, 2026  
**Goal:** Install the tools once, then use them for future TypeScript classes.

Follow the teacher one step at a time. Stop at the first problem and ask for
help. Do not download substitute installers from search ads or unofficial
websites.

## 1. Install Visual Studio Code

1. Open the official page: https://code.visualstudio.com/docs/setup/windows
2. Download the **Windows User Installer** for your computer.
3. Open the downloaded `.exe` file.
4. Accept the agreement and keep the recommended options.
5. Finish the installation and open Visual Studio Code.

The User Installer is recommended for most students and normally does not need
administrator permission.

## 2. Install Node.js LTS

1. Open the official page: https://nodejs.org/en/download/
2. Choose the version marked **LTS**. Do not choose **Current**.
3. Download and open the Windows `.msi` installer.
4. Keep the recommended options and complete the installation.
5. Close and reopen Visual Studio Code.

Node.js runs the JavaScript file created by the TypeScript compiler. The Node
installer also installs `npm`, which installs TypeScript.

## 3. Open the Correct Terminal

1. In VS Code, select **Terminal > New Terminal**.
2. If the terminal says **PowerShell**, select the terminal dropdown.
3. Choose **Select Default Profile > Command Prompt**.
4. Open a new terminal.

We use Command Prompt during class to avoid PowerShell script-policy errors.

## 4. Check Node and npm

Run each command separately:

```text
node --version
npm --version
```

Both commands should print a version number. If either command says "not
recognized," close every VS Code window, reopen VS Code, and try again.

## 5. Install TypeScript Globally

Run this command once:

```text
npm install -g typescript
```

Then verify it:

```text
tsc --version
```

You should see a TypeScript version number. A global installation makes the
`tsc` command available in future class folders without reinstalling it.

## 6. Create the Class Folder

1. In VS Code, select **File > Open Folder**.
2. Create or choose a folder named `KidsComputerScience`.
3. Inside it, create `2026-08-01-decisions`.
4. Open that folder.
5. If Workspace Trust appears, choose **Yes, I trust the authors** because you
   created this folder yourself.
6. In the Explorer, create a file named `decisions.ts`.

## 7. Write, Compile, and Run

Add this code to `decisions.ts`:

```ts
let score: number = 82;

if (score >= 90) {
  console.log("Legend rank!");
} else if (score >= 70) {
  console.log("Hero rank!");
} else if (score >= 50) {
  console.log("Explorer rank!");
} else {
  console.log("Keep training!");
}
```

Save the file. In the VS Code terminal, compile it:

```text
tsc decisions.ts
```

A new file named `decisions.js` should appear. Run it:

```text
node decisions.js
```

The terminal should print `Hero rank!`.

## If Setup Is Blocked

- Record or screenshot the exact error.
- Ask the teacher or an assistant teacher before changing permissions.
- Do not share an administrator password with anyone.
- Continue the coding activity at https://www.typescriptlang.org/play
- You can earn full classwork credit through the Playground backup.

## Green Check List

- [ ] VS Code opens.
- [ ] `node --version` works.
- [ ] `npm --version` works.
- [ ] `tsc --version` works.
- [ ] `decisions.ts` is saved in the class folder.
- [ ] `tsc decisions.ts` creates `decisions.js`.
- [ ] `node decisions.js` prints an answer.

