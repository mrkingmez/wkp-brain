"""Win and cover probabilities for the pick'em card, from the live market.

The card line is frozen on Monday; the market keeps moving. For each NFL game this
measures how far the card sits from today's median line and turns that into a
cover probability, using the real spread of NFL results around closing lines
(measured from nflverse schedules, last 10 seasons).

python pickem_probs.py 2026 6 [--odds <json>]
Reads the card lines and picks from tracker\\predictions.csv (model rows for that week).
"""
import sys
from math import erf, sqrt
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import run_week as rw

season, week = int(sys.argv[1]), int(sys.argv[2])
odds = sys.argv[sys.argv.index("--odds") + 1] if "--odds" in sys.argv else r"D:\WKP\scratch\wk6_odds.json"
Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))

g = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
h = g[(g.season >= 2016) & (g.season < season) & (g.game_type == "REG") & g.result.notna() & g.spread_line.notna()]
sigma = float((h.result - h.spread_line).std())
print(f"Real NFL margin around the closing line: sd {sigma:.2f} points over {len(h)} games\n")

lines = rw.market_lines(odds)
t = pd.read_csv(r"D:\WKP\Fantasy-Football\tracker\predictions.csv")
t = t[(t.season == season) & (t.week == week) & (t.source == "model")]
rows = []
for _, r in t.iterrows():
    mk = lines.get((r.away_team.replace("LAR", "LA").replace("WSH", "WAS"), r.home_team.replace("LAR", "LA").replace("WSH", "WAS")))
    if not mk:
        continue
    m, tot = mk
    card = float(r.line_used)
    home_is_ats = r.pick_ats == r.home_team
    # home covers the card line if margin > card
    p_home_cover = 1 - Phi((card - m) / sigma)
    p_ats = p_home_cover if home_is_ats else 1 - p_home_cover
    p_home_win = Phi(m / sigma)
    p_su = p_home_win if r.pick_su == r.home_team else 1 - p_home_win
    rows.append(dict(game=f"{r.away_team} @ {r.home_team}", ats_pick=r.pick_ats, card_line_home=card, market_home=round(m, 1),
                     gap=round(m - card, 1), p_cover=round(p_ats, 3), su_pick=r.pick_su, p_win=round(p_su, 3)))
d = pd.DataFrame(rows).sort_values("p_cover", ascending=False)
pd.set_option("display.width", 200)
print(d.to_string(index=False))
print(f"\nExpected ATS wins from these {len(d)} NFL picks: {d.p_cover.sum():.1f} ({d.p_cover.mean():.1%} per pick)")
print(f"Expected straight-up wins: {d.p_win.sum():.1f} of {len(d)}")
print("\nEliminator ranking (win probability from market spread, higher is safer):")
e = []
this_week = set(zip(g[(g.season == season) & (g.week == week)].away_team, g[(g.season == season) & (g.week == week)].home_team))
for (a, hm), (m, tot) in lines.items():
    if (a, hm) not in this_week:        # the odds feed also carries next week's games
        continue
    e.append((hm, Phi(m / sigma)))
    e.append((a, 1 - Phi(m / sigma)))
for team, p in sorted(e, key=lambda x: -x[1])[:8]:
    print(f"   {team:4s} {p:.1%}")
d.to_csv(Path(r"D:\WKP\data\ff-simulator") / f"pickem_probs_{season}_wk{week}.csv", index=False)
