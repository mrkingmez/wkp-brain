// DFS week view (2026-11-19). Reads only this localhost server: /api/dfs/weeks, /api/dfs/week?n=N,
// and POST /api/dfs/manual for typed points and place. Nothing here contacts DraftKings.
let dfswWeek = null;
let dfswData = null;
const dfswEsc = (v) => String(v == null ? "" : v).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const dfswNum = (v, d = 2) => (v == null || v === "" ? "" : Number(v).toFixed(d).replace(/\.0+$/, "").replace(/(\.\d*?)0+$/, "$1"));

async function dfswLoadWeeks() {
  const w = await (await fetch("/api/dfs/weeks", { cache: "no-store" })).json();
  document.getElementById("dfsw-root").textContent = w.root;
  if (dfswWeek == null) dfswWeek = w.default;
  const sel = document.getElementById("dfsw-week");
  sel.innerHTML = (w.weeks || []).map((n) =>
    `<option value="${n}" ${n === dfswWeek ? "selected" : ""}>Week ${n}${n === w.state_week ? " (this week)" : n !== w.weeks[0] ? " (archive)" : ""}</option>`).join("")
    || '<option value="">No Week N folders found</option>';
}

function dfswResultBlock(e) {
  const r = e.result, m = e.manual;
  if (r) {
    const top = r.top_pct != null ? `top ${dfswNum(r.top_pct, 1)}%` : "";
    return `<div class="dfsw-result"><b>${dfswNum(r.points)} pts</b> &middot; place ${dfswNum(r.rank, 0)} of ${dfswNum(r.total, 0)} ${top ? "&middot; " + top : ""}` +
      `${r.time_remaining !== "" ? " &middot; time left " + dfswEsc(r.time_remaining) : ""}<span class="dfsw-src">from ${dfswEsc(r.file)}</span>` +
      (r.lineup_matches_built ? "" : '<div class="dfsw-warn">The lineup in the standings file is not the same nine players as the built file. The table below shows what is in the contest.</div>') +
      (m ? '<div class="dfsw-src">A typed result also exists for this entry. The standings file wins.</div>' : "") + "</div>";
  }
  if (m) {
    const top = m.rank && m.total_entries ? ` &middot; top ${dfswNum((m.rank / m.total_entries) * 100, 1)}%` : "";
    return `<div class="dfsw-result"><b>${dfswNum(m.points)} pts</b>${m.rank != null ? ` &middot; place ${dfswNum(m.rank, 0)}${m.total_entries ? " of " + dfswNum(m.total_entries, 0) : ""}` : ""}${top}` +
      `${m.time_remaining ? " &middot; time left " + dfswEsc(m.time_remaining) : ""}<span class="dfsw-src">typed by ${dfswEsc(m.source)}, ${dfswEsc(m.updated)}</span>` +
      `${m.notes ? `<div class="dfsw-src">${dfswEsc(m.notes)}</div>` : ""}</div>`;
  }
  return '<div class="dfsw-result dfsw-none">No score yet.</div>';
}

function dfswPlayers(e) {
  const r = e.result;
  if (r && r.players && r.players.length) {
    return `<table class="dfsw-pl"><thead><tr><th>Slot</th><th>Player</th><th>Team</th><th class="num">Pts</th><th class="num">Drafted</th></tr></thead><tbody>` +
      r.players.map((p) => `<tr><td>${dfswEsc(p.slot)}</td><td>${dfswEsc(p.name)}</td><td>${dfswEsc(p.team)}</td><td class="num">${dfswNum(p.fpts)}</td><td class="num">${dfswEsc(p.drafted)}</td></tr>`).join("") +
      "</tbody></table>";
  }
  return `<table class="dfsw-pl"><thead><tr><th>Slot</th><th>Player</th><th>Team</th><th class="num">Salary</th></tr></thead><tbody>` +
    e.players.map((p) => `<tr><td>${dfswEsc(p.slot)}</td><td>${dfswEsc(p.name)}</td><td>${dfswEsc(p.team)}</td><td class="num">${p.salary ? "$" + Number(p.salary).toLocaleString() : ""}</td></tr>`).join("") +
    "</tbody></table>";
}

async function dfswLoad() {
  const box = document.getElementById("dfsw-entries");
  try {
    await dfswLoadWeeks();
    if (dfswWeek == null) { box.textContent = "No Week N folders found."; return; }
    const d = await (await fetch("/api/dfs/week?n=" + encodeURIComponent(dfswWeek), { cache: "no-store" })).json();
    if (d.error) { box.textContent = "DFS week not available: " + d.error; return; }
    dfswData = d;
    const f = d.files || {};
    document.getElementById("dfsw-files").innerHTML = `<dl class="dfsw-filelist">` +
      `<div><dt>Lineups file</dt><dd>${dfswEsc(f.entries || "none found")}</dd></div>` +
      `<div><dt>Player names from</dt><dd>${dfswEsc((f.salaries || []).join(", ") || "none found")}</dd></div>` +
      `<div><dt>Standings export</dt><dd>${dfswEsc((f.standings || []).join(", ") || "none yet")}</dd></div>` +
      `<div><dt>Typed results</dt><dd>${dfswEsc(f.manual || "none")}</dd></div>` +
      ((f.entries_other || []).length ? `<div><dt>Other entries files, not used</dt><dd>${dfswEsc(f.entries_other.join(", "))}</dd></div>` : "") + "</dl>";
    document.getElementById("dfsw-notes").innerHTML = (d.notes || []).map((n) => `<div class="note">${dfswEsc(n)}</div>`).join("");
    box.innerHTML = (d.entries || []).map((e, i) => {
      const inC = e.status.startsWith("IN CONTEST");
      return `<article class="dfsw-card"><header><span class="dfsw-n">Entry ${i + 1}</span> <span class="path">${dfswEsc(e.entry_id)}</span>` +
        ` <span class="dfs-tag ${inC ? "entered" : "notconfirmed"}">${dfswEsc(e.status)}</span></header>` +
        `<div class="dfsw-meta">${dfswEsc(e.contest_name)} &middot; fee ${dfswEsc(e.entry_fee)}${e.salary_total ? " &middot; salary $" + Number(e.salary_total).toLocaleString() : ""}</div>` +
        dfswResultBlock(e) + dfswPlayers(e) + "</article>";
    }).join("") || "No entries in this week's file.";
    const es = document.getElementById("dfsw-entry");
    const keep = es.value;
    es.innerHTML = (d.entries || []).map((e, i) => `<option value="${dfswEsc(e.entry_id)}">Entry ${i + 1} (${dfswEsc(e.entry_id)})</option>`).join("");
    if (keep) es.value = keep;
  } catch (err) {
    box.textContent = "DFS week not available: " + err;
  }
}

function dfswSetup() {
  const f = document.getElementById("dfsw-form");
  const msg = document.getElementById("dfsw-msg");
  const send = async (extra) => {
    const body = Object.assign(Object.fromEntries(new FormData(f).entries()), { week: dfswWeek }, extra || {});
    try {
      const resp = await fetch("/api/dfs/manual", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const d = await resp.json();
      if (!resp.ok) { msg.className = "dfs-msg err"; msg.textContent = d.error || "save failed"; return; }
      msg.className = "dfs-msg ok";
      msg.textContent = d.saved ? `Saved for entry ${d.entry_id}.` : `Removed the typed result for entry ${d.entry_id}.`;
      dfswLoad();
    } catch (err) { msg.className = "dfs-msg err"; msg.textContent = "save failed: " + err; }
  };
  f.addEventListener("submit", (e) => { e.preventDefault(); send(); });
  document.getElementById("dfsw-clear").onclick = () => send({ clear: "1" });
  document.getElementById("dfsw-entry").addEventListener("change", () => {
    const e = (dfswData && dfswData.entries || []).find((x) => x.entry_id === f.entry_id.value);
    const m = (e && e.manual) || {};
    for (const k of ["points", "rank", "total_entries", "time_remaining", "notes"]) f[k].value = m[k] == null ? "" : m[k];
  });
  document.getElementById("dfsw-week").addEventListener("change", (e) => { dfswWeek = +e.target.value; dfswLoad(); });
  dfswLoad();
  setInterval(dfswLoad, 60000);
}
dfswSetup();
