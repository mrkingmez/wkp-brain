"""python test_scout_state.py  -> checks the character rules hold. No test framework needed."""
import datetime as dt
import json
from pathlib import Path

import scout_state as ss

MOCK = Path(__file__).parent / "mock_data"
DAY = dt.datetime.combine(dt.date.today(), dt.time(10, 0))
EVE = DAY.replace(hour=20)
load = lambda n: json.loads((MOCK / n).read_text(encoding="utf-8"))


def test_thriving():
    v, _ = ss.step(load("1_thriving.json"), {}, DAY)
    assert v["mood"] == ss.THRIVING and v["overlays"] == []


def test_buried():
    v, _ = ss.step(load("2_buried.json"), {}, DAY)
    assert v["mood"] == ss.BURIED and v["counts"]["overdue"] == 4 and v["counts"]["blocked"] == 2


def test_special_layers_on_top_of_buried():
    v, _ = ss.step(load("3_birthday_on_hard_week.json"), {}, DAY)
    assert v["mood"] == ss.BURIED and "SPECIAL" in v["overlays"]


def test_reaction_fires_once_then_expires():
    d = load("4_episode_live.json")
    v1, m = ss.step(d, {}, DAY)
    assert "REACTION" in v1["overlays"] and "EP117" in v1["line"]
    v2, m = ss.step(d, m, DAY + dt.timedelta(seconds=ss.REACTION_SECONDS + 1))
    assert "REACTION" not in v2["overlays"]
    v3, _ = ss.step(d, m, DAY + dt.timedelta(seconds=60))
    assert "REACTION" not in v3["overlays"], "same event must not fire twice"


def test_recap_picks_biggest_thing():
    d = load("4_episode_live.json")
    _, m = ss.step(d, {}, DAY)                        # burn the reaction first
    v, _ = ss.step(d, m, EVE)
    assert "RECAP" in v["overlays"] and "EP117" in v["line"]


def test_hysteresis_holds_mood():
    one = load("5_one_overdue_holds_mood.json")
    v, _ = ss.step(one, {"mood": ss.THRIVING}, DAY)
    assert v["mood"] == ss.THRIVING
    assert "clear" not in v["line"].lower() and "nothing overdue" not in v["line"].lower(), "must not claim a clear board"
    v, _ = ss.step(one, {"mood": ss.BURIED}, DAY)
    assert v["mood"] == ss.BURIED


def test_no_guilt_lines():
    for pool in ss.LINES.values():
        for line in pool:
            assert not any(b in line.lower() for b in ss.BANNED), line
            assert "—" not in line


if __name__ == "__main__":
    n = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            n += 1
            print("pass", name)
    print(f"{n} tests passed")
