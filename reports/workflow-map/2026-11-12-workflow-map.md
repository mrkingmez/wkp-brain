# WKP Workflow Map

Date: 2026-11-12. Built for Zac by a research pass over the repo. Everything below comes from files I opened. Anything I could not open or confirm is marked "not verified" with the reason.

How to read this: Page 1 is the scan table. Then one short section per venture (how it runs, where you act, what is slowing it, what to fix, what is missing). The last part has what you may be forgetting, what to add, and where your time goes.

---

## 1. One-page overview

| Venture | Workflow | Status | Biggest friction |
|---|---|---|---|
| WWD FrostCast | Wednesday chain: transcript, chapters, audio cut, Messenger to Matt, shorts schedule | Working, but heavy | Rules live in 4 places and drifted. You had to repeat the shorts cadence. EP 120 Messenger send and Opus "go" still open. |
| WWD reviews | Photos, run sheet, upload package, shorts | Working (Vision Quest 7 done, Godzilla in progress) | Long bench chain. Cold open blocked on you for weeks. |
| WWD Den Files | Script, research, release | Never run | Episode 1 was due 1 Oct. No log entry shows it shipped. Not verified. |
| WWD shorts | Opus Clip, copy gates, schedule_week.py | Dry run done for EP 120 (59 posts) | Waits for your "go". Gate skill cannot be called by subagents. |
| Fantasy Football | Mon pull, Wed/Thu lineup and card, Tue calibration | Working, best-automated venture | 3 decisions open. Card locks tonight (Thu 11/12). |
| Etsy WarriorKingDesigns | Weekly batch, listing copy, 3/day 8/week cap | Hold | Manual Friday data pull lapsed (last file 2026-08-20). Cap expires Sun 11/15. |
| Kingdom Planners | 7 products, listing prep done for 6 | Blocked | $29 shop fee, flagship file lost, no photos. Payhip test is the way around. |
| KDP | Genten Royalty books | Active, unscheduled | Zero books. CLAUDE.md still says priority 1b. |
| Shattered Empire | Third-draft edit cards, alpha feedback | In progress | Edit cards done through Ch 5. 7 canon items need you. |
| Other books (Stellar Dominion) | Capture only | Dormant | Hand markups from 9/20 never applied. |
| Studio and Ian trailer | Draft 3.2 done, Veo clips next | In progress | Four asks to Ian and music license wait on you. |
| WKP Channel | What If, Hidden Hinge, AAR | Never run | Framework done, no episode produced. |
| PAWS | Scout desk device | Blocked | PAWS-001 and PAWS-004 open since scaffold. |
| Cyber Security | CySA+ | Unknown | Exam date 9/30 passed, outcome unrecorded. No task table. |
| Trading | Watch week, paper trades | Never run | Needs your cue. Broker choice open. |
| Spark Capture | Android app | Active, unscheduled | Phase 2 not scheduled. |
| RUBY TWO | Short film | Pre-production, idle | No module chosen. |
| Photo restore | Side income test | In progress | Stop rule Fri 11/13. |
| Transcription, CMMC kit, Fiverr, LLC | Side ideas | On ice or waiting | Nothing earns yet. Names and USPTO checks owed. |
| Jarvis rhythm | Daily brief, Monday brief, rollup, qa-auditor, Task Observer, decisions triage | Mixed | Monday brief failed 11/09. Daily brief saves nowhere. Weekly reviews not scheduled. |

---

## 2. Rhythm and automation: what actually runs by itself

Only two timers exist in Windows Task Scheduler (checked live):

| Timer | When | Last run | Result |
|---|---|---|---|
| WKP-daily-brief | Tue to Sat, 5:30 AM, `claude -p "run wkp-daily-brief"` | 11/12 5:30 AM | OK (code 0) |
| WKP-Monday-Brief | Mon 5:30 AM | 11/09 5:30 AM | FAILED (code 1). No 11/09 brief exists in `reports\monday\` or `D:\WKP Reports\Monday Brief\`. Last good brief is 11/02. |

Other facts:
- The daily brief renders to a "dashboard" and only saves to `reports\daily\` when asked. That folder does not exist. In a headless 5:30 run, the output is probably lost. Not verified (I did not see the output).
- No Sunday brief timer. Daily brief skips Sunday and Monday.
- `scripts\nightly.bat` (git pull, Jarvis rollup, commit, push) is not in Task Scheduler. Git history shows "Nightly rollup" commits through 11/11 (a682a27), so something ran it. How is not verified. `logs\daily-rollup.md` itself still holds only the 2026-08-21 text.
- tracking-director spec lists a weekly rollup Monday 5:45, a Sunday VidIQ pull, a Friday Etsy read, a Sunday KDP pull. None are scheduled. Its own spec says they only run unattended as cloud routines, and TASKS says cloud routines are "Not Started".
- `wwd-weekly-planner` (Sunday 9:30 PM build) is a user-level skill at `C:\Users\kingz\.claude\skills\`. No timer found. Whether you run it by hand is not verified.
- Numbers: newest `data\weekly-*.md` is 2026-10-30 (13 days old). Newest Etsy file is 2026-08-20. Root rule says if no file in 10 days, a director must call its plan "unguided". Every director is unguided right now except FF.
- Task Observer: weekly review is not scheduled. The 93 KB `observation-log.md` I found is the skill's reference text. Whether real observations were logged is not verified.
- qa-auditor weekly review: in TASKS as "Not Started". No QA reports exist (`logs\qa\` is empty).
- Memory and brain files: `git status` shows about 40 modified files and several untracked. The rule says commit and push before a session ends.

Rhythm map:

| Cadence | What | Who runs it | You act |
|---|---|---|---|
| Daily 5:30 AM Tue to Sat | Daily brief | Task Scheduler | Read it |
| Monday 5:30 AM | Monday brief .docx | Task Scheduler (broken 11/09) | Read, print |
| Monday | Fantasy data pull | fantasy-football-director | Nothing |
| Tuesday after MNF | FF calibration | FF scripts | Nothing |
| Wednesday 9 PM | FrostCast record, then chain | You, then main session | Record, Messenger check |
| Thursday | Card and lineup lock | FF director | Submit by hand, send saved-lineup screenshot |
| Friday | Etsy manual numbers | You type them | Lapsed |
| Sunday night | VidIQ pull, weekly planner | Manual | Not verified |

---

## 3. WWD / FrostCast

### 3a. FrostCast Wednesday chain

| Step | What | Who | Output | You act |
|---|---|---|---|---|
| Trigger | You say "episode is downloaded" (file in `L:\...\Frost-Cast\EP n\`) | Jarvis | | Download |
| 1 | Transcribe with voiceprints, `--num-speakers 3` or 2 | wwd-video-transcriber on GPU | `.txt` in the EP folder | |
| 2 | Chapters | wwd-frostcast-chapters | `EPnnn-chapters.txt` | |
| 3 | Audio-only cut doc | wwd-audio-cut | `.md` in `L:\...\podcast Frostcast audio files\` | Edit audio yourself |
| 4 | Transcript to Matt on Messenger | Main session with Chrome tools | Message with file, screenshot proof | Facebook must be logged in |
| 5 | Shorts: upload to Opus Clip | You | Opus project id | Upload and say "done" |
| 6 | Pick clips, copy through script-room, marketing, no-ai-slop | wwd-director and desks | `EPnnn-approved-copy.json` | |
| 7 | Dry run `schedule_week.py` | Script | plan CSV | Say "go" |
| 8 | `--go` | Script (needs OPUS_API_KEY) | Scheduled posts | The go is public posting |

Also before the show: Tuesday planning photo goes to `Frost-Cast\FrostCast Show docs\Pictures\`, then wwd-show-prep builds the prep sheet and a poll. Both EP 120 docs exist.

Status: working. EP 120 is the proof (transcript, 13 chapters, audio cut, 59-post plan all built).

Friction (evidence):
- Same rule in many files, drifted. Shorts cadence: you said "for the final time" on 11/11 after agents used the old 31-slot logic twice (memory `feedback-shorts-cadence`). Root CLAUDE.md step 7 still says "The 31-slot weekly volume and YouTube one-a-day are locked". The script was patched 11/12 with a `--plan-csv` mode. Not verified that the old SLOTS table is gone.
- Root CLAUDE.md and `WWD\CLAUDE.md` still say FrostCast is at episode 106 and the cold open is "around 112". Logs show EP 120. `WWD\CLAUDE.md` also says voiceprints are "not yet done" while root says enrolled 11/11.
- `wwd-director.md` lists skills `wwd-video-upload-package` and `wwd-shorts-clip-factory` that `WWD\CLAUDE.md` says never existed.
- The no-ai-slop gate fails inside subagents. Logs 11/11 and 11/12: "skill not callable here", so a general-purpose agent or a manual read stood in.
- Two chapter files in EP 120 (12 and 13 entries). Messenger send still open in the log at 23:30 on 11/11. Whether it went out later: not verified.
- 11/11 you were angry about questions on a night that "should just run". The new rule (own the operation) is in memory but not in the director specs.
- fact-check file for EP 120 did not exist when clips were vetted.

Improvements, ranked:
1. One config file for cadence and slots that `schedule_week.py` reads. Delete the rule text from CLAUDE.md and point to it.
2. One `FrostCast-chain.md` runbook with a done-checklist and the "pick, say which in one line" rule. Directors read it instead of rediscovering.
3. Run fact-research on flagged claims before the cut doc, not after.
4. Make the slop gate a script (like `lint_run_sheet.py`) so any agent can run it from Bash.
5. Fix the stale lines (episode count, voiceprints, phantom skills, cold open note).

Gaps: no 48-hour post-publish check (spec only). No scheduled Sunday VidIQ pull. No check that the Messenger send happened besides a screenshot.

### 3b. WWD review pipeline (Vision Quest, Godzilla Minus Zero and others)

| Step | Who | Output |
|---|---|---|
| "We are doing a review on X" | wwd-review-photo-pull intake | folder, 18 pictures, resized to `USE\`, calendar dates (main session adds them, director has no calendar tool) |
| Zac records, cuts banter, exports Premiere transcript | You | transcript |
| Pictures, clips, run sheet | wwd-pictures, wwd-clip-scout, wwd-run-sheet (with wwd-vfx, music, wwd-sound) | run sheet .md and .docx, lint passes |
| Rights | wwd-rights | fair use note |
| Upload package plus shorts captions | wwd-review-pipeline, copy via script-room, marketing | one .docx in `D:\WKP Reports\WWD Upload Packages\` and the movie folder |
| Shorts built, audio extracted | pipeline (shorts-factory) | `\shorts`, `\AUDIO` |
| Post | You | Upload, cards, end screen, schedule |

Status: working. Vision Quest 7 finished and uploaded 11/10. Godzilla Minus Zero package exists, open items listed in TASKS (release date, title pick, loudness -24.7 LUFS, logo sting, IMDb pull).

Friction: the chain is long (director, pictures, clips, run sheet, vfx, music, sound, rights, QA). Cold open shot list blocked on you ("draft built from the wrong script", Higgsfield block stale). Vision Quest EP 8 end card does not exist. Audit 10/29: wwd-director launched 21 times, general-purpose 20 (work landing on a generic agent when a specialist exists).

Improvements: (1) one "Godzilla close-out" session to clear its six open items. (2) Give wwd-vfx the EP 8 end card order now. (3) Decide the cold open: either you hand over the right files or the cold open is dropped for now.

Gaps: no per-review "post-mortem numbers" pull. Calendar entries depend on the main session.

### 3c. Den Files

Trigger: Zac picks a film. Steps in spec: Zac researches and writes, Matt reviews, script-room two passes, fact-research, devils-advocate, release about every 6 weeks. Status: never run. Episode 1 (Fire in the Sky) was locked for 1 Oct 2026. I found no log of it shipping. Not verified. Topic queue beyond episode 1 is still "[FILL IN]". Friction: the script gate (two passes, logged) has no recorded pass for it. Improvement: decide if Den Files is alive. If yes, one scoping session and put Ep 1 on the calendar. If not, say so and remove it from CLAUDE.md. Gap: no format file confirmed at `WWD\formats\den-files.md` (not verified, I listed the folder only by name).

### 3d. WWD money and growth items (all waiting on you)

WWD-2026-11-05-01 to 08 (affiliates, Bookshop, Ko-fi, Earn tab and Spotify numbers, sponsor line layout, spoken sponsor audit, Studio Shopping, Amazon or POD). The agents' own recommendation: do the YouTube Studio Earn tab and Spotify Monetize check first, it is a screenshot, then the rest unlock in order. Also open: Surfshark status, subscriber loss five fixes (review about 11/30, Matt brief not sent), audio-only podcast comeback, Spotify metadata fix, Wolf character short series, COLD TOW comic (needs Matt and Gabby yes).

---

## 4. Fantasy Football (personal)

| Step | Who | Output |
|---|---|---|
| Monday: data pulls (MFL, odds, nflverse) | fantasy-football-director, fantasy-football-data, nfl-data | files in `data\` |
| Tuesday after MNF: calibration | `run_weekly_calibration.py` | scores |
| Wed: first run after practice reports; Thu rerun and on any news | ff-simulator, ff-play-sim | lineup, 20-game pick card, DFS notes |
| Thursday: saved-lineup screenshot or API read | You and `read_saved_lineup.py` | confirmed lineup |
| Submit | You, by hand | Nothing is submitted by agents |
| Recap | Director | tracker `predictions.csv` |

Status: working, most mature loop in the repo. FF-2026-11-12-01 and -02 implemented today.

Friction: 3 old decisions open (bad closing line, lunch notes missing, Week 9 lineups do not reconcile), 3 new (taxi rule, Elimination Challenge, no Week 10 DFS salary file), tracker backfill Weeks 2, 3, 5 approved but not done because the logger refuses post-kickoff rows. `ff-play-sim` and `ff-simulator` files show as modified and uncommitted. College football data for the card: SW-2026-11-11-01 open.

Improvements: (1) answer the three Week 10 questions before tonight's lock. (2) Commit the working changes so backtests are reproducible. (3) Write the backfill as a one-off script with an explicit "historical" flag.

Gaps: DFS has no confirmed source of truth for what you entered. No season scoreboard report (hit rate vs the 12-year 62 percent) is on disk as a saved doc. Not verified.

---

## 5. Etsy WarriorKingDesigns

Trigger: Friday manual data, wkd-weekly-batch. Steps: research (design-market-research), batch plan within cap (wkd-weekly-batch), listing copy (etsy-director, copy through the writing room), listing photos, post (you). Outputs: `ETSY\weekly-prep\`, zips in `_Print Exports`. Status: hold ("triage complete, hold" in root CLAUDE.md). Zero confirmed live listings since before 8/15 per ETSY-2026-11-02-01.

Friction:
- `ETSY\CLAUDE.md` says new listings are digital printables posted Mon and Wed, and root CLAUDE.md repeats it, while the venture is on hold. Two files promise cadence the shop does not run.
- The F-35 hard rule vs live listings (WKD-2026-09-01-01) came up in the etsy-director log; its current status is not in DECISIONS (cleared 11/11).
- The ETSY file says "never launched" skill names twice and carries three [FILL IN] items.
- Audit: etsy-director launched 0 times in a month.

Improvements: (1) Decide the cap before Sun 11/15 (renew through BFCM, loosen, or let lapse). (2) Pick: restart weekly batch for BFCM (Black Friday is 11/27, no copy done) or formally park the shop. (3) One Friday data habit or drop the closed-loop rule for Etsy.

Gaps: no returns or review monitoring for WKD (kp-reviews exists only for KP). No sales ledger for WKD.

---

## 6. Kingdom Planners

Trigger: shop creation. Steps: kp-recon (what sells), kp-generator (spreadsheets), kp-prep (8-image set), kp-planner (batch within shared cap), kp-ledger, kp-reviews. Per-listing copy done 9/24 for 6 of 7. Status: blocked.

Blockers (evidence): $29 Etsy fee (you: wait for funds), Complete Budget System file lost (built in a web chat, never downloaded, the exact loss the retention rule names), photo set not built, Google Sheets compatibility never opened for real. Removed as main effort 11/11. Payhip 1-hour test is prepared (`D:\WKP Reports\Kingdom Planners Payhip Test\`) and would need no Etsy fee. VA tables go stale Dec 1.

Friction: `LOCAL-PATHS.md` lists three empty Kingdom Planners folders; the CLAUDE.md [FILL IN] list is the old state. Standing assessment says do not build product eight, which is correct.

Improvements: (1) Run the 1-hour Payhip test this weekend, it is the only path to revenue that is not gated by $29. (2) Rebuild or retire Complete Budget System, one decision. (3) Update the VA tracker rate tables before Dec 1 or pull the product from the test.

Gaps: no real Sheets-open pass, no photo-capture helper, no Pinterest account yet, no refund or support workflow.

---

## 7. KDP

Trigger: Genten Royalty hands-on session (Day 1 never done). Status: active, unscheduled. Zero books. kdp-director launched 0 times. `KDP\CLAUDE.md` still says "Priority 1b, behind Kingdom Planners" and "ACTIVE/high-priority", contradicting root CLAUDE.md (downgraded 1 Sep) and the Tracker has only the example row.

Improvement: fix the stale priority text in one line. Gap: no hands-on workflow has ever been recorded, so no skill can exist.

---

## 8. Shattered Empire and other books

| Step | Who | Output |
|---|---|---|
| Alpha feedback worksheet | fiction-alpha-feedback via shattered-empire-director | worksheet (template only in `alpha-feedback\`) |
| Third-draft edit cards | scripts from the Third Draft Editorial Report | cards in `third_draft\edit_cards\`, docx in `D:\WKP Reports\Third Draft Edit\` |
| Canon checks | fiction-director, ledgers | 36 conflicts logged, 7 Zac-only items |
| Edit by you | You | Revised chapters |
| Query letters | fiction-director | Not started |

Status: in progress. Cards done for Prologue to Ch 5 (236, all verified). Open for you: Ash name spelling, Fort Dreknor, ring hand, Weslin object, Merrick manor (C-07, C-13, C-15, C-22, C-28).

Friction: `Shattered-Empire\CLAUDE.md` still describes a Google Drive manuscript flow. `LOCAL-PATHS.md` (10/6) says `D:\The Shaterred Empire Series` is the canon set. Source copies in the logs are extracted .txt, not checked against Drive.

Improvements: (1) answer the five canon items in one sitting. (2) Rewrite the workflow section of CLAUDE.md to the D:\ flow. Gap: no word-count or progress tracker for the edit pass, no beta-reader recruiting workflow, no query tracker.

Stellar Dominion: dormant, capture only. Hand markups from 9/20 never applied. Fine for now.

---

## 9. Studio and the Ian Griffin trailer (free, friend favor)

| Step | Who | Output |
|---|---|---|
| Brief and point man | studio-director, marketing-director picked the point man 11/4 | production package |
| Draft 3.2 (45 s master and 15 s cutdown, 9:16 and 16:9) | studio-director | `Post-Production\reports\...Draft3-2.md`, docx in `D:\WKP Reports\Ian Book Trailer\` |
| Reference stills, then Veo 3.1 clips (21 planned, cap 24) | You click generate | clips |
| Rough cut, end card | You in Premiere | cut |
| Gates: script-room 2 passes, clearance, marketing, no-ai-slop, qa-director | desks | PASS or FAIL |
| Deliver files to Ian | You | Ian posts |

Status: in progress. The father question was resolved 11/12 as a misread (Brandon is the father, his child must not be seen). Open for you: buy link on a phone, music pick and license proof, cover maker permission, who is on the cover, back-cover line, AI label toggle advice.

Friction: no Firefly cost per run retrieved, Veo 16:9 start-frame support not verified, no platform upload spec checked.

Improvement: send Ian one text with all five questions. Gap: no generic book-trailer template for the next client; no price or booking page for Post-Production. Fiverr and outreach prep exists but names are not picked.

---

## 10. WKP Channel (What If, Hidden Hinge, AAR)

Trigger: wkp-channel-director plans an episode. Steps: mil-research, fact-research, format skill (whatif-format, hiddenhinge-format, aar-format), script-room two passes, graphic-design art, music, Studio produces, you post. Pilot chosen: AAR Commander, Fort Necessity. Status: never run, framework only. Zero episodes in `WKP-CHANNEL\research\`. Friction: marked ACTIVE-UNSCHEDULED, no producer time, faceless production skill gap (same as RUBY TWO). Improvement: a single 3-minute test video is a better next step than another framework doc. Gap: no production workflow (what tools, who edits) written.

---

## 11. PAWS

Trigger: PAWS-001 (task source) and PAWS-004 (hours per week) answered. Done so far: Scout character locked, state machine on PC (7 tests pass, 10/15), parts research, hardware direction (fused personality plus USB-C hub). Everything firmware is blocked. Hardware purchase paused. Audit: paws-director launched 0 times. Hard rule: no mic, no LLM, no data collection for under 18. Improvement: answer two questions (5 minutes) or formally park. Gap: no budget line for parts.

---

## 12. Cyber Security and CySA+

Day-job practice, not a business. `Cyber-Security\CLAUDE.md` is 20 lines and says exam 30 Sept. Today is 43 days past it, no recorded outcome (CS-2026-10-28-01). No task table exists in TASKS.md so nothing here can ever show as changed. Cisco suite onboarding was promised "fast and practical"; no files exist for it. Improvement: one line from you (passed, failed, rescheduled) and a three-row task table. Gap: no study plan, no Cisco quick-start.

---

## 13. Trading

trading-director plus 11 trader-* skills exist. Watch week "not run" as of 11/10. Needs your cue. Decide Robinhood vs Alpaca (conflict logged in the rules). `WKT_Watcher.zip` built 10/19, never run, unaudited. Investing stays DORMANT in root CLAUDE.md while TASKS lists Trading as a waiting item, which is a small contradiction. The director never places orders or touches keys. Improvement: either start the watch week on paper (free, reversible, zero money) or park. Gap: no scorecard exists yet.

---

## 14. Spark Capture and RUBY TWO

Spark Capture: scaffold only, Phase 2 (app shell) not scheduled, Android Studio on I: paused. No agent by design. RUBY TWO: bible and 14-scene screenplay exist, folder is named `Ruby-One` on disk while root CLAUDE.md says `./RUBY-TWO/` (also `SCI-FI Novel` vs `./SciFi-Novel/`). Neither has a task row. Gap: no one owns either. They stay parked until you pick.

---

## 15. Side income (photo restore, transcription, CMMC, Fiverr, LLC)

| Idea | Status | Evidence |
|---|---|---|
| Photo restore | In progress, first | Launch prep and Photoshop guide done 11/10. Stop rule Fri 11/13: groups list with member counts and selling rules, or it stops. |
| Fiverr and outreach, brand kits | Waiting | Prep doc 11/10. Names, USPTO and Georgia SOS checks owed. |
| LLC | Waiting | Research done (GA $110, $60 a year, EIN free). One entity or many not decided. |
| Transcription business | On ice | HOLD per devils-advocate, test after photo restore week. |
| CMMC Level 1 kit | On ice | Market not shown. Day-job conflict check by you needed first (VENTURE-2026-11-03-01). |
| Newcomer guide | Open | VENTURE-2026-11-05-01, slow or no demand proof, cheap free test proposed. |
| Ian trailer | Free | Never counted as cash (memory). |

Friction: seven ideas, zero revenue, one stop rule. No single place compares them. Improvement: one cash-first scoreboard (hours to first dollar, money needed, blocker). Kingdom Planners on Payhip and photo restore are the closest to cash. Gap: payment app not chosen, no customer intake form.

---

## 16. Shared departments

| Department | Status | Evidence |
|---|---|---|
| Writing room (script-room) | Working | Used for scripts and WWD copy. Two-pass gate depends on it. |
| Marketing (and social-media, video-ugc, market-research) | Partly idle | Audit: video-ugc and market-research 0 launches. Marketing used for WWD copy and monetization research. |
| Graphic design | Idle | No image tool works (Higgsfield 0 credits at last check; Firefly is your hands). |
| Music | Light use | Music is intro and outro only. Ian trailer track pick is open. |
| Fact research | Working | Used for EP 120 and the animation tutorials. |
| Tracking | Lapsed | No pull since 10/30. Etsy file since 8/20. |
| Animation | Built, not used | Specs and 7 skills done. Three sign-offs and tutorial picks wait on you. Starter kit images are inside the git folder (ANIM-2026-11-05-01, copyright risk if pushed). |
| Studio | Working | Ian trailer. |
| QA (director, documents, claims, media, auditor) | Built 11/10, first runs offered | `logs\qa\` empty. |
| Software | Built 11/10 | Used for FF data (SW decisions open). |
| Devils-advocate | Orphaned | Audit: 0 launches, not in any gate chain. WWD spec says it reviews before ship. |

Friction: an agent roster of about 55. 10 never launched in the month audited. Changes load only at the next session start.

---

## 17. What you might be forgetting

Dated and near:

| When | Item | Source |
|---|---|---|
| Tonight Thu 11/12 | Fantasy Week 10 card and lineup lock at Thursday kickoff. Three open questions (taxi rule, Elimination Challenge, no DFS salary file). | DECISIONS FF-2026-11-11-01 to 03 |
| Fri 11/13 | Photo restore stop rule: groups list, selling rules, 3-photo test, payment app, names | TASKS |
| Sun 11/15 | Etsy listing cap expires (3 a day, 8 a week) | root CLAUDE.md, ETSY-2026-11-02-01 |
| Mon 11/16 | Monday brief timer is due again after the 11/09 failure | Task Scheduler |
| Wed 11/18 | FrostCast EP 121 chain, plus EP 120 shorts plan still waiting on your go | logs |
| About 11/30 | Subscriber loss review, brief to Matt not sent | TASKS |
| Thu 11/27 | Thanksgiving and Black Friday (BFCM prep flagged in the Etsy prep doc, no copy done) | ETSY log |
| Dec 1 | VA tables stale, Kingdom Planners VA tracker | TASKS |
| 2027-02-14 | Remains (movie) releases | TASKS |

Open loops with no date:
- CySA+ outcome (exam was 9/30).
- Surfshark sponsor read: plan terms, disclosure wording, attorney question open since September.
- Tailscale and second machine: install status unknown.
- EP 120: Messenger transcript send not confirmed in logs, two chapter files, Opus "go".
- Godzilla Minus Zero: release date, title pick, card links, loudness, rights flags.
- Vision Quest EP 8 finale and its end card.
- Cold open shot list: blocked on you, files and Warden brief.
- Den Files Episode 1 (target was 1 Oct).
- Ian: five questions, music license.
- Etsy shop needs $29 and the flagship file is lost.
- PAWS-001 and 004. LLC choice. Fiverr and brand name checks.
- Package-delivery mileage log (you needed it since 9/13).
- King Debt Planner needs APRs, living costs, due days.
- Shattered Empire canon items (five).
- Animation sign-offs and the starter-kit images in the repo.
- 40 uncommitted files. A commit and push (memory lives in git).
- Connect thewinterwolfsden@gmail.com to Composio.
- Monday brief failure itself (nobody was told).
- Matt: the five fixes brief, and the comic needs his and Gabby's yes.

---

## 18. Workflows you might want to ADD (ranked)

1. Failure alert for the timers. The Monday brief died on 11/09 and you did not find out from the system.
2. Friday money-and-dates check (10 minutes, one command): numbers pull, Etsy file prompt, items due in 14 days, uncommitted files.
3. One FrostCast chain runbook with a done-checklist. It is the workflow you complained about most.
4. Cash-first scoreboard for all side income. Seven ideas, one page.
5. A decision batch session: the 20 open items with recommendations as yes or no, 15 minutes. Start with Studio Earn tab and Spotify numbers.
6. Weekly stale-rule sweep by qa-auditor: CLAUDE.md vs TASKS vs agent specs vs scripts. The drift list in this map is what it would catch.
7. Scripted slop gate any agent can run.
8. Back up `D:\WKP Reports\` (it is not in git, and the Complete Budget System loss shows the risk). One scheduled copy to another drive.
9. Sponsor and affiliate tracker with dates and disclosure wording (Surfshark first).
10. 48-hour post-publish check on each WWD video, already in the tracking spec but never scheduled.

---

## 19. Cross-venture view: your time

What competes for your hours (full-time job, fragments, ADHD):

| Block | What eats it | Agents can take |
|---|---|---|
| Wed 9 to 11 PM plus the night | FrostCast record and chain checks | Everything after the record, except the Opus go and the Messenger login |
| Thursday | FF lock, submit by hand | All analysis. Submission stays yours by design. |
| Friday | Etsy numbers, photo restore stop rule | Pulls if scheduled |
| Sunday | Weekly build, VidIQ, planning | The whole build if a timer exists |
| Any gap | Editing (reviews, Ian trailer) | Prep, run sheets, packages, QA |
| Any gap | Clicking generate in Firefly or Veo | Prompts and settings only. Credits and clicks stay yours. |
| Any gap | Open decisions (20) | Pre-filled recommendations |

Where agents could take more within your two limits (money and public posting):
- Scheduling and timers: set the Task Scheduler jobs for the Friday pull, Sunday build and nightly rollup, with failure alerts. Reversible, no spend.
- Draft everything posting needs, up to the last click. Opus dry run is already built; the go is the only step you own.
- KP and WKD listing packs, photo shot lists and screenshot capture instructions (agents prepare, you post).
- Pre-answer decisions with evidence, so you only say yes or no.
- Stale-file sweeps and uncommitted-work reminders.
- Trading watch week on paper and animation scouting, both free.

Where agents are not the answer: Facebook login, Opus go, Firefly and Veo credit clicks, FF submission, Matt and Gabby yes, anything with a price.

Biggest time sink I can see: the same rule being re-learned each week (shorts cadence, voiceprints, episode count). One place per rule would give back the most Wednesday nights.

---

## 20. Top 10 improvements across everything

1. Put each locked rule in one file and sweep the stale copies (EP 106, voiceprints, cold open, KDP 1b, phantom skills, root folder names, shorts slot rule).
2. Fix the Monday brief and give the daily brief a saved output, plus a failure alert.
3. Restore the weekly numbers pull on a timer (data is 13 days old, Etsy 3 months old).
4. FrostCast chain runbook with a done-checklist and the "decide, do not ask" rule.
5. Answer tonight's FF questions and clear the old FF decisions.
6. Decide the Etsy cap before Sun 11/15 and decide BFCM go or park.
7. Run the Kingdom Planners Payhip test (no $29 needed).
8. A 15 minute decision batch for the 20 open items, WWD monetization first.
9. Make the no-ai-slop gate runnable by any agent as a script.
10. Back up `D:\WKP Reports\` and commit the brain files.

---

## 21. What I could not verify

- Google Calendar contents (not opened).
- Whether the nightly rollup has a scheduler (git commits prove it ran; no Windows task found). The Cloud routines may exist outside Task Scheduler.
- Whether EP 120 transcript reached Matt on Messenger. The log still lists it open at 23:30 11/11.
- Whether Den Files Episode 1 shipped, and whether `WWD\formats\den-files.md` exists.
- Whether real observations are logged for Task Observer.
- Contents of most skill bodies (I read descriptions, plus the briefs, vidiq pull and jarvis skills). Not read in full: ANIMATION\CLAUDE.md, `.claude\agent-memory\`, the PAWS format files, the photo restore and Fiverr docs, `Investing\WKT_Watcher.zip`.
- The Etsy shop's real live state and Higgsfield credit balance today.
- Whether `schedule_week.py` still contains the old 31-slot table.
- The 11/09 Monday brief failure cause (only the exit code 1 was read).
