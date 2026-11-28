"use strict";
/* Fawn Forest Investments dashboard. Read-only. Page text is set as plain text only. */
var HASH = location.hash.replace("#", "").split(",");
var SRC = "auto";
["auto", "live", "demo"].forEach(function (x) { if (HASH.indexOf(x) >= 0) SRC = x; });
var NS = "http://www.w3.org/2000/svg";
var THEME = "jarvis";
try { THEME = localStorage.getItem("ff-theme") === "ares" ? "ares" : "jarvis"; } catch (e) { }
if (HASH.indexOf("ares") >= 0) THEME = "ares"; if (HASH.indexOf("jarvis") >= 0) THEME = "jarvis";
var LAST = null;
/* Wording per skin. Numbers never change, only these words. Anything not listed keeps its plain name. */
var WORDS = {
  ares: {
    "FOUR-WEEK PAPER TEST": "OPERATION CLOCK", "REGIME": "MARKET CONDITIONS", "EQUITY VS SPY BUY-AND-HOLD": "FORCE LINE VS SPY BASELINE",
    "MAIN LEDGER": "MAIN ROSTER", "ZAC-CAN-ACT LEDGER (go-live is judged here)": "ZAC-CAN-ACT ROSTER (go-live judged here)",
    "HAIRCUT VIEW": "COST STRESS TEST", "WATCH LIST HEAT MAP": "TARGET BOARD", "OPEN AND RECENT CLOSED TRADES": "ENGAGEMENTS",
    "GO-LIVE CHECKLIST": "CLEARANCE CHECKLIST", "CRYPTO GROUP": "CRYPTO SECTION", "INSIDER BUYS": "INSIDER SIGNALS",
    "FRESH": "LINK LIVE", "STALE": "LINK STALE", "Trading department": "Command post"
  },
  jarvis: { "REGIME": "Market mood", "FOUR-WEEK PAPER TEST": "Paper test" }
};
function W(t) { var m = WORDS[THEME] || {}; return m[t] !== undefined ? m[t] : t; }
function cvar(n, d) { var v = getComputedStyle(document.documentElement).getPropertyValue(n).trim(); return v || d; }
function applyTheme() {
  document.documentElement.setAttribute("data-theme", THEME);
  Array.prototype.forEach.call(document.querySelectorAll("[data-theme-btn]"), function (b) { b.classList.toggle("on", b.getAttribute("data-theme-btn") === THEME); });
  document.getElementById("eyebrow").textContent = W("Trading department");
}

function h(tag, cls, text, kids) {
  var e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text !== undefined && text !== null) e.textContent = String(text);
  (kids || []).forEach(function (k) { if (k) e.appendChild(k); });
  return e;
}
function clear(id) { var e = document.getElementById(id); while (e.firstChild) e.removeChild(e.firstChild); return e; }
function label(t, right) { return h("div", "label", null, [h("span", null, W(t)), right ? (typeof right === "string" ? h("span", null, right) : h("span", null, null, [right])) : null]); }
function na(what, missing) {
  var d = h("div", "na", null, [h("b", null, "NOT AVAILABLE")]);
  d.appendChild(h("div", null, what));
  if (missing) d.appendChild(h("code", null, "Missing source: " + missing));
  return d;
}
function money(v) { if (v === null || v === undefined) return "n/a"; var s = Math.abs(v).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); return (v < 0 ? "-$" : "$") + s; }
function pct(v, d) { if (v === null || v === undefined) return "n/a"; return (v > 0 ? "+" : "") + v.toFixed(d === undefined ? 2 : d) + "%"; }
function cls(v) { return v > 0 ? "up" : (v < 0 ? "down" : "dim"); }
function fmtTs(s) { if (!s) return "n/a"; var d = new Date(s); return isNaN(d) ? "n/a" : d.toLocaleString([], { month: "short", day: "numeric", hour: "numeric", minute: "2-digit" }); }
function kv(k, v, c) { return h("div", "kv", null, [h("div", "k", k), h("div", "v " + (c || ""), v)]); }
function pill(t, c) { return h("span", "pill " + c, t); }

function render(s) {
  LAST = s; applyTheme();
  renderStatus(s);
  document.getElementById("demo-banner").hidden = !s.demo;
  renderFresh(s);
  if (s.available === false) {
    ["c-chart", "c-main", "c-zac", "c-haircut", "c-heat", "c-trades", "c-regime"].forEach(function (id) {
      var e = clear(id); e.appendChild(label(id.replace("c-", "").toUpperCase())); e.appendChild(na(s.message || "No data yet.", s.missing));
    });
  } else {
    renderChart(s); renderLedger("c-main", "MAIN LEDGER", s, "main"); renderLedger("c-zac", "ZAC-CAN-ACT LEDGER (go-live is judged here)", s, "zac");
    renderHaircut(s); renderHeat(s); renderTrades(s); renderRegime(s);
  }
  renderWeek(s); renderCheck(s); renderCrypto(s); renderInsider(s);
}

function renderStatus(s) {
  var e = clear("statusline"), w = s.week || {}, f = s.freshness || {};
  var bits = ["PAPER ONLY", "NO LIVE ORDERS", "READ-ONLY", "SOURCE " + (s.source || "n/a").toUpperCase(), "GO-COUNTED " + ((w.go_counted && w.go_counted.state) || "n/a")];
  if (s.demo) bits.push("DEMO DATA");
  if (f.stale) bits.push("LINK STALE");
  if (THEME === "ares") e.appendChild(h("span", null, "STATUS // " + bits.join(" // ")));
  else e.appendChild(h("span", null, s.demo ? "Showing the demo. Nothing here is real, and nothing is live." : "All paper. Nothing is live. Nothing can be ordered from here."));
}
function renderFresh(s) {
  var f = s.freshness || {}, e = clear("fresh");
  e.className = "strip" + (f.stale ? " stale" : "");
  e.appendChild(h("span", null, null, [h("span", "dot"), h("b", null, W(f.stale ? "STALE" : "FRESH"))]));
  e.appendChild(h("span", null, "Last scan: " + (f.last_scan ? fmtTs(f.last_scan) : "NOT AVAILABLE")));
  if (f.reason) e.appendChild(h("span", null, f.reason));
  e.appendChild(h("span", null, "Source: " + (s.source || "n/a").toUpperCase()));
  var present = (f.files || []).filter(function (x) { return x.present; }).length;
  e.appendChild(h("span", null, "Files found: " + present + " of " + ((f.files || []).length || 5)));
  e.appendChild(h("span", null, "Page read: " + fmtTs(s.generated_utc)));
}

function renderWeek(s) {
  var w = s.week || {}, e = clear("c-week");
  e.appendChild(label("FOUR-WEEK PAPER TEST", w.ended ? pill("ENDED", "warn") : null));
  var days = w.session_days_seen;
  e.appendChild(h("div", "big", days === undefined || days === null ? "n/a" : days));
  e.appendChild(h("div", "sub", "session days seen" + (w.planned_days ? " of " + w.planned_days + " weekdays to the end date" : "")));
  var row = h("div", "row");
  var g = w.go_counted || {};
  row.appendChild(kv("GO-COUNTED flag", g.state || "n/a", g.state === "SET" ? "up" : "warn"));
  row.appendChild(kv(s.demo ? "Live plan end date" : "End date", w.end_date || "n/a"));
  row.appendChild(kv("Counted decisions", (w.counted_decisions === undefined ? "n/a" : w.counted_decisions) + " / " + (w.decisions_goal || 50)));
  e.appendChild(row);
  e.appendChild(h("div", "sub", "Config hash: " + (w.config_hash || "NOT AVAILABLE (no state.json or config-history.jsonl)")));
  if (w.end_date_source === undefined || !w.end_date) e.appendChild(h("div", "sub warn", "End date not read: config.yaml end_rule.last_day not found"));
}

function renderRegime(s) {
  var r = s.regime, e = clear("c-regime");
  e.appendChild(label("REGIME"));
  if (!r || r.available === false) { e.appendChild(na("No regime line in the log yet.", r && r.missing)); return; }
  var tag = r.tag || "UNKNOWN", c = /^UP/.test(tag) ? "up" : (/^DOWN/.test(tag) ? "down" : "warn");
  e.appendChild(h("div", "big " + c, tag.replace(/_/g, " ")));
  var d = r.detail;
  if (d) {
    var row = h("div", "row");
    if (d.atr_pct !== undefined) row.appendChild(kv("ATR %", String(d.atr_pct)));
    if (d.atr_pct_median !== undefined) row.appendChild(kv("ATR median", String(d.atr_pct_median)));
    if (d.breadth !== undefined) row.appendChild(kv("Breadth", String(d.breadth)));
    if (d.slope_up !== undefined) row.appendChild(kv("Slope up", d.slope_up ? "yes" : "no"));
    e.appendChild(row);
    if (d.close !== undefined) e.appendChild(h("div", "sub", "SPY close " + d.close + ", fast avg " + d.sma_fast + ", slow avg " + d.sma_slow));
  } else if (r.note) e.appendChild(h("div", "sub", r.note));
  var hist = h("div", "hist");
  (r.history || []).forEach(function (x) { hist.appendChild(h("span", null, (x.ts || "").slice(5, 10) + " " + (x.tag || ""))); });
  e.appendChild(hist);
}

function renderChart(s) {
  var e = clear("c-chart"), L = s.ledgers;
  e.appendChild(label("EQUITY VS SPY BUY-AND-HOLD", "percent change from the starting book, realized trades only"));
  if (!L || L.main === undefined) { e.appendChild(na("Ledger files missing.", L && L.missing)); return; }
  var series = [];
  function add(name, color, curve, start, dash) {
    if (!curve || !curve.length || !start) return;
    series.push({ name: name, color: color, dash: dash, pts: curve.map(function (p) { return [new Date(p[0]).getTime(), 100 * (p[1] / start - 1)]; }) });
  }
  add("Main", cvar("--c-main", "#6fb8ff"), L.main.curve, L.main.start_equity);
  add("Zac-can-act", cvar("--c-zac", "#2de2a0"), L.zac.curve, L.zac.start_equity);
  if (s.spy && s.spy.available) add("SPY buy-and-hold", cvar("--c-spy", "#9fb8d6"), s.spy.curve, L.main.start_equity, "6 5");
  if (!series.length) { e.appendChild(na("No closed trades and no SPY marks to draw yet.", "paper-trades.csv, decisions.jsonl")); return; }
  var W = 900, H = 300, pl = 54, pr = 14, pt = 14, pb = 26;
  var xs = [], ys = [0];
  series.forEach(function (se) { se.pts.forEach(function (p) { xs.push(p[0]); ys.push(p[1]); }); });
  var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
  if (x1 === x0) x1 = x0 + 1; if (y1 === y0) { y1 += 1; y0 -= 1; }
  var padY = (y1 - y0) * 0.08; y0 -= padY; y1 += padY;
  function X(v) { return pl + (v - x0) / (x1 - x0) * (W - pl - pr); }
  function Y(v) { return H - pb - (v - y0) / (y1 - y0) * (H - pt - pb); }
  var svg = document.createElementNS(NS, "svg"); svg.setAttribute("viewBox", "0 0 " + W + " " + H); svg.setAttribute("class", "chart"); svg.setAttribute("role", "img");
  svg.setAttribute("aria-label", "Equity curves of both ledgers against SPY buy and hold");
  function el(n, a) { var x = document.createElementNS(NS, n); for (var k in a) x.setAttribute(k, a[k]); return x; }
  for (var i = 0; i <= 4; i++) {
    var v = y0 + (y1 - y0) * i / 4, yy = Y(v);
    svg.appendChild(el("line", { x1: pl, x2: W - pr, y1: yy, y2: yy, stroke: "#232b27", "stroke-width": 1 }));
    var t = el("text", { x: pl - 8, y: yy + 4, "text-anchor": "end", fill: "#8a958f", "font-size": 12, "font-family": "monospace" }); t.textContent = v.toFixed(1) + "%"; svg.appendChild(t);
  }
  svg.appendChild(el("line", { x1: pl, x2: W - pr, y1: Y(0), y2: Y(0), stroke: "#5d6862", "stroke-width": 1.2 }));
  [x0, x1].forEach(function (xv, i) {
    var t = el("text", { x: i ? W - pr : pl, y: H - 6, "text-anchor": i ? "end" : "start", fill: "#8a958f", "font-size": 12 });
    t.textContent = new Date(xv).toLocaleDateString([], { month: "short", day: "numeric" }); svg.appendChild(t);
  });
  series.forEach(function (se) {
    var d = se.pts.map(function (p, i) { return (i ? "L" : "M") + X(p[0]).toFixed(1) + " " + Y(p[1]).toFixed(1); }).join(" ");
    var a = { d: d, fill: "none", stroke: se.color, "stroke-width": 2.4, "stroke-linejoin": "round", "stroke-linecap": "round" };
    if (se.dash) a["stroke-dasharray"] = se.dash;
    svg.appendChild(el("path", a));
    var lp = se.pts[se.pts.length - 1];
    svg.appendChild(el("circle", { cx: X(lp[0]), cy: Y(lp[1]), r: 4, fill: se.color }));
  });
  e.appendChild(svg);
  var lg = h("div", "legend");
  series.forEach(function (se) {
    var last = se.pts[se.pts.length - 1][1], i = h("i"); i.style.borderTopColor = se.color; if (se.dash) i.style.borderTopStyle = "dashed";
    lg.appendChild(h("span", null, null, [i, h("span", null, se.name + " " + pct(last))]));
  });
  e.appendChild(lg);
  if (s.demo) e.appendChild(h("div", "sub warn", "DEMO: fictional prices and dates."));
}

function renderLedger(id, title, s, key) {
  var e = clear(id), L = s.ledgers && s.ledgers[key];
  e.appendChild(label(title));
  if (!L) { e.appendChild(na("Ledger not read.", s.ledgers && s.ledgers.missing)); return; }
  var net = L.net_pnl;
  e.appendChild(h("div", "big " + cls(net), net === null ? "n/a" : money(net)));
  e.appendChild(h("div", "sub", "net P and L after haircut, closed trades" + (net !== null && L.start_equity ? " (" + pct(100 * net / L.start_equity, 2) + " of the book)" : "")));
  var row = h("div", "row");
  row.appendChild(kv("Win rate", L.win_rate === null ? "n/a" : L.win_rate.toFixed(0) + "%  (" + L.wins + " of " + L.closed_n + ")"));
  row.appendChild(kv("Avg R", L.avg_r === null ? "n/a" : L.avg_r.toFixed(2), cls(L.avg_r)));
  row.appendChild(kv("Open", L.open_n));
  e.appendChild(row);
  var lab = L.sample_label, c = lab === "EDGE-TESTABLE" ? "up" : "warn";
  var txt = lab === "NONE" ? "NO CLOSED TRADES YET" : (lab === "LOW SAMPLE" ? "LOW SAMPLE: " + L.closed_n + " of 50 trades. " + (L.closed_n < 20 ? "Win rate means little yet." : "Plumbing works, no edge claim yet.") : "50 OR MORE TRADES");
  var box = h("div", "sub", null, [pill(txt, c)]); box.style.marginTop = "12px"; e.appendChild(box);
  var bar = h("div", "bar", null, [h("div")]); bar.firstChild.style.width = Math.min(100, 100 * L.closed_n / 50) + "%"; e.appendChild(bar);
  e.appendChild(h("div", "sub", L.closed_n + " of 50 trades toward an edge claim"));
}

function renderHaircut(s) {
  var e = clear("c-haircut"), L = s.ledgers;
  e.appendChild(label("HAIRCUT VIEW", "slippage each side. 15 and 30 are stress levels, not measured"));
  if (!L || !L.main) { e.appendChild(na("Ledger not read.", L && L.missing)); return; }
  var t = h("table"), thead = h("tr");
  ["Slippage", "Main net", "Main %", "Zac net", "Zac %"].forEach(function (x, i) { thead.appendChild(h("th", i ? "r" : "t", x)); });
  t.appendChild(thead);
  var anyRow = false;
  ["5", "15", "30"].forEach(function (lvl) {
    var m = L.main.haircut.available ? L.main.haircut.levels[lvl] : null, z = L.zac.haircut.available ? L.zac.haircut.levels[lvl] : null;
    var tr = h("tr");
    tr.appendChild(h("td", "t", lvl + " bps" + (lvl === "30" ? "  (pass line)" : "")));
    [m && m.net, m && m.pct, z && z.net, z && z.pct].forEach(function (v, i) {
      var isPct = i % 2 === 1;
      tr.appendChild(h("td", "r " + (v === null || v === undefined ? "dim" : cls(v)), v === null || v === undefined ? "n/a" : (isPct ? pct(v, 2) : money(v))));
    });
    if (m || z) anyRow = true;
    t.appendChild(tr);
  });
  var sc = h("div", "scroll", null, [t]); e.appendChild(sc);
  if (!anyRow) e.appendChild(na("No closed trades with haircut figures yet.", "state.json closed_stats"));
  e.appendChild(h("div", "sub", "Go-live needs the Zac-can-act ledger positive at 30 bps. Numbers come from the watcher's own state.json."));
}

function heatClass(c) {
  if (c.action === "TRADE") return "h-trade";
  if (c.score !== null && c.score >= 70) return "h-hot";
  if (c.action === "WATCH" || (c.score !== null && c.score >= 55)) return "h-watch";
  return "h-none";
}
function renderHeat(s) {
  var e = clear("c-heat"), H = s.heat;
  e.appendChild(label("WATCH LIST HEAT MAP", "latest score and signal per symbol"));
  if (!H || H.available === false) { e.appendChild(na("No scan lines yet.", H && H.missing)); return; }
  var g = h("div", "heat");
  H.cells.forEach(function (c) {
    var cell = h("div", "cell " + heatClass(c));
    cell.title = (c.reason || "") + (c.score_ts ? " (score at " + fmtTs(c.score_ts) + ")" : "");
    cell.appendChild(h("div", "s", c.symbol));
    cell.appendChild(h("div", "n " + (c.score !== null && c.score >= 70 ? "up" : (c.score !== null ? "" : "dim")), c.score === null ? "--" : c.score.toFixed(0)));
    cell.appendChild(h("div", "a", c.signal + (c.setup && c.score !== null ? " " + c.setup.replace(/_/g, " ") : (c.score === null ? " no score" : ""))));
    g.appendChild(cell);
  });
  e.appendChild(g);
  e.appendChild(h("div", "sub", "Score 70 or more can trade. Grey dashes: the last scan found no setup to score, so there is no score to show."));
}

function renderTrades(s) {
  var e = clear("c-trades"), L = s.ledgers;
  e.appendChild(label("OPEN AND RECENT CLOSED TRADES", "Zac-can-act ledger"));
  if (!L || !L.zac) { e.appendChild(na("Ledger not read.", L && L.missing)); return; }
  var z = L.zac, t = h("table"), hr = h("tr");
  ["", "Symbol", "Exit", "Net", "R"].forEach(function (x, i) { hr.appendChild(h("th", i > 2 ? "r" : "t", x)); });
  t.appendChild(hr);
  z.open.forEach(function (o) {
    var tr = h("tr"); tr.appendChild(h("td", "t", null, [pill("OPEN", "warn")])); tr.appendChild(h("td", "t", o.symbol));
    tr.appendChild(h("td", "t dim", "stop " + (o.stop === null ? "n/a" : o.stop.toFixed(2)))); tr.appendChild(h("td", "r dim", "open")); tr.appendChild(h("td", "r dim", "n/a")); t.appendChild(tr);
  });
  z.closed.slice(-8).reverse().forEach(function (c) {
    var tr = h("tr"); tr.appendChild(h("td", "t dim", (c.closed || "").slice(5, 10))); tr.appendChild(h("td", "t", c.symbol)); tr.appendChild(h("td", "t dim", c.exit));
    tr.appendChild(h("td", "r " + cls(c.net), c.net === null ? "n/a" : money(c.net))); tr.appendChild(h("td", "r " + cls(c.r), c.r === null ? "n/a" : c.r.toFixed(2))); t.appendChild(tr);
  });
  if (!z.open.length && !z.closed.length) { e.appendChild(na("No trades on this ledger yet. A quiet week is a valid result.", "paper-trades.csv")); return; }
  e.appendChild(h("div", "scroll", null, [t]));
  e.appendChild(h("div", "sub", "Open now: " + z.open_n + ". Closed: " + z.closed_n + ". Main ledger: " + L.main.open_n + " open, " + L.main.closed_n + " closed."));
}

function renderCheck(s) {
  var e = clear("c-check"), C = s.checklist;
  e.appendChild(label("GO-LIVE CHECKLIST"));
  if (!C || C.available === false) { e.appendChild(na("Checklist file not found.", C && C.missing)); return; }
  e.appendChild(h("div", "big " + (C.passed === C.total ? "up" : "warn"), C.passed + " of " + C.total));
  e.appendChild(h("div", "sub", "Going live is Zac's call. As of " + (C.as_of || "n/a") + ". Edited by hand in the checklist file."));
  var ul = h("ul", "check");
  C.items.forEach(function (it) {
    var st = it.state, b = h("div", "box " + (st === "PASS" ? "pass" : (st === "FAIL" ? "" : "pend")), st === "PASS" ? "OK" : (st === "FAIL" ? "X" : "?"));
    var li = h("li", null, null, [b, h("div", null, null, [h("div", null, it.n + ". " + it.title), it.note ? h("div", "sub", it.note) : null])]);
    ul.appendChild(li);
  });
  e.appendChild(ul);
  if (C.evidence) e.appendChild(h("div", "sub", (s.demo ? "DEMO run evidence (fictional): " : "Evidence: ") + C.evidence.counted_decisions + " of " + C.evidence.decisions_goal + " counted decisions, " + C.evidence.zac_closed + " closed Zac-ledger trades (goal " + C.evidence.trades_goal + ")."));
}

function renderCrypto(s) {
  var e = clear("c-crypto"), C = s.crypto || {};
  e.appendChild(label("CRYPTO GROUP"));
  if (C.available) {
    e.appendChild(h("div", "big " + cls(C.net_pnl), C.net_pnl === null ? "n/a" : money(C.net_pnl)));
    e.appendChild(h("div", "sub", C.closed_n + " closed simulated trades, " + C.wins + " wins. " + C.sample_label));
  } else {
    e.appendChild(h("div", "big warn", C.status || "NOT BUILT"));
    e.appendChild(h("div", "sub", C.detail || "No crypto ledger on disk."));
  }
}

function renderInsider(s) {
  var e = clear("c-insider"), I = s.insider || {};
  e.appendChild(label("INSIDER BUYS", I.demo ? pill("DEMO", "warn") : "research signal only"));
  if (!I.available) { e.appendChild(na(I.status || "Scanner output not found.", I.missing)); return; }
  e.appendChild(h("div", "mid", I.counted + " counted clusters, " + I.total + " seen"));
  var t = h("table"), hr = h("tr");
  ["Ticker", "Insiders", "Value", "Filed"].forEach(function (x, i) { hr.appendChild(h("th", i ? "r" : "t", x)); });
  t.appendChild(hr);
  I.clusters.slice(0, 6).forEach(function (c) {
    var tr = h("tr"); tr.appendChild(h("td", "t", (c.ticker || "?") + (c.status && c.status !== "COUNTED" ? " (" + c.status.toLowerCase() + ")" : "")));
    tr.appendChild(h("td", "r", c.insiders === null ? "n/a" : c.insiders)); tr.appendChild(h("td", "r", c.value === null ? "n/a" : money(c.value).replace(/\.00$/, ""))); tr.appendChild(h("td", "r dim", c.filed || "n/a")); t.appendChild(tr);
  });
  e.appendChild(h("div", "scroll", null, [t]));
  e.appendChild(h("div", "sub", I.note));
}

function load() {
  fetch("/api/state?source=" + SRC, { cache: "no-store" })
    .then(function (r) { return r.json(); })
    .then(render)
    .catch(function () {
      var f = clear("fresh"); f.className = "strip stale"; f.appendChild(h("span", null, "NOT AVAILABLE: the dashboard server is not answering. Check the black window is still open."));
    });
}
Array.prototype.forEach.call(document.querySelectorAll("[data-theme-btn]"), function (b) {
  b.addEventListener("click", function () {
    THEME = b.getAttribute("data-theme-btn");
    try { localStorage.setItem("ff-theme", THEME); } catch (e) { }
    applyTheme(); if (LAST) render(LAST);
  });
});
applyTheme();
Array.prototype.forEach.call(document.querySelectorAll(".seg button"), function (b) {
  if (b.getAttribute("data-src") === SRC) { Array.prototype.forEach.call(document.querySelectorAll(".seg button"), function (x) { x.classList.remove("on"); }); b.classList.add("on"); }
  b.addEventListener("click", function () { location.hash = b.getAttribute("data-src"); location.reload(); });
});
load();
setInterval(load, 30000);
