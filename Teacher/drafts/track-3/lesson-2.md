# Ask Claude to write a formula

About 10 minutes to read, plus about 35 to do the practice

## What you will be able to do

- Describe a spreadsheet to Claude clearly enough that the formula it writes fits your sheet.
- Test any formula Claude gives you against an answer you worked out yourself.
- Paste an error back to Claude and get a fix you understand.

## What you will make

A gift-list sheet with three working formulas: money spent so far, money still to spend, and how many gifts are left to buy. You will be able to explain each one in your own words, which is the real goal. A formula you cannot explain is one you cannot trust.

## The three steps: describe, test, fix

You learned in the last lesson that formulas are small instructions. The hard part is not typing them. It is knowing which one you need. That is where Claude helps. It is good at turning a plain sentence into a formula, and it never gets tired of "what if I wanted it a different way".

It is also a tool that sounds sure when it is wrong, as you may already have noticed. So the pattern has three steps, and the middle one is not optional.

**1. Describe.** Claude cannot see your sheet. It only knows what you type. So tell it three things: what is in each column, which rows hold your data, and what you want the answer to be. Naming the columns by letter matters. "The price column" can mean anything. "Column C" cannot.

**2. Test.** Before you trust the formula, work out the right answer by hand on a small piece of data. Then see whether the sheet agrees. If it does, try one more case where the answer should change. A formula can look right and be wrong for half your data.

**3. Fix.** If the sheet shows an error, or a number that is not what you worked out, go back to Claude. Paste the exact formula, say what you expected, and say what you got. Copy any error text exactly. The more exact you are, the better the fix.

## A few things that trip people up

- **Rows.** If your data may grow, tell Claude to use rows 2 to 100, not just the rows you have today. You learned why in the last lesson.
- **Quote marks.** When a formula has words in it, the quote marks must be the plain straight kind. If a formula pasted in from a chat looks like it has curly quotes, delete them and type the straight ones yourself on your keyboard. Curly quotes can make Sheets give an error, so if a formula fails, check the quotes first.
- **Commas and semicolons.** Some regions use semicolons between parts of a formula. If Claude's formula has commas and Sheets complains, try semicolons. This depends on your settings, so check Google's help pages: [https://support.google.com/docs](https://support.google.com/docs).
- **Private data.** Use made-up data when you ask. You are describing the layout, not handing over your real list. Claude does not need real names or numbers to write a formula.

## Keep this in your pocket

1. Tell Claude the columns by letter, the rows with data, and the answer you want.
2. Test the formula against an answer you worked out by hand.
3. If it fails, paste the exact formula and the exact error, and say what you expected.

## Practice

Three jobs, about 10 to 15 minutes each. Open Google Sheets in one browser tab and claude.ai in another. The free version of Claude is all you need, and free ChatGPT can do the same jobs, so try the same request in both and compare. If Claude says you have reached a limit for now, take a break and come back. The free plan has limits, and what they are changes, so check Anthropic's own page yourself: [https://claude.ai](https://claude.ai).

Everything uses a made-up gift list.

### Task 1: Describe a sheet and get your first formula

**Why it matters:** this is the skill the whole lesson rests on. Getting the description right is most of the job.

**Do this:** start a new blank sheet. Type these headings in row 1 and the six rows underneath.

| Name | Gift | Price | Bought |
|---|---|---|---|
| Mom | Scarf | 28 | Yes |
| Dad | Book | 18 | Yes |
| Sam | Game | 45 | No |
| Jess | Candle | 15 | Yes |
| Lee | Mug | 12 | No |
| Aunt Ruth | Tea set | 32 | Yes |

Before you ask Claude anything, work out by hand how much you have spent on gifts marked Yes. Write the number down. Then send Claude this:

```text
I am using Google Sheets. Row 1 has headings. Column A is Name, column B is
Gift, column C is Price (a number), column D is Bought (the word Yes or No).
My data is in rows 2 to 7 now, but I will add more later, so please use rows
2 to 100. I want one formula that adds up the Price of every gift where
Bought is Yes. Give me only the formula first, then one sentence on what it does.
```

Click an empty cell to the side, for example F2, type the formula Claude gives you, and press Enter. Compare the answer to your hand number.

**Self-check:**

- [ ] I worked out my own answer before I asked.
- [ ] My description named the columns by letter and gave the row range.
- [ ] The sheet's answer matches my hand number.
- [ ] I can read the formula and point at the part that means "only the Yes rows".

**What good looks like:** 93. If Claude's formula gives something else, do not guess. Go to Task 3's fix step and treat it as a bug to report. If it does match, you now have a formula you wrote in plain English.

---

### Task 2: Make Claude explain it, then explain it back

**Why it matters:** a formula you copied and cannot explain will break one day, and you will not know why. Explaining it back is how you own it.

**Do this:** first ask Claude to explain the formula from Task 1 one piece at a time. Then close your eyes, or look away, and say out loud what each piece does. Then ask Claude two new questions, still using columns A to D:

- The total of Price for gifts marked No, which is the money you still need to spend.
- How many gifts are marked No.

Work out both answers by hand first. Put each formula in its own cell, with a label beside it.

```text
Explain the formula you just gave me one piece at a time, in plain words,
as if I have never seen a spreadsheet. Then tell me one way it could give
a wrong answer on my sheet.
```

**Self-check:**

- [ ] I understand each piece of the first formula well enough to say it out loud.
- [ ] I did the hand math for the two new questions before I asked.
- [ ] The sheet matches my hand answers for both.
- [ ] I asked Claude how a formula could go wrong, and I understood its answer.

**What good looks like:** 57 for the money still to spend (45 plus 12), and 2 gifts left to buy. Claude will probably use `SUMIF` and `COUNTIF`. If it picked something different and the answers still match your hand math, that is fine. There is often more than one right formula. What matters is that you can explain the one in your cell.

---

### Task 3: Break a formula and fix it with Claude

**Why it matters:** formulas fail all the time, and a red error is just a message. Learning to hand that message to Claude is the skill that makes you independent.

**Do this:** type this broken formula into an empty cell. The mistake is that the word Yes has no quote marks around it.

```text
=SUMIF(D2:D100, Yes, C2:C100)
```

Sheets will show an error, probably one that starts with a hash mark. Copy the error text exactly. Send Claude the formula, the error, and what you expected. Ask it to explain the problem before it fixes it.

```text
This formula in Google Sheets: =SUMIF(D2:D100, Yes, C2:C100)
gives me this error: [paste the exact error text]
I expected it to add the Price of every row where Bought is Yes.
First tell me in plain words what is wrong. Then give me the fixed formula.
```

Paste the fix into a cell and test it against your hand number from Task 1.

If you finish early, try this. Change one Bought cell from Yes to No, and watch your totals move. Then add a seventh gift on row 8. Do your formulas include it? If you used rows 2 to 100, they should.

**Self-check:**

- [ ] I copied the error text exactly, not from memory.
- [ ] Claude told me what was wrong before it gave the fix.
- [ ] The fixed formula gives the same answer as Task 1.
- [ ] I tested a change, a Yes switched to No, and the totals moved the right way.

**What good looks like:** Claude should say that the word needs quote marks so Sheets reads it as text and not as a name. If its explanation does not make sense to you, ask again: "say that more simply". If the fix does not give 93, report that back with the new number and ask again. Getting a wrong fix is normal. What counts is that you tested before you believed it.

When you have done the tasks, press the practice button below. It saves that you finished and opens the next lesson. Passing the quiz with 2 of 3 right opens it too.

<div id="practice-done"></div>

## Further reading

These are optional. They go to the companies' own pages, which were not read for this lesson. Read what they say today, since these tools change often.

- Google Docs Editors Help, which covers Sheets: [https://support.google.com/docs](https://support.google.com/docs)
- Claude, from Anthropic: [https://claude.ai](https://claude.ai)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and the next lesson opens.

<div id="quiz"></div>
