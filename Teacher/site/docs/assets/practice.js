// Renders the "I did the practice" button into <div id="practice-done"></div> and records it
// through the same /progress endpoint the quiz uses.
(function () {
  var host = document.getElementById("practice-done");
  if (!host) return;
  var key = host.getAttribute("data-lesson") || (location.pathname.replace(/^\/|\/$/g, "").split("/").slice(-2).join("/"));
  host.innerHTML = '<button type="button" id="practice-btn">I did the practice</button><div class="result" id="practice-result"></div>';
  document.getElementById("practice-btn").addEventListener("click", function () {
    var out = document.getElementById("practice-result");
    fetch("/progress", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ lesson: key, kind: "practice", score: 0, total: 0, passed: true })
    }).then(function (r) {
      if (!r.ok) throw new Error("bad");
      out.textContent = "Saved. Practice marked done.";
      var u = window.TeacherUnlock, c = window.TEACHER_COURSE;
      var nx = u && c && u.nextTarget(c, key);
      if (nx) out.innerHTML = 'Saved. Practice marked done. Next: <a href="' + nx.link + '">' + nx.text + "</a>";
    }).catch(function () { out.textContent = "Could not save. Is the course server running?"; });
  });
})();
