"""Cover probability for a frozen card line against today's market line (NFL). Built 2026-11-12, decision FF-2026-11-12-02.

The old label used a smooth curve: Phi(gap / 13.2). Real NFL margins bunch on 3, 7 and 10, so a half point across one of
those numbers is worth more than the curve says. This blends the curve with what really happened in games whose closing
line sat within half a point of today's market line (nflverse schedules, every season before the current one from 2003).

    p, n = cover_prob(card_home, market_home)        # chance the HOME side covers the card line; n = real games used
    python cover_table.py <card_home> <market_home>

Lines are home-positive (home favored by 3.5 = +3.5), the same convention as tracker\\predictions.csv.
Walk-forward test 2016 to 2025 (19,304 cases, gaps of 1 to 3 points both ways): log loss 0.68090 for the curve,
0.67997 for this blend; the raw table alone is worse (0.68199), which is why it is shrunk toward the curve (N0 = 150).
College: no table. Use Phi(gap / 15.0).
"""
import sys
from functools import lru_cache
from math import erf, sqrt

import numpy as np
import pandas as pd

SIGMA, N0, BAND = 13.2, 150, 0.5
Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))


@lru_cache(maxsize=4)
def _hist(before_season):
    g = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    h = g[(g.season >= 2003) & (g.season < before_season) & (g.game_type == "REG") & g.result.notna() & g.spread_line.notna() & (g.spread_line != 0)]
    return h.spread_line.abs().values, np.where(h.spread_line > 0, h.result, -h.result)


def cover_prob(card_home, market_home, before_season=2026):
    p_norm = 1 - Phi((card_home - market_home) / SIGMA)
    if market_home == 0:
        return p_norm, 0
    favl, favm = _hist(before_season)
    m = (favl >= abs(market_home) - BAND) & (favl <= abs(market_home) + BAND)
    n = int(m.sum())
    if n == 0:
        return p_norm, 0
    if market_home > 0:                       # home is the market favorite: home covers when its margin beats the card line
        p_emp = float((favm[m] > card_home).mean())
    else:                                     # away is the favorite: home covers when the favorite wins by less than -card
        p_emp = float((favm[m] < -card_home).mean()) if float(-card_home) != int(-card_home) else float((favm[m] <= -card_home).mean())
    return (n * p_emp + N0 * p_norm) / (n + N0), n


HOOK = 0.53


def pick_side(card_home, market_home, before_season=2026):
    """The card pick for one NFL game: ("H" or "A", label, chance the pick covers).

    Gap rule (unchanged, venture CLAUDE.md rule 2): market 2+ points off the card = LEAN, 1 to 1.9 = SLIGHT, both on the
    market's side. Under 1 point = NO EDGE. New on 2026-11-12 for NO EDGE games: if the table gives one side 53 percent or
    more (a half point across 3 or 7), take that side and call it HOOK; otherwise the frozen card underdog as before.
    Walk-forward 2016 to 2025 on half-point gaps: table side at 53+ won 54.1 percent (n=1,062), frozen underdog 51.8 on the
    same games. The frozen underdog alone, all half-point games: 50.7 percent (n=2,554)."""
    p_home, n = cover_prob(card_home, market_home, before_season)
    gap = market_home - card_home
    if abs(gap) >= 1.0:
        side = "H" if gap > 0 else "A"
        return side, ("LEAN" if abs(gap) >= 2 else "SLIGHT"), (p_home if side == "H" else 1 - p_home)
    if max(p_home, 1 - p_home) >= HOOK:
        side = "H" if p_home > 0.5 else "A"
        return side, "HOOK", max(p_home, 1 - p_home)
    side = "A" if card_home > 0 else "H"          # frozen card underdog
    return side, "NO EDGE", (p_home if side == "H" else 1 - p_home)


if __name__ == "__main__":
    c, mk = float(sys.argv[1]), float(sys.argv[2])
    p, n = cover_prob(c, mk)
    print(f"home covers the card line {c:+.1f} with the market at {mk:+.1f}: {p:.1%} (curve {1 - Phi((c - mk) / SIGMA):.1%}, {n} real games)")
