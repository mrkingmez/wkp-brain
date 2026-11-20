"""dk_validate.py - check a filled DraftKings entries/upload CSV before Zac uploads it.

python dk_validate.py --filled FILE --friend FRIEND_CSV --slate SLATE_JSON [--dk-salaries DKSalaries.csv] [--template TEMPLATE_CSV]
  (own-numbers mode: pass the reference_pool.csv that dk_gpp.py --own writes in its outdir as --friend)

Checks (every lineup row):
  1. 9 players, slot order QB RB RB WR WR WR TE FLEX DST, each player legal for his slot (FLEX = RB/WR/TE)
  2. no player twice in one lineup
  3. salary total <= 50,000
  4. no two lineups identical (same 9 players)
  5. every player's team is on the early slate list and not on the excluded (international) list
  6. every player ID is in the friend's file, in the DK salary file (if given) and in the template's player list (if the template has one)
  7. no player marked O / OUT / D / IR in the friend's file or the DK salary file
  8. entry rows: Entry ID, Contest ID present; total entry fees reported
Reads data only. Never uploads or enters anything. DK files stay in D:\\Draft Kings.
"""
import argparse, csv, itertools, json, re
import numpy as np
from pathlib import Path
import pandas as pd

SLOTS = ["QB", "RB", "RB", "WR", "WR", "WR", "TE", "FLEX", "DST"]
CAP = 50000
BAD_STATUS = {"O", "OUT", "D", "IR", "DOUBTFUL"}


def parse_id(cell):
    """Accepts '44871008' or 'Josh Allen (44871008)'."""
    s = str(cell).strip()
    m = re.search(r"\((\d+)\)\s*$", s)
    if m:
        return int(m.group(1))
    return int(float(s)) if re.fullmatch(r"\d+(\.0)?", s) else None


def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.reader(f))


def template_pool(rows):
    """DK's edit-entries download sometimes carries the player list to the right of the entries. Find it if present."""
    for r in rows:
        if "Name + ID" in r and "ID" in r:
            c_id = r.index("ID")
            ids = set()
            for rr in rows[rows.index(r) + 1:]:
                if len(rr) > c_id and re.fullmatch(r"\d+", rr[c_id].strip() or "x"):
                    ids.add(int(rr[c_id]))
            return ids
    return None


def lineup_rows(rows):
    """Returns (header, list of (row_index, entry_id_or_None, contest_id, fee, [9 ids or None])."""
    hdr = rows[0]
    if "QB" not in hdr:
        raise SystemExit("no QB column in header: not a DK classic entries/upload file")
    q = hdr.index("QB")
    if [h.strip() for h in hdr[q:q + 9]] != SLOTS:
        raise SystemExit(f"slot header is {hdr[q:q + 9]}, expected {SLOTS}")
    has_entry = "Entry ID" in hdr
    out = []
    for i, r in enumerate(rows[1:], start=1):
        if has_entry:
            if not r or not re.fullmatch(r"\d+", r[0].strip() or "x"):
                continue
            eid, cid, fee = r[0].strip(), r[hdr.index("Contest ID")].strip(), r[hdr.index("Entry Fee")].strip()
        else:
            if len(r) < q + 9 or not any(c.strip() for c in r[q:q + 9]):
                continue
            eid = cid = fee = None
        out.append((i, eid, cid, fee, [parse_id(c) if c.strip() else None for c in r[q:q + 9]]))
    return hdr, out


def validate(filled, friend, slate_json, dk_salaries=None, template=None, quiet=False):
    rows = read_rows(filled)
    hdr, lus = lineup_rows(rows)
    p = pd.read_csv(friend)
    p["pos1"] = p.Pos.str.split("/").str[0]
    info = p.set_index("DFS ID")
    sl = json.loads(Path(slate_json).read_text(encoding="utf-8"))
    early, excl = set(sl["early_teams"]), set(sl.get("excluded_teams", []))
    dk = None
    if dk_salaries:
        dk = pd.read_csv(dk_salaries, encoding="utf-8-sig").set_index("ID")
    tpool = template_pool(read_rows(template)) if template else template_pool(rows)
    problems, lines, seen = [], [], {}
    fees = 0.0
    for n, (ri, eid, cid, fee, ids) in enumerate(lus, start=1):
        tag = f"row {ri}" + (f" entry {eid}" if eid else "")
        if eid is not None and (not eid or not cid):
            problems.append(f"{tag}: missing Entry ID or Contest ID")
        if fee:
            try:
                fees += float(fee.replace("$", "").replace(",", ""))
            except ValueError:
                problems.append(f"{tag}: entry fee '{fee}' not readable")
        if any(i is None for i in ids):
            problems.append(f"{tag}: blank or unreadable player cell"); continue
        if len(set(ids)) != 9:
            problems.append(f"{tag}: same player twice")
        sal = 0
        for slot, pid in zip(SLOTS, ids):
            if pid not in info.index:
                problems.append(f"{tag}: ID {pid} not in the reference file"); continue
            r = info.loc[pid]
            ok = r.pos1 in ("RB", "WR", "TE") if slot == "FLEX" else r.pos1 == slot
            if not ok:
                problems.append(f"{tag}: {r.Name} ({r.pos1}) illegal in {slot}")
            if r.Team not in early:
                problems.append(f"{tag}: {r.Name} team {r.Team} is NOT on the early slate")
            if r.Team in excl:
                problems.append(f"{tag}: {r.Name} team {r.Team} is in an excluded (international) game")
            if str(r.Status).upper() in BAD_STATUS:
                problems.append(f"{tag}: {r.Name} is marked {r.Status} in the reference file")
            if dk is not None:
                if pid not in dk.index:
                    problems.append(f"{tag}: ID {pid} ({r.Name}) not in the DK salary file")
                elif str(dk.loc[pid, "Status"]).upper() in BAD_STATUS:
                    problems.append(f"{tag}: {r.Name} is marked {dk.loc[pid, 'Status']} in the DK salary file")
            if tpool is not None and pid not in tpool:
                problems.append(f"{tag}: ID {pid} ({r.Name}) not in the template's player list")
            sal += int(r.Salary)
        if sal > CAP:
            problems.append(f"{tag}: salary {sal:,} over the 50,000 cap")
        key = frozenset(ids)
        if key in seen:
            problems.append(f"{tag}: identical to lineup on row {seen[key]}")
        seen[key] = ri
        lines.append(f"  lineup {n} ({tag}): salary {sal:,}, left {CAP - sal:,}")
    # 2026-11-19: portfolio rules from the friend's process, checked independently of the builder
    full = [ids for (_, _, _, _, ids) in lus if all(i is not None for i in ids) and all(i in info.index for i in ids)]
    if full:
        expo = pd.Series([i for ids in full for i in ids]).value_counts()
        cap = 4 if len(full) >= 7 else max(1, int(np.ceil(len(full) * 4 / 7)))
        for pid, c in expo[expo > cap].items():
            problems.append(f"exposure: {info.loc[pid, 'Name']} is in {c} of {len(full)} lineups (cap {cap})")
        qbs = pd.Series([next(i for i in ids if info.loc[i, "pos1"] == "QB") for ids in full if any(info.loc[i, "pos1"] == "QB" for i in ids)]).value_counts()
        for pid, c in qbs[qbs > 2].items():
            problems.append(f"QB cap: {info.loc[pid, 'Name']} is the QB in {c} lineups (cap 2)")
        for a_, b_ in itertools.combinations(range(len(full)), 2):
            sh = len(set(full[a_]) & set(full[b_]))
            if sh > 5:
                problems.append(f"overlap: lineups {a_ + 1} and {b_ + 1} share {sh} players (cap 5)")
        opp = {}
        if dk is not None and "Game Info" in dk:
            for _, r in dk.drop_duplicates("TeamAbbrev").iterrows():
                m = re.match(r"(\w+)@(\w+)", str(r["Game Info"]))
                if m:
                    opp[r.TeamAbbrev] = m.group(2) if m.group(1) == r.TeamAbbrev else m.group(1)
        for n_, ids in enumerate(full, 1):
            q = [i for i in ids if info.loc[i, "pos1"] == "QB"]
            if not q:
                continue
            q = q[0]
            if int(info.loc[q, "Salary"]) < 5000:
                problems.append(f"lineup {n_}: QB {info.loc[q, 'Name']} costs under $5,000")
            if opp:
                bb = [i for i in ids if info.loc[i, "pos1"] in ("RB", "WR", "TE") and info.loc[i, "Team"] == opp.get(info.loc[q, "Team"])]
                if len(bb) > 2:
                    problems.append(f"lineup {n_}: {len(bb)} bring-backs (cap 2)")
        lines.append(f"  portfolio rules checked: exposure cap {cap}, QB in at most 2, overlap at most 5, QB salary >= 5,000"
                     + (", bring-backs at most 2" if opp else " (bring-backs not checked: no DK salary file)")
                     + ". Not checked here: the required bring-back in high-total games and the chalk-pool minimum (the build report shows those).")
    rep = [f"VALIDATION of {Path(filled).name}",
           f"  lineups found: {len(lus)} | entry fees total: ${fees:,.2f}" if any(l[1] for l in lus) else f"  lineups found: {len(lus)} (upload file, no entry IDs)",
           f"  ID sources checked: reference file (friend file or own-mode reference_pool.csv)" + (", DK salary file" if dk is not None else "") + (", template player list" if tpool is not None else " (template has no player list)")]
    rep += lines
    rep.append("  RESULT: PASS, no problems found" if not problems else f"  RESULT: FAIL, {len(problems)} problem(s):")
    rep += [f"    - {x}" for x in problems]
    if not quiet:
        print("\n".join(rep))
    return not problems, rep


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--filled", required=True); ap.add_argument("--friend", required=True); ap.add_argument("--slate", required=True)
    ap.add_argument("--dk-salaries"); ap.add_argument("--template")
    a = ap.parse_args()
    ok, _ = validate(a.filled, a.friend, a.slate, a.dk_salaries, a.template)
    raise SystemExit(0 if ok else 1)

