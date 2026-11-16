# Give it a role and context

About 12 minutes to read, plus about 40 to do the practice

## What you will be able to do

- Tell the AI who it should be and who the writing is for, in one or two sentences.
- Give it the background it cannot guess, so the answer fits your real situation.
- Spot when a role changes the voice of an answer and when it changes nothing about the facts.

## What you will make

Three small pieces of real writing, each in a voice you pick on purpose: a grocery list, a note to a teacher, and a firm letter to a company. Same tool, same you, three very different results. By the end you will have a "context block" you can paste at the top of any prompt.

## Why a role helps

In the last lesson you learned four parts of a clear prompt: the job, the details, the reader, and the shape. This lesson zooms in on two of them, the reader and the details, and adds a third idea: the **role**.

A role is a short line that tells the AI who is talking. Think about a note you need written. A retired teacher would write it one way. A busy office manager would write it another way. A friendly neighbor would write it a third way. The AI can write all three. If you do not choose, it picks a middle-of-the-road voice that sounds like nobody in particular.

Here is the difference.

> Write a note asking my landlord to fix the heater.

> You are a calm, polite tenant who has asked for this repair once before. Write a short note to my landlord asking him to fix the heater. He has not answered my first message. Keep it friendly but make clear that I need a date.

The second one tells the AI who is writing (a calm tenant), what has already happened (one message, no answer), and the tone (friendly but firm). You did not ask for anything fancy. You just gave it something to aim at.

## The three pieces

1. **Role.** Who the AI should be. "You are a patient school secretary." "You are a careful editor." "You are a cheerful friend who loves a bargain." One line is plenty.
2. **Context.** The background it cannot see. What happened before, what you already tried, what the deadline is, what you do not want. Context is the part people skip, and it is usually the part that makes the answer fit.
3. **Audience.** Who will read the result. A seven-year-old, a landlord, a school office, your sister. The same facts read very differently for each.

A handy way to remember it: **who is writing, who is reading, and what is going on.**

## A role changes the voice, not the facts

This one matters, so read it twice. When you tell the AI "you are a doctor" or "you are a lawyer," it will write in that style. It will sound confident and professional. It does not become a doctor or a lawyer. It does not suddenly know more, and it can still be wrong.

Use roles for **voice and viewpoint**: tone, level of detail, who it is writing to. Do not use a role to make a medical, legal, or money answer more trustworthy. For those, the AI is a place to start a question, and a real source or a real professional is where you finish it. The Stay Safe track goes deeper on this.

## A context block you can reuse

Once you find a role and context that work, keep them. Here is a template. Fill in the brackets and paste it at the top of a prompt.

```text
You are [who is writing, in a few words].
Background: [what is going on, what has happened, what I need].
This is for [who will read it].
Tone: [two or three words].
Do not: [anything you want avoided].
```

Then add the job on the next line, such as "Write a short note" or "Make me a list."

## A few cautions

- **Do not stack five roles.** "You are a poet, a lawyer, a comedian, and a coach" gets a muddle. One role per job.
- **Keep private details out.** You can describe a situation without naming people. Say "my landlord," not his name and your address.
- **Read for the voice you asked for.** If it says "I hope this finds you well" and you wanted blunt, say so in a follow-up: "Drop the pleasantries. Be direct."

## Keep this in your pocket

1. Say who is writing, who is reading, and what is going on.
2. A role changes the voice. It does not add knowledge or make an answer true.
3. Save a context block that works and paste it into new prompts.

## Practice

Three jobs, about 10 to 15 minutes each. Use claude.ai for all three. In Task 3 you will also try ChatGPT. Use made-up names and places only. Nothing private.

### Task 1: One grocery list, three shoppers

**Why it matters:** the quickest way to feel what a role does is to change only the role and keep everything else the same.

**Do this:** open a new chat in Claude. Paste the prompt below, then fill in the brackets with a role of your own. Run it three times, each in its own new chat (click New chat at the top left of the page, or the plus sign if you see one), with a different role each time. Try one practical role, one silly role, and one that matches your real style, such as "a budget-minded planner," "a pirate with a pantry," and "a relaxed home cook." Save the three lists in one Google Doc or on paper.

```text
You are [your role].
Background: I am shopping for a family of four for one week. We like simple dinners and we want leftovers for lunch. Our budget is about the same as last week.
This is for me, to carry into the store.
Tone: [two or three words that fit your role].
Make me a grocery list for the week, sorted by store section, with one line at the end suggesting where I could save money.
```

**Self-check:**

- [ ] I ran the prompt three times, in three new chats, changing only the role.
- [ ] I can point to the words in each list that came from the role.
- [ ] I noticed whether the actual groceries stayed about the same or changed too.
- [ ] I did not include a real address, name, or store loyalty number.

**What good looks like:** three lists with clearly different voices. The items often overlap. That is the point to notice: a role steers how it speaks, and it can nudge what it picks too. If the three lists sound the same, make your roles more different, or add a word of tone.

---

### Task 2: A school note in two voices

**Why it matters:** audience and context are what make a message fit. This is where you see how much the background matters.

**Do this:** pretend you need to tell a teacher your child, a made-up eight-year-old named Sam, will miss school on Friday for a dentist appointment. Run the first prompt in a new Claude chat. Read the note. Then, in the same chat, add the second prompt and compare. Do not use your own child's real name or school.

```text
You are a parent writing a quick, polite note to a teacher.
Background: my son Sam is in third grade. He has a dentist appointment on Friday morning and will miss the first two hours. He has not missed any other days this month.
This is for his teacher, who reads many notes a day.
Tone: friendly and brief.
Write the note in under 60 words.
```

```text
Now write the same note again, but for the school office. Make it more formal, and add a line asking whether Sam needs to bring anything to make up the work.
```

**Self-check:**

- [ ] I read both notes aloud, or in my head, as if I were the person receiving each.
- [ ] I can say what changed between the two when the reader changed.
- [ ] I checked that the day and the length of the absence are right in both notes.
- [ ] I would be comfortable sending one of them after changing the details to be real.

**What good looks like:** a short note to the teacher and a slightly more formal one for the office, both with the right day and time. If the AI added a detail you did not give it, such as a doctor's name or a reason you did not state, delete it. It guessed. This is why you read before you send.

---

### Task 3: A firm, polite letter

**Why it matters:** this is the job where tone matters most, and where a good role and context turn a stiff letter into one you would sign.

**Do this:** make up a problem with a company. A good one: a blender you bought three weeks ago stopped working, and the company has not replied to two emails. Fill in the template below with your made-up details. Run it in Claude. Then paste the exact same prompt into ChatGPT in a new chat and compare the two letters. Choose the one you would send, and write one sentence on why.

```text
You are a calm customer who writes clear, firm, polite letters and does not threaten anyone.
Background: [what you bought and when, what went wrong, what you already tried, what you want them to do, and by when].
This is for a customer service manager at the company.
Tone: firm, polite, specific.
Do not: use legal threats, shout, or invent facts I did not give you.
Write a letter of no more than 180 words.
```

**Self-check:**

- [ ] I gave real-sounding but made-up details: what, when, what I tried, and what I want.
- [ ] I read both letters for facts the AI added on its own, and I crossed those out.
- [ ] I compared tone, not just length.
- [ ] I picked one letter and wrote one sentence about why.

**What good looks like:** a letter with a clear ask and a date, in a voice that stays polite. A weak result is one that is vague, too long, or full of "I am writing to express my deep concern." If you see that, reply with "Cut the filler. Say what I want in the first two sentences." Then save the version you like and the context block you used. You will build on it in the prompt library lesson later in this track.

When you have done the tasks, press the practice button below. It saves that you finished and opens the next lesson. Passing the quiz with 2 of 3 right opens it too.

<div id="practice-done"></div>

## Further reading

These are optional. They go to the companies' own pages. Read what they say today, since these tools change often.

- Claude, from Anthropic: [https://claude.ai](https://claude.ai)
- ChatGPT, from OpenAI: [https://chatgpt.com](https://chatgpt.com)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and the next lesson opens.

<div id="quiz"></div>
