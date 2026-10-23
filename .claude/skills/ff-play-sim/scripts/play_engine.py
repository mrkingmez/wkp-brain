"""Play-by-play game simulator (ff-play-sim, Phase 1).

One game is played one snap at a time: down, distance, field position, clock, score.
  - Coach layer:   pass/run call and 4th-down go/kick/punt come from league tables by situation,
                   shifted by that head coach's own recency-weighted tendency (log-odds offset).
  - Defense layer: every outcome (completion, yards per completion, sack, interception, yards per carry)
                   is the league rate times the offense's relative rate times the defense's relative rate.
  - Hooks for later phases: Model.adj[team] = dict of multipliers (injury, weather, surface go here).
Everything is learned from nflverse play-by-play played BEFORE the game (walk-forward safe).
Penalties, timeouts and overtime are not modelled (a tie is split 50/50 in win odds).
"""
import math
import random
from pathlib import Path

import numpy as np
import pandas as pd

from player_layer import _draw_cum      # noqa: E402  (defender event-count draws)

PBP_DIR = Path(r"D:\WKP\data\nfl\pbp")
YEARS = (2023, 2024, 2025, 2026)
COLS = ["game_id", "play_id", "season", "week", "season_type", "posteam", "defteam", "home_team", "away_team",
        "home_coach", "away_coach", "play_type", "down", "ydstogo", "yardline_100", "qtr", "game_seconds_remaining",
        "half_seconds_remaining", "score_differential", "yards_gained", "touchdown", "interception", "fumble_lost",
        "sack", "complete_pass", "field_goal_result", "kick_distance", "return_yards", "air_yards", "qb_kneel",
        "qb_spike", "drive", "drive_start_transition", "spread_line", "total_line", "result", "total",
        "penalty", "penalty_team", "penalty_yards", "first_down_penalty", "td_team",
        "receiver_player_id", "receiver_player_name", "rusher_player_id", "rusher_player_name", "passer_player_id",
        "passer_player_name", "kicker_player_id",
        "solo_tackle_1_player_id", "solo_tackle_2_player_id", "assist_tackle_1_player_id", "assist_tackle_2_player_id",
        "assist_tackle_3_player_id", "assist_tackle_4_player_id", "pass_defense_1_player_id", "pass_defense_2_player_id",
        "interception_player_id", "sack_player_id", "half_sack_1_player_id", "half_sack_2_player_id",
        "forced_fumble_player_1_player_id", "forced_fumble_player_2_player_id", "fumble_recovery_1_player_id",
        "fumble_recovery_1_team", "fumble_recovery_2_player_id", "fumble_recovery_2_team", "fumble"]
YCAL = 1.05           # global yardage calibration on non-touchdown gains. Structural gap: the sim needs ~6% more yards than real
                      # offenses to reach real scoring (real drives convert yards to points better), so 1.05 splits the difference
                      # (yards +2%, points still ~1.5 per team light). Totals are bias-corrected in the backtest, see backtest_engine.py.
DECAY = 0.88          # per game back, team ratings
WINDOW = 14           # games in a team rating
COACH_HALF_LIFE = 17  # games


def load_pbp(years=YEARS) -> pd.DataFrame:
    fr = []
    for y in years:
        f = PBP_DIR / f"play_by_play_{y}.parquet"
        if f.exists():
            d = pd.read_parquet(f, columns=[c for c in COLS if c])
            fr.append(d)
    p = pd.concat(fr, ignore_index=True)
    p = p[p.season_type == "REG"].copy()
    p["order"] = p.season * 100 + p.week
    p["off_coach"] = np.where(p.posteam == p.home_team, p.home_coach, p.away_coach)
    return p


# ---------------------------------------------------------------- situation keys
def db_(ytg):
    return 0 if ytg <= 2 else 1 if ytg <= 5 else 2 if ytg <= 9 else 3 if ytg == 10 else 4


def zone_(yl):
    return 0 if yl >= 80 else 1 if yl >= 60 else 2 if yl >= 40 else 3 if yl >= 20 else 4 if yl >= 10 else 5


def ss_(d):
    return 0 if d <= -9 else 1 if d < 0 else 2 if d == 0 else 3 if d <= 8 else 4


def zc_(yl):
    return 0 if yl > 20 else 1 if yl > 5 else 2


def _np(a):
    return np.asarray(a)


def _keys(p):
    d = _np(p.down).astype(int)
    ytg = _np(p.ydstogo).astype(int)
    yl = _np(p.yardline_100).astype(int)
    sd = _np(p.score_differential).astype(int)
    hs = _np(p.half_seconds_remaining).astype(int)
    db = np.where(ytg <= 2, 0, np.where(ytg <= 5, 1, np.where(ytg <= 9, 2, np.where(ytg == 10, 3, 4))))
    zn = np.where(yl >= 80, 0, np.where(yl >= 60, 1, np.where(yl >= 40, 2, np.where(yl >= 20, 3, np.where(yl >= 10, 4, 5)))))
    ss = np.where(sd <= -9, 0, np.where(sd < 0, 1, np.where(sd == 0, 2, np.where(sd <= 8, 3, 4))))
    late = (hs <= 300).astype(int)
    return d, db, zn, ss, late


class Tables:
    """League tables and per-team / per-coach ratings learned from games with order < as_of."""

    def __init__(self, pbp: pd.DataFrame, as_of: int):
        p = pbp[pbp.order < as_of].copy()
        self.as_of = as_of
        self._decision_tables(p)
        self._pools(p)
        self._ratings(p)
        self._clock(p)
        self._coaches(p)

    # ------------------------------------------------------------ pass/run and 4th-down tables
    def _decision_tables(self, p):
        s = p[p.play_type.isin(["pass", "run"]) & p.down.between(1, 3) & p.yardline_100.notna() & p.score_differential.notna()
              & p.half_seconds_remaining.notna() & (p.qb_kneel != 1) & (p.qb_spike != 1)].copy()
        d, db, zn, ss, late = _keys(s)
        s["d"], s["db"], s["zn"], s["ss"], s["late"] = d, db, zn, ss, late
        s["y"] = (s.play_type == "pass").astype(float)
        self.lg_pass = s.y.mean()
        t3 = s.groupby(["d", "db"]).y.agg(["sum", "count"])
        t2 = s.groupby(["d", "db", "ss", "late"]).y.agg(["sum", "count"])
        t1 = s.groupby(["d", "db", "zn", "ss", "late"]).y.agg(["sum", "count"])
        self.pass_p = {}
        for dn in (1, 2, 3):
            for b in range(5):
                base = (t3.loc[(dn, b), "sum"] / t3.loc[(dn, b), "count"]) if (dn, b) in t3.index else self.lg_pass
                for sc in range(5):
                    for lt in (0, 1):
                        k2 = (dn, b, sc, lt)
                        p2 = base
                        if k2 in t2.index:
                            p2 = (t2.loc[k2, "sum"] + 30 * base) / (t2.loc[k2, "count"] + 30)
                        for z in range(6):
                            k1 = (dn, b, z, sc, lt)
                            p1 = p2
                            if k1 in t1.index:
                                p1 = (t1.loc[k1, "sum"] + 30 * p2) / (t1.loc[k1, "count"] + 30)
                            self.pass_p[k1] = min(0.97, max(0.03, p1))
        self.s_dec = s
        # 4th down
        f = p[(p.down == 4) & p.play_type.isin(["pass", "run", "field_goal", "punt"]) & p.yardline_100.notna()
              & p.score_differential.notna() & p.half_seconds_remaining.notna()].copy()
        d4, db4, zn4, ss4, late4 = _keys(f)
        f["db"], f["zn"], f["ss"], f["late"] = db4, zn4, ss4, late4
        f["go"] = f.play_type.isin(["pass", "run"]).astype(float)
        self.lg_go = f.go.mean()
        g3 = f.groupby(["db"]).go.agg(["sum", "count"])
        g2 = f.groupby(["db", "zn"]).go.agg(["sum", "count"])
        g1 = f.groupby(["db", "zn", "ss", "late"]).go.agg(["sum", "count"])
        self.go_p = {}
        for b in range(5):
            base = (g3.loc[b, "sum"] / g3.loc[b, "count"]) if b in g3.index else self.lg_go
            for z in range(6):
                p2 = base
                if (b, z) in g2.index:
                    p2 = (g2.loc[(b, z), "sum"] + 30 * base) / (g2.loc[(b, z), "count"] + 30)
                for sc in range(5):
                    for lt in (0, 1):
                        p1 = p2
                        if (b, z, sc, lt) in g1.index:
                            p1 = (g1.loc[(b, z, sc, lt), "sum"] + 25 * p2) / (g1.loc[(b, z, sc, lt), "count"] + 25)
                        self.go_p[(b, z, sc, lt)] = min(0.95, max(0.01, p1))
        self.s_go = f
        kk = f[f.play_type.isin(["field_goal", "punt"])].copy()
        kk["b5"] = (kk.yardline_100 // 5).astype(int).clip(0, 19)
        kk["fg"] = (kk.play_type == "field_goal").astype(float)
        gf = kk.groupby("b5").fg.agg(["sum", "count"])
        self.fg_p = {b: ((gf.loc[b, "sum"] + 1) / (gf.loc[b, "count"] + 2)) if b in gf.index else 0.0 for b in range(20)}
        # field goal make probability by distance
        fgp = p[(p.play_type == "field_goal") & p.kick_distance.notna() & p.field_goal_result.notna()].copy()
        fgp["made"] = (fgp.field_goal_result == "made").astype(int)
        from sklearn.linear_model import LogisticRegression
        lr = LogisticRegression(C=100).fit(fgp[["kick_distance"]].values, fgp.made.values)
        self.fg_make = {yl: float(lr.predict_proba([[yl + 17]])[0, 1]) for yl in range(1, 70)}

    # ------------------------------------------------------------ outcome pools
    def _pools(self, p):
        ps = p[(p.play_type == "pass") & p.yardline_100.notna() & p.yards_gained.notna()].copy()
        ps["zc"] = np.where(ps.yardline_100 > 20, 0, np.where(ps.yardline_100 > 5, 1, 2))
        ns = ps[ps.sack != 1]
        self.base = {}
        self.comp_pool, self.sack_pool, self.run_pool, self.int_air = {}, {}, {}, []
        for z in range(3):
            a = ns[ns.zc == z]
            b = ps[(ps.zc == z)]
            self.base[z] = dict(sack=float((b.sack == 1).mean()), int=float((a.interception == 1).mean()),
                                cmp=float((a.complete_pass == 1).mean()))
            self.comp_pool[z] = a[a.complete_pass == 1].yards_gained.astype(float).tolist()
            self.sack_pool[z] = b[b.sack == 1].yards_gained.astype(float).tolist() or [-7.0]
        ii = ns[ns.interception == 1]
        shift = (ii.air_yards.fillna(0) - ii.return_yards.fillna(0)).astype(int)   # ball spot moves by air yards, then the return
        self.int_air = shift.clip(-10, 40).tolist() or [4]
        rn = p[(p.play_type == "run") & p.yardline_100.notna() & p.yards_gained.notna() & (p.qb_kneel != 1)].copy()
        rn["zc"] = np.where(rn.yardline_100 > 20, 0, np.where(rn.yardline_100 > 5, 1, 2))
        for z in range(3):
            self.run_pool[z] = rn[rn.zc == z].yards_gained.astype(float).tolist()
        # inside the 20 the yards depend on the exact spot (a 1-yard gain is a TD at the 1, not at the 5): per-yard pools
        # every spot 1..99 gets its own yardage pool (nearby spots are borrowed when thin). A gain of `yl` or more is a touchdown there,
        # so pooling across spots would dilute touchdown chances: borrowed plays are re-capped at this spot (y >= yl -> yl).
        self.comp_yl, self.run_yl = {}, {}
        cmp_rows = ns[ns.complete_pass == 1]
        for src, dst in ((cmp_rows, self.comp_yl), (rn, self.run_yl)):
            byy = {k: g.yards_gained.astype(float).values for k, g in src.groupby(src.yardline_100.astype(int))}
            for yl in range(1, 100):
                got, cnt = [], 0
                for dy in (0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8):
                    if cnt >= (80 if yl <= 20 else 250) and dy != 0:
                        break
                    a = byy.get(yl + dy)
                    if a is None:
                        continue
                    got.append(np.where(a >= yl, float(yl), a))
                    cnt += len(a)
                dst[yl] = np.concatenate(got).tolist() if got else [float(yl)]
        self.lg = dict(cmp=float(ns[ns.complete_pass == 1].shape[0] / len(ns)), ypcmp=float(ns[ns.complete_pass == 1].yards_gained.mean()),
                       sack=float((ps.sack == 1).mean()), int=float((ns.interception == 1).mean()),
                       ypc=float(rn.yards_gained.mean()))
        pooled = pd.concat([ps[["fumble_lost"]], rn[["fumble_lost"]]])
        self.fum = float(pooled.fumble_lost.fillna(0).mean())
        # penalties that wipe out a snap (no_play): rate per snap, yards, automatic first down
        npn = p[(p.play_type == "no_play") & (p.penalty == 1) & p.penalty_team.notna() & p.penalty_yards.notna()
                & p.down.notna() & p.posteam.notna()]
        snaps = len(ps) + len(rn) + len(npn)
        offp = npn[npn.penalty_team == npn.posteam]
        defp = npn[npn.penalty_team == npn.defteam]
        self.pen_off_rate = len(offp) / snaps
        self.pen_def_rate = len(defp) / snaps
        self.pen_off = offp.penalty_yards.astype(int).clip(1, 15).tolist() or [10]
        self.pen_def = list(zip(defp.penalty_yards.astype(int).clip(1, 15).tolist(),
                                defp.first_down_penalty.fillna(0).astype(int).tolist())) or [(5, 1)]
        # defensive / special-teams touchdowns
        to = sc_ = p[p.play_type.isin(["pass", "run"]) & ((p.interception == 1) | (p.fumble_lost == 1))]
        self.p_dtd = float(((to.touchdown == 1) & (to.td_team == to.defteam)).sum() / max(1, len(to)))
        ko_ = p[p.play_type == "kickoff"]
        self.p_ko_td = float((ko_.touchdown == 1).sum() / max(1, len(ko_)))
        pu_ = p[p.play_type == "punt"]
        self.p_pr_td = float(((pu_.touchdown == 1) & (pu_.td_team == pu_.defteam)).sum() / max(1, len(pu_)))
        # punts: net yards by field-position bucket
        pu = p[(p.play_type == "punt") & p.kick_distance.notna() & p.yardline_100.notna()].copy()
        pu["net"] = pu.kick_distance - pu.return_yards.fillna(0)
        pu["b"] = (pu.yardline_100 // 10).astype(int).clip(0, 9)
        self.punt_net = {b: g.net.astype(float).tolist() for b, g in pu.groupby("b")}
        allp = pu.net.astype(float).tolist()
        for b in range(10):
            if len(self.punt_net.get(b, [])) < 20:
                self.punt_net[b] = allp
        # kickoff drive starts: first scrimmage snap of drives that began on a kickoff
        sc = p[p.play_type.isin(["pass", "run"]) & p.yardline_100.notna() & p.drive.notna()]
        first = sc.sort_values(["game_id", "play_id"]).groupby(["game_id", "drive"]).head(1)
        self.ko_start = first[first.drive_start_transition == "KICKOFF"].yardline_100.astype(int).tolist() or [75]

    # ------------------------------------------------------------ team ratings (offense and defense, relative to league)
    def _ratings(self, p):
        sc = p[p.play_type.isin(["pass", "run"]) & p.yardline_100.notna() & p.yards_gained.notna() & (p.qb_kneel != 1)].copy()
        lg = self.lg

        def agg(col):
            out = {}
            for team, g in sc.groupby(col):
                orders = sorted(g.order.unique())[-WINDOW:]
                g = g[g.order.isin(orders)]
                age = {o: len(orders) - 1 - i for i, o in enumerate(orders)}
                w = g.order.map(lambda o: DECAY ** age[o]).values
                ps = g[g.play_type == "pass"]
                wp = w[(g.play_type == "pass").values]
                nsm = (ps.sack != 1).values
                wn = wp[nsm]
                psn = ps[ps.sack != 1]
                cm = (psn.complete_pass == 1).values
                wc = wn[cm]
                ru = g[g.play_type == "run"]
                wr = w[(g.play_type == "run").values]

                def sh(x, wt, base, k):
                    return float((np.sum(x * wt) + k * base) / (np.sum(wt) + k)) if len(x) else base
                out[team] = dict(
                    cmp=sh(cm.astype(float), wn, lg["cmp"], 150),
                    ypcmp=sh(psn[psn.complete_pass == 1].yards_gained.values.astype(float), wc, lg["ypcmp"], 100),
                    sack=sh((ps.sack == 1).values.astype(float), wp, lg["sack"], 60),
                    int=sh((psn.interception == 1).values.astype(float), wn, lg["int"], 200),
                    ypc=sh(ru.yards_gained.values.astype(float), wr, lg["ypc"], 100))
            return out
        self.off = agg("posteam")
        self.dfn = agg("defteam")
        # ---- quarterback ratings (strongly shrunk toward the league) and each team's recent QB mix
        pp = p[(p.play_type == "pass") & p.passer_player_id.notna() & p.yards_gained.notna()]
        allord = sorted(pp.order.unique())
        age = {o: len(allord) - 1 - i for i, o in enumerate(allord)}
        pp = pp.assign(w=pp.order.map(lambda o: 0.97 ** age[o]))
        self.qb_rate = {}
        for q, g in pp.groupby("passer_player_id"):
            ns_ = g[g.sack != 1]
            cm_ = ns_[ns_.complete_pass == 1]

            def sh(num, den, base, k):
                return float((num + k * base) / (den + k))
            self.qb_rate[q] = dict(
                cmp=sh((ns_.w * (ns_.complete_pass == 1)).sum(), ns_.w.sum(), lg["cmp"], 250),
                ypcmp=sh((cm_.w * cm_.yards_gained).sum(), cm_.w.sum(), lg["ypcmp"], 120),
                sack=sh((g.w * (g.sack == 1)).sum(), g.w.sum(), lg["sack"], 120),
                int=sh((ns_.w * (ns_.interception == 1)).sum(), ns_.w.sum(), lg["int"], 400))
        self.team_qb_mix = {}
        for team, g in pp.groupby("posteam"):
            orders = sorted(g.order.unique())[-WINDOW:]
            g = g[g.order.isin(orders)]
            ag = {o: len(orders) - 1 - i for i, o in enumerate(orders)}
            wts = g.groupby("passer_player_id").apply(lambda x: float((DECAY ** x.order.map(ag)).sum()), include_groups=False)
            self.team_qb_mix[team] = (wts / wts.sum()).to_dict()

    # ------------------------------------------------------------ clock
    def _clock(self, p):
        q = p.sort_values(["game_id", "play_id"]).copy()
        g = q.groupby("game_id")
        q["n_gsr"] = g.game_seconds_remaining.shift(-1)
        q["n_pos"] = g.posteam.shift(-1)
        q["n_drive"] = g.drive.shift(-1)
        q["n_qtr"] = g.qtr.shift(-1)
        c = q[q.play_type.isin(["pass", "run"]) & (q.qb_kneel != 1) & (q.qb_spike != 1) & q.score_differential.notna()
              & (q.n_pos == q.posteam) & (q.n_drive == q.drive) & q.n_gsr.notna() & q.half_seconds_remaining.notna()].copy()
        c["e"] = c.game_seconds_remaining - c.n_gsr
        c = c[(c.e >= 0) & (c.e <= 60) & (((c.qtr <= 2) & (c.n_qtr <= 2)) | ((c.qtr >= 3) & (c.n_qtr >= 3)))]
        cat = np.where(c.play_type == "run", "run", np.where(c.sack == 1, "sack", np.where(c.complete_pass == 1, "comp", "inc")))
        c["cat"] = cat
        c["hurry"] = (((c.score_differential < 0) & (c.half_seconds_remaining <= 240))
                      | ((c.qtr == 2) & (c.half_seconds_remaining <= 120))).astype(int)
        self.clock = {k: g.e.astype(float).tolist() for k, g in c.groupby(["cat", "hurry"])}
        for cat_ in ("run", "sack", "comp", "inc"):
            for h in (0, 1):
                if len(self.clock.get((cat_, h), [])) < 30:
                    self.clock[(cat_, h)] = self.clock.get((cat_, 0), [30.0])
        self.lg_pace = float(c.e.mean())
        pace = {}
        orders_all = sorted(c.order.unique())
        for team, gg in c.groupby("posteam"):
            orders = sorted(gg.order.unique())[-WINDOW:]
            gg = gg[gg.order.isin(orders)]
            age = {o: len(orders) - 1 - i for i, o in enumerate(orders)}
            w = gg.order.map(lambda o: DECAY ** age[o]).values
            pace[team] = float((np.sum(gg.e.values * w) + 200 * self.lg_pace) / (np.sum(w) + 200)) / self.lg_pace
        self.pace = pace

    # ------------------------------------------------------------ coach offsets
    def _coaches(self, p):
        """Log-odds shift for the pass call and for the 4th-down go call, per head coach (recency weighted, shrunk)."""
        s = self.s_dec
        s = s.assign(coach=s.off_coach)
        exp_ = np.array([self.pass_p[(a, b, c, d_, e)] for a, b, c, d_, e in zip(s.d, s.db, s.zn, s.ss, s.late)])
        s = s.assign(p_exp=exp_)
        self.coach_pass = {}
        lam = 0.5 ** (1.0 / COACH_HALF_LIFE)
        for co, g in s.groupby("coach"):
            orders = sorted(g.order.unique())
            age = {o: len(orders) - 1 - i for i, o in enumerate(orders)}
            w = g.order.map(lambda o: lam ** age[o]).values
            num = float(np.sum(w * (g.y.values - g.p_exp.values)))
            den = float(np.sum(w * g.p_exp.values * (1 - g.p_exp.values)))
            neff = float(np.sum(w))
            self.coach_pass[co] = (num / den) * neff / (neff + 300.0) if den > 0 else 0.0
        f = self.s_go
        f = f.assign(coach=f.off_coach)
        exp4 = np.array([self.go_p[(a, b, c, d_)] for a, b, c, d_ in zip(f.db, f.zn, f.ss, f.late)])
        f = f.assign(p_exp=exp4)
        self.coach_go = {}
        for co, g in f.groupby("coach"):
            orders = sorted(g.order.unique())
            age = {o: len(orders) - 1 - i for i, o in enumerate(orders)}
            w = g.order.map(lambda o: lam ** age[o]).values
            num = float(np.sum(w * (g.go.values - g.p_exp.values)))
            den = float(np.sum(w * g.p_exp.values * (1 - g.p_exp.values)))
            neff = float(np.sum(w))
            self.coach_go[co] = (num / den) * neff / (neff + 60.0) if den > 0 else 0.0
        # league drift: the last two seasons call games differently (more 4th-down aggression, more passing) than the full table
        cut = (self.as_of // 100 - 1) * 100
        rs = s[s.order >= cut]
        rf = f[f.order >= cut]
        self.pass_shift = float((rs.y.mean() - rs.p_exp.mean()) / (rs.p_exp * (1 - rs.p_exp)).mean()) if len(rs) > 500 else 0.0
        self.go_shift = float((rf.go.mean() - rf.p_exp.mean()) / (rf.p_exp * (1 - rf.p_exp)).mean()) if len(rf) > 150 else 0.0
        self.last_coach = {}
        lastg = p.sort_values("order").groupby("posteam").tail(1)
        for _, r in lastg.iterrows():
            self.last_coach[r.posteam] = r.off_coach


# ---------------------------------------------------------------- the simulator
def _logit_shift(pr, off):
    if off == 0.0:
        return pr
    x = math.log(pr / (1.0 - pr)) + off
    return 1.0 / (1.0 + math.exp(-x))


class Matchup:
    """One offense against one defense: precomputed multipliers and coach offsets."""

    def __init__(self, T: Tables, off_team, def_team, off_coach=None, use_def=True, use_coach=True, adj=None, stretch=1.5, qb=None):
        """qb: gsis id of tonight's quarterback. The team rating reflects whoever threw in its recent games; when `qb` differs,
        the pass multipliers move by (this QB's shrunk rate / the team's recent QB-mix rate)."""
        lg = T.lg
        o, d = T.off.get(off_team), T.dfn.get(def_team)
        if not use_def or o is None or d is None:
            o = d = dict(cmp=lg["cmp"], ypcmp=lg["ypcmp"], sack=lg["sack"], int=lg["int"], ypc=lg["ypc"])
        # stretch > 1 widens the gap between strong and weak units (ratings are shrunk toward the league, which compresses them)
        r = lambda k: ((o[k] / lg[k]) * (d[k] / lg[k])) ** stretch
        self.m_cmp = min(1.35, max(0.7, r("cmp")))
        self.m_sack = min(2.2, max(0.45, r("sack")))
        self.m_int = min(2.5, max(0.4, r("int")))
        self.m_ypcmp = min(1.35, max(0.75, r("ypcmp")))
        self.m_ypc = min(1.4, max(0.7, r("ypc")))
        self.qb_note = None
        mix = T.team_qb_mix.get(off_team)
        if qb is not None and mix:
            lgq = dict(cmp=lg["cmp"], ypcmp=lg["ypcmp"], sack=lg["sack"], int=lg["int"])
            cur_q = T.qb_rate.get(qb, lgq)
            implied = {k: sum(w * T.qb_rate.get(q, lgq)[k] for q, w in mix.items()) for k in lgq}
            m = {k: min(1.25, max(0.8, cur_q[k] / implied[k])) for k in lgq}
            self.m_cmp *= m["cmp"]
            self.m_ypcmp *= m["ypcmp"]
            self.m_sack *= m["sack"]
            self.m_int *= m["int"]
            self.qb_note = {k: round(v, 3) for k, v in m.items()}
        if adj:                                    # hooks for injuries / weather / surface
            self.m_cmp *= adj.get("cmp", 1.0)
            self.m_sack *= adj.get("sack", 1.0)
            self.m_int *= adj.get("int", 1.0)
            self.m_ypcmp *= adj.get("ypcmp", 1.0)
            self.m_ypc *= adj.get("ypc", 1.0)
        co = off_coach or T.last_coach.get(off_team)
        self.c_pass = (T.coach_pass.get(co, 0.0) if use_coach else 0.0) + T.pass_shift
        self.c_go = (T.coach_go.get(co, 0.0) if use_coach else 0.0) + T.go_shift
        self.pace = T.pace.get(off_team, 1.0) if use_coach else 1.0


def _draw(lst):
    return lst[int(random.random() * len(lst))]


def _fg_pts(dist):
    """IRFL kicker scoring by distance."""
    return 3.0 if dist < 30 else 3.5 if dist < 40 else 4.5 if dist < 50 else 5.5 if dist < 60 else 6.5


def sim_game(T: Tables, mu_home: Matchup, mu_away: Matchup, n=400, seed=0, stats=None, pm=None, return_players=False, dm=None):
    """mu_home = home offense vs away defense. Returns arrays (home_pts, away_pts, home_plays, away_plays).
    stats: optional dict of counters (yards, plays, td, fg_att, fg_made, punt, turnover, downs, drives, third_att, third_conv).
    dm: (DefenseModel of the home team, DefenseModel of the away team); defenders then earn IRFL points (tackles, assists, sacks,
        pass breakups, interceptions, forced and recovered fumbles, defensive TDs) from the plays the offense runs against them.
    pm: (PlayerModel home, PlayerModel away) from player_layer.py. With return_players=True a 5th item comes back:
        {player_id: {"pts": array over sims (IRFL offense + kicker), "tgt","rec","rec_yds","car","car_yds": totals over all sims}}."""
    random.seed(seed)
    P_PTS, P_VOL = {}, {}
    cur = {}
    if stats is None:
        stats = {}
    sget = stats.get
    mus = (mu_home, mu_away)
    HP, AP, HN, AN = [], [], [], []
    pass_p, go_p, fg_p, fg_make, base = T.pass_p, T.go_p, T.fg_p, T.fg_make, T.base
    comp_pool, sack_pool, run_pool, int_air = T.comp_pool, T.sack_pool, T.run_pool, T.int_air
    clock, punt_net, ko_start, fum = T.clock, T.punt_net, T.ko_start, T.fum
    rnd = random.random
    pen_off_rate, pen_def_rate, pen_off, pen_def = T.pen_off_rate, T.pen_def_rate, T.pen_off, T.pen_def
    comp_yl, run_yl = T.comp_yl, T.run_yl
    p_dtd, p_ko_td, p_pr_td = T.p_dtd, T.p_ko_td, T.p_pr_td
    def add(pid, v):
        cur[pid] = cur.get(pid, 0.0) + v

    def addp(pid, v):
        if pid is not None:
            cur[pid] = cur.get(pid, 0.0) + v

    def vol(pid, k, v=1):
        row = P_VOL.get(pid)
        if row is None:
            row = P_VOL[pid] = [0, 0, 0, 0, 0]
        row[k] += v

    for si in range(n):
        pts = [0, 0]
        cur = {}

        def ko(recv):
            """Kickoff to `recv`: usually a drive start, rarely a return touchdown (then the kicker gets the ball)."""
            if rnd() < p_ko_td:
                pts[recv] += 7 if rnd() < 0.94 else 6
                return (1 - recv, _draw(ko_start))
            return (recv, _draw(ko_start))
        plays = [0, 0]
        t = 3600
        o = 0 if rnd() < 0.5 else 1
        first_recv = o
        yl = _draw(ko_start)
        down, ytg = 1, 10
        half2 = False
        dp = 0
        rzf = False
        guard = 0
        while t > 0 and guard < 400:
            guard += 1
            mu = mus[o]
            d_ = 1 - o
            lead = pts[o] - pts[d_]
            hs = t - 1800 if t > 1800 else t
            late = 1 if hs <= 300 else 0
            ssb = ss_(lead)
            drive_over = False
            new_poss = None            # (team, yardline) for next drive
            elapsed = 0
            if down <= 3 and t <= 120 and lead > 0 and t <= 2000:
                # victory formation
                elapsed = 40
                down += 1
                ytg += 1
                yl = min(99, yl + 1)
                plays[o] += 1
            else:
                call = None
                if down <= 3:
                    pp = _logit_shift(pass_p[(down, db_(ytg), zone_(yl), ssb, late)], mu.c_pass)
                    call = "pass" if rnd() < pp else "run"
                else:
                    g = _logit_shift(go_p[(db_(ytg), zone_(yl), ssb, late)], mu.c_go)
                    if t <= 30 and lead < 0 and yl > 40:
                        g = max(g, 0.9)
                    if rnd() < g:
                        call = "pass" if rnd() < 0.55 else "run"
                    else:
                        call = "fg" if (yl <= 60 and rnd() < fg_p[min(19, yl // 5)]) else "punt"
                if call == "fg":
                    elapsed = 5
                    stats["fg_att"] = sget("fg_att", 0) + 1
                    if rnd() < fg_make.get(yl, 0.0):
                        stats["fg_made"] = sget("fg_made", 0) + 1
                        pts[o] += 3
                        if pm is not None and pm[o].kicker:
                            add(pm[o].kicker, _fg_pts(yl + 17))
                        new_poss = ko(d_)
                    else:
                        new_poss = (d_, min(80, max(1, 100 - (yl + 7))))
                    drive_over = True
                elif call == "punt":
                    stats["punt"] = sget("punt", 0) + 1
                    elapsed = 10
                    net = _draw(punt_net[min(9, yl // 10)])
                    rem = yl - net
                    if rnd() < p_pr_td:
                        pts[d_] += 7 if rnd() < 0.94 else 6
                        new_poss = ko(o)
                    else:
                        new_poss = (d_, 80 if rem <= 0 else min(99, max(1, 100 - int(rem))))
                    drive_over = True
                else:
                    u_pen = rnd()
                    if u_pen < pen_off_rate:
                        yy = _draw(pen_off)
                        yl = min(99, yl + yy)
                        ytg += yy
                        elapsed = 6
                        t -= elapsed
                        if t <= 0:
                            break
                        continue
                    if u_pen < pen_off_rate + pen_def_rate:
                        yy, auto = _draw(pen_def)
                        yy = min(yy, yl // 2)
                        yl -= yy
                        if auto or yy >= ytg:
                            down, ytg = 1, min(10, yl)
                        else:
                            ytg -= yy
                        elapsed = 6
                        t -= elapsed
                        if t <= 0:
                            break
                        continue
                    plays[o] += 1
                    dp += 1
                    if yl <= 20:
                        rzf = True
                    z = zc_(yl)
                    hurry = 1 if ((lead < 0 and hs <= 240) or (t > 1800 and hs <= 120)) else 0
                    turnover = False
                    int_spot = None
                    pmo = pm[o] if pm is not None else None
                    tid = None
                    tk_pid = None
                    if call == "run":
                        y = _draw(run_yl[yl])
                        if y > 0 and y < yl:
                            y = y * mu.m_ypc * YCAL
                        cat = "run"
                        if rnd() < fum:
                            turnover = True
                    else:
                        b = base[z]
                        if rnd() < min(0.2, b["sack"] * mu.m_sack):
                            y = _draw(sack_pool[z])
                            cat = "sack"
                            if rnd() < fum * 2:
                                turnover = True
                        else:
                            pi = min(0.12, b["int"] * mu.m_int)
                            cr_ = yf_ = 1.0
                            if pmo is not None:
                                tid = pmo.pick_target(z, rnd())
                                if tid is not None:
                                    cr_, yf_ = pmo.cr.get(tid, 1.0), pmo.yf.get(tid, 1.0)
                            pc = min(0.85, max(0.3, b["cmp"] * mu.m_cmp * cr_))
                            u = rnd()
                            if u < pi:
                                y = 0.0
                                cat = "inc"
                                turnover = True
                                int_spot = max(1, yl - _draw(int_air))
                            elif u < pi + pc:
                                y = _draw(comp_yl[yl])
                                if y < yl:
                                    y = min(yl - 1, y * mu.m_ypcmp * YCAL * yf_) if y > 0 else y
                                cat = "comp"
                                if rnd() < fum:
                                    turnover = True
                            else:
                                y = 0.0
                                cat = "inc"
                    y = int(round(y))
                    cl = clock[(cat, hurry)]
                    elapsed = _draw(cl) * mu.pace
                    if pmo is not None:
                        q_ = pmo.qb
                        td_ = 6.0 if y >= yl else 0.0
                        yy_ = y if y < yl else yl
                        if call == "run":
                            rid = pmo.pick_rusher(z, rnd())
                            if rid is not None:
                                add(rid, 0.1 * yy_ + td_ - (2.0 if turnover else 0.0))
                                vol(rid, 3)
                                vol(rid, 4, yy_)
                        elif cat == "comp":
                            if q_:
                                add(q_, 0.04 * yy_ + td_)
                            if tid is not None:
                                add(tid, 1.0 + 0.1 * yy_ + td_ - (2.0 if turnover else 0.0))
                                vol(tid, 0)
                                vol(tid, 1)
                                vol(tid, 2, yy_)
                        elif cat == "inc":
                            if tid is not None:
                                vol(tid, 0)
                            if turnover and q_:
                                add(q_, -2.0)
                        elif cat == "sack" and turnover and q_:
                            add(q_, -2.0)
                    if dm is not None:
                        dmo = dm[d_]
                        lg_ = dmo.league
                        if y < yl:                       # no tackle on a touchdown
                            ctx = "run" if call == "run" else ("comp" if cat == "comp" else ("sack" if cat == "sack" else None))
                            if ctx is not None:
                                for _t in range(_draw_cum(lg_["solo_" + ctx], rnd())):
                                    addp(dmo.pick("solo_" + ctx, rnd()), 1.0)
                                for _t in range(_draw_cum(lg_["ast_" + ctx], rnd())):
                                    addp(dmo.pick("ast_" + ctx, rnd()), 0.5)
                        if cat == "sack":
                            if rnd() < lg_["sack_credit"]:
                                addp(dmo.pick("sack", rnd()), 3.0)
                        elif cat == "inc":
                            if turnover:                 # interception
                                tk_pid = dmo.pick("int", rnd())
                                addp(tk_pid, 3.0)
                            else:
                                for _t in range(_draw_cum(lg_["pd"], rnd())):
                                    addp(dmo.pick("pd", rnd()), 1.0)
                        elif cat == "comp":
                            for _t in range(_draw_cum(lg_["pd_comp"], rnd())):
                                addp(dmo.pick("pd", rnd()), 1.0)
                        if turnover and cat != "inc":    # fumble lost: forced and recovered by the defense
                            if rnd() < lg_["ff_given_fumble"]:
                                addp(dmo.pick("ff", rnd()), 2.0)
                            tk_pid = dmo.pick("fr", rnd())
                            addp(tk_pid, 2.0)
                    stats["plays"] = sget("plays", 0) + 1
                    stats["yards"] = sget("yards", 0) + y
                    _k = "c_" + cat
                    stats[_k] = sget(_k, 0) + 1
                    stats["y_" + cat] = sget("y_" + cat, 0) + (y if y < yl else yl)
                    if y >= yl:
                        stats["td_" + call] = sget("td_" + call, 0) + 1
                    if cat == "inc" and turnover:
                        stats["int"] = sget("int", 0) + 1
                    if yl <= 20:
                        stats["rz_plays"] = sget("rz_plays", 0) + 1
                        stats["rz_yards"] = sget("rz_yards", 0) + y
                        if y >= yl:
                            stats["rz_td"] = sget("rz_td", 0) + 1
                    if yl > 60:
                        stats["own_plays"] = sget("own_plays", 0) + 1
                        stats["own_yards"] = sget("own_yards", 0) + y
                    if down == 3:
                        stats["third_att"] = sget("third_att", 0) + 1
                        if y >= ytg:
                            stats["third_conv"] = sget("third_conv", 0) + 1
                    if call == "pass":
                        stats["pass"] = sget("pass", 0) + 1
                    if turnover:
                        stats["turnover"] = sget("turnover", 0) + 1
                    if down == 4:
                        stats["go4"] = sget("go4", 0) + 1
                    b_ = 0 if yl <= 5 else 1 if yl <= 10 else 2 if yl <= 20 else 3 if yl <= 40 else 4
                    stats["pl_b%d" % b_] = sget("pl_b%d" % b_, 0) + 1
                    if y >= yl:
                        stats["td_b%d" % b_] = sget("td_b%d" % b_, 0) + 1
                        stats["td"] = sget("td", 0) + 1
                        if rnd() < 0.94:
                            pts[o] += 7
                            if pmo is not None and pmo.kicker:
                                add(pmo.kicker, 1.0)
                        else:
                            pts[o] += 6
                        new_poss = ko(d_)
                        drive_over = True
                    else:
                        yl_new = yl - y
                        if yl_new >= 100:          # safety
                            pts[d_] += 2
                            new_poss = ko(d_)
                            drive_over = True
                        elif turnover:
                            spot = int_spot if int_spot is not None else yl_new
                            if rnd() < p_dtd:      # returned for a touchdown
                                if dm is not None:
                                    addp(tk_pid, 6.0)
                                pts[d_] += 7 if rnd() < 0.94 else 6
                                new_poss = ko(o)
                            else:
                                new_poss = (d_, 100 - min(99, max(1, int(spot))))
                            drive_over = True
                        else:
                            yl = yl_new
                            if y >= ytg:
                                down = 1
                                ytg = min(10, yl)
                            else:
                                down += 1
                                ytg -= y
                                if down > 4:
                                    new_poss = (d_, 100 - yl)
                                    drive_over = True
            # clock
            t_old = t
            t -= elapsed
            if t_old > 1800 >= t and not half2:
                t = 1800
                half2 = True
                if dp:
                    k_ = "dl%d" % min(dp, 10)
                    stats[k_] = sget(k_, 0) + 1
                    if rzf:
                        stats["rz_drives"] = sget("rz_drives", 0) + 1
                dp = 0
                rzf = False
                o = 1 - first_recv
                yl = _draw(ko_start)
                down, ytg = 1, 10
                continue
            if t <= 0:
                if dp:
                    k_ = "dl%d" % min(dp, 10)
                    stats[k_] = sget(k_, 0) + 1
                    if rzf:
                        stats["rz_drives"] = sget("rz_drives", 0) + 1
                break
            if drive_over and new_poss is not None:
                o, yl = new_poss
                k_ = "dl%d" % min(dp, 10)
                stats[k_] = sget(k_, 0) + 1
                dp = 0
                if rzf:
                    stats["rz_drives"] = sget("rz_drives", 0) + 1
                rzf = False
                stats["starts"] = sget("starts", 0) + 1
                stats["start_yl"] = sget("start_yl", 0) + yl
                down, ytg = 1, min(10, yl)
        HP.append(pts[0])
        AP.append(pts[1])
        HN.append(plays[0])
        AN.append(plays[1])
        if pm is not None or dm is not None:
            for pid_, v_ in cur.items():
                arr = P_PTS.get(pid_)
                if arr is None:
                    arr = P_PTS[pid_] = np.zeros(n)
                arr[si] = v_
    out = (np.array(HP), np.array(AP), np.array(HN), np.array(AN))
    if return_players:
        players = {}
        for pid_, arr in P_PTS.items():
            v = P_VOL.get(pid_, [0, 0, 0, 0, 0])
            players[pid_] = dict(pts=arr, tgt=v[0] / n, rec=v[1] / n, rec_yds=v[2] / n, car=v[3] / n, car_yds=v[4] / n)
        return out + (players,)
    return out
