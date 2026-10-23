"""Does scheme information (personnel, formation, motion, play action, box count, coverage, blitz) predict play outcomes beyond the basics?

Joins nflverse pbp with pbp_participation (2023-2025) and ftn_charting. Trains on 2023-2024, tests on 2025.
  A: situation only (down, distance, field position, score, time, shotgun, no huddle)
  B: A + offense scheme (personnel group, formation, motion, play action, screen, RPO, backfield size)
  C: B + defense scheme (defenders in box, pass rushers, blitzers, man/zone, coverage type)
Reports pass completion log-loss, pass yards RMSE and run yards RMSE for each set, on held-out plays.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier as HGC
from sklearn.ensemble import HistGradientBoostingRegressor as HGR
from sklearn.metrics import log_loss, mean_squared_error

PBP = r"D:\WKP\data\nfl\pbp\play_by_play_%d.parquet"
PART = r"D:\WKP\data\nfl\pbp_participation\pbp_participation_%d.parquet"
FTN = r"D:\WKP\data\nfl\ftn_charting\ftn_charting_%d.parquet"
BASE = ["down", "ydstogo", "yardline_100", "score_differential", "half_seconds_remaining", "qtr", "shotgun", "no_huddle"]


def pers_group(s):
    """'1 C, 2 G, 1 QB, 1 RB, 2 T, 1 TE, 3 WR' -> '11' style (RB+TE count), tagged FB if present."""
    if not isinstance(s, str):
        return "na"
    d = {}
    for part in s.split(","):
        n, pos = part.strip().split(" ", 1)
        d[pos] = int(n)
    return f"{d.get('RB', 0) + d.get('FB', 0)}{d.get('TE', 0)}"


def load(year):
    p = pd.read_parquet(PBP % year, columns=["game_id", "play_id", "season", "week", "play_type", "complete_pass", "sack", "yards_gained",
                                              "interception", "qb_kneel", "qb_spike"] + BASE)
    q = pd.read_parquet(PART % year, columns=["nflverse_game_id", "play_id", "offense_formation", "offense_personnel", "defenders_in_box",
                                                "number_of_pass_rushers", "defense_man_zone_type", "defense_coverage_type"])
    f = pd.read_parquet(FTN % year, columns=["nflverse_game_id", "nflverse_play_id", "n_offense_backfield", "is_motion", "is_play_action",
                                              "is_screen_pass", "is_rpo", "n_blitzers"])
    d = p.merge(q.rename(columns={"nflverse_game_id": "game_id"}), on=["game_id", "play_id"], how="left") \
         .merge(f.rename(columns={"nflverse_game_id": "game_id", "nflverse_play_id": "play_id"}), on=["game_id", "play_id"], how="left")
    d["pers"] = d.offense_personnel.map(pers_group)
    return d


def encode(d, cols_cat):
    X = d.copy()
    for c in cols_cat:
        X[c] = X[c].astype("category")
    return X


def run(label, train, test, target, kind, feats, cats):
    Xtr, Xte = encode(train[feats], cats), encode(test[feats], cats)
    for c in cats:
        Xte[c] = pd.Categorical(Xte[c], categories=Xtr[c].cat.categories)
    if kind == "clf":
        m = HGC(max_iter=200, learning_rate=0.06, categorical_features="from_dtype", random_state=0).fit(Xtr, train[target])
        return log_loss(test[target], m.predict_proba(Xte)[:, 1])
    m = HGR(max_iter=200, learning_rate=0.06, categorical_features="from_dtype", random_state=0).fit(Xtr, train[target])
    return float(np.sqrt(mean_squared_error(test[target], m.predict(Xte))))


def main():
    d = pd.concat([load(y) for y in (2023, 2024, 2025)], ignore_index=True)
    d = d[d.down.notna() & d.score_differential.notna() & (d.qb_kneel != 1) & (d.qb_spike != 1)]
    for c in ("shotgun", "no_huddle"):
        d[c] = d[c].fillna(0)
    for c in ("is_motion", "is_play_action", "is_screen_pass", "is_rpo"):
        d[c] = d[c].fillna(False).astype(float)
    d["man"] = (d.defense_man_zone_type == "MAN_COVERAGE").astype(float)
    d["pers"] = d.pers.fillna("na")
    d["offense_formation"] = d.offense_formation.fillna("na")
    d["defense_coverage_type"] = d.defense_coverage_type.fillna("na")
    off = ["pers", "offense_formation", "is_motion", "is_play_action", "is_screen_pass", "is_rpo", "n_offense_backfield"]
    dfn = ["defenders_in_box", "number_of_pass_rushers", "n_blitzers", "man", "defense_coverage_type"]
    cats_o, cats_d = ["pers", "offense_formation"], ["defense_coverage_type"]
    tr, te = d[d.season < 2025], d[d.season == 2025]
    for kind_name, mask, target, kind in (
            ("PASS completion (log-loss, lower is better)", lambda x: (x.play_type == "pass") & (x.sack != 1), "complete_pass", "clf"),
            ("PASS yards (RMSE)", lambda x: (x.play_type == "pass") & (x.sack != 1), "yards_gained", "reg"),
            ("RUN yards (RMSE)", lambda x: (x.play_type == "run"), "yards_gained", "reg")):
        a, b = tr[mask(tr)], te[mask(te)]
        r = {}
        r["A situation"] = run("A", a, b, target, kind, BASE, [])
        r["B + offense scheme"] = run("B", a, b, target, kind, BASE + off, cats_o)
        r["C + defense scheme"] = run("C", a, b, target, kind, BASE + off + dfn, cats_o + cats_d)
        print(f"\n{kind_name}: train {len(a)} plays (2023-24), test {len(b)} plays (2025)")
        for k, v in r.items():
            print(f"   {k:22s} {v:.4f}")


if __name__ == "__main__":
    main()
