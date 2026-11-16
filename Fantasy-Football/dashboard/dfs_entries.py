"""DFS entries storage for the dashboard. Reads and writes tracker\\dfs_tracker.csv with the csv
module (every column kept as typed, unknown columns preserved). Every write makes a timestamped
backup first and replaces the file atomically. Nothing here talks to DraftKings or any network."""
import csv
import os
import re
import shutil
import tempfile
import threading
import time
from pathlib import Path

import config

BASE_COLS = ["date", "slate", "lineup_id", "source", "entry_fee", "contest", "projected_score", "actual_score",
             "cash_line", "finish", "profit_loss", "proj_own_avg", "actual_own_avg", "own_proj_vs_actual",
             "low_owned_hits", "qb_used", "qb_result", "notes"]
# Added 2026-11-13 for the dashboard: line_label (A/B/C, F1/F2/F3 or own), lineup_players (9 names joined
# by " | "), status (entered or not entered). Rank after the slate uses the existing "finish" column.
NEW_COLS = ["line_label", "lineup_players", "status"]
ALL_COLS = BASE_COLS + NEW_COLS
LABELS = ["A", "B", "C", "F1", "F2", "F3", "own"]
LABEL_TO_ID = {"A": "OA", "B": "OB", "C": "OC", "F1": "F1", "F2": "F2", "F3": "F3"}
EDITABLE = ["date", "slate", "line_label", "contest", "entry_fee", "lineup_players", "status",
            "actual_score", "finish", "profit_loss", "cash_line", "notes"]
_lock = threading.Lock()


def _clean(v, limit=500):
    v = "" if v is None else str(v)
    v = re.sub(r"[\r\n\t]+", " ", v).strip()
    return v[:limit]


def read_rows(path=None):
    path = Path(path or config.DFS_TRACKER_PATH)
    if not path.exists() or path.stat().st_size == 0:
        return list(ALL_COLS), []
    with open(path, newline="", encoding="utf-8") as f:
        rd = csv.DictReader(f)
        cols = list(rd.fieldnames or [])
        rows = [dict(r) for r in rd]
    for c in NEW_COLS:
        if c not in cols:
            cols.append(c)
    return cols, rows


def _num(s):
    try:
        return float(str(s).replace("$", "").strip())
    except ValueError:
        return None


def summary(rows, date=None):
    """spent = fees of entered rows. reserved = fees set on rows not yet entered. Rows with no fee count for nothing."""
    spent = reserved = 0.0
    dates = sorted({r.get("date", "") for r in rows if r.get("date")})
    if date is None and dates:
        date = dates[-1]  # default: latest slate date
    for r in rows:
        if date and r.get("date") != date:
            continue
        fee = _num(r.get("entry_fee", ""))
        if fee is None:
            continue
        if (r.get("status") or "").strip().lower() == "entered":
            spent += fee
        else:
            reserved += fee
    b = config.DFS_BANKROLL
    return {"date": date, "dates": dates, "bankroll": b, "spent": round(spent, 2), "reserved": round(reserved, 2),
            "available": round(b - spent - reserved, 2)}


def entries(date=None):
    cols, rows = read_rows()
    for r in rows:
        r["status"] = (r.get("status") or "").strip().lower() or "not entered"
    rows.sort(key=lambda r: (r.get("date", ""), r.get("lineup_id", "")), reverse=True)
    return {"columns": cols, "entries": rows, "summary": summary(rows, date), "tracker": str(config.DFS_TRACKER_PATH)}


def _backup(path):
    if not path.exists():
        return None
    config.DFS_BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    dst = config.DFS_BACKUP_DIR / f"dfs_tracker_{stamp}.csv"
    n = 1
    while dst.exists():
        dst = config.DFS_BACKUP_DIR / f"dfs_tracker_{stamp}-{n}.csv"
        n += 1
    shutil.copy2(path, dst)
    return str(dst)


def save_entry(data):
    """Add or edit one entry. Key = (date, lineup_id). Returns (result dict, error string or None)."""
    d = {k: _clean(data.get(k), 500) for k in EDITABLE}
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d["date"]):
        return None, "date must look like 2026-11-15"
    label = d["line_label"] or "own"
    if label not in LABELS:
        return None, "line must be one of " + ", ".join(LABELS)
    d["line_label"] = label
    status = d["status"].lower() or "not entered"
    if status not in ("entered", "not entered"):
        return None, "status must be entered or not entered"
    d["status"] = status
    for k in ("entry_fee", "profit_loss", "cash_line", "actual_score", "finish"):
        if d[k] and _num(d[k]) is None:
            return None, f"{k} must be a number"
    if d["entry_fee"] and _num(d["entry_fee"]) <= 0:
        return None, "entry_fee must be more than 0 (leave it blank if there is no fee yet)"
    names = [n.strip() for n in re.split(r"[|\n]", str(data.get("lineup_players") or "")) if n.strip()]
    if names and len(names) != 9:
        return None, f"lineup needs 9 names (QB, RB, RB, WR, WR, WR, TE, FLEX, DST), got {len(names)}"
    d["lineup_players"] = " | ".join(_clean(n, 60) for n in names)
    lid = _clean(data.get("lineup_id"), 40) or LABEL_TO_ID.get(label, "")
    with _lock:
        path = Path(config.DFS_TRACKER_PATH)
        cols, rows = read_rows(path)
        if not lid:  # a new own entry: OWN-1, OWN-2 ... per date
            n = 1 + sum(1 for r in rows if r.get("date") == d["date"] and str(r.get("lineup_id", "")).startswith("OWN-"))
            lid = f"OWN-{n}"
        hit = next((r for r in rows if r.get("date") == d["date"] and r.get("lineup_id") == lid), None)
        if hit is None:
            hit = {c: "" for c in cols}
            hit.update(date=d["date"], lineup_id=lid,
                       source={"own": "own", "A": "ours", "B": "ours", "C": "ours"}.get(label, "friend"))
            hit.update(line_label=label, status=status)  # defaults for a new row
            rows.append(hit)
        for k, v in d.items():
            if k != "date" and k in data:
                hit[k] = v  # only fields the caller sent are changed
        backup = _backup(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        os.replace(tmp, path)
    return {"ok": True, "lineup_id": lid, "backup": backup, "summary": summary(rows, d["date"])}, None


def lines():
    """Prefill helper: our A/B/C and the friend's F1/F2/F3 as 9 names each, if the local files exist."""
    out = {}
    try:
        with open(config.DFS_OUR_LINES_CSV, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                out.setdefault(r["lineup"], []).append(r["name"])
    except OSError:
        pass
    try:
        cur, n = [], 0
        for raw in config.DFS_FRIEND_LINES_TXT.read_text(encoding="utf-8").splitlines():
            t = raw.strip()
            if not t or t.lower().startswith("lineup") or t.startswith("#"):
                if cur and (not t or t.lower().startswith("lineup")):
                    n += 1
                    out[f"F{n}"] = cur
                    cur = []
                continue
            cur.append(t)
        if cur:
            n += 1
            out[f"F{n}"] = cur
    except OSError:
        pass
    return out
