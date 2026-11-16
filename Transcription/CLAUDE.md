# Transcription (Fiverr side business)

Decided by Zac 2026-11-13: build it and run four gigs. Overrides the earlier HOLD. Zac is an established Fiverr seller (his own statement: over $7,000 since 2016, level and rating not known yet, see `memory\user-fiverr-history.md`).

## The four gigs
| # | Gig | Slug | Typical files | Watch for |
|---|---|---|---|---|
| 1 | Church sermons | sermons | docx, txt, pdf | Scripture references, names, church terms, one speaker plus a prayer or reading |
| 2 | Podcasts and audio shows | podcast | docx, txt, md, srt | 2 to 4 speakers, speaker labels, timestamps, crosstalk |
| 3 | Video captions (subtitle files) | captions | srt, vtt | Timing accuracy, 42 characters a line, two lines a cue, reading speed |
| 4 | General (wide net) | general | any | Accept only what the pipeline handles well. Sensitive content (legal, medical, confidential) goes to Zac before any quote |

## Who does what
Agents run the pipeline, proofread, convert, track and draft messages. **Zac steps in** for: accepting an order on Fiverr, downloading the buyer's file, every message to a buyer, any price quote, uploading the delivery, requesting a review, anything public. Agents only draft. The step-by-step with every step marked [AGENT] or [ZAC STEPS IN] is `SOP.md`. Each job also carries the same checklist in its `notes.md`.
See what needs Zac right now: `python D:\WKP\Transcription\scripts\job_status.py` (the tracker column "Waiting on" is Zac, agent, buyer or none).

## Where things live
| What | Where |
|---|---|
| This folder (rules, SOP, scripts, notes template), in git | `D:\WKP\Transcription\` |
| Job folders, client files, OUTSIDE the repo and OUTSIDE scratch | `D:\Transcription Jobs\<JOB-YYYYMMDD-NNN>_<gig>_<buyerhandle>\` |
| Inside a job | `01-raw-audio`, `02-working` (draft, master, wav, segments.json), `03-final-documents` (every finished deliverable, one per requested file type, filename ends `_transcript.docx` or `_captions.srt`), `notes.md`, `job.json` |
| Template for new jobs | `D:\Transcription Jobs\_template\` (copy of `Transcription\templates\notes.md` plus the three folders) |
| Tracker | `D:\WKP Reports\Transcription Tracker\Transcription Tracker.xlsx` plus `.csv` mirror the scripts write |
| Scripts | `D:\WKP\Transcription\scripts\` |

Never put a client file in `D:\WKP\scratch\` (the nightly safe-fixes deletes scratch files older than 14 days).

## Rules
1. Client files never go in git, never to a cloud tool or API without the buyer's consent. Default is the local pipeline only. No signups, no spend, no posting without Zac.
2. Never run client audio against `D:\WKP\voiceprints`. That would label a client as Zac, Matt or Gabby. `run_pipeline.py` points the diarizer at an empty folder, relabels to Speaker 1, Speaker 2, and aborts if a host name shows up as a label.
3. Ask the buyer questions before accepting (length, audio quality, speakers, file types, names, deadline, verbatim or clean). Zac sends them.
4. Run the clock. Time by category (machine, proofreading, conversion, admin) is what tells Zac if a gig pays per hour.
5. The Fiverr fee in the tracker is typed by Zac and is NOT verified by any script.
6. Honest limits: Whisper large-v3 is a draft, not a final. Proofreading is not optional. No accuracy percentage is promised to a buyer until measured on real jobs.
7. Open items for Zac to check, not verified by this build: Fiverr's current rules on using AI or automated tools to deliver work and any disclosure it requires, and whether each buyer needs to consent to local AI processing. Zac checks the Fiverr terms for his account before the first order.
8. Pricing is Zac's. Nothing in these files is a quoted price.
9. Child-safety and privacy: a recording with minors or private personal details (counseling, medical, legal) goes to Zac before work starts.

## Scripts (Python 3.12 from LOCAL-PATHS, no network)
Run with `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe` (below written as `python`).
| Script | What it does |
|---|---|
| `new_job.py` | Asks gig, order number, handle, audio minutes, price, file types, due date. Creates the folder, notes.md, job.json, tracker row (Waiting on = Zac), stamps start time |
| `run_pipeline.py JOB [--speakers N] [--also-timed]` | ffmpeg to wav, local Whisper large-v3 (and pyannote diarization when speakers is 2 or more), generic labels, writes draft and master, logs machine time |
| `job_clock.py start/pause/resume/stop/add/status JOB [category]` | Timers by category, writes notes.md and the tracker |
| `convert_deliverable.py JOB [--formats ...] [--clean] [--title ...]` | Master in 02-working to docx, txt, md, pdf, srt, vtt, csv in 03-final-documents |
| `close_job.py JOB` | Delivered date, price, fee, revisions, review, final minutes, recomputes the computed columns |
| `job_status.py [JOB --waiting ... --set COLUMN=VALUE]` | Who the jobs are waiting on, edit any tracker cell safely |
| `tjlib.py` | Shared code (paths, tracker read and write) |

## Start a job
```
python D:\WKP\Transcription\scripts\new_job.py
```
It prints the next command. Full flow in `SOP.md`.
