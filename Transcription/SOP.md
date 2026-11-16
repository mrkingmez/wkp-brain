# Transcription SOP (workflow for every job)

Legend: **[AGENT]** = an agent does it. **[ZAC STEPS IN]** = only Zac can do it. Agents draft messages, Zac sends them. `PY` = `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe`, `S` = `D:\WKP\Transcription\scripts`.
Nothing is urgent unless Zac says so. Check the due date on the order before you promise anything.

## Where Zac steps in (the short list)
1. Accept the order on Fiverr.
2. Download the buyer's file from the order into `01-raw-audio`.
3. Send every message to a buyer (questions, quote, delivery note, revision reply, review request).
4. Approve any price quote.
5. Upload the delivery on Fiverr.
6. Request the review.
7. Type the Fiverr fee in the tracker (no script can verify it).
8. Anything that posts publicly.
9. A quick spot-check read of the master for the first 3 jobs of each gig.
`PY S\job_status.py` lists open jobs, Zac items first.

## Steps
| # | Step | Who | Waiting on after | Command or detail |
|---|---|---|---|---|
| 0 | Inquiry or order arrives | [ZAC STEPS IN] reads it, hands the details to an agent | agent | Zac tells the agent: buyer handle, what they want, length, file |
| 1 | Intake check: length (ffprobe), audio quality 1 to 5 (listen to 2 minutes), speaker count, what the buyer wants, which file types, names and terms to spell, deadline, verbatim or clean | [AGENT] | Zac | `ffprobe -v error -show_entries format=duration -of csv=p=0 <file>` |
| 2 | Draft the buyer questions and a go or no-go note (is it inside what the pipeline does well; flag sensitive content) | [AGENT] drafts | Zac | Draft only |
| 3 | Send the questions to the buyer | [ZAC STEPS IN] | buyer | On Fiverr |
| 4 | Price quote or custom offer | [ZAC STEPS IN] | buyer | Zac's number, agents only supply time estimates from the tracker |
| 5 | Accept the order | [ZAC STEPS IN] | Zac | On Fiverr |
| 6 | Create the job folder and tracker row | [AGENT] | Zac | `PY S\new_job.py` (asks gig, order number, handle, minutes, price, file types) |
| 7 | Download the buyer's audio or video into `01-raw-audio` | [ZAC STEPS IN] | agent | Agents cannot log in to Fiverr |
| 8 | Run the local pipeline. One speaker (sermon, captions): `PY S\run_pipeline.py JOB`. Two or more: add `--speakers N`. Add `--also-timed` if subtitles are wanted on a multi-speaker job | [AGENT] | agent | Machine time logs itself. Output: `02-working\<name>_draft_raw.txt` (do not edit), `_master.txt` (edit this), `_segments.json` |
| 9 | Proofread with the clock running. Fix names, terms, scripture references, punctuation, speaker turns, numbers. Listen to every low-confidence stretch. Keep each line as `[HH:MM:SS] Speaker N: text` | [AGENT] | agent | `PY S\job_clock.py start JOB proofreading` ... `pause` and `resume` for breaks ... `stop` |
| 10 | Spot-check read of the master (first 3 jobs of each gig, then optional) | [ZAC STEPS IN] | Zac | About 10 minutes. Replace `Speaker 1` with a real name only if the buyer gave it |
| 11 | Convert to every requested file type | [AGENT] | agent | `PY S\convert_deliverable.py JOB` (formats come from job.json) or `--formats docx,srt`. `--clean` removes timestamps and merges same-speaker lines. Clock category: conversion |
| 12 | Check `03-final-documents`: every requested type present, filenames end with the type, files open, nothing from another job. First jobs of each gig also go to qa-director | [AGENT] | agent | |
| 13 | Draft the delivery message (what is attached, one line on the file types, offer of one fix round) | [AGENT] drafts | Zac | Draft only. No claims about accuracy that were not measured |
| 14 | Upload the files from `03-final-documents` on Fiverr and send the delivery | [ZAC STEPS IN] | buyer | |
| 15 | Record delivery in the tracker | [AGENT] | none | `PY S\close_job.py JOB --delivered now --keep-open` if revisions are possible, or without `--keep-open` to close |
| 16 | Enter price and Fiverr fee in the tracker | [ZAC STEPS IN] | none | `PY S\job_status.py JOB --set "Fiverr fee (Zac enters, NOT verified)=4"` or type it in the xlsx (close Excel first if a script says the file is locked) |
| 17 | Draft the review request | [AGENT] drafts | Zac | Draft only |
| 18 | Send the review request | [ZAC STEPS IN] | buyer | On Fiverr. Anything public is Zac's |
| 19 | Revisions: agent drafts the reply and makes the fix, Zac sends and re-uploads | [AGENT] + [ZAC STEPS IN] | buyer | Log revisions with `close_job.py JOB --revisions N` |
| 20 | Close: review received, final numbers | [AGENT] | none | `PY S\close_job.py JOB --review yes` |

## Gig notes
1. **Sermons.** Ask for the church's spelling of names and the Bible version if verses are quoted. Check every scripture reference. Usually one speaker, `--speakers 1`.
2. **Podcasts.** Ask for host and guest names. Diarization is good but not perfect, check the turns. Timestamps on by default, `--clean` if the buyer wants a reading copy.
3. **Captions.** Run `--speakers 1` (precise millisecond times from `_segments.json`). Cues are 42 characters a line, 2 lines. Proofread timing by playing the video with the .srt loaded (VLC or Premiere) for the first and last minute plus three random spots. The converter splits cues by character count, it does not break on phrases, so tell the buyer if they need phrase-aware breaks, that is extra proofreading time.
4. **General.** If it is not clear speech (music, heavy accents, bad room noise), Zac decides before accepting. Legal, medical, counseling or anything with minors goes to Zac first.

## Tracker
`D:\WKP Reports\Transcription Tracker\Transcription Tracker.xlsx`. Sheet "Jobs" has one row per job (rows with Waiting on = Zac turn yellow). Gray-header columns are formulas: On time, Net, Total min worked, $ per audio min, $ per hour worked, work-min per audio-min. Sheet "Summary by gig" rolls them up by gig. The CSV next to it is rewritten by every script. If a script says the file is locked, close it in Excel and run again, nothing was changed.
