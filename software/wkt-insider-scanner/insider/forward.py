"""Forward-return scoring. PURE functions: bars in, numbers out. No network, no files, no clock.

Entry rule (never the insider's own price): see entry_index (ruling 1). Acceptance time unknown = the open of the first trading day strictly AFTER the filing date. The Zac-can-act ledger enters
zac_extra_trading_days later (assumption in config). h trading days held = open of the entry day to the CLOSE of the entry
day + h - 1. Compared with SPY over the same two dates. Haircut: bps each side on the stock leg (same ladder as the watcher),
SPY gross. A missing bar is UNKNOWN, a horizon that has not happened yet is PENDING. Both are kept and counted, never dropped.
Data: Alpaca IEX daily bars, read-only, feed=iex (the free account cannot read SIP). IEX volume is thin, so dollar volume is an under-count."""
import datetime as dt
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")


def to_daily(parsed_bars):
    """Parsed bars ({'t': aware datetime, o,h,l,c,v}) -> sorted daily rows with a date key. Bad rows are dropped here and counted by the caller."""
    out, seen = [], set()
    for b in parsed_bars or []:
        try:
            d = b["t"].astimezone(ET).date()
            row = {"d": d, "o": float(b["o"]), "h": float(b["h"]), "l": float(b["l"]), "c": float(b["c"]), "v": float(b["v"])}
        except (KeyError, TypeError, ValueError, AttributeError):
            continue
        if not all(x == x and abs(x) != float("inf") for x in (row["o"], row["c"], row["v"])) or row["o"] <= 0 or row["c"] <= 0 or d in seen:
            continue
        seen.add(d)
        out.append(row)
    out.sort(key=lambda r: r["d"])
    return out


def first_index_after(days, date):
    for i, r in enumerate(days):
        if r["d"] > date:
            return i
    return None


def entry_index(spy, signal, cfg):
    """RULING 1. Returns (index into spy or None, basis label). signal is the cluster's signal dict (date, instant_et, basis) or a bare date string
    (date only). Time known and at or before the pre-market cutoff on a trading day: that day's open. Otherwise the next trading day's open,
    labeled, because daily bars cannot price a first trade that happens during the session (so this is later than the true first trade, never earlier)."""
    if isinstance(signal, str):
        signal = {"date": signal, "basis": "date_only", "instant_et": None}
    d = dt.date.fromisoformat(signal["date"])
    if signal.get("basis") == "time" and signal.get("instant_et"):
        t = dt.datetime.fromisoformat(signal["instant_et"])
        hh, mm = str(cfg["timing"]["premarket_entry_cutoff_et"]).split(":")
        if t.time() <= dt.time(int(hh), int(mm), 0):
            for i, r in enumerate(spy):
                if r["d"] == d:
                    return i, "same_day_open(accepted_before_cutoff)"
        return first_index_after(spy, d), "next_open_after_acceptance(daily_bars_cannot_price_an_intraday_first_trade)"
    return first_index_after(spy, d), "next_open_after_filing_date(acceptance_time_unavailable)"


def listing_status(stock, spy, sig_date, cfg):
    """RULING 4. (status, age in trading days). Age = benchmark trading days from the stock's first bar up to the signal date (the first IEX bar is a
    HEURISTIC for the first listed trade). SEASONED if at least the minimum. NEW_LISTING if younger and the first bar sits inside the fetched
    history (so the stock really began trading then). Otherwise UNKNOWN (not enough history before the signal to tell), and UNKNOWN is FAIL."""
    f = cfg["forward"]
    if not stock:
        return "UNKNOWN", None
    first = stock[0]["d"]
    age = sum(1 for r in spy if first <= r["d"] < sig_date)
    if age >= f["min_listing_age_trading_days"]:
        return "SEASONED", age
    if spy and first > spy[0]["d"] + dt.timedelta(days=7):
        return "NEW_LISTING", age
    return "UNKNOWN", age


def cost_side_bps(quote, cfg):
    """RULING 5. Cost each side in bps = max(floor, half the measured spread as a percent of the mid). Returns (bps, basis).
    The spread comes from a logged bid and ask at entry. None or a crossed or zero quote = the floor, labeled spread_unmeasured."""
    floor = float(cfg["forward"]["cost_floor_bps"])
    try:
        bid, ask = float(quote["bid"]), float(quote["ask"])
        if bid > 0 and ask >= bid and ask != float("inf") and ask == ask:
            half = (ask - bid) / ((ask + bid) / 2.0) / 2.0 * 1e4
            return max(floor, half), ("measured_half_spread" if half > floor else "floor(measured_half_spread_smaller)")
    except (TypeError, ValueError, KeyError):
        pass
    return floor, "floor(spread_unmeasured)"


def fill_status(entry_bar, quote, entry_date, cfg):
    """RULING 5. (status, reason). FILLED only when a first-trade time inside the window was measured. UNFILLED when there is no IEX print at all
    on the entry day or the first print came after the window. FILL_UNKNOWN when there is a bar but no intraday data to check the first trade time
    (never counted as filled). Fractional-share eligibility on the broker is NOT VERIFIED and is not used."""
    if entry_bar is None:
        return "UNFILLED", "no_iex_print_on_entry_day"
    ft = (quote or {}).get("first_trade_et")
    if not ft:
        return "FILL_UNKNOWN", "first_trade_time_not_measured(daily bars only)"
    try:
        t = dt.datetime.fromisoformat(ft).astimezone(ET)
    except (ValueError, TypeError):
        return "FILL_UNKNOWN", "first_trade_time_unreadable"
    if t.date() != entry_date:
        return "FILL_UNKNOWN", "first_trade_time_not_on_entry_day"
    mins = (t - dt.datetime.combine(entry_date, dt.time(9, 30), tzinfo=ET)).total_seconds() / 60.0
    if mins > cfg["forward"]["fill_window_minutes"]:
        return "UNFILLED", "first_iex_print_%d_minutes_after_the_open" % round(mins)
    return "FILLED", None


def net_return(o, c, bps):
    fe = o * (1 + bps / 1e4)
    fx = c * (1 - bps / 1e4)
    return fx / fe - 1.0


def liquidity_tags(stock, entry_date, entry_open, cfg):
    f = cfg["forward"]
    tags = []
    if entry_open is not None and entry_open < f["min_price"]:
        tags.append("illiquid_price")
    prior = [r for r in stock if r["d"] < entry_date][-f["liquidity_lookback_days"]:]
    if len(prior) < max(1, f["liquidity_lookback_days"] // 2):
        tags.append("liquidity_unknown")
    else:
        adv = sum(r["c"] * r["v"] for r in prior) / len(prior)
        if adv < f["min_avg_dollar_volume"]:
            tags.append("illiquid_volume")
    return tags


def score_ledger(stock, spy, signal, extra_days, cfg, quote_for=None, bench_days=None):
    """quote_for(entry_date_iso) -> {'bid','ask','first_trade_et'} or None. Optional: logged and used for the cost and the fill check."""
    f = cfg["forward"]
    benches = dict(bench_days) if bench_days else {}
    benches.setdefault(f["benchmark"], spy)
    bmaps = {n: {r["d"]: r for r in days} for n, days in benches.items()}
    i0, basis = entry_index(spy, signal, cfg)
    res = {"entry_date": None, "entry_open": None, "entry_basis": basis, "horizons": {}, "tags": [],
           "entry_quote": None, "fill": {"status": "PENDING", "reason": "entry day has not happened yet"},
           "cost_side_bps": float(f["cost_floor_bps"]), "cost_basis": "floor(spread_unmeasured)", "fractional_eligible": "UNKNOWN(not verified on the broker)"}
    if i0 is None:
        for h in f["horizons"]:
            res["horizons"][str(h)] = {"state": "PENDING", "why": "no trading day after the filing date in the benchmark bars yet"}
        return res
    i = i0 + extra_days
    if i >= len(spy):
        for h in f["horizons"]:
            res["horizons"][str(h)] = {"state": "PENDING", "why": "entry day has not happened yet"}
        res["entry_date"] = None
        return res
    entry = spy[i]["d"]
    res["entry_date"] = entry.isoformat()
    sbd = {r["d"]: r for r in stock}
    eb = sbd.get(entry)
    if eb is None:
        for h in f["horizons"]:
            res["horizons"][str(h)] = {"state": "UNKNOWN", "why": "no stock bar on the entry day"}
        res["tags"].append("no_entry_bar")
        res["fill"] = dict(zip(("status", "reason"), fill_status(None, None, entry, cfg)))
        if stock and stock[-1]["d"] < entry:
            res["tags"].append("DELISTED_OR_ENDED")       # the bars stop before we could even enter: not dropped, flagged
        return res
    res["entry_open"] = eb["o"]
    res["tags"] += liquidity_tags(stock, entry, eb["o"], cfg)
    q = None
    if quote_for:
        try:
            q = quote_for(entry.isoformat())
        except Exception:
            q = None
    res["entry_quote"] = ({"bid": q.get("bid"), "ask": q.get("ask"), "first_trade_et": q.get("first_trade_et")} if isinstance(q, dict) else None)
    res["cost_side_bps"], res["cost_basis"] = cost_side_bps(q, cfg)
    if res["cost_basis"].startswith("floor(spread_unmeasured") and "spread_unmeasured" not in res["tags"]:
        res["tags"].append("spread_unmeasured")
    res["fill"] = dict(zip(("status", "reason"), fill_status(eb, q, entry, cfg)))
    for h in f["horizons"]:
        j = i + h - 1
        if j >= len(spy):
            res["horizons"][str(h)] = {"state": "PENDING", "why": "exit day has not happened yet"}
            continue
        exit_d = spy[j]["d"]
        xb = sbd.get(exit_d)
        marked = None
        if xb is None and stock and stock[-1]["d"] < exit_d:
            # RULING 2: the stock's bars stop before the exit day (delisted, halted, or no later IEX prints). Never dropped:
            # marked to the last available print and flagged.
            marked = max(r["d"] for r in stock if r["d"] < exit_d)
            xb = sbd[marked]
            if "DELISTED_OR_ENDED" not in res["tags"]:
                res["tags"].append("DELISTED_OR_ENDED")
        if xb is None:
            res["horizons"][str(h)] = {"state": "UNKNOWN", "why": "no stock bar on the exit day", "exit_date": exit_d.isoformat()}
            if "bars_end_early_or_gap" not in res["tags"]:
                res["tags"].append("bars_end_early_or_gap")
            continue
        spy_ret = spy[j]["c"] / spy[i]["o"] - 1.0
        bench_ret, bench_missing = {}, []
        for n, bm in bmaps.items():
            b0, b1 = bm.get(entry), bm.get(exit_d)
            if b0 is None or b1 is None:
                bench_missing.append(n)
            else:
                bench_ret[n] = b1["c"] / b0["o"] - 1.0
        missing_required = sorted(set(f["benchmarks"]) - set(bench_ret))
        gross = xb["c"] / eb["o"] - 1.0
        net = {str(b): net_return(eb["o"], xb["c"], b) for b in f["haircut_bps"]}
        net_cost = net_return(eb["o"], xb["c"], res["cost_side_bps"])
        res["horizons"][str(h)] = {"state": "OK", "exit_date": exit_d.isoformat(), "gross": gross, "spy": spy_ret, "net": net,
                                   "excess": {k: v - spy_ret for k, v in net.items()},
                                   "net_cost": net_cost, "excess_cost": net_cost - spy_ret, "round_trip_cost_bps": 2 * res["cost_side_bps"],
                                   "bench": bench_ret, "excess_cost_by_bench": {n: net_cost - r for n, r in bench_ret.items()},
                                   "excess_by_bench": {n: {k: v - r for k, v in net.items()} for n, r in bench_ret.items()},
                                   "bench_missing": missing_required}
        if marked:
            res["horizons"][str(h)].update({"marked_to_last_print": True, "last_print_date": marked.isoformat()})
    return res


def score_cluster(cluster, stock_days, spy_days, regime_tag, cfg, quote_for=None, bench_days=None):
    """One record for a COUNTED cluster. stock_days None or empty = no bars at all (dead, not on IEX or bad ticker): tagged, UNKNOWN."""
    if not cluster.get("counted"):
        raise ValueError("only COUNTED clusters are scored")
    sig = cluster.get("signal") or cluster.get("signal_filing_date") or cluster["last_filing_date"]
    stock = stock_days or []
    tags = []
    if not stock:
        tags.append("no_bars_at_all(possible_delisting_not_on_iex_or_bad_ticker)")
    ledgers = {"main": score_ledger(stock, spy_days, sig, 0, cfg, quote_for, bench_days),
               "zac": score_ledger(stock, spy_days, sig, cfg["forward"]["zac_extra_trading_days"], cfg, quote_for, bench_days)}
    sig_date = dt.date.fromisoformat(sig["date"] if isinstance(sig, dict) else sig)
    missing = (not stock) or stock[0]["d"] > sig_date
    if stock and stock[0]["d"] > sig_date:
        tags.append("no_bars_before_signal(ticker_reuse_or_new_listing: bars belong to a later company or listing)")
    if missing:
        for L in ledgers.values():
            for h in L["horizons"].values():
                if h.get("state") != "PENDING":
                    h["state"] = "MISSING"
            if L["fill"]["status"] != "PENDING":
                L["fill"] = {"status": "UNFILLED", "reason": "no_usable_bars(OTC, foreign, delisted, bad ticker or ticker reuse)"}
    for L in ledgers.values():
        for t in L["tags"]:
            if t not in tags:
                tags.append(t)
    excluded = None
    if not missing:
        ls, age = listing_status(stock, spy_days, sig_date, cfg)
        if ls == "NEW_LISTING":
            excluded = "new_listing_within_%d_trading_days(age %d, heuristic: first IEX bar)" % (cfg["forward"]["min_listing_age_trading_days"], age)
        elif ls == "UNKNOWN":
            excluded = "listing_age_UNKNOWN(not enough bar history before the signal, UNKNOWN is FAIL)"
    data_status = "MISSING" if missing else ("DELISTED_OR_ENDED" if "DELISTED_OR_ENDED" in tags else "OK")
    return {"cluster_id": cluster["cluster_id"], "ticker": cluster["issuer"]["ticker"], "issuer_cik": cluster["issuer"]["cik"],
            "cluster_type": cluster["cluster_type"], "signal": sig if isinstance(sig, dict) else None,
            "signal_filing_date": sig["date"] if isinstance(sig, dict) else sig, "regime": regime_tag or "UNKNOWN",
            "tags": tags, "data_status": data_status, "excluded": excluded, "ledgers": ledgers, "benchmark": cfg["forward"]["benchmark"], "benchmarks": list(cfg["forward"]["benchmarks"]), "feed": "iex",
            "entry_rule": "first trade after the acceptance time of the filing that completed the cluster (daily bars: that day's open if accepted before the cutoff, else the next trading day's open); plus zac_extra_trading_days (zac)"}
