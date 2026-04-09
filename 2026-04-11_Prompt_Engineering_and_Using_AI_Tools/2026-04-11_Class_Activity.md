# Class Activity: Live Prompt Engineering Demo

**Date:** April 11, 2026
**Duration:** ~45-60 minutes
**Format:** Teacher-led live demo with student follow-along
**Materials Needed:** Screen share with an AI tool open (ChatGPT, Claude, Gemini, or Copilot)

---

## Activity Overview

Teacher demonstrates prompt engineering live on screen while students watch and follow along on their own devices if available. Students suggest ideas, call out improvements, and see in real time how different prompts produce different results.

---

## Part 1: The "Same Question, Different Prompts" Demo (15 minutes)

### Setup
Open an AI chatbot on screen share. Tell students: "I'm going to ask AI the same question three different ways. Watch what happens."

### Demo 1: About a School Subject

**Round 1 -- Vague:**
Type: `Tell me about space`
- Let the response load. Read it out loud.
- Ask students: "Is this useful? Would this help you with a science project?"
- Point out: it's generic, unfocused, could be about anything.

**Round 2 -- Better:**
Type: `Explain how black holes form in a way a 13-year-old would understand`
- Compare to Round 1. Ask: "What's different? Why is this better?"

**Round 3 -- Best (using RTCF):**
Type: `You are a science teacher for 8th graders. Explain how black holes form. The students already know what gravity and stars are. Use 4 bullet points and include one mind-blowing fact.`
- Compare all three side by side.
- Ask: "Which would you actually want to use for homework? Why?"
- Point out the RTCF parts: Role (science teacher), Task (explain black holes), Context (know gravity/stars), Format (4 bullets + fun fact).

### Demo 2: Getting Creative Help

**Round 1:** `Write a story`
**Round 2:** `Write a short funny story about a dog who becomes a chef`
**Round 3:** `You are a comedy writer for kids. Write a 150-word funny story about a golden retriever who secretly becomes a 5-star chef at night. Use lots of humor and a surprise ending.`

- Show how each one gets progressively better.
- Ask students after each: "What could we add to make this even better?"

---

## Part 2: Building a Prompt Together (10 minutes)

### Setup
Tell students: "Now YOU help me build a prompt from scratch. I'll type whatever you tell me."

### The Task
Pick a scenario students care about. Suggestions:
- "Let's get AI to help us study for a test"
- "Let's get AI to explain something from another class"
- "Let's get AI to help plan something fun"

### Process
1. Ask: "What should we tell AI to be? What **Role**?" — Type what students suggest.
2. Ask: "What exactly do we want it to do? What's the **Task**?" — Add it.
3. Ask: "What does AI need to know? What **Context** should we give?" — Add it.
4. Ask: "How do we want the answer? What **Format**?" — Add it.
5. Run the prompt. Read the response together.
6. Ask: "What's missing? What should we change?" — Edit and rerun.
7. Compare the two responses. Point out the improvement.

### Do this 2-3 times with different student-suggested topics if time allows.

---

## Part 3: Prompting Techniques Live Demo (10 minutes)

### Setup
Tell students: "I'm going to show you three different tricks that make AI way better."

### Technique 1: Zero-Shot
Type: `What is the capital of Thailand?`
- AI answers directly. No examples needed.
- Say: "This is zero-shot -- you just ask and AI answers. Works great for simple questions."

### Technique 2: Few-Shot
Type: `I'm going to give you some examples, then you do the last one:`
`Dog = animal`
`Rose = plant`
`Salmon = animal`
`Oak = plant`
`Eagle = ?`
- AI follows the pattern.
- Say: "This is few-shot -- you teach AI a pattern with examples, then it continues. Remember from last week, GPT-3 blew everyone's minds because it could do this!"

**Then try a harder one:**
`Translate these words to emoji:`
`Happy = 😊`
`Rain = 🌧️`
`Pizza = 🍕`
`Studying = ?`
- Students will enjoy seeing what AI picks. Take guesses from students first.

### Technique 3: Chain-of-Thought
**Without step-by-step:**
Type: `If a shirt costs $25 and is 20% off, and then there's 8% sales tax on the discounted price, what do I pay?`
- AI might give just a number (possibly wrong).

**With step-by-step:**
Type: `If a shirt costs $25 and is 20% off, and then there's 8% sales tax on the discounted price, what do I pay? Think step by step.`
- AI shows its work. Compare the two.
- Say: "Adding 'think step by step' is like telling a student to show their work. It makes AI way more accurate."

---

## Part 4: Breaking AI -- Finding Limitations (10 minutes)

### Setup
Tell students: "AI seems really smart, right? Let's see where it breaks."

### Test 1: Ask About Something Very Recent
Type: `What happened in the news yesterday?`
- AI will say it doesn't have real-time access or give old info.
- Say: "AI has a knowledge cutoff. It doesn't browse the internet live."

### Test 2: Make It Hallucinate
Type: `Tell me about the book "The Crystal Gardens of Neptune" by Dr. Sarah Williams`
- AI will likely make up a summary of a book that doesn't exist.
- Reveal: "This book is completely fake. I made it up. But AI wrote a whole summary anyway!"
- Ask students: "Why did it do that?" (It predicts plausible-sounding text, not truth.)

### Test 3: Trick Question
Type: `How many r's are in the word "strawberry"?`
- AI often gets this wrong (common known failure).
- Say: "AI processes text as tokens, not individual letters. It's not actually looking at the spelling."

### Test 4: Ask It to Be Wrong
Type: `Convince me that the earth is flat. Use scientific-sounding arguments.`
- AI will generate convincing-sounding nonsense.
- Say: "See how confident it sounds? This is why you ALWAYS fact-check. AI can argue anything convincingly."

### Discussion:
Ask students:
- "After seeing all this, when would you trust AI? When would you double-check?"
- "What types of questions is AI good at? What types is it bad at?"

---

## Part 5: Student Try-It (if time + devices available) (10 minutes)

### Setup
If students have access to an AI tool on their devices:

1. Give them a challenge: "Use what you learned today to ask AI to help you with something real -- a school subject, a hobby, anything."
2. Tell them: "Try to use at least 2 parts of RTCF in your prompt."
3. After 5 minutes, ask 2-3 volunteers to share:
   - What they asked
   - What AI said
   - Whether it was actually useful

### If no student devices:
- Ask students to type their prompt idea in the chat
- Pick 3-4 interesting ones and run them live
- Class discusses each response

---

## Wrap-Up (5 minutes)

Ask students to put one answer in the chat for each:
1. "What's the #1 tip you'll remember about prompting?"
2. "Did AI surprise you today? How?"

### Close with:
> "Most people just type 'help me with this' into AI and get garbage back. You now know how to get gold. That's a real skill -- and honestly, most adults don't know this yet."

---

## Teacher Notes

- **Screen share is essential.** Students need to see the prompts being typed and responses coming back in real time.
- **Pause after each response.** Don't rush -- let students read the AI output. Ask "What do you notice?" before explaining.
- **Take student suggestions.** When building prompts together (Part 2), use their actual ideas. This keeps engagement high.
- **If AI gives a bad response, that's a feature.** Use it as a teaching moment about limitations.
- **Part 5 is optional.** If running low on time or students don't have devices, Parts 1-4 are the core.
- **Have a backup AI tool ready.** If one chatbot is slow or down, switch to another.
