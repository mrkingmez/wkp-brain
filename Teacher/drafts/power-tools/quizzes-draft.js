// Draft quiz entries for the Claude power tools lessons. Merge into site\docs\assets\quizzes.js.
// Keys are working keys, software-director sets the final ones to match the nav.
window.TEACHER_QUIZZES_POWERTOOLS_DRAFT = {
  "stay-safe/tools-that-act": {
    pass: 2,
    questions: [
      {
        text: "What is prompt injection, in plain words?",
        choices: [
          "A setting that hides your chats from other people on the same computer.",
          "Hidden text in a page, email or file that tries to give the AI orders.",
          "A trick that makes the AI answer faster by skipping its safety checks."
        ],
        answer: 1,
        explain: "The text was written by someone else, but the AI sees it as more words in front of it."
      },
      {
        text: "Claude asks to take an action you never requested, right after reading a web page. What should you do?",
        choices: [
          "Click Allow always so it stops asking, since you want the task finished.",
          "Approve it once, because Claude is usually right about what the job needs.",
          "Read the request and refuse it, since you did not ask for that."
        ],
        answer: 2,
        explain: "An unexpected request is the clearest warning sign. Approve each action, and say no to the ones you did not ask for."
      },
      {
        text: "Which choice follows the 'least access' habit?",
        choices: [
          "Connect only the calendar, read-only if the connector offers it.",
          "Connect your whole mailbox now in case you need something from it later.",
          "Connect every app at once and switch things off if there is any trouble."
        ],
        answer: 0,
        explain: "Give the smallest slice that does the job. Less access means less that can go wrong."
      }
    ]
  },
  "power-tools/projects-and-memory": {
    pass: 2,
    questions: [
      {
        text: "In a Claude Project, which is the better home for the note 'Keep answers short and use plain words'?",
        choices: [
          "The project instructions, because it tells Claude how to act.",
          "A project file, because it is a fact that Claude needs to look up.",
          "Neither one, because it has to be retyped at the start of every chat."
        ],
        answer: 0,
        explain: "Instructions are how to act. Files are what to know."
      },
      {
        text: "Why does a brand-new chat not remember what you taught Claude last week?",
        choices: [
          "Claude clears each chat after a day, so nothing can be kept between chats.",
          "Free accounts are not allowed to remember anything between separate chats.",
          "Each chat starts clean unless a project or memory holds the background."
        ],
        answer: 2,
        explain: "Context does not carry between chats unless something carries it, such as project knowledge or memory."
      },
      {
        text: "You are practicing with a new project. What should go into it?",
        choices: [
          "Your real bank numbers, so the practice feels as close to real as possible.",
          "Made-up or trimmed material, with no passwords and no private details.",
          "A scan of every paper in the house, so Claude has the full picture."
        ],
        answer: 1,
        explain: "A project is a drawer you keep stocking. Practice with made-up material and keep private details out."
      }
    ]
  },
  "power-tools/skills-reusable-instructions": {
    pass: 2,
    questions: [
      {
        text: "How is a Skill different from a prompt you type?",
        choices: [
          "A Skill only works on pictures, while a prompt only works on text.",
          "A Skill is saved instructions that Claude loads when they fit the job.",
          "A Skill is the same thing as a prompt, only with a longer and fancier name."
        ],
        answer: 1,
        explain: "A prompt lasts for one conversation. A Skill is reusable and loaded when relevant."
      },
      {
        text: "A stranger online shares a Skill file and says it will change your life. What is the safe move?",
        choices: [
          "Skip it, because Anthropic says to install Skills only from sources you trust.",
          "Install it if it has plenty of comments, since many people must have checked it.",
          "Install it right away, because a Skill is only text and cannot cause trouble."
        ],
        answer: 0,
        explain: "A Skill can carry scripts and instructions. Anthropic compares installing one to installing software."
      },
      {
        text: "Your uploaded Skill never seems to switch on. What is the first thing to check?",
        choices: [
          "The file size, because a larger Skill is always switched on more often.",
          "The folder name, because Claude picks a Skill by how its folder is named.",
          "The description, so it says what the Skill does and when to use it."
        ],
        answer: 2,
        explain: "Claude reads the description to decide when to use a Skill, so a clearer description is the first fix."
      }
    ]
  },
  "power-tools/connectors-and-mcp": {
    pass: 2,
    questions: [
      {
        text: "What does connecting a connector let Claude do?",
        choices: [
          "Copy everything in your account to Anthropic's own storage for good.",
          "Run a program on your Mac that changes your settings without asking.",
          "Reach one of your apps, read your data there and act in it."
        ],
        answer: 2,
        explain: "A connector is a key to one drawer. Claude inherits your permissions in that app, so it reaches what you can already reach."
      },
      {
        text: "You find a custom connector on a stranger's web page. What fits the course rules?",
        choices: [
          "Skip it unless it is from a source you trust, and ask Zac first.",
          "Add it, since Anthropic checks every custom connector before it works.",
          "Add it with Allow always on, so you are not asked about every action."
        ],
        answer: 0,
        explain: "Anthropic says custom connectors are not verified by Anthropic. Trusted source only, and Zac gets asked first."
      },
      {
        text: "You connected a calendar for practice. Which first question follows the read-only habit?",
        choices: [
          "Please tidy my calendar by moving or deleting anything that looks old.",
          "What made-up events are on my test calendar on Friday?",
          "Send my test events to the club members so they can see the dates."
        ],
        answer: 1,
        explain: "A look changes nothing. Moving, deleting or sending are changes, and they are off limits in practice."
      }
    ]
  }
};
