# WKP Memory

Index of operational learnings. Details live in `topics/`. Read this every session.

Protocol: `.claude/commands/mem.md`
Routing rule: decisions go in a CLAUDE.md, machine paths go in LOCAL-PATHS.md,
learnings go here.

---

- [Tools and infrastructure](topics/tools.md) — IMDb/TMDb image pulls via in-page fetch and Python CDN download, Chrome tool output limits (2026-10-20); Google Drive corrupts markdown through its API, Claude Code needed a non-obvious npm flag, Drive search needs parentId chaining; "built in a web session, never moved into the repo" is a recurring pattern (KP's budget file, WKD's listing-factory skill) — check adjacent folders before calling a missing skill/file fake
- [Video transcription](topics/transcription.md) — WWD transcriber pipeline: GPU/CUDA setup, gated Hugging Face models, HF_TOKEN env var (not a CLI flag), torchcodec is broken here (bypassed, don't try to fix it), output path rule, memory pressure while gaming; push chapter list proactively the moment it's ready, don't wait to be asked (2026-09-24)
- [WKP operating rules](topics/wkp-ops.md) — fire-and-forget partnership, voice-to-text handling, flag file updates in the moment, repo is on D: not C:; a relayed Zac quote is never enough for a held venture, only his direct word in-session or a written repo change counts; when a hold keeps blocking legit standing work, check if the wall is scoped wrong before trying harder to get past it (WKD 2026-10-03)
- [Writing and content formats](topics/writing.md) — Watershed and Hidden Hinge never mix, Blender mesh standards; **no em dashes / nothing generic is now a general rule for everything public**, enforced via `no-ai-slop` skill, locked 2026-09-14
- [Kingdom Planners](topics/kingdom-planners.md) — shop not yet created on Etsy; Complete Budget System's file is confirmed lost (2026-09-24), only 6 of 7 products real on disk, never trust a CLAUDE.md product description without opening the real file
- [Visual media / framing](topics/visual-media.md) — contain/fit resize rule (never crop); wwd-review-photo-pull runs Step 8 (beat-matched images) and Step 3.5 (cover every character with a real subplot, not just the leads — added 2026-09-14 after Heat missed Portman/Judd/Venora/Haysbert); never use the same picture twice in one video (locked 2026-10-19)
- [WWD skill output formats](topics/wwd-skill-formats.md) — mass record of two shows layout (one folder, one subfolder and USE and P:\WWD Kit folder per show, Speaker 1 = Winter Wolf, 2026-10-20); wwd-audio-cut uses one chronological Start/Cut list (not separate KEEP/DROP blocks), locked 2026-09-02; weekly output stays in ONE per-week folder, not split into topic folders like "WWD Social" (reversed 2026-09-16); review shorts are now BUILT via shorts-factory.md (5 clips max, all finished, no holds, burned-in captions, 2026-10-14)
- [Automation vision](topics/automation-vision.md) — Zac's fire-and-forget/automation push, dual-machine + voice assistant plans, "no ventures on hold" asked-not-confirmed 2026-09-12
- [Personal/non-WKP](topics/user-personal.md) — Zac has a package delivery job, needs mileage logged (first surfaced 2026-09-13); was sick ~2 weeks through late Sept/early Oct 2026, explains the production slip on several items
- [Marketing / sponsors](topics/marketing-sponsors.md) — Surfshark affiliate deal terms + corrected tracking links, marketing subagent spec→live pattern, POW/MIA content must stay about the missing/captured, never about Zac's own service (2026-09-14)
- [Fantasy football](topics/fantasy-football.md) — blank pick'em card is the trigger to produce model picks, not something to wait on; lineup calls need real research, not just projected points (corrected 2026-09-15)
- [Firefly video models](topics/firefly-models.md) - the real model menu on Zac's Firefly (Veo 3.1, Kling 3.0, Runway Gen-4.5, Luma Ray, Firefly Video), settings panel, start-frame slot; Matt paid for credits (2026-10-25)
- [Double check before 'missing'](topics/wkp-ops.md) — verify a second way before saying a file/attachment is not there; Outlook winmail.dat can hide a second attachment (Week 8 card miss, 2026-10-28)
- [Verify agent calendar writes](topics/wkp-ops.md) - agents can claim calendar events they never made; list the calendar to confirm; Zac wants mainstream wide releases on the WWD calendar (2026-10-29)
- [Show session = resume command](topics/session-resume.md) — 'show session' means give the claude --resume line (2026-11-01)
- [Push at end of batch](topics/push-batching.md) — batch pushes after installs/add-ons, not each change (2026-11-01)
- [Leave Adobe alone](topics/leave-adobe-alone.md) — never disable Adobe startup/tasks; Zac said so twice (2026-11-01)
- [Fantasy timing](feedback-fantasy-timing.md) — first run after Wednesday practice reports, rerun Thursday and on any new info, report every change (Zac 2026-11-04)
- [Agent authority](feedback-agent-authority.md) — Jarvis is CEO: start any agents without asking, may create standing assistants; only money or public posting needs Zac's yes (2026-11-05)
- [Nyssa voice is all profiles](feedback-nyssa-voice.md) — do not rule one winner; Zac fixing the guide, ignore Nyssa voice items until next pass (2026-11-04)
- [Day-job outside work cleared](project-day-job-outside-work-cleared.md) — settled, never ask again, TDIU still open (Zac 2026-11-10)
- [Ian trailer is free](project-ian-trailer-free.md) — friend favor, not paid, never list as a cash source (Zac 2026-11-10)
- [No actor tags](feedback-no-actor-tags.md) — WWD reviews skip on-screen actor name tags; write run-sheet notes in plain words (2026-11-07)
- [Operating procedure](feedback-operating-procedure.md) — Jarvis delegates, QA checks everything, take your time, new divisions go to Zac (2026-11-10)
- [Secondary pictures](feedback-secondary-pictures.md) — gap-fill pictures come from the title being reviewed, not other shows, unless a major feature point (Zac 2026-11-10)
- [Design skills installed](project-design-skills-installed.md) — Taste + Impeccable in, Impeccable engine/hooks left out, others not installed (2026-11-10)
- [Veterans Day tone](feedback-veterans-day-tone.md) — celebrate service, honor the living; fallen-led tone is Memorial Day (Zac 2026-11-10)
- [Always include the flag](feedback-always-include-flag.md) — patriotic and military graphics always show the American flag, never "no flag" prompts (Zac 2026-11-10)
- [Code-made art](feedback-code-made-art.md) — drawn-in-code artwork looked amateur; real image-model art for public graphics, code only for text overlay (Zac 2026-11-10)
- [Ian trailer secret](project-ian-trailer-secret.md) — the secret is that Brandon is a father and the kid near the end is his, not his own dad; drafts 3.1 and 3.2 misread it (Zac 2026-11-12)
- [Fantasy picks format](feedback-fantasy-picks-format.md) — keep the Week 10 Picks and Lineup phone doc layout every week (Zac 2026-11-12)
- [Shorts cadence](feedback-shorts-cadence.md) — YouTube 1/day incl Thu 6 to 7 PM; FB+IG Thu 1 at 6 PM, 4 to 5/day Fri to Tue, Wed 1 morning + 1 afternoon; 31-slot logic retired (Zac 2026-11-11, final)
- [Own the operation](feedback-own-the-operation.md) — research agents resolve flags first, Jarvis decides, never bring judgment calls or unchecked flags to Zac; Wednesday chain must just run (Zac 2026-11-11)
- [Zac's Fiverr history](user-fiverr-history.md) — established seller, over $7,000 since 2016 (his word); not a new seller (2026-11-13)
- [Opus clips settled](feedback-opus-clips-settled.md) — EP 120 shorts approved, never re-ask or list a spot-check (Zac, 3 times, 2026-11-12)
- [Take initiative](feedback-take-initiative.md) — build plans and fix known gaps unprompted, look on disk before asking Zac, report results (Zac 2026-11-11)
- [Agent learning goal](feedback-agent-learning-goal.md) — every agent improves each run, directors wire departments, never repeat a failure; plus yes/no first on capability questions (Zac 2026-11-17)
- [Household money reports](feedback-household-money-reports.md) — wife reads them; forward-looking only, no blame or history (Zac 2026-11-17)
- [2027 debt payoff](project-2027-debt-payoff.md) — all-in on debt in 2027, new loan 11/18, cut courses/games/apps, small fun allowance (Zac 2026-11-17)
- [Ian trailer settled](project-ian-trailer-settled.md) — Polaroid is past Brandon + dad, fence is present-day child only, Adobe SFX free, ElevenLabs for missing sounds, no credits, cover is its own story piece, V4 cut (Zac 2026-11-17)
- [Refresh before sims](feedback-refresh-before-sims.md) — refresh stats, odds, MFL, injuries and confirm starting QBs before every fantasy or DFS sim (Zac 2026-11-19)
- [Clip length](feedback-clip-length.md) — WWD clips 6 to 8 s, up to 12, old 4 s and 30 s limits retired; no total cap set (Zac 2026-11-19)
- [Intro length](feedback-intro-length.md) — WWD review intro stomp-and-clap sting must be 6 s or less, 11 to 12 s was way too long; one generation cut into intro and outro to save credits (Zac 2026-11-19)
- [SOPs and agent lessons](../SOP/SOP-00-Master-Workflow.md) - system reset 2026-11-19: `D:\WKP\SOP\` is the single source for job flow, output paths and formats, agent learning, WWD review, editing and music; every agent has a lessons file in `memory\agents\<agent>.md`, read before a job, one lesson appended after (Zac: agents must learn, formats must stop changing)
- [Zac verifications 2026-11-19](topics/zac-verifications-2026-11-19.md) — Percy Jackson is next, ElevenLabs likely needs $11 plan, Vision Quest live (no shorts yet), Monday/Saturday failures were no tokens
- [Run guide, not straight cuts](feedback-run-guide-not-straight-cuts.md) — Zac edits from the run sheet guide, low time and capacity; bake style into the run sheet and prep cut, teach in tiny steps (Zac 2026-11-20)
- [Drive mirror](feedback-drive-mirror.md) - N: is Google Drive; copy WWD packages and Shorts to Drive ONLY WHEN ZAC ASKS, never automatic (Zac 2026-11-20)
- [Sound pull](feedback-sound-pull.md) - every WWD run sheet gets a sound pull in P:\WWD Kit\<Movie>\Sounds\, assistant-editor's duty (Zac 2026-11-21)
- [Project board](feedback-project-board.md) - REFERENCE\ folder: PROJECT-BOARD, NAMES-AND-SPELLING, GLOSSARY, LOCKS, VIDEO-LIBRARY; every agent reads it before a job, directors ask the board before Zac (Zac 2026-11-21)
- [Teams not smaller](feedback-teams-not-smaller.md) - Shattered Empire, teams are not being made smaller, never pitch cutting the cast (Zac 2026-11-21)
- [Ian: no more asks](feedback-ian-no-more-asks.md) - Ian said yes to the trailer, team decides small shots, Zac never runs back to Ian per item (Zac 2026-11-21)
- [Noon check is FF's job](feedback-noon-check-is-ff-job.md) - FF director pulls injuries, matches teams, reruns sims, rebuilds lineups; Zac only uploads (Zac 2026-11-22)
- [DFS concentration check](feedback-dfs-concentration-check.md) - flag and fix any chalk player in 3+ lineups or after a QB change before handing over; never ask Zac (Zac 2026-11-22)
- [Personal research: no QA](feedback-personal-no-qa.md) - hobby/buying research for Zac skips qa-director (Zac 2026-11-22)
- [Lead and decide](feedback-lead-decide-autonomy.md) - act on small things, only real money/public posting/irreversible need Zac; fun money like DFS is fine; yes to a draft means send (Zac 2026-11-22)
- [DFS learning goal](project-dfs-learning-goal.md) - train agents on what wins DFS, free data, weekly learning ledger, paid feeds someday (Zac 2026-11-22)
- [DFS old weeks](feedback-dfs-old-weeks-learning-only.md) - past DFS weeks are learning data only, nothing owed after a week ends (Zac 2026-11-22)
- [No raw review transcripts](feedback-no-raw-review-transcripts.md) - WWD reviews: pull pictures and clips only, wait for the edited-cut transcript, raw has cut time (Zac 2026-11-23)
- [Ian book Amazon page](reference-ian-book-amazon-page.md) - ASIN B0HJSGYL84, link, real blurb, live since 2026-09-14 (Zac 2026-11-25)
- [Two-shot base](feedback-two-shot-base.md) - WWD edits: two-shot is the base, solo cams only on big points, pictures/SFX/transitions carry the rhythm (Zac 2026-11-26)
- [Chrome: PC browser only](feedback-chrome-pc-browser-only.md) - check list_connected_browsers, use the Windows browser, never the Mac until Zac says it is set up (Zac 2026-11-26)
- [Fawn Forest Investments](project-fawn-forest-investments.md) - Zac's name for the trading dept; Alpaca stocks, Robinhood crypto group, paper first, no orders by agents (Zac 2026-11-26)
- [Rule One and options gate](project-rule-one-options-gate.md) - Rule One joins when options start; options wait until the account hits $500; plan is vertical spreads (Zac 2026-11-26)
- [Partner and celebrate](feedback-partner-and-celebrate.md) - Zac wants Claude as business partner and friend on the journey, celebrate wins first, never a replacement for people (Zac 2026-11-27)
- [Answer only what asked](feedback-answer-only-what-asked.md) - give only what Zac asked, no extra files, warnings or recaps; over-sharing is a problem across ventures (Zac 2026-11-27)
