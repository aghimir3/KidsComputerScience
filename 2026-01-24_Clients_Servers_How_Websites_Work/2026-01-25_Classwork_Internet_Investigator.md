# CLASSWORK: Internet Investigator
## Mission: Analyze Your Digital World

**Name:** ____________________________
**Date:** January 25, 2026

---

## Your Mission

You're now an **Internet Investigator**. Your job is to analyze 3 websites you actually use and uncover the secrets of how they work behind the scenes.

**Choose 3 websites you use regularly:**
- A social media or video site (YouTube, TikTok, Instagram, Discord, etc.)
- A school or learning site (Google Classroom, Khan Academy, Quizlet, etc.)
- A gaming or entertainment site (Steam, Roblox, Twitch, Spotify, etc.)

---

## CASE FILE #1

**Website Name:** _______________________________

**Full URL (copy from browser):** _______________________________

### Part A: URL Breakdown
Identify each part of the URL:

| Part | Your Answer |
|------|-------------|
| Protocol (http or https?) | |
| Subdomain (if any) | |
| Domain Name | |
| TLD (.com, .org, etc.) | |
| Path (if any) | |

### Part B: Security Check

- [ ] Does it have a lock icon? (Yes / No)
- [ ] Is it HTTP or HTTPS?
- [ ] Would you enter a password on this site? Why or why not?

_Your answer:_ _______________________________________________

### Part C: Tracert Investigation

Run this command: `tracert [website]`

- **Total hops:** _______
- **Fastest hop (lowest ms):** Hop #______ with ______ ms
- **Slowest hop (highest ms):** Hop #______ with ______ ms

**Interesting observation:** _______________________________________________

---

## CASE FILE #2

**Website Name:** _______________________________

**Full URL (copy from browser):** _______________________________

### Part A: URL Breakdown

| Part | Your Answer |
|------|-------------|
| Protocol (http or https?) | |
| Subdomain (if any) | |
| Domain Name | |
| TLD (.com, .org, etc.) | |
| Path (if any) | |

### Part B: Security Check

- [ ] Does it have a lock icon? (Yes / No)
- [ ] Is it HTTP or HTTPS?
- [ ] Would you enter a password on this site? Why or why not?

_Your answer:_ _______________________________________________

### Part C: Tracert Investigation

Run this command: `tracert [website]`

- **Total hops:** _______
- **Fastest hop (lowest ms):** Hop #______ with ______ ms
- **Slowest hop (highest ms):** Hop #______ with ______ ms

**Interesting observation:** _______________________________________________

---

## CASE FILE #3

**Website Name:** _______________________________

**Full URL (copy from browser):** _______________________________

### Part A: URL Breakdown

| Part | Your Answer |
|------|-------------|
| Protocol (http or https?) | |
| Subdomain (if any) | |
| Domain Name | |
| TLD (.com, .org, etc.) | |
| Path (if any) | |

### Part B: Security Check

- [ ] Does it have a lock icon? (Yes / No)
- [ ] Is it HTTP or HTTPS?
- [ ] Would you enter a password on this site? Why or why not?

_Your answer:_ _______________________________________________

### Part C: Tracert Investigation

Run this command: `tracert [website]`

- **Total hops:** _______
- **Fastest hop (lowest ms):** Hop #______ with ______ ms
- **Slowest hop (highest ms):** Hop #______ with ______ ms

**Interesting observation:** _______________________________________________

---

## BONUS MISSION: Request Counter (Optional)

Use your browser's Developer Tools (F12 > Network tab) to see how many requests each site makes!

| Website | Number of Requests | Biggest File Type (images? scripts? css?) |
|---------|-------------------|-------------------------------------------|
| Site #1 | | |
| Site #2 | | |
| Site #3 | | |

**Which site made the MOST requests?** _______________________________

**Why do you think that site needs so many requests?**

_______________________________________________

---

## Investigation Summary

Answer these questions based on your investigation:

### Question 1: Client or Server?
When you visited these websites, your computer was the (circle one):

**CLIENT** / **SERVER**

Explain why: _______________________________________________

---

### Question 2: The Fastest Route
Which of your 3 websites had the FEWEST hops? _______________________________

Why might having fewer hops be better?

_______________________________________________

---

### Question 3: Security Matters
Did all 3 of your websites use HTTPS? (Yes / No) _______

If a website did NOT use HTTPS, what information should you NEVER enter on that site?

_______________________________________________

---

### Question 4: Port Detective
You learned that HTTPS uses port 443 and HTTP uses port 80.

If you visited `https://youtube.com`, which port is your browser connecting to?

**Port:** _______

---

### Question 5: DNS in Action
Before your browser could load any of these websites, what had to happen FIRST?

- [ ] A) The server sent you the webpage
- [ ] B) Your browser displayed the content
- [ ] C) DNS translated the domain name to an IP address
- [ ] D) You clicked a link

---

## Creative Challenge: Design Your Own Website

Imagine you're creating a website for something you love (a game, hobby, band, etc.)

**Your website name:** _______________________________

**What would the full URL look like?**

`https://` _____ `.` _____ `.com/` _____
         (subdomain)  (domain)      (path)

**What would your server need to store?** (Check all that apply)

- [ ] Images/photos
- [ ] Videos
- [ ] User accounts/passwords
- [ ] Game data
- [ ] Music files
- [ ] Text/articles
- [ ] Other: _____________

**Would your site NEED to be HTTPS? Why or why not?**

_______________________________________________

---

## Reflection

**One thing I learned today:**

_______________________________________________

**One thing I'm still curious about:**

_______________________________________________

---

## Grading Rubric

| Section | Points |
|---------|--------|
| Case File #1 (complete) | 20 |
| Case File #2 (complete) | 20 |
| Case File #3 (complete) | 20 |
| Investigation Summary (Q1-5) | 25 |
| Creative Challenge | 10 |
| Reflection | 5 |
| **TOTAL** | **100** |

**Bonus Mission:** +10 extra credit

---

### Stuck? Here's Help!

**How to open Command Prompt:**
1. Press `Windows + R`
2. Type `cmd`
3. Press Enter

**How to run tracert:**
```
tracert google.com
```
(Replace google.com with any website)

**How to open Developer Tools:**
1. Press `F12` in your browser
2. Click the "Network" tab
3. Refresh the page to see requests

**Can't run tracert?**
Some networks block it. Try this online tool instead:
https://www.traceroute-online.com/
