r"""espn_snapshot.py -- weekly ESPN college-football snapshot for the pick'em card.
Decision SW-2026-11-11-01 option A.

Builds on Fantasy-Football\tracker\cfb_snapshot.py (imports its Fetcher and parsers,
does not copy them). Adds what that script does not keep:
  * a dated folder per run day:  <data>\cfb\espn\YYYY-MM-DD\HHMM.json
  * a rolling line ledger:       <data>\cfb\espn\line_history.json
    (per game: every distinct spread/total seen, with the time seen; the last
    known line is KEPT after ESPN deletes odds from a finished game)
  * a last-week passing-leader table per team (QB change flag input)
  * a console report of line moves since the previous run

Free, keyless, read-only, 12 calls a run (cap 25), 0.5 s between calls, generic
User-Agent. No key is read or written. Raw data stays on this machine; do not publish it.
NO INJURY DATA exists in this feed.

Run:  <python from LOCAL-PATHS.md> D:\WKP\software\cfb-espn-snapshot\espn_snapshot.py
Options: --back N (default 5, reaches last Saturday)  --ahead N (default 5)  --out DIR  --no-save
"""
import argparse
import json
import os
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "Fantasy-Football", "tracker"))
import cfb_snapshot as base  # noqa: E402

CALL_CAP = 25
MOVE = 1.0



def update_ledger(ledger, games, taken_at):
    """Append a line only when spread or total changed. Never drops a game's history."""
    for g in games:
        o = g.get("odds")
        if not o:
            continue
        key = (base._num(o.get("spread_home")), base._num(o.get("total")))
        e = ledger.setdefault(g["game_id"], {"away": g["away"], "home": g["home"], "kickoff": g["kickoff"],
                                             "open_spread_home": base._num(o.get("open_spread_home")),
                                             "open_total": base._num(o.get("open_total")), "history": []})
        if not isinstance(e.get("history"), list):
            continue
        if not e["history"] or (e["history"][-1]["spread_home"], e["history"][-1]["total"]) != key:
            e["history"].append({"seen": taken_at, "spread_home": key[0], "total": key[1],
                                 "provider": o.get("provider"), "state": g["state"]})
    return ledger


def ledger_moves(ledger, game_ids=None, threshold=MOVE):
    """Games whose spread or total moved >= threshold from open (or first seen) to latest."""
    out = []
    for gid, e in ledger.items():
        if game_ids is not None and gid not in game_ids:
            continue
        if not isinstance(e, dict) or not isinstance(e.get("history"), list):
            continue
        h = e["history"]
        if not h:
            continue
        for k, op, label in (("spread_home", e.get("open_spread_home"), "spread (home fav +)"),
                             ("total", e.get("open_total"), "total")):
            first = base._num(op) if op is not None else h[0].get(k)
            last = h[-1].get(k)
            if isinstance(first, (int, float)) and isinstance(last, (int, float)) and first is not None and last is not None and abs(last - first) >= threshold:
                out.append({"game": f'{e["away"]} at {e["home"]}', "kind": label,
                            "from": first, "to": last, "move": round(last - first, 1)})
    return out


def pass_leaders(responses):
    """Team abbreviation -> passing leader of its last finished game in this pull. ESPN gives ONE game-wide
    leader per category (with a team id), so only the team whose passer led the game is listed. Partial by design."""
    out = {}
    for data in responses:
        for e in (data or {}).get("events", []):
            try:
                comp = e["competitions"][0]
                if comp["status"]["type"]["state"] != "post":
                    continue
                abbr = {c["team"]["id"]: c["team"].get("abbreviation") for c in comp["competitors"]}
                for cat in comp.get("leaders") or []:
                    if cat.get("name") != "passingYards" or not cat.get("leaders"):
                        continue
                    x = cat["leaders"][0]
                    team = abbr.get((x.get("team") or {}).get("id"))
                    if team:
                        out[team] = {"player": x["athlete"].get("displayName"), "line": x.get("displayValue"),
                                     "kickoff": e.get("date")}
            except (KeyError, IndexError, TypeError):
                continue
    return out


def run(fetcher, today, back, ahead, out_dir, save=True, now=None):
    now = now or datetime.now()
    snap = base.build_snapshot(fetcher, today, back, ahead, now=now)
    snap["source"] = "ESPN site.api.espn.com college-football (unofficial, keyless), cfb-espn-snapshot"
    snap["pass_leaders"] = pass_leaders(v for k, v in fetcher.cache.items() if k[0] == base.SCOREBOARD)
    if not snap["games"]:
        return snap, None, [], 1
    ledger_path = os.path.join(out_dir, "line_history.json")
    ledger = {}
    if os.path.exists(ledger_path):
        try:
            with open(ledger_path, encoding="utf-8") as f:
                ledger = json.load(f)
            if not isinstance(ledger, dict):
                raise ValueError("not an object")
        except (OSError, ValueError):
            ledger = {}
            snap["not_retrieved"].append("line_history.json unreadable, started a new ledger (old file kept as .corrupt)")
            if save:
                os.replace(ledger_path, ledger_path + ".corrupt-" + now.strftime("%Y%m%d%H%M"))
    update_ledger(ledger, snap["games"], snap["taken_at"])
    path = None
    if save:
        day_dir = os.path.join(out_dir, now.strftime("%Y-%m-%d"))
        os.makedirs(day_dir, exist_ok=True)
        path = os.path.join(day_dir, now.strftime("%H%M") + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(snap, f, indent=1)
        tmp = ledger_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(ledger, f, indent=1)
        os.replace(tmp, ledger_path)
    return snap, path, ledger_moves(ledger, {g["game_id"] for g in snap["games"]}), 0


def report(snap, path, moves):
    up = [g for g in snap["games"] if g["state"] == "pre"]
    odds = [g for g in snap["games"] if g.get("odds")]
    L = ["ESPN CFB SNAPSHOT " + snap["taken_at"], base.NO_INJURY_HEADER, "",
         f'Games {len(snap["games"])}, upcoming {len(up)}, with a line {len(odds)}, '
         f'calls {snap["calls_made"]}. Saved: {path or "not saved"}']
    for p in snap["rankings"][:2]:
        L.append(f'{p["poll"]} top 5: ' + ", ".join(f'{r["rank"]} {r["team"]}' for r in p["ranks"][:5]))
    L.append(f'Passing leaders kept for {len(snap["pass_leaders"])} teams (QB change flag input).')
    L.append(f"Line moves, open to latest, {MOVE:g}+ points: " + ("none" if not moves else ""))
    L += [f'  {m["game"]}: {m["kind"]} {m["from"]:+g} -> {m["to"]:+g} ({m["move"]:+g})' for m in moves]
    if snap["not_retrieved"]:
        L += ["NOT RETRIEVED:"] + ["  - " + m for m in snap["not_retrieved"]]
    return "\n".join(L)


def main(argv=None, fetcher=None, today=None, now=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--back", type=int, default=5)
    ap.add_argument("--ahead", type=int, default=5)
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-save", action="store_true")
    a = ap.parse_args(argv)
    now = now or datetime.now()
    today = today or now.date()
    out_dir = a.out or os.path.join(os.environ.get("CFB_DATA_DIR") or os.path.join(REPO, "data", "cfb"), "espn")
    fetcher = fetcher or base.Fetcher(cap=CALL_CAP)
    snap, path, moves, rc = run(fetcher, today, a.back, a.ahead, out_dir, not a.no_save, now)
    if rc:
        print("Nothing retrieved, nothing saved.")
        for m in snap["not_retrieved"]:
            print("NOT RETRIEVED: " + m)
        return rc
    print(report(snap, path, moves))
    return 0


if __name__ == "__main__":
    sys.exit(main())
