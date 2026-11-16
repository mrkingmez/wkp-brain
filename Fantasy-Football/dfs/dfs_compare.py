"""dfs_compare.py - compare the friend's three lineups with our three (names typed in a small text file).

python dfs_compare.py FRIEND_FILE.txt [--ours D:\\WKP\\data\\dfs-friend\\our_three_lineups_2026-11-15.csv]

FRIEND_FILE format: three lineups, 9 names each, one name per line, a blank line or a line starting with 'Lineup' between them.
DST may be typed as the team nickname ("Packers") or "GB DST". Team abbreviation after a comma is optional ("Josh Allen, BUF").
The file is read as data only. Output is local analysis, not a public file.
"""
import argparse, json, sys
from itertools import combinations
from pathlib import Path
import numpy as np
import pandas as pd
from dfs_common import prepare, qb_gates, lineup_stats, norm, CAP, LOW_OWN

HERE = Path(__file__).parent
OURS = Path(r"D:\WKP\data\dfs-friend\our_three_lineups_2026-11-15.csv")
DST_ALIAS = {"gb": "packers", "no": "saints", "kc": "chiefs", "atl": "falcons", "mia": "dolphins", "ind": "colts", "buf": "bills", "nyj": "jets",
             "car": "panthers", "min": "vikings", "jax": "jaguars", "ten": "titans", "hou": "texans", "cle": "browns"}


def read_friend(path):
    lineups, cur = [], []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        t = raw.strip()
        if not t or t.lower().startswith("lineup") or t.startswith("#"):
            if cur and (not t or t.lower().startswith("lineup")):
                lineups.append(cur); cur = []
            continue
        cur.append(t)
    if cur:
        lineups.append(cur)
    return lineups


def resolve(m, text):
    name = text.split(",")[0].strip()
    team = text.split(",")[1].strip().upper() if "," in text else None
    k = norm(name)
    low = k.replace(" dst", "").replace(" d", "") if k.endswith((" dst", " d")) else k
    low = DST_ALIAS.get(low, low)
    c = m[(m.key == k) | ((m.pos == "DST") & (m.Name.str.lower() == low))]
    if team:
        c = c[c.Team == team]
    if len(c) != 1:
        raise SystemExit(f"cannot resolve '{text}' to exactly one player on the slate ({len(c)} matches)")
    return int(c.iloc[0]["DFS ID"])


def card(label, s, qq):
    q = s["qb"]
    return dict(label=label, salary=s["salary"], proj=round(s["proj"], 1), own_sum=round(s["own_sum"]), own_avg=round(s["own_avg"], 1), pool=s["pool"],
                qb=q.Name, gate="PASS" if qq.gate_pass else "FAIL", stack=s["stack"], bring=s["bring"], sim_avg=round(s["sim_avg"], 1),
                sim_p25=round(s["sim_p25"], 1), sim_p90=round(s["sim_p90"], 1))


def critique(f, o, fs, os_, qqf, qqo):
    parts = []
    if f["qb"] != o["qb"]:
        parts.append(f"QB: friend {f['qb']} (gate {f['gate']}, sim avg QB {fs['qb'].sim_avg:.1f}) vs ours {o['qb']} (gate {o['gate']}, sim avg QB {os_['qb'].sim_avg:.1f}).")
    else:
        parts.append(f"Same QB, {f['qb']}.")
    d = fs["L"][~fs["L"]["DFS ID"].isin(os_["L"]["DFS ID"])]
    e = os_["L"][~os_["L"]["DFS ID"].isin(fs["L"]["DFS ID"])]
    parts.append(f"Own ownership {f['own_avg']} avg vs {o['own_avg']} for ours ({'friend is the more contrarian build' if f['own_avg'] < o['own_avg'] else 'ours is the more contrarian build'}); pool {f['pool']} vs {o['pool']}.")
    parts.append(f"Projection {f['proj']} vs {o['proj']}; sim average {f['sim_avg']} vs {o['sim_avg']}, sim 90th {f['sim_p90']} vs {o['sim_p90']}.")
    if f["bring"] >= 3:
        parts.append("Friend's lineup breaks his own rule (3 or more bring-backs).")
    if f["pool"] < 5:
        parts.append("Friend's lineup is under 5 chalk-pool players, outside his own rule.")
    risky = fs["L"][fs["L"].q_flag]
    if len(risky):
        parts.append("Q players in the friend's lineup: " + ", ".join(risky.Name) + ".")
    return " ".join(parts)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("friend"); ap.add_argument("--ours", default=str(OURS))
    a = ap.parse_args()
    m, X, defs, notes, nqb = prepare()
    st = json.loads((HERE / "dfs_status_2026-11-15.json").read_text(encoding="utf-8"))
    qg = qb_gates(m, {k: v[0] for k, v in st["qb_start"].items()})
    first = Path(a.friend).read_text(encoding="utf-8").splitlines()[0]
    if first.startswith("#") or "FAKE" in Path(a.friend).name.upper():
        print("INPUT NOTE:", first.lstrip("# "))
    fl = read_friend(a.friend)
    if len(fl) != 3 or any(len(x) != 9 for x in fl):
        raise SystemExit(f"need 3 lineups of 9 names; got {[len(x) for x in fl]}")
    ours = pd.read_csv(a.ours)
    L = {}
    for i, names in enumerate(fl, 1):
        L[f"F{i}"] = [resolve(m, n) for n in names]
    for k in ["A", "B", "C"]:
        L[f"O{k}"] = ours[ours.lineup == k].dfs_id.astype(int).tolist()
    S, C = {}, []
    for k, ids in L.items():
        if len(set(ids)) != 9:
            raise SystemExit(f"{k} does not have 9 distinct players")
        S[k] = lineup_stats(m, X, ids)
        qq = qg[qg.Name == S[k]["qb"].Name]
        qq = qq.iloc[0] if len(qq) else pd.Series(dict(gate_pass=False))
        S[k]["qq"] = qq
        c = card(k, S[k], qq)
        c["legal"] = "OK" if S[k]["salary"] <= CAP else "OVER CAP"
        C.append(c)
    pd.set_option("display.width", 250)
    print(pd.DataFrame(C).to_string(index=False))
    print("\nOverlap (players shared of 9):")
    keys = list(L)
    ov = pd.DataFrame(index=keys, columns=keys, dtype=int)
    for x, y in combinations(keys, 2):
        n = len(set(L[x]) & set(L[y])); ov.loc[x, y] = n; ov.loc[y, x] = n
    for x in keys: ov.loc[x, x] = 9
    print(ov.to_string())
    allf = set(sum([L[f"F{i}"] for i in (1, 2, 3)], [])); allo = set(sum([L[f"O{k}"] for k in "ABC"], []))
    nm = lambda ids: ", ".join(m[m["DFS ID"].isin(ids)].sort_values("own", ascending=False).apply(lambda r: f"{r.Name} ({r.own:.0f}%)", axis=1))
    print("\nOnly on the friend's side:", nm(allf - allo) or "none")
    print("Only on our side:", nm(allo - allf) or "none")
    print("On both sides:", nm(allf & allo) or "none")
    print("\nCritique, friend lineup vs our lineup it overlaps most with:")
    for i in (1, 2, 3):
        f = f"F{i}"
        best = max(["OA", "OB", "OC"], key=lambda k: len(set(L[f]) & set(L[k])))
        cf = next(c for c in C if c["label"] == f); co = next(c for c in C if c["label"] == best)
        print(f" {f} vs {best} ({len(set(L[f]) & set(L[best]))} shared): " + critique(cf, co, S[f], S[best], S[f]["qq"], S[best]["qq"]))
    qbs_f = {S[f"F{i}"]["qb"].Name for i in (1, 2, 3)}; qbs_o = {S[f"O{k}"]["qb"].Name for k in "ABC"}
    print(f"\nQB view: friend uses {sorted(qbs_f)}; we use {sorted(qbs_o)}.")
    if qbs_f - qbs_o:
        print("DECISION RULE (QB disagreement): see the Sunday runbook, rule R1.")
    # sim view: probability friend beats ours on total, head to head per pair of best-of
    print("\nSim view (our simulator, same 20,000 draws, correlation kept):")
    for fi in (1, 2, 3):
        for k in "ABC":
            p = float((S[f"F{fi}"]["total"] > S[f"O{k}"]["total"]).mean())
            print(f"   P(F{fi} total > O{k} total) = {p:.2f}")
    best_f = np.max([S[f"F{i}"]["total"] for i in (1, 2, 3)], axis=0); best_o = np.max([S[f"O{k}"]["total"] for k in "ABC"], axis=0)
    print(f"   best-of-three: P(friend's best > ours) = {float((best_f > best_o).mean()):.2f}; mean best-of-three friend {best_f.mean():.1f} vs ours {best_o.mean():.1f}")
    print("   CAUTION: our three were optimized on this same simulator, so the sim favors them by construction. Read the sim view as 'which lineup has the higher sim ceiling', not as evidence ours is better.")
    print("   (DST uses friend-normal draws, not DraftKings DST scoring; probabilities describe the sim, not reality)")


if __name__ == "__main__":
    main()
