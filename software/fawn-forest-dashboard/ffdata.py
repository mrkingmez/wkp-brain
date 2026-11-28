"""Data layer for the Fawn Forest Investments dashboard.

READ-ONLY. Every function here only opens files for reading. It never writes,
never calls the network, reads no environment variables
(it reads none), and uses no credentials of any kind.

Honesty rule: a number appears only if it is in a file. Anything missing comes
back as {"available": False, "missing": "<path>"} and the page says
NOT AVAILABLE and names the file.
"""
from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
    ET = ZoneInfo("America/New_York")
except Exception:  # tzdata missing: fall back to fixed EST, say so in output
    ET = None

WKP = Path(r"D:\WKP")
WATCHER_DIR = WKP / "software" / "wkt-alpaca-watcher"
LIVE_DIR = WKP / "Investing" / "watch-week"
DEMO_DIR = WATCHER_DIR / "demo-out"
CONFIG_YAML = WATCHER_DIR / "config.yaml"
INSIDER_LIVE = LIVE_DIR / "insider"
INSIDER_DEMO = WKP / "software" / "wkt-insider-scanner" / "demo-out"
CRYPTO_DIR = LIVE_DIR / "crypto"
CHECKLIST = Path(__file__).resolve().parent / "data" / "go-live-checklist.json"

LOW_SAMPLE_TRADES = 20      # watcher README: 20 closed trades = plumbing works
EDGE_TRADES = 50            # watcher README: an edge claim needs 50 or more
EDGE_DECISIONS = 50
MAX_CURVE_POINTS = 400
MAX_LINE_BYTES = 2_000_000


def default_paths(source: str) -> dict:
    """Return the file map for 'live' or 'demo'. Paths only, nothing read."""
    base = DEMO_DIR if source == "demo" else LIVE_DIR
    return {
        "source": source,
        "dir": base,
        "decisions": base / "decisions.jsonl",
        "trades": base / "paper-trades.csv",
        "state": base / "state.json",
        "history": base / "config-history.jsonl",
        "scorecard": base / "scorecard.md",
        "notes": base / "daily-notes.md",
        "flag": LIVE_DIR / "GO-COUNTED.flag",
        "config_yaml": CONFIG_YAML,
        "insider_dir": INSIDER_DEMO if source == "demo" else INSIDER_LIVE,
        "crypto_dir": CRYPTO_DIR,
        "checklist": CHECKLIST,
    }


def clean(obj):
    """Replace NaN/Infinity anywhere in the output with None so JSON never breaks."""
    if isinstance(obj, float):
        return obj if obj == obj and obj not in (float("inf"), float("-inf")) else None
    if isinstance(obj, dict):
        return {str(k): clean(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [clean(v) for v in obj]
    return obj


def as_dict(v):
    return v if isinstance(v, dict) else {}


def missing(path) -> dict:
    return {"available": False, "missing": str(path)}


def _mtime(path: Path):
    try:
        return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()
    except OSError:
        return None


def read_jsonl(path: Path):
    """Return (rows, bad_line_count). Never raises on bad content."""
    rows, bad = [], 0
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                if len(line) > MAX_LINE_BYTES:
                    bad += 1
                    continue
                try:
                    obj = json.loads(line)
                except ValueError:
                    bad += 1
                    continue
                if isinstance(obj, dict):
                    rows.append(obj)
                else:
                    bad += 1
    except OSError:
        return None, 0
    return rows, bad


def read_json(path: Path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            obj = json.load(fh)
        return obj if isinstance(obj, dict) else None
    except (OSError, ValueError):
        return None


def read_csv(path: Path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace", newline="") as fh:
            return list(csv.DictReader(fh))
    except OSError:
        return None


def num(v):
    try:
        if v is None or v == "":
            return None
        f = float(v)
        if f != f or f in (float("inf"), float("-inf")):
            return None
        return f
    except (TypeError, ValueError):
        return None


def parse_ts(s):
    if not isinstance(s, str):
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)   # naive stamps are read as UTC
    return dt


def et_date(dt: datetime) -> str:
    if ET is not None:
        return dt.astimezone(ET).date().isoformat()
    return (dt - timedelta(hours=5)).date().isoformat()


def downsample(points: list, limit: int = MAX_CURVE_POINTS) -> list:
    if len(points) <= limit:
        return points
    step = len(points) / float(limit)
    out = [points[int(i * step)] for i in range(limit)]
    if out[-1] != points[-1]:
        out.append(points[-1])
    return out


def config_last_day(path: Path):
    """Read end_rule.last_day from config.yaml by text match (no YAML library)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = re.search(r"end_rule:\s*(?:#[^\n]*)?\n(?:[ \t]+[^\n]*\n)*?[ \t]+last_day:\s*\"?(\d{4}-\d{2}-\d{2})\"?", text)
    return m.group(1) if m else None


def weekdays_between(a: str, b: str):
    try:
        d0 = datetime.fromisoformat(a).date()
        d1 = datetime.fromisoformat(b).date()
    except ValueError:
        return None
    n, d = 0, d0
    while d <= d1:
        if d.weekday() < 5:
            n += 1
        d += timedelta(days=1)
    return n


# ---------------------------------------------------------------- sections

def build_week(P, decisions, state, history, now):
    out = {}
    cur_hash = (state or {}).get("config_hash")
    hist_rows = history or []
    if not cur_hash and hist_rows:
        cur_hash = hist_rows[-1].get("hash")
    out["config_hash"] = cur_hash or None
    out["config_hash_source"] = "state.json" if (state or {}).get("config_hash") else ("config-history.jsonl" if cur_hash else None)
    out["config_changes"] = [
        {"hash": h.get("hash"), "at": h.get("recorded_at_utc"), "note": h.get("note")}
        for h in hist_rows[-5:]
    ]
    flag = P["flag"]
    if P["source"] == "demo":
        out["go_counted"] = {"state": "DEMO", "detail": "demo run does not use the flag"}
    else:
        out["go_counted"] = {"state": "SET" if flag.exists() else "NOT SET", "detail": str(flag)}
    out["end_date"] = config_last_day(P["config_yaml"])
    out["end_date_source"] = str(P["config_yaml"]) if out["end_date"] else None
    out["ended"] = bool((state or {}).get("ended"))
    # day count from the scan dates present in the decisions file
    dates = set()
    for d in decisions or []:
        dt = parse_ts(d.get("ts_utc"))
        if dt is not None and d.get("clock_open") is True:
            dates.add(et_date(dt))
    dates = sorted(dates)
    out["session_days_seen"] = len(dates)
    out["first_day"] = dates[0] if dates else None
    out["last_day_seen"] = dates[-1] if dates else None
    if P["source"] == "live" and out["first_day"] and out["end_date"]:
        out["planned_days"] = weekdays_between(out["first_day"], out["end_date"])
    else:
        out["planned_days"] = None
    counted = [d for d in (decisions or []) if d.get("counted") is True and d.get("config_hash") == cur_hash]
    out["counted_decisions"] = len(counted)
    out["decisions_goal"] = EDGE_DECISIONS
    out["decisions_total_lines"] = len(decisions or [])
    return out


def pnl_curve(rows, start_equity):
    """Realized-equity curve from CLOSE events, sorted by time."""
    closes = []
    for r in rows:
        if r.get("event") != "CLOSE":
            continue
        net = num(r.get("pnl_net"))
        dt = parse_ts(r.get("ts_utc"))
        if net is None or dt is None:
            continue
        closes.append((dt, net))
    closes.sort(key=lambda x: x[0])
    pts, eq = [], start_equity
    for dt, net in closes:
        eq += net
        pts.append([dt.isoformat(), round(eq, 2)])
    return pts


def build_ledger(name, rows, cur_hash, start_equity, closed_stats):
    mine = [r for r in rows if r.get("ledger") == name and (cur_hash is None or r.get("config_hash") == cur_hash)]
    opens = {r.get("trade_id"): r for r in mine if r.get("event") == "OPEN"}
    closes = {r.get("trade_id"): r for r in mine if r.get("event") == "CLOSE"}
    open_list = []
    for tid, r in sorted(opens.items()):
        if tid not in closes:
            open_list.append({
                "trade_id": tid, "symbol": r.get("symbol"), "opened": r.get("ts_utc"),
                "shares": num(r.get("shares")), "entry": num(r.get("price_filled")),
                "stop": num(r.get("stop")), "target": num(r.get("target")),
                "score": num(r.get("score")), "regime": r.get("regime"),
            })
    closed_list = []
    for tid, r in sorted(closes.items(), key=lambda kv: kv[1].get("ts_utc") or ""):
        o = opens.get(tid, {})
        closed_list.append({
            "trade_id": tid, "symbol": r.get("symbol"), "opened": o.get("ts_utc"),
            "closed": r.get("ts_utc"), "exit": r.get("reason"),
            "net": num(r.get("pnl_net")), "r": num(r.get("r_net")),
            "score": num(r.get("score")), "regime": r.get("regime"),
        })
    wins = sum(1 for c in closed_list if (c["net"] or 0) > 0)
    n = len(closed_list)
    nets = [c["net"] for c in closed_list if c["net"] is not None]
    rs = [c["r"] for c in closed_list if c["r"] is not None]
    sample = "NONE" if n == 0 else ("LOW SAMPLE" if n < EDGE_TRADES else "EDGE-TESTABLE")
    curve = pnl_curve(mine, start_equity)
    # haircut view straight from state.json closed_stats (the watcher's own numbers)
    hc = {"available": False, "missing": "state.json closed_stats"}
    if isinstance(closed_stats, list) and closed_stats:
        use = [c for c in closed_stats if isinstance(c, dict) and (cur_hash is None or c.get("hash") == cur_hash)]
        levels = {}
        for lvl in ("5", "15", "30"):
            vals = [num(as_dict(c.get("net")).get(lvl)) for c in use]
            vals = [v for v in vals if v is not None]
            if vals:
                levels[lvl] = {"net": round(sum(vals), 2), "pct": round(100.0 * sum(vals) / start_equity, 3) if start_equity else None, "n": len(vals)}
        if levels:
            hc = {"available": True, "levels": levels, "source": "state.json closed_stats"}
    return {
        "name": name,
        "start_equity": start_equity,
        "closed_n": n,
        "open_n": len(open_list),
        "wins": wins,
        "win_rate": round(100.0 * wins / n, 1) if n else None,
        "avg_r": round(sum(rs) / len(rs), 3) if rs else None,
        "net_pnl": round(sum(nets), 2) if nets else None,
        "sample_label": sample,
        "curve": downsample(curve),
        "open": open_list,
        "closed": closed_list[-40:],
        "haircut": hc,
    }


def build_spy(decisions, start_equity, cur_hash):
    """SPY buy-and-hold line from the spy_mark on each scan, rebased to the book."""
    pts, first = [], None
    seen = None
    for d in decisions or []:
        m = num(d.get("spy_mark"))
        sid = d.get("scan_id") or d.get("ts_utc")
        if m is None or sid == seen:
            continue
        seen = sid
        dt = parse_ts(d.get("ts_utc"))
        if dt is None:
            continue
        if first is None:
            first = m
        if not first or not start_equity:
            return {"available": False, "missing": "usable spy_mark and starting_equity (zero or missing)"}
        pts.append([dt.isoformat(), round(start_equity * m / first, 2)])
    if not pts:
        return {"available": False, "missing": "spy_mark field in decisions.jsonl"}
    ret = round(100.0 * (pts[-1][1] / pts[0][1] - 1.0), 3)
    return {"available": True, "curve": downsample(pts), "return_pct": ret, "source": "spy_mark on each scan in decisions.jsonl"}


def build_regime(decisions):
    regs = [d for d in (decisions or []) if d.get("action") == "REGIME"]
    if not regs:
        tags = [d for d in (decisions or []) if d.get("regime")]
        if not tags:
            return {"available": False, "missing": "REGIME lines in decisions.jsonl"}
        last = tags[-1]
        return {"available": True, "tag": last.get("regime"), "detail": None, "history": [], "note": "tag only, no REGIME detail line yet"}
    last = regs[-1]
    hist = []
    for r in regs[-8:]:
        hist.append({"ts": r.get("ts_utc"), "tag": r.get("regime")})
    det = as_dict(last.get("regime_detail"))
    keep = ("atr_pct", "atr_pct_median", "breadth", "breadth_symbols", "close", "sma_fast", "sma_slow", "slope_up", "daily_bars", "last_daily_bar_date")
    return {"available": True, "tag": last.get("regime"), "ts": last.get("ts_utc"),
            "detail": {k: det.get(k) for k in keep if k in det and isinstance(det.get(k), (int, float, bool, str))}, "history": hist}


def build_heat(decisions):
    latest, scored = {}, {}
    for d in decisions or []:
        sym = d.get("symbol")
        if not isinstance(sym, str) or not sym or sym == "*" or d.get("action") == "REGIME":
            continue
        if d.get("action") in ("SKIP", "WATCH", "TRADE"):
            latest[sym] = d
            if num(d.get("score")) is not None:
                scored[sym] = d
    if not latest:
        return {"available": False, "missing": "SKIP/WATCH/TRADE lines in decisions.jsonl"}
    cells = []
    for sym in sorted(latest):
        d, s = latest[sym], scored.get(sym)
        cells.append({
            "symbol": sym, "action": d.get("action"), "ts": d.get("ts_utc"),
            "reason": (d.get("reason") or "")[:90], "fresh": d.get("fresh"),
            "score": num(s.get("score")) if s else None,
            "score_ts": s.get("ts_utc") if s else None,
            "setup": (s or d).get("setup"),
            "signal": d.get("action"),
        })
    return {"available": True, "cells": cells}


def build_freshness(P, decisions, now, mode_label):
    last_dt, last_open = None, None
    for d in reversed(decisions or []):
        dt = parse_ts(d.get("ts_utc"))
        if dt is not None:
            last_dt, last_open = dt, d.get("clock_open")
            break
    files = []
    for key in ("decisions", "trades", "state", "scorecard", "notes"):
        p = P[key]
        files.append({"name": p.name, "mtime": _mtime(p), "present": p.exists()})
    out = {"files": files, "last_scan": last_dt.isoformat() if last_dt else None, "stale": None, "reason": None}
    if last_dt is None:
        out["stale"], out["reason"] = True, "no scan lines on disk"
        return out
    age = (now - last_dt).total_seconds()
    out["age_seconds"] = int(age)
    if P["source"] == "demo":
        out["stale"], out["reason"] = False, "DEMO: scan times are fictional, stale check does not apply"
    elif last_open is True and age > 300:
        out["stale"], out["reason"] = True, "market was open at the last scan and it is over 5 minutes old"
    elif last_open is False and age > 4 * 86400:
        out["stale"], out["reason"] = True, "last scan is over 4 days old"
    else:
        out["stale"], out["reason"] = False, "within limits"
    return out


def build_checklist(path: Path, week, ledgers):
    obj = read_json(path)
    if obj is None or not isinstance(obj.get("items"), list):
        return missing(path)
    items = []
    for it in obj["items"][:20]:
        if isinstance(it, dict):
            items.append({"n": it.get("n"), "title": it.get("title"), "state": it.get("state", "FAIL"), "note": it.get("note")})
    passed = sum(1 for i in items if i["state"] == "PASS")
    ev = None
    z = ledgers.get("zac") if ledgers else None
    if z:
        ev = {"counted_decisions": week.get("counted_decisions"), "decisions_goal": EDGE_DECISIONS,
              "zac_closed": z["closed_n"], "trades_goal": LOW_SAMPLE_TRADES}
    return {"available": True, "passed": passed, "total": len(items), "items": items,
            "as_of": obj.get("as_of"), "maintained_by": obj.get("maintained_by"), "source": str(path), "evidence": ev}


def build_insider(P):
    d = P["insider_dir"]
    clusters = d / "clusters.jsonl"
    rows, bad = read_jsonl(clusters)
    if rows is None:
        return {"available": False, "missing": str(clusters),
                "status": "NOT AVAILABLE: scanner is built (software\\wkt-insider-scanner), no live pull has run yet. A live pull needs its LIVE-OK.flag and the SEC_USER_AGENT environment variable (name only)."}
    demo = P["source"] == "demo"
    out = []
    for r in rows:
        iss = as_dict(r.get("issuer"))
        out.append({
            "ticker": iss.get("ticker"), "name": iss.get("name"), "status": r.get("status"),
            "insiders": r.get("n_distinct_insiders"), "value": num(r.get("total_value")),
            "filed": r.get("last_filing_date"), "type": r.get("cluster_type"),
            "flags": r.get("flags") if isinstance(r.get("flags"), list) else [],
        })
    out.sort(key=lambda x: str(x.get("filed") or ""), reverse=True)
    counted = sum(1 for x in out if x["status"] == "COUNTED")
    return {"available": True, "demo": demo, "clusters": out[:12], "counted": counted, "total": len(out), "bad_lines": bad,
            "source": str(clusters), "note": "Research signal only. No sizing and no trade authority."}


def build_crypto(P):
    d = P["crypto_dir"]
    trades, state = d / "paper-trades.csv", d / "state.json"
    if P["source"] == "demo":
        return {"available": False, "status": "NOT BUILT", "detail": "Design only (software\\wkt-crypto-watcher\\DESIGN.md). No demo numbers are invented for crypto."}
    rows = read_csv(trades)
    if rows is None:
        return {"available": False, "status": "NOT BUILT",
                "detail": "Design only (software\\wkt-crypto-watcher\\DESIGN.md). Nothing at " + str(trades)}
    closes = [r for r in rows if r.get("event") == "CLOSE"]
    nets = [num(r.get("pnl_net")) for r in closes]
    nets = [n for n in nets if n is not None]
    return {"available": True, "closed_n": len(closes), "net_pnl": round(sum(nets), 2) if nets else None,
            "wins": sum(1 for n in nets if n > 0), "source": str(trades),
            "sample_label": "LOW SAMPLE" if len(closes) < EDGE_TRADES else "EDGE-TESTABLE",
            "state_file_present": state.exists()}


# ---------------------------------------------------------------- entry

def build_state(source: str = "auto", paths: dict | None = None, now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    if paths is None:
        if source == "auto":
            live = default_paths("live")
            source = "live" if live["decisions"].exists() else "demo"
        paths = default_paths(source)
    P = paths
    source = P["source"]
    out = {
        "department": "FAWN FOREST INVESTMENTS",
        "paper_only": True,
        "source": source,
        "demo": source == "demo",
        "generated_utc": now.isoformat(),
        "read_only": True,
    }
    decisions, bad = read_jsonl(P["decisions"])
    if decisions is None:
        out["available"] = False
        out["missing"] = str(P["decisions"])
        out["message"] = "NOT AVAILABLE: decisions.jsonl not found at " + str(P["decisions"]) + ". The watcher has not written a log here yet."
        out["checklist"] = build_checklist(P["checklist"], {}, {})
        out["insider"] = build_insider(P)
        out["crypto"] = build_crypto(P)
        out["freshness"] = build_freshness(P, [], now, source)
        out["week"] = {"go_counted": {"state": "NOT SET" if not P["flag"].exists() else "SET", "detail": str(P["flag"])},
                       "end_date": config_last_day(P["config_yaml"]), "config_hash": None}
        return out
    out["available"] = True
    out["bad_lines"] = bad
    state = read_json(P["state"])
    history, _ = read_jsonl(P["history"])
    week = build_week(P, decisions, state, history, now)
    out["week"] = week
    cur = week["config_hash"]
    start = num((state or {}).get("starting_equity"))
    rows = read_csv(P["trades"])
    if not start or rows is None:
        out["ledgers"] = missing(P["trades"] if rows is None else P["state"])
        ledgers = {}
    else:
        zac_state = as_dict((state or {}).get("zac"))
        ledgers = {
            "main": build_ledger("main", rows, cur, start, (state or {}).get("closed_stats")),
            "zac": build_ledger("zac", rows, cur, start, zac_state.get("closed_stats")),
        }
        out["ledgers"] = ledgers
        out["spy"] = build_spy(decisions, start, cur)
    out["regime"] = build_regime(decisions)
    out["heat"] = build_heat(decisions)
    out["checklist"] = build_checklist(P["checklist"], week, ledgers)
    out["insider"] = build_insider(P)
    out["crypto"] = build_crypto(P)
    out["freshness"] = build_freshness(P, decisions, now, source)
    return out
