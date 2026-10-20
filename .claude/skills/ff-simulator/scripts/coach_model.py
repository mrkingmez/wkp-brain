"""Coaching-tendency model for the fantasy / pick'em simulator.

Reads nflverse play-by-play (D:\\WKP\\data\\nfl\\pbp, pulled by fetch_pbp.py) and
builds per-coach tendencies from the last few seasons, with recent games
weighted heavier and thin samples pulled toward the league average.

Everything is computed AS OF a cutoff (season, week): only games strictly
before that week are used, so the same code serves the live forecast and the
backtest with no peeking.

Features (all offense, per coach):
  pass_neutral  pass rate on 1st/2nd down, win prob 20-80%, outside the last
                two minutes of a half (the standard "neutral script" filter)
  pass_oe       nflverse pass-over-expected, neutral plays
  rz_pass       pass rate inside the opponent 20
  go4           go-for-it rate on 4th & 1-3 between the opp 2 and own 40+
  trail_boost   pass rate when down 7+ minus neutral pass rate
  lead_boost    pass rate when up 7+ minus neutral pass rate
  plays_pg      offensive plays per game (pace proxy)
  shotgun, no_huddle

New head coaches have no history under their own name, so the model falls
back to the team's own recent plays (weighted lower) and then the league
average. The output says how much real data sits behind each number.
"""
import numpy as np
import pandas as pd
from pathlib import Path

PBP_DIR = Path(r"D:\WKP\data\nfl\pbp")
YEARS = (2023, 2024, 2025, 2026)
HALF_LIFE_GAMES = 17      # a season ago counts about half
TEAM_FALLBACK_W = 0.35    # weight of a team's non-coach history
PRIOR_PLAYS = {           # pseudo-plays pulling thin samples to the league mean
    "pass_neutral": 150, "pass_all": 200, "pass_oe": 150, "rz_pass": 80, "go4": 25,
    "trail_boost": 120, "lead_boost": 120, "shotgun": 200, "no_huddle": 200,
}
FEATURES = list(PRIOR_PLAYS) + ["plays_pg"]


def load_plays(years=YEARS) -> pd.DataFrame:
    cols = ["game_id", "season", "week", "season_type", "posteam", "defteam", "home_team", "away_team",
            "home_coach", "away_coach", "play_type", "pass", "rush", "down", "ydstogo", "yardline_100",
            "wp", "score_differential", "qtr", "half_seconds_remaining", "shotgun", "no_huddle",
            "pass_oe", "two_point_attempt", "qb_kneel", "qb_spike", "epa"]
    fr = []
    for y in years:
        f = PBP_DIR / f"play_by_play_{y}.parquet"
        if f.exists():
            d = pd.read_parquet(f)
            fr.append(d[[c for c in cols if c in d.columns]])
    p = pd.concat(fr, ignore_index=True)
    p = p[(p.season_type == "REG") & p.posteam.notna() & p.down.notna()
          & p.play_type.isin(["pass", "run"]) & (p.two_point_attempt != 1)].copy()
    p["coach"] = np.where(p.posteam == p.home_team, p.home_coach, p.away_coach)
    p["order"] = p.season * 100 + p.week
    return p


def team_game_table(p: pd.DataFrame) -> pd.DataFrame:
    """One row per (team, game) holding the sums/counts each feature needs."""
    q = pd.DataFrame({
        "posteam": p.posteam, "game_id": p.game_id, "season": p.season, "week": p.week,
        "order": p.order, "coach": p.coach,
    })
    ip = (p.play_type == "pass").astype(int)
    neutral = ((p.down <= 2) & p.wp.between(0.2, 0.8) & (p.half_seconds_remaining > 120)).astype(int)
    rz = (p.yardline_100 <= 20).astype(int)
    trail = (p.score_differential <= -7).astype(int)
    lead = (p.score_differential >= 7).astype(int)
    oe_ok = (neutral == 1) & p.pass_oe.notna()
    q["plays"] = 1
    q["pass_all_s"] = ip
    q["n_neutral"] = neutral
    q["pass_neutral_s"] = neutral * ip
    q["oe_s"] = np.where(oe_ok, p.pass_oe, 0.0)
    q["n_oe"] = oe_ok.astype(int)
    q["n_rz"] = rz
    q["rz_pass_s"] = rz * ip
    q["n_trail"] = trail
    q["trail_pass_s"] = trail * ip
    q["n_lead"] = lead
    q["lead_pass_s"] = lead * ip
    q["shotgun_s"] = p.shotgun.fillna(0)
    q["nohuddle_s"] = p.no_huddle.fillna(0)
    keys = ["posteam", "game_id", "season", "week", "order", "coach"]
    return q.groupby(keys, dropna=False).sum().reset_index()


def fourth_down_table(years=YEARS) -> pd.DataFrame:
    """4th & 1-3 decisions need the punt/FG rows too, so read them separately."""
    fr = []
    for y in years:
        f = PBP_DIR / f"play_by_play_{y}.parquet"
        if f.exists():
            d = pd.read_parquet(f, columns=["game_id", "season", "week", "season_type", "posteam", "down",
                                            "ydstogo", "yardline_100", "play_type", "wp"])
            fr.append(d)
    d = pd.concat(fr, ignore_index=True)
    d = d[(d.season_type == "REG") & (d.down == 4) & d.ydstogo.between(1, 3)
          & d.yardline_100.between(2, 60) & d.wp.between(0.1, 0.9) & d.posteam.notna()].copy()
    d["go"] = d.play_type.isin(["pass", "run"]).astype(int)
    d = d[d.play_type.isin(["pass", "run", "punt", "field_goal"])]
    return d.groupby(["posteam", "game_id"]).agg(n_4=("go", "size"), go_s=("go", "sum")).reset_index()


def _agg(rows: pd.DataFrame, weights: np.ndarray, league: dict) -> dict:
    """Weighted, shrunk feature estimates from a block of team-game rows."""
    w = weights
    out, n_eff = {}, {}

    def shrink(num, den, prior_val, k):
        return (num + k * prior_val) / (den + k) if (den + k) > 0 else prior_val

    n = (w * rows.n_neutral.values).sum()
    out["pass_neutral"] = shrink((w * rows.pass_neutral_s.values).sum(), n, league["pass_neutral"], PRIOR_PLAYS["pass_neutral"])
    n_eff["pass_neutral"] = n
    n2 = (w * rows.n_oe.values).sum()
    out["pass_oe"] = shrink((w * rows.oe_s.values).sum(), n2, league["pass_oe"], PRIOR_PLAYS["pass_oe"])
    n3 = (w * rows.n_rz.values).sum()
    out["rz_pass"] = shrink((w * rows.rz_pass_s.values).sum(), n3, league["rz_pass"], PRIOR_PLAYS["rz_pass"])
    if "n_4" in rows:
        n4 = (w * rows.n_4.fillna(0).values).sum()
        out["go4"] = shrink((w * rows.go_s.fillna(0).values).sum(), n4, league["go4"], PRIOR_PLAYS["go4"])
    else:
        out["go4"] = league["go4"]
    npl = (w * rows.plays.values).sum()
    out["pass_all"] = shrink((w * rows.pass_all_s.values).sum(), npl, league["pass_all"], PRIOR_PLAYS["pass_all"])
    nt = (w * rows.n_trail.values).sum()
    tr = shrink((w * rows.trail_pass_s.values).sum(), nt, league["trail_pass"], PRIOR_PLAYS["trail_boost"])
    nl = (w * rows.n_lead.values).sum()
    ld = shrink((w * rows.lead_pass_s.values).sum(), nl, league["lead_pass"], PRIOR_PLAYS["lead_boost"])
    # boosts are relative to the coach's OVERALL pass rate (all downs), because that is what
    # the simulator starts from; trailing/leading rates are also all-downs.
    out["trail_boost"] = tr - out["pass_all"]
    out["lead_boost"] = ld - out["pass_all"]
    out["shotgun"] = shrink((w * rows.shotgun_s.values).sum(), npl, league["shotgun"], PRIOR_PLAYS["shotgun"])
    out["no_huddle"] = shrink((w * rows.nohuddle_s.values).sum(), npl, league["no_huddle"], PRIOR_PLAYS["no_huddle"])
    games = w.sum()
    out["plays_pg"] = (w * rows.plays.values).sum() / games if games > 0 else league["plays_pg"]
    # light shrink on pace: 3 pseudo-games at league pace
    out["plays_pg"] = (out["plays_pg"] * games + 3 * league["plays_pg"]) / (games + 3)
    out["_plays_behind"] = float(npl)
    out["_games_behind"] = float(games)
    return out


def league_means(tg: pd.DataFrame) -> dict:
    return {
        "pass_neutral": tg.pass_neutral_s.sum() / tg.n_neutral.sum(),
        "pass_all": tg.pass_all_s.sum() / tg.plays.sum(),
        "pass_oe": tg.oe_s.sum() / max(tg.n_oe.sum(), 1),
        "rz_pass": tg.rz_pass_s.sum() / tg.n_rz.sum(),
        "go4": tg.go_s.fillna(0).sum() / max(tg.n_4.fillna(0).sum(), 1) if "n_4" in tg else 0.25,
        "trail_pass": tg.trail_pass_s.sum() / tg.n_trail.sum(),
        "lead_pass": tg.lead_pass_s.sum() / tg.n_lead.sum(),
        "shotgun": tg.shotgun_s.sum() / tg.plays.sum(),
        "no_huddle": tg.nohuddle_s.sum() / tg.plays.sum(),
        "plays_pg": tg.plays.mean(),
    }


def build_tables():
    p = load_plays()
    tg = team_game_table(p)
    f4 = fourth_down_table()
    tg = tg.merge(f4, on=["posteam", "game_id"], how="left")
    return p, tg


def tendencies(tg: pd.DataFrame, coach: str, team: str, as_of: int, league: dict | None = None) -> dict:
    """as_of = season*100 + week; only games strictly before are used."""
    hist = tg[tg.order < as_of].copy()
    if league is None:
        league = league_means(hist if len(hist) else tg)
    # game age -> exponential decay, counted in that coach's / team's own games
    def block(rows, scale):
        if rows.empty:
            return rows, np.array([])
        rows = rows.sort_values("order")
        age = np.arange(len(rows))[::-1]
        return rows, scale * 0.5 ** (age / HALF_LIFE_GAMES)

    own, w_own = block(hist[hist.coach == coach], 1.0)
    team_other, w_team = block(hist[(hist.posteam == team) & (hist.coach != coach)], TEAM_FALLBACK_W)
    rows = pd.concat([own, team_other]) if len(team_other) else own
    w = np.concatenate([w_own, w_team]) if len(team_other) else w_own
    if len(rows) == 0:
        out = {k: league.get(k, 0) for k in FEATURES}
        out["trail_boost"] = league["trail_pass"] - league["pass_all"]
        out["lead_boost"] = league["lead_pass"] - league["pass_all"]
        out["_plays_behind"] = 0.0
        out["_games_behind"] = 0.0
    else:
        out = _agg(rows, w, league)
    out["_own_plays"] = float(own.plays.sum()) if len(own) else 0.0
    return out
