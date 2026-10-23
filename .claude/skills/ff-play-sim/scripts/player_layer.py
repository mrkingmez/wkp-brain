"""Player layer for play_engine (ff-play-sim Phase 2): who gets the ball on each simulated snap.

PlayerModel(pbp, as_of, team, avail=None) learns from that team's last 14 games BEFORE as_of (recency weighted):
  - target share by field zone (normal / inside the 20 / inside the 5), shrunk toward the player's overall share
  - carry share by the same zones (QB scrambles count as QB carries)
  - catch rate and yards per catch relative to the team (shrunk), so a back and a deep threat do not look alike
  - the quarterback (most recent weighted dropbacks among available QBs) and the kicker
avail = {gsis_id: play_probability} scales a player's share (0 removes him and his share goes to teammates).
"""
import bisect
import os

import numpy as np
import pandas as pd

EFF = os.environ.get("PS_EFF", "1") == "1"      # per-player catch rate / yards per catch factors
ZONE = os.environ.get("PS_ZONE", "1") == "1"    # separate red-zone and goal-line shares
DECAY = float(os.environ.get("PS_DECAY", "0.88"))
WINDOW = int(os.environ.get("PS_WINDOW", "14"))
K_ZONE = (0, 14.0, 8.0)       # shrink strength toward overall share, zones 0 (>20), 1 (6-20), 2 (<=5)
K_CATCH = 25.0                # targets of prior for catch rate
K_YPR = 15.0                  # catches of prior for yards per catch


def _cum(w):
    s = float(sum(w))
    if s <= 0:
        return [1.0], [0]
    c, acc = [], 0.0
    for x in w:
        acc += x / s
        c.append(acc)
    c[-1] = 1.0
    return c, None


class PlayerModel:
    def __init__(self, pbp: pd.DataFrame, as_of: int, team: str, avail: dict | None = None, qb: str | None = None,
                 active: set | None = None):
        """active: if given, only these player ids can get the ball (everyone else in the team's recent history is treated as out)."""
        avail = dict(avail or {})
        p = pbp[(pbp.order < as_of) & (pbp.posteam == team)]
        orders = sorted(p.order.unique())[-WINDOW:]
        p = p[p.order.isin(orders)].copy()
        if active is not None:
            ids = set()
            for c in ("receiver_player_id", "rusher_player_id", "passer_player_id", "kicker_player_id"):
                if c in p:
                    ids |= set(p[c].dropna().unique())
            for i in ids:
                if i not in active:
                    avail[i] = 0.0
        age = {o: len(orders) - 1 - i for i, o in enumerate(orders)}
        p["w"] = p.order.map(lambda o: DECAY ** age[o])
        p["zk"] = np.where(p.yardline_100 > 20, 0, np.where(p.yardline_100 > 5, 1, 2))
        self.team = team
        self.names = {}
        for c_id, c_nm in (("receiver_player_id", "receiver_player_name"), ("rusher_player_id", "rusher_player_name"),
                           ("passer_player_id", "passer_player_name")):
            if c_id in p and c_nm in p:
                for i, n in p[[c_id, c_nm]].dropna().drop_duplicates().itertuples(index=False):
                    self.names[i] = n

        # ---- targets
        tg = p[(p.play_type == "pass") & (p.sack != 1) & p.receiver_player_id.notna()]
        self.tgt_ids, self.tgt_cum = self._shares(tg, "receiver_player_id", avail)
        # catch rate / yards per catch relative to team
        t_all = tg.w.sum()
        team_cr = (tg.w * (tg.complete_pass == 1)).sum() / max(t_all, 1e-9)
        cs = tg[tg.complete_pass == 1]
        team_ypr = (cs.w * cs.yards_gained).sum() / max(cs.w.sum(), 1e-9)
        self.cr, self.yf = {}, {}
        for pid, g in tg.groupby("receiver_player_id"):
            tw, cw = g.w.sum(), (g.w * (g.complete_pass == 1)).sum()
            self.cr[pid] = ((cw + K_CATCH * team_cr) / (tw + K_CATCH)) / team_cr
            gc = g[g.complete_pass == 1]
            self.yf[pid] = (((gc.w * gc.yards_gained).sum() + K_YPR * team_ypr) / (gc.w.sum() + K_YPR)) / team_ypr
        if not EFF:
            self.cr, self.yf = {}, {}
        # ---- carries
        ru = p[(p.play_type == "run") & p.rusher_player_id.notna() & (p.qb_kneel != 1)]
        self.car_ids, self.car_cum = self._shares(ru, "rusher_player_id", avail)
        # ---- quarterback and kicker
        qbs = p[(p.play_type == "pass") & p.passer_player_id.notna()].groupby("passer_player_id").w.sum()
        qbs = {i: v * avail.get(i, 1.0) for i, v in qbs.items() if avail.get(i, 1.0) > 0}
        self.qb = qb or (max(qbs, key=qbs.get) if qbs else None)
        ks = p[(p.play_type.isin(["field_goal", "extra_point"])) & p.kicker_player_id.notna()].groupby("kicker_player_id").w.sum() \
            if "kicker_player_id" in p else pd.Series(dtype=float)
        ks = {i: v for i, v in ks.items() if avail.get(i, 1.0) > 0}
        self.kicker = max(ks, key=ks.get) if ks else None
        if self.qb:
            self.names.setdefault(self.qb, self.qb)

    def _shares(self, d, col, avail):
        """Per-zone cumulative probability lists over one id list."""
        ids = [i for i in d[col].unique() if avail.get(i, 1.0) > 0]
        if not ids:
            return [], [[1.0], [1.0], [1.0]]
        d = d[d[col].isin(ids)]
        pa = {i: avail.get(i, 1.0) for i in ids}
        base = d.groupby(col).w.sum()
        base = pd.Series({i: base.get(i, 0.0) * pa[i] for i in ids})
        base = base / base.sum()
        cums = []
        for z in range(3):
            if z == 0:
                w = [float(base[i]) for i in ids]
            else:
                dz = d[d.zk == z] if z == 2 else d[d.zk >= 1]
                cz = dz.groupby(col).w.sum()
                nz = float(cz.sum())
                k = K_ZONE[z]
                w = [(cz.get(i, 0.0) * pa[i] + k * float(base[i])) / (nz + k) for i in ids]
            cums.append(_cum(w)[0])
        if not ZONE:
            cums = [cums[0], cums[0], cums[0]]
        return ids, cums

    # ---- picks used inside the simulation loop (pure Python for speed)
    def pick_target(self, zk, u):
        if not self.tgt_ids:
            return None
        return self.tgt_ids[bisect.bisect_left(self.tgt_cum[zk], u)]

    def pick_rusher(self, zk, u):
        if not self.car_ids:
            return None
        return self.car_ids[bisect.bisect_left(self.car_cum[zk], u)]


# =====================================================================================================================
# Defenders (IDP)
# =====================================================================================================================
_LEAGUE_CACHE = {}
SOLO = ["solo_tackle_1_player_id", "solo_tackle_2_player_id"]
ASSIST = ["assist_tackle_1_player_id", "assist_tackle_2_player_id", "assist_tackle_3_player_id", "assist_tackle_4_player_id"]
PDEF = ["pass_defense_1_player_id", "pass_defense_2_player_id"]
FFUM = ["forced_fumble_player_1_player_id", "forced_fumble_player_2_player_id"]


def _pmf(counts):
    """Cumulative distribution over 0..max count."""
    n = len(counts)
    vc = pd.Series(counts).value_counts(normalize=True).sort_index()
    top = int(vc.index.max()) if len(vc) else 0
    c, acc = [], 0.0
    for k in range(top + 1):
        acc += float(vc.get(k, 0.0))
        c.append(acc)
    c[-1] = 1.0
    return c


def league_def(pbp, as_of):
    """League event counts per play context (how many solo tackles, assists, pass breakups a play produces), cached per as_of."""
    if as_of in _LEAGUE_CACHE:
        return _LEAGUE_CACHE[as_of]
    p = pbp[pbp.order < as_of]
    run = p[(p.play_type == "run") & (p.qb_kneel != 1)]
    comp = p[(p.play_type == "pass") & (p.complete_pass == 1)]
    sack = p[(p.play_type == "pass") & (p.sack == 1)]
    inc = p[(p.play_type == "pass") & (p.complete_pass == 0) & (p.sack != 1) & (p.interception != 1)]
    # touchdown plays have no tackle: measure on non-scoring plays, apply on non-scoring plays
    nt = lambda d: d[d.touchdown != 1]
    out = {}
    for name, d in (("run", nt(run)), ("comp", nt(comp)), ("sack", nt(sack))):
        out["solo_" + name] = _pmf(d[SOLO].notna().sum(axis=1).tolist())
        out["ast_" + name] = _pmf(d[ASSIST].notna().sum(axis=1).tolist())
    out["pd"] = _pmf(inc[PDEF].notna().sum(axis=1).tolist())
    out["pd_comp"] = _pmf(comp[PDEF].notna().sum(axis=1).tolist())
    # sacks credited per sack event (half sacks make it fractional): total sack credit / sack events
    full = sack.sack_player_id.notna().sum()
    half = sack.half_sack_1_player_id.notna().sum() + sack.half_sack_2_player_id.notna().sum()
    out["sack_credit"] = float((full + 0.5 * half) / max(1, len(sack)))
    fum = p[(p.fumble_lost == 1)]
    out["ff_given_fumble"] = float(fum[FFUM].notna().any(axis=1).mean()) if len(fum) else 0.7
    _LEAGUE_CACHE[as_of] = out
    return out


def _draw_cum(cum, u):
    return bisect.bisect_left(cum, u)


class DefenseModel:
    """Who on a defense gets the tackles, sacks, breakups, takeaways. Shares come from that defense's last 14 games before `as_of`
    (recency weighted) by event type; availability scales a player's share exactly as PlayerModel does for the offense."""

    def __init__(self, pbp, as_of, team, avail=None, active=None):
        avail = dict(avail or {})
        p = pbp[(pbp.order < as_of) & (pbp.defteam == team)]
        orders = sorted(p.order.unique())[-WINDOW:]
        p = p[p.order.isin(orders)].copy()
        age = {o: len(orders) - 1 - i for i, o in enumerate(orders)}
        p["w"] = p.order.map(lambda o: DECAY ** age[o])
        self.team = team
        self.league = league_def(pbp, as_of)
        cols = SOLO + ASSIST + PDEF + FFUM + ["interception_player_id", "sack_player_id", "half_sack_1_player_id", "half_sack_2_player_id",
                                              "fumble_recovery_1_player_id", "fumble_recovery_2_player_id"]
        if active is not None:
            ids = set()
            for c in cols:
                if c in p:
                    ids |= set(p[c].dropna().unique())
            for i in ids:
                if i not in active:
                    avail[i] = 0.0
        run = p[(p.play_type == "run") & (p.qb_kneel != 1)]
        comp = p[(p.play_type == "pass") & (p.complete_pass == 1)]
        sack = p[(p.play_type == "pass") & (p.sack == 1)]
        inc = p[(p.play_type == "pass") & (p.complete_pass == 0) & (p.sack != 1)]
        self.lists = {}

        def weights(frames_cols):
            """frames_cols: list of (frame, [id columns], value per id) -> {player: weighted count}"""
            tot = {}
            for fr, cs, val in frames_cols:
                for c in cs:
                    g = fr[fr[c].notna()].groupby(c).w.sum() * val
                    for i, v in g.items():
                        tot[i] = tot.get(i, 0.0) + float(v)
            return tot

        spec = {
            "solo_run": [(run, SOLO, 1.0)], "ast_run": [(run, ASSIST, 1.0)],
            "solo_comp": [(comp, SOLO, 1.0)], "ast_comp": [(comp, ASSIST, 1.0)],
            "solo_sack": [(sack, SOLO, 1.0)], "ast_sack": [(sack, ASSIST, 1.0)],
            "sack": [(sack, ["sack_player_id"], 1.0), (sack, ["half_sack_1_player_id", "half_sack_2_player_id"], 0.5)],
            "pd": [(inc, PDEF, 1.0), (comp, PDEF, 1.0)],
            "int": [(p[p.interception == 1], ["interception_player_id"], 1.0)],
            "ff": [(p, FFUM, 1.0)],
        }
        for name, fc in spec.items():
            w = weights(fc)
            w = {i: v * avail.get(i, 1.0) for i, v in w.items() if avail.get(i, 1.0) > 0}
            self.lists[name] = self._cum(w)
        # fumble recoveries by this defense (the recovering team is the defense)
        fr_ = []
        for k in (1, 2):
            f = p[(p["fumble_recovery_%d_team" % k] == team) & p["fumble_recovery_%d_player_id" % k].notna()]
            fr_.append((f, ["fumble_recovery_%d_player_id" % k], 1.0))
        w = weights(fr_)
        w = {i: v * avail.get(i, 1.0) for i, v in w.items() if avail.get(i, 1.0) > 0}
        self.lists["fr"] = self._cum(w)

    @staticmethod
    def _cum(w):
        if not w:
            return [], [1.0]
        ids = list(w)
        c, _ = _cum([w[i] for i in ids])
        return ids, c

    def pick(self, name, u):
        ids, cum = self.lists[name]
        if not ids:
            return None
        return ids[bisect.bisect_left(cum, u)]
