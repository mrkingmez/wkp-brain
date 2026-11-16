# Automate with a spreadsheet

About 10 minutes to read, plus about 35 to do the practice

## What you will be able to do

- Type a formula into Google Sheets so a total updates itself when the numbers change.
- Build a small summary table that adds up each category and flags the ones that went over.
- Catch the two most common spreadsheet slips: a range that is too short and a category spelled two ways.

## What you will make

A budget tracker with a summary block on top. You type in what you spent, and the totals, the amount left, and an "Over" or "OK" flag fill in on their own. If you would rather track chores or a garden, the same pattern works. Pick whichever matters to you in Task 3.

## Why a spreadsheet is the first thing to automate

"Automate" sounds like a big word. Here it means one small thing: you do the job once, and the sheet does the math every time after that.

A spreadsheet is a grid. Each box is a cell, and each cell has an address made of a column letter and a row number. The box in column D, row 2 is **D2**. That is all an address is.

A **formula** is a cell that works something out instead of holding a plain number. It always starts with an equals sign. If you type `=2+2` into a cell and press Enter, the cell shows 4. That is a formula, and it is a boring one. The useful ones point at other cells, so when those cells change, the answer changes with them.

You will use four things in this lesson.

| What you type | What it does |
|---|---|
| `=SUM(D2:D100)` | Adds every number in column D from row 2 down to row 100 |
| `=SUMIF(C2:C100, F2, D2:D100)` | Adds the numbers in D, but only on rows where column C matches what is in F2 |
| `=G2-H2` | Subtracts one cell from another |
| `=IF(I2<0, "Over", "OK")` | Shows "Over" if I2 is below zero, otherwise "OK" |

The part in brackets is called a **range**. `D2:D100` means "from D2 down to D100". You can type a range, or click and drag over the cells while you are inside a formula.

## What you need

A Google account, and a browser. If your email is Gmail, you already have a Google account. If not, Google's sign-in page has a create-account link. That is the one signup this lesson may ask of you, it is your choice, and it is worth reading what Google asks for before you agree.

Go to Google Sheets (search for "Google Sheets" and pick the result from Google) and start a blank spreadsheet. Menus change, so where this lesson names a menu, look for the closest name if you do not see the exact one.

## Why the range goes to row 100

Here is a trap worth learning now. If your range is `D2:D9` because you have eight rows today, a new row at row 10 sits outside it. The total will quietly ignore it. Nothing flashes red. The number is just wrong.

So make the range longer than the data you have. Rows 2 to 100 are empty for now, and an empty cell adds nothing. You will see this in the practice.

## Keep this in your pocket

1. A formula starts with `=` and points at other cells, so the answer updates when they change.
2. `SUM` adds, `SUMIF` adds only the rows that match, `IF` shows one word or another.
3. Make ranges longer than your data, and check the first result against a number you worked out by hand.

## Practice

Three jobs, about 10 to 15 minutes each. Everything uses made-up numbers. Do not type in real account numbers or anything private.

### Task 1: Set up the list and add the total

**Why it matters:** every tracker starts as a plain list. Once the total is a formula, you never add anything by hand again.

**Do this:** in your blank sheet, type these headings in row 1: **Date** in A1, **What** in B1, **Category** in C1, **Amount** in D1. Then type the eight rows below, starting in row 2. Sheets may change how a date looks. That is fine.

| Date | What | Category | Amount |
|---|---|---|---|
| Nov 1 | Weekly shop | Groceries | 84.50 |
| Nov 2 | Fill up | Gas | 40.00 |
| Nov 3 | Movie night | Fun | 25.00 |
| Nov 5 | Milk and bread | Groceries | 12.30 |
| Nov 8 | Fill up | Gas | 38.75 |
| Nov 9 | Coffee with a friend | Fun | 15.50 |
| Nov 10 | Weekly shop | Groceries | 61.20 |
| Nov 12 | Fill up | Gas | 42.10 |

Now click cell F7, type the label **Total**, then click G7 and type the formula below and press Enter. (Keep it out of column D, or the total would try to add itself.) First, add the eight amounts on paper or a calculator. The sheet should agree.

```text
=SUM(D2:D100)
```

If Sheets shows an error instead of a number, check that you typed the brackets and the colon exactly. If your computer is set to a region that uses semicolons in formulas, try a semicolon where this lesson has a comma. That depends on your settings, so check Google's help pages yourself: [https://support.google.com/docs](https://support.google.com/docs).

**Self-check:**

- [ ] My headings are in row 1 and my data starts in row 2.
- [ ] I worked out the total by hand before I looked at the sheet's answer.
- [ ] The sheet's total matches my hand total.
- [ ] I can say what `D2:D100` means in my own words.

**What good looks like:** a total of 319.35. If yours is different, look for a number typed with a letter in it, or an amount in the wrong column. When the hand total and the sheet disagree, the sheet is usually right and the typing is wrong, but check both.

---

### Task 2: Build the category summary

**Why it matters:** one grand total tells you little. A budget answers "how much is left for gas?", and that needs a total per category.

**Do this:** to the right of your data, in column F, build this small table starting at F1. The first three columns are typed. The last three are formulas you will write.

| F | G | H | I | J |
|---|---|---|---|---|
| Category | Budget | Spent | Left | Status |
| Groceries | 200 | formula | formula | formula |
| Gas | 150 | formula | formula | formula |
| Fun | 50 | formula | formula | formula |

In **H2** (Spent for Groceries), type the first formula. It says: look down column C for rows that match F2, and add up the matching amounts from column D.

```text
=SUMIF($C$2:$C$100, F2, $D$2:$D$100)
```

The dollar signs lock the ranges so they do not slide when you copy the formula. Leave them as they are.

In **I2** (Left), type `=G2-H2`. In **J2** (Status), type:

```text
=IF(I2<0, "Over", "OK")
```

Now select H2, I2 and J2 together. At the bottom right corner of the selection there is a small square. Drag it down two rows. Sheets copies the formulas into the Gas and Fun rows and adjusts F2 to F3 and F4 for you.

**Self-check:**

- [ ] Groceries shows 158 spent, Gas shows 120.85, Fun shows 40.5.
- [ ] The Left column equals Budget minus Spent on each row.
- [ ] All three Status cells say OK right now.
- [ ] I can explain why the formula points at F2 and not at the word "Groceries" typed inside it.

**What good looks like:** pointing at F2, instead of typing the word into the formula, is the whole trick. The same formula now works for any category you type in column F. If a Spent cell shows 0 when you expected a number, the category in column C and the category in column F do not match exactly. A trailing space is enough to cause that.

---

### Task 3: Make it yours, then break it on purpose

**Why it matters:** a tracker you trust is one you have tried to fool. Finding the weak spots now is cheaper than finding them next month.

**Do this:** three small experiments, in this order.

1. Add a ninth data row: Nov 14, Snacks, Fun, 12. Watch Fun's Left go negative and its Status flip to Over without you touching a formula.
2. Add a tenth row: Nov 15, Bread, **Grocery**, 4.50. Note the spelling is Grocery, not Groceries. Look at the Groceries total. It does not move. Fix the spelling and watch it update.
3. Make it yours. Either change the three categories and budgets to ones that fit your life, or build a chore tracker with the same layout: Date, Who, Chore, Minutes, with a summary of minutes per person. Anything you change, check one result by hand.

Optional: select the Category and Spent cells in your summary and look for an option to insert a chart. The menu is usually called Insert. Menus change, so look for the closest name. A chart is a nice finish, not a requirement.

If you get stuck on a formula, you can paste it into Claude along with a sentence about what you wanted, using made-up data only. The next lesson is all about that.

```text
I am using Google Sheets. I typed this formula into a cell: [paste it].
I expected [what you expected]. Instead I got [what you got].
Can you tell me what is wrong, in plain words, before you give me a fix?
```

**Self-check:**

- [ ] I added a row and saw the totals change on their own.
- [ ] I saw the misspelled category get left out, and I fixed it.
- [ ] I changed or added something of my own.
- [ ] I checked at least one result by hand after my change.

**What good looks like:** you have a sheet that does its own math, and you know the two ways it can lie to you: a range that stops too soon, and a category spelled two ways. Neither is a flaw in you or in Sheets. They are things every spreadsheet user learns once. Keep this sheet. The next lesson builds on it.

When you have done the tasks, press the practice button below. It saves that you finished and opens the next lesson. Passing the quiz with 2 of 3 right opens it too.

<div id="practice-done"></div>

## Further reading

These are optional. They go to Google's own help pages, which were not read for this lesson. Read what they say today, since menus and wording change.

- Google Docs Editors Help, which covers Sheets: [https://support.google.com/docs](https://support.google.com/docs)

A three-question quiz follows. Get 2 of 3 right, or press the practice button above, and the next lesson opens.

<div id="quiz"></div>
