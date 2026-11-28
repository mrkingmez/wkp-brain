# SOP: WWD Review Workflow (A Knight's Tale model)

Created 2026-11-19 (system reset). Owner: **wwd-director**. Zac is the editor and Matt makes thumbnails. Zac is only in the loop for recording, editing, money and posting.
Paths and formats: `SOP-Output-Locations-and-Formats.md`. Standards: `D:\WKP\WWD\STANDARDS.md`.

## Why it felt slow (evidence, 2026-11-19)

- The agent prep for A Knight's Tale took about 48 minutes (transcript 20:36, run sheet 21:24 on 11/19, `logs\wwd-director.md` lines 440 to 447). The benches were not the slow part.
- **The chain starts late.** It waited for the transcript of Zac's EDITED cut. So Zac edited the talk, then waited for pictures and clips, then went back into the timeline to place 49 stops by hand. Vision Quest EP 8 sat about 46 hours between transcript and run sheet because nobody kicked off the chain until the 11/16 sleep-work doc.
- **Rules changed mid-run.** The clip rule moved from 4 s to 6 to 12 s during the job, so clips and the run sheet were rebuilt twice. `STANDARDS.md` still said 4 s.
- **Missing pieces were found last.** The run sheet reported "intro/outro music not found" and "end card and Next Up card not on disk". Nobody owned the music catalog. The channel theme is at `L:\Winter Wolfs Den review show\Audio\Main Channel Theme.mp3` and was never indexed.
- **Zac placed every stop by hand.** No stringout or Premiere-ready layer existed.
- Some steps were blocked and left loose: the IMDb bot wall, and the `_src\` delete was denied by the permission check.

Fixes in this SOP: start at intake, pull in parallel, music and kit ordered on day one, a prep stringout from the editing department, and rules read from STANDARDS (now corrected).

## The flow

| # | When | Who | Input | Output (see Output SOP for paths) | Budget |
|---|---|---|---|---|---|
| 0 | Zac says "we are doing a review on <title>" | wwd-director | title | movie folder, base 18 pictures (wwd-pictures, Review Intake Mode), CALENDAR NEEDED flag to Jarvis (wwd-director has no calendar tool; Jarvis adds the record and release dates and lists the calendar to confirm they exist), **music** ordered (intro sting 6 s max, outro, owned picks first), **wwd-vfx** checks end card and Next Up card exist for the show and builds if not | 45 min |
| 1 | Recording done (raw files land in `<movie>\Raw\`) | wwd-director | title only (NO raw transcript: WWD CLAUDE.md lock 2026-10-18, never transcribe or build from a raw recording before Zac cuts the banter) | nothing that needs the talk | |
| 2 | Day after recording, in parallel | wwd-clip-scout | title | **clip stock**: official trailer and official clip downloads, Premiere Ready muted copies, shot map with true shot edges. Not yet tied to lines, so step 4 only has to cut, not hunt | 40 min |
| 2b | same time | wwd-pictures | title | stills beyond the base 18 for every main character with a subplot, tagged | 30 min |
| 3 | Zac exports the Premiere transcript of his edited cut into the movie folder | Zac | his cut | `.txt` in movie folder. **This is the trigger.** When Zac says the transcript is in, or Jarvis or chief-of-staff sees a new `.txt` in an open review's movie folder, step 4 starts without waiting to be asked (no automatic watcher exists yet) | |
| 4 | Within the hour, benches in parallel where inputs allow | wwd-pictures (gap fill and fit), wwd-clip-scout (cut stock clips to host lines), fact-research (on-air claims), wwd-sound (cue plan), then wwd-run-sheet (sheet, lint, proof) | edited-cut transcript plus steps 0 to 2b | Edit Run Sheet .md and .docx, sound plan, facts | 45 min |
| 5 | Right after 4 | assistant-editor (WWD practice and prep job), media-manager, head-editor | run sheet, USE, clips | **PREP stringout** in `<movie>\prep\` that Zac drops on V2, plus assembly plan and head-editor notes. Zac may use or ignore it | 45 min |
| 6 | Before package | wwd-rights | clips, stills, music | rights note | 20 min |
| 7 | wwd-director proof | wwd-director | all above | proof against STANDARDS, one send-back max per bench, then qa-director | 15 min |
| 8 | Zac edits and exports the final video into the movie folder | Zac | | final mp4 | Zac's time |
| 9 | Export lands | wwd-review-pipeline (via wwd-director) builds the package frame, AUDIO and shorts; copy order: marketing-director brief, script-room copywriting writes, slop_check (mechanical), judgment pass by marketing-director or Jarvis, qa-director. The skill never hand-writes copy (its rule 16) | final mp4 plus transcript | upload package, AUDIO mp3, 5 shorts max, captions in the package | 45 min |
| 10 | Package ready | Jarvis | | one message to Zac: what is ready, the exact posts and any spend (only those need him). Zac posts | |

## Hand-offs (no Zac in the loop)

- wwd-director sends every handoff with the AGENT-NETWORK note format and names the SOP row.
- Benches hand back to wwd-director with a check line (what was verified and how). No check line, it goes back once.
- On-air factual errors found by fact-research go into the run sheet "Still open" block and the package (pinned correction draft). The team decides the fix (caption, trim or leave), per the zero-question rule 2026-11-11. Only a public post goes to Zac.
- FrostCast (not a review) follows the chain in root CLAUDE.md "FrostCast Transcription Workflow". The Messenger send to Matt stays a manual flag from wwd-director to Jarvis (no browser tool in subagents); Jarvis sends and screenshots "Sent".
- A blocked step (IMDb wall, denied delete, missing kit) is logged in `logs\wwd-director.md` and TASKS.md in the same run. It never just stays in a bench report.

## Rules that travel with every WWD review

- Pictures: max 7 s on screen, never the same picture twice, gap-fill from the title being reviewed, contain and fit, never crop.
- Clips: 6 to 8 s, 12 s max, muted, inside one shot, on a spoken line. Report the total seconds, wwd-rights flags the exposure.
- Music: intro and outro only, intro sting 6 s max, owned first, no bed under the talk.
- No on-screen actor name tags. Matt is Winter Wolf, Zac is KingZ.
- Run sheet: one timeline-order list, revise in place, LIKE AND SUBSCRIBE stop, no new Spoiler Alert build.
- Logs: `logs\wwd-director.md` entry plus one `logs\agent-runs.md` row per bench, plus one lesson per bench in `memory\agents\`.
- Money (ElevenLabs, Firefly, VidIQ credits) and posting: Zac only, with the exact cost or post.


## Sound pull alongside the run sheet (LOCKED 2026-11-21, Zac)
When wwd-run-sheet builds the run sheet, assistant-editor pulls every sound it names into `P:\WWD Kit\<Movie>\Sounds\` at the same time (see SOP-Editing-Department.md). Zac imports from that one place. If Zac changes the run sheet, the pull is updated.
