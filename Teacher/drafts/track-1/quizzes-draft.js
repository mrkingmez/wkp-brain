// Draft quiz entries for Track 1 lessons 1 to 3. Merge into site\docs\assets\quizzes.js.
// Keys are working keys, software-director sets the final ones to match the new nav.
window.TEACHER_QUIZZES_TRACK1_DRAFT = {
  "start-here/what-ai-is": {
    pass: 2,
    questions: [
      {
        text: "What is the main difference between a search engine and an AI chat tool?",
        choices: ["A search engine finds pages that already exist. An AI chat tool writes a new answer that sounds right.", "They are the same thing with different names.", "An AI chat tool only shows a list of links."],
        answer: 0,
        explain: "A search engine hands you something that exists. An AI writes something that sounds right, and sometimes it is smooth and wrong."
      },
      {
        text: "Which of these jobs is a good fit for an AI chat tool?",
        choices: ["Learning what time a store closes today, with no check", "Rewriting a stiff email so it sounds friendly", "Finding the exact phone number of a business, with no check"],
        answer: 1,
        explain: "Writing, rewriting, explaining, brainstorming and sorting are strengths. Live, local facts should come from a search engine or the business itself."
      },
      {
        text: "Which kinds of details should you check somewhere else before you rely on them?",
        choices: ["The greeting at the start of the answer", "The number of paragraphs", "Names, dates, numbers and quotes"],
        answer: 2,
        explain: "Check facts, especially names, dates, numbers and quotes, and anything about health, law or money."
      }
    ]
  },
  "start-here/meet-claude": {
    pass: 2,
    questions: [
      {
        text: "Who makes Claude?",
        choices: ["OpenAI", "Anthropic", "Google"],
        answer: 1,
        explain: "Claude is made by Anthropic. ChatGPT is made by OpenAI."
      },
      {
        text: "In a plain chat, what does Claude work with?",
        choices: ["Everything on your computer", "Everything in your email, automatically", "Only what you type or attach in the chat"],
        answer: 2,
        explain: "It cannot see anything you do not give it, so treat any file you upload as shared."
      },
      {
        text: "Where should you go to learn what the free plan includes today?",
        choices: ["The company's own pricing and help pages, with the date you looked", "Whatever a friend remembers", "The lesson text, because it never changes"],
        answer: 0,
        explain: "Free-plan rules are set by the company and change. Read the company's own page, write the date, and write 'not stated' where it is silent."
      }
    ]
  },
  "start-here/first-good-prompt": {
    pass: 2,
    questions: [
      {
        text: "Which is the best description of a prompt?",
        choices: ["A setting you turn on in your account", "The message you type to the AI", "A special code only experts can write"],
        answer: 1,
        explain: "A prompt is just your message. A thin message gets a bland answer."
      },
      {
        text: "Which set names the four parts of a clear prompt?",
        choices: ["The job, the details, the reader, and the shape", "The title, the date, the length, and the font", "The question, the answer, the proof, and the source"],
        answer: 0,
        explain: "Say the job, give the details, name the reader and tone, and say the shape you want the answer in."
      },
      {
        text: "The reply is close but too long. What do you do?",
        choices: ["Close the browser and give up", "Retype your whole first message with no changes", "Send a follow-up in the same chat, such as 'Shorter, please.'"],
        answer: 2,
        explain: "You can keep talking. Each follow-up builds on the last reply, and you steer a little at a time."
      }
    ]
  }
};
