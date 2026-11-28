"""Tests for the WKT Alpaca paper watcher. Run: python -I tests\\test_watcher.py
Fake key values below are obviously fake sentinels used only to prove nothing leaks."""
import atexit
import copy
import csv
import datetime as dt
import glob
import io
import json
import os
import re
import shutil
import socket
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import run as runmod  # noqa: E402
from wkt import alpaca, guards, logio, regime as regime_mod, risk, scoring, scorecard  # noqa: E402
from wkt import demo as demomod  # noqa: E402
from wkt.config import config_hash  # noqa: E402
from wkt.stats import bdays_between  # noqa: E402
from wkt.stats import net_at  # noqa: E402
from wkt.config import load_config, validate  # noqa: E402
from wkt.demo import make_series, run_demo, scan_times, view_at, DEMO_SYMBOLS  # noqa: E402
from wkt.engine import ET, HOUR, Watcher, iso, new_state, filter_session  # noqa: E402

CFG = load_config(os.path.join(ROOT, "config.yaml"))
SCRATCH = r"D:\WKP\scratch"
FAKE_KEY, FAKE_SECRET = "SENTINELKEYid00112233", "SENTINELSECRETvalue99887766"
UTC = dt.timezone.utc


def read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


_MADE = []


def tmpdir():
    os.makedirs(SCRATCH, exist_ok=True)
    d = tempfile.mkdtemp(prefix="wkt-test-", dir=SCRATCH)
    _MADE.append(d)
    return d


def _cleanup():   # tester F17: do not leave test folders behind
    for d in _MADE:
        shutil.rmtree(d, ignore_errors=True)


atexit.register(_cleanup)


def hbars(n, start, price=100.0, step=0.0):
    """n consecutive hourly bars (9 to 15 ET each weekday) starting at the given ET date."""
    out, d, p = [], start, price
    while len(out) < n:
        if d.weekday() < 5:
            for h in range(9, 16):
                if len(out) < n:
                    t = dt.datetime(d.year, d.month, d.day, h, tzinfo=ET).astimezone(UTC)
                    out.append({"t": t, "o": p, "h": p + 0.5, "l": p - 0.5, "c": p + step, "v": 500000})
                    p += step
        d += dt.timedelta(days=1)
    return out


def make_pos(entry_t, stop=95.0, target=105.0, entry=100.0, shares=100):
    return {"trade_id": "T0001", "shares": shares, "entry_raw": entry, "entry_fill": entry, "entry_fee": 0.0, "stop": stop,
            "target": target, "atr": 2.5, "risk_usd": shares * (entry - stop), "score": 85.0, "setup": "test",
            "entry_bar_t": iso(entry_t), "decision_id": "D000001"}


def exit_case(bars, **kw):
    d = tmpdir()
    w = Watcher(CFG, d, "test")
    pos = make_pos(bars[0]["t"], **kw)
    w.st["positions"]["AAA"] = pos
    w.st["cash"] = 0.0
    now = bars[-1]["t"] + HOUR
    summ = {"trades_opened": 0, "trades_closed": 0}
    summ.update(zac_trades_opened=0, zac_trades_closed=0)
    w._check_exit(now, {"scan_id": "x", "request_ids": []}, "main", w.st, "AAA", bars, summ)
    w.out.save_state(w.st)
    rows = scorecard.read_trades(w.out.trades)
    return w, rows, d


class TestRules(unittest.TestCase):
    def test_kill_switch_trips_at_minus_5_percent(self):
        self.assertTrue(risk.kill_switch_tripped(100000.0, 95000.0, CFG))
        self.assertTrue(risk.kill_switch_tripped(100000.0, 90000.0, CFG))
        self.assertFalse(risk.kill_switch_tripped(100000.0, 95001.0, CFG))
        self.assertFalse(risk.kill_switch_tripped(100000.0, 100000.0, CFG))
        self.assertTrue(risk.kill_switch_tripped(None, 95000.0, CFG), "UNKNOWN start equity must fail closed")

    def test_kill_switch_in_scan_blocks_new_trades_and_logs_kill(self):
        d = tmpdir()
        cfg = copy.deepcopy(CFG)
        cfg["symbols"] = ["DEMX", "ALFA", "AAA"]
        cfg["market_gauge"] = "DEMX"
        w = Watcher(cfg, d, "test")
        start = dt.date(2026, 1, 5)
        allb = {"DEMX": make_series(7, 400.0, 45, start, 0.0002), "ALFA": make_series(8, 90.0, 45, start),
                "AAA": hbars(len(make_series(7, 1, 45, start)), start, 95.0)}
        now = allb["DEMX"][200]["t"] + HOUR
        view = view_at(allb, now)
        view["AAA"] = [dict(b) for b in view["AAA"]]
        w.st["positions"]["AAA"] = make_pos(view["AAA"][-1]["t"] - HOUR * 3, stop=10.0, target=500.0, entry=100.0, shares=1000)
        w.st["positions"]["AAA"]["entry_fill"] = 100.0
        w.st["cash"] = 0.0     # equity now = 1000 shares x mark 95 = 95000
        w.st["day"] = {"date": now.astimezone(ET).date().isoformat(), "start_equity": 100000.0, "killed": False}
        w.scan(now, view, ["rid-1"], clock_open=True)
        self.assertTrue(w.st["day"]["killed"])
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertTrue(any(x["action"] == "KILL" for x in lines))
        self.assertFalse(any(x["action"] == "TRADE" for x in lines), "no new trades after the kill switch")
        self.assertTrue(any("kill switch" in x["reason"] for x in lines if x["symbol"] == "ALFA"))
        self.assertEqual(len(w.st["pending"]), 0)

    def test_position_cap_25_percent_in_sizing(self):
        shares, det = risk.size_shares(100000.0, 100000.0, 100.0, 0.1, 95.0, CFG)  # risk size would be 10000 shares
        self.assertEqual(shares, 250)
        self.assertLessEqual(shares * 100.0, 25000.0)
        self.assertEqual(det["binding"], "position cap")
        s2, d2 = risk.size_shares(100000.0, 10000.0, 100.0, 0.1, 95.0, CFG)
        self.assertEqual(s2, 100)
        self.assertEqual(d2["binding"], "cash")

    def test_risk_tiers(self):
        self.assertEqual(risk.risk_pct_for(69.9, CFG), 0.0)
        self.assertEqual(risk.risk_pct_for(70, CFG), 0.5)
        self.assertEqual(risk.risk_pct_for(79.9, CFG), 0.5)
        self.assertEqual(risk.risk_pct_for(80, CFG), 1.0)
        self.assertEqual(risk.risk_pct_for(89.9, CFG), 1.0)
        self.assertEqual(risk.risk_pct_for(90, CFG), 2.0)
        s, d = risk.size_shares(100000.0, 100000.0, 100.0, 1.0, 85.0, CFG)   # 1 percent = 1000 / (2 x 1) = 500, cap 250
        self.assertEqual(s, 250)
        s, d = risk.size_shares(100000.0, 100000.0, 100.0, 5.0, 85.0, CFG)   # 1000 / 10 = 100
        self.assertEqual((s, d["binding"]), (100, "risk"))

    def test_monday_needs_90(self):
        self.assertIsNotNone(risk.gate_reason(89.9, "Mon", CFG))
        self.assertIsNone(risk.gate_reason(90.0, "Mon", CFG))
        self.assertIsNone(risk.gate_reason(75.0, "Tue", CFG))
        self.assertIsNotNone(risk.gate_reason(69.9, "Tue", CFG))
        self.assertIsNotNone(risk.gate_reason(None, "Tue", CFG))

    def test_threshold_comes_from_config(self):
        c = copy.deepcopy(CFG)
        c["rules"]["min_score_to_trade"] = 95
        self.assertIsNotNone(risk.gate_reason(90.0, "Tue", c))
        c["rules"]["hot_score"] = 80
        self.assertIsNone(risk.gate_reason(85.0, "Mon", {**c, "rules": {**c["rules"], "min_score_to_trade": 70}}))

    def test_config_validation(self):
        c = copy.deepcopy(CFG)
        del c["rules"]["max_open_positions"]
        with self.assertRaises(ValueError):
            validate(c)
        c = copy.deepcopy(CFG)
        c["feed"] = "sip"
        with self.assertRaises(ValueError):
            validate(c)


class TestExits(unittest.TestCase):
    def setUp(self):
        self.start = dt.date(2026, 1, 5)

    def test_stop_hit(self):
        b = hbars(4, self.start)
        b[2].update(l=94.0)
        w, rows, d = exit_case(b)
        r = rows[-1]
        self.assertEqual((r["event"], r["reason"]), ("CLOSE", "stop"))
        self.assertAlmostEqual(float(r["price_raw"]), 95.0)
        self.assertLess(float(r["pnl_net"]), 0)
        self.assertNotIn("AAA", w.st["positions"])

    def test_target_hit(self):
        b = hbars(4, self.start)
        b[1].update(h=106.0)
        w, rows, d = exit_case(b)
        r = rows[-1]
        self.assertEqual(r["reason"], "target")
        self.assertAlmostEqual(float(r["price_raw"]), 105.0)
        self.assertGreater(float(r["pnl_gross"]), 0)
        self.assertLess(float(r["pnl_net"]), float(r["pnl_gross"]), "haircut must reduce the result")

    def test_stop_wins_when_both_in_one_bar(self):
        b = hbars(3, self.start)
        b[1].update(l=94.0, h=106.0)
        w, rows, d = exit_case(b)
        self.assertEqual(rows[-1]["reason"], "stop")

    def test_gap_down_fills_at_open_not_stop(self):
        b = hbars(3, self.start)
        b[1].update(o=90.0, l=89.0, h=91.0, c=90.0)
        w, rows, d = exit_case(b)
        self.assertEqual(rows[-1]["reason"], "stop")
        self.assertAlmostEqual(float(rows[-1]["price_raw"]), 90.0)

    def test_time_stop_after_5_sessions(self):
        b = hbars(7 * 8, self.start)    # 8 sessions, quiet, never reaches stop or target
        w, rows, d = exit_case(b)
        r = rows[-1]
        self.assertEqual(r["reason"], "time_stop")
        sessions = sorted({x["t"].astimezone(ET).date() for x in b})
        want = dt.datetime(sessions[5].year, sessions[5].month, sessions[5].day, 10, tzinfo=ET).astimezone(UTC)
        self.assertEqual(r["bar_t"], iso(want), "exit at the 10:00 bar open of the 6th session date = 5 sessions after entry")

    def test_no_exit_before_time_stop(self):
        b = hbars(7 * 5, self.start)    # entry session plus 4 more
        w, rows, d = exit_case(b)
        self.assertEqual(rows, [])
        self.assertIn("AAA", w.st["positions"])


class TestUnknownIsFail(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 2, 20, 21, tzinfo=UTC)
        self.bars = [dict(b) for b in make_series(3, 100.0, 20, dt.date(2026, 1, 20))]
        self.now = self.bars[-1]["t"] + HOUR

    def test_good_data_passes_filters(self):
        self.assertIsNone(scoring.hard_filters(self.bars, CFG, self.now))

    def test_missing_or_short_data_fails(self):
        self.assertIn("FAIL", scoring.hard_filters([], CFG, self.now))
        self.assertIn("FAIL", scoring.hard_filters(self.bars[:10], CFG, self.now))

    def test_none_and_nan_fields_fail(self):
        b = copy.deepcopy(self.bars)
        b[-3]["v"] = None
        self.assertIn("UNKNOWN", scoring.hard_filters(b, CFG, self.now))
        b = copy.deepcopy(self.bars)
        b[-1]["c"] = float("nan")
        self.assertIn("UNKNOWN", scoring.hard_filters(b, CFG, self.now))
        b = copy.deepcopy(self.bars)
        b[5]["h"], b[5]["l"] = 1.0, 2.0
        self.assertIn("UNKNOWN", scoring.hard_filters(b, CFG, self.now))

    def test_stale_data_fails(self):
        self.assertIn("stale", scoring.hard_filters(self.bars, CFG, self.now + dt.timedelta(days=9)))

    def test_unknown_mood_fails_evaluation(self):
        cand, note = scoring.evaluate(self.bars, None, CFG)
        self.assertIsNone(cand)
        self.assertIn("UNKNOWN", note)

    def test_gauge_missing_means_no_trades_anywhere(self):
        d = tmpdir()
        cfg = copy.deepcopy(CFG)
        cfg["symbols"], cfg["market_gauge"] = ["DEMX", "ALFA"], "DEMX"
        w = Watcher(cfg, d, "test")
        start = dt.date(2026, 1, 5)
        allb = {"ALFA": make_series(8, 90.0, 45, start)}
        now = allb["ALFA"][250]["t"] + HOUR
        view = view_at(allb, now)
        view["DEMX"] = []
        w.scan(now, view, ["r"], clock_open=True)
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertEqual(len(lines), 2)
        self.assertTrue(all(x["action"] == "SKIP" and "FAIL" in x["reason"] for x in lines))

    def test_failed_data_call_logs_every_symbol_as_fail(self):
        d = tmpdir()
        w = Watcher(CFG, d, "test")
        w.scan(dt.datetime(2026, 1, 6, 15, tzinfo=UTC), None, ["r"], "http 500", clock_open=True)
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertEqual(len(lines), len(CFG["symbols"]))
        self.assertTrue(all("FAIL: UNKNOWN" in x["reason"] for x in lines))


class TestMaxPositions(unittest.TestCase):
    def test_four_positions_block_a_fifth(self):
        d = tmpdir()
        cfg = copy.deepcopy(CFG)
        cfg["symbols"], cfg["market_gauge"] = ["DEMX", "ALFA", "BRVO"], "DEMX"
        w = Watcher(cfg, d, "test")
        start = dt.date(2026, 1, 5)
        allb = {"DEMX": make_series(7, 400.0, 45, start, 0.0002), "ALFA": make_series(8, 90.0, 45, start), "BRVO": make_series(9, 130.0, 45, start)}
        now = allb["DEMX"][200]["t"] + HOUR
        for i in range(4):
            w.st["positions"]["P%d" % i] = make_pos(now - HOUR, entry=100.0)
        w.scan(now, view_at(allb, now), ["r"], clock_open=True)
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertFalse(any(x["action"] == "TRADE" for x in lines))
        self.assertTrue(all("max open positions" in x["reason"] for x in lines if x["symbol"] in ("ALFA", "BRVO")))


class TestDemoEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = tmpdir()
        real = socket.socket

        def no_net(*a, **k):
            raise AssertionError("network used in demo")
        with mock.patch.object(socket, "socket", no_net):
            cls.w, cls.totals = run_demo(CFG, cls.dir)
        cls.sc = scorecard.build_scorecard(cls.dir, CFG, note="test")
        cls.dec = scorecard.read_decisions(os.path.join(cls.dir, "decisions.jsonl"))
        cls.trades = scorecard.read_trades(os.path.join(cls.dir, "paper-trades.csv"))

    def test_demo_made_trades_offline(self):
        self.assertGreater(self.totals["trades_opened"], 5)
        self.assertGreater(self.totals["trades_closed"], 3)

    def test_every_skip_has_a_reason(self):
        ev = [d for d in self.dec if d["action"] in ("TRADE", "SKIP", "WATCH")]
        self.assertTrue(all(d.get("reason") for d in ev))
        self.assertTrue(all(d["request_ids"] for d in ev))

    def test_monday_trades_only_at_90(self):
        monday_watch = 0
        for d in self.dec:
            if d["action"] == "TRADE":
                day = dt.datetime.fromisoformat(d["scan_id"].replace("Z", "+00:00")).astimezone(ET)
                if day.strftime("%a") == "Mon":
                    self.assertGreaterEqual(d["score"], 90)
            if d["action"] == "WATCH" and "watch day" in d["reason"]:
                monday_watch += 1
        self.assertGreater(monday_watch, 0, "demo must exercise the Monday rule")

    def test_no_trade_under_70(self):
        self.assertTrue(all(d["score"] >= 70 for d in self.dec if d["action"] == "TRADE"))

    def test_cap_25_percent_at_every_fill(self):
        fills = [d for d in self.dec if d["action"] == "FILL"]
        self.assertTrue(fills)
        for f in fills:
            self.assertLessEqual(f["notional"], 0.25 * f["equity"] + 0.01, f)

    def test_never_more_than_4_open_at_once(self):
        ev = []
        for r in self.trades:
            if r["ledger"] != "main":
                continue
            ev.append((r["ts_utc"], 1 if r["event"] == "OPEN" else -1, r["event"]))
        cur = peak = 0
        for ts, delta, kind in sorted(ev, key=lambda x: (x[0], x[1])):
            cur += delta
            peak = max(peak, cur)
        self.assertLessEqual(peak, 4)

    def test_open_rows_cite_decision_lines(self):
        ids = {d["decision_id"] for d in self.dec}
        for r in self.trades:
            self.assertIn(r["decision_id"], ids)

    def test_scorecard_numbers_trace_to_rows(self):
        text = self.sc["text"]
        rows = re.findall(r"^\| (T\d+) \| \w+ \| (D\d+) \((\d+)\) \| (D\d+) \((\d+)\) \| (\w+) \| ([-\d.]+) \| ([-\d.]+) \| ([-\d.]+) \|", text, re.M)
        self.assertEqual(len(rows), self.sc["closed"])
        self.assertAlmostEqual(sum(float(r[7]) for r in rows), self.sc["net"], places=1)
        self.assertAlmostEqual(sum(float(r[6]) for r in rows), self.sc["gross"], places=1)
        lines = read(os.path.join(self.dir, "decisions.jsonl")).splitlines()
        for r in rows:
            self.assertEqual(json.loads(lines[int(r[2]) - 1])["decision_id"], r[1])
            self.assertEqual(json.loads(lines[int(r[4]) - 1])["decision_id"], r[3])
        self.assertIn("placeholders", text)

    def test_daily_note_written(self):
        day = sorted({d["ts_utc"][:10] for d in self.dec})[3]
        scorecard.write_daily_note(self.dir, day, os.path.join(self.dir, "state.json"))
        self.assertIn("Scans:", read(os.path.join(self.dir, "daily-notes.md")))

    def test_config_change_changes_behavior(self):
        c = copy.deepcopy(CFG)
        c["rules"]["min_score_to_trade"] = 101
        d = tmpdir()
        _, t = run_demo(c, d)
        self.assertEqual(t["trades_opened"], 0)


class TestSecurity(unittest.TestCase):
    def sources(self):
        files = glob.glob(os.path.join(ROOT, "wkt", "*.py")) + [os.path.join(ROOT, "run.py"), os.path.join(ROOT, "config.yaml"),
                                                                 os.path.join(ROOT, "run_watcher.ps1")]
        return {f: read(f) for f in files if os.path.exists(f)}

    def test_no_order_endpoint_or_write_verb_in_source(self):
        bad = [r"/v2/orders", r"/orders", r"submit_order", r"cancel_order", r"\bPOST\b", r"\bDELETE\b", r"\bPATCH\b",
               r"\bPUT\b", r"method\s*=\s*['\"](?!GET)", r"\.post\(", r"\.delete\(", r"\.put\(", r"data\s*=\s*b?['\"]",
               r"/v2/positions/", r"close_all", r"/v2/watchlists", r"api\.alpaca\.markets(?<!paper-api\.alpaca\.markets)(?<!data\.alpaca\.markets)"]
        for path, text in self.sources().items():
            for pat in bad:
                for m in re.finditer(pat, text):
                    line = text[:m.start()].count("\n") + 1
                    ctx = text.splitlines()[line - 1]
                    # the guard module and the client legitimately name the paper and data hosts
                    if pat.startswith("api.alpaca") and ("paper-api.alpaca" in ctx or "data.alpaca" in ctx):
                        continue
                    self.fail("forbidden pattern %r in %s line %d: %s" % (pat, path, line, ctx.strip()))

    def test_only_paper_and_data_hosts_in_source(self):
        for path, text in self.sources().items():
            for host in re.findall(r"https?://([a-z0-9.\-]+)", text):
                self.assertIn(host, ("paper-api.alpaca.markets", "data.alpaca.markets"), path)

    def test_no_secret_looking_strings_in_source(self):
        for path, text in self.sources().items():
            self.assertIsNone(re.search(r"\bPK[A-Z0-9]{16,}\b", text), path)
            self.assertIsNone(re.search(r"\b[A-Za-z0-9/+]{36,}\b", text.replace("\\", "")) if path.endswith(".yaml") else None, path)
            self.assertNotIn(FAKE_KEY, text)

    def test_non_paper_url_refused(self):
        for u in ("https://api.alpaca.markets", "https://paper-api.alpaca.markets/", "http://paper-api.alpaca.markets",
                  "https://paper-api.alpaca.markets/v2", "", None, "https://data.alpaca.markets", "https://paper-api.alpaca.markets.evil.com"):
            with self.assertRaises(guards.GuardError, msg=str(u)):
                guards.assert_paper_url(u)
            with self.assertRaises(guards.GuardError, msg=str(u)):
                alpaca.AlpacaReadOnly("k", "s", u)
        self.assertEqual(guards.assert_paper_url("https://paper-api.alpaca.markets"), "https://paper-api.alpaca.markets")

    def test_start_refused_with_live_url_in_env(self):
        env = {"APCA_API_KEY_ID": FAKE_KEY, "APCA_API_SECRET_KEY": FAKE_SECRET, "APCA_API_BASE_URL": "https://api.alpaca.markets"}
        with mock.patch.dict(os.environ, env):
            with self.assertRaises(guards.GuardError):
                guards.load_env()
            with self.assertRaises(guards.GuardError):
                runmod.main(["--smoke"])

    def test_missing_env_error_names_variables_only(self):
        env = {"APCA_API_KEY_ID": FAKE_KEY}
        with mock.patch.dict(os.environ, env, clear=True):
            with self.assertRaises(guards.GuardError) as cm:
                guards.load_env()
        msg = str(cm.exception)
        self.assertIn("APCA_API_SECRET_KEY", msg)
        self.assertNotIn(FAKE_KEY, msg)

    def test_client_blocks_non_whitelisted_calls(self):
        c = alpaca.AlpacaReadOnly(FAKE_KEY, FAKE_SECRET, guards.PAPER_URL, transport=lambda u, h: (200, {}, b"{}"))
        for u in ("https://paper-api.alpaca.markets/v2/orders", "https://paper-api.alpaca.markets/v2/account/activities",
                  "https://api.alpaca.markets/v2/account", "http://paper-api.alpaca.markets/v2/account",
                  "https://data.alpaca.markets/v2/stocks/bars?feed=sip&symbols=SPY", "https://data.alpaca.markets/v2/stocks/bars?symbols=SPY",
                  "https://evil.example.com/v2/account"):
            with self.assertRaises(alpaca.ClientError, msg=u):
                c.get(u)
        self.assertTrue(c.get("https://paper-api.alpaca.markets/v2/clock").ok)

    def test_counted_mode_is_gated(self):
        d = tmpdir()
        with self.assertRaises(guards.GuardError):
            guards.counted_gate(d, False)
        with self.assertRaises(guards.GuardError):
            guards.counted_gate(d, True)
        with open(os.path.join(d, "GO-COUNTED.flag"), "w") as fh:
            fh.write("x")
        self.assertTrue(guards.counted_gate(d, True))


class FakeAlpaca:
    """Canned transport. Records the headers it saw so the test can prove they never reach a file."""

    def __init__(self, is_open=True, fail_bars=False, leak_in_exception=False, clock_seq=None):
        self.clock_seq = list(clock_seq) if clock_seq else None
        start = dt.date(2026, 1, 5)
        self.allb = {s: make_series(20 + i, 100.0 + 10 * i, 45, start, 0.0002 if i == 0 else 0.0) for i, s in enumerate(CFG["symbols"])}
        self.now = self.allb["SPY"][250]["t"] + HOUR
        self.is_open, self.fail_bars, self.leak = is_open, fail_bars, leak_in_exception
        self.calls = []

    def __call__(self, url, headers):
        self.calls.append(url)
        if self.leak and "/v2/stocks/bars" in url:
            raise RuntimeError("boom with " + headers["APCA-API-SECRET-KEY"] + headers["APCA-API-KEY-ID"])
        if url.endswith("/v2/clock"):
            if self.clock_seq:
                step = self.clock_seq.pop(0)
                if step == "fail":
                    return 500, {"X-Request-ID": "req-clock-500"}, b'{"message":"blip"}'
                return 200, {"X-Request-ID": "req-clock-1"}, json.dumps({"is_open": bool(step)}).encode()
            return 200, {"X-Request-ID": "req-clock-1"}, json.dumps({"is_open": self.is_open}).encode()
        if "/v2/stocks/bars" in url:
            if self.fail_bars:
                return 500, {"X-Request-ID": "req-bars-500"}, b'{"message":"nope"}'
            view = view_at(self.allb, self.now)
            if "timeframe=1Day" in url:
                view = {s: demomod.aggregate_daily(bs) for s, bs in view.items()}
            body = {"bars": {s: [{"t": iso(b["t"]), "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"]} for b in bs] for s, bs in view.items()},
                    "next_page_token": None}
            return 200, {"x-request-id": "req-bars-1"}, json.dumps(body).encode()
        return 200, {"X-Request-ID": "req-other"}, b"{}"


class TestLiveScanWithFakeTransport(unittest.TestCase):
    def run_scan(self, fake, clock_required=True):
        d = tmpdir()
        cl = alpaca.AlpacaReadOnly(FAKE_KEY, FAKE_SECRET, guards.PAPER_URL, transport=fake)
        w = Watcher(CFG, d, "test")
        buf, err = io.StringIO(), io.StringIO()
        with redirect_stdout(buf), redirect_stderr(err), mock.patch.object(runmod, "utcnow", lambda: fake.now):
            summ, cd = runmod.live_scan(w, cl, CFG, clock_required)
        return d, w, summ, buf.getvalue() + err.getvalue()

    def all_text(self, d, extra=""):
        out = extra
        for f in glob.glob(os.path.join(d, "*")):
            out += read(f)
        return out

    def test_request_ids_saved_and_no_secret_in_any_output(self):
        fake = FakeAlpaca()
        d, w, summ, printed = self.run_scan(fake)
        lines = scorecard.read_decisions(w.out.decisions)
        ev = [x for x in lines if x["symbol"] != "*"]
        self.assertEqual(len(ev), len(CFG["symbols"]))
        self.assertTrue(all("req-bars-1" in x["request_ids"] and "req-clock-1" in x["request_ids"] for x in ev))
        blob = self.all_text(d, printed)
        self.assertNotIn(FAKE_KEY, blob)
        self.assertNotIn(FAKE_SECRET, blob)
        self.assertTrue(all("feed=iex" in u for u in fake.calls if "stocks" in u))
        self.assertFalse(any("orders" in u for u in fake.calls))

    def test_exception_text_never_logged(self):
        fake = FakeAlpaca(leak_in_exception=True)
        d, w, summ, printed = self.run_scan(fake)
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertTrue(any("network error: RuntimeError" in x["reason"] for x in lines), "failure reason is logged, type only")
        blob = self.all_text(d, printed)
        self.assertNotIn(FAKE_SECRET, blob)
        self.assertNotIn(FAKE_KEY, blob)

    def test_bars_failure_keeps_request_id_and_fails_closed(self):
        fake = FakeAlpaca(fail_bars=True)
        d, w, summ, printed = self.run_scan(fake)
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertEqual(len(lines), len(CFG["symbols"]))
        self.assertTrue(all("req-bars-500" in x["request_ids"] and "FAIL: UNKNOWN" in x["reason"] for x in lines))
        self.assertFalse(any(x["action"] == "TRADE" for x in lines))

    def test_market_closed_means_no_scan(self):
        fake = FakeAlpaca(is_open=False)
        d, w, summ, printed = self.run_scan(fake)
        self.assertIsNone(summ)
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0]["symbol"], "*")
        self.assertFalse(any("stocks" in u for u in fake.calls), "no data call while the market is closed")

    def test_smoke_style_scan_ignores_closed_clock_but_flags_it(self):
        fake = FakeAlpaca(is_open=False)
        d, w, summ, printed = self.run_scan(fake, clock_required=False)
        self.assertIsNotNone(summ)
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertTrue(all(x["clock_open"] is False for x in lines))


class TestTesterFindings(unittest.TestCase):
    def setup_world(self):
        d = tmpdir()
        cfg = copy.deepcopy(CFG)
        cfg["symbols"], cfg["market_gauge"] = ["DEMX", "ALFA", "AAA"], "DEMX"
        w = Watcher(cfg, d, "test")
        start = dt.date(2026, 1, 5)
        allb = {"DEMX": make_series(7, 400.0, 45, start, 0.0002), "ALFA": make_series(8, 90.0, 45, start),
                "AAA": hbars(len(make_series(7, 1, 45, start)), start, 70.0)}
        now = allb["DEMX"][200]["t"] + HOUR
        return w, allb, now

    def test_overnight_gap_counts_toward_kill_switch(self):
        w, allb, now = self.setup_world()
        w.st["positions"]["AAA"] = make_pos(now - HOUR * 30, stop=10.0, target=500.0, entry=100.0, shares=1000)
        w.st["cash"] = 0.0
        w.st["last_equity"] = 100000.0
        w.st["day"] = {"date": "2000-01-01", "start_equity": 1.0, "killed": False}   # a previous day
        w.scan(now, view_at(allb, now), ["r"], clock_open=True)   # AAA now marks near 70, a 30 percent gap loss
        self.assertEqual(w.st["day"]["start_equity"], 100000.0)
        self.assertTrue(w.st["day"]["killed"])

    def test_pending_signal_is_cancelled_while_killed(self):
        w, allb, now = self.setup_world()
        sig_t = allb["ALFA"][199]["t"]
        w.st["pending"]["ALFA"] = {"decision_id": "D000001", "signal_bar_t": iso(sig_t), "entry_ref": 90.0, "atr": 1.0, "score": 85.0, "setup": "t"}
        w.st["positions"]["AAA"] = make_pos(now - HOUR * 3, stop=10.0, target=500.0, entry=100.0, shares=1000)
        w.st["cash"] = 0.0
        w.st["day"] = {"date": now.astimezone(ET).date().isoformat(), "start_equity": 100000.0, "killed": False}
        w.scan(now, view_at(allb, now), ["r"], clock_open=True)
        self.assertNotIn("ALFA", w.st["positions"])
        self.assertNotIn("ALFA", w.st["pending"])
        self.assertTrue(any(x["action"] == "CANCEL" for x in scorecard.read_decisions(w.out.decisions)))

    def test_redirects_not_followed_and_bad_bars_shape(self):
        self.assertIsNone(alpaca._NoRedirect().redirect_request(None, None, 302, "x", {}, "https://evil.example.com"))
        c = alpaca.AlpacaReadOnly("k", "s", guards.PAPER_URL, transport=lambda u, h: (200, {}, b'{"bars": [1]}'))
        out, rids, err = c.bars(["SPY"], "2026-01-01T00:00:00Z")
        self.assertIsNone(out)
        self.assertEqual(err, "bad bars shape")

    def test_directory_does_not_open_the_gate(self):
        d = tmpdir()
        os.makedirs(os.path.join(d, "GO-COUNTED.flag"))
        with self.assertRaises(guards.GuardError):
            guards.counted_gate(d, True)

    def test_config_range_checks(self):
        for path, val in ((("rules", "daily_kill_switch_pct"), -5), (("rules", "max_open_positions"), "4"), (("paper_book", "starting_equity"), 0)):
            c = copy.deepcopy(CFG)
            c[path[0]][path[1]] = val
            with self.assertRaises(ValueError, msg=str(path)):
                validate(c)


# ---------------------------------------------------------------- build order of 2026-11-26 (amendments, learning loop, F4)
def demo_world():
    c = copy.deepcopy(CFG)
    c["symbols"], c["market_gauge"] = list(DEMO_SYMBOLS), "DEMX"
    c["regime"]["min_breadth_symbols"] = 3
    start = dt.date(2026, 1, 5)
    allb = {"DEMX": make_series(7, 400.0, 45, start, 0.0002)}
    for i, s in enumerate(DEMO_SYMBOLS[1:], 1):
        allb[s] = make_series(7 + i, 50.0 + 40 * i, 45, start)
    full = {s: demomod.aggregate_daily(b) for s, b in allb.items()}
    hist = {s: demomod.make_daily_history(7 + i, allb[s][0]["o"], 230, start) for i, s in enumerate(DEMO_SYMBOLS)}
    times = [t for t in scan_times(allb["DEMX"]) if t > allb["DEMX"][70]["t"]]
    return c, allb, full, hist, times


def drive(w, world, lo, hi):
    c, allb, full, hist, times = world
    for now in times[lo:hi]:
        daily = demomod.daily_view(hist, full, now) if w.needs_daily(now, now.astimezone(ET).date()) else None
        w.scan(now, view_at(allb, now), ["demo-no-network"], clock_open=True, daily=daily)


def daily_series(closes, widths, end_date):
    days, d = [], end_date
    while len(days) < len(closes):
        d -= dt.timedelta(days=1)
        if d.weekday() < 5:
            days.append(d)
    days.reverse()
    out, prev = [], closes[0]
    for d, c, w in zip(days, closes, widths):
        out.append({"t": dt.datetime(d.year, d.month, d.day, tzinfo=ET).astimezone(UTC), "o": prev, "h": max(prev, c) * (1 + w),
                    "l": min(prev, c) * (1 - w), "c": c, "v": 1000000})
        prev = c
    return out


class TestConfigHashAndCounting(unittest.TestCase):
    def test_hash_is_stable_changes_with_a_value_and_is_on_every_line(self):
        h = config_hash(CFG)
        self.assertRegex(h, r"^[0-9a-f]{16}$")
        self.assertEqual(h, config_hash(copy.deepcopy(CFG)))
        c = copy.deepcopy(CFG)
        c["rules"]["reward_multiple"] = 2.6
        self.assertNotEqual(h, config_hash(c))
        w, totals = run_demo(CFG, tmpdir())
        dec = scorecard.read_decisions(w.out.decisions)
        self.assertTrue(all(d["config_hash"] == w.chash for d in dec))
        tr = scorecard.read_trades(w.out.trades)
        self.assertTrue(tr and all(r["config_hash"] == w.chash for r in tr))
        self.assertTrue(all(isinstance(json.loads(r["parts"]), dict) and r["regime"] for r in tr))

    def test_config_change_restarts_counts_and_is_listed(self):
        d = tmpdir()
        wA, _ = run_demo(CFG, d)
        cB = copy.deepcopy(wA.cfg)
        cB["paper_book"]["max_gap_atr"] = 1.5
        wB = Watcher(cB, d, "demo")
        self.assertNotEqual(wA.chash, wB.chash)
        wB.scan(dt.datetime(2026, 3, 2, 15, tzinfo=UTC), None, [], "x", clock_open=True)
        sc = scorecard.build_scorecard(d, cB, chash=wB.chash)
        self.assertEqual((sc["counted"], sc["opened"], sc["closed"]), (0, 0, 0))
        self.assertIn("Lines under any other hash (not counted)", sc["text"])
        hist = scorecard.read_history(d)
        self.assertEqual([h["previous"] for h in hist], [None, wA.chash])
        self.assertIn("CONFIG CHANGED", hist[1]["note"])
        scA = scorecard.build_scorecard(d, wA.cfg, chash=wA.chash)
        self.assertGreater(scA["closed"], 0)

    def test_decision_counts_once_per_setup_at_score_70_plus(self):
        d = tmpdir()
        cfg = copy.deepcopy(CFG)
        cfg["symbols"], cfg["market_gauge"] = ["DEMX", "ALFA"], "DEMX"
        w = Watcher(cfg, d, "test")
        start = dt.date(2026, 1, 5)
        allb = {"DEMX": make_series(7, 400.0, 45, start, 0.0002), "ALFA": make_series(8, 90.0, 45, start)}
        plan = [("pull", 75.0), ("pull", 78.0), ("pull", 72.0), (None, None), ("pull", 75.0), ("pull", 65.0), ("pull", 75.0)]
        seq = {"i": 0}

        def fake_eval(bars, mood, c):
            kind, score = plan[seq["i"]]
            if kind is None:
                return None, "no setup on the latest closed bar"
            return {"setup": kind, "score": score, "parts": {"base": score}, "entry": bars[-1]["c"], "atr": 1.0, "bar_t": bars[-1]["t"]}, "setup found"
        with mock.patch.object(scoring, "evaluate", fake_eval), mock.patch.object(risk, "gate_reason", lambda *a: "test: blocked so no position opens"):
            for k in range(len(plan)):
                seq["i"] = k
                now = allb["DEMX"][200 + k]["t"] + HOUR
                w.scan(now, view_at(allb, now), ["r"], clock_open=True)
        alfa = [x for x in scorecard.read_decisions(w.out.decisions) if x["symbol"] == "ALFA" and x["fresh"]]
        self.assertEqual([x["counted"] for x in alfa], [True, False, False, False, True, False, True])
        self.assertEqual([x["action"] for x in alfa][3], "SKIP")
        sc = scorecard.build_scorecard(d, cfg, chash=w.chash)
        self.assertEqual(sc["counted"], 6, "3 counted decisions for each of the two symbols")

    def test_demo_counted_only_70_plus_and_fewer_than_evaluations(self):
        w, _ = run_demo(CFG, tmpdir())
        dec = scorecard.read_decisions(w.out.decisions)
        counted = [d for d in dec if d.get("counted")]
        self.assertTrue(counted)
        self.assertTrue(all(d["score"] >= 70 and d["fresh"] for d in counted))
        ge70 = [d for d in dec if d["action"] in ("TRADE", "WATCH") and d.get("score", 0) >= 70]
        self.assertLessEqual(len(counted), len(ge70))
        skips = [d for d in dec if d["action"] == "SKIP"]
        self.assertTrue(skips and not any(d.get("counted") for d in skips), "skips are logged and never counted")


class TestZacLedger(unittest.TestCase):
    def world(self):
        d = tmpdir()
        w = Watcher(CFG, d, "test")
        bars = hbars(7 * 4, dt.date(2026, 1, 5), 100.0, 0.1)
        sig_bar = bars[2]
        sig = {"decision_id": "D000001", "signal_bar_t": iso(sig_bar["t"]), "entry_ref": sig_bar["c"], "atr": 0.2, "score": 85.0,
               "setup": "t", "parts": {"base": 55}, "regime": "UPTREND_CALM", "config_hash": w.chash}
        now = bars[-1]["t"] + HOUR
        common = w._common(now, [], True, {"tag": "UPTREND_CALM"})
        summ = {"trades_opened": 0, "zac_trades_opened": 0}
        return w, bars, sig, now, common, summ

    def test_main_fills_next_bar_zac_fills_next_session_open(self):
        w, bars, sig, now, common, summ = self.world()
        w.st["pending"]["AAA"] = dict(sig)
        w.st["zac"]["pending"]["AAA"] = dict(sig)
        w._try_fill(now, common, "zac", w.st["zac"], "AAA", bars, summ)
        w.out.save_state(w.st)
        zp = w.st["zac"]["positions"]["AAA"]
        self.assertEqual(zp["entry_raw"], bars[8]["o"], "10:00 bar open of the NEXT session (not the 09:00 bar)")
        self.assertEqual(zp["trade_id"][0], "Z")
        self.assertTrue(zp["entry_bar_t"] > sig["signal_bar_t"])
        self.assertEqual(bars[8]["t"].astimezone(ET).date(), bars[0]["t"].astimezone(ET).date() + dt.timedelta(days=1))
        self.assertEqual(bars[8]["t"].astimezone(ET).hour, 10)
        # the same signal on the main ledger fills at the very next hourly bar open
        self.assertGreater(abs(zp["entry_raw"] - sig["entry_ref"]), CFG["paper_book"]["max_gap_atr"] * sig["atr"], "zac gap is over the main ledger's 1 ATR cancel rule and still filled")
        w._try_fill(now, common, "main", w.st, "AAA", bars, summ)
        self.assertEqual(w.st["positions"]["AAA"]["entry_raw"], bars[3]["o"])
        self.assertEqual(w.st["positions"]["AAA"]["trade_id"][0], "T")
        w.st["positions"].clear()
        w.st["pending"]["AAA"] = dict(sig, entry_ref=bars[3]["o"] + 5.0)   # a main-ledger signal that gaps by 5 with atr 0.2: cancelled
        w._try_fill(now, common, "main", w.st, "AAA", bars, summ)
        self.assertNotIn("AAA", w.st["positions"])
        w.out.save_state(w.st)
        self.assertTrue(any(x["action"] == "CANCEL" and x["ledger"] == "main" for x in scorecard.read_decisions(w.out.decisions)))

    def test_demo_has_both_ledgers_with_distinct_ids_and_later_zac_entries(self):
        w, totals = run_demo(CFG, tmpdir())
        self.assertGreater(totals["zac_trades_opened"], 3)
        tr = scorecard.read_trades(w.out.trades)
        self.assertTrue(all(r["trade_id"].startswith("T") for r in tr if r["ledger"] == "main"))
        self.assertTrue(all(r["trade_id"].startswith("Z") for r in tr if r["ledger"] == "zac"))
        decs = {d["decision_id"]: d for d in scorecard.read_decisions(w.out.decisions)}
        n = 0
        for r in tr:
            if r["ledger"] == "zac" and r["event"] == "OPEN":
                dec = decs[r["reason"].replace("signal ", "")]
                sd = dt.datetime.fromisoformat(dec["bar_t"].replace("Z", "+00:00")).astimezone(ET).date()
                ed = dt.datetime.fromisoformat(r["bar_t"].replace("Z", "+00:00")).astimezone(ET).date()
                self.assertGreater(ed, sd, "zac entry is on a later session than the signal bar")
                n += 1
        self.assertGreater(n, 3)


class TestScorecardViews(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = tmpdir()
        cls.w, cls.totals = run_demo(CFG, cls.dir)
        cls.sc = scorecard.build_scorecard(cls.dir, CFG, chash=cls.w.chash)
        cls.dec = scorecard.read_decisions(cls.w.out.decisions)
        cls.tr = scorecard.read_trades(cls.w.out.trades)

    def test_haircut_view_matches_recompute_and_falls_with_slippage(self):
        text = self.sc["text"]
        rows = re.findall(r"^\| (5|15|30) bps \| (-?[\d.]+) \| (-?[\d.]+) \| (-?[\d.]+) \| (yes|no) \|$", text, re.M)
        self.assertEqual(len(rows), 6, "3 haircut rows for each of the 2 ledgers")
        main_rows = [float(r[1]) for r in rows[:3]]
        self.assertGreater(main_rows[0], main_rows[1])
        self.assertGreater(main_rows[1], main_rows[2])
        opens = {r["trade_id"]: r for r in self.tr if r["event"] == "OPEN"}
        want = {b: 0.0 for b in (5, 15, 30)}
        for r in self.tr:
            if r["event"] == "CLOSE" and r["ledger"] == "main":
                for b in want:
                    want[b] += net_at(float(opens[r["trade_id"]]["price_raw"]), float(r["price_raw"]), int(r["shares"]), b, 0.0, 0.0)
        for b, got in zip((5, 15, 30), main_rows):
            self.assertAlmostEqual(want[b], got, delta=0.02)
        self.assertAlmostEqual(main_rows[0], self.sc["net"], delta=0.05)

    def test_sixty_dollar_view_present_and_small(self):
        text = self.sc["text"]
        self.assertIn("sized as if the account were $60", text)
        m = re.search(r"^\| 5 bps \| (-?[\d.]+) \| (-?[\d.]+) \|$", text, re.M)
        self.assertIsNotNone(m)
        self.assertLess(abs(float(m.group(1))), 100)

    def test_baseline_uses_spy_marks_from_the_lines(self):
        marks = [d["spy_mark"] for d in self.dec if isinstance(d.get("spy_mark"), (int, float))]
        want = (marks[-1] / marks[0] - 1) * 100
        self.assertAlmostEqual(self.sc["baseline_pct"], want, places=9)
        self.assertIn("Buy-and-hold baseline", self.sc["text"])
        self.assertIn("%.3f percent" % want, self.sc["text"])

    def test_regime_on_every_evaluation_line_and_split_table(self):
        ev = [d for d in self.dec if d["action"] in ("TRADE", "SKIP", "WATCH") and d["symbol"] != "*"]
        self.assertTrue(all(d["regime"] in regime_mod.TAGS for d in ev))
        self.assertGreater(len({d["regime"] for d in ev} - {"UNKNOWN"}), 0)
        self.assertIn("Results split by regime tag", self.sc["text"])
        self.assertTrue(any(d["action"] == "REGIME" and d["regime_detail"] for d in self.dec))

    def test_end_rule_closed_open_trades_at_the_last_mark(self):
        self.assertGreater(self.totals["closed_by_end_rule"], 0)
        self.assertTrue(self.w.st["ended"])
        self.assertEqual(self.w.st["positions"], {})
        self.assertEqual(self.w.st["zac"]["positions"], {})
        for r in self.tr:
            if r["event"] == "CLOSE" and r["reason"] == "end_rule":
                self.assertAlmostEqual(float(r["price_raw"]), self.w.st["marks"][r["symbol"]], places=6)

    def test_go_live_lines_are_numbers_not_a_verdict(self):
        self.assertIn("It never says go live", self.sc["text"])
        self.assertIn("Zac-ledger net P and L at 30 bps", self.sc["text"])


class TestEndRule(unittest.TestCase):
    def test_close_out_closes_at_mark_cancels_pending_and_marks_ended(self):
        d = tmpdir()
        w = Watcher(CFG, d, "test")
        now = dt.datetime(2026, 12, 4, 20, 59, tzinfo=UTC)
        w.st["positions"]["AAA"] = make_pos(now - HOUR * 3, stop=90.0, target=130.0, entry=100.0, shares=10)
        w.st["positions"]["AAA"]["config_hash"] = w.chash
        w.st["cash"] = 0.0
        w.st["marks"]["AAA"] = 103.0
        w.st["pending"]["BBB"] = {"decision_id": "D000009", "signal_bar_t": iso(now), "entry_ref": 1, "atr": 1, "score": 80, "setup": "x"}
        n = w.close_out(now)
        self.assertEqual(n, 1)
        rows = scorecard.read_trades(w.out.trades)
        self.assertEqual((rows[-1]["reason"], float(rows[-1]["price_raw"])), ("end_rule", 103.0))
        self.assertEqual(w.st["pending"], {})
        self.assertTrue(w.st["ended"])
        self.assertTrue(any(x["action"] == "CANCEL" and "end rule" in x["reason"] for x in scorecard.read_decisions(w.out.decisions)))

    def test_position_without_a_mark_is_left_open_and_logged_unknown(self):
        d = tmpdir()
        w = Watcher(CFG, d, "test")
        now = dt.datetime(2026, 12, 4, 20, 59, tzinfo=UTC)
        w.st["positions"]["AAA"] = make_pos(now - HOUR, entry=100.0)
        self.assertEqual(w.close_out(now), 0)
        self.assertIn("AAA", w.st["positions"])
        self.assertTrue(any(x["action"] == "HOLD_UNKNOWN" for x in scorecard.read_decisions(w.out.decisions)))


class TestPdt(unittest.TestCase):
    def test_guard_rolling_and_monthly(self):
        today = dt.date(2026, 12, 3)   # Thursday
        self.assertIsNone(risk.pdt_block([], today, CFG))
        self.assertIsNone(risk.pdt_block(["2026-12-01", "2026-12-02"], today, CFG))
        r = risk.pdt_block(["2026-12-01", "2026-12-02", "2026-12-02"], today, CFG)
        self.assertIn("last 5 trading days", r)
        old = ["2026-12-01", "2026-12-01", "2026-12-01"]
        far = dt.date(2026, 12, 29)
        self.assertIn("calendar month", risk.pdt_block(old, far, CFG))
        c = copy.deepcopy(CFG)
        c["pdt"]["max_day_trades_per_month"] = 99
        self.assertIsNone(risk.pdt_block(old, far, c))
        c["pdt"]["enforce"] = False
        self.assertIsNone(risk.pdt_block(["2026-12-02"] * 5, today, c))

    def test_same_day_exit_counts_a_day_trade_and_guard_cancels_a_fill(self):
        b = hbars(4, dt.date(2026, 1, 5))
        b[2].update(l=94.0)
        w, rows, d = exit_case(b)
        self.assertEqual(rows[-1]["day_trade"], "True")
        self.assertEqual(len(w.st["day_trades"]), 1)
        d2 = tmpdir()
        w2 = Watcher(CFG, d2, "test")
        bars = hbars(7 * 4, dt.date(2026, 1, 5), 100.0, 0.1)
        today = bars[-1]["t"].astimezone(ET).date()
        w2.st["day_trades"] = [today.isoformat()] * 3
        w2.st["pending"]["AAA"] = {"decision_id": "D000001", "signal_bar_t": iso(bars[2]["t"]), "entry_ref": bars[2]["c"], "atr": 5.0, "score": 85.0, "setup": "t"}
        now = bars[-1]["t"] + HOUR
        w2._try_fill(now, w2._common(now, [], True, {"tag": "RANGE"}), "main", w2.st, "AAA", bars, {"trades_opened": 0})
        self.assertNotIn("AAA", w2.st["positions"])
        w2.out.save_state(w2.st)
        self.assertTrue(any("PDT guard" in x["reason"] for x in scorecard.read_decisions(w2.out.decisions)))


class TestPdtOpenEntriesCount(unittest.TestCase):
    """Change 4 (2026-11-27), S4 fix: an entry opened today could be exited today, so it counts as a potential day trade."""

    def test_unit_open_entry_today_counts_and_yesterday_does_not(self):
        today = dt.date(2026, 12, 3)
        self.assertIsNone(risk.pdt_block(["2026-12-02", "2026-12-02"], today, CFG, open_entry_dates=["2026-12-02"]))   # entered yesterday: not a day trade today
        self.assertIsNone(risk.pdt_block(["2026-12-02"], today, CFG, open_entry_dates=["2026-12-03"]))   # boundary: 1 closed + 1 open today = 2, under 3
        self.assertIn("PDT guard", risk.pdt_block(["2026-12-02"], today, CFG, open_entry_dates=["2026-12-03"] * 2))   # boundary: 1 + 2 = 3 = limit, refuse
        self.assertIn("PDT guard", risk.pdt_block([], today, CFG, open_entry_dates=["2026-12-03"] * 3))
        self.assertIsNone(risk.pdt_block(["2026-12-02", "2026-12-02"], today, CFG))   # no open entry today: allowed
        self.assertIn("calendar month", risk.pdt_block(["2026-12-01", "2026-12-01"], dt.date(2026, 12, 29), CFG, open_entry_dates=["2026-12-29"]))

    def _four_signals_same_day(self, fixed):
        c = copy.deepcopy(CFG)
        c["rules"]["max_open_positions"] = 6
        d = tmpdir()
        w = Watcher(c, d, "test")
        bars = hbars(7 * 3, dt.date(2026, 1, 5), 100.0, 0.0)
        now = bars[-1]["t"] + HOUR
        syms = ["AAA", "BBB", "CCC", "DDD"]
        common = w._common(now, [], True, {"tag": "UPTREND_CALM"})
        for i, s in enumerate(syms):
            w.st["pending"][s] = {"decision_id": "D%06d" % (i + 1), "signal_bar_t": iso(bars[6]["t"]), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
                                  "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}
        # force the fill bar and the scan to be the same ET day by giving the main ledger the day-2 bars and scanning at that day's close
        day2 = [b for b in bars if b["t"].astimezone(ET).date() == bars[7]["t"].astimezone(ET).date()]
        now = day2[-1]["t"] + HOUR
        for s in syms:
            w._try_fill(now, common, "main", w.st, s, bars[:7] + day2, {"trades_opened": 0})
        return w

    def test_four_same_day_entries_the_fourth_is_refused_and_ledger_cannot_exceed_limit(self):
        w = self._four_signals_same_day(True)
        self.assertEqual(sorted(w.st["positions"]), ["AAA", "BBB", "CCC"])
        w.out.save_state(w.st)
        refused = [x for x in scorecard.read_decisions(w.out.decisions) if x["action"] == "CANCEL" and "PDT guard" in x["reason"]]
        self.assertEqual([x["symbol"] for x in refused], ["DDD"])
        # all three exit the same day: 3 day trades, never above the limit of 3
        for s in list(w.st["positions"]):
            w.st["positions"][s]["stop"] = 1000.0
            w._check_exit(dt.datetime(2026, 1, 6, 21, tzinfo=dt.timezone.utc), {"scan_id": "x", "request_ids": []}, "main", w.st, s,
                          [b for b in hbars(14, dt.date(2026, 1, 5))], {"trades_closed": 0, "zac_trades_closed": 0})
        self.assertLessEqual(len(w.st["day_trades"]), CFG["pdt"]["max_day_trades_rolling"])

    def test_demo_zac_ledger_never_exceeds_the_limit(self):
        c, allb, full, hist, times = demo_world()
        w = Watcher(c, tmpdir(), "test")
        drive(w, (c, allb, full, hist, times), 0, len(times))
        from collections import Counter
        for name, bk in w.books():
            ds = sorted(dt.date.fromisoformat(x) for x in bk["day_trades"])
            for d0 in ds:
                inwin = [x for x in ds if x <= d0 and bdays_between(x, d0) < c["pdt"]["window_trading_days"]]
                self.assertLessEqual(len(inwin), c["pdt"]["max_day_trades_rolling"], name)
            months = Counter((x.year, x.month) for x in ds)
            self.assertLessEqual(max(months.values() or [0]), c["pdt"]["max_day_trades_per_month"], name)


class TestRegime(unittest.TestCase):
    def cfg(self, n_symbols=12):
        c = copy.deepcopy(CFG)
        c["symbols"] = ["SPY"] + ["S%d" % i for i in range(n_symbols - 1)]
        c["market_gauge"] = "SPY"
        return c

    def run_tag(self, closes, widths, n_symbols=12, extra_today=False):
        c = self.cfg(n_symbols)
        today = dt.date(2026, 12, 1)
        bars = daily_series(closes, widths, today)
        daily = {s: bars for s in c["symbols"]}
        if extra_today:   # a crazy forming bar for today must be ignored
            crazy = dict(bars[-1], t=dt.datetime(2026, 12, 1, tzinfo=ET).astimezone(UTC), c=1.0, o=1.0, h=1.0, l=1.0)
            daily = {s: bars + [crazy] for s in c["symbols"]}
        return regime_mod.compute(daily, c, today)

    def widths(self, n, tail):
        return [0.004] * (n - 20) + tail

    def test_all_five_tags(self):
        n = 260
        up = [100 * 1.001 ** i for i in range(n)]
        dn = [100 * 0.999 ** i for i in range(n)]
        calm = self.widths(n, [0.004 - 0.00015 * i for i in range(20)])
        wild = self.widths(n, [0.004] * 5 + [0.03] * 15)
        self.assertEqual(self.run_tag(up, calm)["tag"], "UPTREND_CALM")
        self.assertEqual(self.run_tag(up, wild)["tag"], "UPTREND_VOLATILE")
        self.assertEqual(self.run_tag(dn, calm)["tag"], "DOWNTREND_CALM")
        self.assertEqual(self.run_tag(dn, wild)["tag"], "DOWNTREND_VOLATILE")
        mixed = [100 * 1.001 ** i for i in range(240)]
        mixed += [mixed[-1] * 0.997 ** (i + 1) for i in range(20)]
        self.assertEqual(self.run_tag(mixed, calm)["tag"], "RANGE")
        self.assertEqual(self.run_tag(up, calm, extra_today=True)["tag"], "UPTREND_CALM")

    def test_unknown_is_fail_cases(self):
        n = 260
        up = [100 * 1.001 ** i for i in range(n)]
        calm = self.widths(n, [0.002] * 20)
        r = self.run_tag(up[:100], calm[:100])
        self.assertEqual(r["tag"], "UNKNOWN")
        self.assertIn("daily bars", r["detail"]["why"])
        self.assertEqual(self.run_tag(up, calm, n_symbols=4)["tag"], "UNKNOWN", "too few symbols for breadth")
        self.assertEqual(regime_mod.compute(None, self.cfg(), dt.date(2026, 12, 1))["tag"], "UNKNOWN")
        bad = daily_series(up, calm, dt.date(2026, 12, 1))
        bad[-3]["c"] = float("nan")
        c = self.cfg()
        self.assertEqual(regime_mod.compute({s: bad for s in c["symbols"]}, c, dt.date(2026, 12, 1))["tag"], "UNKNOWN")


class TestStepUp(unittest.TestCase):
    def on(self):
        c = copy.deepcopy(CFG)
        c["sizing"]["step_up"]["enabled"] = True
        return c

    def test_default_is_off_and_demo_never_steps_up(self):
        self.assertIs(CFG["sizing"]["step_up"]["enabled"], False)
        pct, why = risk.step_up_check(CFG, 95, "UPTREND_CALM", 0, [10.0] * 30, None, dt.date(2026, 12, 3))
        self.assertIsNone(pct)
        self.assertIn("OFF", why[0])
        w, _ = run_demo(CFG, tmpdir())
        fills = [d for d in scorecard.read_decisions(w.out.decisions) if d["action"] == "FILL"]
        self.assertTrue(fills and all(f["size"]["risk_pct"] <= 2.0 and "OFF" in f["size"]["step_up"][0] for f in fills))

    def test_every_condition_must_hold(self):
        c, today = self.on(), dt.date(2026, 12, 3)
        good = dict(score=92, regime_tag="UPTREND_CALM", open_positions=1, nets=[5.0] * 25, last_kill=None)

        def call(**kw):
            a = dict(good, **kw)
            return risk.step_up_check(c, a["score"], a["regime_tag"], a["open_positions"], a["nets"], a["last_kill"], today)
        self.assertEqual(call()[0], 3.0)
        self.assertIsNone(call(score=85)[0])
        self.assertIsNone(call(regime_tag="UNKNOWN")[0])
        self.assertIsNone(call(regime_tag="UPTREND_VOLATILE")[0])
        self.assertIsNone(call(nets=[5.0] * 19)[0])
        self.assertIsNone(call(nets=[-1.0] * 25)[0])
        self.assertIsNone(call(open_positions=2)[0])
        self.assertIsNone(call(last_kill="2026-12-01")[0])
        self.assertEqual(call(last_kill="2026-11-20")[0], 3.0)

    def test_hard_cap_per_trade_and_stepped_size(self):
        base, _ = risk.size_shares(100000.0, 100000.0, 100.0, 5.0, 95, CFG)
        up, det = risk.size_shares(100000.0, 100000.0, 100.0, 5.0, 95, CFG, risk_pct=3.0)
        self.assertEqual((base, up), (200, 250))   # 2 percent = 200 shares; 3 percent = 300 but the 25 percent cap holds at 250
        s, det = risk.size_shares(100000.0, 100000.0, 100.0, 50.0, 95, CFG, risk_pct=9.0)
        self.assertEqual(det["risk_pct"], 3.0)
        self.assertEqual(s, 30)
        c = copy.deepcopy(CFG)
        c["sizing"]["step_up"]["risk_pct"] = 4.0
        with self.assertRaises(ValueError):
            validate(c)

    def test_weekly_loss_limit_blocks_new_trades(self):
        w = Watcher(CFG, tmpdir(), "test")
        start = dt.date(2026, 1, 5)
        allb = {s: make_series(7 + i, 100.0, 45, start) for i, s in enumerate(CFG["symbols"])}
        now = allb["SPY"][200]["t"] + HOUR
        view = view_at(allb, now)
        w.st["day"] = {"date": now.astimezone(ET).date().isoformat(), "start_equity": 100000.0, "killed": False}
        monday = now.astimezone(ET).date() - dt.timedelta(days=now.astimezone(ET).weekday())
        w.st["week"] = {"start": monday.isoformat(), "start_equity": 100000.0, "blocked": False}
        w.st["day"]["start_equity"] = 93500.0     # today looks fine, only the WEEK is down 6.5 percent
        w.st["cash"] = 93500.0
        w.scan(now, view, ["r"], clock_open=True)
        self.assertTrue(w.st["week"]["blocked"])
        self.assertFalse(w.st["day"]["killed"])
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertTrue(any(x["action"] == "WEEK_LIMIT" for x in lines))
        self.assertFalse(any(x["action"] == "TRADE" for x in lines))


class TestCrashSafety(unittest.TestCase):
    """Tester F4: a crash between the log writes and the state save used to duplicate ids on restart."""

    def reference(self, world, n):
        d = tmpdir()
        w = Watcher(world[0], d, "demo")
        drive(w, world, 0, n)
        return d

    def crash_and_resume(self, mode):
        world = demo_world()
        N, K = 70, 35
        d = tmpdir()
        w = Watcher(world[0], d, "demo")
        drive(w, world, 0, K)
        orig_flush, orig_write = logio.Out._flush, logio.Out._write_state
        calls = {"n": 0}

        def half_flush(self, decs, trs):
            orig_flush(self, decs[:max(1, len(decs) // 2)], [])
            raise RuntimeError("simulated crash mid log write")

        def dead_first_write(self, st):
            raise RuntimeError("simulated crash before anything was written")

        def dead_second_write(self, st):
            calls["n"] += 1
            if calls["n"] == 2:
                raise RuntimeError("simulated crash after the logs, before the journal was cleared")
            orig_write(self, st)
        patch = {"A": ("_flush", half_flush), "B": ("_write_state", dead_first_write), "C": ("_write_state", dead_second_write)}[mode]
        with mock.patch.object(logio.Out, patch[0], patch[1]):
            with self.assertRaises(RuntimeError):
                drive(w, world, K, K + 1)
        w2 = Watcher(world[0], d, "demo")
        resume_from = K if mode == "B" else K + 1       # B lost the whole scan, so it is run again
        drive(w2, world, resume_from, N)
        return d, w2

    def check(self, mode):
        world = demo_world()
        ref = self.reference(world, 70)
        d, w2 = self.crash_and_resume(mode)
        ids = [x["decision_id"] for x in scorecard.read_decisions(os.path.join(d, "decisions.jsonl"))]
        self.assertEqual(len(ids), len(set(ids)), "no duplicate decision ids")
        self.assertEqual(ids, ["D%06d" % (i + 1) for i in range(len(ids))], "no gaps either")
        keys = [(r["trade_id"], r["event"]) for r in scorecard.read_trades(os.path.join(d, "paper-trades.csv"))]
        self.assertEqual(len(keys), len(set(keys)), "no duplicate trade rows")
        self.assertEqual(read(os.path.join(d, "decisions.jsonl")), read(os.path.join(ref, "decisions.jsonl")), "same lines as a run that never crashed")
        self.assertEqual(read(os.path.join(d, "paper-trades.csv")), read(os.path.join(ref, "paper-trades.csv")))
        self.assertIsNone(w2.st["journal"])
        return w2

    def test_crash_half_way_through_the_log_append(self):
        w2 = self.check("A")
        self.assertGreater(w2.recovered, 0)

    def test_crash_before_state_is_written(self):
        self.check("B")

    def test_crash_after_logs_before_journal_cleared(self):
        self.check("C")

    def test_trade_rows_are_replayed_once(self):
        d = tmpdir()
        out = logio.Out(d, "t")
        st = {"next_decision": 0, "cash": 1, "positions": {}, "pending": {}}
        did = out.decision(st, {"symbol": "X", "action": "FILL"})
        out.trade({"trade_id": "T0001", "event": "OPEN", "decision_id": did})
        st["journal"] = {"decisions": out.buf_dec, "trades": out.buf_tr}
        out._write_state(st)                      # crash right here: nothing appended yet
        out2 = logio.Out(d, "t")
        st2 = out2.load_state({})
        self.assertEqual(out2.recover(st2), 2)
        out3 = logio.Out(d, "t")
        self.assertEqual(out3.recover(out3.load_state({})), 0, "a second recovery adds nothing")
        self.assertEqual(len(scorecard.read_trades(os.path.join(d, "paper-trades.csv"))), 1)
        self.assertEqual(len(scorecard.read_decisions(os.path.join(d, "decisions.jsonl"))), 1)

    def test_torn_last_line_does_not_hide_the_record(self):
        d = tmpdir()
        with open(os.path.join(d, "decisions.jsonl"), "w") as f:
            f.write('{"decision_id": "D000001", "symbol": "X"}\n{"decision_id": "D000002", "sym')
        out = logio.Out(d, "t")
        out._flush([{"decision_id": "D000002", "symbol": "X"}], [])
        bad = []
        rows = scorecard.read_decisions(os.path.join(d, "decisions.jsonl"), bad)
        self.assertEqual([r["decision_id"] for r in rows], ["D000001", "D000002"])
        self.assertEqual(len(bad), 1, "the torn fragment is skipped and reported, not fatal")

    def test_bad_state_files_give_a_readable_error_and_change_nothing(self):
        for payload in (b"", b"not json", b"\xff\xfe\x00bin", b"[]", b"{}", b"null", b'{"cash": 1, "positions": {'):
            d = tmpdir()
            p = os.path.join(d, "state.json")
            with open(p, "wb") as f:
                f.write(payload)
            with self.assertRaises(logio.StateError, msg=repr(payload)):
                Watcher(CFG, d, "test")
            with open(p, "rb") as f:
                self.assertEqual(f.read(), payload)


class TestLoopRegression(unittest.TestCase):
    """Tester F1 and qa N1: one unreadable /v2/clock call must not end the counted watch week."""

    def test_counted_loop_survives_one_clock_failure_then_stops_at_close(self):
        wk = tmpdir()
        with open(os.path.join(wk, "GO-COUNTED.flag"), "w") as fh:
            fh.write("test")
        fake = FakeAlpaca(clock_seq=[True, "fail", True, False])
        sleeps = []
        env = {"APCA_API_KEY_ID": FAKE_KEY, "APCA_API_SECRET_KEY": FAKE_SECRET, "APCA_API_BASE_URL": guards.PAPER_URL}
        buf = io.StringIO()
        with mock.patch.dict(os.environ, env), mock.patch.object(runmod, "WATCH_WEEK", wk), \
                mock.patch.object(runmod, "utcnow", lambda: fake.now), redirect_stdout(buf):
            rc = runmod.main(["--counted", "--loop"], client_factory=lambda k, s, b: alpaca.AlpacaReadOnly(k, s, b, transport=fake),
                             sleep=lambda n: sleeps.append(n))
        self.assertEqual(rc, 0)
        self.assertEqual(sleeps, [CFG["scan_interval_seconds"], 30, CFG["scan_interval_seconds"]], "scan, blip, scan, then the close")
        self.assertEqual(sum(1 for u in fake.calls if u.endswith("/v2/clock")), 4)
        self.assertEqual(sum(1 for u in fake.calls if "timeframe=1Day" in u), 1, "daily bars for the regime are fetched once a day")
        self.assertEqual(buf.getvalue().count("scan:"), 2)
        for name in ("daily-notes.md", "scorecard.md", "decisions.jsonl", "state.json", "config-history.jsonl"):
            self.assertTrue(os.path.exists(os.path.join(wk, name)), name)
        dec = scorecard.read_decisions(os.path.join(wk, "decisions.jsonl"))
        self.assertTrue(all(x["config_hash"] == config_hash(CFG) for x in dec))
        blob = "".join(read(os.path.join(wk, f)) for f in os.listdir(wk) if os.path.isfile(os.path.join(wk, f))) + buf.getvalue()
        self.assertNotIn(FAKE_SECRET, blob)
        self.assertNotIn(FAKE_KEY, blob)

    def test_end_rule_applies_on_the_last_day_and_blocks_a_rerun(self):
        wk = tmpdir()
        with open(os.path.join(wk, "GO-COUNTED.flag"), "w") as fh:
            fh.write("test")
        fake = FakeAlpaca(clock_seq=[True, False])
        cfgpath = os.path.join(tmpdir(), "config.yaml")
        txt = read(os.path.join(ROOT, "config.yaml")).replace('last_day: "2026-12-24"', 'last_day: "%s"' % fake.now.astimezone(ET).date().isoformat())
        with open(cfgpath, "w", encoding="utf-8") as fh:
            fh.write(txt)
        env = {"APCA_API_KEY_ID": FAKE_KEY, "APCA_API_SECRET_KEY": FAKE_SECRET, "APCA_API_BASE_URL": guards.PAPER_URL}
        buf = io.StringIO()
        fac = lambda k, s, b: alpaca.AlpacaReadOnly(k, s, b, transport=fake)
        with mock.patch.dict(os.environ, env), mock.patch.object(runmod, "WATCH_WEEK", wk), \
                mock.patch.object(runmod, "utcnow", lambda: fake.now), redirect_stdout(buf):
            runmod.main(["--counted", "--loop", "--config", cfgpath], client_factory=fac, sleep=lambda n: None)
            self.assertIn("end rule applied", buf.getvalue())
            st = json.loads(read(os.path.join(wk, "state.json")))
            self.assertTrue(st["ended"])
            calls_before = len(fake.calls)
            runmod.main(["--counted", "--loop", "--config", cfgpath], client_factory=fac, sleep=lambda n: None)
            self.assertEqual(len(fake.calls), calls_before, "after the end rule the program makes no further calls")

    def test_live_scan_reports_lookback_and_response_shapes(self):
        fake = FakeAlpaca()
        d = tmpdir()
        cl = alpaca.AlpacaReadOnly(FAKE_KEY, FAKE_SECRET, guards.PAPER_URL, transport=fake)
        w = Watcher(CFG, d, "test")
        with mock.patch.object(runmod, "utcnow", lambda: fake.now):
            runmod.live_scan(w, cl, CFG, False)
        self.assertEqual(w.info["min_bars_filter"], 60)
        self.assertEqual(len(w.info["hourly_closed_bars_min_median_max"]), 3)
        self.assertIn("1Hour", w.info["response_shapes"])
        self.assertIn("1Day", w.info["response_shapes"])
        self.assertEqual(w.info["response_shapes"]["1Hour"]["bar_keys"], ["c", "h", "l", "o", "t", "v"])
        self.assertNotIn(FAKE_SECRET, repr(cl) + json.dumps(w.info, default=str))



class FakeExtendedHours(FakeAlpaca):
    """Like the real IEX feed: hourly bars also start at 08:00 ET (pre-market) and 16:00 ET (after hours)."""

    def __call__(self, url, headers):
        st, h, body = super().__call__(url, headers)
        if "/v2/stocks/bars" in url and "timeframe=1Day" not in url and st == 200:
            data = json.loads(body)
            for s, rows in data["bars"].items():
                first = dt.datetime.fromisoformat(rows[0]["t"].replace("Z", "+00:00")).astimezone(ET)
                last = dt.datetime.fromisoformat(rows[-1]["t"].replace("Z", "+00:00")).astimezone(ET)
                pre = dt.datetime(first.year, first.month, first.day, 8, tzinfo=ET)
                post = dt.datetime(last.year, last.month, last.day, 16, tzinfo=ET)
                rows.insert(0, {"t": iso(pre), "o": 1e9, "h": 1e9, "l": 1e9, "c": 1e9, "v": 5})
                rows.append({"t": iso(post), "o": 1e9, "h": 1e9, "l": 1e9, "c": 1e9, "v": 5})
            body = json.dumps(data).encode()
        return st, h, body


class TestSessionBars(unittest.TestCase):
    def test_filter_keeps_only_regular_hour_bars(self):
        from wkt.engine import filter_session
        day = dt.date(2026, 1, 6)
        bars = [{"t": dt.datetime(day.year, day.month, day.day, h, tzinfo=ET).astimezone(UTC), "o": 1, "h": 1, "l": 1, "c": 1, "v": 1} for h in range(7, 18)]
        kept, dropped = filter_session(bars, CFG)
        self.assertEqual([b["t"].astimezone(ET).hour for b in kept], list(range(9, 16)))
        self.assertEqual(dropped, 4)
        c = copy.deepcopy(CFG)
        c["session_bars"]["regular_hours_only"] = False
        self.assertEqual(filter_session(bars, c), (bars, 0))

    def test_live_scan_drops_extended_hours_before_scoring(self):
        fake = FakeExtendedHours()
        d = tmpdir()
        cl = alpaca.AlpacaReadOnly(FAKE_KEY, FAKE_SECRET, guards.PAPER_URL, transport=fake)
        w = Watcher(CFG, d, "test")
        with mock.patch.object(runmod, "utcnow", lambda: fake.now):
            summ, cd = runmod.live_scan(w, cl, CFG, True)
        self.assertEqual(w.info["extended_hours_bars_dropped"], 2 * len(CFG["symbols"]))
        self.assertEqual(w.info["gauge_bar_start_times_et"], ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"])
        self.assertTrue(all(m < 1e6 for m in w.st["marks"].values()), "the 1e9 extended-hours prints never became a mark")
        lines = scorecard.read_decisions(w.out.decisions)
        self.assertFalse(any("UNKNOWN" in x["reason"] and "impossible" in x["reason"] for x in lines))

    def test_session_config_checked(self):
        c = copy.deepcopy(CFG)
        c["session_bars"]["first_bar_start_hour_et"] = 16
        with self.assertRaises(ValueError):
            validate(c)
        c = copy.deepcopy(CFG)
        c["zac_ledger"]["max_gap_atr"] = -1
        with self.assertRaises(ValueError):
            validate(c)
        c = copy.deepcopy(CFG)
        del c["session_bars"]
        with self.assertRaises(ValueError):
            validate(c)


class TestTesterPass2(unittest.TestCase):
    def test_last_day_and_nan_validation(self):
        for bad in ("12/04/2026", "2026-12-4", "Friday", "", dt.date(2026, 12, 4)):
            c = copy.deepcopy(CFG)
            c["end_rule"]["last_day"] = bad
            with self.assertRaises(ValueError, msg=str(bad)):
                validate(c)
        for path in (("paper_book", "starting_equity"), ("rules", "daily_kill_switch_pct"), ("sizing", "max_loss_per_week_pct"), ("paper_book", "haircut_bps_each_side")):
            c = copy.deepcopy(CFG)
            c[path[0]][path[1]] = float("nan")
            with self.assertRaises(ValueError, msg=str(path)):
                validate(c)
        c = copy.deepcopy(CFG)
        c["sizing"]["step_up"]["regime"] = "BOGUS"
        with self.assertRaises(ValueError):
            validate(c)

    def test_ended_flag_resets_on_new_hash(self):
        d = tmpdir()
        w = Watcher(CFG, d, "test")
        w.close_out(dt.datetime(2026, 12, 4, 21, tzinfo=UTC))
        self.assertTrue(Watcher(CFG, d, "test").st["ended"])
        c = copy.deepcopy(CFG)
        c["end_rule"]["last_day"] = "2026-12-11"
        self.assertFalse(Watcher(c, d, "test").st["ended"])

    def test_restart_after_close_on_last_day_applies_end_rule(self):
        wk = tmpdir()
        with open(os.path.join(wk, "GO-COUNTED.flag"), "w") as fh:
            fh.write("t")
        fake = FakeAlpaca(clock_seq=[False])
        cfgpath = os.path.join(tmpdir(), "config.yaml")
        txt = read(os.path.join(ROOT, "config.yaml")).replace('last_day: "2026-12-24"', 'last_day: "%s"' % fake.now.astimezone(ET).date().isoformat())
        with open(cfgpath, "w", encoding="utf-8") as fh:
            fh.write(txt)
        env = {"APCA_API_KEY_ID": FAKE_KEY, "APCA_API_SECRET_KEY": FAKE_SECRET, "APCA_API_BASE_URL": guards.PAPER_URL}
        buf = io.StringIO()
        with mock.patch.dict(os.environ, env), mock.patch.object(runmod, "WATCH_WEEK", wk), mock.patch.object(runmod, "utcnow", lambda: fake.now), redirect_stdout(buf):
            runmod.main(["--counted", "--loop", "--config", cfgpath], client_factory=lambda k, s, b: alpaca.AlpacaReadOnly(k, s, b, transport=fake), sleep=lambda n: None)
        self.assertIn("end rule applied", buf.getvalue())
        self.assertTrue(json.loads(read(os.path.join(wk, "state.json")))["ended"])


class TestFillAtTenOclock(unittest.TestCase):
    """Change 2 (2026-11-27, Jarvis decision 2026-11-26): Zac-ledger entry and time-stop exit fill at the 10:00 ET bar open.
    Scoring still sees the 09:00 bar."""

    def test_config_has_a_separate_fill_setting_and_scoring_hour_is_unchanged(self):
        self.assertEqual(CFG["fills"]["session_open_fill_hour_et"], 10)
        self.assertEqual(CFG["session_bars"]["first_bar_start_hour_et"], 9)
        kept, dropped = filter_session(hbars(14, dt.date(2026, 1, 5)), CFG)
        self.assertEqual(sorted({b["t"].astimezone(ET).hour for b in kept}), [9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(dropped, 0)

    def test_zac_entry_never_uses_the_nine_o_clock_bar(self):
        d = tmpdir()
        w = Watcher(CFG, d, "test")
        bars = hbars(7 * 3, dt.date(2026, 1, 5), 100.0, 0.0)
        for b in bars:
            h = b["t"].astimezone(ET).hour
            b["o"] = 111.0 if h == 9 else 100.0   # a pre-open print on the 09:00 bar
        sig = {"decision_id": "D000001", "signal_bar_t": iso(bars[6]["t"]), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
               "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}
        w.st["zac"]["pending"]["AAA"] = dict(sig)
        now = bars[-1]["t"] + HOUR
        common = w._common(now, [], True, {"tag": "UPTREND_CALM"})
        w._try_fill(now, common, "zac", w.st["zac"], "AAA", bars, {"trades_opened": 0, "zac_trades_opened": 0})
        zp = w.st["zac"]["positions"]["AAA"]
        self.assertEqual(zp["entry_raw"], 100.0)
        self.assertEqual(dt.datetime.fromisoformat(zp["entry_bar_t"].replace("Z", "+00:00")).astimezone(ET).hour, 10)

    def test_zac_entry_waits_while_only_the_nine_o_clock_bar_exists(self):
        d = tmpdir()
        w = Watcher(CFG, d, "test")
        bars = hbars(8, dt.date(2026, 1, 5), 100.0, 0.0)   # day 1 plus day 2 09:00 bar only
        self.assertEqual(bars[-1]["t"].astimezone(ET).hour, 9)
        sig = {"decision_id": "D000001", "signal_bar_t": iso(bars[6]["t"]), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
               "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}
        w.st["zac"]["pending"]["AAA"] = dict(sig)
        now = bars[-1]["t"] + dt.timedelta(minutes=40)   # 09:40 ET
        common = w._common(now, [], True, {"tag": "UPTREND_CALM"})
        w._try_fill(now, common, "zac", w.st["zac"], "AAA", bars, {"trades_opened": 0, "zac_trades_opened": 0})
        self.assertNotIn("AAA", w.st["zac"]["positions"])
        self.assertIn("AAA", w.st["zac"]["pending"], "still waiting for the 10:00 bar")

    def test_time_stop_uses_the_ten_o_clock_open_and_a_stop_on_the_nine_bar_still_fires(self):
        b = hbars(7 * 8, dt.date(2026, 1, 5))
        sessions = sorted({x["t"].astimezone(ET).date() for x in b})
        s6 = sessions[5]
        for x in b:
            if x["t"].astimezone(ET).date() == s6:
                x["o"] = 100.0 + 0.01 * x["t"].astimezone(ET).hour   # distinct open per hour
        w, rows, d = exit_case(b)
        r = rows[-1]
        self.assertEqual(r["reason"], "time_stop")
        self.assertAlmostEqual(float(r["price_raw"]), 100.10)
        b2 = hbars(7 * 8, dt.date(2026, 1, 5))
        for x in b2:
            if x["t"].astimezone(ET).date() == s6 and x["t"].astimezone(ET).hour == 9:
                x.update(l=90.0)
        w2, rows2, d2 = exit_case(b2)
        self.assertEqual(rows2[-1]["reason"], "stop")


class TestMainFillAtTenOclock(unittest.TestCase):
    """Change 5 (2026-11-27, trading-director decision): the MAIN ledger entry also fills at the first bar open at or after
    fills.session_open_fill_hour_et (10:00 ET), because the 09:00 bar holds pre-open prints. Scoring bars unchanged."""

    def _sig(self, w, bars, i):
        return {"decision_id": "D000001", "signal_bar_t": iso(bars[i]["t"]), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
                "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}

    def test_overnight_signal_fills_at_the_ten_open_not_the_nine_bar(self):
        w = Watcher(CFG, tmpdir(), "test")
        bars = hbars(7 * 3, dt.date(2026, 1, 5), 100.0, 0.0)
        for b in bars:
            b["o"] = 111.0 if b["t"].astimezone(ET).hour == 9 else 100.0   # fake pre-open print on every 09:00 bar
        w.st["pending"]["AAA"] = self._sig(w, bars, 6)   # last bar of day 1 (15:00)
        now = bars[10]["t"] + HOUR
        w._try_fill(now, w._common(now, [], True, {"tag": "UPTREND_CALM"}), "main", w.st, "AAA", bars[:11], {"trades_opened": 0})
        p = w.st["positions"]["AAA"]
        self.assertEqual(p["entry_raw"], 100.0)
        self.assertEqual(dt.datetime.fromisoformat(p["entry_bar_t"].replace("Z", "+00:00")).astimezone(ET).hour, 10)

    def test_main_entry_waits_while_only_the_nine_bar_exists(self):
        w = Watcher(CFG, tmpdir(), "test")
        bars = hbars(8, dt.date(2026, 1, 5), 100.0, 0.0)   # day 1 plus the day 2 09:00 bar only
        w.st["pending"]["AAA"] = self._sig(w, bars, 6)
        now = bars[-1]["t"] + dt.timedelta(minutes=40)
        w._try_fill(now, w._common(now, [], True, {"tag": "UPTREND_CALM"}), "main", w.st, "AAA", bars, {"trades_opened": 0})
        self.assertNotIn("AAA", w.st["positions"])
        self.assertIn("AAA", w.st["pending"])

    def test_same_day_signal_still_fills_at_the_next_bar_when_it_is_after_ten(self):
        w = Watcher(CFG, tmpdir(), "test")
        bars = hbars(7, dt.date(2026, 1, 5), 100.0, 0.0)
        w.st["pending"]["AAA"] = self._sig(w, bars, 2)   # 11:00 bar signal, next bar 12:00 is after the fill hour
        now = bars[3]["t"] + HOUR
        w._try_fill(now, w._common(now, [], True, {"tag": "UPTREND_CALM"}), "main", w.st, "AAA", bars[:4], {"trades_opened": 0})
        self.assertEqual(dt.datetime.fromisoformat(w.st["positions"]["AAA"]["entry_bar_t"].replace("Z", "+00:00")).astimezone(ET).hour, 12)

    def test_nine_bar_signal_fills_on_the_ten_bar_and_scoring_hour_unchanged(self):
        w = Watcher(CFG, tmpdir(), "test")
        bars = hbars(7, dt.date(2026, 1, 5), 100.0, 0.0)
        w.st["pending"]["AAA"] = self._sig(w, bars, 0)   # signal on the 09:00 bar, due 10:00
        now = bars[1]["t"] + HOUR
        w._try_fill(now, w._common(now, [], True, {"tag": "UPTREND_CALM"}), "main", w.st, "AAA", bars[:2], {"trades_opened": 0})
        self.assertEqual(dt.datetime.fromisoformat(w.st["positions"]["AAA"]["entry_bar_t"].replace("Z", "+00:00")).astimezone(ET).hour, 10)
        self.assertEqual(CFG["session_bars"]["first_bar_start_hour_et"], 9)


class TestEarlyCloseEndRule(unittest.TestCase):
    """Change 1 (2026-11-27): last_day is Thu 2026-12-24, an NYSE early close (1:00 PM ET). Fri 12-25 is closed."""

    def _run(self, now_et, clock_seq):
        wk = tmpdir()
        with open(os.path.join(wk, "GO-COUNTED.flag"), "w") as fh:
            fh.write("t")
        fake = FakeAlpaca(clock_seq=clock_seq)
        fake.now = now_et.astimezone(UTC)
        env = {"APCA_API_KEY_ID": FAKE_KEY, "APCA_API_SECRET_KEY": FAKE_SECRET, "APCA_API_BASE_URL": guards.PAPER_URL}
        buf = io.StringIO()
        with mock.patch.dict(os.environ, env), mock.patch.object(runmod, "WATCH_WEEK", wk), mock.patch.object(runmod, "utcnow", lambda: fake.now), redirect_stdout(buf):
            runmod.main(["--counted", "--loop"], client_factory=lambda k, s, b: alpaca.AlpacaReadOnly(k, s, b, transport=fake), sleep=lambda n: None)
        return wk, buf.getvalue()

    def test_config_last_day_is_the_last_regular_trading_day_of_week_four(self):
        ld = dt.date.fromisoformat(CFG["end_rule"]["last_day"])
        self.assertEqual(ld, dt.date(2026, 12, 24))
        self.assertEqual(ld.weekday(), 3)

    def test_end_rule_applies_after_the_one_pm_early_close(self):
        wk, out = self._run(dt.datetime(2026, 12, 24, 13, 5, tzinfo=ET), [False])
        self.assertIn("end rule applied", out)
        self.assertTrue(json.loads(read(os.path.join(wk, "state.json")))["ended"])


class TestConfigExtra(unittest.TestCase):
    def test_new_sections_are_required_and_checked(self):
        for dotted in ("counting.min_score", "end_rule.last_day", "pdt.enforce", "regime.sma_slow", "sizing.step_up.enabled", "scorecard.haircut_views_bps"):
            c = copy.deepcopy(CFG)
            cur = c
            parts = dotted.split(".")
            for p in parts[:-1]:
                cur = cur[p]
            del cur[parts[-1]]
            with self.assertRaises(ValueError, msg=dotted):
                validate(c)
        c = copy.deepcopy(CFG)
        c["sizing"]["step_up"]["expectancy_haircut_bps"] = 7
        with self.assertRaises(ValueError):
            validate(c)
        c = copy.deepcopy(CFG)
        c["counting"]["min_score"] = 60
        with self.assertRaises(ValueError):
            validate(c)

    def test_repr_of_client_hides_keys(self):
        cl = alpaca.AlpacaReadOnly(FAKE_KEY, FAKE_SECRET, guards.PAPER_URL, transport=lambda u, h: (200, {}, b"{}"))
        self.assertNotIn(FAKE_KEY, repr(cl))
        self.assertNotIn(FAKE_SECRET, repr(cl) + str(cl))



class TestZacPendingExpiry(unittest.TestCase):
    """Change 6 (2026-11-27, tester pass 3 F2): Zac-ledger pending signals expire. A signal whose fill session passed
    (more than zac_ledger.max_pending_sessions weekdays after the signal date) is cancelled, never filled at a stale price."""

    def _zsig(self, w, t):
        return {"decision_id": "D000001", "signal_bar_t": iso(t), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
                "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}

    def _try(self, w, sig, bars, now):
        w.st["zac"]["pending"]["AAA"] = dict(sig)
        w._try_fill(now, w._common(now, [], True, {"tag": "RANGE"}), "zac", w.st["zac"], "AAA", bars, {"zac_trades_opened": 0})
        w.out.save_state(w.st)

    def test_signal_with_no_usable_bar_for_two_weeks_is_cancelled_not_filled_stale(self):
        w = Watcher(CFG, tmpdir(), "test")
        sig_t = hbars(7, dt.date(2026, 1, 5))[6]["t"]                     # Mon Jan 5, 15:00 ET
        late = hbars(35, dt.date(2026, 1, 19), 150.0, 0.0)                # data only from Mon Jan 19, price +50 percent
        now = late[-1]["t"] + HOUR
        self._try(w, self._zsig(w, sig_t), late, now)
        self.assertNotIn("AAA", w.st["zac"]["positions"])
        self.assertNotIn("AAA", w.st["zac"]["pending"])
        cancels = [x for x in scorecard.read_decisions(w.out.decisions) if x["action"] == "CANCEL" and x["ledger"] == "zac"]
        self.assertEqual(len(cancels), 1)
        self.assertIn("expired", cancels[0]["reason"])

    def test_friday_signal_fills_monday_and_monday_signal_fills_wednesday_but_thursday_is_too_late(self):
        w = Watcher(CFG, tmpdir(), "test")
        bars = hbars(7 * 8, dt.date(2026, 1, 5), 100.0, 0.0)
        by_day = {}
        for b in bars:
            by_day.setdefault(b["t"].astimezone(ET).date(), []).append(b)
        days = sorted(by_day)
        fri, nextmon = days[4], days[5]
        self.assertEqual((fri.weekday(), nextmon.weekday()), (4, 0))
        sig_fri = by_day[fri][-1]["t"]
        self._try(w, self._zsig(w, sig_fri), by_day[nextmon], by_day[nextmon][-1]["t"] + HOUR)
        self.assertIn("AAA", w.st["zac"]["positions"], "Friday signal, Monday 10:00 fill is the normal weekend case")
        # Monday signal, bars only from Wednesday (a one day data gap): 2 weekdays, still inside the default of 2
        w2 = Watcher(CFG, tmpdir(), "test")
        mon, wed, thu = days[0], days[2], days[3]
        self._try(w2, self._zsig(w2, by_day[mon][-1]["t"]), by_day[wed], by_day[wed][-1]["t"] + HOUR)
        self.assertIn("AAA", w2.st["zac"]["positions"])
        # Monday signal, bars only from Thursday: 3 weekdays, expired
        w3 = Watcher(CFG, tmpdir(), "test")
        self._try(w3, self._zsig(w3, by_day[mon][-1]["t"]), by_day[thu], by_day[thu][-1]["t"] + HOUR)
        self.assertNotIn("AAA", w3.st["zac"]["positions"])
        self.assertNotIn("AAA", w3.st["zac"]["pending"])

    def test_scan_cancels_a_stale_signal_even_when_the_symbol_has_no_bars_at_all(self):
        w = Watcher(CFG, tmpdir(), "test")
        sig_t = hbars(7, dt.date(2026, 1, 5))[6]["t"]
        w.st["zac"]["pending"]["AAA"] = self._zsig(w, sig_t)
        now = dt.datetime(2026, 1, 9, 15, tzinfo=UTC)                      # Fri Jan 9, 4 weekdays after the signal
        w.scan(now, {s: [] for s in CFG["symbols"]}, ["r"], clock_open=True)
        self.assertNotIn("AAA", w.st["zac"]["pending"])
        cancels = [x for x in scorecard.read_decisions(w.out.decisions) if x["action"] == "CANCEL" and x["ledger"] == "zac"]
        self.assertEqual(len(cancels), 1)
        self.assertIn("expired", cancels[0]["reason"])

    def test_config_value_is_required_validated_and_moves_the_hash(self):
        self.assertEqual(CFG["zac_ledger"]["max_pending_sessions"], 2)
        for bad in (0, -1, 1.5, True, "2", None):
            c = copy.deepcopy(CFG)
            c["zac_ledger"]["max_pending_sessions"] = bad
            with self.assertRaises(ValueError, msg=repr(bad)):
                validate(c)
        c = copy.deepcopy(CFG)
        del c["zac_ledger"]["max_pending_sessions"]
        with self.assertRaises(ValueError):
            validate(c)
        c = copy.deepcopy(CFG)
        c["zac_ledger"]["max_pending_sessions"] = 3
        self.assertNotEqual(config_hash(c), config_hash(CFG))


class TestBadEntryBarTOnOpenPosition(unittest.TestCase):
    """Change 7 (2026-11-27, tester pass 3 F3): a missing or garbage entry_bar_t on an open position must not crash _try_fill.
    It is logged as UNKNOWN (FAIL) and fails safe: the position counts as opened today in the PDT guard."""

    BAD = [("missing", None), ("empty", ""), ("garbage", "not-a-date"), ("none", False), ("int", 12345), ("list", ["x"])]

    def _world(self, kind, value, n_bad=1):
        c = copy.deepcopy(CFG)
        c["rules"]["max_open_positions"] = 8
        w = Watcher(c, tmpdir(), "test")
        bars = hbars(7 * 3, dt.date(2026, 1, 5), 100.0, 0.0)
        for i in range(n_bad):
            pos = make_pos(bars[0]["t"])
            pos["trade_id"] = "T%04d" % (i + 50)
            if kind == "missing":
                del pos["entry_bar_t"]
            elif kind == "none":
                pos["entry_bar_t"] = None
            else:
                pos["entry_bar_t"] = value
            w.st["positions"]["BAD%d" % i] = pos
        w.st["pending"]["AAA"] = {"decision_id": "D000001", "signal_bar_t": iso(bars[2]["t"]), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
                                  "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}
        now = bars[3]["t"] + HOUR
        return w, bars, now

    def test_every_bad_value_is_survived_and_logged_unknown_and_a_single_bad_entry_does_not_block(self):
        for kind, value in self.BAD:
            w, bars, now = self._world(kind, value)
            try:
                w._try_fill(now, w._common(now, [], True, {"tag": "RANGE"}), "main", w.st, "AAA", bars[:4], {"trades_opened": 0})
            except Exception as e:   # noqa: BLE001
                self.fail("%s: _try_fill crashed with %r" % (kind, e))
            w.out.save_state(w.st)
            self.assertIn("AAA", w.st["positions"], kind)
            unk = [x for x in scorecard.read_decisions(w.out.decisions) if x["action"] == "HOLD_UNKNOWN"]
            self.assertEqual(len(unk), 1, kind)
            self.assertEqual(unk[0]["symbol"], "BAD0")
            self.assertIn("FAIL: UNKNOWN", unk[0]["reason"])
            self.assertIn("entry_bar_t", unk[0]["reason"])

    def test_unknown_entry_date_fails_safe_by_counting_as_opened_today(self):
        # limit 3: three positions with an unknown entry date count as three potential day trades today, so the new entry is refused
        for kind, value in (("missing", None), ("garbage", "not-a-date")):
            w, bars, now = self._world(kind, value, n_bad=3)
            w._try_fill(now, w._common(now, [], True, {"tag": "RANGE"}), "main", w.st, "AAA", bars[:4], {"trades_opened": 0})
            w.out.save_state(w.st)
            self.assertNotIn("AAA", w.st["positions"], kind)
            self.assertNotIn("AAA", w.st["pending"], kind)
            self.assertTrue(any(x["action"] == "CANCEL" and "PDT guard" in x["reason"] for x in scorecard.read_decisions(w.out.decisions)), kind)

    def test_good_entries_are_unchanged_and_no_unknown_line_is_written(self):
        w, bars, now = self._world("garbage", "x", n_bad=0)
        w.st["positions"]["OK"] = make_pos(bars[0]["t"])
        w._try_fill(now, w._common(now, [], True, {"tag": "RANGE"}), "main", w.st, "AAA", bars[:4], {"trades_opened": 0})
        w.out.save_state(w.st)
        self.assertIn("AAA", w.st["positions"])
        self.assertFalse([x for x in scorecard.read_decisions(w.out.decisions) if x["action"] == "HOLD_UNKNOWN"])


class TestPdtUsesFillBarDate(unittest.TestCase):
    """Change 8 (2026-11-27, tester pass 3 F1): the PDT guard dates an entry by its FILL BAR (ET), not by the scan time,
    so a backfill after an outage still counts same-day fills (four same-day fills against limit 3)."""

    SYMS = ["AAA", "BBB", "CCC", "DDD"]

    def _run(self, ledger):
        c = copy.deepcopy(CFG)
        c["rules"]["max_open_positions"] = 8
        w = Watcher(c, tmpdir(), "test")
        bars = hbars(7 * 3, dt.date(2026, 1, 5), 100.0, 0.0)
        d1 = [b for b in bars if b["t"].astimezone(ET).date() == dt.date(2026, 1, 5)]
        d2 = [b for b in bars if b["t"].astimezone(ET).date() == dt.date(2026, 1, 6)]
        # main: signal on the 11:00 bar of day 1, fills on the 12:00 bar the SAME day. zac: signal at day 1 15:00, fills day 2 10:00.
        sig_bar, fill_day = (d1[2], d1) if ledger == "main" else (d1[6], d2)
        book = w.st if ledger == "main" else w.st["zac"]
        for i, s in enumerate(self.SYMS):
            book["pending"][s] = {"decision_id": "D%06d" % (i + 1), "signal_bar_t": iso(sig_bar["t"]), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
                                  "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}
        # the scan resumes the NEXT morning after an outage: the data holds the old bars, the clock is a later ET date
        now = dt.datetime(2026, 1, 8, 9, 5, tzinfo=ET).astimezone(UTC)
        sb = d1 + d2 if ledger == "zac" else d1
        common = w._common(now, [], True, {"tag": "RANGE"})
        for s in self.SYMS:
            w._try_fill(now, common, ledger, book, s, sb, {"trades_opened": 0, "zac_trades_opened": 0})
        w.out.save_state(w.st)
        refused = [x for x in scorecard.read_decisions(w.out.decisions) if x["action"] == "CANCEL" and "PDT guard" in x["reason"]]
        return book, refused

    def test_main_backfill_four_same_day_fills_the_fourth_is_refused(self):
        book, refused = self._run("main")
        self.assertEqual(sorted(book["positions"]), ["AAA", "BBB", "CCC"])
        self.assertEqual([x["symbol"] for x in refused], ["DDD"])

    def test_zac_backfill_four_same_day_fills_the_fourth_is_refused(self):
        book, refused = self._run("zac")
        self.assertEqual(sorted(book["positions"]), ["AAA", "BBB", "CCC"])
        self.assertEqual([x["symbol"] for x in refused], ["DDD"])

    def test_closed_day_trades_on_the_fill_date_count_too(self):
        # three closed day trades dated the fill day: a backfilled fill on that day is refused even though the scan date is later
        c = copy.deepcopy(CFG)
        c["pdt"]["max_day_trades_per_month"] = 99   # isolate the rolling 5 day rule
        w = Watcher(c, tmpdir(), "test")
        bars = hbars(7 * 2, dt.date(2026, 1, 5), 100.0, 0.0)
        d1 = [b for b in bars if b["t"].astimezone(ET).date() == dt.date(2026, 1, 5)]
        w.st["day_trades"] = ["2026-01-05"] * 3
        w.st["pending"]["AAA"] = {"decision_id": "D000001", "signal_bar_t": iso(d1[2]["t"]), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
                                  "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}
        now = dt.datetime(2026, 1, 12, 9, 5, tzinfo=ET).astimezone(UTC)
        w._try_fill(now, w._common(now, [], True, {"tag": "RANGE"}), "main", w.st, "AAA", d1, {"trades_opened": 0})
        self.assertNotIn("AAA", w.st["positions"])
        w.out.save_state(w.st)
        self.assertTrue(any("PDT guard" in x["reason"] for x in scorecard.read_decisions(w.out.decisions)))

    def test_live_same_day_case_is_unchanged(self):
        w = Watcher(CFG, tmpdir(), "test")
        bars = hbars(7, dt.date(2026, 1, 5), 100.0, 0.0)
        w.st["pending"]["AAA"] = {"decision_id": "D000001", "signal_bar_t": iso(bars[2]["t"]), "entry_ref": 100.0, "atr": 5.0, "score": 85.0,
                                  "setup": "t", "parts": {}, "regime": "UPTREND_CALM", "config_hash": w.chash}
        now = bars[3]["t"] + HOUR
        w._try_fill(now, w._common(now, [], True, {"tag": "RANGE"}), "main", w.st, "AAA", bars[:4], {"trades_opened": 0})
        self.assertIn("AAA", w.st["positions"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
