"""Offline tests (no network). Run: <python> -m unittest test_espn_snapshot -v  from this folder."""
import copy, json, os, sys, tempfile, unittest
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import espn_snapshot as es  # noqa: E402
base = es.base
FIX = os.path.join(es.REPO, "Fantasy-Football", "tracker", "fixtures")


def load(n):
    with open(os.path.join(FIX, n), encoding="utf-8") as f:
        return json.load(f)


class R:
    def __init__(self, d, code=200): self.d, self.status_code = d, code
    def raise_for_status(self):
        if self.status_code >= 400:
            import requests; raise requests.HTTPError(str(self.status_code))
    def json(self): return self.d


class S:
    def __init__(self, board, ranks): self.board, self.ranks, self.headers, self.n = board, ranks, {}, 0
    def get(self, url, params=None, timeout=None):
        self.n += 1
        return R(self.ranks if url.endswith("/rankings") else self.board)


def fetch(board=None):
    return base.Fetcher(cap=es.CALL_CAP, session=S(board or load("cfb_scoreboard_sample.json"),
                        load("cfb_rankings_sample.json")), sleep=lambda s: None)


class T(unittest.TestCase):
    def test_repo_root(self):
        self.assertTrue(os.path.exists(os.path.join(es.REPO, "CLAUDE.md")))

    def test_run_saves_dated_folder_and_ledger(self):
        with tempfile.TemporaryDirectory() as d:
            snap, path, moves, rc = es.run(fetch(), date(2026, 11, 12), 5, 5, d, True, datetime(2026, 11, 12, 9, 5))
            self.assertEqual(rc, 0)
            self.assertTrue(path.endswith(os.path.join("2026-11-12", "0905.json")))
            self.assertTrue(os.path.exists(os.path.join(d, "line_history.json")))
            self.assertEqual(snap["calls_made"], 12)  # 11 days + rankings, under cap
            self.assertFalse(snap["contains_injury_data"])

    def test_no_save_writes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            es.run(fetch(), date(2026, 11, 12), 0, 0, d, False)
            self.assertEqual(os.listdir(d), [])

    def test_ledger_keeps_line_after_game_final(self):
        board = load("cfb_scoreboard_sample.json")
        with tempfile.TemporaryDirectory() as d:
            es.run(fetch(board), date(2026, 11, 12), 0, 0, d, True, datetime(2026, 11, 12, 9, 5))
            final = copy.deepcopy(board)
            for e in final["events"]:
                e["competitions"][0].pop("odds", None)
                e["competitions"][0]["status"]["type"]["state"] = "post"
            es.run(fetch(final), date(2026, 11, 14), 0, 0, d, True, datetime(2026, 11, 14, 23, 0))
            with open(os.path.join(d, "line_history.json")) as fh:
                led = json.load(fh)
            self.assertTrue(led)
            self.assertTrue(all(e["history"] for e in led.values()))

    def test_ledger_records_only_changes_and_moves(self):
        g = base.parse_event(load("cfb_scoreboard_sample.json")["events"][0])
        led = {}
        es.update_ledger(led, [g], "t1")
        es.update_ledger(led, [g], "t2")
        self.assertEqual(len(led[g["game_id"]]["history"]), 1)
        g2 = copy.deepcopy(g); g2["odds"]["spread_home"] += 2.5
        es.update_ledger(led, [g2], "t3")
        self.assertEqual(len(led[g["game_id"]]["history"]), 2)
        mv = es.ledger_moves(led, {g["game_id"]})
        self.assertTrue(any(m["kind"].startswith("spread") for m in mv))

    def test_corrupt_ledger_is_reported_not_fatal(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "line_history.json"), "w") as fh:
                fh.write("{bad")
            snap, path, moves, rc = es.run(fetch(), date(2026, 11, 12), 0, 0, d, True)
            self.assertEqual(rc, 0)
            self.assertTrue(any("ledger" in m for m in snap["not_retrieved"]))

    def test_empty_board_returns_1(self):
        with tempfile.TemporaryDirectory() as d:
            snap, path, moves, rc = es.run(fetch({"events": []}), date(2026, 11, 12), 0, 0, d, True)
            self.assertEqual(rc, 1)
            self.assertEqual(os.listdir(d), [])

    def test_call_cap(self):
        f = base.Fetcher(cap=3, session=S(load("cfb_scoreboard_sample.json"), load("cfb_rankings_sample.json")), sleep=lambda s: None)
        snap = base.build_snapshot(f, date(2026, 11, 12), 5, 5)
        self.assertEqual(f.calls, 3)
        self.assertTrue(snap["not_retrieved"])

    def test_pass_leaders_from_game_level_leaders(self):
        ev = {"date": "d", "competitions": [{"status": {"type": {"state": "post"}},
              "competitors": [{"team": {"id": "1", "abbreviation": "AAA"}}, {"team": {"id": "2", "abbreviation": "BBB"}}],
              "leaders": [{"name": "passingYards", "leaders": [{"displayValue": "20/30", "team": {"id": "2"},
                          "athlete": {"displayName": "Q B"}}]}]}]}
        out = es.pass_leaders([{"events": [ev]}, None, {"events": [{"bad": 1}]}])
        self.assertEqual(out, {"BBB": {"player": "Q B", "line": "20/30", "kickoff": "d"}})

    def test_string_odds_and_wrong_shape_ledger(self):
        g = base.parse_event(load("cfb_scoreboard_sample.json")["events"][0])
        g["odds"]["total"] = "54.5"
        led = {}
        es.update_ledger(led, [g], "t1")
        es.ledger_moves(led)  # must not raise
        es.ledger_moves({"1": "x", "2": {"history": 5}})
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "line_history.json"), "w") as fh:
                fh.write("[]")
            snap, path, moves, rc = es.run(fetch(), date(2026, 11, 12), 0, 0, d, True, datetime(2026, 11, 12, 9, 5))
            self.assertEqual(rc, 0)
            self.assertTrue(any(n.startswith("line_history.json.corrupt") for n in os.listdir(d)))

    def test_no_secrets_in_source(self):
        with open(os.path.join(HERE, "espn_snapshot.py"), encoding="utf-8") as fh:
            src = fh.read().lower()
        for bad in ("api_key", "apikey", "bearer", "password"):
            self.assertNotIn(bad, src)


if __name__ == "__main__":
    unittest.main()
