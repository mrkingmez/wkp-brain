// Live DFS points panel (2026-11-22). Reads only /api/dfs/live (file written by poller.py). No outside calls.
const dlEsc = (v) => String(v == null ? "" : v).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const dlN = (v, d = 1) => (v == null ? "" : Number(v).toFixed(d));
async function dlLoad() {
  const box = document.getElementById("dfslive-entries");
  try {
    const d = await (await fetch("/api/dfs/live", { cache: "no-store" })).json();
    if (d.error) { box.textContent = d.error; return; }
    const age = Math.round((Date.now() - Date.parse(d.generated_at)) / 60000);
    document.getElementById("dfslive-meta").textContent = `Week ${d.week}, entries file ${d.entries_file || "?"}, updated ${age} min ago, games live: ${d.games_live ? "yes" : "no"}. ` +
      (d.games || []).map((g) => `${g.teams} ${g.state === "pre" ? "not started" : g.state === "in" ? "LIVE " + g.detail : "final"}`).join("; ");
    box.innerHTML = (d.entries || []).map((e, i) => {
      const dk = e.dk_points != null ? ` &middot; DK official <b>${dlN(e.dk_points, 2)}</b>${e.dk_rank ? " (place " + e.dk_rank + " of " + e.dk_total + ")" : ""}` +
        ` &middot; diff ${e.diff > 0 ? "+" : ""}${dlN(e.diff, 2)}` : "";
      const st = e.all_final ? "all final" : `${e.live_count} live, ${e.not_started} not started`;
      return `<article class="dfsw-card"><header><span class="dfsw-n">${i === 0 ? "Best " : ""}#${i + 1}</span> <span class="path">${dlEsc(e.entry_id)}</span></header>` +
        `<div class="dfsw-result"><b>${dlN(e.total, 2)} pts</b> &middot; ${st}${e.all_final ? "" : ` &middot; projected remaining about ${dlN(e.proj_remaining)}`}${dk}</div>` +
        `<table class="dfsw-pl"><thead><tr><th>Slot</th><th>Player</th><th>Team</th><th class="num">Pts</th><th>Game</th></tr></thead><tbody>` +
        e.players.map((p) => `<tr><td>${dlEsc(p.slot)}</td><td>${dlEsc(p.name)}</td><td>${dlEsc(p.team)}</td><td class="num">${p.pts == null ? "?" : dlN(p.pts, 2)}</td>` +
          `<td>${dlEsc(p.game_state)}${p.flag && p.flag !== "not started" ? " (" + dlEsc(p.flag) + ")" : ""}</td></tr>`).join("") + "</tbody></table></article>";
    }).join("") || "No built entries in this week's file.";
    document.getElementById("dfslive-notes").innerHTML = (d.notes || []).map((n) => `<div class="note">${dlEsc(n)}</div>`).join("");
  } catch (err) { box.textContent = "Live DFS not available: " + err; }
}
dlLoad(); setInterval(dlLoad, 30000);
