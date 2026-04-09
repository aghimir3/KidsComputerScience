# Class Activity: Command Line Translator (Instructor-Led)

**Date:** February 28, 2026
**Topic:** Windows & Mac Command Line — Everything Connects
**Duration:** ~45-60 minutes (before classwork)
**Format:** Instructor demonstrates via MS Teams screenshare, students follow along on their OWN machines

---

## Overview

Students spent 2 weeks on Linux via DistroSea. Today they discover that the same concepts work on their own computers — just with different syntax. This demo walks them through opening a terminal, running commands, and seeing familiar results.

**Remote Teaching Tips:**
- Have CMD or Terminal open and zoomed in (150%+)
- Type slowly and narrate every command
- Pause after each command so students can try it on their machines
- Ask "Did that work?" after each step — some students may get errors
- If a student has a Mac, they can follow along with the Linux/Mac column

---

## Before You Start: Quick Check (2 minutes)

Ask in chat:
- "Who has Windows?"
- "Who has Mac?"
- "Who has both?"

> This helps you know which commands to emphasize. Most students will likely be on Windows.

---

## Demo 1: Opening the Terminal (5 minutes)

### Windows
1. Press `Win + R` (show the Run dialog)
2. Type `cmd` and press Enter
3. "This is Command Prompt — Windows' version of the terminal"

### Mac
1. Press `Cmd + Space` (opens Spotlight)
2. Type `Terminal` and press Enter
3. "This is Terminal — and here's the secret: it uses the SAME commands as Linux!"

### Key Point
> "Every operating system has a terminal. The idea is the same — you type commands to talk to your computer. Only the words change."

### Quick Check
- "Can everyone see a blinking cursor? Type 'hello' and press Enter. What happened?"
- (It will say "'hello' is not recognized" — good! That proves the terminal is listening.)

---

## Demo 2: Where Am I? (5 minutes)

### What You Learned on Linux
```
pwd          # prints current directory
```

### On Windows
```
cd           # (with no arguments) shows current directory
```

### On Mac
```
pwd          # same as Linux!
```

**Demo it live:**
1. Type `cd` on Windows (or `pwd` on Mac)
2. Point out the path: `C:\Users\YourName`
3. "Notice Windows uses BACKSLASHES `\` and starts with `C:\`"
4. "Linux and Mac use FORWARD SLASHES `/` and start from `/home/`"

### Quick Check
- "What directory are you in right now? Type it in chat!"

---

## Demo 3: Listing Files (5 minutes)

### Linux → Windows Translation
```
Linux:     ls
Windows:   dir
Mac:       ls       (same as Linux!)
```

**Demo it live:**
1. Type `dir` on Windows (or `ls` on Mac)
2. "Look — you can see files and folders, just like `ls` on Linux!"
3. Point out the differences: Windows shows dates, sizes, `<DIR>` for folders

### Key Point
> "Same idea, different word. `ls` and `dir` do the exact same thing."

---

## Demo 4: Creating Folders and Files (10 minutes)

### Step 1: Create a folder
```
Linux:     mkdir demo_folder
Windows:   mkdir demo_folder       (same!)
Mac:       mkdir demo_folder       (same!)
```

**Demo it:** "Hey, `mkdir` works EVERYWHERE! Some commands are universal."

### Step 2: Navigate into it
```
Linux:     cd demo_folder
Windows:   cd demo_folder          (same!)
Mac:       cd demo_folder          (same!)
```

**Demo it:** "And `cd` works everywhere too!"

### Step 3: Create an empty file
```
Linux:     touch hello.txt
Windows:   echo. > hello.txt       (no touch command!)
Mac:       touch hello.txt         (same as Linux!)
```

**Demo it live on Windows:**
1. Type `echo. > hello.txt`
2. "On Linux we used `touch`. Windows doesn't have `touch`, so we use this trick instead."
3. Type `dir` to confirm the file was created

### Step 4: Write text into the file
```
Linux:     echo "I love CS" > hello.txt
Windows:   echo I love CS > hello.txt      (no quotes needed)
Mac:       echo "I love CS" > hello.txt    (same as Linux)
```

### Step 5: View the file
```
Linux:     cat hello.txt
Windows:   type hello.txt
Mac:       cat hello.txt           (same as Linux!)
```

**Demo it:**
1. Type `type hello.txt` on Windows
2. "On Linux we used `cat`. Windows uses `type`. Same idea!"

### Quick Check
- "Can everyone create a file and read it back? Try it now!"
- Give students 1-2 minutes to try on their machines

---

## Demo 5: Copy, Move, Rename, Delete (10 minutes)

### Copy a file
```
Linux:     cp hello.txt backup.txt
Windows:   copy hello.txt backup.txt
Mac:       cp hello.txt backup.txt
```

**Demo it:** Type `copy hello.txt backup.txt` on Windows, then `dir` to confirm.

### Rename a file
```
Linux:     mv old.txt new.txt
Windows:   ren old.txt new.txt         (different command!)
Mac:       mv old.txt new.txt
```

**Demo it:** Type `ren backup.txt copy.txt` on Windows, then `dir`.

"On Linux and Mac, `mv` does double duty — it moves AND renames. Windows has a separate `ren` command just for renaming."

### Move a file
```
Linux:     mv file.txt folder/
Windows:   move file.txt folder\
Mac:       mv file.txt folder/
```

### Delete a file
```
Linux:     rm file.txt
Windows:   del file.txt
Mac:       rm file.txt
```

**Demo it:** Type `del copy.txt` on Windows, then `dir` to confirm it's gone.

### Clean up
```
cd ..
rmdir demo_folder        (works on all three!)
```

> "And `rmdir` works everywhere — another universal command!"

### Quick Check
- "How many commands work the SAME on all three systems?" (mkdir, cd, rmdir, ping, nslookup)

---

## Demo 6: The Three Key Differences (5 minutes)

Write these on screen or show the slide:

### 1. Backslash vs Forward Slash
```
Windows:   C:\Users\Student\Documents
Linux/Mac: /home/student/documents
```

### 2. Case Sensitivity
```
Windows:   MyFile.txt = myfile.txt = MYFILE.TXT    (all the same!)
Linux/Mac: MyFile.txt ≠ myfile.txt ≠ MYFILE.TXT    (all different!)
```

**Demo it live:** On Windows, create `Test.txt`, then type `type test.txt` — it works! "Windows doesn't care about uppercase or lowercase."

### 3. Different Command Names
```
ls → dir       cat → type       rm → del       cp → copy       clear → cls
```

### 4. Drive Letters
```
Windows:   C:\   D:\   E:\     (each drive has a letter)
Linux/Mac: /     /home  /mnt   (everything starts from /)
```

---

## Demo 7: Networking Commands Revisited (5 minutes)

"Remember back in January when you used `ipconfig` and `ping`? Those are Windows commands! Let's connect the dots."

### Show the translation
```
Windows:    ipconfig          Mac/Linux:  ifconfig
Windows:    tracert site      Mac/Linux:  traceroute site
ALL:        ping site         (same everywhere!)
ALL:        nslookup site     (same everywhere!)
```

**Demo it live:**
1. Run `ipconfig` on Windows (or `ifconfig` on Mac)
2. "You already know this one from January! Now you know the Mac/Linux version too."

### Quick Check
- "Which networking command works on ALL operating systems?" (ping, nslookup)

---

## Demo 8: Windows Bonus — Task Manager & systeminfo (5 minutes)

### Task Manager
1. Press `Ctrl + Shift + Esc`
2. "This shows everything running on your computer — like a dashboard"
3. Show the Processes tab: "See how much CPU and memory each app uses"

### systeminfo Command
1. In CMD, type `systeminfo`
2. "This tells you everything about your computer"
3. Point out: OS name, computer name, total RAM, processor

### Mac Equivalent
- "On Mac, you can run `sw_vers` to see your macOS version"
- "Or `system_profiler SPHardwareDataType` for full hardware details"

---

## Demo 9: Mac's Secret — It's Unix! (3 minutes)

"Here's something cool. Why do Mac Terminal and Linux use the same commands?"

Draw or show:
```
         Unix (1970s)
        /           \
    Linux            macOS
  (free, open)    (Apple's version)
```

> "Mac and Linux are both based on Unix. That's why `ls`, `cd`, `cat`, `cp`, `mv`, `rm`, `touch` — they ALL work on Mac. Mac Terminal IS basically Linux."

### Key Takeaway
> "If you learn Linux commands, you already know Mac commands. If you learn Windows commands, you can use any Windows PC. And the CONCEPTS are the same everywhere — only the syntax changes."

---

## Demo 10: AI Meets the Command Line (5 minutes)

"So why does learning the terminal matter beyond just managing files? Let me show you something cool."

### AI Runs on Linux Terminals

"Remember in January when we learned about cloud data centers? ChatGPT, Claude, Gemini — all the AI models you use — they train on THOUSANDS of Linux servers in those data centers. Engineers control those servers using the exact same terminal commands you've been learning: `ls`, `cd`, `mkdir`, `cp`."

### Developers Use AI THROUGH the Terminal

"Here's where it gets really interesting. The newest AI tools don't even use a website — they run right inside the terminal!"

Show or describe:
- **Claude Code** (by Anthropic): "You open your terminal, type a question, and Claude helps you write code. No browser needed — it's all in the command line."
- **Codex CLI** (by OpenAI): "Same idea — OpenAI made a tool where you talk to AI directly in your terminal."

### Key Point
> "The terminal you are learning RIGHT NOW is the same interface that real AI engineers and developers use every single day. When we start learning about AI in April, you'll already know how to use the tools."

### Quick Prompt
- "Why do you think AI developers chose the terminal instead of a website for these tools?"
- (Let students speculate — speed, power, automation, no mouse needed)

---

## Transition to Classwork (2 minutes)

"Now it's YOUR turn. I'm going to give you a classwork assignment where you'll:
1. Translate Linux commands to Windows/Mac
2. Run real commands on YOUR computer
3. Try networking commands again

Open the classwork PDF I'm posting in Teams. You have about an hour. Ask me if you get stuck!"

**Post in Teams:**
- Classwork PDF
- Remind students: "You need Command Prompt or Terminal open alongside the PDF"

---

## Troubleshooting Tips

### If a student can't open CMD:
- Try searching "Command Prompt" in the Start menu
- Or press `Win + S` and type "cmd"
- Some school-managed devices may block CMD — have the student watch and follow along

### If a command gives "Access Denied":
- This happens on restricted accounts
- Skip that task and move on — it's not the student's fault
- They can still complete the translation/theory questions

### If `ping` runs forever on Windows:
- Press `Ctrl + C` to stop it
- Or use `ping -n 4 google.com` to send only 4 pings

### If a Mac student is confused:
- Reassure them: "Almost everything is the same as Linux! Just use the Linux column."
- The only Mac-specific things are `ifconfig` (vs `ipconfig`) and `sw_vers`

### If activity runs long:
- Skip Demo 8 (Task Manager / systeminfo) — students will discover it in classwork/homework
- Demo 4 and 5 are the highest value

### If activity runs short:
- Have students try `cls` (Windows) or `clear` (Mac) to clear the screen
- Show `echo %USERNAME%` (Windows) or `whoami` (Mac/Linux) to see their username
- Challenge: "Can anyone figure out how to append text to a file?" (`>>`)

---

## Materials Checklist

### MS Teams Setup
- [ ] Meeting started and students joined
- [ ] Screen sharing enabled
- [ ] CMD or Terminal open, zoomed to 150%+
- [ ] Notifications silenced

### Ready to Share
- [ ] Classwork PDF uploaded to Teams
- [ ] Homework PDF ready (assign at end of class)

### On Your Screen
- [ ] Command Prompt (or Terminal) open
- [ ] Slides open for reference (translation tables)
- [ ] This activity guide open for reference

---

*By the end of this demo, students should feel confident that their Linux skills transfer directly to their own computers.*
