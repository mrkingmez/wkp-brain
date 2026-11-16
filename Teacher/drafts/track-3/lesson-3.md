# Forms to sheets

About 10 minutes to read, plus about 40 to do the practice

## What you will be able to do

- Build a Google Form and send its answers into a Google Sheet automatically.
- Add a formula that counts the answers as they come in.
- Know who can see and fill in a form before you ever share it.

## What you will make

A "family dinner vote" form with four questions, wired to a sheet that tallies the votes by itself. Then a second form of your own choosing. You will fill both in yourself with made-up answers. Nobody else gets a link in this lesson.

## What a form does that a sheet does not

In the last two lessons you typed every row yourself. That works when you are the only person with the information. It stops working the moment other people hold it: who is coming Saturday, which night works, who signed up for which chore.

A **Google Form** is a page of questions. Anyone you give the link to fills it in, and each submitted answer lands as a new row in a Google Sheet. You do not copy and paste anything. You do not chase people for a reply in three different places. The sheet fills up while you do something else.

That is automation of the most useful kind. You set it up once, and it keeps working without you.

The pieces are simple.

| Piece | What it is |
|---|---|
| **The form** | The questions people see and answer |
| **The responses** | Each submitted answer, one per person |
| **The linked sheet** | A spreadsheet where every response is one row, and every question is one column |

## Question types, in plain words

When you add a question, a Form asks what kind it is. Names change over time, so look for the closest match.

- **Short answer** is a one-line box. Good for a name.
- **Multiple choice** lets a person pick one option. Good for "which night".
- **Checkboxes** let a person pick several.
- **Dropdown** is a list that opens when clicked. Good for long lists.

Pick the type that makes the answers easy to count. Multiple choice and dropdown are the easiest, because everyone picks from the same words. If you use short answer for something like a dish, you will get "Tacos", "Taco night", and "tacos please", and your count will split three ways. That is the same trap as the spelling problem in lesson 1.

## Who can see and fill in your form

This part is easy to skip and worth reading. A form has a link, and a link can be passed around. Who is allowed to open it, and whether they need to sign in, are settings that Google controls and may change. Check Google's own help pages yourself before you share a form with anyone: [https://support.google.com/docs](https://support.google.com/docs).

Two habits cover most of it.

- Ask only for what you need. A dinner vote needs a first name and a choice. It does not need an address.
- Test with yourself first. Send nothing to anyone until you have filled in the form and seen the answer land in the sheet.

## Keep this in your pocket

1. A form collects answers from other people, and each answer becomes a row in a sheet.
2. Use multiple choice or dropdown for anything you plan to count.
3. Ask only for what you need, and test it yourself before sharing the link.

## Practice

Three jobs, about 10 to 15 minutes each. You need a browser and a Google account. Go to Google Forms (search for "Google Forms" and pick the result from Google) and start a blank form. Menus change, so where this lesson names a button or menu, look for the closest name.

Everything uses made-up answers. Do not put in anyone's real details.

### Task 1: Build the dinner vote form

**Why it matters:** building one end to end is the fastest way to see how forms work. It takes about ten minutes.

**Do this:** give the form a title, **Family dinner vote**. Add these four questions.

| Question | Type | Options |
|---|---|---|
| First name | Short answer | |
| Which night works best? | Multiple choice | Friday, Saturday, Sunday |
| What should we make? | Multiple choice | Tacos, Pasta, Stir fry |
| Anything we should know? | Short answer | |

For the first three, look for a switch labeled **Required** and turn it on. Leave the last one optional. Then find the preview option, which is usually an eye icon near the top, and open the form as a person would see it. A preview may or may not record answers you submit, so check in Task 2 rather than assuming.

Paste this into any note to yourself as your question list, and tick them off as you add them.

```text
1. First name (short answer, required)
2. Which night works best? Friday, Saturday, Sunday (multiple choice, required)
3. What should we make? Tacos, Pasta, Stir fry (multiple choice, required)
4. Anything we should know? (short answer, optional)
```

**Self-check:**

- [ ] My form has a title and four questions.
- [ ] The two "pick one" questions use multiple choice, not short answer.
- [ ] The first three questions are marked required, the last is not.
- [ ] I opened the preview and read it as a visitor would.

**What good looks like:** a short form that takes about thirty seconds to fill in. If you find yourself writing more than five or six questions, stop and ask whether you need them all. Short forms get answered. Long ones get closed.

---

### Task 2: Send the answers to a sheet and count them

**Why it matters:** the sheet is where a form becomes useful. Counting the votes is the same skill from lesson 1, with answers that now arrive on their own.

**Do this:** in your form, look for a tab called **Responses**. There should be a button or icon to link to Google Sheets, often a green sheet icon. Click it and choose to create a new spreadsheet. Menus change, so look for the closest wording. Open the new sheet.

Now fill in your own form three times, using the preview link or the share option for your own use only, with made-up answers, for example:

| Name | Night | Dish |
|---|---|---|
| Pat | Friday | Tacos |
| Sam | Saturday | Tacos |
| Lee | Friday | Pasta |

Go back to the sheet and watch three new rows appear. You may need to refresh the page. Look at the headings in row 1. Google usually adds a time column, so your first question may be in column B, not A. Do not assume. Read the headings and find the column that holds the dish.

Now count. Click an empty cell off to the side and type this, changing the column letter to match the dish column in your sheet. Work out the right answer by hand first.

```text
=COUNTIF(D2:D100, "Tacos")
```

Make a second count for Pasta, and a third for Stir fry. Then ask Claude for something harder, using a description of your layout only and no real data.

```text
I use Google Sheets with a Google Form feeding it. Column B is the person's
name, column C is the night they picked (Friday, Saturday or Sunday), and
column D is the dish they picked. Rows 2 to 100 hold the answers. Give me
one formula that shows which night got the most votes, and tell me what it
does in plain words.
```

Test what Claude gives you against your three rows.

**Self-check:**

- [ ] My three test answers appeared as rows in the sheet.
- [ ] I read the headings to find the right column instead of guessing.
- [ ] The Tacos count matches my hand count.
- [ ] I tested Claude's "most votes" formula against the three rows.

**What good looks like:** Tacos 2, Pasta 1, Stir fry 0, and Friday as the winning night with two votes. If your sheet has a different layout from the one in the prompt, change the prompt to match your real columns. One honest warning. If two nights tie, a formula that picks a single winner may only show one of them. Ask Claude what happens in a tie, then test it by adding a fourth test answer.

One more rule while the sheet is open. Do not type over the columns that the form fills in. Put your counts and notes off to the side. If a form is still collecting answers, edits in those columns can cause confusion, and Google's help pages say how it behaves: [https://support.google.com/docs](https://support.google.com/docs). Check that yourself.

---

### Task 3: Design a form for a real small job

**Why it matters:** the next time you need answers from several people, you will already know how to get them.

**Do this:** pick one real small job where you would otherwise ask people one at a time. Ideas: a Saturday cookout RSVP, a chore sign-up, a book club pick, a potluck sign-up. Sketch it on paper first. Write the question, the type, and the options for each question, and ask only for what the job needs. Then build it, link it to a new sheet, fill it in three times with made-up answers, and add one formula that summarizes the results.

Use this sketch template, one block per question.

```text
Question: [what you are asking]
Type: [short answer, multiple choice, checkboxes or dropdown]
Options: [the choices, if any]
Why I need it: [one sentence]
```

Do not send the link to anyone as part of this lesson. When you decide to, that is your call. Check who can open it and whether it needs a sign-in, using Google's help pages, before you do.

**Self-check:**

- [ ] I sketched the questions on paper before building.
- [ ] Every question I picked has a reason, and none asks for something I do not need.
- [ ] I tested with three made-up answers and checked my summary formula by hand.
- [ ] I know where to look to check who can fill the form in before I share it.

**What good looks like:** a small form, a sheet that fills itself, and one formula that answers the question you built the form to ask. A summary that matches your hand count means the whole chain works, from questions to answers to totals.

When you have done the tasks, press the practice button below. It saves that you finished and opens the next lesson. Passing the quiz with 2 of 3 right opens it too.

<div id="practice-done"></div>

## Further reading

These are optional. They go to Google's own help pages, which were not read for this lesson. Read what they say today, since menus and settings change.

- Google Docs Editors Help, which covers Forms and Sheets: [https://support.google.com/docs](https://support.google.com/docs)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and the next lesson opens.

<div id="quiz"></div>
