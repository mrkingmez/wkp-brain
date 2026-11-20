# SOP: Output Locations and Formats

Created 2026-11-19 (system reset). ONE table for where every deliverable goes and what it looks like.
Zac's complaint that started this: "formats changing, saving stuff to new places." From now on an agent that saves somewhere not in this table is wrong, even if an older skill line says otherwise.

## Base rules

1. **Deliverable a human reads** (guide, report, run sheet, package, worksheet): `.docx` at `D:\WKP Reports\<Type Folder>\<YYYY-MM-DD> - <Name>.docx`. The working `.md` stays in the repo (never in `D:\WKP Reports\`). Source: root CLAUDE.md, locked 2026-10-05.
2. **Raw media and media-side outputs** (pictures, clips, exports, shorts, audio) live next to the source on `L:\` or `P:\`. L: is NOT a deliverables location (root CLAUDE.md line "Deliverables: L:\" is stale, corrected 2026-11-19).
3. **Working documents are revised in place** (run sheets, upload packages, plans for one title): a revision overwrites the same file name, no second dated copy unless Zac asks for side-by-side versions. **Recurring reports** (Monday brief, Saturday wrap, guides re-issued later) get a new dated file each run, every dated version kept, per root CLAUDE.md 2026-10-05. Video renders keep v1, v2 (never overwrite a render Zac may already be using).
4. **One type folder per deliverable type** in `D:\WKP Reports\`. Use the exact folder names below. Do not invent a new folder when one in this table fits.
5. Scratch: `D:\WKP\scratch\<job>\`. Never system Temp. Delete scratch only through the system check.

## WWD

| Deliverable | Folder | File name | Format | Owner |
|---|---|---|---|---|
| Review transcript (Premiere, Zac's edited cut) | movie folder `L:\Winter Wolfs Den review show\Raw Footage\<Movie>\` | as Zac saves it | .txt | Zac |
| Diarized transcript (FrostCast, raw recordings) | same folder as the video | `<video-name>_transcript.txt` | .txt | wwd-video-transcriber |
| Chapters | inside the upload package description; chat copy | n/a | text, `00:00:00 - Start` first | wwd-frostcast-chapters |
| Picture set | `<movie folder>\USE\` (originals in `<movie folder>\` then deleted; temp downloads `_src\` deleted after resize) | `NN-<slug>.png`, plus `pictures-tags.md` | 1920x1080 PNG, contain and fit, alpha padding, never crop | wwd-pictures |
| Picture placements (working list) | `<movie folder>\USE\timeline-placements.md` | fixed name | .md, feeds the run sheet only, not a deliverable | wwd-pictures |
| Trailer clips | `<movie folder>\clips\` (`source\`, `Premiere Ready\`, cut files), `clip-list.md` | `<SHORT>-clip-N-<slug>.mp4` | muted H.264, 6 to 8 s, 12 s max, no total cap (Zac 2026-11-19) | wwd-clip-scout |
| Edit Run Sheet | .md `D:\WKP\WWD\reports\<Movie>-Edit-Run-Sheet.md`; .docx `D:\WKP Reports\Asset Placement Run Sheets\<YYYY-MM-DD> - <Movie> Edit Run Sheet.docx` plus one copy in the movie folder | name "Edit Run Sheet" (never "Image Placement") | one timeline-order list, revise in place | wwd-run-sheet |
| Rights note | `D:\WKP\WWD\reports\<Movie>-Rights-Note.md` | fixed | .md (internal) | wwd-rights |
| Sound plan | `D:\WKP\WWD\reports\<Movie>-Sound-Plan.md` (was scratch, moved 2026-11-19 so it is findable) | fixed | .md | wwd-sound |
| Music picks and prompts | .md `D:\WKP\WWD\reports\<Movie>-Music.md`; .docx `D:\WKP Reports\Music Prompts\<YYYY-MM-DD> - <Movie> Music.docx`; chosen owned track copied to `P:\WWD Kit\<Show>\Sounds\` | | intro sting 6 s max | music |
| Kit pieces (cards, stickers, stings, openers) | `P:\WWD Kit\<Show>\` or `P:\WWD Kit\Cards\`, `Stickers\`, `Transitions\` | as wwd-vfx names them | MP4 or PNG | wwd-vfx |
| LUTs | `P:\WWD Kit\Color\<look> <date>.cube` | | .cube | wwd-color |
| Editing prep (stringout, assembly plan) | video `<movie folder>\prep\`; plan .md `D:\WKP\WWD\reports\<Movie>-Prep-Assembly-Plan.md` | `<Movie>-PREP-Stringout-vN.mp4` | silent H.264, black gaps | assistant-editor |
| Final export | movie folder | Zac's name | mp4 | Zac |
| Upload package | .md `D:\WKP\WWD\reports\<Movie>-Upload-Package.md` (the ONE working copy); .docx in the movie folder (editor copy) AND `D:\WKP Reports\WWD Upload Packages\<Movie> Upload Package\<YYYY-MM-DD> - <Movie> Upload Package.docx` | | shorts captions merged in, no separate captions doc (2026-10-18) | wwd-review-pipeline |
| Review shorts | `<movie folder>\shorts\` | `clipN-<slug>.mp4` plus cover PNG | 5 max, 30 to 75 s, burned-in captions | wwd-review-pipeline |
| Audio-only review | `<movie folder>\AUDIO\<Title>.mp3` | | mp3 | wwd-review-pipeline |
| FrostCast audio cut | `L:\Winter Wolfs Den review show\Audio\podcast Frostcast audio files\FrostCast ep ### YYYY-MM-DD.md` plus `.docx` beside it | | one chronological Start/Cut list; .docx required from 2026-11-19 on (no backfill) | wwd-audio-cut |
| FrostCast Opus shorts copy | `D:\WKP\WWD\opusclip\EPnnn-approved-copy.json`, plan csv, schedule-log | | cadence per root CLAUDE.md 2026-11-11; copy written by script-room copywriting desk from a marketing-director brief, EP 119 set format, gates run | wwd-director |
| FrostCast show prep | .md `D:\WKP\WWD\reports\FrostCast-EPnnn-Show-Prep.md`; .docx `D:\WKP Reports\FrostCast\<YYYY-MM-DD> - FrostCast EPnnn Show Prep.docx` | | | wwd-show-prep |
| Review prep (pre-record notes) | `D:\WKP Reports\Review Prep\<YYYY-MM-DD> - <Movie> Review Prep.docx` | | | wwd-director |
| Weekly social and planner package | `L:\Winter Wolfs Den review show\<date> Week of <Mon DD>\` (01 Images to 05 Social Copy) | | the 2026-09-16 week-folder rule now covers ONLY this weekly package | wwd-weekly-planner, marketing |
| Shorts copy for social (review or FrostCast) | inside the upload package (reviews) or the Opus json (FrostCast). Folder `D:\WKP Reports\WWD Shorts Copy\` only for a printable copy | | | brief by marketing-director, written by script-room copywriting desk, slop_check plus judgment pass, Zac posts |

## Studio, Music, Everything else

| Deliverable | Folder | Format |
|---|---|---|
| Studio project package, rough cut plans | .md `D:\WKP\Post-Production\reports\`; .docx `D:\WKP Reports\<Project Name>\` (one folder per project, e.g. `Ian Book Trailer`) | .md + .docx |
| Rough cut renders (non-WWD) | the project's own media folder on P: (e.g. `P:\01 Warrior King Productions\02 Video Project\<Project>\Rough Cut\`), versioned v1, v2 | mp4 |
| Documentary assembly plans | .md `D:\WKP\WKP-CHANNEL\reports\`; .docx `D:\WKP Reports\<Episode>\` | |
| Research briefs | `D:\WKP\research\<topic>\YYYY-MM-DD-<slug>.md` | .md (internal) |
| WKP channel research spine and premise bank | `D:\WKP\research\channel\` (create on first job), premise bank `premise-bank.md` | .md (internal) |
| Scripts (any venture, from script-room) | the venture's own folder (`D:\WKP\WKP-CHANNEL\scripts\`, `D:\WKP\WWD\scripts\`, create on first job), both writing-room passes logged in `logs\script-room.md`; .docx to `D:\WKP Reports\<Episode or Title>\` when final | .md + .docx |
| Art and Firefly prompts (graphic-design) | .md in the requesting venture's `reports\`; .docx to `D:\WKP Reports\<Name>\` when it is a printable pack | .md + .docx |
| QA reports | `D:\WKP\logs\qa\YYYY-MM-DD-<slug>.md` | .md |
| Monday brief / Saturday wrap | `D:\WKP Reports\Monday Brief\`, `D:\WKP Reports\Saturday Wrap\` (.md in `reports\monday\`, `reports\saturday\`) | .docx |
| Media map, music catalog, P index | `D:\WKP\data\assets\` (`media-map.md`, `music-catalog.md` + `.csv`, `p-drive-index.csv`) | .md / .csv |
| Org and system reports | .md `D:\WKP\reports\`; .docx `D:\WKP Reports\<Name>\` | |

## Conflict rulings (2026-11-19)

| # | Conflict | Winner | Why |
|---|---|---|---|
| 1 | Root CLAUDE.md "Deliverables: L:\" vs "D:\WKP Reports" | D:\WKP Reports | Zac 2026-10-05, newer and explicit. Root line corrected |
| 2 | Run sheet .docx named "Image Placement" (photo-pull skill) vs "Edit Run Sheet" | Edit Run Sheet | one-run-sheet lock 2026-10-17/18; skill line corrected |
| 3 | Second dated run sheet copies vs revise in place; root CLAUDE.md "every dated version inside" | Revise in place for working docs on one title (run sheets, packages); new dated file for recurring reports | wwd-run-sheet spec 2026-10-26 for run sheets; root CLAUDE.md 2026-10-05 for recurring reports (QA note N3) |
| 4 | `timeline-placements.md` as a second run sheet | Working list only | one run sheet rule 2026-10-17/18 |
| 5 | "Adobe defaults, Cross Dissolve" (photo-pull) vs half designed transitions | Designed transitions, Cross Dissolve 3 max | Zac 2026-10-14; skill line corrected |
| 6 | Trailer clips 4 s max, 30 s total (STANDARDS.md) vs 6 to 8 s, 12 max, no cap | 6 to 8 s, 12 max | Zac 2026-11-19; STANDARDS corrected |
| 7 | Shorts "5 to 7 per video" (WWD CLAUDE.md) vs 5 max (reviews) vs Opus 23 to 28 a week | 5 max for review shorts; FrostCast follows the 2026-11-11 cadence | newest per case; WWD CLAUDE.md line corrected |
| 8 | Week-folder rule vs type folders | Type folders for everything except the weekly social package | type-folder rules are newer (2026-10-05, 2026-10-19) |
| 9 | Upload package .md in two places | ONE .md in `WWD\reports\`; movie folder gets the .docx only | stops drift |
| 10 | Separate "Shorts Captions" doc | Merged into the package | Zac 2026-10-18; memory line corrected |
| 11 | WWD benches and music log only to `logs\wwd-director.md` | Both: director log AND `logs\agent-runs.md` row | root CLAUDE.md 2026-11-12 |
| 12 | Music copied to kit vs owned only | Pick from owned catalog, copy to `P:\WWD Kit\<Show>\Sounds\`, never move the original | both rules hold together |
| 13 | Audio cut .md only vs .docx rule | .md plus .docx | root .docx rule is the newer general rule |
| 14 | Intro length: "hook in 5 s" / ~15 s old briefs vs 6 s max | 6 s max sting | Zac 2026-11-19; music spec and reference corrected |
| 15 | Lessons path `memory\topics\lessons\` (AGENT-NETWORK) vs `memory\agents\` | `memory\agents\<agent>.md` | one place, created 2026-11-19; AGENT-NETWORK corrected |

## D:\WKP Reports type folders in use (keep these names)

In use: Asset Placement Run Sheets, WWD Upload Packages, WWD Shorts Copy, Music Prompts, FrostCast, Review Prep, Monday Brief, Ian Book Trailer, System Reset (created 2026-11-19), and one folder per Zac-named report type. Planned, created on first use: Saturday Wrap (and `reports\saturday\`), and `D:\WKP\WKP-CHANNEL\reports\`.
Near-duplicates found 2026-11-19 (left in place, nothing moved, new files follow the rule above): `Ian Book Trailer Draft 3` (new Ian files go to `Ian Book Trailer`), `Godzilla Minus Zero` (per-title folder, new WWD files go to their type folder), `WWD Social Captions` (new files go to `WWD Shorts Copy`).

## Drive mirror rule (Zac gave this command Wednesday 2026-11-18, it was never written down, recorded 2026-11-20)
ONLY WHEN ZAC ASKS (Zac 2026-11-20, it is not automatic and not a step of every review). When he asks, the finished upload package .docx, Shorts titles and captions .docx, and the finished Shorts videos with covers are COPIED (never moved) to `N:\My Drive\01 Warrior King Productions\WWD\Upload Packages\<Movie>\` with Shorts in a `shorts\` subfolder, The D:\WKP Reports and L: copies stay the source. Operational repo files never go to Drive (root CLAUDE.md rule stays). Copy with `cp -n` or robocopy, no overwrite of Zac's edits.
