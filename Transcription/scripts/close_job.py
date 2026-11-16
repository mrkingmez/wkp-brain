"""Close out a job: final numbers into the tracker, recompute the computed columns.

  python close_job.py JOB --delivered 2026-11-14 --revisions 0 --review yes --fee 8
Any flag you leave out is asked for (press Enter to skip). Flags:
  --delivered YYYY-MM-DD, or the word now
  --price N  --fee N       fee is Zac's number, NOT verified by this script
  --revisions N  --review yes|no|none  --quality 1-5  --notes "text"
  --keep-open              record numbers but leave Status = Delivered (for revisions)
  --no-prompt              never ask, use only the flags
Stops any running clock first. Sets Waiting on = none (buyer with --keep-open).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tjlib as T
import job_clock


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job")
    ap.add_argument("--delivered")
    ap.add_argument("--price")
    ap.add_argument("--fee")
    ap.add_argument("--revisions")
    ap.add_argument("--review")
    ap.add_argument("--quality")
    ap.add_argument("--notes")
    ap.add_argument("--keep-open", action="store_true")
    ap.add_argument("--no-prompt", action="store_true")
    a = ap.parse_args()
    folder = T.find_job(a.job)
    jid = T.job_id_of(folder)

    state = T.load_clock(folder)
    if state["running"]:
        job_clock.stop_running(folder, state)
        T.save_clock(folder, state)

    def get(val, prompt):
        if val is not None or a.no_prompt:
            return val
        s = input(prompt + " (Enter to skip): ").strip()
        return s or None

    f = {}
    d = get(a.delivered, "Delivered date YYYY-MM-DD, or 'now'")
    if d:
        f["Delivered date"] = T.today() if d == "now" else d
    for val, prompt, col in ((a.price, "Price", "Price"),
                             (a.fee, "Fiverr fee in dollars (your number, unverified)", T.FEE),
                             (a.revisions, "Revisions", "Revisions"),
                             (a.review, "Review received (yes/no/none, or stars)", "Review received"),
                             (a.quality, "Audio quality 1-5", "Audio quality 1-5"),
                             (a.notes, "Closing note", "Notes")):
        v = get(val, prompt)
        if v is not None:
            f[col] = v
    for c in T.CATEGORIES:
        f[T.CAT_COL[c]] = round(state["totals"][c] / 60, 1)
    f.setdefault("Notes", "Delivered, open for revisions" if a.keep_open else "Closed")
    f["Status"] = "Delivered" if a.keep_open else "Closed"
    f["Waiting on"] = "buyer" if a.keep_open else "none"
    T.tracker_upsert(jid, f)
    word = "delivered (open for revisions)" if a.keep_open else "closed"
    T.append_to_notes(folder, f"- {T.today()}  job {word}; tracker updated")
    row = T.tracker_get(jid)
    print(f"{jid} {word}. Computed numbers:")
    for h in ("On time", "Net", "Total min worked", "$ per audio min", "$ per hour worked",
              "Work-min per audio-min"):
        print(f"  {h}: {row.get(h)!r}")
    if row.get("Net") in ("", None):
        print("  (no Net yet: enter the Fiverr fee, then dollar figures fill in)")


if __name__ == "__main__":
    main()
