// The course map. Edit this when a lesson is added. Order here is the unlock order.
// Unlocking is OFF (unlock_enabled false in config.json), so tracks can be taken in any order.
// If it is ever turned back on, a track with no lessons cannot be finished, so nothing requires another track.
window.TEACHER_COURSE = {
  modules: [
    { id: "start-here", title: "Start Here", lessons: [], requires: [] },
    { id: "make-things", title: "Make Things", lessons: [], requires: [] },
    { id: "build-automate", title: "Build and Automate", lessons: [], requires: [] },
    { id: "stay-safe", title: "Stay Safe", lessons: [
      { key: "stay-safe/check-what-ai-tells-you", title: "How to check what AI tells you" } ], requires: [] }
  ]
};
