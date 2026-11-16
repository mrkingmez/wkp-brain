// Draft quiz entries for Track 1 lessons 4 to 9 (lessons 1 to 3 are in quizzes-draft.js). Merge into site\docs\assets\quizzes.js.
// Keys are working keys, software-director sets the final ones to match the nav.
window.TEACHER_QUIZZES_TRACK1_DRAFT_B = {
  "start-here/role-and-context": {
    pass: 2,
    questions: [
      {
        text: "What does telling the AI 'You are a patient school secretary' change?",
        choices: ["It makes the AI know the school's real rules", "It makes every fact in the answer true", "The voice and viewpoint of the writing"],
        answer: 2,
        explain: "A role changes the voice. It does not add knowledge and it does not make an answer true."
      },
      {
        text: "Which set matches the short reminder 'who is writing, who is reading, and what is going on'?",
        choices: ["Role, audience, and context", "Title, date, and length", "Question, answer, and proof"],
        answer: 0,
        explain: "The role is who is writing, the audience is who reads it, and the context is the background the AI cannot see."
      },
      {
        text: "The AI adds a detail you never gave it, such as a doctor's name, in your note. What should you do?",
        choices: ["Leave it, because the AI is probably right", "Delete it, because the AI guessed", "Send it, since the reader will not notice"],
        answer: 1,
        explain: "Anything you did not provide is a guess. Read before you send and cut what you did not give."
      }
    ]
  },
  "start-here/show-examples": {
    pass: 2,
    questions: [
      {
        text: "Why does showing a sample often work better than describing the format in words?",
        choices: ["A sample is shorter, so the AI works faster", "A sample carries small choices you would never think to write down", "A sample makes the AI skip checking facts"],
        answer: 1,
        explain: "A sample shows length, order, tone and many small choices at once."
      },
      {
        text: "Your two examples both start with the same sentence, and every answer now starts that way. What is the best fix?",
        choices: ["Add more examples that all start the same way", "Delete the examples and describe the format in words", "Make the examples differ in small details, and say not to reuse phrases"],
        answer: 2,
        explain: "If the examples differ, the AI learns the pattern and not the phrase. You can also tell it not to reuse phrases."
      },
      {
        text: "How should you set up a prompt that has examples?",
        choices: ["Label them Example 1 and Example 2, then put the new job last", "Mix the examples into the new job with no labels", "Put the new job first and hide the examples at the bottom"],
        answer: 0,
        explain: "Labels keep a sample from being mixed up with the job. Examples first, new job last."
      }
    ]
  },
  "start-here/show-its-work": {
    pass: 2,
    questions: [
      {
        text: "You ask the AI to work step by step and the steps read smoothly. What does that prove?",
        choices: ["The answer is correct", "Nothing yet, it only makes mistakes easier for you to find", "The AI checked its own work with a calculator"],
        answer: 1,
        explain: "Showing work gives you something to check. It does not make a mistake less likely to be there."
      },
      {
        text: "The AI names a book as a source. What is the safe way to treat it?",
        choices: ["As proof, because it gave a title and an author", "As proof if it sounds well known", "As a lead to look up, and not rely on it if you cannot find it"],
        answer: 2,
        explain: "An AI can write a source that looks real and is not. Look it up before you rely on it."
      },
      {
        text: "Which prompt helps you check a long answer one piece at a time?",
        choices: ["List every separate factual claim, one per line, and mark each as sure or guessing", "Make the answer longer", "Say it again in a friendlier tone"],
        answer: 0,
        explain: "A list of separate claims is easy to check one at a time, and the marks show where to look first."
      }
    ]
  },
  "start-here/long-tasks": {
    pass: 2,
    questions: [
      {
        text: "What is a good way to work on a long document?",
        choices: ["Ask for everything in one huge message", "Give the material, ask for a small first step, check it, then build on it", "Paste only the last page"],
        answer: 1,
        explain: "Small steps are easy to check, and a mistake in step two gets caught before it spreads."
      },
      {
        text: "Where should you go to learn whether your free plan accepts file attachments and how large they can be?",
        choices: ["Ask a friend, because it never changes", "Guess from a different app", "The company's own pricing and help pages, noting the date you looked"],
        answer: 2,
        explain: "File and chat limits depend on the plan and change. The company's own pages are the ones to trust."
      },
      {
        text: "You want to continue a job tomorrow in a new chat. What works on any tool without a memory feature?",
        choices: ["A handoff note you read, fix, and paste into the new chat", "Hoping the new chat remembers", "Starting over from nothing"],
        answer: 0,
        explain: "A handoff note carries the job across chats. A new chat starts empty by default."
      }
    ]
  },
  "start-here/prompt-library": {
    pass: 2,
    questions: [
      {
        text: "In a saved prompt, what should become a [blank in square brackets]?",
        choices: ["The role, tone and rules you always want", "The parts that change each time", "Your passwords, so you do not forget them"],
        answer: 1,
        explain: "The parts that stay are the real work. The parts that change become blanks."
      },
      {
        text: "Which of these should stay out of your prompt library?",
        choices: ["A role you like", "A note on what to check", "Passwords and other people's private details"],
        answer: 2,
        explain: "Use brackets and fill in details fresh each time. Do not save secrets in the library."
      },
      {
        text: "You changed a prompt to make it work better. What is the best next step?",
        choices: ["Put the fix back into the saved entry and update the test date", "Keep the fix in your head", "Delete the old entry and the new one"],
        answer: 0,
        explain: "A one-minute fix saved into the entry pays off every time you use it again."
      }
    ]
  },
  "start-here/chains-and-checking": {
    pass: 2,
    questions: [
      {
        text: "What is a chain?",
        choices: ["One very long prompt", "A planned set of small prompts, each feeding the next, with a checkpoint between them", "A tool that checks facts for you"],
        answer: 1,
        explain: "Each step gets one clear job, and you look at the result before the next step."
      },
      {
        text: "Which review is stronger?",
        choices: ["Asking the same chat 'is this good?'", "Asking the AI to be more sure", "Reviewing in a new chat or the other tool, with a specific job such as 'check every ingredient in the plan appears in the list'"],
        answer: 2,
        explain: "A fresh read and a specific job catch more. Two tools disagreeing is a signal to look closer."
      },
      {
        text: "An AI review says your result is fine. Does that prove it is right?",
        choices: ["No, a reviewer can share the same blind spots, so the final check on anything that matters is yours", "Yes, a second pass always proves it", "Yes, if the review sounded confident"],
        answer: 0,
        explain: "A review is a second pair of eyes, not proof. Check against a real source when it matters."
      }
    ]
  }
};
