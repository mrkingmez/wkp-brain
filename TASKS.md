TASKS.md â€” WKP Master Task List
One shared list, all ventures. Rule: when you start something new in any project, it gets added here. When a check-in happens, this file is what gets read.

Status options: Not Started / In Progress / Blocked / Done


ðŸ§¹ ONE-TIME CLEANUP â€” Delete Drive Duplicates
(Every file below now exists in 2-3 places because Claude's Drive tools can only copy, never move/delete. Delete the "Old" column entries â€” the "New" column is the real one. One pass, then this section gets deleted from this file.)

File
ðŸ—‘ï¸ Delete (old location)
âœ… Keep (new location)
Status
ME.md
Drive root
Warrior King Productions/ root
Not Started
projects.md
Drive root
Warrior King Productions/ root
Not Started
TASKS.md (this file â€” old version)
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
"Files from Claude" folder Ã—2, Drive root
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
Drive root Ã—2
WKP-CHANNEL/
Not Started
Watershed-Predictive-Model
Drive root
WKP-CHANNEL/
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


Leave alone (not part of this cleanup): WarriorKingDesigns - Etsy Ops folder (drag whole folder into ETSY/ yourself when ready â€” too large to copy file-by-file) Â· the Listing Tracker that already lives inside that Etsy Ops folder (different file, deal with it when you handle that folder) Â· winterwolf Den upload (staying put, shared with Matt) Â· rename Shttered-Empire â†’ Shattered-Empire (typo fix, no tool for this either, manual rename)


â“ OPEN QUESTION
Cyber Security folder â€” created under Warrior King Productions/, but still waiting on: is this a real 8th venture (gets a CLAUDE.md + projects.md entry) or a personal reference folder (certs/resume, not something being actively built)?


## ðŸ—ï¸ Repository Build-Out Pass (all ventures) â€” added 2026-09-12
Zac's call 2026-09-12: get every venture that already has assets/work sitting outside a real repo (local downloads, or built in a Claude web/Cowork session) actually moved in and scaffolded. Do the physical build work, don't just plan it. Venture status labels (DORMANT/ACTIVE-UNSCHEDULED) are NOT being changed by this â€” Zac gave no preference on reclassifying the board when asked directly 2026-09-12, so repos get built but planning surfacing rules in root CLAUDE.md stay as-is until he says otherwise.
| Task | Deadline | Status | Notes |
|---|---|---|---|
| Identify "Rider's [or Ryder's] Room" venture/project | â€” | Not Started | Zac referenced building this out 2026-09-12 ("I have all the stuff, just need to sit down and put it in the repository") â€” name doesn't match anything in projects.md, memory, or any existing folder. Needs Zac to confirm what this is before a folder/repo gets created for it. |
| Build Investing repository from ready material | â€” | Not Started | Zac says he has everything for the trading/swing-scanner tool already (built in a Cowork/web session per his 2026-09-12 note) â€” just needs it moved into `D:\WKP\Investing\` and actually built. Investing is currently DORMANT (capture-only) but Zac asked directly, which the DORMANT rule allows acting on. |
| Inventory + build remaining Cowork/web-session repos | â€” | Not Started | Zac: "there's a few others we've done over in the web base/Cowork one" with everything downloaded, just needing the actual repo built. Needs Zac to list which ones (not captured yet â€” ask him directly next check-in). |

## WKP Company Formation (top-level, not a venture)
| Task | Deadline | Status | Notes |
|---|---|---|---|
| Research cheapest way to form the LLC | â€” | Done | 2026-09-14, Zac's ask, top-level (WKP itself, not a single venture). Real numbers pulled live, not guessed: GA Articles of Organization $110 one-time (state fee, identical online or by mail); GA Annual Registration $60/year starting the year after formation (Jan 1 to Apr 1 window); EIN always $0 direct from irs.gov (third-party sites charging $50 to $300 for this are the single most common new-LLC scam); Zac can serve as his own registered agent at $0 since he has a GA street address (Grovetown), versus $50 to $300/year for a commercial registered agent; Georgia has no LLC publication requirement (that only applies to corporations here), so no newspaper-notice cost either. Cheapest real path: DIY-file directly with GA Secretary of State in-state, skip formation services (LegalZoom/ZenBusiness etc. add a markup plus often a bundled paid registered-agent year) and skip Wyoming/Delaware/Nevada "cheap LLC state" offers, which actually cost MORE for him specifically since WKP operates in Georgia. Full breakdown delivered to Zac in chat. Next step (not started): Zac decides whether to file now, and whether this is WKP as one top-level entity or a structure with per-venture entities later, before anything gets filed. |

## Shared Infrastructure (not a venture â€” cross-venture tooling)
| Task | Deadline | Status | Notes |
|---|---|---|---|
| Build no-ai-slop skill + lock the writing rule | â€” | Done | 2026-09-14, Zac's call ("remember my writing rule no emdashes and nothing generic, lets run any thing going public goes through the no ai slop skill"). Generalizes the Shattered Empire "no em dashes" rule (was fiction-only) to everything public across every venture, plus a new "nothing generic" rule (no AI-tell phrases, no throat-clearing, sound like the actual people). Built `.claude\skills\no-ai-slop\` and locked it into root CLAUDE.md's standing rules. Ran it immediately against the two just-drafted, not-yet-aired Surfshark sponsor reads and the weekly social calendar â€” both had em dashes throughout (including in the POW/MIA post and Heat promo copy), now cleaned; both `.docx` pairs regenerated to match via a new `md_to_docx.py` utility in the skill's `scripts\` folder. See `memory\topics\writing.md`. |
| Spin up marketing subagents (copywriting, social-media, graphic-design, video-ugc) | â€” | Done | 2026-09-14, Zac's call ("spin them up they are in the _spec folder bring them to live and pass on their instructions"). Moved all 4 from `.claude\agents\_spec\` to `.claude\agents\`, status banners updated SPEC'Dâ†’LIVE. Triggered by marketing-director hand-building a Surfshark sponsor campaign + weekly social calendar itself because these were still dormant â€” that gap is now closed. marketing-director remains the only one who can task them (per each spec's "reports to marketing-director only" rule); venture directors still route marketing asks through marketing-director, not these directly. |
| Build nfl-data skill (nflverse) | â€” | Done | 2026-09-12. Shared data layer at `.claude\skills\nfl-data\` + cache `D:\WKP\data\nfl\`. Serves fantasy football (EPA pick'em tiebreaker, IDP matchup data for lineup optimizer) and an undecided sports-content venture (play-level angles) â€” data layer only, no scripts/calendar/naming for that venture per spec. Discovery-first design: filenames pulled live from `api.github.com/repos/nflverse/nflverse-data/releases`, never hardcoded. Confirmed 2026-09-12: all 6 target releases exist; `stats_team`/`stats_player`/`pfr_advstats` split into week/reg/regpost per-season files; `schedules`/`players` are single rolling multi-season files, not per-season; `player_stats` (no split) is a separate, deprecated-2025-08-01 release â€” never use it, use `stats_player`. `stats_team` confirmed carries `passing_epa`/`rushing_epa`/`receiving_epa`; `schedules` confirmed carries full betting lines (`spread_line`, `total_line`, moneylines). Required installing `pyarrow` on this machine to read parquet (now installed). Flag for the fantasy-football-data MFL/Sleeper ID bridge: nflverse's `players` release has `espn_id`/`gsis_id` (overlaps Sleeper) but no `mfl_id` â€” doesn't fully solve the bridge, only a secondary cross-check. |

## WKP Automation / Jarvis Build
| Task | Deadline | Status | Notes |
|---|---|---|---|
| Build Cowork Scheduled Task for daily queue check | â€” | Not Started | Reads calendar/sheet, executes what's due, runs during morning window |
| Set up Claude Code Routine against wkp-brain | â€” | Not Started | Cloud-side, runs with PC off, picks up .claude/skills and .claude/agents automatically since they're git-tracked |
| Decide connector list per Routine | â€” | Not Started | Connectors don't inherit from Cowork â€” attach Calendar/Drive/whatever each Routine needs explicitly |
| Set autonomy boundary | â€” | Not Started | Routines run with zero approval prompts â€” keep anything that posts live or spends money on Desktop tasks (permission mode on); Routines limited to draft/build/prep |
| Attach pending MCPs | â€” | Not Started | Zac has additional MCPs he wants connected (2026-09-12) â€” not yet specified which ones, ask him for the list. |
| Second-machine setup â€” split processing between two machines | â€” | In Progress | Zac wants a second machine running so work can be divvied up by compute/processing power (2026-09-12). LOCAL-PATHS.md is already structured per-machine (one `## MACHINE:` section per box) for exactly this. Cross-session messaging (SendMessage/ListAgents) already lets sessions on different machines talk to each other once both are set up â€” Tailscale guide built 2026-10-10 (`D:WKP ReportsTailscale Setup Guide`). Needs: second machine acquired/available, LOCAL-PATHS.md section added for it, Claude Code installed there. |
| Voice assistant â€” TTS/STT personal-assistant mode | â€” | Not Started | Zac wants voice output (ElevenLabs MCP already connected) and eventually a mode where Claude can proactively reach out with a question rather than only responding when spoken to (2026-09-12: "call me and ask me when you have a question"). Outbound calling isn't available in the current toolset â€” needs research into what's possible (e.g., ElevenLabs Conversational AI + a phone number) before this is buildable. |


ðŸ”´ Etsy Store (top priority)
Task
Deadline
Status
Notes
WKD Christian line digital resize/zip
â€”
Done
2026-09-01. 22/22 designs, 6 sizes each (8x10/5x7/11x14/16x20/A4/A3, 300 DPI JPG), zipped one-per-design at D:\04 New Warrior King Designs\_Print Exports\christian\. One source file ("Genesis Cosmic Light") was a truncated PNG, recovered â€” see logs\etsy-director.md 2026-09-01 entry.
Post this week's WKD digital batch
â€”
Not Started
2026-10-03 update: new `wkd-weekly-batch` skill run for real (first time), still unguided (newest data\ file is 44 days stale). Prepped 6 new candidates to current digital spec â€” Military (Arlington Autumn Salute, Apache Attack in Desert, Submarine Night Surfacing) and Landscape (Majestic Scottish Highlands, Autumn Forest Splendor, Tropical Waterfall Paradise) â€” per ETSY\CLAUDE.md's locked Active Plan (Military + Landscape lead). Cap counter unconfirmed (queued WKD-2026-10-03-02); sized to Mon/Wed 3+3=6 cadence rather than the full 8/week to leave headroom. Still needs titles/tags/descriptions/pricing + AI disclosure sentence before listing â€” the 2026-09-01 Christian batch (22 designs, never confirmed posted) is still available too and hasn't aged out.
Post next design batch (Fantasy/sci-fi or Military)
â€”
Not Started
Military and Landscape lines don't have digital (6-size JPG) exports yet â€” only the older 4-size PNG spec exists for a few designs. Needs the same resize/zip pass as Christian before it can post digitally. **Unblocked 2026-10-03** â€” new `wkd-weekly-batch` skill generates this as a standing weekly report (what to post, prep included), no longer gated behind per-instance permission. Run it to get this week's actual recommendation rather than reading this note as current.
Launch wall art line
â€”
Not Started
Expanding beyond puzzles

ðŸ”µ Kingdom Planners (MAIN EFFORT â€” digital planners, 6 of 7 products confirmed on disk, 0 listings)
Task
Deadline
Status
Notes
Create Etsy shop (Kingdom Planners name)
â€”
Blocked
2026-09-07 â€” Etsy showing a $29 one-time setup fee Zac doesn't have on hand. Gates only the shop-goes-live step. Business email is ready: kingdomplannerszk@gmail.com. NOT touched in the 2026-09-24 prep pass â€” spend decision stays Zac's.
Per-listing prep for 6 of 7 products (free, done 2026-09-24)
â€”
Done
etsy-director ran the full free-prep pass while Zac was off for the weekend: title + 13 tags + full tab-by-tab description for Debt Freedom Planner, PCS, Deployment, VA Tracker, Terminal Leave, and Road Trip (all checked against Etsy's confirmed-current 140-char title / 13-tag / 20-char-tag limits), anchor+sale pricing for all 6 plus the bundle, About section, shop-policy draft, and the AI-disclosure sentence/checklist. Full package: `D:\WKP Reports\Kingdom Planners Listing Prep\2026-09-24 - Kingdom Planners Listing Prep.docx` (moved 2026-10-05 into the new one-folder deliverables system, see root CLAUDE.md; `.md` source now lives at `Kingdom-Planners\reports\` in the repo). **Complete Budget System (the flagship 16-tab product) is blocked â€” its .xlsx file does not exist anywhere on disk**, confirmed by a full LOCAL-PATHS.md + C:/D:/E:/L: drive search; it was built in a past web-chat session and never downloaded out of that session's temp storage. Needs Zac to re-pull it from that chat (if still open) or rebuild it before it gets a listing pack, and before the Military Family bundle (needs all 6 military-relevant files zipped together) can be assembled. Listing photos still not done, see next row.
Listing photos / mockup screenshots (kp-prep skill)
â€”
Not Started
Per `kp-prep` skill: cards 1 (title card) and 6 (contents graphic) have all their real copy ready now (in the 2026-09-24 batch doc) but need the actual image built in Adobe Express, or routed to the graphic-design department â€” no image-generation tool was available in this session to produce them. Cards 2-5 need real screenshots of each working file, which per the skill's own rule has to be Zac opening each file by hand, not staged. Cards 7-8 are already-existing permanent shop assets, nothing further needed.
Resolve Etsy AI-disclosure question for KP
â€”
Done
2026-09-24. Etsy's own policy pages block automated fetch, so this is sourced from search/third-party citations, not a direct pull â€” flagged for a live logged-in-browser double-check before launch. Confirmed: no clean policy carve-out between "AI-generated art" and "AI-assisted tool," so KP discloses too, just with different wording than WKD. Locked sentence: "This planner was built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified before this file shipped. This is an original tool, not AI-generated artwork." Full detail in Kingdom-Planners\CLAUDE.md and the batch doc Section 11.
Recover or rebuild Complete Budget System file
â€”
Not Started
Flagship 16-tab product, file is genuinely gone (see row above). Blocks its own listing, its photo cards, and the Military Family bundle listing. Zac's action: check whether the original web-chat session that built it is still reachable to re-download, otherwise it needs to be rebuilt from scratch.
Run a real Google Sheets compatibility pass
â€”
Not Started
2026-09-24 formula-safety scan of all 6 confirmed files found none of the functions that typically break in Sheets (XLOOKUP, FILTER, UNIQUE, LET, SORT, SEQUENCE, LAMBDA, TEXTJOIN, IFS, SWITCH) â€” good sign, not a substitute for actually opening each file in Sheets, which still hasn't happened.

ðŸŸ  KDP Publishing â€” Math Mystery & Puzzle Books (ACTIVE-UNSCHEDULED, downgraded from priority 1b 9/1 â€” pivoting, no agent/schedule, do not surface in daily planning)
Task
Deadline
Status
Notes
Full market research (naming/description/pricing)
â€”
Done
Opus research pass 8/24 â€” see `KDP\Launch-Guide.md`. Name locked: "Math Case Files." Pricing locked: launch $10.99, never below $9.99. Full comp table + trademark check in the guide's appendix.
Build Launch Guide + Tracker + kdp-director agent
â€”
Done
`KDP\Launch-Guide.md` / `.docx`, `KDP\Tracker.csv`, `.claude\agents\kdp-director.md` all built 8/24. jarvis routing updated.
Run Genten Royalty hands-on with Zac
â€”
Not Started
Day 1 priority â€” confirms real page count/export format/option set, which every pricing and bundling number in the Launch Guide currently assumes from one 15-page sample
Run KDP Niche Finder (free BowesPaz tool)
â€”
Not Started
Pick 2-3 low-competition grade/theme combos before generating anything
Verify Genten's content-ownership/commercial-use terms
â€”
Not Started
Confirm generated content is actually clear to publish commercially, before publishing anything
Pick pen name / imprint for Math Case Files
â€”
Not Started
Single KDP account (zac@warriorkingproductions.com), multiple pen names â€” confirmed safe, no second account needed
Build cover template
â€”
Not Started
Needed before first submission
Generate + publish Book 1 (6-8 bundled cases)
â€”
Not Started
Not a single case â€” bundle for print-cost/royalty reasons, see Launch Guide Section 1
Start Sunday KDP data pull
â€”
Not Started
No API exists â€” manual dashboard pull every Sunday into `data\kdp-manual-YYYY-MM-DD.md` + `KDP\Tracker.csv`, once a title is live
Kindle Scribe write-on books: how-to + market check
â€”
Done (research only)
2026-10-15, Zac asked. Sold mainly as interactive hyperlinked PDFs (Etsy, Gumroad); readers send them to the Scribe and write on the page. Whether KDP itself takes a self-published write-on Kindle edition is unconfirmed (old KDP forum thread says print-replica is not supported on e-ink; one Scribe-only maze book is listed as a Kindle Edition). No sales data found, only Etsy listing counts and review counts. Next: Zac's call on a test title (Shigai mystery sudoku fits best), and testing on a real Scribe.
Explore Shigai Royalty (murder-mystery Sudoku)
â€”
Not Started
Second product line on the same Elite account â€” scope after Genten's first batch

The Winter Wolf's Den / FrostCast
Task
Deadline
Status
Notes
Picture gather â€” Good Boy (2025) & The Whisper Man (2026 Netflix) | â€” | Done | 18 images each (poster + 17 stills) pulled from IMDb, saved to `L:\Winter Wolfs Den review show\Raw Footage\Mass recording 30 Aug\<movie>\`, resized to 1920x1080 PNGs in each `USE\` folder. Contain/fit rule only (no cropping, ever) â€” this superseded the old edge-to-edge cover-crop default from the EP1 pass, see `memory\topics\visual-media.md`. Built new skill `wwd-review-photo-pull` (wired into wwd-director) so future "record video on this movie X" requests run this whole pipeline unprompted â€” finds/creates the Raw Footage folder, pulls the IMDb set, filters duplicate poster art and off-topic cross-title contamination, resizes. Note: The Whisper Man's gallery was thin (new release, mostly character-poster key art) â€” flagged, not padded.
Picture gather â€” Heat (1995) | â€” | Done | 2026-09-13, corrected 2026-09-14. Final set: 1 poster + 32 real stills (33 total) in `L:\Winter Wolfs Den review show\Raw Footage\Heat\USE\`. First pass (25 images) was TMDb backdrops/posters only â€” strong on De Niro/Pacino and action beats but had zero coverage of Natalie Portman (Lauren), Ashley Judd (Charlene Shiherlis), Diane Venora (Justine), or Dennis Haysbert (Breedan) â€” all major subplot characters. Zac caught it: "these are all people major to the story... pull ones that are not just cool but hit major beats." Added 8 more via IMDb's per-character filtered still-frame galleries (2 each for the 4 missing characters, incl. Lauren's suicide-attempt still and the Hanna/bus-stop scene). Skill `wwd-review-photo-pull` updated with new **Step 3.5** so future pulls check the full cast list and cover every character carrying a real subplot, not just the leads â€” see `memory\topics\visual-media.md`. **Step 8 (beat-matched pass) still PENDING** â€” no script/outline/beat sheet exists yet for a Heat episode.
EP 106 transcript | â€” | Done | Transcript generated 2026-08-09, saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 106\Spider-man DOMINATES the Box Office  _ FrostCast Episode 106_transcript.txt` (1,406 lines, full 83-min episode). Speakers came back as Guest/Unknown [1]/[2]/[3] â€” voiceprints still aren't enrolled, so needs hand-mapping to Matt/Zac/Gabby before downstream use. Fixed a real bug along the way: pyannote's speaker-embedding step was crashing on a broken torchcodec install; `transcribe.py` now reads WAV clips directly instead of routing through torchcodec, permanent fix. Chapter timecodes pulled from the transcript and given to Zac in-session (not saved to a file yet).
EP 110 transcript, audio cut, and Matt email | â€” | Done | 2026-09-02. Transcript (1,650 lines, 92:58 runtime) saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 110\Gunn killed Lanterns _ FrostCast Episode 110_transcript.txt` â€” speakers still Guest/Unknown, voiceprints not enrolled. Audio cut saved to `L:\Winter Wolfs Den review show\Audio\podcast Frostcast audio files\FrostCast ep 110 2026-09-02.md` (~74:28 finished runtime, above the 55-70 min target â€” flagged in the doc rather than force-cutting more of the actual commentary). Full transcript emailed to Matt (mattkhourie32@gmail.com) from kingzpotus@gmail.com. **Pipeline change, Zac's call 2026-09-02:** audio cut + emailing Matt the transcript are now permanent steps 5 and 6 of the FrostCast Transcription Workflow in CLAUDE.md â€” run automatically every episode going forward, not just this one.
Week of 8/10 weekly build package | â€” | Done | `wwd-weekly-planner` run 2026-08-10. Priority call: Last House Tue (decay window, edited), Point Break Thu (evergreen debut, edit still open â€” due night of 8/11). Full package (social copy, 2 polls, short-form bank, growth notes, cold open check-in) saved to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\04 Upload Packages\WWD_Weekly_Package_2026-08-10.docx`. Higgsfield credits were at 0, so this week's 7 images shipped as Firefly prompts instead of generated art â€” see doc Section 5.
The Whisper Man (2026 Netflix) review upload package | â€” | Done (needs re-trim) | 2026-09-06. Full wwd-review-pipeline run â€” export landed mid-session so audio + shorts got done too. All deliverables in `L:\Winter Wolfs Den review show\Raw Footage\Mass recording 30 Aug\The Whisper Man (2026 Netflix)\`: `The Whisper Man - Upload Package.docx` + `.md` (SEO title, description w/ QUICK ANSWERS, 14-line chapters, backend tags 476 chars python-verified, 5 high-volume hashtags, thumbnail, FB/IG posts, cards in MM:SS:frame, schedule, flags); `AUDIO\The Whisper Man.mp3` (192k, matches source); `shorts\` = 6 vertical clips (1080x1920, verified) + `shorts_manifest.txt`. **All 6 shorts are HOLD FOR RE-TRIM** â€” block-level Premiere timing, soft spoken opens, need manual in-point nudges; clip5 also needs a bleep ("piece of shit" ~21s); clips 4/5/6 under 30s = YT+FB only unless extended for IG. Garbles held: "Michelle Monaghan" spelled 3 ways, "Winter Wolfstein"/"Kingsley" in the cold open. Explicit on-air language flagged for the edit.
The Last House upload package | â€” | Done | Built from transcript by hand since `wwd-video-upload-package` skill isn't installed on this machine â€” title/description/tags/thumbnail concepts/pinned comment saved to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\04 Upload Packages\The Last House - Upload Package.txt` (+.docx/.md, 2026-09-24). **Closed out per Zac 2026-10-05** â€” no further action, moving on.
EP 103 upload package | â€” | Done | Built by hand from FROSTCAST.md format spec (`wwd-video-upload-package` skill still not installed on this machine). SEO title, 18-chapter description, backend tags, hashtags, thumbnail concept, 6 scored shorts candidates (4 elite ships, 2 held for re-cut), FB/IG posts w/ Firefly prompts, end screens/cards, posting schedule â€” saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 103\FrostCast Episode 103 - Upload Package.txt` (+.docx/.md, 2026-09-24). Reviewed by a general-purpose agent standing in for the unavailable devils-advocate agent type (verdict: SHIP WITH FIXES, 4 issues found and fixed â€” see logs\wwd-director.md 2026-08-20 entry). **Closed out per Zac 2026-10-05** â€” any remaining open flags (shorts re-cut, end-screen placeholders, host attribution) not being chased further, moving on.
Good Boy (2025) review | â€” | Done | Picture gather + upload package (title/description/tags/thumbnail/6 shorts candidates) completed 2026-08-31, docx/md retrofit 2026-09-24 â€” see `L:\Winter Wolfs Den review show\Raw Footage\Mass recording 30 Aug\Good Boy (2025)\`. **Closed out per Zac 2026-10-05** â€” no further action, moving on.
Cold open â€” Warden character designs | ~2026-09-25 (was ~mid-to-late Sept) | Blocked | Punted 3 more weeks, Zac's call 2026-09-04 (target now ~2026-09-25). Still blocked on Higgsfield credits (balance confirmed at 0, free plan, checked 2026-08-10) â€” cost analysis still pending before topping up. Nothing can generate â€” including weekly images â€” until credits are back.
T-2 (Terminator 2) review | â€” | Done | Released. Closed out per Zac 2026-09-14 â€” picture set, upload package (.docx+.md), and beat-matched B-roll (Step 8 model case, see `memory\topics\visual-media.md`) all already delivered pre-release.
Resident Evil review â€” recording date | 2026-09-21 (moved from original date) | Done | Moved to next Monday, Zac's call 2026-09-14 â€” Matt's travel plans changed after the original date was set. Whatever prep (script/B-roll) was targeting the old date now retargets 2026-09-21. **Done 2026-10-19: recorded, posted a while ago (Zac).**
Heat (1995) review â€” record + release | Was Fri 2026-09-18, slipped | Done | **POSTED 2026-10-06 (Zac confirmed).** All social posts and all 6 Shorts are posted/scheduled as of 2026-10-06 (Zac confirmed), so the Heat package is fully closed out. **Updated 2026-10-05:** recorded, but still in the edit â€” slipped past the locked 9/18 release because Zac's been sick, just getting back on his feet as of this update. No new release date set yet, don't assume one. Picture set already delivered (`Raw Footage\Heat\USE\`, 33 images) â€” see the Heat picture-gather entry above. Step 8 beat-matched pass still pending (needs a script/outline, which may exist by now â€” check before assuming it doesn't). Real next step once the edit's done: upload package, ready to build the moment Zac says the cut's locked. **Updated 2026-10-06:** Zac says the transcript is saved and asked for the upload pipeline. The episode is actually a "First Watch" format (KingZ makes Winter Wolf watch Heat, 35:25, 2 speakers), not a standard review. `wwd-review-pipeline` run: `Heat - Upload Package` (.md + .docx), `AUDIO\First Watch of Heat.mp3`, and 6 Shorts in `shorts\` (1 ready, 5 held for re-trim) all in `L:\Winter Wolfs Den review show\Raw Footage\Heat\`. Open flags for Zac and Winter Wolf: Winter Wolf says on air he fell asleep on Heat as a teen but also calls this a first watch, and no release date is set yet. Full list in package Section 12. **Re-confirmed 2026-10-19: Heat is up and posted, complete (Zac).**
Cold open â€” Higgsfield credit top-up cost (real numbers, checked 2026-09-14) | â€” | Not Started | Zac asked cost to fund from company money vs. sticking with Firefly. Current balance: 0 credits, free plan. **No one-time top-up packs are currently offered** (checked live â€” only recurring plans exist right now, despite Higgsfield's own tool description mentioning 500/1000/2000/4000 packs). Real options: (1) 3-Day Free Plus Trial â€” $0 today, 100 credits, MCP-only, auto-renews to $49/mo unless cancelled before day 3; (2) PLUS â€” $49/mo, or $39/mo billed annually ($468/yr), 1,000 credits/mo; (3) ULTRA â€” $129/mo, or $99/mo billed annually ($1,188/yr), 3,000 credits/mo. Recommendation: the free trial is the zero-risk way to test if Higgsfield's output is actually worth it before committing company money â€” set a reminder to cancel by day 3 if it's not a clear win. Firefly remains the free fallback already used for the Week of 8/10 package and stays viable if the trial/upgrade doesn't get greenlit. This is a spend decision â€” queued for Zac's call, not made here.
Next FrostCast episode prep | Wed 9pm (weekly) | Not Started | **2026-10-19, Zac: this week is EP117. EP112 and EP113 are over and done, dropped. The carry-forward topic list from EP112 is cleared, do not bring those six topics back.** Each week's prep comes from Matt's Tuesday list image per wwd-show-prep. **EP117 chain done 2026-10-22:** transcript (1:52:03, speakers still Guest/Unknown) and 39-line chapter file saved in `L:\Winter Wolfs Den review show\Frost-Cast\EP 117\`; audio cut (68:07 finished, 30 keeps) at `L:\Winter Wolfs Den review show\Audio\podcast Frostcast audio files\FrostCast ep 117 2026-10-22.md`; transcript sent to Matt on Messenger, confirmed "Sent" in the thread. Open for Zac: three flags at the bottom of the cut doc (crude analogy at 0:43:43, Doomsday hint at 0:35:37, "Alien 3" poll read).
Bring back the audio-only podcast (relaunch) | â€” | Not Started | Merged 2026-09-04 â€” this is the same initiative as the old "FrostCast relaunch episode / We're Back" task: WWD/CLAUDE.md notes the audio side has been dark ~18 months even though the video show never stopped. Needs a real deep-dive/plan before anything posts; may still end in a "We're Back" cross-post episode once scoped. Video-side relaunch is NOT needed (no gap there).
Fix Spotify show metadata | â€” | Not Started | Fix "Winters" typo, standardize episode titles. Holding 2026-09-04 pending the audio relaunch plan above â€” Zac wants a deep dive before posting fixes live.
Decide new podcast host | â€” | Done | Decided 2026-09-04 â€” sticking with Spotify for Creators (free) for now.
Wolf-character short series â€” concept + production plan | â€” | Not Started | Idea captured 2026-09-08. Short series built around a wolf character with an "animated but live-action feel." Two open questions before anything else: (1) WHAT is the series about â€” premise, format, episode length, tone, how it fits alongside FrostCast / Den Files / reviews. (2) HOW do we make it â€” the animated-live-action look (AI video gen e.g. Higgsfield, 2D/3D animation, hybrid comp, puppet/mocap) and the pipeline for it. Also decide whether this wolf is Winter Wolf (Matt's handle), the WKP wolf character (shared with PAWS, has a 3D model somewhere), the cold-open Warden, or a new character entirely â€” Zac's call, don't assume. Needs a scoping session with Zac.
Track "Remains" movie for review | 2027-02-14 | Not Started | Releases Valentine's Day 2027 â€” flag for trailer reaction / review pipeline closer to date.
Other Mommy (2026) review - placement report + transitions | Release Tue 2026-10-13 | Done | 2026-10-11. Recording tonight (Sun 10/11), release Tue 10/13, both on the WWD calendar. Photo set done: 15 PNGs in `L:\Winter Wolfs Den review show\Raw Footage\Other Mommy (2026)\USE\` (1 poster, 13 stills, 1 promo portrait, short of 18 because it is two days old). Originals deleted. **2026-10-12: placement report DONE, rebuilt on a real two-speaker transcript.** The Premiere .txt only covered the edit and dropped most of Winter Wolf's lines. Re-transcribed the raw 37:48 recording (`--num-speakers 2`), saved labeled KingZ/Winter Wolf as `Other Mommy _2026_ - Recap and Review_transcript.txt` in the movie folder. Edit timecode = raw minus 14:58. 16 placements, all 15 images used, transitions per premiere-transitions.md: `D:\WKP Reports\Review Image Placement\2026-10-12 - Other Mommy Image Placement.docx`, md at `WWD\reports\Other-Mommy-Image-Placement.md`, copy in `USE\timeline-placements.md`. No-image beats listed in the report (book cover and other-release posters can be pulled if Zac wants). **2026-10-13: final cut transcript came in, review pipeline run.** Upload package (.md + .docx), `AUDIO\Other Mommy.mp3`, and 6 shorts (1 ready, 5 held for re-trim) are all in the movie folder. Placement report retimed to the final cut and given fun poster transitions (melt on open, blood on close). Still open for Zac: confirm publish date (calendar said Tue 10/13), fill the card destinations, check garbles in package Section 12. **Done 2026-10-19: review posted, shorts scheduled and posted (Zac).**
Carrie (2026 Prime Video series) review - placement report + transitions | Release Thu 2026-10-15 | Done | 2026-10-12. Recording tonight (Mon 10/12, 7 to 9 PM ET assumed from the usual pattern), release Thu 10/15, both on the WWD calendar. TMDb tv/288673, premiered Oct 7 (8 eps, Flanagan). Photo set done: 18 PNGs in `L:\Winter Wolfs Den review show\Raw Footage\Carrie (2026 series)\USE\` (1 poster + 17 real series stills, full 18). Originals deleted, source list `D:\WKP\scratch\carrie_urls.txt`. **2026-10-12 later: Zac asked for more (about 40 min review), added 26 IMDb stills as USE 19 to 44, 44 total, all 1920x1080 RGBA.** **2026-10-13: edit transcript in (39:18), placement report DONE.** 44 placements, 43 of 44 images used (37.png skipped), blood bucket drop on the finale and blood ooze on the poster close: `D:\WKP Reports\Review Image Placement\2026-10-13 - Carrie Image Placement.docx`, md at `WWD\reports\Carrie-Image-Placement.md`, copy in `USE\timeline-placements.md`. **2026-10-14: fun pass added** (Zac: "where is the fun"): poster slam open, Wolfie Awards sticker, spoiler alarm, blood bucket with sound, Next Up card, 36-cue sound map, Suno prompts, Firefly sticker prompts, all in the same placement doc (docx regenerated in place). Still open: Zac generates the sticker and music, checks garbled lines at 01:53 and 35:53, checks a few guessed character IDs (31, 34, 35, 40) and the logo sting at the open. After the edit locks, run the review pipeline (upload package, audio, shorts). Release Thu 10/15. **2026-10-17: replaced by one timeline-order Edit Run Sheet** (`D:\WKP Reports\Review Image Placement\2026-10-17 - Carrie Edit Run Sheet.docx`, 52 stops, owned sounds only, no music beds, two stickers). Sticker kit built at `P:\WWD Kit\Stickers\`, Next Up card at `P:\WWD Kit\Cards\`. Open: confirm 32.png is Tina (stop 21). **2026-10-17 later: final render in (`Carrie 2026 Review best show of the year.mp4`, 39:29.8), review pipeline run.** Upload package (.md + .docx), `AUDIO\Carrie (2026).mp3`, 5 finished shorts + `Shorts Captions` md/docx with dated checklist, all in the movie folder. Open: real publish date (calendar still says 10/15; package assumes Sun 10/18, shorts Wed 10/21 to Sun 10/25 to clear the Other Mommy shorts). **Done 2026-10-19: full video and shorts posted and scheduled (Zac).**
Post Other Mommy (2026) shorts | 2026-10-16 | Done | **Rebuilt 2026-10-14: five finished clips, nothing held, no re-trim needed.** Clips and covers in `L:\Winter Wolfs Den review show\Raw Footage\Other Mommy (2026)\shorts\`, titles/descriptions/captions in `Other Mommy (2026) - Shorts Captions.md/.docx` (replaces the old manifest). Original note: cut 2026-10-13, clip 1 ready, 2 to 6 held (superseded). One per day starting the day after the full review publishes. Reminder set for 2026-10-16. **Done 2026-10-19: all shorts scheduled and posted (Zac).**
Rework WWD doc formats (Shorts Captions, Upload/Post Package, Image Placement report) | Sun 2026-10-18 | Done | 2026-10-18: formats decided and written into wwd-review-pipeline (SKILL.md + shorts-factory.md), wwd-review-photo-pull Step 8, and WWD/CLAUDE.md. First real use is Street Fighter, once Zac's cut is in. Original note 2026-10-17, Zac's call: talk through the format of all three before the next review runs. Use the Carrie versions as the examples. Calendar reminder set for Sun 10/18 10:00 AM on kingzpotus@gmail.com. Once a format is decided, update wwd-review-pipeline (SKILL.md + shorts-factory.md) and wwd-review-photo-pull so it sticks.
Street Fighter (2026) review - photos + placement report | Release TBD | Done | 2026-10-16. Movie opened 10/16, review filmed tonight (10/16). TMDb 1153576. Photo set done: 18 PNGs in `L:\Winter Wolfs Den review show\Raw Footage\Street Fighter 2026\USE\` (1 poster + 17 real stills, all 1920x1080 RGBA). Originals deleted, source list `D:\WKP\scratch\street_fighter_urls.txt`. Waiting on: review release date (calendar entry), edit transcript for the placement report. **2026-10-18: edit transcript in (20:37), Run Sheet Version 1 DONE in the new format** (timecode + PNG + spoken line per stop, video order): `D:\WKP Reports\Review Image Placement\2026-10-18 - Street Fighter Edit Run Sheet.docx`, md at `WWD\reports\Street-Fighter-Edit-Run-Sheet.md`, copy in `USE\`. 13 pictures added from the transcript (USE 19 to 31, 31 total). **New section right after the header: 14 numbered video-game-feel suggestions (V1 to V14), none built.** Zac picks, then Claude builds the chosen ones as Python kit pieces and issues Version 2. Recommended five: V1 rounds, V2 versus screen, V3 health bars, V5 combo counter, V8 continue countdown. **2026-10-18 later: Zac picked V1, V2, V3, V5, V8, V10. Built** with `scripts\make_arcade_kit.py` into `P:\WWD Kit\Street Fighter\` (rounds, versus, health-bar tags and hit clips, combo counter, Continue cards for Crystal Lake and Clayface, fireball). **Run Sheet Version 2:** `D:\WKP Reports\Review Image Placement\2026-10-18 - Street Fighter Edit Run Sheet v2.docx`. Next Up is Crystal Lake (series, SEASON 1 REVIEW) then Clayface; spoken line at 20:25 still says Clayface, Zac to decide. Still open: release date, then run the review pipeline after the edit locks. **2026-10-19 later: edit locked, export rendering. Upload package v1 DONE** (built from the older two-speaker transcript, final.txt had one speaker label): `D:\WKP Reports\WWD Upload Packages\Street Fighter Upload Package\2026-10-19 - Street Fighter Upload Package.docx`, md at `WWD\reports\Street-Fighter-Upload-Package.md`, copies in the movie folder. Chapter times are DRAFT (0 to 5 s drift vs the final cut). Background job `D:\WKP\scratch\sf_export_watch.ps1` waits for the export, then makes a 2-speaker transcript for the re-time. Still to do after the export lands: re-time chapters, ffprobe header, AUDIO mp3, up to 5 finished shorts (copy for 5 is already in Section 7). Zac decides: Clayface vs Crystal Lake on the end card, release date, card links. Pictures rule 2026-10-19: no picture twice, 7 s max, solo cams only a few. **Street Fighter package FINAL 2026-10-19 9:30 PM:** chapters re-timed from the final export (20:46), AUDIO mp3 and 5 finished shorts built (`Raw Footage\Street Fighter 2026\shorts\`), docx in `D:\WKP Reports\WWD Upload Packages\Street Fighter Upload Package\`. Open for Zac: Clayface vs Crystal Lake end card, card links, release date, check the shorts. **Done 2026-10-22 (Zac): full review and all 5 shorts posted, Facebook included.**
Crystal Lake (Peacock series, all 8 eps) review | Release TBD | Done | 2026-10-19, Zac: all 8 episodes dropped, review recorded last night (Sun 10/18). Next: photo pull, then edit transcript, then run sheet and upload package. Street Fighter's Next Up card says Crystal Lake, SEASON 1 REVIEW. A 15-second intro script was drafted but Zac used part of it, no more work needed on it. **2026-10-20, mass record layout (Zac): both shows were recorded in one session. Folder `L:\Winter Wolfs Den review show\Raw Footage\mass record crystal LAke Vision Quest\` holds the raw `Untitled recording.mp4`, the King-Z and Winter Wolf StreamYard webcam files, and one subfolder per show with its transcript. Speaker 1 = Winter Wolf, Speaker 2 = KingZ. Crystal Lake goes first, kept straight-forward (Friday the 13th franchise). DONE: 59 pictures in `Crystal Lake\USE\` (IMDb per-actor stills plus callback posters), kit at `P:\WWD Kit\Crystal Lake\` (Spoiler Alert, That Was Weird, Weird Good, Next Up - Vision Quest), timeline-order Edit Run Sheet at `D:\WKP Reports\Review Image Placement\2026-10-20 - Crystal Lake Edit Run Sheet.docx`, md at `WWD\reports\Crystal-Lake-Edit-Run-Sheet.md`. 68 stops, 58 different pictures, no hold over 7 s, 3 CAM stops. Open for Zac: second That Was Weird stamp is optional; run the review pipeline after the edit locks.** **2026-10-20 later: opening scare (Zac): 19.0 s, starts at 0:01, girl in a canoe, the show poster erupts from the lake and drags her under, she just disappears. Option 1 BUILT: `P:\WWD Kit\Crystal Lake\Opening - Lake Scare (Option 1).mov` (stylized, owned sounds, script `make_cl_opening.py`). Option 2 (realistic, Firefly plates) waiting on Zac generating 5 plates, prompts in `D:\WKP Reports\Crystal Lake OpeningÂ‚6-10-20 - Crystal Lake Opening Firefly Prompts.docx`. Run sheet needs a re-time (+19 s) and a swap for stop 2 (poster PNG 1 is now in the opener).** **2026-10-20 night: Option 2 BUILT from Zac's 5 Firefly plates** (`P:\WWD Kit\Crystal Lake\Opening - Lake Scare (Option 2 Firefly).mov`, 19.0 s, script `make_cl_opening_firefly.py`). Poster erupts at 9.15 s, covers the girl, hard cut to the empty canoe at 12.0 s. Plates are in `Crystal Lake\opening pates\`. **2026-10-21: final cut in, review pipeline DONE.** Upload package (.md + .docx, shorts merged in): `D:\WKP Reports\WWD Upload Packages\Crystal Lake Upload Package\2026-10-21 - Crystal Lake Upload Package.docx`, md at `WWD\reports\Crystal-Lake-Upload-Package.md`, copies in the movie folder. `AUDIO\Crystal Lake.mp3` (35:43.6), 5 finished shorts + covers in `shorts\`. Public copy went through copywriting, social-media, no-ai-slop via marketing-director. Open for Zac: pick title (primary or alt), fill 2 card destinations, check the AI-footage and Suno disclosure at upload, set the gory label on Short 2, post date. Flags in package Section 12 (Kingsley garble in the audio at 0:23, Vinson spelled two ways on air). **Done 2026-10-22 (Zac): full review and all 5 shorts posted, Facebook included.**
Post Crystal Lake (2026) shorts | 2026-10-24 | Done | 2026-10-21: 5 finished clips in `L:\Winter Wolfs Den review show\Raw Footage\mass record crystal LAke Vision Quest\Crystal Lake\shorts\`, copy and posting windows in the Upload Package Sections 7 and 11. Post only after the full review is live, first short 24 to 48 hours after, then one every 1 to 2 days. Publish date not set, move this deadline when it is. Listen-check Shorts 3, 4, 5 for the speaker first. **Done 2026-10-22 (Zac): full review and all 5 shorts posted, Facebook included.**
Vision Quest ep 1 + 2 review | Release 2026-10-24 | Done | 2026-10-19, Zac: recorded episodes 1 and 2 last night (Sun 10/18). Next: photo pull and calendar entry, then transcript. **2026-10-20: tech-y cut for the AI and robot angle. DONE: 66 pictures in `Vision Quest ep 1 and 2\USE\`, kit at `P:\WWD Kit\Vision Quest\` (System Boot opener, Spoiler Alert, five AI Tags for EDITH, FRIDAY, JARVIS, DUM-E and U, three Wrong Name Counters for Winter Wolf's request: Kevin, David, Dave Spader), Edit Run Sheet at `D:\WKP Reports\Review Image Placement\2026-10-20 - Vision Quest Edit Run Sheet.docx`, md at `WWD\reports\Vision-Quest-Edit-Run-Sheet.md`. 76 stops, 62 different pictures, 3 CAM stops. Open for Zac: transcript opens with two hook takes and chatter to about 01:55 (cut first), the episode schedule lines at 21:12 are stale after Oct 20, no end card yet (tell me what comes next).** **2026-10-23: v1 was too much (76 stops), rebuilt as v2 at Zac's call: 38 stops, 25 pictures, 10 stickers, 3 solo cams, fun beats kept. `D:\WKP Reports\Review Image Placement\2026-10-23 - Vision Quest Edit Run Sheet v2.docx`, md updated in place. v1 docx is still there from 10-20, ignore it.** **2026-10-23 later: v3 run sheet (new Firefly-based opener `Opener - Firefly (MP4).mp4`, Clayface end card, ProRes freezes on Zac's machine so use MP4). Final cut in, review pipeline DONE.** Upload package (.md + .docx): `D:\WKP Reports\WWD Upload Packages\Vision Quest Upload Package\2026-10-23 - Vision Quest Upload Package.docx`, md at `WWD\reports\Vision-Quest-Upload-Package.md`, copies in the movie folder. `AUDIO\Vision Quest Ep 1 and 2.mp3`, 5 finished shorts + covers in `shorts\`. The finished video landed in `Raw Footage\Street Fighter 2026\` (Premiere default), not moved. Open for Zac: pick title (primary or alt), fill 2 card destinations, confirm the Clayface end card and opener are in the export, stale release-date lines at 19:34 to 21:10, post date. **Done 2026-10-23 (Zac): video uploaded and scheduled for 2026-10-24, social posts and shorts scheduled.**
Post Vision Quest (eps 1 + 2) shorts | 2026-10-26 | Done | 2026-10-23: 5 finished clips in `L:\Winter Wolfs Den review show\Raw Footage\mass record crystal LAke Vision Quest\Vision Quest ep 1 and 2\shorts\`, copy and posting windows in the Upload Package Sections 7 and 11. Post only after the full review is live, first short 24 to 48 hours after, then one every 1 to 2 days. The Ultron short (clip2) is a spoiler for the end of episode 2, post it last, 72+ hours after the full video. Publish date not set, move this deadline when it is. Reminder set for 2026-10-26. **Done 2026-10-23 (Zac): all 5 shorts scheduled. The 10-26 calendar reminder is no longer needed.**
Mass record: Clayface + Vision Quest eps 3 & 4 | Sat 2026-10-24 | Not Started | 2026-10-23, Zac: both recorded tomorrow in one session. Same layout as the Crystal Lake / Vision Quest mass record (one folder, one subfolder and USE and P:\WWD Kit folder per show, Speaker 1 = Winter Wolf). After recording: photo pull for both, transcripts, run sheets, review pipeline once each edit locks. Vision Quest eps 1 and 2 end card already says Clayface next, eps 3 and 4 is the follow-up.
WWD short: Top 5 Halloween movies that will scare you | Before 2026-10-31 | In Progress | 2026-10-19, Zac's ask. BUILT: 53s vertical short, all captions and sounds in, only Zac's voice recording is left. Docx guide at `D:\WKP Reports\Halloween Top 5\`. Trailer clips not added (no verified links, download needs Zac's OK). Files in `L:\Winter Wolfs Den review show\Raw Footage\Halloween Top 5\`. See that folder's build notes.
Instagram data for WWD via Composio (like Facebook) | â€” | Done (first pull) | 2026-10-19, Zac: VidIQ is not connected to Instagram, pull IG numbers through the Composio Instagram connection the same way Facebook is pulled. First pull saved: `data\instagram-wwd-2026-10-19.md` (68 followers, 70 likes on last 30 posts, no views available under 1,000 followers).
eBay: best profit margin products, US shipping only | â€” | In Progress | 2026-10-19, Zac: this is what is next for eBay. Find the best margin products and show him the list. US-based shipping only. Ranked shortlist of 5 product types delivered (assumed costs, nothing verified): `D:\WKP Reports\eBay Margin Picks\2026-10-19 - eBay Margin Picks.docx`. Real products need Doba trial (spend, Zac yes) plus Terapeak sold data.
eBay refresh token + live check (home desktop) | Tonight 2026-10-19 6:30 PM ET | Not Started | 2026-10-19, Zac at work on laptop, did the RuName form (WKP Commerce, privacy doc on Google Docs, scopes sell.inventory/sell.fulfillment/sell.account if picked) but not the swap. At 6:30 PM on the home desktop: OAuth sign-in link, Agree, copy address, run `ebay-dropship\tools\get_refresh_token.py` (never paste code or token in chat). CLAUDE: ask Zac about this at 6:30 PM, then verify EBAY_REFRESH_TOKEN is set and run a live seller-account test. Also still waiting on: Doba trial yes/no (spend), Terapeak or sold numbers, confirm scopes were ticked. Calendar reminder set 6:30 PM (popups 6:20 and 6:30). Privacy text: `ebay-dropship\reports\privacy-policy-text.md`.
Post Street Fighter (2026) shorts | 2026-10-22 | Done | 2026-10-19: 5 finished clips in `L:\Winter Wolfs Den review show\Raw Footage\Street Fighter 2026\shorts\` plus copy in the Upload Package Section 7 (docx in `D:\WKP Reports\WWD Upload Packages\Street Fighter Upload Package\`). Post only after the full review is live, 24 to 48 hours after, then one every 1 to 2 days. Release date not set yet. Calendar reminder 10/22 10:00 AM. **Done 2026-10-22 (Zac): full review and all 5 shorts posted, Facebook included.**
"Together" (2025) review recording | Sat 2026-10-31 7:00 PM ET | Not Started | Punted 2026-10-15, Zac's call, from Sun 10/18. Calendar event on the Winter Wolf's Den calendar moved to Sat 10/31 7 to 9 PM. Watch it with Matt first. Halloween night, so confirm Matt is free.
Review intake flow built into wwd-review-photo-pull | â€” | Done | 2026-10-11, Zac's call. "We are doing a review on X" now runs calendar entries, photo pull, resize, delete originals, then a transcript-driven placement report with transitions. Transition list from Adobe's Help Center saved at `.claude\skills\wwd-review-photo-pull\premiere-transitions.md`. wwd-director routing updated (it has no calendar tool, so the main session adds calendar events).
Shorts factory (Part 2) installed into wwd-review-pipeline | â€” | Done | 2026-10-14, Zac's call ("the shorts look like they were just cut up, no other build to it"). New `shorts-factory.md` in the skill folder plus `scripts\build_short.py` and bundled Poppins fonts. Five clips max, all finished, floor 7, no HOLD FOR RE-TRIM, silence-detection cut points, burned-in captions, timed hook text, cover PNG plus one-frame prepend, per-platform captions doc. SKILL.md Sections 5 to 7 now point to it. Tested end to end on an Other Mommy window (scratch only, nothing real overwritten), two bugs found and fixed in testing. Local only, NOT yet committed or pushed. **Other Mommy rebuilt same day (2026-10-14, Zac's call):** 5 finished clips + covers + `Shorts Captions` md/docx in `shorts\`, old cuts archived in `shorts\_superseded_2026-10-14\`, upload package Section 7/11/12 and docx updated. Added `word_times.py` and `check_clip.py` (local Whisper word timing and edge verification). **Open:** Good Boy and Whisper Man held clips are still the old cuts, rebuild if Zac wants.
Retrofit older WWD output docs to .docx | â€” | Done | 2026-09-24, weekend handoff work. T-2 was already fixed 2026-09-12. Retrofitted the three remaining `.txt`-only packages this pass: The Last House, FrostCast EP103, and Good Boy (2025) â€” each now has a matching `.md` (content unchanged, reformatted to real markdown headers) and `.docx` alongside the original `.txt`, same folder. No content was altered beyond markdown formatting.
Connect thewinterwolfsden@gmail.com to Composio | â€” | Not Started | Not currently connected anywhere â€” checked 2026-09-11. Existing Gmail connections are kingzpotus@gmail.com (native), zachary.d.king4@gmail.com and kingdomplannerszk@gmail.com (Composio). Needed to read/manage the show's own inbox.
Surfshark sponsor read â€” FrostCast EP111 + reusable insert | Wed 2026-09-16 (EP111 recording) | In Progress | Built 2026-09-14 by marketing-director, cleared by `clearance` twice (initial pass + re-check after the CTA rewrite). **Finalized 2026-09-14 pm** â€” real deal terms confirmed from Zac + Surfshark's approval emails: rev-share affiliate (VPN 40%, Antivirus 60%, Adblock 60%), VPN is the flagship read, corrected tracking link `https://get.surfshark.net/aff_c?offer_id=926&aff_id=47475`, no discount code exists (link-based tracking only â€” both scripts rewritten to say "link's in the description," code placeholder removed), $100 net / ~5 conversion payout threshold, 90-day cookie window (Zac's figure, not independently verified). Fix routed through `copywriting` (live department, not hand-written). Saved to `L:\Winter Wolfs Den review show\Sponsors\Surfshark\Surfshark-Sponsor-Reads-2026-09-14.md` / `.docx`. STILL NEEDS: (1) confirm "one subscription covers every device" still matches Surfshark's current plan terms â€” VERIFY BEFORE AIR, (2) Zac/Matt sign-off on disclosure wording, (3) link posted in EP111 description AND pinned comment when it goes live, (4) email affiliates@surfshark.com once the read airs, (5) attorney check on whether written disclosure must sit next to the link in the description/pinned comment (FTC question, flagged by clearance pass 2, unresolved). Backlog, not this week: Antivirus/Adblock pay 60% vs VPN's 40%, worth a future insert. **`no-ai-slop` pass 2026-09-14 (run by Jarvis, standing gate as of today):** em dashes throughout, including inside spoken script lines, cleaned; docx regenerated. Same file paths, edited in place.
Week of 9/14 social calendar (FrostCast EP111, Heat review, Surfshark launch, Constitution Day, POW/MIA Recognition Day) | Runs through 2026-09-20 | In Progress | Full post-by-post plan built 2026-09-14 by marketing-director â€” platform/day/time/copy for every post, plus short-form ideas list. **Finalized 2026-09-14 pm**, fix routed through `social-media` (live department): Heat release day locked to **Friday 9/18, confirmed** (Thursday-flex language removed); POW/MIA post rewritten per Zac's direction â€” kept entirely about the POW/MIA service members, no reference to his own service, echoes his "until they all come home" sentiment without attributing it to him by name. Saved to `L:\Winter Wolfs Den review show\WWD Social\WWD_Weekly_Social_Calendar_2026-09-14.md` / `.docx` (moved 2026-09-15 out of the per-week `04 Upload Packages` folder into a new dedicated `WWD Social` folder). **Reversed 2026-09-16 â€” Zac doesn't like the split-folder look, wants everything back to one per-week folder matching `2026-08-10 Week of Aug 10\`'s structure; see WWD/CLAUDE.md Working Notes for the new locked rule.** These 9/14 files stay put (fix is going-forward only, Zac's call) but every week's build after this one saves social copy into that week's own `05 Social Copy` folder, not a standalone top-level one. Still unguided on hard engagement numbers â€” no WWD file exists in `D:\WKP\data\`; times adapted from the established stagger convention (YouTube 11:00 AM ET, IG +45 min, FB +90 min) confirmed in prior upload packages. Remaining open flags: fill episode-specific promo copy after EP111/Heat are actually recorded; route the Surfshark announcement-post badge graphic to `graphic-design` (live department now) if Zac wants one before Tuesday, otherwise text-only. Zac must approve/post everything â€” nothing here has been published, drafts only. **`no-ai-slop` pass 2026-09-14 (run by Jarvis, standing gate as of today):** em dashes throughout, including the Constitution Day post, the POW/MIA post, and the Heat promo copy, cleaned; POW/MIA wording preserved exactly (only the dash removed); docx regenerated. Same file paths, edited in place.
Department spin-up â€” copywriting, social-media, graphic-design, video-ugc | â€” | Done | 2026-09-14, Zac's call. All four moved out of `.claude\agents\_spec\` into `.claude\agents\`, status LIVE. First real use same day: copywriting fixed the Surfshark sponsor-read CTA, social-media fixed the weekly calendar's Heat date and POW/MIA copy. marketing-director routes department-shaped work to them going forward instead of hand-writing it.
Transcript delivery to Matt switched from email to Facebook Messenger | â€” | Done | 2026-09-16, Zac's call. Tested via `claude-in-chrome` browser automation against Zac's own logged-in Facebook session (not the Composio Facebook API connection, which can only send a message to someone with an existing Page conversation thread and can only attach a public URL, not a local file â€” confirmed dead end for file delivery). Sent EP111's transcript (`Spider-man cancelled BEFORE Rings of Power__ _ FrostCast Episode 111_transcript.txt`, 154 KB) as a direct file upload into Matt Khourie's personal Messenger thread; Zac confirmed it came through. Zac then had email retired entirely for this step rather than run both channels. FrostCast Transcription Workflow step 6 in root CLAUDE.md rewritten to describe the Messenger browser-upload steps in place of the old Gmail send. See `memory\topics\transcription.md` for the full technical path (why the API route fails, why the UI upload works).

WKP â€” "What If" Military History
Task
Deadline
Status
Notes
Alexander the Great episode
â€”
Not Started
3 branching timelines from his death in first battle
Continental Army M-16s episode
â€”
Not Started
Later in the pipeline

WKP Post-Production House
Task
Deadline
Status
Notes
Build service offerings/rate sheet
â€”
Not Started
Sound, video edit, motion graphics, animation
Research color grading tools
â€”
Not Started
Planned service addition

Novel â€” Shattered Empire (Book 1)
Task
Deadline
Status
Notes
Collect reader feedback
â€”
In Progress
Draft 2 out with readers
Third edit pass
â€”
Not Started
After feedback is in
World Bible update pass
â€”
Not Started
Lock in recent changes + character voice on page. **Blocked on Zac 2026-10-05** â€” he's consolidating/verifying the canon docs himself first (found real duplication + stale copies across 3 backup locations on Drive while an agent got ahead of him and prematurely tried to pick a "current" copy, see logs\DECISIONS.md SE-2026-09-24-01, reopened). Plan: Zac downloads his trusted Drive folder to L:\ once he's sorted it â€” not there yet as of this note. **Superseded 2026-10-06:** Zac confirmed `D:\The Shaterred Empire Series` is the settled canon set (see row below and LOCAL-PATHS.md), so the L:\ plan is dead and the hold is lifted for files in that folder. Still do not pick a "current" copy of any canon doc beyond what LOCAL-PATHS.md says. The voice bible now lives inside the Story Guide, which Zac is revising himself right now, so leave the Story Guide alone until he says it's done.
Confirm canon set location (D:\The Shaterred Empire Series)
â€”
Done
2026-10-06, answered by Zac. Settled canon set, replaces L:\ plan and Drive copies. `REwrites` = draft 1 (archive). Manuscript .docx/.epub/.pdf are the same book in three formats. Voice bible now lives inside `The_Patience_of_the_Dark_Story_Guide v2.docx` (10/5/2026), which Zac is reading/revising now. Old `Master_Voice_Bible.docx` (9/2025) and `voice_bible_performance` PDF sit in `Editing\`, treat as old. Newest Aether Stone Magic System is in `Editing\` (10/4/2026). Old Character Annex/Prompt Master copies also sit in `Edited folder_\`. Folder layout in LOCAL-PATHS.md.
Query letters to agents
â€”
Not Started
After third edit
Research: flipped heart condition (situs inversus / dextrocardia)
â€”
Done (research only)
2026-10-20, Zac via Jarvis. Brief at D:\WKP\research\books\shattered-empire\2026-10-20 flipped heart dextrocardia situs inversus.md. Next: Zac answers which character, which book, which version (healthy mirror, Kartagener cough, heterotaxy), and whether White healing magic can sense or fix it. Log in Shattered-Empire\logs\director.md.

Novel â€” Shattered Empire (Book 2)
Task
Deadline
Status
Notes
Planning
â€”
In Progress



Novel â€” Military Sci-Fi (untitled)
Task
Deadline
Status
Notes
Confirm Stellar Dominion file set (D:\Stellar Dominion)
â€”
Done
2026-10-06, answered by Zac. Stellar Dominion is the working name of the military sci-fi novel (SCI-FI Novel\CLAUDE.md and projects.md updated). Markups are in `Scan documents\` (Markup_Capture.docx is the transcription), NOT yet applied to the base docs. `Series Documents\` is for the finalized story/world-building docs, empty because those are not done ("a long way to go"). Venture stays DORMANT per root CLAUDE.md, no promotion.
Apply 9/20 markups to the six Stellar Dominion base docs
â€”
Not Started
Added 2026-10-06. Source of the edits: `D:\Stellar Dominion\Scan documents\` (merged MARKUP PDFs) plus `Stellar_Dominion_Markup_Capture.docx`. Two PNGs in `Claude outputs\` held handwriting that did not read, resolved by Zac 2026-10-06: `unreadable_word.png` = "resources", `unreadable_word_2.png` = "squadron". Dormant venture, so only start when Zac asks.
Decide POV (1st vs 3rd person)
â€”
Not Started


Build World Bible from scratch
â€”
Not Started
History, worlds, characters, factions, ships, ranks

Investing Challenge ($50 â†’ $60+)
Task
Deadline
Status
Notes
Build swing-trade scanner/alert tool
â€”
Not Started
Passive alerts, no manual checking
Review current watchlist
â€”
Not Started





Spark Capture (Android app)
Task
Deadline
Status
Notes
Repo scaffold applied
â€”
Done
Phase 1 â€” folders, Gradle config, interface stubs
Phase 2 â€” app shell (UI, note storage, settings)
â€”
Not Started
Vibe-codeable; do before wake-word SDK work. First coding session planned 2026-09-05 â€” Zac's call 2026-09-04, build guide delivered to `D:\WKP-Guides\Spark Capture - Build Guide.md/.docx` (Android Studio setup through first run, then Note/Room/note-list-screen as session 1 scope).
Decide wake-word engine
â€”
Not Started
OpenWakeWord (free/MVP) vs. Porcupine vs. Outspoken
Decide transcription approach
â€”
Not Started
On-device vs. cloud
Branding pass
â€”
Not Started
App name, package name, launcher icon are all placeholders


PAWS (hardware venture)
Task
Deadline
Status
Notes
Decide task source (Todoist / Microsoft To Do / Google Tasks / Notion / local file)
â€”
Not Started
Phase 0 â€” BLOCKS all firmware work. See PAWS-001 in decisions/DECISIONS.md
Locate the WKP wolf 3D model, drop into art/
â€”
Not Started
Phase 0
Confirm Elegoo Mars generation and build volume
â€”
Not Started
Phase 0 â€” see PAWS-003
Set realistic hours per week so the timeline means something
â€”
Not Started
Phase 0 â€” see PAWS-004
Create GitHub repo, push scaffold
â€”
Not Started
Phase 0
Order tools (see docs build guide, Tools section)
â€”
Not Started
Phase 0
Order Build 1 parts â€” TWO boards, not one
â€”
Not Started
Phase 0
Board boots, wifi connects, static sprite on screen
â€”
Not Started
Phase 1 â€” Taskagotchi
State machine written and tested on PC, no hardware
â€”
Done
2026-10-15. D:\WKP\PAWS\sim\ (double-click "Run Scout.bat"). 7 tests pass. Mock data stands in for PAWS-001. Hardware purchase paused by Zac (cost), PAWS-008 still open.
Task API call, parse JSON, map completions to stat changes
â€”
Not Started
Phase 1 â€” Taskagotchi
Port state machine to firmware, swap animations by state
â€”
Not Started
Phase 1 â€” Taskagotchi
Flash persistence, sleep and power management
â€”
Not Started
Phase 1 â€” Taskagotchi
Character art: 8 states, 3 frames each
â€”
Not Started
Phase 1 â€” Taskagotchi
Enclosure designed and printed
â€”
Not Started
Phase 1 â€” Taskagotchi
Photograph finished unit for the pitch deck
â€”
Not Started
Phase 1 â€” Taskagotchi
XIAO board boots, serves hardcoded JSON state
â€”
Not Started
Phase 2 â€” MAC
Web page polls endpoint, draws a face from the JSON
â€”
Not Started
Phase 2 â€” MAC
Servos: mood to pose mapping, easing, home on boot
â€”
Not Started
Phase 2 â€” MAC
Capacitors installed, brownout tested under full servo load
â€”
Not Started
Phase 2 â€” MAC
Software angle limits set BEFORE first animation loop
â€”
Not Started
Phase 2 â€” MAC
Camera face tracking
â€”
Not Started
Phase 2 â€” MAC
Pan and tilt bracket mounted, cable management
â€”
Not Started
Phase 2 â€” MAC
Photograph and film for content
â€”
Not Started
Phase 2 â€” MAC
Proposal letter
â€”
Not Started
Phase 3 â€” Investor materials
Pitch deck
â€”
Not Started
Phase 3 â€” Investor materials
Image prompts sent to Zac, images returned
â€”
Not Started
Phase 3 â€” Investor materials
Real prototype photos swapped in for renders
â€”
Not Started
Phase 3 â€” Investor materials
Teacher workflow defined
â€”
Not Started
Phase 4 â€” Education variant (ClassPaw)
Confirm zero student-facing data path
â€”
Not Started
Phase 4 â€” Education variant (ClassPaw)
Teacher interviews for real needs
â€”
Not Started
Phase 4 â€” Education variant (ClassPaw)
Variant spec written
â€”
Not Started
Phase 4 â€” Education variant (ClassPaw)


Personal / Admin (non-WKP)
Task
Deadline
Status
Notes
Log Saturday 9/12 package-delivery mileage (~149 mi)
â€”
Not Started
Zac's package delivery job â€” quick reminder captured 2026-09-13, log the actual odometer/trip number wherever mileage gets tracked for this job.
King Debt Planner (personal debt payoff plan)
â€”
In Progress
2026-10-15, Zac's ask. Built from the KP Debt Freedom Planner, expanded to 30 debts, 96 months, real paydays (retirement 1st, county every other Thu from 11/5). File: D:\WKP Reports\King Debt Planner\2026-10-15 - King Debt Planner.xlsx (personal data, never in the repo). Waiting on Zac: living costs (food, gas, insurance), APRs for OneMain and Verizon, confirm photo reads (loan APRs, PayPal min 119 vs 251), due days for utilities, cell, Verizon. **v2 2026-10-16:** added Monthly View (bills, insurance/health, subscriptions, living, debts grouped by month), every-other-week payments (Upstart 1 and 2, OneMain), car insurance, TRICARE, BENEFEDS, Foresters, Mutual of Omaha, SBA, IRS, unnamed $216.74 payment. File `2026-10-16 - King Debt Planner.xlsx`. Nov leftover only $278.66 before food and gas. Confirmed later 10/16: Upstart 1 $527.18 on county paydays, Upstart 2 $144.50 every other week from Oct 26, car insurance $220 x2, $216.74 = Eldorado timeshare, Netflix 27th. Weekend delivery pay added (avg $196/weekend, Yes/No switch, tax set-aside %): debt-free Aug 2029, no short months. Still open: car insurance days, OneMain next date, Verizon/IRS rates, confirm photo APRs. **Update 2026-10-16:** food $300, gas $300, Netflix $19.98, Mazda 12.99%, OneMain 17.59%, PayPal normal min $119, cell due 12th, Simple Bill and Verizon due mid-month. Result: Nov short $341, Mar 2027 short $124, debt-free Mar 2030 (Avalanche), interest about $82K.

Fantasy Football (personal, off the venture board) â€” added 2026-10-15
Task
Deadline
Status
Notes
Week 6 pick sheet + lineup
Thu 2026-10-15 8:15 PM ET
Done (Zac submits by hand)
Doc at D:\Documents\Pickups 2026\Week 6\Pickups 2026 - Week 6.docx. 14 NFL picks logged to tracker\predictions.csv (model source). College picks and the card .xls are NOT in the tracker.
Backfill tracker Weeks 2 to 5
â€”
Not Started
predictions.csv holds Week 1 (12 rows) and Week 6 (14 rows) only. Model picks for Weeks 2, 3, 5 exist in the pick docs; Week 4 has no record. Logged after kickoff would break the tracker's integrity rule, so needs Zac's call on a labelled backfill.
Add Next Gen Stats to nfl-data
â€”
Done
2026-10-15. nflverse release nextgen_stats (passing/receiving/rushing), data through week 5.
Build ff-simulator (coach tendencies, game sim, lineup optimizer)
â€”
In Progress
Started 2026-10-15, Zac's call. Skill at .claude\skills\ff-simulator\. Coach model backtested (small real edge over league average), full simulation backtested, Week 6 run produced. Needs: tuning from backtest, head-to-head opponent model, pick'em ATS/total model, gambler friend's source (Zac sends 2026-10-16), DFS salary-cap mode.
Build ff-play-sim (play-by-play simulator: defense, coach, injury, weather, field, coach head-to-head, NGS)
—
In Progress
Started 2026-10-22, Zac's call. Skill at .claude\skills\ff-play-sim\ (read-only, current ff-simulator untouched). Phase 1 engine + defense + coach layers built and backtested on 269 games (2025 wk5-18, 2026 wk3-6): spread width matches the market (stretch 1.5), margin MAE 9.73 vs market 9.57, no information beyond the closing line (coef +0.18, t 0.9). Scoring still ~1.3 pts per team light (totals bias -2.1 per game). **2026-10-22 later: Phase 2 done.** Player layer + QB layer + injury file wired in; whole-slate run for Week 7 compared with the old sim (`data\ff-play-sim\roster_compare_2026_wk7.csv`). Player backtest: play sim best at QB (MAE 7.70 vs 8.32 plain average), level at K, trails old sim at RB/WR/TE; blended weights QB 0.9, K 0.5, RB 0.15, WR 0.2, TE 0.2. Signal tests: scheme data helps completion odds only (-2.2% log-loss), weather adds nothing at play level but wind >= 15 mph takes about 2 pts off the closing total, coach head-to-head has no edge. **2026-10-22 later still: defenders (IDP) built into the play sim and backtested.** No defender method beats a plain recent average at the player-week level (play sim DL/LB/DB MAE 1.85/2.47/2.27 vs average 1.71/2.23/2.05, old sim ties the average), so IDP stays on the old sim or the average; the play sim defenders are for what-if questions. Still open: NGS ratings, scheme/wind layers, 1.3 pts per team scoring gap, using participation and PFR defense data.
Full-week simulation report + DFS tools
2026-10-15
Done (Week 6)
Zac's ask. full_week.py (box scores, winners, 5 lineups, DK/FD points), power_rating.py (EPA rating tested against market: no edge), dfs_optimize.py (ready, needs the DK/FD salary CSV Zac downloads). Report at D:\WKP Reports\Week 6 Full Simulation\. Open: salary files, FA bids (Zac places, cannot guarantee a win). Zac's call 2026-10-15: model on the head coach only, no coordinator/play-caller data, since the head coach owns the decision.
Gambler friend's FanDuel lineup method
2026-10-16
Blocked
Zac gives the source tomorrow; add as extra features to ff-simulator.
Confirm taxi activation rule (Matthew Golden)
2026-10-15
Not Started
Superseded 2026-10-15: Zac signed Golden from the practice squad to the active roster on a 3-year contract, so he is active for Week 6 (sim 127.8 avg with him). Zac also bid on two low-cost FAs (a safety and a DE), may land in 2 days, so Week 7 not Week 6; evaluate names when he has them.

How to use this file
New task in any venture â†’ add a row here, same turn it comes up.
Finished something â†’ mark it Done (or just tell me â€” I'll update it).
Deadlines you don't have yet stay blank â€” fill in real dates as they get set, especially anything tied to a publisher or a launch.


eBay Dropship (working name WKP Commerce) â€” Phase 0, scaffold built 2026-10-10
Task
Deadline
Status
Notes
Scaffold built (agents, skills, data, tools, tests) | â€” | Done | 2026-10-10. See ebay-dropship\CLAUDE.md. pricing.py tests pass (9 checks); ebay_api.py dry-run check: inventory/orders OK, auth/browse clean SKIP (no keys).
Confirm venture name | â€” | Not Started | EBAY-002 in ebay-dropship\decisions-queue.md. Placeholder WKP Commerce.
Zac setup checklist (seller account, business policies, developer keyset, env vars, dedicated card, notifications, GitHub connected) | â€” | Not Started | Full list in EBAY-DROPSHIP-BUILD.md section 7.
Populate data\fee-table.md from eBay's current fee page | â€” | Not Started | pricing.py refuses to run until filled and dated.
Verify eBay API endpoint paths/scopes in ebay_api.py against developer docs | â€” | Not Started | Written from knowledge, doc pages were not machine-readable at build time.
Run ebay-director Phase 0 kickoff, then answer "Where do we go?" (EBAY-001) | â€” | Not Started | Researcher scheduled task is created only after the category pick.
Cold open shot list + Firefly swap | â€” | Blocked | 2026-10-10 Zac: draft 1 is built from the wrong script, he is finding the right files himself. Do not work this until he hands them over. Draft 1 (wrong source) was: Source `WWD\reports\Cold-Open-Shot-List.md`, docx in `D:\WKP Reports\Cold Open Shot List\`. Built from "Hey all you warden.docx" (Big Trouble version). Blockers on Zac: confirm script base, Warden design brief, Winter Wolf Express look, who appears in shots 1 and 7. Then Claude writes Firefly prompts.
