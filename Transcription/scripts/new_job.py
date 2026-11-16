"""Start a Fiverr transcription job.

Interactive:   python new_job.py
Or with flags: python new_job.py --gig 1 --order FO123 --handle pastor_bob --minutes 45 --price 40 --types docx,txt --due 2026-11-16

Creates the job folder (JOB-YYYYMMDD-NNN_gig_handle) under D:/Transcription Jobs from _template,
adds the tracker row (Waiting on = Zac, because Zac accepts the order),
stamps the start time. No network.
"""
import argparse
import datetime as dt
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tjlib as T

VALID_TYPES = {"docx", "txt", "md", "pdf", "srt", "vtt", "csv"}


def ask(prompt, default=None, required=True):
    while True:
        try:
            s = input(f"{prompt}{f' [{default}]' if default else ''}: ").strip()
        except EOFError:
            sys.exit(f"Missing value for: {prompt}. Pass it as a flag (see --help).")
        if not s and default is not None:
            return default
        if s or not required:
            return s
        print("  needed.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gig", type=int, choices=[1, 2, 3, 4])
    ap.add_argument("--order")
    ap.add_argument("--handle")
    ap.add_argument("--minutes", type=float)
    ap.add_argument("--price", type=float)
    ap.add_argument("--types")
    ap.add_argument("--due")
    ap.add_argument("--speakers", type=int)
    a = ap.parse_args()

    if a.gig is None:
        print("Gigs: " + "  ".join(f"{k}={v}" for k, v in T.GIG_NAMES.items()))
        a.gig = int(ask("Gig number (1-4)"))
    if a.gig not in T.GIGS:
        sys.exit("Gig must be 1 to 4.")
    a.order = a.order or ask("Fiverr order number (type 'none' if not yet ordered)")
    a.handle = a.handle or ask("Buyer handle")
    if a.minutes is None:
        a.minutes = float(ask("Audio minutes (from ffprobe or the order)"))
    if a.price is None:
        a.price = float(ask("Price (the number Zac agreed, no $)"))
    default_types = "srt,vtt" if a.gig == 3 else "docx,txt"
    a.types = a.types or ask("File types the buyer wants (docx,txt,md,pdf,srt,vtt,csv)", default_types)
    a.due = a.due or ask("Due date YYYY-MM-DD", required=False)

    types = [t.strip().lower().lstrip(".") for t in a.types.replace(" ", ",").split(",") if t.strip()]
    bad = [t for t in types if t not in VALID_TYPES]
    if bad:
        sys.exit(f"Unsupported file type(s): {bad}. Supported: {sorted(VALID_TYPES)}")
    if a.due:
        dt.date.fromisoformat(a.due)

    date_str = T.today()
    jid = f"JOB-{date_str.replace('-', '')}-{T.next_job_number(date_str):03d}"
    folder = os.path.join(T.JOBS_ROOT, f"{jid}_{T.GIGS[a.gig]}_{T.slug(a.handle)}")
    if os.path.exists(folder):
        sys.exit(f"Folder already exists: {folder}")
    if not os.path.isdir(T.TEMPLATE_DIR):
        sys.exit(f"Template missing: {T.TEMPLATE_DIR}")
    shutil.copytree(T.TEMPLATE_DIR, folder)

    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    subs = {"{{JOB_ID}}": jid, "{{GIG}}": str(a.gig), "{{GIG_NAME}}": T.GIG_NAMES[a.gig],
            "{{HANDLE}}": a.handle, "{{CREATED}}": stamp, "{{ORDER}}": a.order,
            "{{AUDIO_MIN}}": f"{a.minutes:g}", "{{PRICE}}": f"${a.price:g}",
            "{{FILE_TYPES}}": ", ".join(types), "{{DUE}}": a.due or "(not set)"}
    p = os.path.join(folder, "notes.md")
    with open(p, encoding="utf-8") as f:
        text = f.read()
    for k, v in subs.items():
        text = text.replace(k, v)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)

    T.write_job_json(folder, {"job_id": jid, "gig": a.gig, "gig_name": T.GIG_NAMES[a.gig],
                              "order": a.order, "handle": a.handle, "audio_minutes": a.minutes,
                              "price": a.price, "file_types": types, "due": a.due,
                              "created": stamp, "speakers": a.speakers})
    T.append_to_notes(folder, f"- {stamp}  job created, start time stamped")
    T.tracker_upsert(jid, {
        "Status": "Intake", "Date received": date_str, "Gig (1-4)": a.gig,
        "Fiverr order #": a.order, "Buyer handle": a.handle, "Audio minutes": a.minutes,
        "Speakers": a.speakers, "Requested file types": ", ".join(types), "Due date": a.due,
        "Price": a.price, "Waiting on": "Zac", "Revisions": 0,
        "Notes": "Intake: Zac sends buyer questions and accepts the order"})
    print(f"\nJob created: {jid}")
    print(f"Folder:  {folder}")
    print(f"Tracker: {T.TRACKER_XLSX}  (Waiting on = Zac)")
    print("Next: Zac accepts the order, downloads the audio into 01-raw-audio, then run:")
    print('  python "' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'run_pipeline.py') + '" ' + jid)


if __name__ == "__main__":
    main()
