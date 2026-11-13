// Lesson unlocking. Soft lock for a family site: it hides locked pages in the browser, it is not security.
// State comes from GET /unlock-state (quiz passed or practice marked done). If that call fails, nothing is locked.
(function () {
  function keyOf(path) {
    var m = /(module-\d+(?:\/lesson-\d+)?)\/?$/.exec(String(path).replace(/index\.html$/, ""));
    return m ? m[1] : null;
  }

  // Returns null when open, or {msg, link, linkText} when locked.
  function lockReason(course, doneList, key) {
    var done = {};
    doneList.forEach(function (k) { done[k] = true; });
    var mi = -1, i;
    var modId = key.split("/")[0];
    for (i = 0; i < course.modules.length; i++) if (course.modules[i].id === modId) mi = i;
    if (mi < 0) return null;
    var mod = course.modules[mi];
    var reqs = mod.requires || (mi > 0 ? [mi - 1] : []);
    for (var r = 0; r < reqs.length; r++) {
      var need = course.modules[reqs[r]];
      if (need.lessons.length === 0) {
        return { msg: "This opens after you finish " + need.title + ", and that module is not written yet." };
      }
      for (var l = 0; l < need.lessons.length; l++) {
        if (!done[need.lessons[l].key]) {
          return { msg: "This opens after you finish " + need.title + ".", link: "/" + need.lessons[l].key + "/", linkText: "Go to: " + need.lessons[l].title };
        }
      }
    }
    if (key.indexOf("/") > 0) {
      for (var j = 0; j < mod.lessons.length; j++) {
        if (mod.lessons[j].key === key) break;
        if (!done[mod.lessons[j].key]) {
          return { msg: "This opens after you finish the lesson before it.", link: "/" + mod.lessons[j].key + "/", linkText: "Go to: " + mod.lessons[j].title };
        }
      }
    }
    return null;
  }

  // What to offer after a lesson is finished: next lesson in the module, else the next module page.
  function nextTarget(course, key) {
    for (var i = 0; i < course.modules.length; i++) {
      var m = course.modules[i];
      for (var j = 0; j < m.lessons.length; j++) {
        if (m.lessons[j].key === key) {
          if (j + 1 < m.lessons.length) return { link: "/" + m.lessons[j + 1].key + "/", text: m.lessons[j + 1].title };
          if (i + 1 < course.modules.length) return { link: "/" + course.modules[i + 1].id + "/", text: course.modules[i + 1].title };
        }
      }
    }
    return null;
  }

  var api = { keyOf: keyOf, lockReason: lockReason, nextTarget: nextTarget };
  if (typeof module !== "undefined" && module.exports) { module.exports = api; return; }
  window.TeacherUnlock = api;

  var course = window.TEACHER_COURSE;
  if (!course || !window.fetch) return;
  fetch("/unlock-state", { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (st) {
    if (!st || st.unlock_enabled === false) return;
    window.TeacherUnlock.state = st;
    // Mark locked links in the side menu.
    var links = document.querySelectorAll(".md-nav__link[href]");
    Array.prototype.forEach.call(links, function (a) {
      var k = keyOf(a.pathname);
      if (k && lockReason(course, st.completed, k)) {
        a.classList.add("tc-locked");
        if (a.textContent.indexOf("(locked)") < 0) a.appendChild(document.createTextNode(" (locked)"));
      }
    });
    // Replace the page if it is locked.
    var here = keyOf(location.pathname);
    var why = here && lockReason(course, st.completed, here);
    if (!why) return;
    var box = document.querySelector(".md-content__inner");
    if (!box) return;
    var html = '<div id="tc-lock"><h1>Not open yet</h1><p>' + why.msg + "</p>";
    if (why.link) html += '<p><a class="md-button md-button--primary" href="' + why.link + '">' + why.linkText + "</a></p>";
    html += '<p><a href="/">Back to the course home</a></p></div>';
    box.innerHTML = html;
  }).catch(function () {});
})();
