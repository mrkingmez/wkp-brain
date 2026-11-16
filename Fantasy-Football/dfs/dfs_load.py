"""dfs_load.py - merge the friend's projections file with the DraftKings salary file.

python dfs_load.py [--proj PATH] [--sal PATH] [--out PATH]

Join: projections 'DFS ID' = salary file 'ID'. Salary-file Status (OUT, IR, Q, D) is the authority.
Drops OUT, IR, D (and the friend's 'O'). Flags Q. Ignores every column that is not in KEEP (extra FanDuel,
Yahoo and other-site columns). Stale ownership: a scratched player's ownership is removed and the remaining
players at that position are scaled so the position total stays the same as in the file (stated in the output).
Friends data is paid, local only: output stays in the dfs-friend data folder.
"""
import argparse
import os
from pathlib import Path
import pandas as pd

D = Path(r"D:\WKP\data\dfs-friend")
PROJ = Path(os.environ.get("DFS_PROJ", D / "NFL_2026-11-15-100pm_DK_Early-Only.csv"))   # set DFS_PROJ / DFS_SAL to point at the 11:30 AM files
SAL = Path(os.environ.get("DFS_SAL", D / "DKSalaries-2026-11-15-early.csv"))
OUT = D / "slate_clean_2026-11-15.csv"
KEEP = ["DFS ID", "Name", "Pos", "Team", "Opp", "Salary", "My Proj", "Value", "My Own", "Saber Team", "Saber Total",
        "dk_points", "dk_25_percentile", "dk_50_percentile", "dk_75_percentile", "dk_85_percentile",
        "dk_95_percentile", "dk_99_percentile", "dk_std"]


def load(proj=PROJ, sal=SAL, verbose=True):
    p = pd.read_csv(proj)
    s = pd.read_csv(sal, encoding="utf-8-sig")
    ignored = [c for c in p.columns if c not in KEEP + ["Status", "Actual", "SS Proj", "Live Proj"]]
    p = p[[c for c in KEEP + ["Status"] if c in p.columns]].rename(columns={"Status": "proj_status"})
    s = s.rename(columns={"ID": "DFS ID", "Status": "sal_status", "Salary": "sal_salary", "Game Info": "game",
                          "Roster Position": "slots", "AvgPointsPerGame": "dk_avg"})
    s["sal_status"] = s.sal_status.fillna("").str.upper()
    m = p.merge(s[["DFS ID", "sal_status", "sal_salary", "game", "slots", "dk_avg", "TeamAbbrev"]], on="DFS ID", how="outer", indicator=True)
    notes = {"ignored_columns": ignored, "unmatched": m[m._merge != "both"][["DFS ID", "Name", "_merge"]].values.tolist()}
    m = m[m._merge == "both"].drop(columns="_merge")
    m["proj_status"] = m.proj_status.fillna("").str.upper()
    notes["salary_mismatch"] = int((m.Salary != m.sal_salary).sum())
    notes["status_disagree"] = m[m.proj_status != m.sal_status][["Name", "Pos", "proj_status", "sal_status"]].values.tolist()
    m["pos1"] = m.Pos.str.split("/").str[0]
    m["status"] = m.sal_status
    scratched = m.status.isin(["OUT", "IR", "D"]) | (m.proj_status == "O")
    m["scratched"] = scratched
    # stale ownership: position totals before and after
    m["own_raw"] = m["My Own"].fillna(0.0)
    tot_before = m.groupby("pos1").own_raw.sum()
    live = m[~scratched]
    tot_live = live.groupby("pos1").own_raw.sum()
    notes["scratched_with_ownership"] = m[scratched & (m.own_raw > 0)][["Name", "Pos", "Team", "status", "proj_status", "own_raw"]].sort_values("own_raw", ascending=False).values.tolist()
    scale = (tot_before / tot_live).to_dict()
    m["own_adj"] = m.own_raw
    for pos1, f in scale.items():
        k = (m.pos1 == pos1) & ~scratched
        m.loc[k, "own_adj"] = m.loc[k, "own_raw"] * f
    m.loc[scratched, "own_adj"] = 0.0
    m["own_stale_flag"] = scratched & (m.own_raw > 0)
    notes["pos_total_before"] = tot_before.round(1).to_dict()
    notes["pos_total_live_raw"] = tot_live.round(1).to_dict()
    notes["scale"] = {k: round(v, 3) for k, v in scale.items()}
    m["q_flag"] = m.status == "Q"
    slate = m[~scratched].copy()
    slate["sim_name"] = slate.Name
    slate = slate.rename(columns={"My Proj": "proj", "My Own": "own_file", "Saber Team": "imp_team", "Saber Total": "game_total"})
    slate["own"] = slate.own_adj
    return slate.reset_index(drop=True), m, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proj", default=str(PROJ)); ap.add_argument("--sal", default=str(SAL)); ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args()
    slate, full, n = load(a.proj, a.sal)
    slate.to_csv(a.out, index=False)
    full.to_csv(Path(a.out).with_name("slate_full_flags_2026-11-15.csv"), index=False)
    print(f"merged rows: {len(full)} | usable (not OUT/IR/D/O): {len(slate)} | Q flagged: {int(slate.q_flag.sum())}")
    print("ignored extra columns:", n["ignored_columns"] or "none")
    print("unmatched IDs:", n["unmatched"] or "none", "| salary mismatches:", n["salary_mismatch"])
    print("status disagreements (friend file vs salary file; salary file wins):", len(n["status_disagree"]))
    for r in n["status_disagree"][:40]: print("   ", r)
    print("\nSTALE OWNERSHIP (scratched players that still carry ownership in the projections file):")
    for r in n["scratched_with_ownership"]: print(f"   {r[0]:<24s} {r[1]:8s} {r[2]:4s} salary-status={r[3] or '-'} friend-status={r[4] or '-'}  own={r[5]:.2f}%")
    print("position ownership totals in file:", n["pos_total_before"])
    print("position totals of live players before rescale:", n["pos_total_live_raw"])
    print("rescale factors applied to live players by position:", n["scale"])
    print("wrote", a.out)


if __name__ == "__main__":
    main()
