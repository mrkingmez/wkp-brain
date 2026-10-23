"""Offensive-line layer for the simulator: availability, team OL strength, and data-fitted effect sizes.

python ol_model.py fit [--train-before 202506]     # fit effects on games BEFORE the cutoff, write ol_coefs.json
python ol_model.py week 2026 7                      # Week N OL starters, who is missing (needs injuries_<season>_wk<week>.csv)

Data (all nflverse, cached under D:\\WKP\\data\\nfl): snap_counts (OL offense snaps per game), play_by_play
(sacks, QB hits, yards, EPA), pfr_advstats pass (pressures allowed) and rush (yards before contact).

Definitions
  usual OL5 for a team-game = the 5 linemen (T, G, C, OL) with the most offensive snap share over the team's previous
      6 games (needs 3 prior games). His weight w = that average snap share.
  miss (ex-ante) = sum of w over usual OL5 who played 0 snaps in this game / sum of w. A lineman who did not dress is
      known before kickoff, so the backtest can use it without peeking at in-game injuries.
  The effect sizes are slopes on `miss` from a fixed-effects regression: team-season and opposing-defense-season
      dummies absorb QB, scheme and opponent quality, so the slope is the OL-absence effect only.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(r"D:\WKP\data\nfl")
OUT = Path(r"D:\WKP\data\ff-simulator")
COEF_FILE = OUT / "ol_coefs.json"
OL_POS = {"T", "G", "C", "OL"}
YEARS = (2023, 2024, 2025, 2026)
PRIOR = 6
MIN_PRIOR = 3
OUT_PCT = 0.0         # "did not play" = zero offensive snaps


def load_snaps():
    fr = [pd.read_parquet(DATA / "snap_counts" / f"snap_counts_{y}.parquet") for y in YEARS
          if (DATA / "snap_counts" / f"snap_counts_{y}.parquet").exists()]
    s = pd.concat(fr, ignore_index=True)
    s = s[(s.game_type == "REG")].copy()
    s["order"] = s.season * 100 + s.week
    return s


def ol_games(s):
    """Per OL player-game: team, order, offense_pct, snaps. Returns also the list of team games in order."""
    o = s[s.position.isin(OL_POS)].copy()
    o["offense_pct"] = o.offense_pct.fillna(0)
    return o


def usual_and_missing(s):
    """One row per team-game with miss (ex-ante), lost (snap based), n_out, and the usual OL5 names."""
    o = ol_games(s)
    games = (s.groupby(["team", "game_id", "season", "week", "order", "opponent"]).size().reset_index()[
        ["team", "game_id", "season", "week", "order", "opponent"]].sort_values(["team", "order"]))
    rows = []
    for team, g in games.groupby("team"):
        g = g.reset_index(drop=True)
        ot = o[o.team == team]
        by_game = {gid: x for gid, x in ot.groupby("game_id")}
        for k in range(len(g)):
            if k < MIN_PRIOR:
                continue
            prior = g.iloc[max(0, k - PRIOR):k].game_id.tolist()
            hist = pd.concat([by_game[x] for x in prior if x in by_game])
            avg = hist.groupby("player").offense_pct.sum() / len(prior)
            top = avg.sort_values(ascending=False).head(5)
            cur = by_game.get(g.game_id[k])
            curp = cur.set_index("player").offense_pct if cur is not None else pd.Series(dtype=float)
            w = top.values
            pc = np.array([curp.get(n, 0.0) for n in top.index])
            out = pc <= OUT_PCT
            rows.append(dict(team=team, game_id=g.game_id[k], season=g.season[k], week=g.week[k], order=g.order[k],
                             opponent=g.opponent[k], miss=float((w * out).sum() / w.sum()), n_out=int(out.sum()),
                             lost=float(np.clip(1 - pc / np.maximum(w, 1e-6), 0, 1).dot(w) / w.sum()),
                             usual=";".join(top.index), out_names=";".join(top.index[out])))
    return pd.DataFrame(rows)


def team_game_outcomes():
    """Sacks, pressure, pass/rush efficiency per offense team-game from pbp + pfr."""
    fr = []
    for y in YEARS:
        f = DATA / "pbp" / f"play_by_play_{y}.parquet"
        if f.exists():
            fr.append(pd.read_parquet(f, columns=["season", "week", "season_type", "game_id", "posteam", "defteam", "qb_dropback",
                                                  "sack", "qb_hit", "epa", "pass_attempt", "rush_attempt", "yards_gained",
                                                  "qb_scramble", "play_type", "success", "air_yards", "complete_pass"]))
    p = pd.concat(fr, ignore_index=True)
    p = p[(p.season_type == "REG") & p.posteam.notna() & p.play_type.isin(["pass", "run"])]
    p["is_db"] = (p.qb_dropback == 1)
    p["is_rush"] = (p.rush_attempt == 1) & (p.qb_scramble != 1)
    g = p.groupby(["game_id", "posteam", "defteam"])
    d = pd.DataFrame({
        "db": g.is_db.sum(), "sacks": g.sack.sum(), "hits": g.qb_hit.sum(),
        "pass_epa": p[p.is_db].groupby(["game_id", "posteam", "defteam"]).epa.mean(),
        "att": g.pass_attempt.sum(),
        "ypa": p[p.pass_attempt == 1].groupby(["game_id", "posteam", "defteam"]).yards_gained.mean(),
        "carries": g.is_rush.sum(),
        "ypc": p[p.is_rush].groupby(["game_id", "posteam", "defteam"]).yards_gained.mean(),
        "rush_epa": p[p.is_rush].groupby(["game_id", "posteam", "defteam"]).epa.mean(),
        "rush_succ": p[p.is_rush].groupby(["game_id", "posteam", "defteam"]).success.mean(),
    }).reset_index()
    d["sack_rate"] = d.sacks / d.db
    d["hit_rate"] = d.hits / d.db
    # pfr pressure + yards before contact
    pr, rr = [], []
    for y in YEARS:
        a = DATA / "pfr_advstats" / f"advstats_week_pass_{y}.parquet"
        b = DATA / "pfr_advstats" / f"advstats_week_rush_{y}.parquet"
        if a.exists():
            x = pd.read_parquet(a)
            pr.append(x.groupby(["game_id", "team"])[["times_pressured", "times_hurried", "times_hit"]].sum().reset_index())
        if b.exists():
            x = pd.read_parquet(b)
            x = x.assign(ybc=x.rushing_yards_before_contact)
            rr.append(x.groupby(["game_id", "team"])[["ybc", "carries"]].sum().reset_index().rename(columns={"carries": "pfr_car"}))
    if pr:
        pr = pd.concat(pr)
        d = d.merge(pr.rename(columns={"team": "posteam"}), on=["game_id", "posteam"], how="left")
        d["press_rate"] = d.times_pressured / d.db
    if rr:
        rr = pd.concat(rr)
        d = d.merge(rr.rename(columns={"team": "posteam"}), on=["game_id", "posteam"], how="left")
        d["ybc_att"] = d.ybc / d.pfr_car
    return d


def build_panel():
    s = load_snaps()
    av = usual_and_missing(s)
    out = team_game_outcomes()
    # snap_counts uses game_id like 2026_01_ARI_LAC; nflverse pbp game_id has the same format
    d = av.merge(out.rename(columns={"posteam": "team", "defteam": "def"}), on=["game_id", "team"], how="inner")
    d["ts"] = d.team + d.season.astype(str)
    d["ds"] = d["def"] + d.season.astype(str)
    return d


def wls_fe(d, y, wcol, x="miss", fe=("ts", "ds")):
    """Weighted least squares of y on x plus team-season and opposing-defense-season dummies (ridge-stabilised)."""
    z = d.dropna(subset=[y, x, wcol]).copy()
    z = z[z[wcol] > 0]
    cols = []
    for f in fe:
        cols.append(pd.get_dummies(z[f], dtype=float))
    X = np.hstack([z[[x]].values.astype(float)] + [c.values for c in cols])
    w = np.sqrt(z[wcol].values.astype(float))
    Xw, yw = X * w[:, None], z[y].values.astype(float) * w
    lam = np.r_[0.0, np.full(X.shape[1] - 1, 1e-3)]
    A = Xw.T @ Xw + np.diag(lam)
    beta = np.linalg.solve(A, Xw.T @ yw)
    resid = yw - Xw @ beta
    dof = max(len(z) - np.linalg.matrix_rank(Xw), 1)
    s2 = (resid ** 2).sum() / dof
    cov = s2 * np.linalg.pinv(A)
    return float(beta[0]), float(np.sqrt(cov[0, 0])), len(z), float((z[x] > 0).sum())


def fit(train_before):
    d = build_panel()
    tr = d[d.order < train_before]
    res = {}
    spec = [("sack_rate", "db"), ("hit_rate", "db"), ("press_rate", "db"), ("pass_epa", "db"), ("ypa", "att"),
            ("ypc", "carries"), ("rush_epa", "carries"), ("rush_succ", "carries"), ("ybc_att", "carries")]
    print(f"train games {len(tr)} (orders < {train_before}); games with >=1 usual OL starter out: {(tr.n_out > 0).sum()}, "
          f"2+ out: {(tr.n_out > 1).sum()}")
    for y, w in spec:
        if y not in tr:
            continue
        b, se, n, nz = wls_fe(tr, y, w)
        mean = float(np.average(tr[y].dropna(), weights=tr.loc[tr[y].notna(), w].clip(lower=1)))
        res[y] = dict(beta=b, se=se, t=b / se if se else 0, n=n, n_missing_games=nz, league_mean=mean)
        print(f"{y:10s} slope per full OL absence {b:+.4f} (se {se:.4f}, t {b / se:+.2f})  = {b / 5:+.4f} per starter out | "
              f"league mean {mean:.3f} | n {n}")
    res["_meta"] = dict(train_before=train_before, trained_on=int(len(tr)))
    json.dump(res, open(COEF_FILE, "w"), indent=1)
    d.to_csv(OUT / "ol_panel.csv", index=False)
    print("saved", COEF_FILE)
    return d, res


def team_index(d, as_of):
    """OL strength index per team from games before `as_of` (this season + last), opponent-adjusted by fixed effects.
    Components: sack rate, pressure rate, rush EPA, yards before contact. z-scored; positive = better line.
    Caveat: sack and pressure rate also carry the QB (scrambling, time to throw), which team-season dummies cannot separate."""
    z = d[(d.order < as_of) & (d.order >= as_of - 100 - (as_of % 100) + 0)].copy()
    out = {}
    for y, sign in (("sack_rate", -1), ("press_rate", -1), ("rush_epa", 1), ("ybc_att", 1)):
        if y not in z:
            continue
        w = "db" if y in ("sack_rate", "press_rate") else "carries"
        g = z.dropna(subset=[y]).groupby("team").apply(lambda x: np.average(x[y], weights=x[w].clip(lower=1)), include_groups=False)
        out[y] = sign * (g - g.mean()) / g.std()
    return pd.DataFrame(out)


def week_report(season, week):
    s = load_snaps()
    o = ol_games(s)
    inj = pd.read_csv(OUT / f"injuries_{season}_wk{week}.csv")
    ov = json.load(open(OUT / f"overrides_{season}_wk{week}.json")) if (OUT / f"overrides_{season}_wk{week}.json").exists() else {"players": []}
    ovd = {(p["name"], p["team"]): p for p in ov["players"]}
    sched = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    wk = sched[(sched.season == season) & (sched.week == week)]
    teams = sorted(set(wk.home_team) | set(wk.away_team))
    rows = []
    last_order = season * 100 + week
    for t in teams:
        g = o[(o.team == t) & (o.order < last_order)]
        games = sorted(g.order.unique())[-PRIOR:]
        gg = g[g.order.isin(games)]
        tot_games = len(games)
        # games started proxy: games with >= 50% offensive snaps this season
        ss = o[(o.team == t) & (o.season == season) & (o.order < last_order)]
        started = ss[ss.offense_pct >= 0.5].groupby("player").size()
        avg = (gg.groupby("player").offense_pct.sum() / max(tot_games, 1)).sort_values(ascending=False)
        top = avg.head(7)
        for rank, (name, pct) in enumerate(top.items(), 1):
            row = inj[(inj.team == t) & (inj.player.map(lambda x: x.lower().replace(".", "").replace(" jr", "")) ==
                                          name.lower().replace(".", "").replace(" jr", ""))]
            cat, src, asof = ("not in table", "", "")
            if len(row):
                cat, src, asof = row.iloc[0].category, row.iloc[0].source, row.iloc[0].as_of
            ovr = ovd.get((name, t))
            if ovr:
                cat, src, asof = ovr["category"] + " (override)", ovr["source"][:40], ovr["as_of"]
            rows.append(dict(team=t, rank=rank, player=name, snap_share=round(float(pct), 2), games_started=int(started.get(name, 0)),
                             status=cat, source=src, as_of=asof))
    return pd.DataFrame(rows)


PLAY_PROB = {"ACTIVE": 1.0, "NONE": 1.0, "QUESTIONABLE": 0.75, "DOUBTFUL": 0.25}


def week_miss(season, week):
    """team -> expected share of usual starting-OL snaps unavailable in this week (0..1), from week_report().
    Usual OL5 = the 5 linemen with the most snap share over the previous 6 games; unavailable (out, IR, reserve, PUP,
    practice squad, suspended) counts 1, Doubtful 0.75, Questionable 0.25. Players not in the injury table count as available."""
    r = week_report(season, week)
    out = {}
    for t, g in r.groupby("team"):
        g5 = g.sort_values("rank").head(5)
        pp = []
        for st in g5.status:
            base = st.replace(" (override)", "")
            pp.append(PLAY_PROB.get(base, 1.0 if base in ("not in table",) else 0.0))
        w = g5.snap_share.values
        out[t] = float((w * (1 - np.array(pp))).sum() / w.sum())
    return out


if __name__ == "__main__":
    if sys.argv[1] == "fit":
        tb = int(sys.argv[sys.argv.index("--train-before") + 1]) if "--train-before" in sys.argv else 202506
        fit(tb)
    elif sys.argv[1] == "miss":
        m = week_miss(int(sys.argv[2]), int(sys.argv[3]))
        for t, v in sorted(m.items(), key=lambda kv: -kv[1]):
            print(f"{t:4s} {v:.3f}")
    elif sys.argv[1] == "week":
        pd.set_option("display.width", 250)
        df = week_report(int(sys.argv[2]), int(sys.argv[3]))
        df.to_csv(OUT / f"ol_week_{sys.argv[2]}_{sys.argv[3]}.csv", index=False)
        print(df.to_string(index=False))
