"""Tests for the Fawn Forest dashboard data layer and server. Run:
  python -I tests\\test_dashboard.py
Uses temp fixture folders under D:\\WKP\\scratch\\ffdash-tests (never touches real files).
"""
import json
import shutil
import sys
import threading
import unittest
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import ffdata  # noqa: E402
import server  # noqa: E402

TMP = Path(r"D:\WKP\scratch\ffdash-tests")


def paths_for(base: Path, source="live"):
    p = ffdata.default_paths(source)
    p.update({"dir": base, "decisions": base / "decisions.jsonl", "trades": base / "paper-trades.csv",
              "state": base / "state.json", "history": base / "config-history.jsonl",
              "scorecard": base / "scorecard.md", "notes": base / "daily-notes.md",
              "flag": base / "GO-COUNTED.flag", "insider_dir": base / "insider", "crypto_dir": base / "crypto"})
    return p


class Base(unittest.TestCase):
    def setUp(self):
        if TMP.exists():
            shutil.rmtree(TMP)
        TMP.mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(TMP, ignore_errors=True)


class TestMissing(Base):
    def test_empty_folder_says_not_available(self):
        s = ffdata.build_state(paths=paths_for(TMP))
        self.assertFalse(s["available"])
        self.assertIn("NOT AVAILABLE", s["message"])
        self.assertIn("decisions.jsonl", s["missing"])
        self.assertTrue(s["paper_only"])
        self.assertEqual(s["crypto"]["status"], "NOT BUILT")
        self.assertFalse(s["insider"]["available"])
        json.dumps(s, allow_nan=False)

    def test_flag_state(self):
        p = paths_for(TMP)
        self.assertEqual(ffdata.build_state(paths=p)["week"]["go_counted"]["state"], "NOT SET")
        p["flag"].write_text("x")
        self.assertEqual(ffdata.build_state(paths=p)["week"]["go_counted"]["state"], "SET")


class TestDamaged(Base):
    def test_bad_lines_and_garbage(self):
        d = TMP / "decisions.jsonl"
        d.write_text('not json\n{"action":"SKIP","symbol":"AAA","ts_utc":"2026-12-01T15:00:00Z","clock_open":true,"counted":false}\n[1,2]\n\n{"ts_utc":5}\n', encoding="utf-8")
        (TMP / "paper-trades.csv").write_text("garbage,,\n1,2\n", encoding="utf-8")
        (TMP / "state.json").write_text("{broken", encoding="utf-8")
        s = ffdata.build_state(paths=paths_for(TMP), now=datetime(2026, 12, 1, 15, 2, tzinfo=timezone.utc))
        self.assertTrue(s["available"])
        self.assertGreaterEqual(s["bad_lines"], 2)
        json.dumps(s, allow_nan=False)

    def test_nan_and_inf_never_reach_json(self):
        self.assertIsNone(ffdata.num("nan"))
        self.assertIsNone(ffdata.num("inf"))
        self.assertIsNone(ffdata.num(""))
        self.assertEqual(ffdata.num("2.5"), 2.5)

    def test_missing_state_means_ledgers_not_available(self):
        (TMP / "decisions.jsonl").write_text('{"action":"SKIP","symbol":"AAA","ts_utc":"2026-12-01T15:00:00Z","clock_open":true}\n', encoding="utf-8")
        (TMP / "paper-trades.csv").write_text("trade_id,event\n", encoding="utf-8")
        s = ffdata.build_state(paths=paths_for(TMP), now=datetime(2026, 12, 1, 15, 1, tzinfo=timezone.utc))
        self.assertFalse(s["ledgers"]["available"])
        self.assertIn("missing", s["ledgers"])


class TestDemoNumbers(unittest.TestCase):
    """Numbers shown must equal the watcher's own scorecard (demo-out)."""

    @classmethod
    def setUpClass(cls):
        cls.s = ffdata.build_state("demo")

    def test_demo_flag(self):
        self.assertTrue(self.s["demo"])

    def test_matches_scorecard(self):
        m = self.s["ledgers"]["main"]
        self.assertEqual(m["closed_n"], 26)
        self.assertEqual(m["net_pnl"], 1540.11)
        self.assertEqual(m["haircut"]["levels"]["30"]["net"], -1773.44)
        z = self.s["ledgers"]["zac"]
        self.assertEqual(z["closed_n"], 22)
        self.assertEqual(z["haircut"]["levels"]["15"]["net"], -291.55)
        self.assertEqual(self.s["spy"]["return_pct"], 10.716)
        self.assertEqual(self.s["week"]["counted_decisions"], 39)

    def test_low_sample(self):
        self.assertEqual(self.s["ledgers"]["main"]["sample_label"], "LOW SAMPLE")

    def test_crypto_never_invented(self):
        self.assertFalse(self.s["crypto"]["available"])

    def test_checklist_zero_of_seven(self):
        self.assertEqual((self.s["checklist"]["passed"], self.s["checklist"]["total"]), (0, 7))

    def test_curve_limit(self):
        self.assertLessEqual(len(self.s["spy"]["curve"]), ffdata.MAX_CURVE_POINTS + 1)


class TestStale(Base):
    def test_stale_when_market_open_and_old(self):
        (TMP / "decisions.jsonl").write_text('{"action":"SKIP","symbol":"AAA","ts_utc":"2026-12-01T15:00:00Z","clock_open":true}\n', encoding="utf-8")
        s = ffdata.build_state(paths=paths_for(TMP), now=datetime(2026, 12, 1, 16, 0, tzinfo=timezone.utc))
        self.assertTrue(s["freshness"]["stale"])
        s = ffdata.build_state(paths=paths_for(TMP), now=datetime(2026, 12, 1, 15, 2, tzinfo=timezone.utc))
        self.assertFalse(s["freshness"]["stale"])


class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = server.ThreadingHTTPServer((server.HOST, 0), server.Handler)
        cls.port = cls.httpd.server_address[1]
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()

    def get(self, path, method="GET", headers=None):
        req = urllib.request.Request("http://127.0.0.1:%d%s" % (self.port, path), method=method, headers=headers or {})
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                return r.status, r.read(), r.headers
        except urllib.error.HTTPError as e:
            return e.code, b"", e.headers

    def test_bound_to_loopback(self):
        self.assertEqual(self.httpd.server_address[0], "127.0.0.1")

    def test_page_and_state(self):
        self.assertEqual(self.get("/")[0], 200)
        code, body, hdr = self.get("/api/state?source=demo")
        self.assertEqual(code, 200)
        self.assertTrue(json.loads(body)["demo"])
        self.assertIn("default-src 'self'", hdr["Content-Security-Policy"])

    def test_only_get(self):
        for m in ("POST", "PUT", "DELETE", "PATCH"):
            self.assertEqual(self.get("/api/state", method=m)[0], 405, m)

    def test_traversal_and_unknown(self):
        for p in ("/../server.py", "/..%2fserver.py", "/ffdata.py", "/data/go-live-checklist.json", "/static/app.js", "/%2e%2e/server.py"):
            self.assertEqual(self.get(p)[0], 404, p)

    def test_bad_source_and_bad_host(self):
        self.assertEqual(self.get("/api/state?source=../../x")[0], 400)
        self.assertEqual(self.get("/", headers={"Host": "evil.example"})[0], 403)
        self.assertEqual(self.get("/", headers={"Host": "localhost:abc@evil"})[0], 403)
        self.assertEqual(self.get("/", headers={"Host": "localhost:abc@evil"})[0], 403)


class TestThemes(unittest.TestCase):
    def test_badges_never_themed_away(self):
        html = (HERE / "static" / "index.html").read_text(encoding="utf-8")
        js = (HERE / "static" / "app.js").read_text(encoding="utf-8")
        css = (HERE / "static" / "themes.css").read_text(encoding="utf-8") + (HERE / "static" / "style.css").read_text(encoding="utf-8")
        self.assertIn("PAPER ONLY", html)
        self.assertIn("DEMO DATA", html)
        self.assertIn('data-theme="ares"', css)
        self.assertIn('data-theme="jarvis"', css)
        self.assertNotIn("PAPER ONLY\": ", js)      # no word swap for the badge
        self.assertNotRegex(css, r"paper-badge[^}]*display:\s*none")
        self.assertNotRegex(css, r"demo-banner[^}]*display:\s*none")
        self.assertIn("localStorage", js)


class TestNoDangerousCode(unittest.TestCase):
    """The product must have no order words, no key reads, no outbound network code."""

    def test_source_greps(self):
        import re
        banned = [r"os\.environ", r"getenv", r"APCA_", r"requests", r"urllib\.request", r"socket\.connect", r"/v2/orders", r"\bplace_order\b", r"submit_order",
                  r"api[_-]?key", r"secret"]
        for f in [HERE / "ffdata.py", HERE / "server.py", HERE / "static" / "app.js", HERE / "static" / "index.html"]:
            text = f.read_text(encoding="utf-8")
            for pat in banned:
                self.assertIsNone(re.search(pat, text, re.I), "%s matches %s" % (f.name, pat))
        html = (HERE / "static" / "index.html").read_text(encoding="utf-8")
        self.assertNotRegex(html, r"<(form|input|textarea)")
        self.assertNotRegex((HERE / "static" / "app.js").read_text(encoding="utf-8"), r"innerHTML|method:\s*[\"']POST|eval\(")
        self.assertNotRegex(html + (HERE / "static" / "style.css").read_text(encoding="utf-8"), r"https?://")

    def test_open_calls_are_read_only(self):
        import re
        for f in [HERE / "ffdata.py", HERE / "server.py"]:
            for m in re.finditer(r"open\(([^)]*)\)", f.read_text(encoding="utf-8")):
                self.assertNotRegex(m.group(1), r"[\"'][wax]\+?b?[\"']", f.name + ": " + m.group(0))
            self.assertNotRegex(f.read_text(encoding="utf-8"), r"write_text|write_bytes|\.unlink|os\.remove|shutil")


if __name__ == "__main__":
    unittest.main(verbosity=2)
