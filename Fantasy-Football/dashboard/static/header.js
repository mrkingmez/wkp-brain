// Read-only header line. Reads generated_at from the same /state.json the page already uses.
// Writes only to #hdr-week and #gen-line. Red when the data is more than a day old.
(function () {
  const DAY_MS = 24 * 3600 * 1000;
  let generated = null;
  function ago(ms) {
    const m = Math.round(ms / 60000);
    if (m < 1) return "under a minute ago";
    if (m < 60) return m + " min ago";
    const h = Math.floor(m / 60);
    if (h < 24) return h + " h " + (m % 60) + " min ago";
    return Math.floor(h / 24) + " d " + (h % 24) + " h ago";
  }
  function paint() {
    const el = document.getElementById("gen-line");
    if (!el) return;
    if (!generated) { el.textContent = "Data updated at unknown"; el.className = "gen-line stale"; return; }
    const age = Date.now() - generated.getTime();
    const when = generated.toLocaleString([], { weekday: "short", hour: "numeric", minute: "2-digit" });
    el.textContent = "Data updated at " + when + " (" + ago(age) + ")";
    el.className = "gen-line" + (age > DAY_MS ? " stale" : "");
  }
  async function load() {
    try {
      const s = await (await fetch("/state.json", { cache: "no-store" })).json();
      generated = s.generated_at ? new Date(s.generated_at) : null;
      if (generated && isNaN(generated)) generated = null;
      const w = document.getElementById("hdr-week");
      if (w && s.week != null) w.textContent = "Week " + s.week + (s.games_live ? ", games live" : ", no games live, polling paused");
    } catch (e) { generated = null; }
    paint();
  }
  load();
  setInterval(load, 30000);
  setInterval(paint, 30000);
})();
