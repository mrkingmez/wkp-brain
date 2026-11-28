"""WKT insider scanner. Read-only SEC Form 4 purchase clusters. Paper research only. No order code exists in this program.

  python -I run.py --demo                       offline, fictional filings and bars, no network, no keys
  python -I run.py --live --route daily --since 2026-11-16 --until 2026-11-25
                                                official SEC daily index plus one filing per Form 4 (needs LIVE-OK.flag and SEC_USER_AGENT)
  python -I run.py --live --route dataset --dataset-quarter 2025q4 --since 2025-10-01 --until 2025-12-31
                                                one SEC bulk file (history)
  python -I run.py --score                      forward returns for counted clusters (Alpaca read-only keys by name)
  python -I run.py --scorecard                  rebuild insider-scorecard.md
This signal has NO sizing and NO trade authority."""
import argparse
import datetime as dt
import os
import shutil
import socket
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)  # python -I drops the script folder from the path

from insider import VERSION, bars_live, demo, forward, guards, runner  # noqa: E402
from insider.config import ConfigChangeError, config_hash, load_config, record_config  # noqa: E402
from insider.sec_client import SecClient, SecStop  # noqa: E402
from insider import sources  # noqa: E402

WATCH_WEEK_INSIDER = r"D:\WKP\Investing\watch-week\insider"
DEMO_DIR = os.path.join(HERE, "demo-out")


def utcnow():
    return dt.datetime.now(dt.timezone.utc)


class _NoNet(socket.socket):
    def connect(self, *a, **k):
        raise AssertionError("network attempted in demo mode")


def demo_config(cfg):
    """The fictional demo filings are dated October and November 2026, so the freeze is moved back for the demo only (the demo hash differs from the real one)."""
    import copy
    c = copy.deepcopy(cfg)
    c["freeze"]["counted_signals_from_et"] = "2026-01-01T00:00:00"
    return c


def run_demo(cfg, outdir=DEMO_DIR, now=None, quiet=False):
    """Everything fictional. The socket class is replaced so any network attempt raises."""
    cfg = demo_config(cfg)
    real = socket.socket
    socket.socket = _NoNet
    try:
        now = now or dt.datetime(2026, 11, 26, 12, 0, tzinfo=dt.timezone.utc)
        if os.path.isdir(outdir):
            for n in ("clusters.jsonl", "skips.jsonl", "forward-returns.jsonl", "insider-scorecard.md", "config-history.jsonl"):
                p = os.path.join(outdir, n)
                if os.path.exists(p):
                    os.remove(p)
        os.makedirs(outdir, exist_ok=True)
        h, _, _ = record_config(cfg, os.path.join(outdir, "config-history.jsonl"), now.date().isoformat())
        run = runner.new_run(h, "demo", now)
        skips = []
        items = demo.demo_filings()
        filings = runner.parse_all(items, skips)
        clusters, allskips = runner.cluster_run(filings, skips, cfg, outdir, run, ["demo://fictional"], now.strftime("%Y-%m-%dT%H:%M:%SZ"))
        parsed = demo.demo_bars(cfg["forward"]["benchmark"])
        daily = {s: forward.to_daily(b) for s, b in parsed.items()}
        watcher = runner.load_watcher(cfg)
        wcfg = None
        if watcher:
            import copy
            wcfg = copy.deepcopy(watcher["cfg"])
            wcfg["symbols"] = [cfg["forward"]["benchmark"]] + demo.BREADTH
            wcfg["market_gauge"] = cfg["forward"]["benchmark"]
        regime_for = runner.make_regime_for(watcher, parsed, wcfg)
        recs = runner.score_run(clusters, lambda s: daily.get(s), regime_for, cfg, outdir, run)
        sc = runner.write_scorecard(outdir, cfg, h, now.strftime("%Y-%m-%d %H:%M UTC"), "demo (FICTIONAL data, not a result)")
        if not quiet:
            print("demo: %d clusters (%d counted), %d skips, %d forward records, scorecard %s" % (
                len(clusters), sum(1 for c in clusters if c["counted"]), len(allskips), len(recs), sc))
        return clusters, allskips, recs
    finally:
        socket.socket = real


def run_live(args, cfg):
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)
    guards.live_gate(outdir)
    ua = guards.load_user_agent(cfg)          # refuses to run if unset. The value is never printed or stored.
    now = utcnow()
    h, keys, new = record_config(cfg, os.path.join(outdir, "config-history.jsonl"), now.date().isoformat(), args.reason, args.allow_multi_change)
    run = runner.new_run(h, "live", now)

    def on_stop(status, host):
        with open(os.path.join(outdir, "SEC-STOP.flag"), "w", encoding="utf-8") as f:
            f.write("Stopped %s by HTTP %s from %s. Do not rerun until you have read the SEC fair access page and waited.\n" % (now.isoformat(), status, host))
    client = SecClient(cfg, ua, os.path.join(outdir, "cache"), on_stop=on_stop)
    until = dt.date.fromisoformat(args.until) if args.until else now.date()
    since = dt.date.fromisoformat(args.since) if args.since else until - dt.timedelta(days=cfg["sec"]["lookback_days"])
    skips = []
    try:
        if args.route == "daily":
            filings, skips, urls = sources.collect_live(client, cfg, since, until)
        else:
            url = args.dataset_url or "https://www.sec.gov/files/structureddata/data/insider-transactions-data-sets/%s_form345.zip" % args.dataset_quarter
            got = client.fetch(url)
            filings, skips, info = sources.filings_from_dataset_zip(got.body, url, got.fetched_utc, (since.isoformat(), until.isoformat()))
            urls = [url]
    except SecStop as e:
        print("STOPPED: %s" % e)
        return 2
    clusters, allskips = runner.cluster_run(filings, skips, cfg, outdir, run, urls, now.strftime("%Y-%m-%dT%H:%M:%SZ"))
    print("live: %d filings, %d clusters (%d counted), %d skips, %d requests, %d cache hits" % (
        len(filings), len(clusters), sum(1 for c in clusters if c["counted"]), len(allskips), client.requests_made, client.cache_hits))
    return 0


def run_score(args, cfg):
    from insider import logio
    outdir = args.outdir
    now = utcnow()
    h, _, _ = record_config(cfg, os.path.join(outdir, "config-history.jsonl"), now.date().isoformat(), args.reason, args.allow_multi_change)
    run = runner.new_run(h, "score", now)
    clusters = [c for c in logio.read_jsonl(os.path.join(outdir, "clusters.jsonl")) if c.get("config_hash") == h and c.get("counted")]
    uniq = {c["cluster_id"]: c for c in clusters}
    if not uniq:
        print("no counted clusters under this config hash: nothing to score")
        return 0
    watcher = runner.load_watcher(cfg)
    wsyms = watcher["cfg"]["symbols"] if watcher else []
    tickers = {c["issuer"]["ticker"] for c in uniq.values() if c["issuer"]["ticker"]}
    first_sig = min((c.get("signal_filing_date") or c["last_filing_date"]) for c in uniq.values())
    back = max(cfg["forward"]["listing_history_calendar_days"], int(watcher["cfg"]["regime"]["daily_lookback_days"]) + 30 if watcher else 60)
    start = dt.date.fromisoformat(first_sig) - dt.timedelta(days=back)
    parsed, daily, errors = bars_live.fetch_daily(cfg, list(tickers) + wsyms + list(cfg["forward"]["benchmarks"]), start)
    for e in errors:
        print("bars error: " + e)
    regime_for = runner.make_regime_for(watcher, parsed)
    try:
        quote_for = bars_live.make_quote_provider(cfg)
    except Exception as e:      # no keys or no watcher: score on daily bars only, fills stay FILL_UNKNOWN and costs use the floor
        print("entry quotes not available (%s): costs use the floor, fills are FILL_UNKNOWN" % type(e).__name__)
        quote_for = None
    recs = runner.score_run(list(uniq.values()), lambda s: daily.get(s), regime_for, cfg, outdir, run, quote_for)
    path = runner.write_scorecard(outdir, cfg, h, now.strftime("%Y-%m-%d %H:%M UTC"), "live")
    print("scored %d clusters, scorecard %s" % (len(recs), path))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="WKT insider scanner (paper research, read-only)")
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--backtest", action="store_true", help="design stub only: refuses, see docs/BACKTEST-DESIGN.md")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--score", action="store_true")
    ap.add_argument("--scorecard", action="store_true")
    ap.add_argument("--route", choices=["daily", "dataset"], default="daily")
    ap.add_argument("--dataset-quarter", default=None)
    ap.add_argument("--dataset-url", default=None)
    ap.add_argument("--since", default=None)
    ap.add_argument("--until", default=None)
    ap.add_argument("--outdir", default=WATCH_WEEK_INSIDER)
    ap.add_argument("--config", default=os.path.join(HERE, "config.yaml"))
    ap.add_argument("--reason", default=None)
    ap.add_argument("--allow-multi-change", action="store_true")
    args = ap.parse_args(argv)
    if args.backtest:
        print("NOT BUILT: backtest mode is a documented plan only (docs\\BACKTEST-DESIGN.md). Nothing was run.")
        return 4
    cfg = load_config(args.config)
    try:
        if args.live or args.score or args.scorecard:
            guards.assert_own_ledger(args.outdir, cfg)
        if args.demo:
            run_demo(cfg)
            return 0
        if args.live:
            if args.route == "dataset" and not (args.dataset_quarter or args.dataset_url):
                ap.error("--route dataset needs --dataset-quarter (like 2025q4) or --dataset-url")
            return run_live(args, cfg)
        if args.score:
            return run_score(args, cfg)
        if args.scorecard:
            h = config_hash(cfg)
            print(runner.write_scorecard(args.outdir, cfg, h, utcnow().strftime("%Y-%m-%d %H:%M UTC"), "rebuild"))
            return 0
    except (guards.GuardError, ConfigChangeError) as e:
        print("REFUSED: %s" % e)
        return 3
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
