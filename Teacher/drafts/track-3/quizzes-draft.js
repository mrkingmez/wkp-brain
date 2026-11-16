// Draft quiz entries for Track 3 lessons 3.1, 3.2, 3.3 and 3.5. Merge into site\docs\assets\quizzes.js.
// Keys are working keys, software-director sets the final ones to match the nav.
window.TEACHER_QUIZZES_TRACK3_DRAFT = {
  "build-automate/automate-with-a-spreadsheet": {
    pass: 2,
    questions: [
      {
        text: "What does =SUM(D2:D100) do?",
        choices: ["Subtracts D2 from D100", "Adds every number in column D from row 2 down to row 100", "Counts the words in column D"],
        answer: 1,
        explain: "A formula starts with an equals sign. SUM adds, and D2:D100 is the range, from D2 down to D100."
      },
      {
        text: "Why make the range go to row 100 when you only have eight rows of data?",
        choices: ["So a row you add later is still counted", "So the sheet runs faster", "Because Sheets will not accept a shorter range"],
        answer: 0,
        explain: "A range that stops too soon quietly ignores new rows. Empty cells add nothing, so a longer range costs you nothing."
      },
      {
        text: "Your Groceries total ignores a row you typed with the category Grocery. Why?",
        choices: ["Sheets cannot add small numbers", "The total formula needs to be restarted", "The spelling does not match Groceries exactly, so the row is not counted"],
        answer: 2,
        explain: "SUMIF matches the category word exactly. A different spelling, or a trailing space, means no match."
      }
    ]
  },
  "build-automate/ask-claude-for-a-formula": {
    pass: 2,
    questions: [
      {
        text: "What should you tell Claude so the formula fits your sheet?",
        choices: ["Your password to the sheet", "What is in each column by letter, which rows hold data, and the answer you want", "Only the name of the sheet"],
        answer: 1,
        explain: "Claude cannot see your sheet. Naming columns by letter and giving the row range removes the guessing."
      },
      {
        text: "Claude gives you a formula and the sheet shows a number with no error. What next?",
        choices: ["Trust it, because there is no error", "Ask Claude if it is sure", "Compare it to an answer you worked out by hand on a small piece of data"],
        answer: 2,
        explain: "A formula can run without an error and still be wrong. The hand-worked answer is your test."
      },
      {
        text: "A formula shows an error. What is the best message to send Claude?",
        choices: ["The exact formula, the exact error text, and what you expected", "It broke, please fix it", "Describe the whole sheet again without the formula"],
        answer: 0,
        explain: "The more exact you are, the better the fix. Claude needs the formula, the error and your goal."
      }
    ]
  },
  "build-automate/forms-to-sheets": {
    pass: 2,
    questions: [
      {
        text: "Where does each submitted Google Form answer go when the form is linked to a sheet?",
        choices: ["It is emailed to everyone who filled it in", "It becomes a new row in the linked sheet", "It is deleted after you look at it"],
        answer: 1,
        explain: "Each response is one row, and each question is one column."
      },
      {
        text: "Which question type makes answers easiest to count?",
        choices: ["Short answer", "A long paragraph box", "Multiple choice or dropdown"],
        answer: 2,
        explain: "Everyone picks from the same words, so the counts do not split into wordings like Tacos, Taco night and tacos please."
      },
      {
        text: "What should you do before sharing a form link with anyone?",
        choices: ["Fill it in yourself, see the answer land in the sheet, and check who is allowed to open it", "Send it right away to see what happens", "Add questions asking for addresses so you have them"],
        answer: 0,
        explain: "Test it yourself, ask only for what you need, and check Google's help pages for who can open and fill in a form."
      }
    ]
  },
  "build-automate/your-first-web-page": {
    pass: 2,
    questions: [
      {
        text: "What is a web page file made of?",
        choices: ["Plain text with HTML tags that label the parts", "A photograph of the page", "A word processor document with hidden formatting"],
        answer: 0,
        explain: "Your browser reads a text file and draws it. HTML labels what is a heading, a paragraph or a list."
      },
      {
        text: "What should the file be called so your browser treats it as a web page?",
        choices: ["index.html.txt", "index.html", "index"],
        answer: 1,
        explain: "The ending .html matters. A plain text editor and the right name keep the file from becoming index.html.txt."
      },
      {
        text: "Claude gives you page code. What should you do before you save and open it?",
        choices: ["Nothing, Claude is always right", "Open it first and read it afterward", "Read it, and look for script lines or web addresses you did not ask for"],
        answer: 2,
        explain: "Ask for plain HTML and CSS only. Read the code, and ask Claude about any line you do not understand."
      }
    ]
  }
};
