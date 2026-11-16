# Projects: a workspace Claude can come back to

About 12 minutes to read, plus about 50 to do the practice

## What you will be able to do

- Say what a Claude Project is and when it beats starting a new chat.
- Tell project instructions apart from project files, and know which one to use for what.
- Explain, in plain words, why Claude forgets things, and what to do about it.
- Keep private details out of a project.

## What you will make

A small Project called "Home Paperwork Helper," built only from made-up material. It will hold a short instruction note and one pretend household file, and you will test whether a fresh chat inside it knows what the project knows.

## The problem a Project solves

You spend twenty minutes teaching Claude how your family eats and what tone you want in notes to the school. The answers get good. Next week you open a new chat and Claude knows none of it.

That is not a bug. Each chat starts clean unless something carries the background across. A Project is one way to carry it.

## What a Project is

Anthropic describes a project as a self-contained workspace with its own chat history and its own background material. You add documents, text or notes once, and every chat inside the project can use them.

A Project has two parts you control:

- **Project instructions.** A short note on how Claude should behave in this project. Who it is helping, the tone, what to avoid, how long answers should be. It applies to every chat in the project.
- **Project knowledge.** Files and text that Claude can look things up in. A pretend budget sheet, a list of the family's favorite recipes, notes about a club.

The simplest way to remember it: **instructions are how to act, files are what to know.** "Keep answers short and use plain words" is an instruction. "The club meets the second Tuesday and dues are twelve dollars" is something to know.

## What Pro adds

Projects are on your Pro plan. Anthropic says that on paid plans, when a project's material gets close to its limit, Claude switches on a method called RAG by itself, which can stretch the capacity by up to ten times.

## How to make one

These steps come from Anthropic's help page. Menus change, so look for the closest name on your own screen.

1. In the left sidebar, click **Projects**. You can also go to claude.ai/projects.
2. Click **+ New Project**, near the top right.
3. Give it a name and a short description. Claude cannot see the name or description. They are labels for you.
4. Save.
5. On the right side of the project page, click **+** to add files or text. That is your knowledge.
6. Click **Set project instructions**, type your note, then click **Save instructions**.

A newer version of Projects is rolling out in stages, so your screen may differ.

## Why Claude forgets

Claude can only look at so much text at once while it works on your request. That span is often called the **context window**. Think of a desk: everything Claude should use has to be on it, and the desk is large but not endless.

Three things follow:

1. **A new chat is a clean desk.** Nothing from an earlier chat is on it, unless you put it there, a project did, or memory did.
2. **A very long chat can get crowded.** If a long chat starts to drift, a short summary pasted into a fresh chat often works better than pushing on.
3. **Anthropic says context does not carry between chats unless it is in project knowledge.** That is the reason Projects exist. Memory, below, is the other way context can come along.

Claude also has a memory feature. Anthropic's page says it is on by default on individual plans, Pro included. You can pause or reset it under Settings, in a section called Your Claude. Resetting deletes all memories, including project memories, for good. Check your own screen to see what yours is set to.

## Project or new chat?

Use a **new chat** for one-off jobs, like a thank-you note.

Use a **Project** when:

- you will come back to the same subject again and again,
- the same background applies each time (the family's food rules, a club's schedule, how you like letters written),
- you want to stop retyping the same paragraph at the top of every prompt.

If you are not sure, start a chat. If you have pasted the same background three times, make a Project.

## Keeping private data out

A Project is a drawer you keep stocking. That makes it easy to put in more than you meant to.

- Do not put in passwords, bank numbers, Social Security numbers, or medical details.
- Use made-up or trimmed versions of documents while you learn.
- If a document is mostly private, write a three-line summary yourself.
- If you put in something you should not have, remove it. Check your own screen for how.

## Keep this in your pocket

Instructions are how to act, files are what to know. Each chat starts with a clean desk, and a project puts the background back. Keep private details out.

## Practice

Three jobs, about 15 to 20 minutes each. Use claude.ai. Made-up details only, no real account numbers, passwords or medical details.

### Task 1: Build the Home Paperwork Helper

**Why it matters:** making one small project shows you where each piece goes, and what each piece does.

**Do this:** follow the six steps in "How to make one." Name the project "Home Paperwork Helper." For the instructions, paste the first block below. For knowledge, click **+** and choose the option to add text, then paste the second block. If your screen only offers a file upload, save the lines in a plain text file first. On your Mac, open TextEdit, choose Format, then Make Plain Text, paste, and save to a folder you can find in Finder. Copy only the text inside the blocks. To copy and paste, press Command-C and Command-V.

```text
You help one person keep home paperwork simple. Use plain words, no jargon. Keep answers under 150 words unless I ask for more. When you use a fact from the project files, say which line it came from. If a fact is not in the files, say you do not know. Do not guess.
```

```text
The Okafor household is made up. Two adults, one dog named Biscuit.
The electric bill is due on the 9th of each month.
The water bill is due on the 22nd of each month.
The dog's vaccines are due every spring, and the vet is Dr. Lindqvist.
The made-up internet plan costs $60 a month.
The family keeps receipts in a blue box in the hall closet.
```

**Self-check:**

- [ ] My project has a name, saved instructions and one knowledge item.
- [ ] Every detail in my knowledge is made up.
- [ ] I did not add anything private.

**What good looks like:** a project page showing your instruction note and one knowledge item.

---

### Task 2: Test what the project knows

**Why it matters:** you need to see for yourself that a chat inside the project knows what a chat outside does not.

**Do this:** inside the project, start a new chat and ask the question below. Then open a completely separate chat, outside the project, and ask the same question. Compare.

```text
When is the water bill due, and who is the vet?
```

Then ask one question the file does not answer, inside the project:

```text
What is the electric company's phone number?
```

**Self-check:**

- [ ] The chat inside the project answered from the file.
- [ ] The chat outside it did not know, or I noted that memory gave it something.
- [ ] For the phone number, I saw whether Claude said it did not know, or invented a number.
- [ ] I checked each answer against my own text.

**What good looks like:** correct answers inside the project, a blank or a request for details outside it, and an honest "not in the files" for the phone number. If Claude made up a number, write it down. Instructions help and do not guarantee.

---

### Task 3: Fix a forgetting problem

**Why it matters:** you find where the forgetting happened and decide where the fix belongs.

**Do this:** in a new chat inside the project, ask for a short note to the vet. Read it. The project has no sign-off name and no tone rule. Pick a made-up name, such as "Sam," and a tone rule, such as "warm, never more than one exclamation mark." Decide which is how to act and which is what to know, put each in the right place, run the request again, and compare.

```text
Write a short, friendly note to our vet, Dr. Lindqvist, asking what we need to book for the spring vaccines. Keep it under 80 words.
```

**Self-check:**

- [ ] I named what the first note was missing.
- [ ] I put the tone rule in the instructions and the sign-off name in the knowledge, or I can say why I chose differently.
- [ ] I changed the project and ran the request again.
- [ ] The second note was better, or I wrote down why it was not.

**What good looks like:** a second note that is signed with your made-up name and follows your tone rule because the project now holds both. "How to act" goes in instructions, "what to know" in a file.

When you have done the tasks, press the practice button below. It saves that you finished.

<div id="practice-done"></div>

## Further reading

Optional. These go to Anthropic's own pages. Read what they say today, since they change.

- What are projects: [https://support.claude.com/en/articles/9517075-what-are-projects](https://support.claude.com/en/articles/9517075-what-are-projects)
- Chat search and memory: [https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and you can move on.

<div id="quiz"></div>
