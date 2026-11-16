# Skills: instructions Claude can reuse

About 12 minutes to read, plus about 50 to do the practice

## What you will be able to do

- Say what a Skill is, and how it differs from a prompt you type.
- Find the Skills area on your screen, turn a built-in Skill on, and see it work.
- Ask Claude to help you write a simple Skill of your own, and test it on made-up material.
- Know why Anthropic says to install Skills only from sources you trust.

## What you will make

A small Skill called `friendly-reminder-notes`, for turning rough notes into a short, kind reminder in the same shape every time. Claude builds it for you as a downloadable file. You upload it and test it with a made-up message.

## Prompt, project, skill

You already have two ways to give Claude instructions.

- A **prompt** is what you type in a chat. It lasts for that conversation.
- A **Project** holds instructions and files for one subject, and its chats can use them.

A **Skill** is a third kind. Anthropic describes Skills as folders of instructions, scripts and resources that Claude loads when they are relevant. Its contrast: a prompt is a one-off set of instructions for a conversation, while a Skill is loaded on demand so you do not repeat the guidance.

A Skill is a recipe card in a box. The helper reads the card only when the job calls for that recipe.

Skills are about a way of doing a job, such as "always format a letter like this." If a good prompt gets you there, you do not need one.

## What is inside a Skill

Every Skill is a folder. The folder holds one file named `SKILL.md`. At the top of that file is a short header with two things: a **name** and a **description**. Below it, in plain writing, are the instructions.

Claude reads the description to decide whether the Skill fits the job. That makes it the most important line you write. Keep it short: what the Skill does, and when to use it.

Anthropic's developer page says the name can use lowercase letters, numbers and hyphens, and that "anthropic" and "claude" are reserved words.

Here is the shape, with made-up content:

```text
---
name: friendly-reminder-notes
description: Turns rough notes into a short, kind reminder message. Use when someone asks for a reminder note to a friend, club or neighbor.
---

# Friendly reminder notes

1. Start with a warm greeting that uses the person's name.
2. State the reminder in one sentence, with the date and place.
3. Add one friendly line, such as thanks or a small joke.
4. Keep the message under 60 words, not counting the closing line.
5. Never invent a date, time or place. If one is missing, ask.
6. End with this exact line on its own: Reminder card ready.
```

## Turn on and use a built-in Skill

Anthropic supplies built-in Skills for Excel, Word, PowerPoint and PDF files. Claude uses them without being told. If you ask for a presentation, a Word document or a spreadsheet, the matching Skill can step in.

Steps from Anthropic's help pages. Menus change, so look for the closest name.

1. Open Settings, then Capabilities, or look under Customize. Turn on **Code execution and file creation**, which may be called **Create and edit files** in the newer layout.
2. Open **Customize**, then **Skills**. You will see a list with a switch beside each Skill.
3. Switch on the ones you want.
4. Ask for something a Skill would handle, such as a short Word document. Claude decides whether to use one.

## Uploading a Skill of your own

Anthropic's help page says to put the Skill folder inside a zip file, then go to Customize, Skills, click **+**, then **+ Create skill**, then **Upload a skill**, and choose the zip. Then switch it on. An upload can fail when:

- the zip is too big,
- the folder name does not match the Skill's name,
- the `SKILL.md` file is missing,
- the name or description has characters that are not allowed.

The zip should have the folder at its top level, with `SKILL.md` inside the folder. Claude builds that zip for you, so you do not make folders by hand. Your Pro plan covers uploads. If a menu is missing, check your own screen.

A custom Skill you upload in Claude does not sync to other places that use Skills.

**Optional, Mac only: recording a Skill.** Anthropic's page says recording a Skill by screen exists only in Cowork, in the Claude app for Mac, on Pro, Max, Ultra and Team plans. Cowork's name and menus may differ on your screen. Ask Zac before you try it. This lesson does not need it.

## Be careful with other people's Skills

Anthropic is firm here: install Skills only from trusted sources. It compares a Skill to installing software. It can include scripts and files, and it can carry instructions that make Claude do things you did not want. The risks it names are prompt injection, which you met in "When AI can act, not just talk," and data leaking out.

What that means for you:

- Prefer Skills you wrote yourself or got from Anthropic.
- Do not install one because a stranger online says it is great.
- You can switch a Skill off, or delete it. Open it in Customize, Skills, and use the three-dot menu.

## Keep this in your pocket

A Skill is saved instructions in a folder with a `SKILL.md` file, used when it fits the job. Built-in ones work once file creation is on. Install Skills only from sources you trust.

## Practice

Three jobs, about 15 to 20 minutes each. Use claude.ai. Made-up details only. Upload only the Skill Claude makes from your own request, never anyone else's.

### Task 1: Find the Skills area and try a built-in one

**Why it matters:** you should know where the switches are, and see a Skill do real work before you make your own.

**Do this:** follow the four steps in "Turn on and use a built-in Skill." Write down the real menu names from your screen. Then ask Claude for the document below.

```text
Make me a one-page Word document called "Garden Club Schedule" with a simple table. Use made-up details: four meetings, one per month starting in March, each with a date, a place and a snack person. Use the names Marlene, Dana, Walt and Priya.
```

**Self-check:**

- [ ] I found the Skills list on my screen, or I wrote down what I saw instead.
- [ ] I turned on file creation.
- [ ] I got a document back that I could open. Word or Pages both open it.
- [ ] I checked the table by eye for anything that looked wrong.

**What good looks like:** a one-page document with a table that matches your request. If no file appeared, check the file-creation switch and try once more.

---

### Task 2: Have Claude build a Skill for you

**Why it matters:** a Skill is only as good as its description and steps, and you need to read it before you trust it.

**Do this:** first, in a new chat, run the reminder request from Task 3 with no Skill and keep the answer for later. Then paste the prompt below into a new chat and read what comes back with the checklist in mind. If anything is off, tell Claude what to change.

If Claude does not offer a download, stop here and come back to this task later with Zac. Do not build the folder yourself.

```text
Using file creation, make a simple Skill called friendly-reminder-notes and give it to me as a downloadable zip file. The zip must contain one folder named friendly-reminder-notes, and that folder must contain only a file named SKILL.md. Put a name and description at the top of SKILL.md. Rules: warm greeting with the person's name, one sentence for the reminder with date and place, one friendly closing line, under 60 words not counting the final line, never invent a date, time or place, and end with this exact line on its own: Reminder card ready. No scripts, no extra files, no links. Do not add anything I did not ask for.
```

**Self-check:**

- [ ] I ran the reminder request once with no Skill and kept the answer.
- [ ] The name uses only lowercase letters, numbers and hyphens, and does not contain "claude" or "anthropic."
- [ ] The description says what the Skill does and when to use it.
- [ ] The rules match the ones I asked for. There is only a `SKILL.md`, with no scripts and no links.

**What good looks like:** a downloaded zip, and a short `SKILL.md` you can read in one minute and agree with. If Claude added a rule you did not ask for, ask it to take that rule out and give you a new zip.

---

### Task 3: Upload it, test it, then switch it off

**Why it matters:** a Skill that never activates is a recipe card nobody reads.

**Do this:** use the upload steps in "Uploading a Skill of your own" with the zip Claude gave you. Switch it on. Start a new chat and run the first test below. Your answer should end with "Reminder card ready." That line is how you know the Skill ran, and your earlier answer from Task 2 will not have it. Then run the second test, to see that the Skill stays out of the way. When you are done, open the Skill's three-dot menu and switch it off.

```text
Rough notes: Priya, book club, Thursday the 12th, my porch, bring a pen. Write the reminder.
```

```text
Give me three ideas for a rainy-day game for a seven-year-old.
```

**Self-check:**

- [ ] The upload worked, or I wrote down which failure it was.
- [ ] The reminder had a greeting with Priya's name, one reminder sentence, one friendly line, and the closing line.
- [ ] The rainy-day answer did not look like a reminder note.
- [ ] I switched the Skill off at the end.

**What good looks like:** a reminder that follows your rules and ends with the closing line, and a rainy-day answer that ignores them. If the Skill did not run, fix the description first, upload again and retest. If the upload failed, compare the folder name to the Skill name and check that `SKILL.md` is inside the folder.

When you have done the tasks, press the practice button below. It saves that you finished.

<div id="practice-done"></div>

## Further reading

Optional. This goes to Anthropic's own page. Read what it says today, since it changes.

- Use Skills in Claude: [https://support.claude.com/en/articles/12512180-use-skills-in-claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and you can move on.

<div id="quiz"></div>
