r"""Offline tests for cfb_snapshot.py. Uses saved ESPN sample responses in
fixtures\ (trimmed copies of real 2026-11-11 pulls). No network.
Run: <python> -m unittest Fantasy-Football\tracker\test_cfb_snapshot -v
 or: cd tracker; <python> test_cfb_snapshot.py"""
import copy
import json
import os
import sys
import tempfile
import unittest
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cfb_snapshot as cs  # noqa: E402

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def load(name):
    with open(os.path.join(FIX, name), encoding="utf-8") as f:
        return json.load(f)


class FakeResp:
    def __init__(self, data, status=200):
        self.data, self.status_code = data, status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests_error(self.status_code)

    def json(self):
        return self.data


def requests_error(code):
    import requests
    return requests.HTTPError(f"HTTP {code}")


class FakeSession:
    def __init__(self, board, ranks, fail_dates=()):
        self.board, self.ranks, self.fail_dates = board, ranks, fail_dates
        self.headers, self.urls = {}, []

    def get(self, url, params=None, timeout=None):
        self.urls.append((url, params))
        if url.endswith("/rankings"):
            return FakeResp(self.ranks)
        if params and params.get("dates") in self.fail_dates:
            return FakeResp({}, 500)
        # same sample for every day; dedup by id happens in the script
        return FakeResp(self.board)


def fetcher(board=None, ranks=None, **kw):
    return cs.Fetcher(session=FakeSession(board or load("cfb_scoreboard_sample.json"),
                                          ranks or load("cfb_rankings_sample.json"), **kw),
                      sleep=lambda s: None)


class Tests(unittest.TestCase):
    def test_parse_event_sign_and_open_line(self):
        ev = load("cfb_scoreboard_sample.json")["events"][0]
        g = cs.parse_event(ev)
        self.assertEqual((g["away"], g["home"]), ("DUKE", "MIA"))
        # ESPN home line -13.5 (home favored) -> repo convention +13.5
        self.assertEqual(g["odds"]["spread_home"], 13.5)
        self.assertEqual(g["odds"]["open_spread_home"], 20.5)
        self.assertEqual(g["odds"]["total"], 54.5)
        self.assertEqual(g["odds"]["open_total"], 55.5)
        self.assertIn("passingLeader", g["leaders"]["home"])

    def test_num(self):
        self.assertEqual(cs._num("o54.5"), 54.5)
        self.assertEqual(cs._num("PK"), 0.0)
        self.assertIsNone(cs._num("x"))
        self.assertIsNone(cs._num(None))

    def test_snapshot_dedup_and_calls(self):
        f = fetcher()
        snap = cs.build_snapshot(f, date(2026, 11, 11), 5, 5, now=datetime(2026, 11, 11, 9, 30))
        self.assertEqual(len(snap["games"]), 3)  # 11 identical days deduped
        self.assertEqual(f.calls, 12)  # 11 days + rankings
        self.assertFalse(snap["contains_injury_data"])
        self.assertTrue(snap["rankings"])

    def test_cache_within_run(self):
        f = fetcher()
        f.get(cs.RANKINGS, None)
        f.get(cs.RANKINGS, None)
        self.assertEqual(f.calls, 1)

    def test_call_cap(self):
        f = cs.Fetcher(cap=3, session=FakeSession({}, {}), sleep=lambda s: None)
        snap = cs.build_snapshot(f, date(2026, 11, 11), 5, 5)
        self.assertEqual(f.calls, 3)
        self.assertTrue(any("call cap" in m for m in snap["not_retrieved"]))

    def test_failure_message_names_what_is_missing(self):
        f = fetcher(fail_dates=("20261111",))
        snap = cs.build_snapshot(f, date(2026, 11, 11), 1, 1)
        self.assertTrue(any("scoreboard 20261111" in m and "not retrieved" in m for m in snap["not_retrieved"]))
        self.assertEqual(len(snap["games"]), 3)

    def test_user_agent_generic(self):
        f = fetcher()
        ua = f.session.headers["User-Agent"]
        self.assertNotIn("@", ua)
        self.assertNotIn("kingz", ua.lower())
        self.assertNotIn("zac", ua.lower())

    def test_diff_finds_moves_of_one_point_only(self):
        f = fetcher()
        old = cs.build_snapshot(f, date(2026, 11, 11), 0, 0)
        new = copy.deepcopy(old)
        new["games"][0]["odds"]["spread_home"] += 1.0     # 1.0 -> reported
        new["games"][1]["odds"]["spread_home"] += 0.5     # 0.5 -> ignored
        new["games"][2]["odds"]["total"] -= 2.5           # total move reported
        d = cs.diff_snapshots(old, new)
        kinds = sorted((m["kind"], m["move"]) for m in d["moves"])
        self.assertEqual(kinds, [("spread (home fav +)", 1.0), ("total", -2.5)])

    def test_end_to_end_save_and_diff(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "cfb")
            rc = cs.main(["--out", out, "--back", "0", "--ahead", "0"], fetcher=fetcher(),
                         today=date(2026, 11, 11), now=datetime(2026, 11, 11, 9, 0))
            self.assertEqual(rc, 0)
            files = os.listdir(out)
            self.assertEqual(files, ["2026-11-11-0900-cfb.json"])
            board = load("cfb_scoreboard_sample.json")
            board["events"][0]["competitions"][0]["odds"][0]["pointSpread"]["home"]["close"]["line"] = "-15.5"
            import io
            from contextlib import redirect_stdout
            buf = io.StringIO()
            with redirect_stdout(buf):
                cs.main(["--out", out, "--back", "0", "--ahead", "0"], fetcher=fetcher(board=board),
                        today=date(2026, 11, 12), now=datetime(2026, 11, 12, 9, 0))
            text = buf.getvalue()
            self.assertEqual(len(os.listdir(out)), 2)
            self.assertIn("NO INJURY DATA", text)
            self.assertIn("SECONDARY", text)
            self.assertIn("DUKE at MIA", text)
            self.assertIn("+2", text)

    def test_header_printed_even_when_nothing_retrieved(self):
        import io
        from contextlib import redirect_stdout
        f = cs.Fetcher(session=FakeSession({}, {}, fail_dates=tuple(
            d.strftime("%Y%m%d") for d in [date(2026, 11, 11)])), sleep=lambda s: None)
        buf = io.StringIO()
        with redirect_stdout(buf), tempfile.TemporaryDirectory() as tmp:
            rc = cs.main(["--out", tmp, "--back", "0", "--ahead", "0"], fetcher=f,
                         today=date(2026, 11, 11), now=datetime(2026, 11, 11, 9, 0))
        self.assertEqual(rc, 1)
        self.assertIn("NO INJURY DATA", buf.getvalue())
        self.assertIn("NOT RETRIEVED", buf.getvalue())


class CfbdSession:
    """Fake CFBD: answers by path, records calls, never needs a real key."""
    def __init__(self, fail=()):
        self.calls, self.fail = [], fail

    def get(self, url, params=None, headers=None, timeout=None):
        path = url.replace(cs.CFBD, "")
        self.calls.append((path, params, headers))
        if path in self.fail:
            return FakeResp({}, 500)
        data = {
            "/calendar": [{"week": 10, "seasonType": "regular", "startDate": "2026-11-02T00:00:00Z", "endDate": "2026-11-08T23:59:00Z"},
                          {"week": 11, "seasonType": "regular", "startDate": "2026-11-09T00:00:00Z", "endDate": "2026-11-16T07:59:00Z"}],
            "/lines": [{"id": 401856885, "homeTeam": "LSU", "awayTeam": "Texas",
                        "lines": [{"provider": "DraftKings", "spread": -4.0, "spreadOpen": 2.5, "overUnder": 46.5, "overUnderOpen": 47.5}]},
                       {"id": 1, "homeTeam": "A", "awayTeam": "B", "lines": []}],
            "/ratings/sp": [{"team": "LSU", "rating": 22.9, "ranking": 7}, {"team": "Texas", "rating": 23.5, "ranking": 5}],
            "/ratings/elo": [{"team": "LSU", "elo": 1800}, {"team": "Texas", "elo": 1900}],
            "/ratings/fpi": [{"team": "LSU", "fpi": 22.5}, {"team": "Texas", "fpi": 23.9}],
        }[path]
        return FakeResp(data)


class CfbdTests(unittest.TestCase):
    def test_block_week_sign_flip_ratings_and_budget(self):
        s = CfbdSession()
        b = cs.cfbd_block(date(2026, 11, 12), session=s, key="TESTKEY", sleep=lambda x: None)
        self.assertEqual(b["week"], 11)
        self.assertEqual(b["calls_made"], 5)                       # the monthly budget depends on this number
        self.assertEqual(len(b["lines"]), 1)                       # a game with no book is dropped
        bk = b["lines"][0]["books"][0]
        self.assertEqual((bk["spread_home"], bk["open_spread_home"]), (4.0, -2.5))   # home favored is positive here
        self.assertEqual(b["ratings"]["LSU"], {"sp": 22.9, "sp_rank": 7, "elo": 1800, "fpi": 22.5})
        m = cs.rating_margins(b, "LSU", "Texas")
        self.assertEqual(m["sp"], 1.9)
        self.assertAlmostEqual(m["elo"], round(0.0404 * -100 + 3.98, 1))
        self.assertTrue(all(h == {"Authorization": "Bearer TESTKEY"} for _, _, h in s.calls))

    def test_key_never_lands_in_the_snapshot(self):
        b = cs.cfbd_block(date(2026, 11, 12), session=CfbdSession(), key="SECRET-KEY-123", sleep=lambda x: None)
        self.assertNotIn("SECRET-KEY-123", json.dumps(b))

    def test_failure_is_listed_not_raised(self):
        b = cs.cfbd_block(date(2026, 11, 12), session=CfbdSession(fail=("/ratings/sp",)), key="K", sleep=lambda x: None)
        self.assertTrue(any("/ratings/sp" in m for m in b["not_retrieved"]))
        self.assertIn("elo", b["ratings"]["LSU"])

    def test_no_key_says_not_available(self):
        old = cs.cfbd_key
        cs.cfbd_key = lambda: None
        try:
            b = cs.cfbd_block(date(2026, 11, 12), session=CfbdSession())
        finally:
            cs.cfbd_key = old
        self.assertEqual(b["calls_made"], 0)
        self.assertIn("not available", b["not_retrieved"][0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
