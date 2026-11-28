"""Regime and trend tag from daily bars (free IEX data). Pure functions, no network.
Tags: UPTREND_CALM, UPTREND_VOLATILE, RANGE, DOWNTREND_CALM, DOWNTREND_VOLATILE, UNKNOWN.
UNKNOWN (short history, bad or missing bars, too few symbols for breadth) counts as FAIL: no size step-up.
Thresholds live in config.yaml under regime and are frozen with the score."""
import statistics
from zoneinfo import ZoneInfo

from . import indicators, scoring

ET = ZoneInfo("America/New_York")
TAGS = ("UPTREND_CALM", "UPTREND_VOLATILE", "RANGE", "DOWNTREND_CALM", "DOWNTREND_VOLATILE", "UNKNOWN")


def _unknown(why):
    return {"tag": "UNKNOWN", "detail": {"why": why}}


def _closed_days(bars, today_date):
    """Completed daily bars only: drop today's forming bar and anything later."""
    out = [b for b in (bars or []) if b["t"].astimezone(ET).date() < today_date]
    return out


def compute(daily, cfg, today_date):
    """daily: dict symbol -> parsed daily bars. Returns {'tag', 'detail'}."""
    R, gauge = cfg["regime"], cfg["market_gauge"]
    if not isinstance(daily, dict):
        return _unknown("no daily data")
    g = _closed_days(daily.get(gauge), today_date)
    fast, slow, slope_n = R["sma_fast"], R["sma_slow"], R["slope_days"]
    need = max(slow, fast + slope_n, R["vol_median_days"] + R["atr_period"])
    if len(g) < need:
        return _unknown("gauge %s has %d daily bars, need %d" % (gauge, len(g), need))
    bad = scoring.bars_valid(g)
    if bad:
        return _unknown("gauge daily bars: " + bad)
    closes = [b["c"] for b in g]
    c = closes[-1]
    sma_f = sum(closes[-fast:]) / fast
    sma_s = sum(closes[-slow:]) / slow
    sma_f_prev = sum(closes[-fast - slope_n:-slope_n]) / fast
    slope_up = sma_f > sma_f_prev
    # breadth proxy: share of the watch list above its own fast average
    above = n = 0
    for s in cfg["symbols"]:
        sb = _closed_days(daily.get(s), today_date)
        if len(sb) >= fast and scoring.bars_valid(sb[-fast:]) is None:
            n += 1
            above += 1 if sb[-1]["c"] > sum(x["c"] for x in sb[-fast:]) / fast else 0
    if n < R["min_breadth_symbols"]:
        return _unknown("breadth needs %d symbols with %d daily bars, got %d" % (R["min_breadth_symbols"], fast, n))
    breadth = above / n
    atrs = indicators.atr(g, R["atr_period"])
    pct = [a / b["c"] * 100.0 for a, b in zip(atrs, g) if a is not None]
    cur = pct[-1]
    med = statistics.median(pct[-R["vol_median_days"]:])
    if not (indicators.finite(cur) and indicators.finite(med) and med > 0):
        return _unknown("volatility not computable")
    volatile = cur > med * R["vol_ratio_volatile"]
    bmin = R["breadth_min_up"]
    if c > sma_f and sma_f > sma_s and slope_up and breadth >= bmin:
        trend = "UPTREND"
    elif c < sma_f and sma_f < sma_s and not slope_up and breadth <= 1 - bmin:
        trend = "DOWNTREND"
    else:
        trend = "RANGE"
    tag = "RANGE" if trend == "RANGE" else trend + ("_VOLATILE" if volatile else "_CALM")
    return {"tag": tag, "detail": {"close": round(c, 4), "sma_fast": round(sma_f, 4), "sma_slow": round(sma_s, 4),
                                   "slope_up": slope_up, "atr_pct": round(cur, 4), "atr_pct_median": round(med, 4),
                                   "breadth": round(breadth, 3), "breadth_symbols": n, "daily_bars": len(g),
                                   "last_daily_bar_date": g[-1]["t"].astimezone(ET).date().isoformat()}}
