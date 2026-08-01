# macOS Homework Setup Guide

**Goal:** Install VS Code, Node.js LTS, and TypeScript once, then run a local
TypeScript file.  
**Official references:**

- https://code.visualstudio.com/docs/setup/mac
- https://nodejs.org/en/download/
- https://www.typescriptlang.org/download/

## Before You Start

- Ask a parent or guardian before approving an installer.
- Never share the computer administrator password.
- Download only from the official links above.
- If a step is blocked, save the exact error and use the 4:30-5:30 PM Pacific
  Hangout Session in Microsoft Teams for help.

## Step 1 - Install Visual Studio Code

1. Open https://code.visualstudio.com/docs/setup/mac.
2. Download Visual Studio Code for macOS. The Universal build supports both
   Apple silicon and Intel-based Macs.
3. Open the downloaded `.dmg` file.
4. Drag `Visual Studio Code.app` into Applications.
5. Open VS Code from Applications.

Checkpoint: VS Code opens and shows the Welcome screen.

## Step 2 - Install Node.js LTS

1. Open https://nodejs.org/en/download/.
2. Choose the version marked **LTS**. Do not choose **Current**.
3. Download the normal macOS installer for your computer.
4. Open the installer and keep the normal choices.
5. Finish the installation.
6. Close every VS Code window.
7. Reopen VS Code.

Node.js runs JavaScript. Its installer also provides `npm`, which we use to
install TypeScript.

## Step 3 - Open the VS Code Terminal

Choose **Terminal > New Terminal**. The normal macOS shell should say `zsh`.

Run one command at a time:

```text
node --version
npm --version
```

Both commands should print a version number.

If a command is not found:

1. Close every VS Code window.
2. Reopen VS Code.
3. Open a new terminal.
4. Try again.
5. If it still fails, record the exact error and ask for help in the Hangout
   Session.

## Step 4 - Install TypeScript Globally

Try this command first:

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

### If macOS Reports `EACCES` or a Permission Error

Stop and save the exact error. Do not repeatedly change permissions.

With parent, guardian, or teacher approval, the documented class fallback is:

```text
sudo npm install -g typescript
```

macOS may ask for the computer administrator password. Nothing appears while
the password is typed. Never say, display, screenshot, or send the password.
Do not use `sudo` for other class commands.

If you are unsure, wait for the Hangout Session instead.

## Step 5 - Create the Homework Folder

1. In VS Code, choose **File > Open Folder**.
2. Create or choose `KidsComputerScience`.
3. Create `2026-08-01-homework-setup` inside it.
4. Open the dated folder.
5. If Workspace Trust appears, trust the folder only because you created it.
6. Create `local-ready.ts` in the Explorer.

## Step 6 - Type the First Local Program

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

## macOS Troubleshooting

### `node` or `npm` is not found

Restart VS Code after confirming that the Node.js LTS installer finished.

### The global install reports a permission error

Stop, record the error, and use the approved help path above. Never reveal a
password.

### `tsc` is not found

Confirm the global install finished, open a new terminal, and retry
`tsc --version`.

### `tsc local-ready.ts` prints nothing

That can mean it worked. Look for `local-ready.js` in the Explorer.

### Node cannot find `local-ready.js`

Confirm the terminal is inside the homework folder and that the generated file
appears in the Explorer.

## Green Check List

- [ ] VS Code opens from Applications.
- [ ] The terminal uses `zsh`.
- [ ] `node --version` works.
- [ ] `npm --version` works.
- [ ] `tsc --version` works.
- [ ] `local-ready.ts` is saved.
- [ ] `tsc local-ready.ts` creates `local-ready.js`.
- [ ] `node local-ready.js` prints a message.

If a box remains unchecked, save the exact error and bring it to the Hangout
Session.
