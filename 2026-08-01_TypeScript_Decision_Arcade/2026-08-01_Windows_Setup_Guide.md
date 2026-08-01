# Windows Homework Setup Guide

**Goal:** Install VS Code, Node.js LTS, and TypeScript once, then run a local
TypeScript file.  
**Official references:**

- https://code.visualstudio.com/docs/setup/windows
- https://nodejs.org/en/download/
- https://www.typescriptlang.org/download/

## Before You Start

- Use a Windows account that is allowed to install applications.
- Ask a parent or guardian before approving an installer.
- Never share an administrator password.
- Download only from the official links above.
- If a step is blocked, save the exact error and use the 4:30-5:30 PM Pacific
  Hangout Session in Microsoft Teams for help.

## Step 1 - Install Visual Studio Code

1. Open https://code.visualstudio.com/docs/setup/windows.
2. Choose the **User Installer**. Microsoft recommends User setup for most
   people, and it normally does not require administrator permission.
3. Open `VSCodeUserSetup-{version}.exe`.
4. Accept the agreement.
5. Keep the normal setup choices.
6. Finish the installation and open VS Code.

Checkpoint: VS Code opens and shows the Welcome screen.

## Step 2 - Install Node.js LTS

1. Open https://nodejs.org/en/download/.
2. Choose the version marked **LTS**. Do not choose **Current**.
3. Download the Windows installer for your computer.
4. Run the installer and keep the normal choices.
5. Finish the installation.
6. Close every VS Code window.
7. Reopen VS Code.

Node.js runs JavaScript. Its installer also provides `npm`, which we use to
install TypeScript.

## Step 3 - Use Command Prompt in VS Code

1. Choose **Terminal > New Terminal**.
2. If the terminal says PowerShell, open the terminal dropdown.
3. Choose **Select Default Profile**.
4. Choose **Command Prompt**.
5. Open a new terminal.

We use Command Prompt to avoid PowerShell script-policy errors. Do not change
the Windows execution policy for this assignment.

## Step 4 - Verify Node.js and npm

Run one command at a time:

```text
node --version
npm --version
```

Both commands should print a version number.

If a command is not recognized:

1. Close every VS Code window.
2. Reopen VS Code.
3. Open a new Command Prompt terminal.
4. Try again.
5. If it still fails, record the exact error and ask for help in the Hangout
   Session.

## Step 5 - Install TypeScript Globally

Run once:

```text
npm install -g typescript
```

Then verify:

```text
tsc --version
```

The official TypeScript documentation supports this global installation for
using `tsc` anywhere in the terminal. Our beginner class uses it so future
lesson folders do not need another TypeScript install.

## Step 6 - Create the Homework Folder

1. In VS Code, choose **File > Open Folder**.
2. Create or choose `KidsComputerScience`.
3. Create `2026-08-01-homework-setup` inside it.
4. Open the dated folder.
5. If Workspace Trust appears, trust the folder only because you created it.
6. Create `local-ready.ts` in the Explorer.

## Step 7 - Type the First Local Program

Type the code from Part 5 of the homework. Save the file.

Compile:

```text
tsc local-ready.ts
```

A new `local-ready.js` file should appear.

Run:

```text
node local-ready.js
```

The terminal should print a rank message.

## Windows Troubleshooting

### PowerShell says scripts are disabled

Switch the VS Code terminal to **Command Prompt**. Do not change the security
policy.

### `node` or `npm` is not recognized

Restart VS Code after confirming that the Node.js LTS installer finished.

### `tsc` is not recognized

Confirm the global install finished, open a new terminal, and retry
`tsc --version`.

### `tsc local-ready.ts` prints nothing

That can mean it worked. Look for `local-ready.js` in the Explorer.

### Node cannot find `local-ready.js`

Confirm the terminal is inside the homework folder and that the generated file
appears in the Explorer.

## Green Check List

- [ ] VS Code opens.
- [ ] The terminal is Command Prompt.
- [ ] `node --version` works.
- [ ] `npm --version` works.
- [ ] `tsc --version` works.
- [ ] `local-ready.ts` is saved.
- [ ] `tsc local-ready.ts` creates `local-ready.js`.
- [ ] `node local-ready.js` prints a message.

If a box remains unchecked, save the exact error and bring it to the Hangout
Session.
