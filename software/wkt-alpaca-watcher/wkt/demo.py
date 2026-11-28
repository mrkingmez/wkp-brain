"""Offline demo. Fictional symbols, fictional prices, seeded random numbers, no network.
Replays hourly bars through the same engine the live scan uses."""
import copy
import datetime as dt
import math
import random

from .engine import ET, HOUR, Watcher

DEMO_SYMBOLS = ["DEMX", "ALFA", "BRVO", "CHAR", "DLTA"]   # fictional tickers. DEMX is the fictional market gauge.


def make_series(seed, start_price, days, start_date, drift_bias=0.0):
    rng = random.Random(seed)
    bars, price, d = [], start_price, start_date
    regime, left = 0.0004, 30
    n_days = 0
    while n_days < days:
        if d.weekday() < 5:
            for hr in range(9, 16):
                t = dt.datetime(d.year, d.month, d.day, hr, 0, tzinfo=ET).astimezone(dt.timezone.utc)
                left -= 1
                if left <= 0:
                    regime = rng.choice([0.0006, 0.0003, -0.0004, 0.0, 0.0008]) + drift_bias
                    left = rng.randint(15, 45)
                r = regime + rng.gauss(0, 0.0045)
                o, c = price, price * math.exp(r)
                wick = abs(rng.gauss(0, 0.0025))
                v = int(abs(rng.gauss(300000, 80000)) * (3.0 if rng.random() < 0.06 else 1.0)) + 1000
                bars.append({"t": t, "o": o, "h": max(o, c) * (1 + wick), "l": min(o, c) * (1 - wick), "c": c, "v": v})
                price = c
            n_days += 1
        d += dt.timedelta(days=1)
    return bars


def scan_times(bars):
    """Scan at 9:31 ET each day (sees the prior day's last closed bar) and at the end of each bar except the last."""
    by_day = {}
    for b in bars:
        by_day.setdefault(b["t"].astimezone(ET).date(), []).append(b)
    times = []
    for d, bs in sorted(by_day.items()):
        times.append(dt.datetime(d.year, d.month, d.day, 9, 31, tzinfo=ET).astimezone(dt.timezone.utc))
        times += [b["t"] + HOUR for b in bs[:-1]]
    return times


def view_at(all_bars, now):
    """Bars visible at 'now': closed bars in full, the bar in progress shows only its open (no future peeking)."""
    out = {}
    for s, bs in all_bars.items():
        vis = [b for b in bs if b["t"] + HOUR <= now]
        forming = next((b for b in bs if b["t"] <= now < b["t"] + HOUR), None)
        if forming is not None:
            vis = vis + [dict(forming, h=forming["o"], l=forming["o"], c=forming["o"], v=0)]
        out[s] = vis
    return out


UTC = dt.timezone.utc


def aggregate_daily(bars):
    """Hourly demo bars -> daily bars stamped at midnight ET (the way Alpaca stamps daily bars)."""
    by = {}
    for b in bars:
        by.setdefault(b["t"].astimezone(ET).date(), []).append(b)
    out = []
    for d, bs in sorted(by.items()):
        t = dt.datetime(d.year, d.month, d.day, 0, 0, tzinfo=ET).astimezone(UTC)
        out.append({"t": t, "o": bs[0]["o"], "h": max(x["h"] for x in bs), "l": min(x["l"] for x in bs),
                    "c": bs[-1]["c"], "v": sum(x["v"] for x in bs)})
    return out


def make_daily_history(seed, end_price, n, before_date, drift=0.0004):
    """n fictional weekday daily bars ending the weekday before before_date. Rescaled so the last close equals end_price."""
    rng = random.Random(seed * 101 + 5)
    days, d = [], before_date
    while len(days) < n:
        d -= dt.timedelta(days=1)
        if d.weekday() < 5:
            days.append(d)
    days.reverse()
    price, raw = 100.0, []
    for d in days:
        o = price
        c = price * math.exp(drift + rng.gauss(0, 0.011))
        raw.append({"t": dt.datetime(d.year, d.month, d.day, 0, 0, tzinfo=ET).astimezone(UTC), "o": o, "h": max(o, c) * 1.004,
                    "l": min(o, c) * 0.996, "c": c, "v": 1000000})
        price = c
    k = end_price / raw[-1]["c"]
    return [dict(b, o=b["o"] * k, h=b["h"] * k, l=b["l"] * k, c=b["c"] * k) for b in raw]


def daily_view(hist, full_daily, now):
    """Daily bars visible at `now`: the fictional history plus every demo day that has fully finished."""
    today = now.astimezone(ET).date()
    return {s: hist[s] + [b for b in full_daily[s] if b["t"].astimezone(ET).date() < today] for s in hist}


def run_demo(cfg, outdir, days=45, seed=7):
    c = copy.deepcopy(cfg)
    c["symbols"], c["market_gauge"] = list(DEMO_SYMBOLS), "DEMX"
    c["regime"]["min_breadth_symbols"] = 3        # the demo has 5 fictional symbols, not 20
    start = dt.date(2026, 1, 5)  # a Monday, fictional calendar use only
    allb = {"DEMX": make_series(seed, 400.0, days, start, 0.0002)}
    for i, s in enumerate(DEMO_SYMBOLS[1:], 1):
        allb[s] = make_series(seed + i, 50.0 + 40 * i, days, start)
    full_daily = {s: aggregate_daily(bs) for s, bs in allb.items()}
    hist = {s: make_daily_history(seed + i, allb[s][0]["o"], 230, start) for i, s in enumerate(DEMO_SYMBOLS)}
    w = Watcher(c, outdir, "demo")
    times = [t for t in scan_times(allb["DEMX"]) if t > allb["DEMX"][70]["t"]]
    totals = {"scans": 0, "decisions": 0, "trades_opened": 0, "trades_closed": 0, "zac_trades_opened": 0, "zac_trades_closed": 0}
    for now in times:
        daily = daily_view(hist, full_daily, now) if w.needs_daily(now, now.astimezone(ET).date()) else None
        s = w.scan(now, view_at(allb, now), ["demo-no-network"], clock_open=True, daily=daily)
        totals["scans"] += 1
        for k in ("decisions", "trades_opened", "trades_closed", "zac_trades_opened", "zac_trades_closed"):
            totals[k] += s[k]
    totals["closed_by_end_rule"] = w.close_out(times[-1]) if c["end_rule"]["close_open_at_last_close"] else 0
    return w, totals
