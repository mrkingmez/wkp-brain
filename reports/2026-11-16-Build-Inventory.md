# WKP Build Inventory

Date: 2026-11-16. Built from disk and local config, not from memory. Requested by Zac because a pivot may be coming.

How to read this: every claim names its source. "Not available" means the source was missing or unreachable, and the row says what is missing. A log mention is not proof of a run; where a stronger source exists (the `skillUsage` counter in `C:\Users\kingz\.claude.json`, the agent run ledger) it is used and labeled. No secret values were read or printed anywhere in this document.

---

## 0. One-page pivot decision summary

**The honest picture.** Of every venture on disk, exactly one has outside traction: WWD / FrostCast. It has 744 YouTube subscribers, 1,090,874 lifetime views (VidIQ pull 2026-11-13), 120 FrostCast episodes recorded, and a weekly rhythm that has not broken. It earns about $4 a month (Zac, 2026-11-12, his word, no file). Everything else has zero recorded revenue. The build around it (57 skill folders, 51 agents, 6 Windows tasks, 40+ connectors) is far larger than the revenue it supports.

**Ranking by evidence of traction (best first)**

| Rank | Venture | Evidence of traction | Money in / out on record | Call |
|---|---|---|---|---|
| 1 | WWD / FrostCast | 744 subs, 1.09M lifetime views, 120 episodes, weekly output for months. 1 net sub gained in the latest 6-day window, views falling (4,370 prior 7 days, 1,398 latest 6 days, windows not equal). Subscriber loss work in progress. | About $4 a month in. Spend not available (tool and credit costs are not tallied anywhere). | KEEP. Only venture with an audience. Fix growth, do not add features. |
| 2 | Fiverr transcription | Zero jobs recorded. Zac says he has made over $7,000 on Fiverr since 2016 (his word, not verified). System built and tested on a fake job 2026-11-13. | $0 in. $0 spent (free tools). | KEEP, test fast. Cheapest path to the first dollar because demand history is Zac's own. Needs his gig pages, nothing else. |
| 3 | Post-Production / Studio | Zero paying clients. One free job (Ian book trailer, Draft 3.2, about 2,000 Firefly credits spent, two usable shots, Zac told to stop buying runs). Zac names editing his strongest skill. | $0 in. Credit spend not available in dollars. | KEEP as the skill base. Tie it to #1 and #2 (captions, edits) rather than a standalone shop. |
| 4 | Shattered Empire | 234,860-word Book 1, second draft done, with alpha readers. No sales possible yet. | $0 in. $0 out. | KEEP as a personal goal. Not a revenue test. Needs reader feedback, not agents. |
| 5 | WarriorKingDesigns (Etsy) | About 70 listings, 4 lifetime reviews, week ending 2026-08-20: 23 visits, 0 favorites, 0 orders, $0. "No sales in months" (ETSY CLAUDE.md). Manual data pull lapsed after 2026-08-20. | $0 in on record. Etsy fees and Printify costs not available. | PIVOT CANDIDATE. 3 months of listings with no sale. Hold is already set. Decide by a date, not by drift. |
| 6 | KDP Publishing | Zero books published. | $0 / not available. | PAUSE (already). Zac pivoted away 2026-09-01. |
| 7 | Kingdom Planners | Seven finished products, zero listings, Etsy shop never created (blocked on a $29 fee), one product file lost. | $0 in. | PAUSE (already, back burner 2026-11-12). Pipeline far ahead of any proof of demand. |
| 8 | WKP Channel (What If, Hidden Hinge, AAR) | Zero episodes published. One commit (2026-08-30). Three skills and an agent exist. | $0. | PAUSE. All machinery, no product. Revive only if Zac wants it after #1 is growing. |
| 9 | PAWS (Scout hardware) | Zero prototypes, zero firmware. PAWS CLAUDE.md says two Waveshare screens "already ordered", projects.md says "zero parts ordered", cost not available. Scout render looked like a jumble of pixels. | Spend not available. | PAUSE (already). Hardware cost with no demand test. |
| 10 | Teacher | Built and running on the home LAN, four tracks, lessons in draft. Her progress not asked yet. | $0. | KEEP as family use. Not a business, ignore for the pivot. |
| 11 | RUBY TWO (short film) | Production Bible and screenplay exist, nothing produced. | $0. | PAUSE. Learning project. |
| 12 | Spark Capture | Phase 1 scaffold, one commit 2026-09-04, nothing since. | $0. | PAUSE. |
| 13 | Investing | $50 started April 2026, about $60 as of 2026-07-24 (stale, not refreshed). Trading dept built (11 trader skills), watch week never run. | Net about +$10 as of 7/24. | PAUSE. Skills built for a $60 account. |
| 14 | Stellar Dominion (sci-fi novel) | Planning docs only, markups unapplied. | $0. | DORMANT. |
| 15 | Fantasy football | Personal, running weekly, heavy tooling (2 simulators, DFS workflow). Not a venture. | $3 DFS cap (Zac, 2026-11-13). | Personal. Biggest agent-time sink after WWD that is not income. Zac's call. |
| n/a | Cyber Security | Day job, not a venture. CySA+ punted on exam cost. | Day job pay. | Keep as career practice. |

**Three pivot options the evidence supports (a recommendation, Zac decides)**

1. **Double down on WWD plus services built on its skills.** Audience exists. Add the two cheapest revenue tests that use skills already built: Fiverr transcription and captions, and paid edits. Pause everything with zero traction.
2. **Wind down the Etsy POD line.** Three months of live listings, no recorded sale. Either set a hard end date or name one concrete change that could move it. The listing cap expired 2026-11-15, so the constraint that justified the hold is gone and the decision is open. Do not let it drift.
3. **Cut tooling that has no user.** 24 skills and 7 agents have no evidence of ever running (sections 1 and 2). They cost nothing to keep on disk but they inflate how big the system looks and make routing noisier.

**What this inventory could not establish:** total money spent (no ledger exists), per-skill spend, whether any connector costs a monthly fee, current Etsy numbers (manual pull lapsed 2026-08-20), WWD revenue beyond Zac's word.

---

## 1. Skills

### 1a. Project skills in `D:\WKP\.claude\skills` (57 folders)

Counts by verdict: 11 used with an authoritative invoke count, 8 used by log evidence only, 2 installed for Teacher design work, 24 never used, 3 mentioned with no run record, 3 weak evidence, plus retired, test, used-once, never-run and 2 folders that are not skills.

Evidence sources: (a) `skillUsage` in `C:\Users\kingz\.claude.json`, which counts Skill-tool invocations only, so scheduled `claude -p` runs and subagent reads may not show; (b) a text scan of logs, reports, memory, research and venture folders for the skill name, excluding the skill's own folder. Treat (b) as a hint.

| Skill | What it was for | Verdict | Evidence |
|---|---|---|---|
| .claude | not available | Not a skill | Stray nested folder inside skills, no SKILL.md. Check and delete. |
| aar-format | AAR Commander | Never used | Format C of the WKP Channel, which has zero episodes. Pause with the channel. |
| blender-asset-quality | The quality standard every finished Blender asset must meet before it leaves the Blender section of the Animation department | Never used | No mention in logs, reports, memory or research. |
| blender-asset-sourcing | How the asset-scout agent finds existing 3D models, textures and HDRIs properly for Zac's Animation department, and records exactly what license each ... | Never used | No mention in logs, reports, memory or research. |
| blender-character-craft | How to build good characters and creatures in Blender for Zac's Animation department | Used (log evidence) | 3 files mention it, latest 2026-11-13 in logs/animation-director.md. Not in skillUsage, so mention evidence only. |
| blender-mcp-ops | How to drive Zac's live Blender safely and well through the blender MCP tools (get_addon_status, get_scene_info, execute_blender_code, look, search_as... | Used (log evidence) | 3 files mention it, latest 2026-11-13 in research/animation/2026-11-13-version-tags-and-delta-sheets.md. Not in skillUsage, so mention evidence only. |
| blender-planar-head-modeling | Planar (block-plane) head modeling in Blender from a plaster-style planar reference, the viewport settings that make flat planes readable (Cavity, Aut... | Used (log evidence) | 3 files mention it, latest 2026-11-13 in logs/animation-director.md. Not in skillUsage, so mention evidence only. |
| canary | Test skill | Test only | Test skill, one invoke 2026-08-19. Safe to delete. |
| design-taste-frontend | tasteskill 2.5.1, the anti-slop frontend skill | Installed, used by Teacher | Taste skill, mentioned in 2026-11-15 ledger rows for Teacher and dashboard design work. |
| fantasy-football-data | Pulls live data for Zac's IRFL dynasty league and pick'em pool , MFL roster/player exports and current NFL/CFB odds | Used (invoke count) | skillUsage: 1 invokes, last 2026-09-15. |
| ff-play-sim | Play-by-play NFL game simulator for Zac's fantasy football (built 2026-10-22) | Used (log evidence) | 19 files mention it, latest 2026-11-16 in logs/system-check/2026-11-16.md. Not in skillUsage, so mention evidence only. |
| ff-simulator | Monte Carlo simulator for Zac's IRFL lineup and the weekly pick'em card | Used (log evidence) | 28 files mention it, latest 2026-11-16 in logs/DECISIONS.md. Not in skillUsage, so mention evidence only. |
| fiction-alpha-feedback | Turns alpha reader feedback into a canon-checked decision worksheet, grouped by chapter, showing which readers flagged what and whether it conflicts w... | Weak evidence | 2 mention(s), latest 2026-11-12. A mention is not proof of a run. |
| hiddenhinge-format | Format B. The battle everyone credits versus the lesser known engagement that carried the actual causal weight | Never used | Format B, zero episodes made. Pause with the channel. |
| impeccable | Use to design, redesign, critique, audit, polish or animate a frontend: websites, landing pages, dashboards, app UI, components, native iOS/Android sc... | Installed, used by Teacher | Same as design-taste-frontend, 55 files. |
| jarvis | WKP command layer | Used (invoke count) | skillUsage: 10 invokes, last 2026-11-16. |
| kp-generator | Builds the spreadsheet itself - tab structure, formula blocks, validation rules | Never used | Kingdom Planners on ice. Only descriptive mentions. |
| kp-ledger | Tracks Kingdom Planners sales and revenue | Never used | KP has zero listings, nothing to track. |
| kp-planner | Weekly listing batch scheduler for Kingdom Planners | Never used | KP on ice. |
| kp-prep | Builds the eight-image photo set for a Kingdom Planners listing | Never used | KP on ice. Photo set never built per Kingdom-Planners CLAUDE.md. |
| kp-recon | Finds Kingdom Planners product gaps by reading Etsy autocomplete and REVIEW TEXT in military and veteran planner categories | Never used | KP on ice. |
| kp-reviews | Monitors and drafts responses to Kingdom Planners reviews | Never used | KP has no shop, no reviews. |
| mil-research | The WKP military history research standard | Never used | Shared research spine for the three formats, no run record. |
| nfl-data | Shared nflverse data layer , play-by-play, team/player stats, schedules with betting lines, cross-platform player ID mappings, and PFR advanced stats | Used (log evidence) | 9 files mention it, latest 2026-11-13 in data/weekly-2026-11-13.md. Not in skillUsage, so mention evidence only. |
| no-ai-slop | Content-quality gate for anything WKP publishes publicly - social posts, video titles/descriptions, sponsor reads, Etsy listings, thumbnails, pinned c... | Used (invoke count) | skillUsage: 7 invokes, last 2026-11-11. |
| remotion-motion-graphics | Create and edit professional motion graphics videos with Remotion (React-based video) | Never used | Appears only in a tool research batch. |
| task-observer | Monitors task execution for skill improvement opportunities: logs patterns, user corrections and methodology worth preserving to the workspace, turns ... | Never run | Weekly review is required by root CLAUDE.md, no observation-log run found on disk. |
| trader-alerts | Price Alerts | Never used | Trading dept: watch week not run, no run record. |
| trader-analyst | The Earnings Analyst | Never used | Trading dept: watch week not run, no run record. |
| trader-broker | Order Executor | Never used | Trading dept: watch week not run, no run record. |
| trader-budget | Budget Manager | Never used | Trading dept: watch week not run, no run record. |
| trader-entry | Entry Timer | Never used | Trading dept: watch week not run, no run record. |
| trader-exit | Exit Planner | Never used | Trading dept: watch week not run, no run record. |
| trader-news | News Monitor | Never used | Trading dept: watch week not run, no run record. |
| trader-pelosi | The Pelosi Tracker | Never used | Trading dept: watch week not run, no run record. |
| trader-risk | Risk Manager | Never used | Trading dept: watch week not run, no run record. |
| trader-scanner | Chart Scanner | Never used | Trading dept: watch week not run, no run record. |
| trader-timemachine | Time Machine | Never used | Trading dept: watch week not run, no run record. |
| tuesday-intell-tool | not available | Not a skill | Empty folder, no SKILL.md. Safe to delete. |
| ue-import-pipeline | How to move assets from Blender 5.x into Unreal Engine 5.8 correctly | Used (log evidence) | 4 files mention it, latest 2026-11-13 in research/animation/2026-11-13-version-tags-and-delta-sheets.md. Not in skillUsage, so mention evidence only. |
| ue-mcp-and-automation | How Claude can drive Unreal Engine 5.8 the way it drives Blender | Weak evidence | 2 mention(s), latest 2026-11-13. A mention is not proof of a run. |
| ue-scene-lighting-render | How to create, light, shoot and render scenes in Unreal Engine 5.8 on an 8 GB RTX 5060 and get the best final image | Weak evidence | 2 mention(s), latest 2026-11-13. A mention is not proof of a run. |
| whatif-format | Format A. A single major event that changed the world, run through a nine-step weighted predictive branch model | Never used | Format A, zero episodes made. Pause with the channel. |
| wkd-weekly-batch | Weekly automated report for WarriorKingDesigns - what should post this week, within the shared cap, based on what's actually ready on disk, plus draft... | Mentioned, no run record | Etsy WKD on hold, only system-check output mentions it. Not in skillUsage. |
| wkp-daily-brief | RETIRED 2026-11-12 (Zac, no more daily briefs; only the Monday brief and the Saturday wrap remain) | Retired | 43 invokes, last 2026-11-12, retired by Zac. Windows task still enabled (section 5). |
| wkp-monday-brief | The full WKP weekly brief | Used (invoke count) | skillUsage: 10 invokes, last 2026-11-02. |
| wkp-saturday-wrap | The Saturday week-wrap (added 2026-11-12, replaces the daily brief) | Used (invoke count) | skillUsage: 1 invokes, last 2026-11-14. |
| wkp-system-check | SYSTEM CHECK (read-only checks plus a tiny allowlisted SAFE FIXES tier, dry-run by default) of Zac's machine (and later other machines) | Used (log evidence) | 12 files mention it, latest 2026-11-16 in logs/system-check/2026-11-16.md. Not in skillUsage, so mention evidence only. |
| wkp-update | Interactive check-in session - pulls every open task and open decision across all ventures, reads them back one venture at a time, and writes Zac's sp... | Used once | One invoke 2026-09-04, no log trace since. |
| wwd-audio-cut | Turns a diarized FrostCast transcript into a cut document | Used (invoke count) | skillUsage: 7 invokes, last 2026-11-04. |
| wwd-broll-prep | Takes a folder of mixed-source still images (screenshots, movie posters, newspaper clippings, Google Images grabs, archive photos) gathered for a Den ... | Mentioned, no run record | Last mention 2026-10-31. Photo-pull skill covers the same job. |
| wwd-frostcast-chapters | Turns a diarized, timestamped transcript into a YouTube chapter list | Used (invoke count) | skillUsage: 4 invokes, last 2026-11-04. |
| wwd-review-photo-pull | Pulls the standard 18-picture set (exactly 1 movie poster + 17 real film stills, cast photos kept to a minimum) for a WWD review video, drops it in a ... | Used (invoke count) | skillUsage: 5 invokes, last 2026-11-09. |
| wwd-review-pipeline | End-to-end Winter Wolf's Den review video pipeline | Used (invoke count) | skillUsage: 4 invokes, last 2026-10-23. |
| wwd-show-prep | Turns Matt's photographed topic list into a per-topic prep sheet for FrostCast | Used (invoke count) | skillUsage: 6 invokes, last 2026-10-27. |
| wwd-video-transcriber | Pulls a video file off Zac's local machine, extracts audio, and produces a fully diarized transcript with speakers auto-mapped to Matt/Winter Wolf, Za... | Used (invoke count) | skillUsage: 2 invokes, last 2026-08-19. |
| wwd-vidiq-pull | Weekly VidIQ analytics pull for Winter Wolf's Den | Mentioned, no run record | Last mention Sept 2026 Monday brief. Weekly pull now runs via tracking-director. |

### 1b. User-level skills in `C:\Users\kingz\.claude\skills`

| Skill | What it was for | Verdict | Evidence |
|---|---|---|---|
| wwd-weekly-planner | Weekly WWD production build: calendar sync, release priority, week folder, one Word package. Only exists at user level, not in the repo. | Used (invoke count) | 2 invokes, last 2026-09-01. File dated 2026-08-11. Not in git, so not backed up by the repo. |
| synced (account-synced set, about 40 folders) | Anthropic account skills synced from claude.ai (analytics-dashboard, docx, pdf, pptx, xlsx, deep-research, stop-slop, post-writer, reels-scripting, youtube-thumbnail, wwd-shorts-clip-factory, wwd-video-upload-package, wwd-video-transcriber, listing-factory-weekly-batch-skill, and others). | Mostly never used | Only `anthropic-skills:wwd-video-transcriber` has a count (2 invokes, last 2026-08-19, superseded by the repo copy). The other synced skills have no count. |

### 1c. Plugin skills (installed with plugins)

From the `pluginUsage` block in `C:\Users\kingz\.claude.json`.

| Plugin | Approx. skills | Evidence of use |
|---|---|---|
| small-business | about 50 | 3 uses recorded (last 2026-10-31). No WKP log mentions a small-business skill by name. |
| carta-investors | about 25 | Counter shows 1,671 uses (synced) and 149 (inline), last 2026-11-16. This number is not believable for a solo creator and no WKP file mentions Carta. Counter not verified, cause not available. |
| adobe-for-creativity | about 15 | 1 use (the `/adobe` tour, 2026-10-20). The Adobe connector itself needs authentication (section 3). |
| product-management, sp-global, productivity, cowork-plugin-management, desktop-commander | various | 0 recorded uses each. |
| built-ins (agents-md, telemetry, plugin-authoring, plugin-diff, privacy) | 5 | 0 uses. |

Also invoked from outside the WKP folders: the built-in `loop` (28 uses, last 2026-09-25), `schedule` (2 uses, 2026-10-05), `claude-in-chrome` (3 uses, 2026-10-22), `artifact-capabilities` and `artifact-design` (1 each, 2026-09-10).

### 1d. Duplicates and strays found

- `wwd-video-transcriber` exists in three places: `D:\WKP\.claude\skills\`, `D:\WKP\skills\wwd-video-transcriber\` (old copy from Downloads, git history shows the `skills` folder was last touched 2026-08-22), and the synced account copy. The repo `.claude` one is the live one (CLAUDE.md points at its scripts).
- `wkd-weekly-batch` (repo) and `anthropic-skills:listing-factory-weekly-batch-skill` (synced) do the same Etsy job. Memory notes this was "built in a web session, never moved into the repo".
- `D:\WKP\.claude\skills\.claude` (nested stray folder) and `tuesday-intell-tool` (empty) are not skills.
- Five briefing and planning skills overlap in purpose: `wkp-daily-brief` (retired), `wkp-monday-brief`, `wkp-saturday-wrap`, `wkp-update`, `wwd-weekly-planner`.

---

## 2. Agents (51 in `D:\WKP\.claude\agents`)

Evidence of runs: the ledger `logs\agent-runs.md` started 2026-11-12 and has 43 lines, so almost no earlier work appears in it. Many directors keep their own log in `logs\<name>.md`, which counts as a run record. The earlier 2026-10-29 audit is in `D:\WKP Reports\Agent Audit\`. "Mention only" means the name appears in a log, report or memory file, which shows a director was named, not that it ran.

Counts: 16 with a run record, 28 mention only, 7 with no evidence of any run.

| Agent | Department | Run record | Mentions on disk | Status |
|---|---|---|---|---|
| animation-director | Animation (boss) | 2 ledger row(s) | 15 files, latest 2026-11-16 | Run record |
| blender-asset-scout | Animation | none | 4 files, latest 2026-11-13 | Mention only |
| blender-builder-characters | Animation | none | 3 files, specs only | No evidence of any run |
| blender-builder-props | Animation | none | 3 files, specs only | No evidence of any run |
| clearance | Writing room | no ledger row, own log logs/clearance.md | 72 files, latest 2026-11-16 | Run record |
| copywriting | Writing room | none | 50 files, latest 2026-11-12 | Mention only |
| data-sourcing | Software | none | 5 files, latest 2026-11-12 | Mention only |
| devils-advocate | Shared gate | none | 34 files, latest 2026-11-13 | Mention only |
| dialogue-doctor | Writing room | 1 ledger row(s) | 31 files, latest 2026-11-15 | Run record |
| ebay-researcher | Studio research desk | none | 3 files, latest 2026-10-29 | Mention only |
| etsy-director | Venture director | no ledger row, own log logs/etsy-director.md | 17 files, latest 2026-11-12 | Run record |
| fact-research | Shared research | 2 ledger row(s) | 20 files, latest 2026-11-16 | Run record |
| fantasy-football-director | Venture director | 3 ledger row(s) | 13 files, latest 2026-11-16 | Run record |
| fiction-director | Venture director | none | 6 files, latest 2026-11-12 | Mention only |
| graphic-design | Shared design | no ledger row, own log logs/graphic-design.md | 24 files, latest 2026-11-12 | Run record |
| kdp-director | Venture director | none | 5 files, latest 2026-11-12 | Mention only |
| market-research | Marketing / research | 3 ledger row(s) | 21 files, latest 2026-11-16 | Run record |
| marketing-director | Marketing (boss) | no ledger row, own log logs/marketing-director.md | 76 files, latest 2026-11-16 | Run record |
| military-scifi-director | Venture director | none | 4 files, latest 2026-11-12 | Mention only |
| music | Shared music | no ledger row, own log logs/music.md | 108 files, latest 2026-11-15 | Run record |
| originality | Writing room | none | 57 files, latest 2026-11-16 | Mention only |
| paws-director | Venture director | none | 6 files, latest 2026-11-12 | Mention only |
| qa-auditor | QA | none | 5 files, latest 2026-11-12 | Mention only |
| qa-claims | QA | none | 2 files, latest 2026-11-13 | Mention only |
| qa-director | QA (boss) | 3 ledger row(s) | 25 files, latest 2026-11-16 | Run record |
| qa-documents | QA | none | 1 files, specs only | No evidence of any run |
| qa-media | QA | none | 1 files, specs only | No evidence of any run |
| room-writer | Writing room | none | 21 files, latest 2026-11-13 | Mention only |
| script-room | Writing room (boss) | 10 ledger row(s) | 58 files, latest 2026-11-15 | Run record |
| shattered-empire-director | Venture director | none | 6 files, latest 2026-11-12 | Mention only |
| social-media | Marketing | none | 25 files, latest 2026-11-12 | Mention only |
| software-architect | Software | none | 1 files, specs only | No evidence of any run |
| software-director | Software (boss) | 8 ledger row(s) | 13 files, latest 2026-11-16 | Run record |
| software-engineer | Software | none | 3 files, latest 2026-11-15 | Mention only |
| software-tester | Software | none | 1 files, specs only | No evidence of any run |
| studio-director | Studio (boss) | no ledger row, own log logs/studio-director.md | 12 files, latest 2026-11-12 | Run record |
| tracking-director | Tracking (boss) | none | 6 files, latest 2026-11-16 | Mention only |
| trading-director | Venture director | none | 4 files, latest 2026-11-12 | Mention only |
| ue-asset-integrator | Animation | none | 3 files, specs only | No evidence of any run |
| ue-scene-builder | Animation | none | 4 files, latest 2026-11-13 | Mention only |
| venture-scout | New-venture research desk | none | 3 files, latest 2026-11-03 | Mention only |
| video-ugc | Marketing | no ledger row, own log logs/video-ugc.md | 12 files, latest 2026-11-12 | Run record |
| wkp-channel-director | Venture director | none | 3 files, latest 2026-11-12 | Mention only |
| wwd-clip-scout | WWD | none | 6 files, latest 2026-11-12 | Mention only |
| wwd-color | WWD | none | 5 files, latest 2026-11-12 | Mention only |
| wwd-director | WWD (boss) | no ledger row, own log logs/wwd-director.md (52 KB) | 25 files, latest 2026-11-16 | Run record |
| wwd-pictures | WWD | none | 5 files, latest 2026-11-12 | Mention only |
| wwd-rights | WWD | none | 29 files, latest 2026-11-12 | Mention only |
| wwd-run-sheet | WWD | none | 5 files, latest 2026-11-12 | Mention only |
| wwd-sound | WWD | none | 5 files, latest 2026-11-12 | Mention only |
| wwd-vfx | WWD | none | 20 files, latest 2026-11-16 | Mention only |

Agents with no evidence of ever running (7): see Status column. Of these, `qa-documents` and `qa-media` are QA benches that only qa-director can call, and the QA reports in `logs\qa\` do not name which bench did the work, so "no evidence" here may mean "not logged by name".

Organization (from `AGENT-NETWORK.md` and root CLAUDE.md): Jarvis is the main session acting as CEO. Shared departments open to every director: writing room, marketing, graphic design, music, fact research, market research, tracking, QA, Software, Animation, Studio. Venture directors: wwd, etsy, kdp, paws, fiction, shattered-empire, military-scifi, wkp-channel, fantasy-football, trading.

---

## 3. Connectors and plugins (MCP)

Sources: `C:\Users\kingz\.claude.json` (global and project `mcpServers`, `claudeAiMcpEverConnected`, `mcpNeedsAuthNoticed`), `C:\Users\kingz\.claude\mcp-needs-auth-cache.json`, and the tool list this session exposed. There is no `.mcp.json` anywhere under `D:\WKP`. "Connected" means the server exposed working tools in this session. Live probing of each connector was not run (none were called), so "connected" is "tools present", not "tested today".

### 3a. Connected

| Connector | Type | What it is for in WKP | Evidence of use |
|---|---|---|---|
| blender (`mcp-for-blender`, via uvx) | Local stdio, user scope | Drive Blender for the Animation dept | Mentioned in 8 files. One agent run on 2026-11-13 noted the link was DOWN. |
| espn (npx) | Local stdio, project scope D:/WKP | Scores and schedules for fantasy and CFB | 69 files mention ESPN; scheduled snapshot tasks exist but have never run (section 5). |
| claude-in-chrome | Browser extension | Facebook Messenger transcript send, site pulls | 3 skill invokes, last 2026-10-22; 5 file mentions. |
| claude.ai VidIQ | Account connector | YouTube numbers, tags, competitor data | Heaviest real use: 51 file mentions, latest 2026-11-16. Weekly pull for WWD. |
| claude.ai OpusClip | Account connector | Shorts from FrostCast episodes (scheduling uses the REST API, not the connector, per CLAUDE.md) | 30 mentions, latest 2026-11-16. |
| claude.ai Gmail | Account connector | Mail reads and drafts | 30 mentions, latest 2026-11-16. |
| claude.ai Google Calendar | Account connector | WWD calendar | 12 mentions, latest 2026-11-16. |
| claude.ai Composio | Account connector | Facebook and Instagram pulls | 12 mentions, latest 2026-11-13. Note on file: the Composio Facebook API cannot send a local file. |
| claude.ai Higgsfield | Account connector | AI video and image generation | 31 mentions, latest 2026-11-13. Balance check allowed in settings. Memory says 0 credits, dormant. |
| claude.ai ElevenLabs (entry 1) | Account connector | Voices, image, video generation | 18 mentions, latest 2026-11-10 (research). |
| claude.ai ElevenLabs (3) (entry 3) | Account connector | Same tools as entry 1 | Duplicate, see 3c. |
| claude.ai OpenWhisper | Account connector | Dictation notes and transcription | 3 mentions, latest 2026-11-03. Local OpenWhispr app is the working one. |
| claude.ai Claude Docs | Account connector | Docs for sharing | Zero WKP file mentions. |
| plugin desktop-commander | Plugin | Local file and process tools | 1 mention (2026-10-12). Overlaps Claude Code's own tools. |
| plugin small-business: google-drive | Plugin | Drive file tools | Drive is reference-only per CLAUDE.md (never for operational files). |
| plugin small-business: shopify | Plugin | Shopify store tools | Tools exposed; 2 research mentions. No store on record. |

### 3b. Installed but not authenticated (tools are only an `authenticate` stub)

From `mcpNeedsAuthNoticed` and the session tool list. None has any WKP use on record.

- Adobe for creativity plugin (`Adobe`) and the older `Adobe for creativity` claude.ai entry. Note: Adobe is OFF LIMITS for startup and task changes (memory), but the connector itself is simply unauthenticated.
- product-management plugin: amplitude, amplitude-eu, atlassian, clickup, figma, fireflies, intercom, linear, pendo, similarweb (also slack, asana, monday, notion in the notice list).
- small-business plugin: airwallex, apollo-io, atlassian, canva, clay, emergent, expensify, gusto, intuit-mailchimp, intuit-quickbooks, monday-com, myob, notion, paypal, ramp, ringex-chat, slack, square, stripe, tiktok, trello, wix, zapier, zoho-books, zoho-crm, zoho-desk, zoho-projects (plus docusign, hubspot, xero, zoom in the notice list).
- sp-global plugin: spglobal.
- claude.ai ElevenLabs (2) (entry 2): authenticate and complete_authentication stubs only.
- `mcp-needs-auth-cache.json` currently lists three: `adobe-for-creativity:Adobe`, `small-business:intuit-mailchimp`, `small-business:intuit-quickbooks`.

About 55 plugin connectors are installed and unauthenticated. They arrived with plugin bundles; none was set up for WKP.

### 3c. Duplicates and overlaps

| Duplicate | Entries | Note |
|---|---|---|
| ElevenLabs | Three claude.ai entries: `ElevenLabs`, `ElevenLabs (2)` (needs auth), `ElevenLabs (3)` (connected, identical tool set to entry 1) | Keep one. Entries 1 and 3 expose the same tools, which doubles the tool noise. Entry 2 is a dead stub. Whether they point at one account or two is not available. |
| Google Drive | claude.ai Google Drive (in `everConnected`, tools not exposed this session) and plugin small-business google-drive | One is enough, and Drive is reference-only. |
| Adobe | claude.ai "Adobe for creativity" and plugin `Adobe` | Both unauthenticated. |
| Atlassian, Amplitude, Notion, Slack, Monday, Zapier | Appear in both product-management and small-business bundles | Neither authenticated. Zapier was once connected (`everConnected`) and is gone. |
| Voice and transcription | OpenWhisper connector, local OpenWhispr app, local WhisperX transcriber | Only the local pipeline is in the Wednesday chain. |

### 3d. Non-MCP services referenced (not connectors)

Opus Clip REST API (key in env), VidIQ, Suno, Adobe Firefly (Veo 3.1 inside it), Printify, Etsy, Payhip (test not run), Fiverr, Amazon Associates (joined 2026-11-12, tracking ID not sent), Surfshark affiliate. Costs for these are not recorded in one place.

---

## 4. Ventures

Source for each row: the venture's CLAUDE.md, git history for the folder (`git log`), `TASKS.md`, `logs\DECISIONS.md`, and `data\`. Git commit counts show how much work landed in the repo, not output quality.

| Venture | Folder (files, commits, last commit) | State | Believed purpose | Money in / out on record | Call and one-line reason |
|---|---|---|---|---|---|
| WWD / FrostCast | `WWD\` (100 files, 35 commits, 2026-11-12) | ACTIVE. Weekly FrostCast, reviews, shorts via Opus, EP 120 done 2026-11-11, Vision Quest EP 8 and Godzilla Minus Zero in the queue. Run with Matt, LLC is Matt's. | Nerd-verse reviews and weekly podcast with Matt, the one collaborative venture. | In: about $4 a month (Zac's word). Out: not available. | KEEP. Only audience on disk. |
| Etsy WarriorKingDesigns | `ETSY\` (7 files, 11 commits, 2026-11-01) | On hold. About 70 listings, listing cap lapsed 2026-11-15, manual data lapsed 2026-08-20. | AI-art puzzles and wall art, priority 1 in ME.md. | In: $0 in the one weekly file, "no sales in months". Out: not available. | PIVOT CANDIDATE. Never converted traffic to a sale. |
| Kingdom Planners | `Kingdom-Planners\` (3 files, 5 commits, 2026-11-10); xlsx in `D:\05 Kingdom Planners\` | Back burner (Zac 2026-11-12). Seven products on paper, one file lost, shop not created, $29 blocking. | Digital spreadsheet planners on Etsy, veteran and budget buyers. | $0 in. | PAUSE. No demand test ever run. |
| KDP Publishing | `KDP\` (4 files, 2 commits, 2026-11-12) | Active-unscheduled. Zero books. Uses Zac's wife's paid BowesPaz Elite apps. | Math-mystery workbooks (Genten Royalty) and sudoku mysteries (Shigai). | $0. | PAUSE. Zac pivoted away 2026-09-01. |
| Shattered Empire | `Shattered-Empire\` (271 files, 6 commits, 2026-11-11); canon at `D:\The Shaterred Empire Series` | ACTIVE. Book 1 draft 2 with readers. Third edit and queries next. | Fantasy series, Zac's novel. | $0. | KEEP (personal goal). |
| Stellar Dominion | `SCI-FI Novel\` (1 file, 2 commits, 2026-10-07); files `D:\Stellar Dominion` | Dormant. Planning documents, markups not applied. | Military sci-fi novel after Book 1. | $0. | DORMANT. |
| WKP Channel | `WKP-CHANNEL\` (7 files, 1 commit, 2026-08-30) | Active-unscheduled. Frameworks and models only. | What If, Hidden Hinge, AAR Commander military history videos. | $0 (Zac: "$0 WKP"). | PAUSE. No episode exists. |
| Post-Production / Studio | `Post-Production\` (70 files, 11 commits, 2026-11-15) | Active in practice. Ian trailer Draft 3.2 is the only job (free, friend). | Editing, sound, motion graphics service, sports highlight niche. | $0 in. Out: about 2,000 Firefly credits (dollars not available). | KEEP. Strongest skill, link it to paid work. |
| Transcription (Fiverr) | `Transcription\` (15 files, 1 commit, 2026-11-15) | Built 2026-11-13, tested on fake job. No real job. | Four Fiverr gigs: sermons, podcasts, captions, general. | $0 in. $0 out. | KEEP, test. |
| Teacher | `Teacher\` (19,326 files because a vendored repo is cloned inside, 2 commits, 2026-11-15) | Active, family use. Site runs on home LAN only when started. | Course site so Zac's wife learns AI well. | $0. | KEEP (family). |
| PAWS | `PAWS\` (37 files, 7 commits, 2026-11-12) | Paused 2026-11-12. No parts running, interface needs rework. | Scout desk-pet hardware plus USB-C hub. | Spend not available (CLAUDE.md says two screens ordered, projects.md says none; contradiction). | PAUSE. |
| RUBY TWO | `Ruby-One\` (1 file, 2 commits, 2026-09-17) | Pre-production, nothing made. | WWII short film, learning and portfolio. | $0. | PAUSE. |
| Spark Capture | `spark-capture\` (19 files, 1 commit, 2026-09-04) | Phase 1 scaffold only. | Wake-word voice capture Android app. | $0. | PAUSE. |
| Investing | `Investing\` (3 files, 2 commits, 2026-10-22) | Dormant. Trading dept (11 skills, trading-director) built but never run. | $50 swing-trading challenge. | $50 stake, about $60 as of 2026-07-24, not refreshed. | PAUSE. |
| Fantasy football | `Fantasy-Football\` (187 files, 26 commits, 2026-11-15) | Personal, weekly, heaviest non-WWD tooling. | Win IRFL and the pick'em pool. | DFS capped at $3 entries. | Personal, Zac's call. |
| Cyber Security | `Cyber-Security\` (1 file, 3 commits, 2026-11-12) | Day-job reference. CySA+ punted. | Playbook for the day job. | Day job pay. | Not a venture. |
| Animation dept | `ANIMATION\` (12 files, 4 commits, 2026-11-15) | Shared department, built 2026-10-31. Tutorial research and training skills. Blender 5.2.4, Unreal 5.8.4 installed. | 3D assets for any venture. | $0 (free assets only). | PAUSE until a job needs it. No asset delivered to a venture in the logs. |
| Software dept | `software\` (5 files, 1 commit, 2026-11-12) plus `scripts\` | Used for Teacher, Transcription, fantasy dashboard, system-check fixes. | Build tools for any venture. | $0. | KEEP. It actually ships. |
| Trading dept | `.claude\agents\trading-director.md`, 11 `trader-*` skills | Never run. | Paper trading watcher. | $0. | PAUSE with Investing. |

Side items from `TASKS.md`: photo restoration (stop rule 2026-11-13 not recorded as resolved), WWD comic COLD TOW, WWD monetization (vidIQ, OpusClip yes from Matt), King Debt Planner (personal, not in repo), side-business brand kits (names pick, trademark checks owed).

Money: no ledger tracks spend. What is on record: WWD earns about $4 a month, WKP earns $0, Fiverr history over $7,000 since 2016 (Zac), Investing +$10 as of 2026-07-24, Etsy $0 in the last weekly file. Subscription costs of VidIQ, OpusClip, Firefly, Suno, ElevenLabs, Higgsfield, Claude are not recorded in any file, so "money spent" is not available for any venture.

---

## 5. Scheduled tasks, hooks, scripts, environment variables

### 5a. Windows scheduled tasks (read with `Get-ScheduledTask`)

| Task | Runs | Last run | Last result | Note |
|---|---|---|---|---|
| WKP-Monday-Brief | `claude -p "run wkp-monday-brief"`, Mon 05:30 | 2026-11-16 05:30 | 1 (failure code) | A Monday brief file for 2026-11-16 does exist in `reports\monday\`, so it may have partly run. Exit code 1 not explained. |
| WKP-Saturday-Wrap | `scripts\saturday-wrap.bat`, Sat 05:30 | 2026-11-14 05:30 | 1 (failure code) | Same pattern. Registered after Zac's yes. |
| WKP-System-Check | `scripts\nightly-system-check.bat`, daily 23:30 | 2026-11-16 23:30 | 0 | Healthy. Reports in `logs\system-check\`. |
| WKP-daily-brief | `claude -p "run wkp-daily-brief"`, 05:30 | 2026-11-14 05:30 | 0 | Skill is RETIRED but the task is still Ready and next runs 2026-11-17. TASKS.md says it still needs Zac's yes to disable. Spends tokens every run. |
| WKP-ESPN-Snapshot-Wed | `software\cfb-espn-snapshot\espn_snapshot.py`, Wed 15:00 | never | 267011 (never ran) | First run due 2026-11-18. |
| WKP-ESPN-Snapshot-Thu | same script, Thu 09:00 | never | 267011 (never ran) | First run due 2026-11-19. |

Also: `scripts\nightly.bat` (dated 2026-08-21) has no matching task; older rollup leftover.

### 5b. Hooks

No hooks configured in `C:\Users\kingz\.claude\settings.json` or `D:\WKP\.claude\settings*.json`. Git hooks folder has samples only.

### 5c. Settings

User settings: permission mode auto, model sonnet, auto-mode rules describing the repo `github.com/mrkingmez/wkp-brain`. Project settings allow `Agent` and git, ffmpeg and dir commands, deny `rm -rf` and reading `.env`, and add extra directories `L:\`, `E:\Puzzle Art`, `C:\Tools\PCHealth`. Local settings hold a long list of one-off allowed commands from August (transcriber install). `E:\Puzzle Art` and `C:\Tools\PCHealth` may be stale (not checked); LOCAL-PATHS says the PC health suite is at `D:\Tools\PCHealth`.

### 5d. Scripts and batch files in the repo

`scripts\nightly-system-check.bat`, `scripts\saturday-wrap.bat`, `scripts\nightly.bat`; `Fantasy-Football\dfs\sunday_refresh.bat`; `PAWS\sim\Run Scout.bat`; Teacher start and stop bats; skill-owned Python under each `.claude\skills\<name>\scripts\`; Transcription scripts (7); `software\cfb-espn-snapshot`.

### 5e. Environment variable NAMES (user scope; values not read)

`CFBD_API_KEY`, `CLAUDE_CODE_GIT_BASH_PATH`, `EBAY_CLIENT_ID`, `EBAY_CLIENT_SECRET`, `EBAY_ENV`, `EBAY_REFRESH_TOKEN`, `GEMINI_API_KEY`, `HEADROOM_TELEMETRY`, `HF_Token`, `MFL_API_KEY`, `ODDS_API_KEY`, `OPUS_API_KEY`, `SPORTSDATAIO_KEY`, `UE-LocalDataCachePath`, plus two vendor-style names beginning `PRD-` and `ZacharyK-WKPComme-PRD-` (purpose not available). Standard names (Path, TEMP, TMP, OneDrive, OneDriveConsumer) omitted from meaning.

Observations: the EBAY_* set belongs to the archived eBay venture and Zac has not decided whether to remove it. CLAUDE.md says the transcriber reads `HF_TOKEN`, but the user variable is named `HF_Token`; Windows names are case-insensitive so this works, but the spelling differs. No variable was read by value. Machine-scope variables matching key, token or secret patterns: none found.

---

## 6. Findings worth acting on

1. `WKP-daily-brief` task is still enabled for a retired skill. Zac's yes to disable is the only blocker.
2. Monday brief and Saturday wrap scheduled runs both returned exit code 1 on their last run. Cause not available (no run logs were read).
3. The two ESPN snapshot tasks have never run; first runs are this week.
4. ElevenLabs is connected twice (entries 1 and 3) with a third dead stub.
5. About 55 plugin connectors sit unauthenticated; none is used.
6. 24 skills and 7 agents have no evidence of a run. 17 of the 24 are `kp-*` (6) and `trader-*` (11), tied to ventures that are paused.
7. `wwd-weekly-planner` exists only at user level, not in git. If the machine dies it is gone.
8. The agent run ledger began 2026-11-12, so earlier agent work cannot be counted. Per-agent token cost is not available except for ledger rows.
9. `task-observer`'s weekly review has no run on disk, though root CLAUDE.md requires it.
10. PAWS parts: CLAUDE.md and projects.md disagree on whether hardware was ordered.

## 7. What was not verified

Connector auth state was read from config and tool presence, not by calling each connector. No dollar figure for any subscription or credit was found in any file. Etsy and Instagram and Facebook numbers: not available (manual pull lapsed, no connector account). Current Investing balance: not available (last figure 2026-07-24). The 2026-11-16 Monday brief failure cause: not available. Skill "last used" for scheduled runs may be undercounted by `skillUsage`.
