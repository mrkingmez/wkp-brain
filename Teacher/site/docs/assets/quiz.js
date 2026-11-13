// Plain-JS quiz. Reads window.TEACHER_QUIZZES[lessonKey], renders into <div id="quiz">,
// then POSTs {lesson, score, total, passed} to /progress on the same server.
(function () {
  var host = document.getElementById("quiz");
  if (!host) return;
  var key = host.getAttribute("data-lesson") || (location.pathname.replace(/^\/|\/$/g, "").split("/").slice(-2).join("/"));
  var quiz = (window.TEACHER_QUIZZES || {})[key];
  if (!quiz) { host.textContent = "No quiz for this page."; return; }

  var html = "<h2>Check yourself</h2>";
  quiz.questions.forEach(function (q, i) {
    html += '<div class="q" data-i="' + i + '"><p>' + (i + 1) + ". " + q.text + "</p>";
    q.choices.forEach(function (c, j) {
      html += '<label><input type="radio" name="q' + i + '" value="' + j + '"> ' + c + "</label>";
    });
    html += '<div class="fb"></div></div>';
  });
  html += '<button type="button" id="quiz-check">Check my answers</button><div class="result" id="quiz-result"></div>';
  host.innerHTML = html;

  document.getElementById("quiz-check").addEventListener("click", function () {
    var score = 0, answered = 0;
    quiz.questions.forEach(function (q, i) {
      var box = host.querySelector('.q[data-i="' + i + '"]');
      var fb = box.querySelector(".fb");
      var pick = host.querySelector('input[name="q' + i + '"]:checked');
      if (!pick) { fb.className = "fb"; fb.textContent = "Pick an answer."; return; }
      answered++;
      var right = Number(pick.value) === q.answer;
      if (right) score++;
      fb.className = "fb " + (right ? "ok" : "no");
      fb.textContent = (right ? "Right. " : "Not quite. ") + q.explain;
    });
    var out = document.getElementById("quiz-result");
    if (answered < quiz.questions.length) { out.textContent = "Answer all " + quiz.questions.length + " questions first."; return; }
    var total = quiz.questions.length;
    var passed = score >= (quiz.pass || total);
    out.textContent = "You got " + score + " of " + total + (passed ? ". Lesson complete." : ". Read the lesson again and retry.");
    try {
      fetch("/progress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ lesson: key, score: score, total: total, passed: passed })
      }).then(function () {
        var u = window.TeacherUnlock, c = window.TEACHER_COURSE;
        var nx = passed && u && c && u.nextTarget(c, key);
        if (nx) out.innerHTML += ' Next: <a href="' + nx.link + '">' + nx.text + "</a>";
      }).catch(function () {});
    } catch (e) {}
  });
})();
