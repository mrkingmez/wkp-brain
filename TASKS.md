TASKS.md — WKP Master Task List
One shared list, all ventures. Rule: when you start something new in any project, it gets added here. When a check-in happens, this file is what gets read.

Status options: Not Started / In Progress / Blocked / Done


🧹 ONE-TIME CLEANUP — Delete Drive Duplicates
(Every file below now exists in 2-3 places because Claude's Drive tools can only copy, never move/delete. Delete the "Old" column entries — the "New" column is the real one. One pass, then this section gets deleted from this file.)

File
🗑️ Delete (old location)
✅ Keep (new location)
Status
ME.md
Drive root
Warrior King Productions/ root
Not Started
projects.md
Drive root
Warrior King Productions/ root
Not Started
TASKS.md (this file — old version)
Drive root, Warrior King Productions/ root (previous version)
Warrior King Productions/ root (this version)
Not Started
WKP-Master-Command-Document
Drive root
guides/
Not Started
WKP_Cowork_Setup_Guide.docx
"Files from Claude" folder
guides/
Not Started
WKP-Home-Setup-Template (2 copies in "Files from Claude" + 1 in Drive root)
"Files from Claude" folder ×2, Drive root
guides/
Not Started
frostcast-audio-cut-SKILL.md (3 copies total)
Drive root, guides/
skills/
Not Started
voice bible appendix 1
Drive root
Shttered-Empire/
Not Started
Alpha Reader Feedback Form
Drive root
Shttered-Empire/
Not Started
Contact Information (Responses)
Drive root
Shttered-Empire/ (renamed "Alpha Reader Signups")
Not Started
TheUltimateGuide.pdf
Drive root
Shttered-Empire/
Not Started
Watershed-SOP-v3.md (2 old copies)
Drive root ×2
WhatIF/
Not Started
Watershed-Predictive-Model
Drive root
WhatIF/
Not Started
WarriorKingDesigns Listing Tracker
Drive root
ETSY/
Not Started
Production Company Business Plan Template
Drive root
Post Production/
Not Started
Winter Wolf Scheduler
Drive root
WWD/
Not Started


Leave alone (not part of this cleanup): WarriorKingDesigns - Etsy Ops folder (drag whole folder into ETSY/ yourself when ready — too large to copy file-by-file) · the Listing Tracker that already lives inside that Etsy Ops folder (different file, deal with it when you handle that folder) · winterwolf Den upload (staying put, shared with Matt) · rename Shttered-Empire → Shattered-Empire (typo fix, no tool for this either, manual rename)


❓ OPEN QUESTION
Cyber Security folder — created under Warrior King Productions/, but still waiting on: is this a real 8th venture (gets a CLAUDE.md + projects.md entry) or a personal reference folder (certs/resume, not something being actively built)?


🔴 Etsy Store (top priority)
Task
Deadline
Status
Notes
WKD Christian line digital resize/zip
—
Done
2026-09-01. 22/22 designs, 6 sizes each (8x10/5x7/11x14/16x20/A4/A3, 300 DPI JPG), zipped one-per-design at D:\04 New Warrior King Designs\_Print Exports\christian\. One source file ("Genesis Cosmic Light") was a truncated PNG, recovered — see logs\etsy-director.md 2026-09-01 entry.
Post this week's WKD digital batch
—
Not Started
Recommendation delivered 2026-09-01, unguided (8/20 traffic data is 12 days stale): lead with 6 of the newly-packaged Christian designs, 3 today + 3 Wed 9/3, within the shared 8/week cap (KP using 0 this week, shop not yet created). Still needs titles/tags/descriptions/pricing + AI disclosure sentence before listing.
Post next design batch (Fantasy/sci-fi or Military)
—
Not Started
Military and Landscape lines don't have digital (6-size JPG) exports yet — only the older 4-size PNG spec exists for a few designs. Needs the same resize/zip pass as Christian before it can post digitally.
Launch wall art line
—
Not Started
Expanding beyond puzzles

🟠 KDP Publishing — Math Mystery & Puzzle Books (ACTIVE-UNSCHEDULED, downgraded from priority 1b 9/1 — pivoting, no agent/schedule, do not surface in daily planning)
Task
Deadline
Status
Notes
Full market research (naming/description/pricing)
—
Done
Opus research pass 8/24 — see `KDP\Launch-Guide.md`. Name locked: "Math Case Files." Pricing locked: launch $10.99, never below $9.99. Full comp table + trademark check in the guide's appendix.
Build Launch Guide + Tracker + kdp-director agent
—
Done
`KDP\Launch-Guide.md` / `.docx`, `KDP\Tracker.csv`, `.claude\agents\kdp-director.md` all built 8/24. jarvis routing updated.
Run Genten Royalty hands-on with Zac
—
Not Started
Day 1 priority — confirms real page count/export format/option set, which every pricing and bundling number in the Launch Guide currently assumes from one 15-page sample
Run KDP Niche Finder (free BowesPaz tool)
—
Not Started
Pick 2-3 low-competition grade/theme combos before generating anything
Verify Genten's content-ownership/commercial-use terms
—
Not Started
Confirm generated content is actually clear to publish commercially, before publishing anything
Pick pen name / imprint for Math Case Files
—
Not Started
Single KDP account (zac@warriorkingproductions.com), multiple pen names — confirmed safe, no second account needed
Build cover template
—
Not Started
Needed before first submission
Generate + publish Book 1 (6-8 bundled cases)
—
Not Started
Not a single case — bundle for print-cost/royalty reasons, see Launch Guide Section 1
Start Sunday KDP data pull
—
Not Started
No API exists — manual dashboard pull every Sunday into `data\kdp-manual-YYYY-MM-DD.md` + `KDP\Tracker.csv`, once a title is live
Explore Shigai Royalty (murder-mystery Sudoku)
—
Not Started
Second product line on the same Elite account — scope after Genten's first batch

The Winter Wolf's Den / FrostCast
Task
Deadline
Status
Notes
Picture gather — Good Boy (2025) & The Whisper Man (2026 Netflix) | — | Done | 18 images each (poster + 17 stills) pulled from IMDb, saved to `L:\Winter Wolfs Den review show\Raw Footage\Mass recording 30 Aug\<movie>\`, resized to 1920x1080 PNGs in each `USE\` folder. Contain/fit rule only (no cropping, ever) — this superseded the old edge-to-edge cover-crop default from the EP1 pass, see `memory\topics\visual-media.md`. Built new skill `wwd-review-photo-pull` (wired into wwd-director) so future "record video on this movie X" requests run this whole pipeline unprompted — finds/creates the Raw Footage folder, pulls the IMDb set, filters duplicate poster art and off-topic cross-title contamination, resizes. Note: The Whisper Man's gallery was thin (new release, mostly character-poster key art) — flagged, not padded.
EP 106 transcript | — | Done | Transcript generated 2026-08-09, saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 106\Spider-man DOMINATES the Box Office  _ FrostCast Episode 106_transcript.txt` (1,406 lines, full 83-min episode). Speakers came back as Guest/Unknown [1]/[2]/[3] — voiceprints still aren't enrolled, so needs hand-mapping to Matt/Zac/Gabby before downstream use. Fixed a real bug along the way: pyannote's speaker-embedding step was crashing on a broken torchcodec install; `transcribe.py` now reads WAV clips directly instead of routing through torchcodec, permanent fix. Chapter timecodes pulled from the transcript and given to Zac in-session (not saved to a file yet).
EP 110 transcript, audio cut, and Matt email | — | Done | 2026-09-02. Transcript (1,650 lines, 92:58 runtime) saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 110\Gunn killed Lanterns _ FrostCast Episode 110_transcript.txt` — speakers still Guest/Unknown, voiceprints not enrolled. Audio cut saved to `L:\Winter Wolfs Den review show\Audio\podcast Frostcast audio files\FrostCast ep 110 2026-09-02.md` (~74:28 finished runtime, above the 55-70 min target — flagged in the doc rather than force-cutting more of the actual commentary). Full transcript emailed to Matt (mattkhourie32@gmail.com) from kingzpotus@gmail.com. **Pipeline change, Zac's call 2026-09-02:** audio cut + emailing Matt the transcript are now permanent steps 5 and 6 of the FrostCast Transcription Workflow in CLAUDE.md — run automatically every episode going forward, not just this one.
Week of 8/10 weekly build package | — | Done | `wwd-weekly-planner` run 2026-08-10. Priority call: Last House Tue (decay window, edited), Point Break Thu (evergreen debut, edit still open — due night of 8/11). Full package (social copy, 2 polls, short-form bank, growth notes, cold open check-in) saved to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\04 Upload Packages\WWD_Weekly_Package_2026-08-10.docx`. Higgsfield credits were at 0, so this week's 7 images shipped as Firefly prompts instead of generated art — see doc Section 5.
The Last House upload package | — | Done | Built from transcript by hand since `wwd-video-upload-package` skill isn't installed on this machine — title/description/tags/thumbnail concepts/pinned comment saved to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\04 Upload Packages\The Last House - Upload Package.txt`.
EP 103 upload package | — | Done | Built by hand from FROSTCAST.md format spec (`wwd-video-upload-package` skill still not installed on this machine). SEO title, 18-chapter description, backend tags, hashtags, thumbnail concept, 6 scored shorts candidates (4 elite ships, 2 held for re-cut), FB/IG posts w/ Firefly prompts, end screens/cards, posting schedule — saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 103\FrostCast Episode 103 - Upload Package.txt`. Reviewed by a general-purpose agent standing in for the unavailable devils-advocate agent type (verdict: SHIP WITH FIXES, 4 issues found and fixed — see logs\wwd-director.md 2026-08-20 entry). Open flags: shorts clips not yet cut, end-screen/card links are placeholders pending real channel data, shorts host attributions need audio confirmation before crediting Winter Wolf or KingZ by name (voiceprints still not enrolled). Devils-advocate agent gap queued as decision WWD-2026-08-20-01.
Cold open — Warden character designs | ~2026-09-25 (was ~mid-to-late Sept) | Blocked | Punted 3 more weeks, Zac's call 2026-09-04 (target now ~2026-09-25). Still blocked on Higgsfield credits (balance confirmed at 0, free plan, checked 2026-08-10) — cost analysis still pending before topping up. Nothing can generate — including weekly images — until credits are back.
Story Behind the Story — Fire in the Sky | 2026-10-01 | In Progress | Recording set for Sunday 2026-09-06 — B-Roll fully downloaded. Release date locked 2026-08-26.
Next FrostCast episode prep | Wed 9pm (weekly) | Not Started | News/trailers/books/games. This is EP111 (Wed 9/9) — EP110 already recorded/transcribed 2026-09-02.
FrostCast relaunch episode | — | Not Needed | Cut 2026-09-04 — Zac's call: no relaunch needed, schedule has had no gap. Premise was a stale assumption.
Fix Spotify show metadata | — | Not Started | Fix "Winters" typo, standardize episode titles. Holding 2026-09-04 pending the audio-only podcast relaunch task list below — Zac wants a deep dive before posting fixes live.
Build task list — bring back audio-only version of the podcast | — | Not Started | New 2026-09-04, Zac's call. Needs its own plan/scope before Spotify metadata fixes go live.
Decide new podcast host | — | Done | Decided 2026-09-04 — sticking with Spotify for Creators (free) for now.

WKP — "What If" Military History
Task
Deadline
Status
Notes
Alexander the Great episode
—
Not Started
3 branching timelines from his death in first battle
Continental Army M-16s episode
—
Not Started
Later in the pipeline

WKP Post-Production House
Task
Deadline
Status
Notes
Build service offerings/rate sheet
—
Not Started
Sound, video edit, motion graphics, animation
Research color grading tools
—
Not Started
Planned service addition

Novel — Shattered Empire (Book 1)
Task
Deadline
Status
Notes
Collect reader feedback
—
In Progress
Draft 2 out with readers
Third edit pass
—
Not Started
After feedback is in
World Bible update pass
—
Not Started
Lock in recent changes + character voice on page
Query letters to agents
—
Not Started
After third edit

Novel — Shattered Empire (Book 2)
Task
Deadline
Status
Notes
Planning
—
In Progress



Novel — Military Sci-Fi (untitled)
Task
Deadline
Status
Notes
Decide POV (1st vs 3rd person)
—
Not Started


Build World Bible from scratch
—
Not Started
History, worlds, characters, factions, ships, ranks

Investing Challenge ($50 → $60+)
Task
Deadline
Status
Notes
Build swing-trade scanner/alert tool
—
Not Started
Passive alerts, no manual checking
Review current watchlist
—
Not Started





Spark Capture (Android app)
Task
Deadline
Status
Notes
Repo scaffold applied
—
Done
Phase 1 — folders, Gradle config, interface stubs
Phase 2 — app shell (UI, note storage, settings)
—
Not Started
Vibe-codeable; do before wake-word SDK work
Decide wake-word engine
—
Not Started
OpenWakeWord (free/MVP) vs. Porcupine vs. Outspoken
Decide transcription approach
—
Not Started
On-device vs. cloud
Branding pass
—
Not Started
App name, package name, launcher icon are all placeholders


PAWS (hardware venture)
Task
Deadline
Status
Notes
Decide task source (Todoist / Microsoft To Do / Google Tasks / Notion / local file)
—
Not Started
Phase 0 — BLOCKS all firmware work. See PAWS-001 in decisions/DECISIONS.md
Locate the WKP wolf 3D model, drop into art/
—
Not Started
Phase 0
Confirm Elegoo Mars generation and build volume
—
Not Started
Phase 0 — see PAWS-003
Set realistic hours per week so the timeline means something
—
Not Started
Phase 0 — see PAWS-004
Create GitHub repo, push scaffold
—
Not Started
Phase 0
Order tools (see docs build guide, Tools section)
—
Not Started
Phase 0
Order Build 1 parts — TWO boards, not one
—
Not Started
Phase 0
Board boots, wifi connects, static sprite on screen
—
Not Started
Phase 1 — Taskagotchi
State machine written and tested on PC, no hardware
—
Not Started
Phase 1 — Taskagotchi
Task API call, parse JSON, map completions to stat changes
—
Not Started
Phase 1 — Taskagotchi
Port state machine to firmware, swap animations by state
—
Not Started
Phase 1 — Taskagotchi
Flash persistence, sleep and power management
—
Not Started
Phase 1 — Taskagotchi
Character art: 8 states, 3 frames each
—
Not Started
Phase 1 — Taskagotchi
Enclosure designed and printed
—
Not Started
Phase 1 — Taskagotchi
Photograph finished unit for the pitch deck
—
Not Started
Phase 1 — Taskagotchi
XIAO board boots, serves hardcoded JSON state
—
Not Started
Phase 2 — MAC
Web page polls endpoint, draws a face from the JSON
—
Not Started
Phase 2 — MAC
Servos: mood to pose mapping, easing, home on boot
—
Not Started
Phase 2 — MAC
Capacitors installed, brownout tested under full servo load
—
Not Started
Phase 2 — MAC
Software angle limits set BEFORE first animation loop
—
Not Started
Phase 2 — MAC
Camera face tracking
—
Not Started
Phase 2 — MAC
Pan and tilt bracket mounted, cable management
—
Not Started
Phase 2 — MAC
Photograph and film for content
—
Not Started
Phase 2 — MAC
Proposal letter
—
Not Started
Phase 3 — Investor materials
Pitch deck
—
Not Started
Phase 3 — Investor materials
Image prompts sent to Zac, images returned
—
Not Started
Phase 3 — Investor materials
Real prototype photos swapped in for renders
—
Not Started
Phase 3 — Investor materials
Teacher workflow defined
—
Not Started
Phase 4 — Education variant (ClassPaw)
Confirm zero student-facing data path
—
Not Started
Phase 4 — Education variant (ClassPaw)
Teacher interviews for real needs
—
Not Started
Phase 4 — Education variant (ClassPaw)
Variant spec written
—
Not Started
Phase 4 — Education variant (ClassPaw)


How to use this file
New task in any venture → add a row here, same turn it comes up.
Finished something → mark it Done (or just tell me — I'll update it).
Deadlines you don't have yet stay blank — fill in real dates as they get set, especially anything tied to a publisher or a launch.

