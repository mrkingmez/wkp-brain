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
Post next design batch
—
Not Started
Fantasy/sci-fi, Christian, or military line
Launch wall art line
—
Not Started
Expanding beyond puzzles

🟠 KDP Publishing — Math Mystery & Puzzle Books (priority 1b, set 8/24)
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
EP 106 transcript | — | Done | Transcript generated 2026-08-09, saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 106\Spider-man DOMINATES the Box Office  _ FrostCast Episode 106_transcript.txt` (1,406 lines, full 83-min episode). Speakers came back as Guest/Unknown [1]/[2]/[3] — voiceprints still aren't enrolled, so needs hand-mapping to Matt/Zac/Gabby before downstream use. Fixed a real bug along the way: pyannote's speaker-embedding step was crashing on a broken torchcodec install; `transcribe.py` now reads WAV clips directly instead of routing through torchcodec, permanent fix. Chapter timecodes pulled from the transcript and given to Zac in-session (not saved to a file yet).
Week of 8/10 weekly build package | — | Done | `wwd-weekly-planner` run 2026-08-10. Priority call: Last House Tue (decay window, edited), Point Break Thu (evergreen debut, edit still open — due night of 8/11). Full package (social copy, 2 polls, short-form bank, growth notes, cold open check-in) saved to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\04 Upload Packages\WWD_Weekly_Package_2026-08-10.docx`. Higgsfield credits were at 0, so this week's 7 images shipped as Firefly prompts instead of generated art — see doc Section 5.
The Last House upload package | — | Done | Built from transcript by hand since `wwd-video-upload-package` skill isn't installed on this machine — title/description/tags/thumbnail concepts/pinned comment saved to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\04 Upload Packages\The Last House - Upload Package.txt`.
EP 103 upload package | — | Done | Built by hand from FROSTCAST.md format spec (`wwd-video-upload-package` skill still not installed on this machine). SEO title, 18-chapter description, backend tags, hashtags, thumbnail concept, 6 scored shorts candidates (4 elite ships, 2 held for re-cut), FB/IG posts w/ Firefly prompts, end screens/cards, posting schedule — saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 103\FrostCast Episode 103 - Upload Package.txt`. Reviewed by a general-purpose agent standing in for the unavailable devils-advocate agent type (verdict: SHIP WITH FIXES, 4 issues found and fixed — see logs\wwd-director.md 2026-08-20 entry). Open flags: shorts clips not yet cut, end-screen/card links are placeholders pending real channel data, shorts host attributions need audio confirmation before crediting Winter Wolf or KingZ by name (voiceprints still not enrolled). Devils-advocate agent gap queued as decision WWD-2026-08-20-01.
Cold open — Warden character designs | — | Blocked | Blocked on Higgsfield credits (balance confirmed at 0, free plan, checked 2026-08-10). Zac needs to run a cost analysis before topping up. Nothing can generate — including this week's weekly images — until credits are back.
Story Behind the Story — Fire in the Sky
2026-10-01
Not Started
First episode of new series. Release date locked 2026-08-26.
Next FrostCast episode prep
Wed 9pm (weekly)
Not Started
News/trailers/books/games
FrostCast relaunch episode
—
Not Started
"We're Back" ep, cross-post YouTube + new audio feed same day
Fix Spotify show metadata
—
Not Started
Fix "Winters" typo, standardize episode titles
Decide new podcast host
—
Not Started
Spotify for Creators (free) vs. RSS.com/Buzzsprout (paid, auto multi-platform)

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





How to use this file
New task in any venture → add a row here, same turn it comes up.
Finished something → mark it Done (or just tell me — I'll update it).
Deadlines you don't have yet stay blank — fill in real dates as they get set, especially anything tied to a publisher or a launch.

