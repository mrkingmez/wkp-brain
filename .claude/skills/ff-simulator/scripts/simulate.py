"""Game-by-game Monte Carlo for the IRFL lineup and pick'em model.

For one week it simulates every game thousands of times:
  1. Game script: final margin and total drawn around the market line.
  2. Coach tendencies (coach_model.py) turn script into pass/run volume,
     pace, red-zone mix. Trailing teams throw more, leading teams run more,
     each by that coach's own history.
  3. Team volume is split among players by their recency-weighted shares of
     targets, carries and touchdowns (this season plus last).
  4. Defenders score off the opponent's simulated plays and pass attempts.
  5. Every stat is scored with the IRFL rules (FF-SCORING-RULES.md), so one
     simulated game gives every player a correlated stat line.

Outputs a draws matrix (players x sims) so the optimizer can use ceilings,
floors and head-to-head odds, not just averages.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import coach_model as cm

DATA = Path(r"D:\WKP\data\nfl")
WINDOW_GAMES = 14        # last N team games feed usage and efficiency
DECAY = 0.88             # weight per game back
MISS_WEIGHT = 0.4        # weight of a game where the player has no stat line (see build_players)

# ---------------------------------------------------------------- offensive line layer (ol_model.py)
# OL_SCALE multiplies the data-fitted effect sizes in ol_coefs.json. 0 = layer off (Week 6 behaviour, default).
OL_SCALE = 0.0
_OL_COEF = {}


def set_ol(scale, zero=(), coef_path=r"D:\WKP\data\ff-simulator\ol_coefs.json"):
    """Turn the OL layer on at `scale` (1.0 = the fitted size). Needs ol_coefs.json from ol_model.py fit."""
    global OL_SCALE, _OL_COEF
    OL_SCALE = float(scale)
    _OL_COEF = json.load(open(coef_path)) if scale else {}
    for k in zero:                       # switch single components off (e.g. zero=("sack_rate",))
        if k in _OL_COEF:
            _OL_COEF[k] = dict(_OL_COEF[k], beta=0.0)


# ---------------------------------------------------------------- scoring
PTS = dict(pass_yd=0.04, pass_td=6, int=-2, rush_yd=0.1, rush_td=6, rec=1, rec_yd=0.1, rec_td=6,
           fum_lost=-2, solo=1, ast=0.5, sack=3, def_int=3, pd=1, ff=2, fr=2, def_td=6, safety=4, xp=1,
           fg_avg=3.75)


def load_player_weeks(seasons=(2025, 2026)) -> pd.DataFrame:
    fr = []
    for s in seasons:
        f = DATA / "stats_player" / f"stats_player_week_{s}.parquet"
        if f.exists():
            fr.append(pd.read_parquet(f))
    d = pd.concat(fr, ignore_index=True)
    d = d[d.season_type == "REG"].copy()
    d["order"] = d.season * 100 + d.week
    return d


def defense_table(as_of: int) -> tuple[pd.DataFrame, dict]:
    """What each defense allows per pass attempt / carry, plus pass rush and ball hawking."""
    fr = []
    for y in cm.YEARS:
        f = cm.PBP_DIR / f"play_by_play_{y}.parquet"
        if f.exists():
            fr.append(pd.read_parquet(f, columns=["season", "week", "season_type", "defteam", "posteam", "play_type",
                                                  "yards_gained", "sack", "interception", "qb_scramble"]))
    p = pd.concat(fr, ignore_index=True)
    p = p[(p.season_type == "REG") & p.defteam.notna() & p.play_type.isin(["pass", "run"])]
    p["order"] = p.season * 100 + p.week
    p = p[p.order < as_of]
    out = {}
    lg = {}
    ps, rs = p[p.play_type == "pass"], p[p.play_type == "run"]
    lg["ypa"] = ps.yards_gained.sum() / len(ps)
    lg["ypc"] = rs.yards_gained.sum() / len(rs)
    lg["sack"] = ps.sack.sum() / len(ps)
    lg["int"] = ps.interception.sum() / len(ps)
    for team, g in p.groupby("defteam"):
        g = g.sort_values("order")
        orders = sorted(g.order.unique())[-WINDOW_GAMES:]
        g = g[g.order.isin(orders)]
        gp, gr = g[g.play_type == "pass"], g[g.play_type == "run"]
        k = 150.0
        out[team] = dict(
            ypa=(gp.yards_gained.sum() + k * lg["ypa"]) / (len(gp) + k),
            ypc=(gr.yards_gained.sum() + k * lg["ypc"]) / (len(gr) + k),
            sack=(gp.sack.sum() + 60 * lg["sack"]) / (len(gp) + 60),
            int=(gp.interception.sum() + 200 * lg["int"]) / (len(gp) + 200),
        )
    return pd.DataFrame(out).T, lg


class TeamModel:
    """Everything the simulator needs to know about one offense and its players."""

    def __init__(self, team, pw, tg, tend, as_of, latest=None):
        self.team = team
        self.tend = tend
        games = tg[(tg.posteam == team) & (tg.order < as_of)].sort_values("order").tail(WINDOW_GAMES)
        self.orders = list(games.order)
        n = len(self.orders)
        age = np.arange(n)[::-1]
        self.w = dict(zip(self.orders, DECAY ** age))
        rows = pw[(pw.team == team) & pw.order.isin(self.orders)].copy()
        rows["w"] = rows.order.map(self.w)
        self.rows = rows
        by_game = rows.groupby("order").agg(
            att=("attempts", "sum"), sacked=("sacks_suffered", "sum"), car=("carries", "sum"),
            tgt=("targets", "sum"), ptd=("passing_tds", "sum"), rtd=("rushing_tds", "sum"),
            pyd=("passing_yards", "sum"), comp=("completions", "sum"), ryd=("rushing_yards", "sum"),
            ints=("passing_interceptions", "sum"))
        by_game = by_game.reindex(self.orders).fillna(0)
        W = np.array([self.w[o] for o in self.orders])
        self.by_game, self.W = by_game, W
        tot = lambda c: float((by_game[c].values * W).sum())
        self.pass_plays = tot("att") + tot("sacked")
        L = dict(ypa=7.0, cmp=0.64, int=0.022, ypc=4.4)
        att = max(tot("att"), 1)
        # shrink toward league: pseudo-attempts of league-average play
        self.off = dict(
            ypa=(tot("pyd") + 120 * L["ypa"]) / (att + 120),
            cmp=(tot("comp") + 80 * L["cmp"]) / (att + 80),
            int=(tot("ints") + 200 * L["int"]) / (att + 200),
            ypc=(tot("ryd") + 100 * L["ypc"]) / (max(tot("car"), 1) + 100),
        )
        self.avail = {}                      # player_id -> chance he plays (set by the runner)
        self.ol_missing = 0.0                # share of usual starting-OL snaps unavailable (0..1), set by the runner
        self.team_tgt = max(tot("tgt"), 1)
        self.team_car = max(tot("car"), 1)
        self.team_ptd = max(tot("ptd"), 0.5)
        self.team_rtd = max(tot("rtd"), 0.5)
        self.build_players()
        # players who have since left (traded, released) took their usage with them:
        # hand it to the teammates who are still here
        if latest is not None:
            self.drop([pid for pid in list(self.players) if latest.get(pid) not in (None, team)])

    def drop(self, player_ids):
        """Take injured/inactive players out and hand their share to teammates,
        so the team's volume still goes somewhere (it does not just vanish)."""
        gone = [i for i in player_ids if i in self.players]
        if not gone:
            return []
        for field in ("tgt_share", "car_share", "rec_td_share", "rush_td_share", "qb_share"):
            before = sum(max(v[field], 0) for v in self.players.values())
            after = before - sum(max(self.players[i][field], 0) for i in gone)
            if after > 0:
                f = before / after
                for i, v in self.players.items():
                    if i not in gone:
                        v[field] = max(v[field], 0) * f
        for i in gone:
            del self.players[i]
        return gone

    def build_players(self):
        r = self.rows
        pos_group = r.groupby("player_id").position_group.last()
        players = {}
        for pid, g in r.groupby("player_id"):
            first = g.order.min()
            gs = [o for o in self.orders if o >= first]
            appeared = set(g.order)
            # A game with no stat line counts at MISS_WEIGHT: he may have been hurt or unused,
            # and we cannot tell which. Full weight would bake injuries into every rate and
            # make a healthy starter look worse than he is when he plays.
            gw = np.array([self.w[o] * (1.0 if o in appeared else MISS_WEIGHT) for o in gs])
            wsum = float(gw.sum())
            ws = g.w.values

            def rate(c):
                return float((g[c].fillna(0).values * ws).sum() / wsum)

            idx = [self.orders.index(o) for o in gs]
            Wg = gw
            bg = self.by_game.iloc[idx]

            def share(c, tc):
                den = float((bg[tc].values * Wg).sum())
                return float((g[c].fillna(0).values * ws).sum() / den) if den > 0 else 0.0

            players[pid] = dict(
                name=g.player_display_name.iloc[-1], pos=g.position.iloc[-1], group=pos_group[pid],
                games=len(g), window=len(gs), wsum=wsum,
                tgt_share=share("targets", "tgt"), car_share=share("carries", "car"),
                rec_td_share=share("receiving_tds", "ptd"), rush_td_share=share("rushing_tds", "rtd"),
                catch=(float((g.receptions.fillna(0).values * ws).sum()) + 8 * 0.66)
                / (float((g.targets.fillna(0).values * ws).sum()) + 8),
                ypr=(float((g.receiving_yards.fillna(0).values * ws).sum()) + 6 * 11.0)
                / (float((g.receptions.fillna(0).values * ws).sum()) + 6),
                ypc=(float((g.rushing_yards.fillna(0).values * ws).sum()) + 40 * 4.3)
                / (float((g.carries.fillna(0).values * ws).sum()) + 40),
                fum=rate("rushing_fumbles_lost") + rate("receiving_fumbles_lost") + rate("sack_fumbles_lost"),
                solo=rate("def_tackles_solo"), ast=rate("def_tackle_assists"), sacks=rate("def_sacks"),
                dint=rate("def_interceptions"), pd=rate("def_pass_defended"), ff=rate("def_fumbles_forced"),
                fr=rate("fumble_recovery_opp"), dtd=rate("def_tds"),
                # kickers: pull a thin sample toward the league's ~1.7 made FG per team game
                fgm=(float((g.fg_made.fillna(0).values * ws).sum()) + 5 * 1.7) / (wsum + 5),
                xpm=rate("pat_made"), att=rate("attempts"),
                att_total=float(g.attempts.fillna(0).sum()),
                qb_share=share("attempts", "att"),
            )
        self.players = players


def kick_pts_per_make(pw, team_orders=None) -> float:
    return PTS["fg_avg"]


def simulate_game(home: TeamModel, away: TeamModel, spread_home: float, total: float, defs, lg_def, rng, S, box=None):
    """Returns {player_id: (name, team, pos, draws[S])} plus a small environment summary.

    box: optional dict. When given it is filled with every player's simulated stat line
    (box[pid] = dict of arrays) and box["_game"] with the margin, total, team points and team stats,
    so a full box score and DraftKings/FanDuel scoring can be built from the same simulated games."""
    margin = rng.normal(spread_home, 13.2, S)
    tot = np.clip(rng.normal(total, 9.0, S), 17, None)
    pts = {home.team: np.clip((tot + margin) / 2, 0, None), away.team: np.clip((tot - margin) / 2, 0, None)}
    ctx = {}
    teams = ((home, away, margin), (away, home, -margin))
    sim = {}
    for off, dfn, mg in teams:
        t = off.tend
        # --- volume
        # 1.025: the pbp play filter drops kneels/spikes/aborted snaps that the box score counts
        pace = t["plays_pg"] * 1.025 * (tot / total) ** 0.35
        plays = np.clip(rng.normal(pace, 6.0, S), 40, 85)
        script = np.clip(-mg / 14.0, -1, 1) * 0.7              # + trailing, - leading
        # trailing (script > 0): add that coach's trailing boost; leading: add his (negative) leading boost
        pr = t["pass_all"] + np.where(script > 0, t["trail_boost"] * script, t["lead_boost"] * (-script))
        pr = np.clip(pr + rng.normal(0, 0.035, S), 0.30, 0.78)
        dropbacks = np.rint(plays * pr).astype(int)
        carries = np.rint(plays - dropbacks).astype(int)
        d = defs.loc[dfn.team] if dfn.team in defs.index else None
        ypa = off.off["ypa"] + (0.7 * (d["ypa"] - lg_def["ypa"]) if d is not None else 0)
        ypc = off.off["ypc"] + (0.6 * (d["ypc"] - lg_def["ypc"]) if d is not None else 0)
        sack_rate = np.clip(((d["sack"] if d is not None else lg_def["sack"]) * 0.7 + lg_def["sack"] * 0.3), 0.01, 0.2)
        if OL_SCALE and off.ol_missing:
            m_ = off.ol_missing * OL_SCALE
            sack_rate = np.clip(sack_rate + _OL_COEF["sack_rate"]["beta"] * m_, 0.01, 0.25)
            ypa = ypa + _OL_COEF["ypa"]["beta"] * m_
            ypc = ypc + _OL_COEF["ypc"]["beta"] * m_
        int_rate = off.off["int"] * 0.6 + (d["int"] if d is not None else lg_def["int"]) * 0.4
        sacks = rng.binomial(dropbacks, sack_rate)
        att = dropbacks - sacks
        pass_yds = np.clip(att * ypa + rng.normal(0, 11.5, S) * np.sqrt(np.maximum(att, 1)), 0, None)
        comp = rng.binomial(att, np.clip(off.off["cmp"] + 0.0, 0.45, 0.8))
        ints = rng.binomial(att, np.clip(int_rate, 0.005, 0.06))
        rush_yds = np.clip(carries * ypc + rng.normal(0, 7.0, S) * np.sqrt(np.maximum(carries, 1)) / 1.0, 0, None)
        # --- touchdowns / kicks
        tds = rng.poisson(0.76 * pts[off.team] / 7.0)
        p_pass = np.clip(0.57 * (t["rz_pass"] / 0.503) * (pr / max(t["pass_all"], 0.35)) ** 0.5, 0.30, 0.85)
        ptd = rng.binomial(tds, p_pass)
        rtd = tds - ptd
        fgm = rng.poisson(0.075 * pts[off.team])
        xpm = rng.binomial(tds, 0.94)
        sim[off.team] = dict(plays=plays, dropbacks=dropbacks, att=att, carries=carries, comp=comp, pass_yds=pass_yds,
                             rush_yds=rush_yds, ints=ints, ptd=ptd, rtd=rtd, fgm=fgm, xpm=xpm, sacks=sacks)
    out = {}
    for off, dfn in ((home, away), (away, home)):
        s, o = sim[off.team], sim[dfn.team]
        pl = off.players
        # ----- offense: shares (normalized per bucket so sums stay coherent)
        def norm(keys, field, cap_other=0.0):
            v = np.array([max(pl[k][field], 0.0) for k in keys])
            tot_ = v.sum()
            other = max(1 - tot_, 0.02)
            return np.append(v, other) / (tot_ + other)

        skill = [k for k, v in pl.items() if v["group"] in ("QB", "RB", "WR", "TE")]
        tk = [k for k in skill if pl[k]["tgt_share"] > 0.004]
        ck = [k for k in skill if pl[k]["car_share"] > 0.004]
        tdk = [k for k in skill if pl[k]["rec_td_share"] > 0 or pl[k]["tgt_share"] > 0.02]
        rk = [k for k in skill if pl[k]["rush_td_share"] > 0 or pl[k]["car_share"] > 0.02]
        # target, carry, TD allocation
        Z = np.zeros(S)
        draws = {k: dict(rec=Z, rec_yd=Z, rush=Z, rush_yd=Z, rtd=Z, rcd=Z, pass_yd=Z, ptd=Z, ints=Z) for k in skill}
        if tk:
            p = norm(tk, "tgt_share")
            tgt = rng.multinomial(s["att"], p)           # S x (len+1)
            catch = np.array([pl[k]["catch"] for k in tk])
            rec = rng.binomial(tgt[:, :-1], catch)
            ypr = np.array([pl[k]["ypr"] for k in tk])
            raw = rec * ypr * rng.gamma(6.0, 1 / 6.0, rec.shape)
            others_rec = np.maximum(s["comp"] - rec.sum(1), 0)
            tot_raw = raw.sum(1) + others_rec * 9.0
            scale = np.where(tot_raw > 0, s["pass_yds"] / np.maximum(tot_raw, 1e-6), 1.0)
            ryd = raw * scale[:, None]
            w = np.array([pl[k]["rec_td_share"] * 0.5 + pl[k]["tgt_share"] * 0.5 for k in tdk]) if tdk else None
            for i, k in enumerate(tk):
                draws[k]["rec"], draws[k]["rec_yd"] = rec[:, i], ryd[:, i]
            if tdk:
                w = np.append(w, 0.03)
                w = w / w.sum()
                rt = rng.multinomial(s["ptd"], w)
                for i, k in enumerate(tdk):
                    draws[k]["rcd"] = rt[:, i]
        if ck:
            p = norm(ck, "car_share")
            car = rng.multinomial(s["carries"], p)
            ypc = np.array([pl[k]["ypc"] for k in ck])
            raw = car[:, :-1] * ypc * rng.gamma(8.0, 1 / 8.0, car[:, :-1].shape)
            tot_raw = raw.sum(1) + car[:, -1] * 4.0
            scale = np.where(tot_raw > 0, s["rush_yds"] / np.maximum(tot_raw, 1e-6), 1.0)
            ry = raw * scale[:, None]
            for i, k in enumerate(ck):
                draws[k]["rush"], draws[k]["rush_yd"] = car[:, i], ry[:, i]
            wr = np.array([pl[k]["rush_td_share"] * 0.5 + pl[k]["car_share"] * 0.5 for k in rk]) if rk else None
            if rk:
                wr = np.append(wr, 0.02)
                wr = wr / wr.sum()
                rt = rng.multinomial(s["rtd"], wr)
                for i, k in enumerate(rk):
                    draws[k]["rtd"] = rt[:, i]
        # QB passing credit: split among passers by attempt share
        # QBs play in order of workload in the window. The first one plays unless he sits
        # that sim (his availability), then the next in line takes the whole game.
        qbs = sorted([k for k in skill if pl[k]["group"] == "QB" and pl[k]["att_total"] > 15],
                     key=lambda k: -pl[k]["att_total"])[:3]
        if qbs:
            taken = np.zeros(len(s["att"]), dtype=bool)
            for i, k in enumerate(qbs):
                av = 1.0 if i == len(qbs) - 1 else off.avail.get(k, 1.0)
                plays_ = (~taken) & (rng.random(len(taken)) < av)
                taken |= plays_
                draws[k]["pass_yd"] = np.where(plays_, s["pass_yds"], 0.0)
                draws[k]["ptd"] = np.where(plays_, s["ptd"], 0)
                draws[k]["ints"] = np.where(plays_, s["ints"], 0)
                if i == 0:
                    pass
        for k in skill:
            v = draws[k]
            touches = v["rec"] + v["rush"]
            fum = rng.poisson(touches * 0.006 + (0.04 if pl[k]["group"] == "QB" else 0.0))
            pts_ = (v["pass_yd"] * PTS["pass_yd"] + v["ptd"] * PTS["pass_td"] + v["ints"] * PTS["int"]
                    + v["rush_yd"] * PTS["rush_yd"] + v["rtd"] * PTS["rush_td"]
                    + v["rec"] * PTS["rec"] + v["rec_yd"] * PTS["rec_yd"] + v["rcd"] * PTS["rec_td"]
                    + fum * PTS["fum_lost"])
            out[k] = (pl[k]["name"], off.team, pl[k]["group"], pts_.astype(np.float32))
            if box is not None:
                box[k] = dict(name=pl[k]["name"], team=off.team, group=pl[k]["group"],
                              pass_yd=v["pass_yd"], ptd=v["ptd"], ints=v["ints"], rush=v["rush"], rush_yd=v["rush_yd"],
                              rtd=v["rtd"], rec=v["rec"], rec_yd=v["rec_yd"], rcd=v["rcd"], fum=fum)
        # ----- kickers: share of the team's simulated field goals and extra points
        for k, v in pl.items():
            if v["pos"] != "K":
                continue
            ratio = s["fgm"] / max(float(s["fgm"].mean()), 0.3)
            n_fg = rng.poisson(np.maximum(v["fgm"], 0.3) * ratio)
            pts_ = n_fg * PTS["fg_avg"] + s["xpm"] * PTS["xp"]
            out[k] = (v["name"], off.team, "K", pts_.astype(np.float32))
            if box is not None:
                box[k] = dict(name=v["name"], team=off.team, group="K", fg=n_fg, xp=s["xpm"])
    # ----- defenders face the OTHER offense's simulated plays
    for dfn, opp in ((home, away), (away, home)):
        o = sim[opp.team]
        for k, v in dfn.players.items():
            if v["group"] not in ("DL", "LB", "DB"):
                continue
            if v["solo"] + v["ast"] + v["sacks"] < 0.05:
                continue
            f_play = o["plays"] / 62.0          # their rates were earned against ~62 opponent plays
            f_pass = o["dropbacks"] / 36.0
            g = rng.gamma(8.0, 1 / 8.0, S)
            lam = lambda x, f: x * f * g
            solo = rng.poisson(np.clip(lam(v["solo"], f_play), 0, None))
            ast = rng.poisson(np.clip(lam(v["ast"], f_play), 0, None))
            sck = rng.poisson(np.clip(v["sacks"] * f_pass * g, 0, None))
            dint = rng.poisson(np.clip(v["dint"] * f_pass, 0, None))
            pdf = rng.poisson(np.clip(v["pd"] * f_pass * g, 0, None))
            ff = rng.poisson(np.clip(v["ff"] * f_play, 0, None))
            fr = rng.poisson(np.clip(v["fr"] * f_play, 0, None))
            dtd = rng.poisson(np.clip(v["dtd"] * f_play, 0, None))
            pts_ = (solo * PTS["solo"] + ast * PTS["ast"] + sck * PTS["sack"] + dint * PTS["def_int"] + pdf * PTS["pd"]
                    + ff * PTS["ff"] + fr * PTS["fr"] + dtd * PTS["def_td"])
            out[k] = (v["name"], dfn.team, v["group"], pts_.astype(np.float32))
            if box is not None:
                box[k] = dict(name=v["name"], team=dfn.team, group=v["group"], solo=solo, ast=ast, sck=sck,
                              dint=dint, pdf=pdf, ff=ff, fr=fr, dtd=dtd)
    if box is not None:
        box["_game"] = dict(home=home.team, away=away.team, margin=margin, tot=tot, pts=pts, sim=sim)
    env = {t: {k: float(np.mean(x)) for k, x in s.items()} for t, s in sim.items()}
    env["_pts"] = {t: float(np.mean(x)) for t, x in pts.items()}
    return out, env
