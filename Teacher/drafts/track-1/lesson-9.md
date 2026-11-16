# Advanced: chains and checking

About 12 minutes to read, plus about 50 to do the practice

## What you will be able to do

- Break a big chore into a chain of small prompts, where each one feeds the next.
- Put a checkpoint between the links, so a mistake does not ride all the way to the end.
- Use a second pass, and a second tool, to review a result, and know what that does and does not prove.

## What you will make

A three-step workflow for a real chore you do every week. You will run a practice chain first, a weekly dinner plan that turns into a grocery list that gets checked against the plan. Then you will build your own chain, test it, and save it in your prompt library.

## What a chain is

So far you have done jobs in one message, or in a few messages back and forth. A chain is a planned set of steps. The result of step one goes into step two. The result of step two goes into step three. You decide the order ahead of time, and you check along the way.

Why not ask for everything at once? Because a big, tangled request gives the AI too many things to juggle, and you cannot tell which part went wrong. A chain gives each step one clear job, and a place where you can look.

Picture an assembly line with a person at each station who glances at the part before passing it on. That glance is the whole point.

## A chain for a real chore

Take the weekly dinner problem. One message that says "plan my week of dinners, make a shopping list, and make sure it is cheap and has no waste" is a lot. Split it.

1. **Plan.** Seven dinners from what you have and what your family eats. *Checkpoint: you read the list and fix anything you would not cook.*
2. **List.** Turn the approved plan into a grocery list, sorted by store section. *Checkpoint: you pick two meals and confirm every ingredient made it onto the list.*
3. **Review.** Ask for a check of the list against the plan, to flag anything missing or doubled. *Checkpoint: you decide what to change. The review is advice, not the answer.*

Notice the checkpoints are yours. The chain is not "AI does three things." It is "AI does a step, you look, AI does the next step."

## The review step

Asking the AI to review a result is useful. It can catch a missing item, a doubled item, or a line that does not match the plan. It is quick, and on the free versions it costs you nothing but a few minutes. If a tool tells you that you have hit a usage limit, stop, come back later, or use the other tool for that step.

It has a limit. A reviewer made by the same type of tool can share the same blind spots. If the first pass invented a fact, the review may accept it, because it reads fine. So treat a review as a second pair of eyes that can miss things, and not as proof. A few ways to make it stronger:

- **Review in a new chat.** Give the reviewer the plan and the list only, not the conversation that made them. It reads them fresh.
- **Review in the other tool.** Run the same check in ChatGPT on Claude's work, or the other way around. Two tools disagreeing is a signal to look closer.
- **Give the reviewer a specific job.** "Check that every ingredient in the plan appears in the list" works better than "is this good?"
- **Keep the final check human.** On anything that matters, such as money, health, law, or what you send to another person, the last look is yours, with a real source.

## When a chain is too much

Not every job needs one. A short thank-you note does not need three steps. Use a chain when a job has several parts, when the later parts depend on the earlier ones, or when a mistake early on would be expensive later. If you can check the whole result in one glance, one prompt is fine.

## Keep it simple

Three links is plenty. A chain with eight steps is hard to check and hard to repeat. If you want more, you probably have two chains.

## Keep this in your pocket

1. A chain is a planned set of small prompts, each one feeding the next, with a checkpoint between them.
2. A review pass helps, and it can share the original's mistakes. Use a new chat or the other tool, and give it a specific job.
3. The final check on anything that matters is yours, against a real source.

## Practice

Three jobs, about 15 to 20 minutes each. Use claude.ai and chatgpt.com. Keep your prompt library Doc open. Made-up details only.

### Task 1: Run the dinner chain

**Why it matters:** running a chain once, with checkpoints, shows you how the pieces fit before you build your own.

**Do this:** open a new Claude chat. Send step 1. Read the plan and change anything you would not cook by telling Claude what to swap. Send step 2. Pick two meals and tick each ingredient off the list by hand. Then open a **new** chat, and send step 3 with your plan and list pasted in.

```text
STEP 1:
Plan seven dinners for a family of four. We like simple food, we have about 30 minutes on weeknights, one person does not eat meat, and we want two dinners that make leftovers for lunch. Give me one line per dinner that names the dish and its main ingredients.
```

```text
STEP 2:
Using this approved plan, make a grocery list sorted by store section. Combine items that appear in more than one dinner and show the quantity needed for four people.

[paste the approved plan]
```

```text
STEP 3:
Check this grocery list against this dinner plan. Tell me (1) any ingredient in the plan that is missing from the list, (2) any item on the list that does not belong to any dinner, and (3) any item that is listed twice. Do not rewrite the list. Only report.

PLAN:
[paste the plan]

LIST:
[paste the list]
```

**Self-check:**

- [ ] I checked the plan before I made the list, and changed at least one dinner if I wanted to.
- [ ] I ticked two meals' ingredients off the list by hand.
- [ ] I ran step 3 in a new chat so it read the plan and list fresh.
- [ ] I decided what to fix myself, and did not just accept the review.

**What good looks like:** a plan, a list, and a short review that is either "all fine" or names real gaps. If you found a missing ingredient on your own that the review missed, write that down. It is a good lesson in what a review can miss. If the review flagged something that was not actually wrong, you used your own judgment to ignore it, and that is exactly the job.

---

### Task 2: Build your own three-step chain

**Why it matters:** a chain you built for your own chore is the one you will actually keep using.

**Do this:** pick one real chore with several parts that you do again and again. Good candidates: planning a week of chores, preparing for a trip, organizing a pile of paperwork notes into a to-do list, planning a small party, or writing and tidying a weekly message to a group. Write the three steps on paper first. For each one, write what goes in, what comes out, and what you will check. Then write each step as a prompt with blanks, and run the whole chain once in Claude with made-up details. If you want a start, this prompt helps.

```text
I want to build a three-step workflow for this chore: [describe it]. Each step should take the output of the last one. For each step, give me the prompt, with [blanks] for the parts that change, and tell me what I should check before moving to the next step. Ask me up to three questions first if you need them.
```

**Self-check:**

- [ ] My chain has three steps, each with one clear job.
- [ ] Each step names what I will check before moving on.
- [ ] I ran the whole chain once, start to finish, with made-up details.
- [ ] I changed at least one prompt after seeing where it went wrong.

**What good looks like:** three step prompts you can run in order, plus a line for each checkpoint. If a step did two jobs, split it. If two steps did almost the same thing, merge them. The first run is almost always a little wrong. The second is where it starts to work.

---

### Task 3: Cross-check with the other tool

**Why it matters:** this is where you learn how much a second opinion is worth, and where it falls short.

**Do this:** take the final output of your chain from Task 2. Paste it into ChatGPT in a new chat with the prompt below. Then read what it says and decide, one point at a time, whether the review was right. For each point, check against something that is not an AI: your own knowledge, a calculator, a real website, or a person. Then save your chain, with its checkpoints, into your prompt library.

```text
Here is a result I made with an AI. I want you to check it carefully. Do not rewrite it. List anything that looks wrong, missing, or unsupported, and say how sure you are about each point. If you think everything is fine, tell me what you checked.

[paste the result]
```

**Self-check:**

- [ ] I decided for each review point whether it was right, wrong, or could not tell.
- [ ] I checked at least one point against something that is not an AI.
- [ ] I noticed whether the review missed something I already knew was a problem.
- [ ] I saved the chain in my prompt library with a name, a use, the steps, and a test date.

**What good looks like:** a short list of review points, with your own mark next to each. A good result can go several ways. The review can catch something real. It can raise a false alarm, which you ignored. Or it can say all is fine when you can see a flaw, which is the one to remember. Whichever happened, you now have a chain, a review step, and a clear sense of where your judgment is the last word.

When you have done the tasks, press the practice button below. It saves that you finished. That completes Track 1, so the next track on the home page is yours to pick.

<div id="practice-done"></div>

## Further reading

These are optional. They go to the companies' own pages. Read what they say today, since these tools change often.

- Claude, from Anthropic: [https://claude.ai](https://claude.ai)
- ChatGPT, from OpenAI: [https://chatgpt.com](https://chatgpt.com)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and you have finished Track 1.

<div id="quiz"></div>
