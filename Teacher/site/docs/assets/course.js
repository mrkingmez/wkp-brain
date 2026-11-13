// The course map. Edit this when a lesson is added. Order here is the unlock order.
// A module with no lessons is "not written yet" and cannot be finished, so what comes after it stays locked.
window.TEACHER_COURSE = {
  modules: [
    { id: "module-1", title: "Module 1: Is it right?", lessons: [
      { key: "module-1/lesson-1", title: "How to check what AI tells you" } ] },
    { id: "module-2", title: "Module 2: Privacy", lessons: [] },
    { id: "module-3", title: "Module 3: Scams and fakes", lessons: [] },
    { id: "module-4", title: "Module 4: When not to use AI", lessons: [] },
    { id: "module-5", title: "Module 5: Advanced track", lessons: [], requires: [0, 1, 2, 3] }
  ]
};
