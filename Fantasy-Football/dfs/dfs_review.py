"""dfs_review.py - weekly review loop (the friend's step 7). Fills D:\\WKP\\Fantasy-Football\\tracker\\dfs_tracker.csv.

Step 1, before lock (seeds one row per lineup with the projected score):
  python dfs_review.py init --date 2026-11-15 --slate "NFL Early 2026-11-15" [--friend friend_lineups.txt]
Step 2, after the slate, when Zac gives results (all optional except lineup_id and actual_score):
  python dfs_review.py fill --date 2026-11-15 --results results.csv [--ownership dk_lineup_export.csv] [--actuals actuals.csv]

results.csv columns: lineup_id (OA OB OC F1 F2 F3), entry_fee, contest, actual_score, cash_line, finish, profit_loss, notes
--ownership: DraftKings 'Export Lineups to CSV' file from the contest GameCenter (needs columns Player and %Drafted; available 10 days
   after the contest ends, SECONDARY source in Fixes-2026-11-10-DFS.md). Actual ownership is compared with the projected My Own.
--actuals: csv with Name and Actual (DraftKings points per player), e.g. the friend's file once its Actual column is filled.
Low-owned hit = a player under 10 percent projected ownership who scored at least 3x his salary in thousands (the usual DK value bar).
Nothing here enters or submits anything.
"""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from dfs_common import prepare, norm, LOW_OWN
from dfs_compare import read_friend, resolve

TRACK = Path(r"D:\WKP\Fantasy-Football\tracker\dfs_tracker.csv")
OURS = Path(r"D:\WKP\data\dfs-friend\our_three_lineups_2026-11-15.csv")
IDS = Path(r"D:\WKP\data\dfs-friend\lineup_ids_{date}.json")
COLS = ["date", "slate", "lineup_id", "source", "entry_fee", "contest", "projected_score", "actual_score", "cash_line", "finish", "profit_loss",
        "proj_own_avg", "actual_own_avg", "own_proj_vs_actual", "low_owned_hits", "qb_used", "qb_result", "notes",
        "line_label", "lineup_players", "status"]  # last three added 2026-11-13 by the dashboard DFS panel


# Fields the dashboard (or Zac) may have filled in. init must never wipe these.
PROTECT = ["entry_fee", "contest", "actual_score", "cash_line", "finish", "profit_loss", "notes",
           "line_label", "lineup_players", "status"]


def backup_track():
    """Copy the tracker to trackerackups before any write (2026-11-13)."""
    import shutil, time
    if TRACK.exists() and TRACK.stat().st_size > 0:
        d = TRACK.parent / "backups"; d.mkdir(exist_ok=True)
        dst = d / f"dfs_tracker_{time.strftime('%Y%m%d-%H%M%S')}-review.csv"
        shutil.copy2(TRACK, dst)
        return dst


def upsert(df, row, keep=False):
    k = (df.date == row["date"]) & (df.lineup_id == row["lineup_id"])
    if keep and k.any():
        old = df[k].iloc[0].to_dict()
        for f in PROTECT:
            if pd.notna(old.get(f)) and str(old.get(f)) != "":
                row[f] = old[f]
    df = df[~k]
    return pd.concat([df, pd.DataFrame([row])], ignore_index=True)


def load_track():
    return pd.read_csv(TRACK, dtype=str) if TRACK.exists() and TRACK.stat().st_size > 0 else pd.DataFrame(columns=COLS)


def init(a):
    import json
    m, X, *_ = prepare()
    lineups = {}
    o = pd.read_csv(OURS)
    for k in "ABC":
        lineups["O" + k] = o[o.lineup == k].dfs_id.astype(int).tolist()
    if a.friend:
        for i, names in enumerate(read_friend(a.friend), 1):
            lineups[f"F{i}"] = [resolve(m, n) for n in names]
    df = load_track()
    for lid, ids in lineups.items():
        L = m[m["DFS ID"].isin(ids)]
        qb = L[L.pos == "QB"].iloc[0]
        df = upsert(df, dict(date=a.date, slate=a.slate, lineup_id=lid, source="ours" if lid.startswith("O") else "friend",
                             projected_score=round(L.proj.sum(), 1), proj_own_avg=round(L.own.mean(), 1), qb_used=qb.Name,
                             own_proj_vs_actual="; ".join(f"{r.Name}:{r.own:.1f}/" for _, r in L.iterrows())), keep=True)
    IDS.with_name(IDS.name.format(date=a.date)).write_text(json.dumps(lineups))
    backup_track()
    df[COLS].to_csv(TRACK, index=False)
    print(f"seeded {len(lineups)} rows for {a.date} in {TRACK}")


def fill(a):
    import json
    lineups = json.loads(IDS.with_name(IDS.name.format(date=a.date)).read_text())
    m, X, *_ = prepare()
    res = pd.read_csv(a.results)
    own = None
    if a.ownership:
        o = pd.read_csv(a.ownership)
        o["key"] = o.Player.map(norm); o["actual_own"] = o["%Drafted"].astype(str).str.rstrip("%").astype(float)
        own = o.groupby("key").actual_own.first()
    act = None
    if a.actuals:
        t = pd.read_csv(a.actuals); col = "Actual" if "Actual" in t else "actual_points"
        t["key"] = t.Name.map(norm); act = t.groupby("key")[col].first()
    df = load_track()
    for _, r in res.iterrows():
        lid = r.lineup_id; ids = lineups[lid]
        L = m[m["DFS ID"].isin(ids)].copy(); L["key"] = L.Name.map(norm)
        row = df[(df.date == a.date) & (df.lineup_id == lid)].iloc[0].to_dict()
        for c in ["entry_fee", "contest", "actual_score", "cash_line", "finish", "profit_loss", "notes"]:
            if c in r and pd.notna(r[c]): row[c] = r[c]
        if own is not None:
            L["act_own"] = L.key.map(own)
            row["actual_own_avg"] = round(L.act_own.mean(), 1)
            row["own_proj_vs_actual"] = "; ".join(f"{x.Name}:{x.own:.1f}/{x.act_own:.1f}" for _, x in L.iterrows())
        if act is not None:
            L["pts"] = L.key.map(act)
            hits = L[(L.own < LOW_OWN) & (L.pos != "QB") & (L.pts >= 3 * L.Salary / 1000)]
            row["low_owned_hits"] = "; ".join(f"{x.Name} {x.pts:.1f} pts at {x.own:.1f}%" for _, x in hits.iterrows()) or "none"
            qb = L[L.pos == "QB"].iloc[0]
            row["qb_used"] = qb.Name; row["qb_result"] = f"{qb.pts:.1f} pts vs proj {qb.proj:.1f}" if pd.notna(qb.pts) else ""
        df = upsert(df, row)
    backup_track()
    df[COLS].to_csv(TRACK, index=False)
    print(df[df.date == a.date][["lineup_id", "projected_score", "actual_score", "cash_line", "finish", "profit_loss", "qb_used", "qb_result", "low_owned_hits"]].to_string(index=False))
    print("\nOwnership error (projected minus actual, percentage points, all lineup players):")
    if own is not None:
        allp = m[m["DFS ID"].isin(sorted({i for v in lineups.values() for i in v}))].copy(); allp["act"] = allp.Name.map(norm).map(own)
        print(f"  mean absolute error {float((allp.own - allp.act).abs().mean()):.1f} points over {int(allp.act.notna().sum())} players")
    else:
        print("  no ownership file given")


def main():
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    i = sp.add_parser("init"); i.add_argument("--date", required=True); i.add_argument("--slate", required=True); i.add_argument("--friend")
    f = sp.add_parser("fill"); f.add_argument("--date", required=True); f.add_argument("--results", required=True)
    f.add_argument("--ownership"); f.add_argument("--actuals")
    a = ap.parse_args()
    init(a) if a.cmd == "init" else fill(a)


if __name__ == "__main__":
    main()
