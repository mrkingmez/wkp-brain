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


## 🏗️ Repository Build-Out Pass (all ventures) — added 2026-09-12
Zac's call 2026-09-12: get every venture that already has assets/work sitting outside a real repo (local downloads, or built in a Claude web/Cowork session) actually moved in and scaffolded. Do the physical build work, don't just plan it. Venture status labels (DORMANT/ACTIVE-UNSCHEDULED) are NOT being changed by this — Zac gave no preference on reclassifying the board when asked directly 2026-09-12, so repos get built but planning surfacing rules in root CLAUDE.md stay as-is until he says otherwise.
| Task | Deadline | Status | Notes |
|---|---|---|---|
| Identify "Rider's [or Ryder's] Room" venture/project | — | Not Started | Zac referenced building this out 2026-09-12 ("I have all the stuff, just need to sit down and put it in the repository") — name doesn't match anything in projects.md, memory, or any existing folder. Needs Zac to confirm what this is before a folder/repo gets created for it. |
| Build Investing repository from ready material | — | Not Started | Zac says he has everything for the trading/swing-scanner tool already (built in a Cowork/web session per his 2026-09-12 note) — just needs it moved into `D:\WKP\Investing\` and actually built. Investing is currently DORMANT (capture-only) but Zac asked directly, which the DORMANT rule allows acting on. |
| Inventory + build remaining Cowork/web-session repos | — | Not Started | Zac: "there's a few others we've done over in the web base/Cowork one" with everything downloaded, just needing the actual repo built. Needs Zac to list which ones (not captured yet — ask him directly next check-in). |

## WKP Company Formation (top-level, not a venture)
| Task | Deadline | Status | Notes |
|---|---|---|---|
| Research cheapest way to form the LLC | — | Done | 2026-09-14, Zac's ask, top-level (WKP itself, not a single venture). Real numbers pulled live, not guessed: GA Articles of Organization $110 one-time (state fee, identical online or by mail); GA Annual Registration $60/year starting the year after formation (Jan 1 to Apr 1 window); EIN always $0 direct from irs.gov (third-party sites charging $50 to $300 for this are the single most common new-LLC scam); Zac can serve as his own registered agent at $0 since he has a GA street address (Grovetown), versus $50 to $300/year for a commercial registered agent; Georgia has no LLC publication requirement (that only applies to corporations here), so no newspaper-notice cost either. Cheapest real path: DIY-file directly with GA Secretary of State in-state, skip formation services (LegalZoom/ZenBusiness etc. add a markup plus often a bundled paid registered-agent year) and skip Wyoming/Delaware/Nevada "cheap LLC state" offers, which actually cost MORE for him specifically since WKP operates in Georgia. Full breakdown delivered to Zac in chat. Next step (not started): Zac decides whether to file now, and whether this is WKP as one top-level entity or a structure with per-venture entities later, before anything gets filed. |

## Shared Infrastructure (not a venture — cross-venture tooling)
| Task | Deadline | Status | Notes |
|---|---|---|---|
| Build no-ai-slop skill + lock the writing rule | — | Done | 2026-09-14, Zac's call ("remember my writing rule no emdashes and nothing generic, lets run any thing going public goes through the no ai slop skill"). Generalizes the Shattered Empire "no em dashes" rule (was fiction-only) to everything public across every venture, plus a new "nothing generic" rule (no AI-tell phrases, no throat-clearing, sound like the actual people). Built `.claude\skills\no-ai-slop\` and locked it into root CLAUDE.md's standing rules. Ran it immediately against the two just-drafted, not-yet-aired Surfshark sponsor reads and the weekly social calendar — both had em dashes throughout (including in the POW/MIA post and Heat promo copy), now cleaned; both `.docx` pairs regenerated to match via a new `md_to_docx.py` utility in the skill's `scripts\` folder. See `memory\topics\writing.md`. |
| Spin up marketing subagents (copywriting, social-media, graphic-design, video-ugc) | — | Done | 2026-09-14, Zac's call ("spin them up they are in the _spec folder bring them to live and pass on their instructions"). Moved all 4 from `.claude\agents\_spec\` to `.claude\agents\`, status banners updated SPEC'D→LIVE. Triggered by marketing-director hand-building a Surfshark sponsor campaign + weekly social calendar itself because these were still dormant — that gap is now closed. marketing-director remains the only one who can task them (per each spec's "reports to marketing-director only" rule); venture directors still route marketing asks through marketing-director, not these directly. |
| Build nfl-data skill (nflverse) | — | Done | 2026-09-12. Shared data layer at `.claude\skills\nfl-data\` + cache `D:\WKP\data\nfl\`. Serves fantasy football (EPA pick'em tiebreaker, IDP matchup data for lineup optimizer) and an undecided sports-content venture (play-level angles) — data layer only, no scripts/calendar/naming for that venture per spec. Discovery-first design: filenames pulled live from `api.github.com/repos/nflverse/nflverse-data/releases`, never hardcoded. Confirmed 2026-09-12: all 6 target releases exist; `stats_team`/`stats_player`/`pfr_advstats` split into week/reg/regpost per-season files; `schedules`/`players` are single rolling multi-season files, not per-season; `player_stats` (no split) is a separate, deprecated-2025-08-01 release — never use it, use `stats_player`. `stats_team` confirmed carries `passing_epa`/`rushing_epa`/`receiving_epa`; `schedules` confirmed carries full betting lines (`spread_line`, `total_line`, moneylines). Required installing `pyarrow` on this machine to read parquet (now installed). Flag for the fantasy-football-data MFL/Sleeper ID bridge: nflverse's `players` release has `espn_id`/`gsis_id` (overlaps Sleeper) but no `mfl_id` — doesn't fully solve the bridge, only a secondary cross-check. |

## WKP Automation / Jarvis Build
| Task | Deadline | Status | Notes |
|---|---|---|---|
| Build Cowork Scheduled Task for daily queue check | — | Not Started | Reads calendar/sheet, executes what's due, runs during morning window |
| Set up Claude Code Routine against wkp-brain | — | Not Started | Cloud-side, runs with PC off, picks up .claude/skills and .claude/agents automatically since they're git-tracked |
| Decide connector list per Routine | — | Not Started | Connectors don't inherit from Cowork — attach Calendar/Drive/whatever each Routine needs explicitly |
| Set autonomy boundary | — | Not Started | Routines run with zero approval prompts — keep anything that posts live or spends money on Desktop tasks (permission mode on); Routines limited to draft/build/prep |
| Attach pending MCPs | — | Not Started | Zac has additional MCPs he wants connected (2026-09-12) — not yet specified which ones, ask him for the list. |
| Second-machine setup — split processing between two machines | — | Not Started | Zac wants a second machine running so work can be divvied up by compute/processing power (2026-09-12). LOCAL-PATHS.md is already structured per-machine (one `## MACHINE:` section per box) for exactly this. Cross-session messaging (SendMessage/ListAgents) already lets sessions on different machines talk to each other once both are set up — needs: second machine acquired/available, LOCAL-PATHS.md section added for it, Claude Code installed there. |
| Voice assistant — TTS/STT personal-assistant mode | — | Not Started | Zac wants voice output (ElevenLabs MCP already connected) and eventually a mode where Claude can proactively reach out with a question rather than only responding when spoken to (2026-09-12: "call me and ask me when you have a question"). Outbound calling isn't available in the current toolset — needs research into what's possible (e.g., ElevenLabs Conversational AI + a phone number) before this is buildable. |


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

🔵 Kingdom Planners (MAIN EFFORT — digital planners, 7 products finished, 0 listings)
Task
Deadline
Status
Notes
Create Etsy shop (Kingdom Planners name)
—
Blocked
2026-09-07 — Etsy showing a $29 one-time setup fee Zac doesn't have on hand. Gates only the shop-goes-live step. Business email is ready: kingdomplannerszk@gmail.com.
Per-listing prep for all 7 products (free, do now)
—
Not Started
Titles + 13 tags + descriptions each, listing photos/mockup screenshots, individual pricing for the 5 unpriced products, Military Family bundle price, About + shop-policy copy. All doable with no money down so launch is paste-and-go once the $29 is available.
Resolve Etsy AI-disclosure question for KP
—
Not Started
These are original tools built with AI assistance, not AI-generated content like WKD art. Confirm the actual Etsy policy language before listing.

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
Picture gather — Heat (1995) | — | Done | 2026-09-13, corrected 2026-09-14. Final set: 1 poster + 32 real stills (33 total) in `L:\Winter Wolfs Den review show\Raw Footage\Heat\USE\`. First pass (25 images) was TMDb backdrops/posters only — strong on De Niro/Pacino and action beats but had zero coverage of Natalie Portman (Lauren), Ashley Judd (Charlene Shiherlis), Diane Venora (Justine), or Dennis Haysbert (Breedan) — all major subplot characters. Zac caught it: "these are all people major to the story... pull ones that are not just cool but hit major beats." Added 8 more via IMDb's per-character filtered still-frame galleries (2 each for the 4 missing characters, incl. Lauren's suicide-attempt still and the Hanna/bus-stop scene). Skill `wwd-review-photo-pull` updated with new **Step 3.5** so future pulls check the full cast list and cover every character carrying a real subplot, not just the leads — see `memory\topics\visual-media.md`. **Step 8 (beat-matched pass) still PENDING** — no script/outline/beat sheet exists yet for a Heat episode.
EP 106 transcript | — | Done | Transcript generated 2026-08-09, saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 106\Spider-man DOMINATES the Box Office  _ FrostCast Episode 106_transcript.txt` (1,406 lines, full 83-min episode). Speakers came back as Guest/Unknown [1]/[2]/[3] — voiceprints still aren't enrolled, so needs hand-mapping to Matt/Zac/Gabby before downstream use. Fixed a real bug along the way: pyannote's speaker-embedding step was crashing on a broken torchcodec install; `transcribe.py` now reads WAV clips directly instead of routing through torchcodec, permanent fix. Chapter timecodes pulled from the transcript and given to Zac in-session (not saved to a file yet).
EP 110 transcript, audio cut, and Matt email | — | Done | 2026-09-02. Transcript (1,650 lines, 92:58 runtime) saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 110\Gunn killed Lanterns _ FrostCast Episode 110_transcript.txt` — speakers still Guest/Unknown, voiceprints not enrolled. Audio cut saved to `L:\Winter Wolfs Den review show\Audio\podcast Frostcast audio files\FrostCast ep 110 2026-09-02.md` (~74:28 finished runtime, above the 55-70 min target — flagged in the doc rather than force-cutting more of the actual commentary). Full transcript emailed to Matt (mattkhourie32@gmail.com) from kingzpotus@gmail.com. **Pipeline change, Zac's call 2026-09-02:** audio cut + emailing Matt the transcript are now permanent steps 5 and 6 of the FrostCast Transcription Workflow in CLAUDE.md — run automatically every episode going forward, not just this one.
Week of 8/10 weekly build package | — | Done | `wwd-weekly-planner` run 2026-08-10. Priority call: Last House Tue (decay window, edited), Point Break Thu (evergreen debut, edit still open — due night of 8/11). Full package (social copy, 2 polls, short-form bank, growth notes, cold open check-in) saved to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\04 Upload Packages\WWD_Weekly_Package_2026-08-10.docx`. Higgsfield credits were at 0, so this week's 7 images shipped as Firefly prompts instead of generated art — see doc Section 5.
The Whisper Man (2026 Netflix) review upload package | — | Done (needs re-trim) | 2026-09-06. Full wwd-review-pipeline run — export landed mid-session so audio + shorts got done too. All deliverables in `L:\Winter Wolfs Den review show\Raw Footage\Mass recording 30 Aug\The Whisper Man (2026 Netflix)\`: `The Whisper Man - Upload Package.docx` + `.md` (SEO title, description w/ QUICK ANSWERS, 14-line chapters, backend tags 476 chars python-verified, 5 high-volume hashtags, thumbnail, FB/IG posts, cards in MM:SS:frame, schedule, flags); `AUDIO\The Whisper Man.mp3` (192k, matches source); `shorts\` = 6 vertical clips (1080x1920, verified) + `shorts_manifest.txt`. **All 6 shorts are HOLD FOR RE-TRIM** — block-level Premiere timing, soft spoken opens, need manual in-point nudges; clip5 also needs a bleep ("piece of shit" ~21s); clips 4/5/6 under 30s = YT+FB only unless extended for IG. Garbles held: "Michelle Monaghan" spelled 3 ways, "Winter Wolfstein"/"Kingsley" in the cold open. Explicit on-air language flagged for the edit.
The Last House upload package | — | Done | Built from transcript by hand since `wwd-video-upload-package` skill isn't installed on this machine — title/description/tags/thumbnail concepts/pinned comment saved to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\04 Upload Packages\The Last House - Upload Package.txt`.
EP 103 upload package | — | Done | Built by hand from FROSTCAST.md format spec (`wwd-video-upload-package` skill still not installed on this machine). SEO title, 18-chapter description, backend tags, hashtags, thumbnail concept, 6 scored shorts candidates (4 elite ships, 2 held for re-cut), FB/IG posts w/ Firefly prompts, end screens/cards, posting schedule — saved to `L:\Winter Wolfs Den review show\Frost-Cast\EP 103\FrostCast Episode 103 - Upload Package.txt`. Reviewed by a general-purpose agent standing in for the unavailable devils-advocate agent type (verdict: SHIP WITH FIXES, 4 issues found and fixed — see logs\wwd-director.md 2026-08-20 entry). Open flags: shorts clips not yet cut, end-screen/card links are placeholders pending real channel data, shorts host attributions need audio confirmation before crediting Winter Wolf or KingZ by name (voiceprints still not enrolled). Devils-advocate agent gap queued as decision WWD-2026-08-20-01.
Cold open — Warden character designs | ~2026-09-25 (was ~mid-to-late Sept) | Blocked | Punted 3 more weeks, Zac's call 2026-09-04 (target now ~2026-09-25). Still blocked on Higgsfield credits (balance confirmed at 0, free plan, checked 2026-08-10) — cost analysis still pending before topping up. Nothing can generate — including weekly images — until credits are back.
T-2 (Terminator 2) review | — | Done | Released. Closed out per Zac 2026-09-14 — picture set, upload package (.docx+.md), and beat-matched B-roll (Step 8 model case, see `memory\topics\visual-media.md`) all already delivered pre-release.
Resident Evil review — recording date | 2026-09-21 (moved from original date) | Not Started | Moved to next Monday, Zac's call 2026-09-14 — Matt's travel plans changed after the original date was set. Whatever prep (script/B-roll) was targeting the old date now retargets 2026-09-21.
Heat (1995) review — record + release | Record tonight 2026-09-14; release Fri 2026-09-18 (confirmed by Zac) | In Progress | Moved up, Zac's call 2026-09-14. Release day confirmed Friday 2026-09-18 (locked, no more flex). Picture set already delivered (`Raw Footage\Heat\USE\`, 33 images) — see the Heat picture-gather entry above. Step 8 beat-matched pass still pending no script.
Cold open — Higgsfield credit top-up cost (real numbers, checked 2026-09-14) | — | Not Started | Zac asked cost to fund from company money vs. sticking with Firefly. Current balance: 0 credits, free plan. **No one-time top-up packs are currently offered** (checked live — only recurring plans exist right now, despite Higgsfield's own tool description mentioning 500/1000/2000/4000 packs). Real options: (1) 3-Day Free Plus Trial — $0 today, 100 credits, MCP-only, auto-renews to $49/mo unless cancelled before day 3; (2) PLUS — $49/mo, or $39/mo billed annually ($468/yr), 1,000 credits/mo; (3) ULTRA — $129/mo, or $99/mo billed annually ($1,188/yr), 3,000 credits/mo. Recommendation: the free trial is the zero-risk way to test if Higgsfield's output is actually worth it before committing company money — set a reminder to cancel by day 3 if it's not a clear win. Firefly remains the free fallback already used for the Week of 8/10 package and stays viable if the trial/upgrade doesn't get greenlit. This is a spend decision — queued for Zac's call, not made here.
Next FrostCast episode prep | Wed 9pm (weekly) | Not Started | News/trailers/books/games. This is EP111 (Wed 9/9) — EP110 already recorded/transcribed 2026-09-02.
Bring back the audio-only podcast (relaunch) | — | Not Started | Merged 2026-09-04 — this is the same initiative as the old "FrostCast relaunch episode / We're Back" task: WWD/CLAUDE.md notes the audio side has been dark ~18 months even though the video show never stopped. Needs a real deep-dive/plan before anything posts; may still end in a "We're Back" cross-post episode once scoped. Video-side relaunch is NOT needed (no gap there).
Fix Spotify show metadata | — | Not Started | Fix "Winters" typo, standardize episode titles. Holding 2026-09-04 pending the audio relaunch plan above — Zac wants a deep dive before posting fixes live.
Decide new podcast host | — | Done | Decided 2026-09-04 — sticking with Spotify for Creators (free) for now.
Wolf-character short series — concept + production plan | — | Not Started | Idea captured 2026-09-08. Short series built around a wolf character with an "animated but live-action feel." Two open questions before anything else: (1) WHAT is the series about — premise, format, episode length, tone, how it fits alongside FrostCast / Den Files / reviews. (2) HOW do we make it — the animated-live-action look (AI video gen e.g. Higgsfield, 2D/3D animation, hybrid comp, puppet/mocap) and the pipeline for it. Also decide whether this wolf is Winter Wolf (Matt's handle), the WKP wolf character (shared with PAWS, has a 3D model somewhere), the cold-open Warden, or a new character entirely — Zac's call, don't assume. Needs a scoping session with Zac.
Track "Remains" movie for review | 2027-02-14 | Not Started | Releases Valentine's Day 2027 — flag for trailer reaction / review pipeline closer to date.
Retrofit older WWD output docs to .docx | — | Not Started | Root CLAUDE.md's output-document rule (re-locked 2026-09-12, "how many times do I have to tell you") applies to any deliverable, not just guides. T-2's upload package fixed in place 2026-09-12 (.docx built alongside the .md). Still `.txt` only: The Last House and EP103 upload packages. Good Boy (2025) package also needs checking.
Connect thewinterwolfsden@gmail.com to Composio | — | Not Started | Not currently connected anywhere — checked 2026-09-11. Existing Gmail connections are kingzpotus@gmail.com (native), zachary.d.king4@gmail.com and kingdomplannerszk@gmail.com (Composio). Needed to read/manage the show's own inbox.
Surfshark sponsor read — FrostCast EP111 + reusable insert | Wed 2026-09-16 (EP111 recording) | In Progress | Built 2026-09-14 by marketing-director, cleared by `clearance` twice (initial pass + re-check after the CTA rewrite). **Finalized 2026-09-14 pm** — real deal terms confirmed from Zac + Surfshark's approval emails: rev-share affiliate (VPN 40%, Antivirus 60%, Adblock 60%), VPN is the flagship read, corrected tracking link `https://get.surfshark.net/aff_c?offer_id=926&aff_id=47475`, no discount code exists (link-based tracking only — both scripts rewritten to say "link's in the description," code placeholder removed), $100 net / ~5 conversion payout threshold, 90-day cookie window (Zac's figure, not independently verified). Fix routed through `copywriting` (live department, not hand-written). Saved to `L:\Winter Wolfs Den review show\Sponsors\Surfshark\Surfshark-Sponsor-Reads-2026-09-14.md` / `.docx`. STILL NEEDS: (1) confirm "one subscription covers every device" still matches Surfshark's current plan terms — VERIFY BEFORE AIR, (2) Zac/Matt sign-off on disclosure wording, (3) link posted in EP111 description AND pinned comment when it goes live, (4) email affiliates@surfshark.com once the read airs, (5) attorney check on whether written disclosure must sit next to the link in the description/pinned comment (FTC question, flagged by clearance pass 2, unresolved). Backlog, not this week: Antivirus/Adblock pay 60% vs VPN's 40%, worth a future insert. **`no-ai-slop` pass 2026-09-14 (run by Jarvis, standing gate as of today):** em dashes throughout, including inside spoken script lines, cleaned; docx regenerated. Same file paths, edited in place.
Week of 9/14 social calendar (FrostCast EP111, Heat review, Surfshark launch, Constitution Day, POW/MIA Recognition Day) | Runs through 2026-09-20 | In Progress | Full post-by-post plan built 2026-09-14 by marketing-director — platform/day/time/copy for every post, plus short-form ideas list. **Finalized 2026-09-14 pm**, fix routed through `social-media` (live department): Heat release day locked to **Friday 9/18, confirmed** (Thursday-flex language removed); POW/MIA post rewritten per Zac's direction — kept entirely about the POW/MIA service members, no reference to his own service, echoes his "until they all come home" sentiment without attributing it to him by name. Saved to `L:\Winter Wolfs Den review show\2026-09-14 Week of Sep 14\04 Upload Packages\WWD_Weekly_Social_Calendar_2026-09-14.md` / `.docx`. Still unguided on hard engagement numbers — no WWD file exists in `D:\WKP\data\`; times adapted from the established stagger convention (YouTube 11:00 AM ET, IG +45 min, FB +90 min) confirmed in prior upload packages. Remaining open flags: fill episode-specific promo copy after EP111/Heat are actually recorded; route the Surfshark announcement-post badge graphic to `graphic-design` (live department now) if Zac wants one before Tuesday, otherwise text-only. Zac must approve/post everything — nothing here has been published, drafts only. **`no-ai-slop` pass 2026-09-14 (run by Jarvis, standing gate as of today):** em dashes throughout, including the Constitution Day post, the POW/MIA post, and the Heat promo copy, cleaned; POW/MIA wording preserved exactly (only the dash removed); docx regenerated. Same file paths, edited in place.
Department spin-up — copywriting, social-media, graphic-design, video-ugc | — | Done | 2026-09-14, Zac's call. All four moved out of `.claude\agents\_spec\` into `.claude\agents\`, status LIVE. First real use same day: copywriting fixed the Surfshark sponsor-read CTA, social-media fixed the weekly calendar's Heat date and POW/MIA copy. marketing-director routes department-shaped work to them going forward instead of hand-writing it.

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
Vibe-codeable; do before wake-word SDK work. First coding session planned 2026-09-05 — Zac's call 2026-09-04, build guide delivered to `D:\WKP-Guides\Spark Capture - Build Guide.md/.docx` (Android Studio setup through first run, then Note/Room/note-list-screen as session 1 scope).
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


Personal / Admin (non-WKP)
Task
Deadline
Status
Notes
Log Saturday 9/12 package-delivery mileage (~149 mi)
—
Not Started
Zac's package delivery job — quick reminder captured 2026-09-13, log the actual odometer/trip number wherever mileage gets tracked for this job.

How to use this file
New task in any venture → add a row here, same turn it comes up.
Finished something → mark it Done (or just tell me — I'll update it).
Deadlines you don't have yet stay blank — fill in real dates as they get set, especially anything tied to a publisher or a launch.

