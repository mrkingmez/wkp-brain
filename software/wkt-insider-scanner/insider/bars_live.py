"""Live daily bars through the watcher's READ-ONLY Alpaca client (GET only, whitelisted paths, feed forced to iex, paper URL asserted,
keys read by environment variable NAME). NOT RUN in this build: needs the Alpaca keys in the environment. Nothing here can place an order."""
import datetime as dt
import sys

from . import forward


def make_quote_provider(cfg, transport=None):
    """RULING 5. Returns quote_for(ticker, entry_date_iso) -> {'bid': None, 'ask': None, 'first_trade_et': iso} or None.
    First trade time = the start of the first 1 minute IEX bar of the entry day, read through the watcher read-only client (GET, whitelisted
    bars path, feed=iex, 5 rows). BID AND ASK ARE NOT AVAILABLE: the quotes path is not on the watcher whitelist and this scanner may not edit
    the watcher, so the cost falls back to the floor and is tagged spread_unmeasured. NOT RUN LIVE in this build (no keys used)."""
    import urllib.parse
    wdir = cfg["forward"]["watcher_dir"]
    if wdir not in sys.path:
        sys.path.insert(0, wdir)
    from wkt import guards as wguards   # noqa: E402
    from wkt.alpaca import AlpacaReadOnly, DATA_HOST   # noqa: E402
    key, secret, base = wguards.load_env()
    cl = AlpacaReadOnly(key, secret, base, transport=transport)
    cache = {}

    def quote_for(ticker, entry_iso):
        k = (ticker, entry_iso)
        if k in cache:
            return cache[k]
        d = dt.date.fromisoformat(entry_iso)
        qs = {"symbols": ticker, "timeframe": "1Min", "start": "%sT13:00:00Z" % d.isoformat(), "end": "%sT21:00:00Z" % d.isoformat(),
              "limit": "5", "feed": "iex", "adjustment": "raw"}
        out = None
        try:
            r = cl.get("https://%s/v2/stocks/bars?%s" % (DATA_HOST, urllib.parse.urlencode(qs)))
            rows = ((r.data or {}).get("bars") or {}).get(ticker) if r.ok and isinstance(r.data, dict) else None
            if rows and isinstance(rows[0], dict) and rows[0].get("t"):
                t = dt.datetime.fromisoformat(str(rows[0]["t"]).replace("Z", "+00:00"))
                out = {"bid": None, "ask": None, "first_trade_et": t.astimezone(forward.ET).isoformat()}
        except Exception:
            out = None
        cache[k] = out
        return out
    return quote_for


def fetch_daily(cfg, symbols, start_date, transport=None):
    """Returns (parsed_by_symbol, daily_by_symbol, errors). parsed_by_symbol is in the watcher's bar format (regime module input)."""
    wdir = cfg["forward"]["watcher_dir"]
    if wdir not in sys.path:
        sys.path.insert(0, wdir)
    from wkt import guards as wguards   # noqa: E402
    from wkt.alpaca import AlpacaReadOnly   # noqa: E402
    from wkt.engine import parse_bars   # noqa: E402
    key, secret, base = wguards.load_env()
    cl = AlpacaReadOnly(key, secret, base, transport=transport)
    parsed, daily, errors = {}, {}, []
    syms = sorted(set(symbols))
    start_iso = dt.datetime(start_date.year, start_date.month, start_date.day, tzinfo=dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for i in range(0, len(syms), 40):
        chunk = syms[i:i + 40]
        raw, rids, err = cl.bars(chunk, start_iso, "1Day")
        if raw is None:
            errors.append("bars request failed for %d symbols: %s" % (len(chunk), err))
            continue
        for s, rows in raw.items():
            p = parse_bars(rows)
            parsed[s] = p
            daily[s] = forward.to_daily(p)
    return parsed, daily, errors
