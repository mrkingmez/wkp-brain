"""Week-aware DFS view for the dashboard (added 2026-11-19).

Reads Zac's DraftKings files from the week folders he already uses (D:\\Draft Kings\\Week N\\).
Read only on every DraftKings file: nothing here moves, renames or deletes anything there.
The only file this module writes is manual-results.json inside a week folder (typed points and
place, for when there is no standings export yet). Nothing here talks to DraftKings or any
network. Agents never log in to DraftKings, enter lineups or spend.

What it looks for inside D:\\Draft Kings\\Week N\\ (top level and one level of subfolders):
  entries   a csv whose header starts with "Entry ID" and has a "Contest ID" column
            (DKEntries*.csv). Pick order: name contains FINAL, then name contains FILLED,
            then any other; newest file wins inside the same tier.
  salaries  DKSalaries*.csv (player ID to name, team, salary). Falls back to the salary
            block DraftKings prints on the right side of the entries file.
  standings contest-standings-*.csv or contest-standings-*.zip (the DraftKings GameCenter
            "Export Lineups to CSV" download), or any csv/zip with "standings" in the name.
            Must have the columns Rank, EntryId, EntryName, TimeRemaining, Points, Lineup.
Skipped everywhere: any path with FAKE, MOCK, dryrun, smoketest or NEGATIVE_TEST in it.
"""
import csv
import io
import json
import os
import re
import tempfile
import threading
import time
import zipfile
from pathlib import Path

DK_ROOT = Path(os.environ.get("DFS_DK_ROOT", r"D:\Draft Kings"))
SKIP_RE = re.compile(r"fake|mock|dryrun|smoketest|negative_test", re.IGNORECASE)
WEEK_RE = re.compile(r"^Week (\d{1,2})$", re.IGNORECASE)
SLOTS = ["QB", "RB", "RB", "WR", "WR", "WR", "TE", "FLEX", "DST"]
MANUAL_NAME = "manual-results.json"
_lock = threading.Lock()


def weeks():
    out = []
    if DK_ROOT.is_dir():
        for p in DK_ROOT.iterdir():
            m = WEEK_RE.match(p.name)
            if p.is_dir() and m:
                out.append(int(m.group(1)))
    return sorted(out, reverse=True)


def week_dir(n):
    n = int(n)
    if not 1 <= n <= 25:
        raise ValueError("week out of range")
    return DK_ROOT / f"Week {n}"


def _files(folder, exts=(".csv",)):
    """Files at the top level and one level down, skipping test and fake paths."""
    found = []
    if not folder.is_dir():
        return found
    for p in folder.iterdir():
        if SKIP_RE.search(p.name):
            continue
        if p.is_file() and p.suffix.lower() in exts:
            found.append(p)
        elif p.is_dir():
            for q in p.iterdir():
                if q.is_file() and q.suffix.lower() in exts and not SKIP_RE.search(q.name):
                    found.append(q)
    return found


def _read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.reader(f))


def _header(path):
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            return next(csv.reader(f), [])
    except (OSError, UnicodeDecodeError):
        return []


def _num(s):
    try:
        return float(str(s).replace("$", "").replace("%", "").replace(",", "").strip())
    except ValueError:
        return None


def _rel(p, folder):
    try:
        return str(Path(p).relative_to(folder))
    except ValueError:
        return str(p)


def find_entries(folder):
    cands = []
    for p in _files(folder):
        h = [c.strip() for c in _header(p)]
        if h[:1] == ["Entry ID"] and "Contest ID" in h:
            name = p.name.lower()
            tier = 0 if "final" in name else 1 if "filled" in name else 2
            cands.append((tier, -p.stat().st_mtime, p))
    cands.sort(key=lambda t: (t[0], t[1]))
    return [c[2] for c in cands]


def find_salaries(folder):
    """DKSalaries*.csv first (top level, then newest). Then any other player list with an ID and Name
    column (for example a projections csv with "DFS ID"), used only to fill names the salary file lacks."""
    dk, other = [], []
    for p in _files(folder):
        if p.name.lower().startswith("dksalaries"):
            dk.append(p)
            continue
        h = [c.strip() for c in _header(p)]
        if "Name" in h and ("DFS ID" in h or ("ID" in h and "Salary" in h)) and h[:1] != ["Entry ID"]:
            other.append(p)
    key = lambda p: (len(p.relative_to(folder).parts), -p.stat().st_mtime)
    return sorted(dk, key=key) + sorted(other, key=key)


def find_standings(folder):
    out = []
    for p in _files(folder, (".csv", ".zip")):
        n = p.name.lower()
        if n.startswith("contest-standings") or "standings" in n:
            out.append(p)
    return sorted(out, key=lambda p: p.name)


def _player_map(salary_files, entries_rows):
    """ID -> {name, team, salary, pos}. Salary files first, then the block on the right of the entries file."""
    m = {}
    for sf in salary_files:
        try:
            rows = _read_rows(sf)
        except (OSError, UnicodeDecodeError):
            continue
        if not rows:
            continue
        h = [c.strip() for c in rows[0]]
        if "ID" not in h and "DFS ID" in h:
            h[h.index("DFS ID")] = "ID"
        if "TeamAbbrev" not in h and "Team" in h:
            h[h.index("Team")] = "TeamAbbrev"
        if "Position" not in h and "Pos" in h:
            h[h.index("Pos")] = "Position"
        if "ID" not in h or "Name" not in h:
            continue
        ix = {k: h.index(k) for k in reversed(h)}  # first occurrence wins
        for r in rows[1:]:
            if len(r) <= ix["ID"]:
                continue
            pid = r[ix["ID"]].strip()
            if pid and pid not in m:
                m[pid] = {"name": r[ix["Name"]].strip(), "team": r[ix["TeamAbbrev"]].strip() if "TeamAbbrev" in ix else "",
                          "salary": _num(r[ix["Salary"]]) if "Salary" in ix else None,
                          "pos": r[ix["Position"]].strip() if "Position" in ix else ""}
    # right-side block in a DKEntries file: a row whose cells contain Position, Name + ID, Name, ID ...
    start = None
    for i, r in enumerate(entries_rows):
        cells = [c.strip() for c in r]
        if "Name + ID" in cells and "ID" in cells:
            start = (i, cells.index("Position"))
            break
    if start:
        i0, c0 = start
        h = [c.strip() for c in entries_rows[i0][c0:]]
        for r in entries_rows[i0 + 1:]:
            seg = r[c0:c0 + len(h)]
            if len(seg) < len(h):
                continue
            d = dict(zip(h, [s.strip() for s in seg]))
            pid = d.get("ID", "")
            if pid and pid not in m:
                m[pid] = {"name": d.get("Name", ""), "team": d.get("TeamAbbrev", ""), "salary": _num(d.get("Salary", "")),
                          "pos": d.get("Position", "")}
    return m


def _entries(path):
    rows = _read_rows(path)
    h = [c.strip() for c in rows[0]]
    out = []
    for r in rows[1:]:
        if not r or not r[0].strip().isdigit():
            continue
        out.append({"entry_id": r[0].strip(), "contest_name": r[1].strip(), "contest_id": r[2].strip(),
                    "entry_fee": r[3].strip(), "ids": [c.strip() for c in r[4:13]]})
    return out, rows


def _norm(name):
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


LINEUP_SPLIT = re.compile(r"(?:^|\s)(QB|RB|WR|TE|FLEX|DST)\s+")


def parse_lineup(s):
    """'QB Dak Prescott RB Jaylen Warren ... DST Steelers' -> [(slot, name), ...]"""
    parts = LINEUP_SPLIT.split(" " + (s or "").strip())
    out = []
    for i in range(1, len(parts) - 1, 2):
        out.append((parts[i], parts[i + 1].strip()))
    return out


def _standings_rows(path):
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist() if n.lower().endswith(".csv")]
            if not names:
                raise ValueError("zip has no csv inside")
            text = z.read(names[0]).decode("utf-8-sig", errors="replace")
        return list(csv.reader(io.StringIO(text)))
    return _read_rows(path)


def parse_standings(path):
    """Returns {entries: {EntryId: {...}}, total, players: {normname: {name, pos, drafted, fpts}}, contest_id}"""
    rows = _standings_rows(path)
    if not rows:
        raise ValueError("empty file")
    h = [c.strip() for c in rows[0]]
    need = ["Rank", "EntryId", "EntryName", "Points", "Lineup"]
    miss = [k for k in need if k not in h]
    if miss:
        raise ValueError("missing columns: " + ", ".join(miss))
    ix = {k: h.index(k) for k in need}
    tr = h.index("TimeRemaining") if "TimeRemaining" in h else None
    pl = {k: h.index(k) for k in ("Player", "Roster Position", "%Drafted", "FPTS") if k in h}
    ents, players = {}, {}
    for r in rows[1:]:
        g = lambda i: r[i].strip() if i is not None and i < len(r) else ""
        eid = g(ix["EntryId"])
        if eid:
            ents[eid] = {"rank": _num(g(ix["Rank"])), "points": _num(g(ix["Points"])), "entry_name": g(ix["EntryName"]),
                         "time_remaining": g(tr), "lineup": g(ix["Lineup"])}
        if "Player" in pl and g(pl["Player"]):
            nm = g(pl["Player"])
            players[_norm(nm)] = {"name": nm, "pos": g(pl.get("Roster Position")), "drafted": g(pl.get("%Drafted")),
                                  "fpts": _num(g(pl.get("FPTS")))}
    m = re.search(r"(\d{6,})", path.name)
    return {"entries": ents, "total": len(ents), "players": players, "contest_id": m.group(1) if m else ""}


def _load_manual(folder):
    p = folder / MANUAL_NAME
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def week_view(n):
    folder = week_dir(n)
    notes = []
    out = {"week": int(n), "folder": str(folder), "exists": folder.is_dir(), "files": {}, "entries": [], "notes": notes}
    if not folder.is_dir():
        notes.append(f"No folder {folder}. Make it and drop the week's DraftKings files in it.")
        return out
    ent_files = find_entries(folder)
    sal_files = find_salaries(folder)
    st_files = find_standings(folder)
    out["files"] = {"entries": _rel(ent_files[0], folder) if ent_files else None,
                    "entries_other": [_rel(p, folder) for p in ent_files[1:]],
                    "salaries": [_rel(p, folder) for p in sal_files],
                    "standings": [_rel(p, folder) for p in st_files],
                    "manual": MANUAL_NAME if (folder / MANUAL_NAME).exists() else None}
    if not ent_files:
        notes.append("No entries file found (a csv starting with the column Entry ID).")
        return out
    ents, raw = _entries(ent_files[0])
    pmap = _player_map(sal_files, raw)
    standings, all_players = {}, {}
    for sf in st_files:
        try:
            s = parse_standings(sf)
        except (OSError, ValueError, zipfile.BadZipFile) as e:
            notes.append(f"Could not read standings file {sf.name}: {e}")
            continue
        for eid, row in s["entries"].items():
            standings[eid] = dict(row, total=s["total"], file=sf.name, contest_id=s["contest_id"])
        all_players.update(s["players"])
    manual = _load_manual(folder)
    team_by_name = {_norm(v["name"]): v["team"] for v in pmap.values() if v.get("name")}
    for e in ents:
        players, sal = [], 0.0
        for slot, pid in zip(SLOTS, e["ids"]):
            p = pmap.get(pid, {})
            if p.get("salary"):
                sal += p["salary"]
            players.append({"slot": slot, "id": pid, "name": p.get("name") or (pid and f"ID {pid}") or "(empty)",
                            "team": p.get("team", ""), "salary": p.get("salary")})
        row = {"entry_id": e["entry_id"], "contest_name": e["contest_name"], "contest_id": e["contest_id"],
               "entry_fee": e["entry_fee"], "players": players, "salary_total": round(sal) if sal else None,
               "built": any(e["ids"]), "status": "BUILT, NOT CONFIRMED ENTERED" if any(e["ids"]) else "EMPTY RESERVATION",
               "result": None, "manual": manual.get(e["entry_id"])}
        st = standings.get(e["entry_id"])
        if st:
            total, rank = st["total"], st["rank"]
            in_lineup = parse_lineup(st["lineup"])
            built_names = {_norm(p["name"]) for p in players}
            res_players = []
            for slot, nm in in_lineup:
                pp = all_players.get(_norm(nm), {})
                team = team_by_name.get(_norm(nm), "")
                res_players.append({"slot": slot, "name": nm, "team": team, "fpts": pp.get("fpts"), "drafted": pp.get("drafted", "")})
            matches = bool(in_lineup) and {_norm(nm) for _, nm in in_lineup} == built_names
            row["result"] = {"points": st["points"], "rank": rank, "total": total,
                             "top_pct": round(rank / total * 100, 1) if rank and total and rank <= total else None,
                             "time_remaining": st["time_remaining"], "file": st["file"], "players": res_players,
                             "lineup_matches_built": matches, "source": "standings file"}
            row["status"] = "IN CONTEST (standings file)"
        elif row["manual"]:
            row["status"] = "IN CONTEST (typed by hand)"
        out["entries"].append(row)
    if not st_files:
        notes.append("No standings file yet. Drop the DraftKings export (contest-standings-*.csv or .zip) in this folder, or type points and place by hand.")
    return out


def save_manual(data):
    """Typed points and place for one entry. Written to <week folder>\\manual-results.json, old copy kept as .bak."""
    try:
        folder = week_dir(int(data.get("week")))
    except (TypeError, ValueError):
        return None, "week must be a number"
    if not folder.is_dir():
        return None, "no folder for that week"
    eid = str(data.get("entry_id") or "").strip()
    ents = find_entries(folder)
    if not ents:
        return None, "no entries file for that week"
    ids = {e["entry_id"] for e in _entries(ents[0])[0]}
    if eid not in ids:
        return None, "that Entry ID is not in this week's entries file"
    rec = {}
    for k in ("points", "rank", "total_entries"):
        v = str(data.get(k) or "").strip()
        if v and _num(v) is None:
            return None, f"{k} must be a number"
        rec[k] = _num(v) if v else None
    if rec["rank"] and rec["total_entries"] and rec["rank"] > rec["total_entries"]:
        return None, "rank cannot be bigger than total entries"
    src = str(data.get("source") or "Zac").strip()
    rec["source"] = src if src in ("Zac", "Jarvis from screenshot") else "Zac"
    rec["time_remaining"] = re.sub(r"[\r\n\t]+", " ", str(data.get("time_remaining") or ""))[:40]
    rec["notes"] = re.sub(r"[\r\n\t]+", " ", str(data.get("notes") or ""))[:300]
    rec["updated"] = time.strftime("%Y-%m-%d %H:%M")
    clear = str(data.get("clear") or "") == "1"
    with _lock:
        p = folder / MANUAL_NAME
        cur = _load_manual(folder)
        if clear:
            cur.pop(eid, None)
        else:
            cur[eid] = rec
        if p.exists():
            (folder / (MANUAL_NAME + ".bak")).write_bytes(p.read_bytes())
        fd, tmp = tempfile.mkstemp(dir=str(folder), suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(cur, f, indent=1)
        os.replace(tmp, p)
    return {"ok": True, "entry_id": eid, "saved": None if clear else rec}, None
