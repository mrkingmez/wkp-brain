"""Damaged and reshaped watcher files must never crash the data layer or break JSON.
Run: python -I tests\\test_hardening.py
"""
import json
import shutil
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "tests"))
import ffdata  # noqa: E402
from test_dashboard import paths_for  # noqa: E402

TMP = Path(r"D:\WKP\scratch\ffdash-hardening")
NOW = datetime(2026, 12, 1, 15, 2, tzinfo=timezone.utc)
NL = "\n"


class TestHardening(unittest.TestCase):
    def setUp(self):
        if TMP.exists():
            shutil.rmtree(TMP)
        TMP.mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(TMP, ignore_errors=True)

    def run_state(self, lines, trades=None, state=None):
        (TMP / "decisions.jsonl").write_text(NL.join(lines) + NL, encoding="utf-8")
        if trades is not None:
            (TMP / "paper-trades.csv").write_text(NL.join(trades) + NL, encoding="utf-8")
        if state is not None:
            (TMP / "state.json").write_text(state, encoding="utf-8")
        s = ffdata.build_state(paths=paths_for(TMP), now=NOW)
        json.dumps(ffdata.clean(s), allow_nan=False)
        return s

    def test_nan_in_regime_detail(self):
        self.run_state(['{"action":"REGIME","regime":"RANGE","ts_utc":"2026-12-01T15:00:00Z","regime_detail":{"atr_pct":NaN,"close":Infinity}}'])

    def test_mixed_naive_and_aware_times(self):
        self.run_state(['{"action":"SKIP","symbol":"A","ts_utc":"2026-12-01T15:00:00"}',
                        '{"action":"SKIP","symbol":"B","ts_utc":"2026-12-01T15:01:00Z","clock_open":true}'])

    def test_zero_equity_and_odd_state(self):
        st = json.dumps({"starting_equity": 0, "zac": "oops", "closed_stats": "nope"})
        self.run_state(['{"action":"SKIP","symbol":["x"],"ts_utc":"2026-12-01T15:00:00Z","spy_mark":0}'],
                       ["trade_id,event,ts_utc,ledger", "T1,CLOSE,2026-12-01T15:00:00,main"], st)

    def test_bad_closed_stats(self):
        st = json.dumps({"starting_equity": 100, "zac": [], "closed_stats": [1, {"net": [1]}, {"net": {"5": "x"}}]})
        s = self.run_state(['{"action":"SKIP","symbol":"A","ts_utc":"2026-12-01T15:00:00Z","spy_mark":5}'],
                           ["trade_id,event,ts_utc,ledger,pnl_net", "T1,CLOSE,2026-12-01T15:00:00,main,5"], st)
        self.assertEqual(s["ledgers"]["main"]["closed_n"], 1)

    def test_insider_odd_shapes(self):
        d = TMP / "insider"
        d.mkdir()
        (d / "clusters.jsonl").write_text('{"issuer":"str","last_filing_date":5}' + NL + '{"issuer":{"ticker":"A"},"last_filing_date":"2026-01-01"}' + NL, encoding="utf-8")
        s = ffdata.build_insider(paths_for(TMP))
        self.assertTrue(s["available"])
        json.dumps(ffdata.clean(s), allow_nan=False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
