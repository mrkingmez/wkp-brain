"""Running clock for a job, by category: machine, proofreading, conversion, admin.

  python job_clock.py start  JOB proofreading   start a timer (stops any running one first)
  python job_clock.py pause  JOB                stop the running timer, remember its category
  python job_clock.py resume JOB                restart the paused category
  python job_clock.py stop   JOB                stop the running timer
  python job_clock.py add    JOB machine 12.5   add minutes by hand (for work done off the clock)
  python job_clock.py status JOB

Every stop writes a line in notes.md (Timer log) and updates the tracker minutes columns.
JOB can be the job ID (JOB-20261113-001) or the folder path. No network.
"""
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tjlib as T


def now():
    return dt.datetime.now()


def push(folder, state):
    jid = T.job_id_of(folder)
    fields = {T.CAT_COL[c]: round(state["totals"][c] / 60.0, 1) for c in T.CATEGORIES}
    T.tracker_upsert(jid, fields)


def stop_running(folder, state, note=""):
    if not state["running"]:
        return None
    cat = state["running"]
    secs = (now() - dt.datetime.fromisoformat(state["since"])).total_seconds()
    state["totals"][cat] += secs
    T.append_to_notes(folder, f"- {now():%Y-%m-%d %H:%M}  {cat}: {secs / 60:.1f} min {note}".rstrip())
    state["running"], state["since"] = None, None
    return cat, secs


def add_minutes(folder, cat, minutes, note="added"):
    state = T.load_clock(folder)
    state["totals"][cat] += minutes * 60
    T.append_to_notes(folder, f"- {now():%Y-%m-%d %H:%M}  {cat}: {minutes:.1f} min ({note})")
    T.save_clock(folder, state)
    push(folder, state)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd, ref = sys.argv[1], sys.argv[2]
    folder = T.find_job(ref)
    state = T.load_clock(folder)
    if cmd == "start":
        if len(sys.argv) < 4 or sys.argv[3] not in T.CATEGORIES:
            sys.exit(f"Category must be one of {T.CATEGORIES}")
        stop_running(folder, state)
        state["running"], state["since"], state["paused"] = sys.argv[3], now().isoformat(), None
        T.save_clock(folder, state)
        push(folder, state)
        print(f"Clock running: {sys.argv[3]} (started {now():%H:%M:%S})")
        return
    if cmd in ("stop", "pause"):
        r = stop_running(folder, state, "(paused)" if cmd == "pause" else "")
        if r and cmd == "pause":
            state["paused"] = r[0]
        T.save_clock(folder, state)
        push(folder, state)
        print(f"{cmd}: {r[0]} {r[1] / 60:.1f} min" if r else "Nothing was running.")
        return
    if cmd == "resume":
        cat = state.get("paused")
        if not cat:
            sys.exit("Nothing paused.")
        state["running"], state["since"], state["paused"] = cat, now().isoformat(), None
        T.save_clock(folder, state)
        print(f"Clock running: {cat}")
        return
    if cmd == "add":
        cat, mins = sys.argv[3], float(sys.argv[4])
        if cat not in T.CATEGORIES:
            sys.exit(f"Category must be one of {T.CATEGORIES}")
        add_minutes(folder, cat, mins, "added by hand")
        print(f"Added {mins:g} min to {cat}")
        return
    if cmd == "status":
        run = state["running"]
        for c in T.CATEGORIES:
            extra = 0
            if run == c:
                extra = (now() - dt.datetime.fromisoformat(state["since"])).total_seconds()
            print(f"  {c:13s} {(state['totals'][c] + extra) / 60:7.1f} min" + ("   <- running" if run == c else ""))
        if state.get("paused"):
            print(f"  paused: {state['paused']}")
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
