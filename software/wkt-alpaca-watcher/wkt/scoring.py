"""Hard filters first (cheap), then setup scoring on closed 1-hour bars. Long only.
UNKNOWN or missing data is FAIL. Score points and rule thresholds come from config. Indicator periods (EMA 20/50, Bollinger 20, MACD 12/26/9, stochastic 14/3, ADX 14, volume average 20, 20-bar high) and the market-mood weights are fixed in code."""
from .indicators import enrich, finite

NEEDED_LAST = ("ema20", "ema50", "rsi", "atr", "bb_lo", "macd_hist", "stoch_k", "stoch_d", "adx", "vol_ratio", "hi20")
NEEDED_PREV = ("rsi", "bb_lo", "macd_hist", "stoch_k", "adx")


def bars_valid(bars):
    """Return reason string if the bar data is unusable (UNKNOWN), else None."""
    for b in bars:
        for k in ("o", "h", "l", "c", "v"):
            if not finite(b.get(k)):
                return "UNKNOWN: bad value in bar field " + k
        if b["c"] <= 0 or b["h"] < b["l"] or b["v"] < 0:
            return "UNKNOWN: impossible bar"
    return None


def hard_filters(bars, cfg, now_utc):
    """Cheap checks before any indicator math. Returns None if pass, else FAIL reason."""
    f = cfg["filters"]
    if not bars:
        return "FAIL: UNKNOWN no bars"
    if len(bars) < f["min_bars"]:
        return "FAIL: UNKNOWN only %d bars, need %d" % (len(bars), f["min_bars"])
    bad = bars_valid(bars)
    if bad:
        return "FAIL: " + bad
    age_days = (now_utc - bars[-1]["t"]).total_seconds() / 86400.0
    if age_days > f["max_stale_days"]:
        return "FAIL: stale data, last bar %.1f days old" % age_days
    if bars[-1]["c"] < f["min_price"]:
        return "FAIL: price under minimum"
    last = bars[-20:]
    adv = sum(b["c"] * b["v"] for b in last) / len(last)
    if adv < f["min_avg_dollar_volume_1h"]:
        return "FAIL: average hourly dollar volume under minimum"
    return None


def market_mood(bars, cfg, now_utc):
    """-1..+1 from the gauge symbol. Returns None (UNKNOWN) if it cannot be computed."""
    if hard_filters(bars, cfg, now_utc):
        return None
    e = enrich(bars)
    c = bars[-1]["c"]
    vals = (e["ema20"][-1], e["ema50"][-1], e["macd_hist"][-1])
    if not all(finite(v) for v in vals):
        return None
    m = 0.4 if c > vals[1] else -0.4
    m += 0.3 if vals[0] > vals[1] else -0.3
    m += 0.3 if vals[2] > 0 else -0.3
    return max(-1.0, min(1.0, m))


def evaluate(bars, mood, cfg):
    """Returns (best_candidate or None, note). Candidate has setup, score, parts, entry, atr, bar_t.
    UNKNOWN indicator values return (None, 'FAIL: UNKNOWN ...')."""
    S, R = cfg["scoring"], cfg["rules"]
    if mood is None:
        return None, "FAIL: UNKNOWN market mood"
    e = enrich(bars, R["atr_period"])
    for k in NEEDED_LAST:
        if not finite(e[k][-1]):
            return None, "FAIL: UNKNOWN indicator " + k
    for k in NEEDED_PREV:
        if not finite(e[k][-2]):
            return None, "FAIL: UNKNOWN previous " + k
    b, p = bars[-1], bars[-2]
    L = {k: e[k][-1] for k in e}
    P = {k: e[k][-2] for k in e}
    if L["atr"] <= 0:
        return None, "FAIL: UNKNOWN atr not positive"
    stretch = (b["c"] - L["ema20"]) / L["atr"]
    uptrend = L["ema20"] > L["ema50"] and b["c"] > L["ema50"]
    downtrend = L["ema20"] < L["ema50"] and b["c"] < L["ema50"]
    trending = L["adx"] >= S["adx_trending"]
    cands = []

    pb = S["pullback"]
    if uptrend and b["l"] <= L["ema20"] + pb["atr_touch"] * L["atr"] and b["c"] > L["ema20"] and b["c"] > b["o"]:
        c = {"base": S["base"]}
        c["rsi_reset"] = pb["rsi_pts"] if pb["rsi_lo"] <= L["rsi"] <= pb["rsi_hi"] and L["rsi"] > P["rsi"] else 0
        c["momentum_turn"] = pb["macd_pts"] if L["macd_hist"] > P["macd_hist"] else 0
        c["trend_strength"] = pb["trend_pts"] if trending else 0
        cands.append(("trend_pullback", c))

    mr = S["mean_reversion"]
    if p["c"] < P["bb_lo"] and b["c"] > L["bb_lo"] and P["rsi"] < mr["prev_rsi_max"] and L["rsi"] > P["rsi"]:
        c = {"base": S["base"]}
        c["range_regime"] = mr["range_pts"] if L["adx"] < S["adx_range"] else (
            mr["semi_range_pts"] if L["adx"] < S["adx_trending"] else mr["trend_penalty"])
        c["deep_oversold"] = mr["deep_pts"] if P["rsi"] < mr["deep_rsi"] else 0
        c["stoch_turn"] = mr["stoch_pts"] if L["stoch_k"] > L["stoch_d"] and P["stoch_k"] < mr["stoch_low"] else 0
        if downtrend and trending:
            c["falling_knife"] = mr["knife_pts"]
        cands.append(("mean_reversion", c))

    bo = S["breakout"]
    if b["c"] > L["hi20"] and L["vol_ratio"] >= bo["vol_ratio_min"] and not downtrend:
        c = {"base": S["base"]}
        c["volume_surge"] = bo["vol_big_pts"] if L["vol_ratio"] >= bo["vol_ratio_big"] else bo["vol_pts"]
        c["trend_strength"] = bo["trend_pts"] if trending and L["adx"] > P["adx"] else 0
        c["close_near_high"] = bo["near_high_pts"] if (b["h"] - b["c"]) < bo["near_high_frac"] * (b["h"] - b["l"] + 1e-12) else 0
        cands.append(("breakout", c))

    if not cands:
        return None, "no setup on the latest closed bar"

    best = None
    for setup, c in cands:
        if stretch > S["stretch_far"]:
            c["overextended"] = S["stretch_far_pts"]
        elif stretch > S["stretch_mid"]:
            c["overextended"] = S["stretch_mid_pts"]
        c["volume"] = S["volume_good_pts"] if L["vol_ratio"] >= S["volume_good_ratio"] else (
            S["volume_bad_pts"] if L["vol_ratio"] < S["volume_bad_ratio"] else 0)
        c["market_mood"] = round(S["mood_weight"] * mood, 1)
        stop_pct = R["atr_stop_multiple"] * L["atr"] / b["c"] * 100
        if stop_pct > S["too_volatile_stop_pct"]:
            c["too_volatile"] = S["too_volatile_pts"]
        score = max(0.0, min(100.0, sum(c.values())))
        cand = {"setup": setup, "score": round(score, 1), "parts": c, "entry": b["c"], "atr": L["atr"], "bar_t": b["t"]}
        if best is None or cand["score"] > best["score"]:
            best = cand
    return best, "setup found"
