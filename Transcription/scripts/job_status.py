"""See what needs Zac, and change a job's Waiting on or Status.

  python job_status.py                          list open jobs, Zac items first
  python job_status.py JOB --waiting buyer      set Waiting on (Zac / agent / buyer / none)
  python job_status.py JOB --status "In progress"
  python job_status.py JOB --set "Audio quality 1-5=4" --set "Speakers=2"
Waiting on = Zac means a Zac step in notes.md is the next thing in the way.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tjlib as T


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job", nargs="?")
    ap.add_argument("--waiting", choices=T.WAITING)
    ap.add_argument("--status")
    ap.add_argument("--set", action="append", default=[], metavar="COLUMN=VALUE")
    a = ap.parse_args()
    if a.job and (a.waiting or a.status or a.set):
        jid = T.job_id_of(T.find_job(a.job))
        f = {}
        if a.waiting:
            f["Waiting on"] = a.waiting
        if a.status:
            f["Status"] = a.status
        for kv in a.set:
            k, _, v = kv.partition("=")
            f[k.strip()] = v.strip()
        T.tracker_upsert(jid, f)
        print(f"{jid} updated: {f}")
        return
    rows = [r for r in T.tracker_rows() if r.get("Status") != "Closed"]
    order = {"Zac": 0, "agent": 1, "buyer": 2, "none": 3}
    rows.sort(key=lambda r: order.get(r.get("Waiting on") or "none", 3))
    if not rows:
        print("No open jobs.")
    for r in rows:
        print(f"{(r.get('Waiting on') or '-'):6s} {r['Job ID']}  gig {r.get('Gig (1-4)')}  "
              f"{r.get('Status')}  due {str(r.get('Due date') or '')[:10]}  {r.get('Notes') or ''}")


if __name__ == "__main__":
    main()
