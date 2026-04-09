# Class Activity — January 25, 2026
## Topic: Clients, Servers & How Websites Work

**Duration:** ~45-60 minutes (flexible)
**Format:** Guided hands-on, students follow along

---

## Activity 1: URL Detective (10 min)

### Setup
Have students open a new browser tab.

### Instructions
"Let's become URL detectives! I'll show you some URLs and you tell me the parts."

#### Round 1: Identify the Domain
Show these URLs (share screen), students type answers in chat:

```
1. https://www.youtube.com/watch
2. https://mail.google.com/inbox
3. https://www.reddit.com/r/gaming
4. https://docs.microsoft.com/en-us/learn
```

**Ask:** "What's the DOMAIN in each one?"
- Answers: youtube, google, reddit, microsoft

#### Round 2: Identify the Path
Same URLs - "What's the PATH (the part after .com)?"
- Answers: /watch, /inbox, /r/gaming, /en-us/learn

#### Round 3: Spot the Subdomain
"Which ones have a SUBDOMAIN (something before the main name)?"
- Answers: mail (in google), docs (in microsoft), www (in youtube & reddit)

#### Discussion Point
"Why do companies use subdomains like 'mail' or 'docs'?"
- Answer: To organize different services/apps under one domain!

---

## Activity 2: HTTPS Security Check (10 min)

### Instructions
"Let's be security inspectors! Check if these sites are secure."

Have students visit these sites and report what they see:

| Site | Check for Lock Icon | HTTP or HTTPS? |
|------|---------------------|----------------|
| google.com | | |
| amazon.com | | |
| wikipedia.org | | |
| Your school website | | |

### Discussion Questions
1. "Did any site NOT have the lock? What would you do?"
2. "Why is it extra important to check for HTTPS on Amazon?"
   - Answer: Because you enter payment info!
3. "What does the lock actually mean?"
   - Answer: Your connection is encrypted - only you and the server can read it

### Fun Fact to Share
"Even if a site HAS https, it doesn't mean the site is trustworthy - just that your connection is private. A scam site can still have HTTPS!"

---

## Activity 3: Trace the Route with tracert (15-20 min)

### This is the main hands-on activity!

### Step 1: Open Command Prompt
**Windows:**
- Press `Windows + R`
- Type `cmd` and press Enter

**Mac:**
- Open Terminal (search for it in Spotlight)
- Use `traceroute` instead of `tracert`

### Step 2: First Trace - Google
Type this command:
```
tracert google.com
```

**While waiting, explain:**
- "Each line is a HOP - a stop your data makes"
- "The numbers are milliseconds - how long each hop took"
- "Some hops might show * * * - that's okay, they just didn't respond"

### Step 3: Discuss the Results
Ask students:
- "How many hops did it take to reach Google?"
- "Which hop was the slowest?"
- "Can anyone guess what some of these stops might be?"

**Typical hops:**
1. Your router (192.168.x.x or 10.x.x.x)
2. Your ISP's equipment
3. Major internet exchange points
4. Google's data center

### Step 4: Compare Different Destinations
Have students try:
```
tracert youtube.com
tracert microsoft.com
tracert amazon.com
```

**Discussion:**
- "Do they all take the same path?"
- "Which one has the most/fewest hops?"
- "Why might some be faster than others?"

### Step 5: Try a Far Away Server
```
tracert bbc.co.uk
```
or
```
tracert google.co.jp
```

"Notice how international sites often have more hops!"

---

## Activity 4: See Real Requests in Your Browser (10-15 min)

### This shows client-server communication in action!

### Step 1: Open Developer Tools
- **Chrome/Edge:** Press `F12` or `Ctrl + Shift + I`
- **Firefox:** Press `F12`
- Click the **"Network"** tab

### Step 2: Visit a Website
With DevTools open, go to: `google.com`

### Step 3: Observe the Requests
Point out:
- "Look at all those requests! Each one is your browser (client) asking the server for something"
- "See the Status column? 200 means SUCCESS"
- "See the Type column? There are HTML files, images (png, jpg), scripts (js), and styles (css)"

### Step 4: Click on a Request
Click on the first request (the main HTML file)

Show them:
- **Headers tab:** "This is the REQUEST your browser sent"
- **Response tab:** "This is what the SERVER sent back"
- **Timing tab:** "This shows how long each step took"

### Discussion
"When you load ONE webpage, how many requests does your browser make?"
- Let them count - it's usually 20-100+ requests!

"This is why slow internet makes pages load slowly - every single request has to travel to the server and back!"

---

## Activity 5: Client-Server Role Play (5-10 min)

### A quick, fun activity to reinforce concepts

### Setup
- You (instructor) are the SERVER
- Students are CLIENTS
- Chat is the "internet"

### Round 1: Basic Request/Response
**Instructor says:** "I am the Google server. If you want to see my homepage, send me a REQUEST in chat!"

Students type: "REQUEST: google.com homepage"

**Instructor responds:** "RESPONSE: Here's the Google homepage! [describes it or shows screenshot]"

### Round 2: Add Ports
**Instructor:** "Now I'm running TWO services - a website on port 80 and email on port 25. You need to tell me which port!"

Students must type: "REQUEST: port 80 - homepage" or "REQUEST: port 25 - check email"

### Round 3: Add HTTPS
**Instructor:** "Now I only accept SECURE requests on port 443. Anyone using port 80 gets rejected!"

Students learn to type: "SECURE REQUEST: port 443 - homepage"

### Debrief
"See how the server needs to know:
1. WHAT you want (the path)
2. WHERE to send it (which service/port)
3. HOW to send it (secure or not)"

---

## Wrap-Up Discussion (5 min)

### Quick Review Questions
Ask these and let students answer in chat:

1. "When you visit Netflix, is your phone the client or server?"
   → Client

2. "What port would Netflix use - 80 or 443?"
   → 443 (because it's secure, you have a password!)

3. "What translates 'netflix.com' into an IP address?"
   → DNS

4. "If tracert shows 15 hops, what does that mean?"
   → Your data went through 15 different stops/routers

### Preview Next Week
"Next week we'll learn about [TOPIC] - any questions about today before Kahoot?"

---

## Troubleshooting Tips

### If tracert doesn't work:
- Some school/work networks block it
- Try: `ping google.com` instead (shows if you can reach it)
- Or use online traceroute tools: https://www.traceroute-online.com/

### If students can't open DevTools:
- School Chromebooks sometimes block F12
- Show it on your screen share instead
- Or use: https://www.webpagetest.org/ to show requests

### If activity runs long:
- Skip Activity 4 (DevTools) - it's the most complex
- Activity 3 (tracert) is the highest value hands-on

### If activity runs short:
- Add more tracert destinations
- Have students find the "weirdest" domain names they can think of and trace them
- Challenge: Who can find a site with the MOST hops?

---

## Materials Checklist

- [ ] Students have Command Prompt/Terminal access
- [ ] Students have a browser with DevTools (Chrome recommended)
- [ ] URLs ready to share in chat
- [ ] Backup: Online traceroute tool bookmarked
- [ ] Kahoot ready to launch after activities
