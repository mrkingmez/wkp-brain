"""scorecard.md and daily-notes.md generators. Every number is computed from decisions.jsonl and
paper-trades.csv and the table lists the line or id it came from. If paper looks too good, suspect the simulator first.

Only lines and trades that carry the CURRENT config hash are counted. A changed config means a new experiment:
older lines stay in the files, are listed as "not counted", and the counts start again."""
import collections
import csv
import datetime as dt
import json
import os
from zoneinfo import ZoneInfo

from . import risk
from .config import config_hash
from .stats import bdays_between, net_at

ET = ZoneInfo("America/New_York")
LEDGER_TITLE = {"main": "MAIN ledger (fills at the next hourly bar open)",
                "zac": "ZAC-CAN-ACT ledger (fills only at the next trading session open; go-live is judged here)"}


def read_decisions(path, bad=None):
    rows = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for n, line in enumerate(f, 1):
                if not line.strip():
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    if bad is not None:
                        bad.append(n)
                    continue
                r["_line"] = n
                rows.append(r)
    return rows


def read_trades(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def pair_trades(rows):
    opens, closes = {}, {}
    for r in rows:
        (opens if r["event"] == "OPEN" else closes)[r["trade_id"]] = r
    return opens, closes


def max_drawdown(pnls, start_equity):
    eq = peak = start_equity
    worst = 0.0
    for p in pnls:
        eq += p
        peak = max(peak, eq)
        worst = max(worst, peak - eq)
    return worst, (worst / peak * 100 if peak else 0.0)


def read_history(outdir):
    p = os.path.join(outdir, "config-history.jsonl")
    out = []
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    out.append(json.loads(line))
                except ValueError:
                    pass
    return out


def _ledger_of(r):
    return r.get("ledger") or "main"


def _fees(cfg):
    pb = cfg["paper_book"]
    return float(pb["fee_bps_each_side"]), float(pb["sell_reg_fee_bps"])


def ledger_block(name, rows, cfg, start_equity, line_of, dec_cur):
    """Returns (markdown lines, stats dict) for one ledger."""
    opens, closes = pair_trades(rows)
    closed = sorted((closes[t] for t in closes if t in opens), key=lambda r: r["ts_utc"])
    still_open = [t for t in opens if t not in closes]
    wins = [r for r in closed if float(r["pnl_net"]) > 0]
    gross = sum(float(r["pnl_gross"]) for r in closed)
    net = sum(float(r["pnl_net"]) for r in closed)
    rs = [float(r["r_net"]) for r in closed if r["r_net"] not in ("", None)]
    dd, ddp = max_drawdown([float(r["pnl_net"]) for r in closed], start_equity)
    by_end = [r for r in closed if r["reason"] == "end_rule"]
    fee_bps, reg_bps = _fees(cfg)
    views = cfg["scorecard"]["haircut_views_bps"]
    passbps = cfg["scorecard"]["pass_haircut_bps"]
    L = ["", "## %s" % LEDGER_TITLE[name],
         "- Paper trades opened: %d. Closed: %d (of those closed by the end rule at the last mark: %d). Still open, not in P and L: %d." % (len(opens), len(closed), len(by_end), len(still_open))]
    nets_by_view = {}
    if closed:
        L += ["- Win rate (net above zero, at the run's own %s bps haircut): %d of %d = %.1f percent." % (cfg["paper_book"]["haircut_bps_each_side"], len(wins), len(closed), 100.0 * len(wins) / len(closed)),
              ("- Average R (net P and L over risk at entry): %.3f over %d trades." % (sum(rs) / len(rs), len(rs))) if rs else "- Average R: not available.",
              "- Gross P and L (before slippage and fees): %.2f" % gross,
              "- Net P and L (after slippage and fees): %.2f (%.3f percent of the simulated book)" % (net, net / start_equity * 100),
              "- Max drawdown on realized net P and L: %.2f (%.3f percent of peak equity). Open positions and unrealized swings are not in this figure." % (dd, ddp)]
        L += ["", "Haircut view (slippage each side recomputed from raw prices; 15 and 30 are stress levels, not measured; share counts were sized at the run's own haircut):", "",
              "| Slippage each side | Net P and L | Per trade | Percent of book | Positive |", "|---|---|---|---|---|"]
        for b in views:
            v = sum(net_at(float(opens[r["trade_id"]]["price_raw"]), float(r["price_raw"]), int(float(r["shares"])), b, fee_bps, reg_bps) for r in closed)
            nets_by_view[b] = v
            L.append("| %s bps | %.2f | %.2f | %.3f | %s |" % (b, v, v / len(closed), v / start_equity * 100, "yes" if v > 0 else "no"))
        # small-account view
        eq = float(cfg["scorecard"]["sizing_view_equity"])
        mult = cfg["rules"]["atr_stop_multiple"]
        L += ["", "Small-account sizing view: the same signals sized as if the account were $%.0f (fractional shares allowed, same risk tiers, same 25 percent cap; fractional stop orders and the broker's minimum order are NOT VERIFIED):" % eq, "",
              "| Slippage each side | Net P and L on $%.0f | Percent of $%.0f |" % (eq, eq), "|---|---|---|"]
        sized = []
        for r in closed:
            o = opens[r["trade_id"]]
            fill, stop = float(o["price_filled"]), float(o["stop"])
            atr = (fill - stop) / mult
            sh, det = risk.size_shares(eq, eq, fill, atr, float(o["score"]), cfg, fractional=True)
            sized.append((r, o, sh, det))
        for b in views:
            v = sum(sh * net_at(float(o["price_raw"]), float(r["price_raw"]), 1, b, fee_bps, reg_bps) for r, o, sh, det in sized)
            L.append("| %s bps | %.4f | %.3f |" % (b, v, v / eq * 100))
        tiny = sum(1 for r, o, sh, det in sized if sh * float(o["price_filled"]) < 1.0)
        bind = collections.Counter(det.get("binding", "none") for r, o, sh, det in sized)
        L.append("")
        L.append("Sizing view detail: size bound by %s. Positions under $1 of notional (likely below a broker minimum): %d of %d." % (
            ", ".join("%s %d" % (k, v) for k, v in sorted(bind.items())) or "none", tiny, len(sized)))
        # regime split
        reg = collections.defaultdict(list)
        for r in closed:
            reg[opens[r["trade_id"]].get("regime") or "UNKNOWN"].append(r)
        L += ["", "Results split by regime tag at entry:", "", "| Regime | Trades | Wins | Net P and L |", "|---|---|---|---|"]
        for k in sorted(reg):
            L.append("| %s | %d | %d | %.2f |" % (k, len(reg[k]), sum(1 for r in reg[k] if float(r["pnl_net"]) > 0), sum(float(r["pnl_net"]) for r in reg[k])))
    else:
        L.append("- No closed trades yet. A no-trade stretch is allowed and is reported as is.")
    # PDT
    dts = sorted({dt.datetime.fromisoformat(r["bar_t"].replace("Z", "+00:00")).astimezone(ET).date() for r in closed if r.get("day_trade") == "True"})
    allc = [dt.datetime.fromisoformat(r["bar_t"].replace("Z", "+00:00")).astimezone(ET).date() for r in closed if r.get("day_trade") == "True"]
    win = cfg["pdt"]["window_trading_days"]
    peak_roll = max([sum(1 for x in allc if 0 <= bdays_between(x, d) < win and x <= d) for d in dts] or [0])
    months = collections.Counter((d.year, d.month) for d in allc)
    blocked = sum(1 for d in dec_cur if d["action"] == "CANCEL" and "PDT guard" in d["reason"] and (d.get("ledger") or "main") == name)
    L.append("- Day trades (opened and closed the same ET day): %d. Most in any rolling %d trading days: %d (limit %d). Most in one calendar month: %d (limit %d). Entries refused by the PDT guard: %d. Rule text NOT confirmed, holidays not modeled." % (
        len(allc), win, peak_roll, cfg["pdt"]["max_day_trades_rolling"], max(months.values() or [0]), cfg["pdt"]["max_day_trades_per_month"], blocked))
    L += ["", "Every closed trade (trace):", "",
          "| Trade | Symbol | Opened by decision (jsonl line) | Closed by decision (jsonl line) | Exit | Gross | Net | R |", "|---|---|---|---|---|---|---|---|"]
    for r in closed:
        o = opens[r["trade_id"]]
        sig = o["reason"].replace("signal ", "")
        L.append("| %s | %s | %s (%s) | %s (%s) | %s | %s | %s | %s |" % (r["trade_id"], r["symbol"], sig, line_of.get(sig, "?"),
                 r["decision_id"], line_of.get(r["decision_id"], "?"), r["reason"], r["pnl_gross"], r["pnl_net"], r["r_net"]))
    if not closed:
        L.append("| none | | | | | | | |")
    return L, {"opened": len(opens), "closed": len(closed), "wins": len(wins), "gross": gross, "net": net, "max_dd": dd,
               "nets_by_view": nets_by_view, "end_rule": len(by_end), "still_open": len(still_open)}


def build_scorecard(outdir, cfg, start_equity=None, note="", chash=None):
    bad = []
    dec = read_decisions(os.path.join(outdir, "decisions.jsonl"), bad)
    tr_all = read_trades(os.path.join(outdir, "paper-trades.csv"))
    if chash is None:
        hs = [d["config_hash"] for d in dec if d.get("config_hash")]
        chash = hs[-1] if hs else config_hash(cfg)
    start_equity = float(start_equity or cfg["paper_book"]["starting_equity"])
    dec_cur = [d for d in dec if d.get("config_hash") == chash]
    not_counted = len(dec) - len(dec_cur)
    tr = [r for r in tr_all if r.get("config_hash") == chash]
    evals = [d for d in dec_cur if d["action"] in ("TRADE", "SKIP", "WATCH") and d["symbol"] != "*"]
    fresh = [d for d in evals if d.get("fresh")]
    counted = [d for d in evals if d.get("counted")]
    by_action = collections.Counter(d["action"] for d in evals)
    fresh_by_action = collections.Counter(d["action"] for d in fresh)
    counted_by_action = collections.Counter(d["action"] for d in counted)
    skip_reasons = collections.Counter(d["reason"].split(":")[0][:70] if d["reason"].startswith("FAIL") else d["reason"][:70]
                                       for d in evals if d["action"] == "SKIP")
    line_of = {d["decision_id"]: d["_line"] for d in dec}
    h = cfg["paper_book"]
    regimes = collections.Counter(d.get("regime", "UNKNOWN") for d in evals if d.get("fresh"))
    L = ["# Watch week scorecard (paper only)", "",
         "Generated %s. Config hash counted: %s. Source files: decisions.jsonl (%d lines, %d with this hash), paper-trades.csv (%d rows, %d with this hash). %s" % (
             dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), chash, len(dec), len(dec_cur), len(tr_all), len(tr), note), "",
         "Not financial advice. No real order was ever placed. Trades are our own simulated fills."]
    if bad:
        L.append("WARNING: %d unreadable line(s) in decisions.jsonl were skipped (line numbers %s)." % (len(bad), ", ".join(map(str, bad[:10]))))
    L += ["", "## Frozen config",
          "- Counting only lines and trades carrying hash %s. Lines under any other hash (not counted): %d." % (chash, not_counted)]
    hist = read_history(outdir)
    for e in hist:
        L.append("- %s: hash %s (previous %s). %s" % (e.get("recorded_at_utc"), e.get("hash"), e.get("previous"), e.get("note")))
    L += ["", "## Labeled assumptions (placeholders, not measured)",
          "- Fill at the next 1-hour bar open after the signal bar closes (main ledger) or at the next session open (Zac-can-act ledger), plus slippage %s bps each side." % h["haircut_bps_each_side"],
          "- Fee line %s bps each side, sell regulatory fee %s bps. Placeholders until set from a real source." % (h["fee_bps_each_side"], h["sell_reg_fee_bps"]),
          "- Data feed %s (IEX only, thinner than the full tape). Simulated book start %.2f (a placeholder size, judge results in percent)." % (cfg["feed"], start_equity),
          "- Exits are checked against hourly high and low. If stop and target are both inside one bar, the stop is assumed to hit first. A gap through the stop fills at the worse of the stop and the bar open.",
          "- End rule: last day %s. Open trades are closed at the last mark seen by the final scan (close to, not equal to, the official close)." % cfg["end_rule"]["last_day"],
          "", "## Counts (each traceable to lines in decisions.jsonl)",
          "- COUNTED decisions (score %s or higher, once per setup): %d. TRADE %d, WATCH %d. These are the decisions that count toward the 50." % (cfg["counting"]["min_score"], len(counted), counted_by_action["TRADE"], counted_by_action["WATCH"]),
          "- Evaluation lines (TRADE, SKIP, WATCH), all logged, NOT the counted number: %d. TRADE %d, WATCH %d, SKIP %d." % (len(evals), by_action["TRADE"], by_action["WATCH"], by_action["SKIP"]),
          "- Fresh evaluations (a new closed bar was actually scored): %d. TRADE %d, WATCH %d, SKIP %d." % (len(fresh), fresh_by_action["TRADE"], fresh_by_action["WATCH"], fresh_by_action["SKIP"]),
          "- Fresh evaluations by regime tag: %s." % (", ".join("%s %d" % (k, v) for k, v in sorted(regimes.items())) or "none")]
    stats = {}
    for name in ("main", "zac"):
        if name == "zac" and not cfg["zac_ledger"]["enabled"]:
            continue
        rows = [r for r in tr if _ledger_of(r) == name]
        blk, s = ledger_block(name, rows, cfg, start_equity, line_of, dec_cur)
        L += blk
        stats[name] = s
    # baseline
    marks = [(d["_line"], d["ts_utc"], d["spy_mark"]) for d in dec_cur if isinstance(d.get("spy_mark"), (int, float))]
    L += ["", "## Buy-and-hold baseline (%s, same IEX bars, from the scan marks in decisions.jsonl)" % cfg["market_gauge"]]
    base_pct = None
    if len(marks) >= 2 and marks[0][2] > 0:
        base_pct = (marks[-1][2] / marks[0][2] - 1) * 100
        L.append("- %s mark %.2f at %s (line %d) to %.2f at %s (line %d): %.3f percent." % (cfg["market_gauge"], marks[0][2], marks[0][1], marks[0][0], marks[-1][2], marks[-1][1], marks[-1][0], base_pct))
        for name in stats:
            L.append("- %s ledger net P and L as percent of the book: %.3f percent (versus baseline %.3f)." % (name, stats[name]["net"] / start_equity * 100, base_pct))
    else:
        L.append("- Not available: fewer than two scans with a %s mark under this hash." % cfg["market_gauge"])
    # go-live view
    z = stats.get("zac")
    pb = cfg["scorecard"]["pass_haircut_bps"]
    L += ["", "## Plan checks (the numbers, not a verdict)",
          "- Counted decisions: %d (the plan asks for 50)." % len(counted),
          "- Zac-ledger closed trades: %d. About 20 means the plumbing works, 50 or more is needed before any edge claim." % (z["closed"] if z else 0)]
    if z and z["closed"]:
        v = z["nets_by_view"].get(pb)
        L.append("- Zac-ledger net P and L at %s bps each side: %.2f (%s). The plan passes only if this is positive." % (pb, v, "positive" if v > 0 else "NOT positive"))
    else:
        L.append("- Zac-ledger net at %s bps: not available (no closed trades)." % pb)
    L += ["- This scorecard is evidence for the trading-director and Zac. It never says go live.", "",
          "## Skip reasons (SKIP lines)"]
    L += ["- %s: %d" % (k, v) for k, v in skip_reasons.most_common(12)] or ["- none"]
    L += ["", "Checks for QA: totals above equal the sums of the table rows; decision ids resolve to decisions.jsonl lines; "
          "if results look too good, check the haircut and the stop-first assumption before believing them.", ""]
    text = "\n".join(L)
    with open(os.path.join(outdir, "scorecard.md"), "w", encoding="utf-8") as f:
        f.write(text)
    m = stats["main"]
    out = {"evals": len(evals), "fresh": len(fresh), "counted": len(counted), "opened": m["opened"], "closed": m["closed"], "wins": m["wins"],
           "gross": m["gross"], "net": m["net"], "max_dd": m["max_dd"], "text": text, "config_hash": chash, "baseline_pct": base_pct}
    if z:
        out.update(zac_opened=z["opened"], zac_closed=z["closed"], zac_net=z["net"], zac_nets_by_view=z["nets_by_view"])
    return out


def write_daily_note(outdir, date_et, state_path=None):
    """Append one note for an ET date: scans, decisions, trades, kill switch, request ids, data problems."""
    dec = [d for d in read_decisions(os.path.join(outdir, "decisions.jsonl"))
           if dt.datetime.fromisoformat(d["ts_utc"].replace("Z", "+00:00")).astimezone(ET).date().isoformat() == date_et]
    scans = {d["scan_id"] for d in dec}
    ev = [d for d in dec if d["action"] in ("TRADE", "SKIP", "WATCH") and d["symbol"] != "*"]
    cnt = collections.Counter(d["action"] for d in dec)
    rids = {r for d in dec for r in d.get("request_ids", []) if r}
    bad = [d for d in dec if "data call failed" in d.get("reason", "")]
    regs = collections.Counter(d.get("regime", "UNKNOWN") for d in ev)
    hashes = sorted({d.get("config_hash") for d in dec if d.get("config_hash")})
    st = None
    if state_path and os.path.exists(state_path):
        with open(state_path, "r", encoding="utf-8") as f:
            st = json.load(f)
    L = ["", "## %s (ET)" % date_et,
         "- Scans: %d. Evaluation lines: %d. Fresh: %d. COUNTED decisions: %d." % (len(scans), len(ev), sum(1 for d in ev if d.get("fresh")), sum(1 for d in ev if d.get("counted"))),
         "- Actions today: " + ", ".join("%s %d" % (k, v) for k, v in sorted(cnt.items())),
         "- Config hash on today's lines: %s. Regime tags on evaluation lines: %s." % (", ".join(hashes) or "none", ", ".join("%s %d" % (k, v) for k, v in sorted(regs.items())) or "none"),
         "- Kill switch tripped today: %s. Weekly loss limit hit today: %s." % ("YES" if cnt["KILL"] else "no", "YES" if cnt["WEEK_LIMIT"] else "no"),
         "- Alpaca request ids recorded: %d (in each decisions.jsonl line)." % len(rids),
         "- Data failures: %d lines." % len(bad)]
    if st:
        L.append("- End of state file, main ledger: cash %.2f, open positions %s, pending signals %s." % (st["cash"], ", ".join(st["positions"]) or "none", ", ".join(st["pending"]) or "none"))
        z = st.get("zac")
        if z:
            L.append("- End of state file, Zac-can-act ledger: cash %.2f, open positions %s, pending signals %s." % (z["cash"], ", ".join(z["positions"]) or "none", ", ".join(z["pending"]) or "none"))
    path = os.path.join(outdir, "daily-notes.md")
    head = "" if os.path.exists(path) else "# Watch week daily notes (paper only)\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(head + "\n".join(L) + "\n")
    return "\n".join(L)
