# Class Activity: Cybersecurity Challenge Lab (Instructor-Led)

**Date:** March 21, 2026
**Topic:** Cybersecurity — Passwords, Phishing, Social Engineering & AI
**Duration:** ~60-75 minutes (after slides, before classwork)
**Format:** Interactive challenges via MS Teams — students participate through chat, screen demos, and live exercises

---

## Overview

This is NOT a lecture — the slides already cover the concepts. This activity puts students in the hot seat with live challenges, games, and demos that make cybersecurity feel real. Students compete, vote, investigate, and test their own security.

**Key Principle:** Students learn cybersecurity by DOING, not watching.

---

## Activity 1: Password Battle Arena (15 minutes)

### Setup
Students compete to create the strongest password using the passphrase method.

### Round 1: Wall of Shame (3 min)
Show these passwords one at a time. Students type in chat how long they think each takes to crack:

| Password | Reveal Answer |
|----------|--------------|
| `123456` | Instantly |
| `fluffy` | 10 seconds |
| `Fluffy12` | 8 hours |
| `Fl!ffy_12cats` | 200 years |

> "See how MASSIVE the difference is? Let's see if you can do better."

### Round 2: Passphrase Showdown (7 min)

**Rules:**
1. Pick 3-4 random, unrelated words
2. Add at least one number and one symbol
3. Must be 16+ characters
4. Must be memorable (you'll need to type it back later!)

> "Type your passphrase in the chat. DO NOT use a real password — make up a new one just for this exercise!"

**Judge entries out loud:**
- "Too short!"
- "No symbols — add some spice!"
- "That's a strong one — explain your method!"

Pick the top 3 and have those students explain their thinking.

### Round 3: Memory Test (5 min)
> "Clear your chat. Now WITHOUT looking back, type your passphrase again from memory."

> "See? A good passphrase is strong AND memorable. That's the whole point."

**Bonus mention:** "If you can't remember 50 different passphrases, use a password manager like Bitwarden (free). You remember ONE master passphrase, and it remembers the rest."

---

## Activity 2: Phishing Forensics — Real or Scam? (20 minutes)

### Setup
You will show 6 messages on screen (screenshare). For each one, students vote **REAL** or **SCAM** in chat, then you reveal the answer and break down the evidence.

**Scoring:** Keep a tally in chat — students track their own score. 6/6 = "Phishing Expert!"

### Message 1: Obvious Scam
```
FROM: security@amaz0n-verify.com
Subject: URGENT! Your account will be SUSPENDED in 24 hours!

Dear Customer,

We detected unusual activity on your account. Click here
immediately to verify your identity:
http://amaz0n-login.sketchy.ru

Amazon Security Team
```

**Answer: SCAM**
> Walk through red flags together: `amaz0n` with a zero, "Dear Customer" not your name, URGENCY, `.ru` domain. Ask: "Who spotted the zero in Amazon?"

### Message 2: Legitimate
```
FROM: noreply@microsoft.com
Subject: Your Microsoft 365 subscription renewal

Hi [Student Name],

Your M365 Education plan renews automatically on April 1, 2026.
No action is needed on your part.

View your subscription details:
https://account.microsoft.com/services

Microsoft 365 Team
```

**Answer: REAL**
> "Not everything is a scam! This one is legit." Walk through why: real domain, uses your name, no urgency, no password request, "no action needed," link goes to real Microsoft.

### Message 3: Tricky Scam
```
FROM: support@paypa1.com
Subject: Payment of $499.99 confirmed

Hi there,

Your payment of $499.99 to ElectronicsHub has been processed.
If you did NOT authorize this payment, click below to dispute:

https://paypa1-dispute-center.com/case/29481

PayPal Support
```

**Answer: SCAM**
> "Who caught it?" — `paypa1` with a number 1 instead of letter L. The dispute link also goes to a fake domain. Designed to scare you into clicking.

### Message 4: AI-Generated Scam (Hard!)
```
FROM: helpdesk@your-school-district.org
Subject: Important: Student Account Security Update

Dear [Student Name],

As part of our annual security review, we are requiring all
students to verify their login credentials. This helps us
protect your account from unauthorized access.

Please complete the verification form by Friday:
https://your-school-district-verify.com/student-login

Thank you for helping us keep our systems secure.

IT Department
[Your School District]
```

**Answer: SCAM**
> "This one is HARD. Perfect grammar, no spelling mistakes, sounds professional. This is what AI-generated phishing looks like." Red flags: asks you to "verify credentials" (schools don't do this via email), link goes to a different domain than the school's real website. "When in doubt, walk into the IT office and ask in person."

### Message 5: Legitimate
```
FROM: noreply@google.com
Subject: Security alert — new sign-in to your Google Account

Hi [Student Name],

Someone just signed in to your Google Account from a new device:

Device: Windows laptop
Location: Portland, OR
Time: March 20, 2026 at 3:45 PM

If this was you, you can ignore this message.
If this wasn't you, secure your account:
https://myaccount.google.com/security

Google Security Team
```

**Answer: REAL**
> Real Google alert: comes from google.com, has specific details (device, location, time), links to real google.com, says "if this was you, ignore" — scams never say that.

### Message 6: AI Voice Clone Scenario
```
You get a PHONE CALL that sounds exactly like your mom/dad:

"Hey, it's me. I got into a car accident and I need you to
send $500 to this number right away. Don't tell anyone,
just do it quickly. I'll explain later."
```

**Answer: SCAM (AI voice clone)**
> "This is real and happening NOW. AI can clone someone's voice from a short video or voicemail. The defense? Hang up and call your parent back on THEIR real number. If it's really them, they'll answer."

### Scoreboard
> "How many did you get right? Type your score! 6/6 = Phishing Expert, 5/6 = Sharp Eye, 4/6 = Good Start, 3 or below = We need to practice more!"

---

## Activity 3: Social Engineering Live Roleplay (10 minutes)

### Setup
You (the teacher) play the attacker. Students must decide how to respond. Do this live over Teams voice — it's way more engaging than reading scenarios.

### Scenario 1: The Fake IT Call
**You say (in a "professional" voice):**
> "Hi, this is tech support from your school. We've detected a security issue with your account and need to verify your identity. Can you tell me your username and password so I can fix it?"

**Ask students:** "What do you do? Type in chat!"

**Reveal:** No real IT person will EVER ask for your password. Hang up. Walk to the IT office in person if you're worried.

### Scenario 2: The Friendly Stranger
**You say:**
> "Hey! I'm a student from [another school]. We're doing a project about online security. Can you send me a screenshot of your browser with your saved passwords visible? It's for research!"

**Ask students:** "Would you do it? Why or why not?"

### Scenario 3: The Guilt Trip
**You say:**
> "Come on, we've been friends forever. Just let me use your Netflix login. I'll only use it for one show. If you were a real friend, you'd share."

**Ask students:** "What do you say back?"

**Reveal:** Real friends don't pressure you to share passwords. Your password = your responsibility. If someone gets in trouble with your account, YOU are responsible.

### Scenario 4: The USB Bait
**You say:**
> "I found this USB drive in the hallway labeled 'TEACHER PASSWORDS.' Who wants to see what's on it?"

**Ask students:** "Who's plugging it in?"

**Reveal:** NEVER plug in unknown USB drives. They can install malware the instant you plug them in. This is a real attack called "baiting."

### Debrief
> "In every scenario, the attacker was hacking YOU, not a computer. That's social engineering — and it's the #1 way people actually get hacked. No firewall can protect you if you hand over your password."

---

## Activity 4: Digital Footprint Investigation (10 minutes)

### Setup
Students investigate their own digital footprint in real time.

### Step 1: Google Yourself (3 min)
> "Open a browser and Google your own name in quotes. Example: 'John Smith Portland'
> What comes up? Type in chat: 'found something' or 'nothing came up'"

> "If you found something — is it something you'd want a college admissions officer to see?"

### Step 2: Social Media Privacy Check (5 min)
> "Open your Instagram, TikTok, or whatever you use most. Answer these in chat:"

1. "Is your profile PUBLIC or PRIVATE?"
2. "Can strangers see your posts?"
3. "Does your bio have your real school name, age, or city?"
4. "Do any of your photos show your school uniform, house, or street signs?"

> "If you answered 'public' or 'yes' to 2-4... you might want to change some settings after class."

### Step 3: The Recruiter Test (2 min)
> "Imagine you're applying for your dream job in 5 years. You made it to the final round. The hiring manager Googles you and finds your social media. Would you get the job?"

> "The internet never forgets. Screenshots spread. Posts can be un-deleted by others. Think before you post."

---

## Activity 5: AI Threat Demo (10 minutes)

### Setup
Show students how AI is changing cybersecurity — both the attacks and the defenses.

### Demo 1: AI-Written Phishing (3 min)

> "Remember Message 4 from our phishing game? Perfect grammar, personalized, professional. Old phishing emails were easy to spot because of typos. AI changed that."

Ask the class:
> "If AI removes spelling mistakes from phishing, what OTHER red flags can we still use?"

Collect answers in chat. Good answers include:
- Urgency / threats
- Asking for passwords (no legit company does this)
- Suspicious URLs (hover before you click!)
- Too good to be true
- Verify through a different channel

> "You're smarter than the AI if you know WHAT to look for!"

### Demo 2: Deepfake Awareness (4 min)

> "AI can now create videos of real people saying things they never said. These are called deepfakes."

Show or describe real examples:
- Fake celebrity endorsement videos used to scam people into bad investments
- AI voice clones that sound exactly like a family member asking for money
- Fake video calls where the person on screen isn't real

> "The defense is simple but powerful: VERIFY THROUGH A DIFFERENT CHANNEL. If you get a weird call from 'your mom,' hang up and call her back on her real number. If you see a celebrity promoting something, check their official accounts."

### Demo 3: AI Defenses — The Good Side (3 min)

> "AI isn't just used by attackers. Here's how AI protects YOU every day:"

1. **Gmail blocks 15 million phishing emails PER DAY** — AI reads every email before it reaches your inbox
2. **Banks flag suspicious transactions** — AI notices if your card is suddenly used in another country
3. **CAPTCHA puzzles** — Those "click the traffic lights" tests are AI separating humans from bots
4. **Antivirus software** — Modern antivirus uses AI to detect new malware it's never seen before

> "The people who understand BOTH cybersecurity AND AI will be the ones keeping everyone safe. Starting next month, that's going to be YOU — we begin our AI unit in April!"

---

## Wrap-Up: Quick Fire Round (5 minutes)

Rapid-fire questions — students answer in chat as fast as possible:

1. "What's stronger: `fluffy` or `PurpleTiger$Eats42Tacos!`?" (passphrase)
2. "You get an email from `amaz0n.com` — real or fake?" (fake — zero not O)
3. "Someone asks for your password to 'fix your account' — what do you do?" (hang up / say no)
4. "What does 2FA stand for?" (Two-Factor Authentication)
5. "HTTPS — what does the S mean?" (Secure)
6. "You find a USB labeled 'Exam Answers' — do you plug it in?" (NO!)
7. "AI can clone your voice from a short clip — true or false?" (TRUE)
8. "What's the #1 rule of cybersecurity?" (Think before you click/share!)

> "You all crushed it. Time for classwork — let's see if you can spot even trickier scams!"

---

## Transition to Classwork (2 minutes)

> "I'm posting the classwork in Teams now. You'll:
> 1. Rate password strength
> 2. Analyze phishing messages (harder ones this time!)
> 3. Handle social engineering scenarios
> 4. Answer AI + cybersecurity questions
>
> Write in your own words — I want to see that you UNDERSTAND, not that you memorized definitions!"

**Post in Teams:**
- Classwork PDF

---

## Troubleshooting Tips

### If students are shy about participating:
- Use anonymous polls ("Type 1 for Real, 2 for Scam" — no names attached)
- Share your own "almost fell for a scam" story to break the ice
- The roleplay scenarios tend to loosen everyone up

### If students share concerning online experiences:
- Take it seriously but keep the class moving
- Say: "That's exactly why we're learning this. If anything ever worries you online, tell a trusted adult."
- Follow up privately after class if needed

### If the phishing game is too easy:
- Message 4 (AI-generated) and Message 6 (voice clone) are the hard ones — spend more time there
- Ask: "What if the email came from a domain that looked EXACTLY right?" — discuss domain spoofing

### If activity runs long:
- Cut Activity 4 (Digital Footprint) — students can explore this on their own
- The Phishing Forensics and Social Engineering Roleplay are highest value

### If activity runs short:
- Have students check haveibeenpwned.com with a throwaway/test email
- Challenge: "Write the most convincing phishing email you can" — then have others spot the red flags
- Discuss: "How would you explain 2FA to your grandparents?"

---

## Materials Checklist

### MS Teams Setup
- [ ] Meeting started and students joined
- [ ] Screen sharing enabled
- [ ] Chat visible and active for polls/responses
- [ ] Notifications silenced

### Ready to Share
- [ ] Classwork PDF uploaded to Teams
- [ ] Homework PDF ready (assign at end of class)

### On Your Screen
- [ ] This activity guide open for reference
- [ ] Phishing messages ready to screenshare (copy from above or put in slides)
- [ ] Browser open for Digital Footprint activity

### After Class
- [ ] Post homework PDF to Teams
- [ ] Remind students about 2FA homework task
- [ ] Upload Kahoot quiz

---

*The goal is for students to leave class feeling empowered and alert — not scared. They should feel like they have real skills to protect themselves, not just a list of warnings.*
