"""Regression tests for the 2026-11-12 audit fixes. Uses the nflverse cache on disk (no network).

    python -I test_sim_fixes.py

1. Same inputs give the same numbers (fixed seed).
2. Changing one game's line leaves every other game's numbers untouched (one random stream per game).
3. A quarterback named in the overrides is the one credited with the passing, even with no history on that team.
4. A defender who changed teams is simulated on his new team; a receiver who changed teams is listed, not guessed.
5. Kicker spread is sane (the double-draw bug gave about 7.7 points against a real 4.35).
6. The injury builder no longer maps players with no ESPN id onto one shared bogus id.
"""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import run_week as rw

SEASON, WEEK, SIMS = 2026, 6, 600
_cache = {}


def base():
    if "b" not in _cache:
        _cache["b"] = rw.load_all(SEASON, WEEK)
    return _cache["b"]


def run(lines=None, **kw):
    tg, lg, pw, defs, lg_def, sched = base()
    ids, results, M, envs, dropped = rw.simulate_week(SEASON, WEEK, dict(lines or {}), tg, lg, pw, defs, lg_def, sched,
                                                      sims=SIMS, seed=2026, verbose=False, **kw)
    return ids, results, M, envs


class SimFixes(unittest.TestCase):
    def test_same_inputs_same_numbers(self):
        a, b = run(), run()
        self.assertEqual(a[0], b[0])
        self.assertTrue(np.array_equal(a[2], b[2]))

    def test_one_game_change_leaves_the_others_alone(self):
        ids, results, M, envs = run()
        key = sorted(envs)[0]
        away, home = key.split("@")
        e = envs[key]
        ids2, results2, M2, envs2 = run({(away, home): (e["spread_home"] + 6.0, e["total"])})
        touched = {away, home}
        same = [np.array_equal(M[i], M2[ids2.index(p)]) for i, p in enumerate(ids) if results[p][1] not in touched and p in ids2]
        moved = [not np.array_equal(M[i], M2[ids2.index(p)]) for i, p in enumerate(ids)
                 if results[p][1] in touched and results[p][2] == "QB" and p in ids2]
        self.assertTrue(len(same) > 500 and all(same))
        self.assertTrue(any(moved))

    def test_named_quarterback_gets_the_passing(self):
        ids, results, M, envs = run()
        team = results[ids[0]][1]
        notes = {}
        ids2, results2, M2, _ = run(qb_start={team: ("00-TESTQB", "Test Quarterback")}, notes=notes)
        self.assertIn("00-TESTQB", ids2)
        self.assertEqual(results2["00-TESTQB"][1:3], (team, "QB"))
        self.assertGreater(float(M2[ids2.index("00-TESTQB")].mean()), 8.0)
        self.assertIn((team, "Test Quarterback"), notes["qb_named"])

    def test_player_who_changed_teams(self):
        tg, lg, pw, defs, lg_def, sched = base()
        as_of = SEASON * 100 + WEEK
        recent = pw[(pw.order < as_of) & (pw.order >= as_of - 2)]
        d = recent[recent.position_group.isin(["DL", "LB", "DB"]) & (recent.def_tackles_solo.fillna(0) >= 3)].iloc[0]
        r = recent[recent.position_group.isin(["WR"]) & (recent.targets.fillna(0) >= 6)].iloc[0]
        wk = sched[(sched.season == SEASON) & (sched.week == WEEK)]
        new_d = next(t for t in list(wk.home_team) if t != d.team)
        new_r = next(t for t in list(wk.home_team) if t != r.team)
        notes = {}
        ids, results, M, _ = run(team_now={d.player_id: new_d, r.player_id: new_r}, notes=notes)
        self.assertIn(d.player_id, ids)
        self.assertEqual(results[d.player_id][1], new_d)
        # receivers who change teams: simulated at a reduced share (0.6 of the old target share) and always listed by name
        self.assertTrue(r.player_id in ids, "traded receiver has no projection")
        self.assertEqual(results[r.player_id][1], new_r)
        self.assertIn(r.player_display_name, [x[1] for x in notes["transfers_reduced_share"]])
        base_ids, base_res, base_M, _ = run()
        self.assertLess(float(M[ids.index(r.player_id)].mean()), float(base_M[base_ids.index(r.player_id)].mean()))

    def test_kicker_spread(self):
        ids, results, M, _ = run()
        k = [i for i, p in enumerate(ids) if results[p][2] == "K" and M[i].mean() > 5]
        self.assertGreater(len(k), 10)
        sd = float(np.mean([M[i].std() for i in k]))
        self.assertLess(sd, 6.8)
        self.assertGreater(sd, 3.0)

    def test_injury_builder_has_no_shared_bogus_id(self):
        src = (Path(__file__).parent / "build_injuries.py").read_text(encoding="utf-8")
        self.assertIn("BAD_KEYS", src)
        self.assertNotIn('df.loc[miss, "espn_id"].map(e2g)', src)
        import pandas as pd
        f = Path(r"D:\WKP\data\ff-simulator\injuries_2026_wk10.csv")
        if f.exists():
            d = pd.read_csv(f)
            ids_ = d.gsis_id.dropna()
            self.assertTrue(ids_.str.startswith("00-").all(), "a merged row carries a non-player id")


if __name__ == "__main__":
    unittest.main()
