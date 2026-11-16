# Make it show its work

About 12 minutes to read, plus about 40 to do the practice

## What you will be able to do

- Ask the AI to go step by step, so you can see where an answer goes wrong.
- Ask it to separate what it is sure of from what it is guessing.
- Check one answer against a real source, and know why "it explained itself" is not proof.

## What you will make

A short "checked answer" sheet. You will have the AI work through a small problem step by step, check the arithmetic yourself, pull a list of claims out of an answer, and look two of them up in a real place. You finish with proof, in your own handwriting or Google Doc, of one thing the AI got right and one thing worth a second look.

## Why ask for the steps

Imagine a student hands you the answer to a math problem and nothing else. You cannot tell if they understood it or got lucky. Ask for the steps, and now you can read along. If step three is wrong, you see it.

The AI is the same. If you ask a multi-part question and get one confident line back, you have nothing to check. If you ask it to go step by step, you get a trail. You can follow the trail, and the trail is easier to catch mistakes in than the final answer.

Compare these two.

> Is it cheaper to buy the family pack of chicken or two small packs?

> Is it cheaper to buy the family pack of chicken or two small packs? Work it out step by step. Show the price per pound for each, then say which is cheaper. Tell me the numbers you used so I can check them.

The second one makes the AI lay out the prices it is using. You can compare those to the real shelf tags.

## Useful phrases

You can add any of these to a prompt.

- **"Work through it step by step."** Good for plans, comparisons, and anything with numbers.
- **"Show your numbers so I can check them."** Good for money, time, and measurements.
- **"List the facts you are relying on."** Good when the answer depends on things that could be wrong.
- **"Tell me what you are sure of and what you are guessing."** Good for anything you plan to act on.
- **"What would change this answer?"** Good for decisions. It surfaces the things you did not mention.

## Showing work is not proof

This is the most important idea in the lesson, so slow down for it.

When the AI shows its steps, it is writing steps that read well. A smooth explanation can still contain a wrong number, a wrong rule, or a made-up fact. The steps make a mistake **easier for you to find**. They do not make a mistake **less likely to be there**.

So the habit has two halves:

1. Ask for the steps, so there is something to check.
2. Then actually check one or two of them against something outside the AI: a calculator, a price tag, an official website, a book, or a person who knows.

If you do only the first half, you have a nicer-looking answer and the same risk.

## Be careful with sources

You can ask the AI to name where a fact comes from. That is a good question. It is not a safe answer.

An AI can write a source that looks real: a book title, an author, a web address. It may be real. It may also be invented, because inventing something plausible is the thing these tools do. Treat any source it names as a **lead to look up**, not as proof. Open the link, or search for the exact title. If you cannot find it, then the answer rests on nothing.

The Stay Safe lesson "How to check what AI tells you" covers this in depth. Here you will practice the basic move.

## Keep this in your pocket

1. Ask for the steps and the numbers, so you can see where an answer could go wrong.
2. Ask what it is sure of and what it is guessing.
3. Showing work is not proof. Check one or two steps or sources outside the AI.

## Practice

Three jobs, about 10 to 15 minutes each. Use claude.ai. You will need a calculator (the one on your phone is fine) and a web browser for a search. Use made-up numbers and public topics only.

### Task 1: Work a money problem step by step

**Why it matters:** numbers are where a smooth answer can hide a small mistake, and you can check numbers with a calculator in a minute.

**Do this:** paste the prompt below into a new Claude chat. Read each step. Then take out your calculator and redo every calculation yourself. Mark each step as correct or not.

```text
I am planning a small family dinner for 8 people. I have a budget of $60.
Chicken costs $3.50 a pound and I need half a pound per person.
Rice costs $2 a bag and one bag feeds 8 people.
Vegetables cost $12 in total.
Work through it step by step. Show every number you use and every calculation, then tell me how much money I would have left.
```

**Self-check:**

- [ ] I redid every calculation on my own calculator.
- [ ] I marked each step as correct or not.
- [ ] I can say which step I checked first, and why.
- [ ] If anything was off, I noticed whether the explanation still sounded sure.

**What good looks like:** the numbers should work out to 4 pounds of chicken at $14, $2 of rice, $12 of vegetables, $28 total, and $32 left. Your calculator is the authority, not this lesson, so do the math yourself and confirm. If the AI got it right, that is one clean result, not a guarantee, so keep checking when the numbers matter. If it got a step wrong, copy the wrong step into your sheet. That is exactly what the step-by-step habit catches.

---

### Task 2: Pull the claims out of an answer

**Why it matters:** a paragraph of facts is hard to check as a block. A list of claims, each one separate, is easy to check one at a time.

**Do this:** in a new Claude chat, ask the first prompt. When it answers, send the second prompt in the same chat. Choose a public topic you do not know well, so you are truly learning, such as how a lighthouse works or why leaves change color. Then pick the two claims on the list that matter most, and look each one up on a source that is not an AI: an encyclopedia, a museum or university site, or a government site. Write down whether the source agreed.

```text
In three or four sentences, explain [a public topic you want to learn about].
```

```text
Now list every separate factual claim you just made, one per line. Next to each, write "sure" or "guessing" and say why.
```

**Self-check:**

- [ ] The list has one claim per line, and each one has a sure or guessing mark.
- [ ] I looked up two claims on a source that is not an AI.
- [ ] I wrote down whether each source agreed, disagreed, or did not say.
- [ ] I noticed whether its "sure" marks matched what I found.

**What good looks like:** a short sheet with the claims, the AI's marks, and your checks. The usual result is that most claims hold up and one is a little off or too general. A claim marked "sure" that turns out wrong is the most useful thing you can find, because it tells you the AI's confidence is not a measure of truth. If you could not find a claim anywhere, write "could not confirm" and treat it as unproven.

---

### Task 3: Ask for sources, then open every one

**Why it matters:** this is how you see for yourself that a source named on the screen may not exist anywhere else.

**Do this:** in a new Claude chat, send the prompt below. For each source it names, try to find it. If it gives a web address, type it into your browser. If it names a book or article, search the exact title in a search engine. Mark each as found, not found, or found but it does not say that. Then try the same prompt in ChatGPT and compare.

```text
I want to learn about [a public topic, such as how bees make honey]. Give me three sources I can read, with the title and who made it. Tell me clearly if you are not sure a source exists.
```

**Self-check:**

- [ ] I tried to find every source, not only the first one.
- [ ] I marked each as found, not found, or found but it does not support the claim.
- [ ] I checked whether the AI warned me when it was unsure.
- [ ] I compared what Claude and ChatGPT did.

**What good looks like:** a list of sources with your honest marks next to each. You may find all of them are real. You may find one that does not exist. Either is a good outcome. The thing to carry out of here is the habit: a named source is a lead, you open it, and if it is not there you do not rely on it.

When you have done the tasks, press the practice button below. It saves that you finished and opens the next lesson. Passing the quiz with 2 of 3 right opens it too.

<div id="practice-done"></div>

## Further reading

These are optional. They go to the companies' own pages. Read what they say today, since these tools change often.

- Claude, from Anthropic: [https://claude.ai](https://claude.ai)
- ChatGPT, from OpenAI: [https://chatgpt.com](https://chatgpt.com)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and the next lesson opens.

<div id="quiz"></div>
