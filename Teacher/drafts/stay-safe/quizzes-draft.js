// Draft quiz entries for Stay Safe lessons: privacy and when not to use AI. Merge into site\docs\assets\quizzes.js.
// Keys are working keys, software-director sets the final ones to match the nav.
window.TEACHER_QUIZZES_STAYSAFE_DRAFT = {
  "stay-safe/privacy": {
    pass: 2,
    questions: [
      {
        text: "You want help replying to an email about a late order. What does the AI need?",
        choices: ["The whole email, signature included, so it has the full picture", "Your name and the order number, so the reply sounds personal", "The situation: an order is late and you want a polite reply"],
        answer: 2,
        explain: "It needs the situation, not the identity. Use placeholders for names and numbers and fill them back in yourself."
      },
      {
        text: "You covered a name on a screenshot with a light highlighter. What should you do before you share it?",
        choices: ["Zoom in and check whether the letters still read through, and use a solid box if they do", "Nothing, any mark over the name hides it", "Make the picture smaller so the name is harder to read"],
        answer: 0,
        explain: "A thin marker or a light highlight can leave letters readable. Cover it with a solid box, or crop it out, then zoom in and check."
      },
      {
        text: "You swapped real names for [Person A] and [Person B]. Where should the key that says who they are live?",
        choices: ["In the same chat, so the AI can fill the names back in", "On paper or in your own document, never in the chat", "In a second chat with the same AI"],
        answer: 1,
        explain: "The AI never needs the key. Keep it yourself and swap the names back with Find and replace."
      }
    ]
  },
  "stay-safe/when-not-to-use": {
    pass: 2,
    questions: [
      {
        text: "An AI tells you, very confidently, that it is fine to stop a medicine early. What does that confidence tell you?",
        choices: ["That it found the answer in a medical source", "Nothing about whether it is right, so a doctor or pharmacist decides", "That you can skip asking anyone if the answer is detailed enough"],
        answer: 1,
        explain: "Sureness is not information. It sounds the same when it is right and when it is wrong. Health calls belong to the person with the license."
      },
      {
        text: "Which set is the three-question gate from this lesson?",
        choices: ["Is it fast? Is it free? Is it easy?", "Did it cite a source? Is it detailed? Did it sound sure?", "Can I check this? What happens if it is wrong? Is this mine to decide, or someone else's?"],
        answer: 2,
        explain: "If all three answers come easy, the AI can do the job. If any one gives you pause, the AI helps you prepare and a person decides."
      },
      {
        text: "You used AI as a second opinion on two repair quotes. What is the last step?",
        choices: ["Write your decision in one sentence yourself and name who confirms it", "Ask the AI which quote to pick and go with it", "Ask a second AI and pick the answer they agree on"],
        answer: 0,
        explain: "The AI gives you questions, trade-offs and the case against. You write the decision, and you name the person who confirms it."
      }
    ]
  }
};
