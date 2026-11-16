// DFS Entries panel (2026-11-13). Talks only to this localhost server (/api/dfs), which reads and writes
// tracker\dfs_tracker.csv. Nothing here contacts DraftKings or enters a lineup.
let dfsLines = {};
let dfsRows = [];
let dfsDate = "";
const LABEL_NAMES = { A: "Our A", B: "Our B", C: "Our C", F1: "Friend 1", F2: "Friend 2", F3: "Friend 3", own: "Own" };
const dfsEsc = (v) => String(v == null ? "" : v).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

function dfsLabelOf(r) {
  if (r.line_label) return r.line_label;
  const m = { OA: "A", OB: "B", OC: "C", F1: "F1", F2: "F2", F3: "F3" };
  return m[r.lineup_id] || "own";
}

async function loadDfs() {
  try {
    const d = await (await fetch("/api/dfs" + (dfsDate ? "?date=" + encodeURIComponent(dfsDate) : ""), { cache: "no-store" })).json();
    dfsRows = d.entries || [];
    const s = d.summary;
    document.getElementById("dfs-path").textContent = d.tracker;
    const sel = document.getElementById("dfs-date");
    sel.innerHTML = (s.dates || []).map((x) => `<option value="${dfsEsc(x)}" ${x === s.date ? "selected" : ""}>${dfsEsc(x)}</option>`).join("");
    const money = (n) => (Number(n) < 0 ? "-$" : "$") + Math.abs(Number(n)).toFixed(2);
    document.getElementById("dfs-summary").innerHTML =
      `<div class="dfs-slate">Totals for slate <b>${dfsEsc(s.date || "none")}</b> only</div>` +
      `<dl class="dfs-stats"><div><dt>Bankroll</dt><dd>${money(s.bankroll)}</dd></div><div><dt>Entered (spent)</dt><dd>${money(s.spent)}</dd></div>` +
      `<div><dt>Reserved, not entered</dt><dd>${money(s.reserved)}</dd></div><div class="stat-key"><dt>Left</dt><dd${s.available < 0 ? ' class=\"over\"' : ""}>${money(s.available)}</dd></div></dl>`;
    const plClass = (v) => { const n = parseFloat(v); return isNaN(n) ? "" : n > 0 ? " pos" : n < 0 ? " neg" : ""; };
    document.querySelector("#dfs-table tbody").innerHTML = dfsRows.map((r, i) => {
      const names = (r.lineup_players || "").split(" | ").filter(Boolean).join(", ") || "(no names saved)";
      const fee = r.entry_fee ? "$" + dfsEsc(r.entry_fee) : "";
      const entered = r.status === "entered";
      return `<tr><td data-label="Slate">${dfsEsc(r.slate || r.date)}</td><td data-label="Line" class="line-cell">${dfsEsc(LABEL_NAMES[dfsLabelOf(r)] || r.lineup_id)}</td>` +
        `<td data-label="Contest">${dfsEsc(r.contest)}</td><td data-label="Fee" class="num">${fee}</td><td data-label="Status"><span class="dfs-tag ${entered ? "entered" : ""}">${dfsEsc(r.status)}</span></td>` +
        `<td data-label="Lineup" class="names">${dfsEsc(names)}</td><td data-label="Points" class="num">${dfsEsc(r.actual_score)}</td><td data-label="Rank" class="num">${dfsEsc(r.finish)}</td><td data-label="P/L" class="num${plClass(r.profit_loss)}">${dfsEsc(r.profit_loss)}</td>` +
        `<td class="act"><button data-i="${i}" class="dfs-edit">Edit</button></td></tr>`;
    }).join("") || '<tr class="empty"><td colspan="10">No entries for this slate yet. Use Add or edit an entry below.</td></tr>';
  } catch (e) {
    document.getElementById("dfs-summary").textContent = "DFS data not available: " + e;
  }
}

function dfsFill(row) {
  const f = document.getElementById("dfs-form");
  f.lineup_id.value = row.lineup_id || "";
  for (const k of ["date", "slate", "contest", "entry_fee", "status", "actual_score", "finish", "cash_line", "profit_loss", "notes"]) {
    f[k].value = row[k] || (k === "status" ? "not entered" : "");
  }
  f.line_label.value = dfsLabelOf(row);
  f.lineup_players.value = (row.lineup_players || "").split(" | ").filter(Boolean).join("\n");
  document.getElementById("dfs-form-wrap").open = true;
}

function setupDfs() {
  fetch("/api/dfs/lines").then((r) => r.json()).then((l) => { dfsLines = l; }).catch(() => {});
  document.querySelector("#dfs-table tbody").addEventListener("click", (e) => {
    if (e.target.classList.contains("dfs-edit")) dfsFill(dfsRows[+e.target.dataset.i]);
  });
  const f = document.getElementById("dfs-form");
  const msg = document.getElementById("dfs-msg");
  document.getElementById("dfs-clear").onclick = () => { f.reset(); f.lineup_id.value = ""; msg.textContent = ""; };
  document.getElementById("dfs-fill").onclick = () => {
    const names = dfsLines[f.line_label.value];
    if (names) f.lineup_players.value = names.join("\n");
    else { msg.className = "dfs-msg err"; msg.textContent = "No saved names for that line. Type the nine names."; }
  };
  f.line_label.addEventListener("change", () => { f.lineup_id.value = ""; });
  f.addEventListener("submit", async (e) => {
    e.preventDefault();
    const body = Object.fromEntries(new FormData(f).entries());
    try {
      const resp = await fetch("/api/dfs", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const d = await resp.json();
      if (!resp.ok) { msg.className = "dfs-msg err"; msg.textContent = d.error || "save failed"; return; }
      msg.className = "dfs-msg ok";
      msg.textContent = `Saved ${d.lineup_id}. Backup: ${d.backup || "none (new file)"}`;
      loadDfs();
    } catch (err) { msg.className = "dfs-msg err"; msg.textContent = "save failed: " + err; }
  });
  document.getElementById("dfs-date").addEventListener("change", (e) => { dfsDate = e.target.value; loadDfs(); });
  loadDfs();
  setInterval(loadDfs, 60000);
}
setupDfs();
