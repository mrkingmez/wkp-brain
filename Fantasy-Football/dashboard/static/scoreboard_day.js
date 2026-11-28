// Day scoreboard (2026-11-22): reads /api/scoreboard/day (file kept by the poller). No outside calls.
async function sdLoad() {
  const g = document.getElementById("day-games"), f = document.getElementById("day-dfs");
  try {
    const d = await (await fetch("/api/scoreboard/day", { cache: "no-store" })).json();
    document.getElementById("day-h").textContent = d.date ? `Scores for ${d.date} (kept until the next game day)` : "Today's scores";
    g.innerHTML = "";
    (d.games || []).forEach(x => {
      const row = document.createElement("div");
      row.className = "scoreboard-row" + (x.on_card ? " on-card" : "");
      const t = (s) => { const e = document.createElement("span"); e.textContent = s; return e; };
      const when = x.state === "pre" ? new Date(x.kickoff).toLocaleTimeString([], { hour: "numeric", minute: "2-digit" })
        : x.state === "post" ? "Final" : x.detail;
      row.append(t("NFL"), t(`${x.away_team} ${x.away_score ?? "-"} @ ${x.home_team} ${x.home_score ?? "-"}`), t(when));
      g.appendChild(row);
    });
    if (!(d.games || []).length) g.textContent = "No game day recorded yet.";
    const q = d.dfs;
    if (q && q.entries) {
      const es = Object.values(q.entries).sort((a, b) => (b.total || 0) - (a.total || 0));
      f.textContent = `DFS day result: best lineup ${Number(q.best_total).toFixed(2)} (entry ${q.best_entry}). ` +
        es.map(e => `${e.entry_id} ${Number(e.total).toFixed(2)}${e.all_final ? " final" : ""}${e.dk_rank ? " (place " + e.dk_rank + " of " + e.dk_total + ")" : ""}`).join("; ");
    } else f.textContent = "";
  } catch (err) { g.textContent = "Day scoreboard not available: " + err; }
}
sdLoad(); setInterval(sdLoad, 30000);
