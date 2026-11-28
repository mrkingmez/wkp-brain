#!/usr/bin/env python3
"""Build the plan-input CSV for schedule_week.py --plan-csv (added 2026-11-26).

Zac 2026-11-26: Facebook and Instagram get TWO posts a day (default), YouTube Shorts one a day at 6 to 7 PM.
schedule_week.py itself is unchanged and the older hand-built CSV route (EP120, EP121) still works.

Input: an order file (JSON) listing days in order, each with the clips for that day best-first.
  {"days": [{"date": "2026-11-26", "clips": ["curationIdA", "curationIdB"], "youtube": "curationIdB"}, ...]}
Clips are posted to FB and IG in slot order; the per-platform slot times below come from WWD\\data\\post-times.md.
--fbig-per-day N uses the first N slots of each day (N=2 is the 2026-11-26 rule, a day with more clips than N is an error).

  python build_plan_csv.py order.json --copy EP122-approved-copy.json --out plan-input-P3112603SKaV.csv [--fbig-per-day 2]
Then: python schedule_week.py PROJECT --copy ... --plan-csv plan-input.csv --plan-out plan-checked.csv   (dry run)
"""
import argparse, csv, json
from datetime import date

# (facebook times, instagram times) per weekday, Mon=0. Source: WWD\data\post-times.md (2026-11-02), LOW to MED confidence.
SLOTS = {
    0: (["09:30", "12:00"], ["09:00", "18:00"]),
    1: (["09:30", "12:00"], ["09:00", "18:00"]),
    2: (["09:00", "12:00"], ["09:00", "18:00"]),
    3: (["09:00", "12:00"], ["09:00", "18:00"]),
    4: (["09:30", "12:00"], ["12:00", "18:00"]),
    5: (["11:00", "14:00"], ["10:00", "18:00"]),
    6: (["10:00", "13:00"], ["10:00", "18:00"]),
}
YT_TIME = "18:30"  # locked cadence: YouTube Shorts 6 to 7 PM ET
# Optional per-date overrides, for example a day that starts after the plan is approved: {"2026-11-26": (["15:30","18:00"], ["15:00","18:00"])}
OVERRIDES = {"2026-11-26": (["15:30", "18:00"], ["15:00", "18:00"])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("order")
    ap.add_argument("--copy", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fbig-per-day", type=int, default=2)
    a = ap.parse_args()
    order = json.load(open(a.order, encoding="utf-8"))["days"]
    cp = json.load(open(a.copy, encoding="utf-8"))
    titles = {c["id"]: (c.get("youtube", {}).get("title") or c.get("title", "")) for c in cp["clips"]}
    rows, used = [], set()
    for d in order:
        y, m, dd = map(int, d["date"].split("-"))
        fb, ig = OVERRIDES.get(d["date"]) or SLOTS[date(y, m, dd).weekday()]
        if len(d["clips"]) > a.fbig_per_day or len(d["clips"]) > min(len(fb), len(ig)):
            raise SystemExit(f"{d['date']}: {len(d['clips'])} clips exceeds the FB/IG per-day limit {a.fbig_per_day}")
        for i, cid in enumerate(d["clips"]):
            if cid in used:
                raise SystemExit(f"clip {cid} used twice")
            used.add(cid)
            if cid not in titles:
                raise SystemExit(f"clip {cid} has no approved copy")
            rows.append([d["date"], fb[i], "facebook", cid, titles[cid]])
            rows.append([d["date"], ig[i], "instagram", cid, titles[cid]])
        yt = d.get("youtube")
        if yt:
            if yt not in d["clips"]:
                raise SystemExit(f"{d['date']}: youtube clip must be one of that day's clips")
            rows.append([d["date"], YT_TIME, "youtube", yt, titles[yt]])
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows([["date", "time_et", "platform", "clip_id", "title"]] + rows)
    print(f"{len(rows)} rows, {len(used)} clips, FB/IG {a.fbig_per_day} per day. Wrote {a.out}")


if __name__ == "__main__":
    main()
