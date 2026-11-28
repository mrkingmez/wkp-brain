"""WKT Alpaca paper watcher. Paper only. Read-only Alpaca calls. No order code exists in this program.

  python -I run.py --demo                 offline, fictional data, no network, no keys
  python -I run.py --smoke                one read-only scan, writes to watch-week\\test (not counted)
  python -I run.py --counted --loop       counted watch week (locked until GO-COUNTED.flag exists)
  python -I run.py --counted --scan-once  one counted scan
  python -I run.py --scorecard [--counted|--demo]   rebuild scorecard.md
Keys are read only from the user's environment variables by name (see run_watcher.ps1)."""
import argparse
import datetime as dt
import json
import os
import statistics
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)  # python -I drops the script folder from the path, our own code needs it

from wkt import guards, scorecard  # noqa: E402
from wkt.alpaca import AlpacaReadOnly  # noqa: E402
from wkt.config import config_hash, load_config  # noqa: E402
from wkt.engine import ET, HOUR, Watcher, filter_session, parse_bars  # noqa: E402

WATCH_WEEK = r"D:\WKP\Investing\watch-week"
DEMO_DIR = os.path.join(HERE, "demo-out")


def test_dir():
    return os.path.join(WATCH_WEEK, "test")


def utcnow():
    return dt.datetime.now(dt.timezone.utc)


def parse_clock(r):
    d = r.data if isinstance(r.data, dict) else {}
    return bool(d.get("is_open")) if r.ok else None, d


def _closed_counts(bars, now):
    return {s: sum(1 for b in sb if b["t"] + HOUR <= now) for s, sb in bars.items()}


def live_scan(w, cl, cfg, clock_required):
    c = cl.clock()
    is_open, cd = parse_clock(c)
    now = utcnow()
    if clock_required and not is_open:
        w._log(now, {"scan_id": now.strftime("%Y%m%dT%H%M%SZ"), "feed": cfg["feed"], "request_ids": [c.request_id], "clock_open": bool(is_open),
                     "config_hash": w.chash}, "*", "SKIP", "market closed (or clock unreadable) per /v2/clock, no scan", fresh=False)
        w.out.save_state(w.st)
        return None, cd
    start = (now - dt.timedelta(days=cfg["bars_lookback_days"])).strftime("%Y-%m-%dT%H:%M:%SZ")
    raw, rids, err = cl.bars(cfg["symbols"], start, cfg["timeframe"])
    bars = None if raw is None else {s: parse_bars(rows) for s, rows in raw.items()}
    dropped = 0
    if bars is not None:
        for s in list(bars):
            bars[s], n = filter_session(bars[s], cfg)
            dropped += n
    rids = ([c.request_id] if c.request_id else []) + rids
    daily, today_date = None, now.astimezone(ET).date()
    w.info = {}
    if bars is not None:
        cc = _closed_counts(bars, now)
        w.info["extended_hours_bars_dropped"] = dropped
        w.info["hourly_rows_per_symbol"] = {s: len(r) for s, r in raw.items()}
        w.info["hourly_closed_bars_min_median_max"] = [min(cc.values()), statistics.median(cc.values()), max(cc.values())]
        w.info["min_bars_filter"] = cfg["filters"]["min_bars"]
        w.info["symbols_under_min_bars_now"] = sorted(s for s, n in cc.items() if n < cfg["filters"]["min_bars"])
        gauge = bars.get(cfg["market_gauge"]) or []
        if gauge:
            w.info["gauge_first_bar_utc"], w.info["gauge_last_bar_utc"] = gauge[0]["t"].strftime("%Y-%m-%dT%H:%M:%SZ"), gauge[-1]["t"].strftime("%Y-%m-%dT%H:%M:%SZ")
            w.info["gauge_bar_start_times_et"] = sorted({b["t"].astimezone(ET).strftime("%H:%M") for b in gauge})
        try:   # bars that will still be inside the lookback window at the next open, and 3 days later (a Monday after a Friday open)
            no = dt.datetime.fromisoformat(str(cd.get("next_open"))).astimezone(dt.timezone.utc)
            for label, shift in (("next_open", 0), ("next_open_plus_3_days", 3)):
                ps = no + dt.timedelta(days=shift) - dt.timedelta(days=cfg["bars_lookback_days"])
                pc = {s: sum(1 for b in sb if b["t"] >= ps and b["t"] + HOUR <= now) for s, sb in bars.items()}
                w.info["projected_%s_min_median_max" % label] = [min(pc.values()), statistics.median(pc.values()), max(pc.values())]
                w.info["projected_%s_symbols_under_min_bars" % label] = sorted(s for s, n in pc.items() if n < cfg["filters"]["min_bars"])
        except (ValueError, TypeError):
            w.info["projected_min_median_max"] = "not available (next_open unreadable)"
        if w.needs_daily(now, today_date):
            w._daily_try = now
            dstart = (now - dt.timedelta(days=cfg["regime"]["daily_lookback_days"])).strftime("%Y-%m-%dT%H:%M:%SZ")
            rawd, ridd, errd = cl.bars(cfg["symbols"], dstart, "1Day")
            rids = rids + ridd
            if rawd is not None:
                daily = {s: parse_bars(rows) for s, rows in rawd.items()}
                w.info["daily_rows_per_symbol_min_median_max"] = [min(len(r) for r in rawd.values()), statistics.median(len(r) for r in rawd.values()), max(len(r) for r in rawd.values())]
            else:
                w.info["daily_fetch_error"] = errd
        w.info["response_shapes"] = getattr(cl, "shapes", {})
    return w.scan(now, bars, rids, err, clock_open=bool(is_open), daily=daily), cd


def main(argv=None, client_factory=None, sleep=time.sleep):
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--demo", action="store_true")
    g.add_argument("--smoke", action="store_true")
    g.add_argument("--scorecard", action="store_true")
    ap.add_argument("--counted", action="store_true")
    ap.add_argument("--loop", action="store_true")
    ap.add_argument("--scan-once", action="store_true")
    ap.add_argument("--daily-note", metavar="YYYY-MM-DD")
    ap.add_argument("--config", default=os.path.join(HERE, "config.yaml"))
    a = ap.parse_args(argv)
    cfg = load_config(a.config)

    if a.demo:
        from wkt.demo import run_demo
        import shutil
        if os.path.isdir(DEMO_DIR):
            shutil.rmtree(DEMO_DIR)
        w, totals = run_demo(cfg, DEMO_DIR)
        sc = scorecard.build_scorecard(DEMO_DIR, cfg, note="DEMO: fictional data, not a result.", chash=w.chash)
        scorecard.write_daily_note(DEMO_DIR, sorted({d["ts_utc"][:10] for d in scorecard.read_decisions(os.path.join(DEMO_DIR, "decisions.jsonl"))})[3], os.path.join(DEMO_DIR, "state.json"))
        print("demo:", totals, {k: sc[k] for k in ("evals", "fresh", "counted", "opened", "closed", "wins", "gross", "net", "zac_opened", "zac_closed", "zac_net") if k in sc})
        print("outputs in", DEMO_DIR)
        return 0

    if a.scorecard or a.daily_note:
        if a.counted:
            guards.counted_gate(WATCH_WEEK, True)
        d = WATCH_WEEK if a.counted else (test_dir() if os.path.isdir(test_dir()) else DEMO_DIR)
        if a.scorecard:
            scorecard.build_scorecard(d, cfg, chash=config_hash(cfg) if a.counted else None)
        if a.daily_note:
            scorecard.write_daily_note(d, a.daily_note, os.path.join(d, "state.json"))
        print("done in", d)
        return 0

    # live (read-only) paths from here on
    if a.counted:
        guards.counted_gate(WATCH_WEEK, True)
        outdir, mode = WATCH_WEEK, "counted"
    elif a.smoke:
        outdir, mode = test_dir(), "test"
    else:
        print("choose --demo, --smoke, --counted or --scorecard"); return 2
    key, secret, base = guards.load_env()
    cl = (client_factory or AlpacaReadOnly)(key, secret, base)
    w = Watcher(cfg, outdir, mode)
    if w.recovered:
        print("recovered %d log record(s) left by an interrupted scan (no duplicates written)" % w.recovered, flush=True)
    last_day = cfg["end_rule"]["last_day"]
    if a.counted and w.st.get("ended"):
        print("the end rule was already applied (last day %s). Nothing to scan. Change config.yaml (new hash, counts restart) to run again." % last_day)
        return 0

    if a.counted and utcnow().astimezone(ET).date().isoformat() > last_day:
        n = w.close_out(utcnow())     # the last day passed without the loop finishing it: apply the end rule now
        scorecard.build_scorecard(outdir, cfg, chash=w.chash)
        print("end rule applied late (last day %s): %d open paper position(s) closed at the last mark" % (last_day, n))
        return 0

    if a.smoke:
        acct, pos = cl.account(), cl.positions()
        summ, cd = live_scan(w, cl, cfg, clock_required=False)
        ad = acct.data if isinstance(acct.data, dict) else {}
        ids = {"account": [acct.status, acct.request_id], "positions": [pos.status, pos.request_id]}
        facts = {"account_fields_seen": sorted(ad.keys()),
                 "account_safe_values": {k: ad.get(k) for k in ("status", "trading_blocked", "pattern_day_trader", "daytrade_count", "currency", "equity", "multiplier") if k in ad},
                 "positions_count": len(pos.data) if isinstance(pos.data, list) else "not a list",
                 "clock_fields_seen": sorted(cd.keys())}
        with open(os.path.join(outdir, "smoke-preflight.json"), "w", encoding="utf-8") as f:
            json.dump({"ts_utc": utcnow().isoformat(), "calls": ids, "clock": {k: cd.get(k) for k in ("is_open", "next_open", "next_close")},
                       "scan": summ, "config_hash": w.chash, "facts": facts, "info": w.info, "regime": w.st.get("regime")}, f, indent=1, default=str)
        print("smoke scan:", summ, "calls:", ids)
        print("facts:", json.dumps(facts, default=str))
        print("info:", json.dumps(w.info, default=str))
        print("regime:", json.dumps(w.st.get("regime"), default=str))
        return 0

    last_date = None
    while True:
        if a.counted and w.st.get("ended"):
            break
        summ, cd = live_scan(w, cl, cfg, clock_required=True)
        if summ is not None:
            last_date = utcnow().astimezone(ET).date().isoformat()
            print(utcnow().strftime("%H:%M:%S"), "scan:", summ, flush=True)
        if not a.loop:
            break
        confirmed_closed = summ is None and (cd or {}).get("is_open") is False   # an unreadable clock is NOT closed
        today_et = utcnow().astimezone(ET).date().isoformat()
        end_due = a.counted and confirmed_closed and today_et >= last_day    # also when this process never scanned today (restart after the close)
        if confirmed_closed and (last_date or end_due):   # market closed after we scanned today: apply the end rule if due, write the notes and stop
            last_date = last_date or today_et
            if a.counted and last_date >= last_day:
                n = w.close_out(utcnow())
                print("end rule applied: %d open paper position(s) closed at the last mark" % n, flush=True)
            scorecard.write_daily_note(outdir, last_date, w.out.state_path)
            scorecard.build_scorecard(outdir, cfg, chash=w.chash)
            break
        sleep(cfg["scan_interval_seconds"] if summ is not None else 30)
    return 0


if __name__ == "__main__":
    sys.exit(main())
