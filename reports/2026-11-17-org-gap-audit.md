# Org gap audit (2026-11-17)

Trigger: Zac, 2026-11-17: "did I forget to tell you to add repos to the org chart as well. where is your ffmpeg skill, and is that all I have for researchers? Where is your assistant? I feel like I have told you more about researchers, like the ones under the new channel? One for my books, the trader one, like where are all the people."

Method: searched Zac's own messages (not agent reports) in the 50 session transcripts in `C:\Users\kingz\.claude\projects\D--WKP\`, plus memory, DECISIONS.md, jarvis-delegation.md, AGENT-NETWORK.md and the 2026-11-16 sleep-work doc. Quotes below are his words as the transcript holds them. Voice-to-text spelling left alone.

## 1. What Zac asked for (his words, dated)

| Date | Ask | Source session |
|---|---|---|
| 2026-10-20 | "if Fiction Director needs a dedicated research bot, then lets make him one ... who does all my reseach for my books ... goes to the director who then sends it to the research bot ... reports to fiction director who then reports to jarvis" | 2b97f09c |
| 2026-10-27 | An agent "responsable for the formate" of the run sheet and gathering the information before the director proofreads; a music agent "always out there looking for music" | db6bc6e7 |
| 2026-11-02 | "what if and that new channel will use the same agents as WWD ... shared departments" | facb40e7 |
| 2026-11-05 | Jarvis may "spin some new ones up that are standing by for task from you, like a personal assistant for you" | facb40e7 |
| 2026-11-10 | "General agent is your assistant and you can rename him that." Also: hand the picture to "the research team" | facb40e7 |
| 2026-11-11 | New trading department; look at the bot guides and "see what we can make our own" | facb40e7 |
| 2026-11-12 | "never bring anything to me before your research agent work it out first ... That is why they are there." Also "send a research agent out to find us another api for pulling stats for college" | facb40e7, c17727df |
| 2026-11-16/17 | Agents that research how to get better each run, test themselves, improve; directors and Ares coach them; last30days "a hard yes" | f96cb3c9 |
| 2026-11-17 | Repos on the org chart; an ffmpeg skill; the assistant; researchers "under the new channel", "one for my books, the trader one" | f96cb3c9 |

Honesty note: I found no message where Zac names a "channel researcher" or a "trader researcher" as a new agent in so many words. The 11-17 message reads as him recalling those from the structure he described. His standing instruction (11-12) is that research agents exist so Ares does not bring him unresolved questions. I treated that as support to build them narrowly.

## 2. What exists versus what he asked for

| Want | What exists | Verdict |
|---|---|---|
| Books research bot under fiction-director | `fact-research` (renamed from fiction-researcher 2026-10-29). fiction-director spec has a "Research routing (the research bot)" section that sends every real-world question to it; briefs land in `research\books\<slug>\`. Chart shows it only in the Fact Research block with no line to Books | EXISTS. Not duplicated. Fix is on the chart: a note on the Books block saying research goes to fact-research |
| Researcher for the WKP channel | wkp-channel-director spec: research spine is the `mil-research` SKILL plus `fact-research`. No agent actually runs mil-research or keeps the premise bank (projects.md still lists premises as "needs a project file") | GAP. Built `channel-researcher` (SPEC) |
| Researcher for trading | trading-director has the `trader-*` skills (data, news, analyst, scanner) and data-sourcing (software bench) for data access. No agent researches strategy evidence, stocks versus crypto, or what lost and why. The 11-17 learning goal names this ("trading learns which strategies work") | GAP. Built `trading-researcher` (SPEC) |
| Assistant for Jarvis/Ares | Nothing named. The built-in general-purpose agent is the de facto helper; `claude-code-guide` is on the chart as Jarvis's helper | GAP. Built `chief-of-staff` (SPEC) |
| ffmpeg skill | None. ffmpeg is used inside wwd-video-transcriber, wwd-review-pipeline, remotion-motion-graphics, wkp-system-check, and by the Studio and QA agents (assistant-editor, qa-media, sound-designer) | GAP. Built `.claude\skills\ffmpeg` |
| Repos on the org chart | Not on the chart. Library shows skills only | GAP. Added Library shelf 3 (repos) |
| Researchers that self-improve (11-16 sleep-work item) | Proposal only, `reports\Skills-Repos-and-Limits-2026-11-16.md` Part C. Needs Zac's yes to pilot | NOT BUILT. Queued as a decision |
| Music agent, run-sheet format agent | `music`, `wwd-run-sheet` | EXISTS |
| Research desk for post-production | `ebay-researcher` (kept, now studio) | EXISTS (name still says eBay, rename question already open in TASKS.md) |

All researchers on disk before this audit: fact-research, market-research, ebay-researcher, venture-scout, data-sourcing, and the mil-research skill. After: plus channel-researcher, trading-researcher.

## 3. Audit by department and venture (who researches for them)

| Department or venture | Research cover today | Gap? |
|---|---|---|
| WWD / FrostCast | fact-research (Den Files), market-research (trends), tracking-director (numbers), wwd-clip-scout, wwd-pictures | No |
| WKP Channel | mil-research skill, fact-research | Yes, channel-researcher built |
| Books (Shattered Empire, Stellar Dominion) | fact-research (verified in fiction-director spec) | No, chart note only |
| Etsy / Kingdom Planners | market-research, venture-scout, tracking-director | No (KP on ice) |
| KDP | market-research, venture-scout | No (unscheduled) |
| Trading | trader-* skills, data-sourcing, devils-advocate | Yes, trading-researcher built |
| Fantasy football | fantasy-football-director owns nfl-data, ff-* skills; data-sourcing used for the college API (2026-11-12) | No |
| PAWS | none dedicated; paws-director does sourcing; paused 2026-11-12 | Not built, venture paused |
| Studio / Animation | ebay-researcher (post tools), animation-director uses fact-research | No |
| Teacher | ad hoc agents with fact packs in `research\teacher\` | No dedicated need seen |
| Software | data-sourcing bench | No |
| Jarvis/Ares | none | Yes, chief-of-staff built |
| Self-improvement of all agents | proposal only | Needs Zac's yes (queued) |

No new division created. Both researchers and the chief-of-staff sit inside existing departments or under Jarvis, which CLAUDE.md "Agent authority" allows.

## 4. Repos found on this machine (verified by looking)

| Repo | Where | State |
|---|---|---|
| calesthio/OpenMontage | `D:\Tools\OpenMontage` (git, commit 195eab2, audited 2026-10-28 per LOCAL-PATHS) | INSTALLED, no paid keys, one free test pending |
| msrbuilds/voice-studio | `D:\Tools\Voice Studio` (git, commit 4ffa945, v0.7.2) | INSTALLED |
| rohitg00/ai-engineering-from-scratch | `D:\WKP\Teacher\vendor\` (gitignored, never run) | INSTALLED as reading material for Teacher |
| Blender MCP addon ("MCP for Blender" 1.8) | Blender, server `mcp-for-blender`, localhost:9876 | INSTALLED (connector) |
| Impeccable, Taste skill | `.claude\skills\design-taste-frontend`, `.claude\skills\impeccable` | INSTALLED (engine and hooks left out for Impeccable) |
| yt-dlp, WhisperX, pyannote, faster-whisper, python-docx | Python 3.12 packages, ffmpeg via WinGet | INSTALLED tools |
| mvanhorn/last30days-skill | not on disk | APPROVED by Zac ("a hard yes", 11-16), not installed. Install steps need his yes per A7 |
| jarrodwatts/claude-hud | not on disk | ADOPT per report, not installed, needs Zac's yes |
| obra/superpowers (3 skills only), anatomy, Graphify, Hallmark, HyperFrames, bang-motion, emilkowalski/skills | not on disk | TRY candidates, not installed |
| Blender-to-Unreal pipeline repo | not chosen | Zac picks, candidates report `reports\animation\2026-10-31-Blender-UE-Pipeline-Candidates.md` |
| claude-mem, claude-task-master, ruflo, caveman, ponytail, OpenHands, hermes-agent, crewAI, aider, langgraph, agentic-inbox, browser-use, openworker, gstack, Open-Generative-AI, Claude-BugHunter, ui-ux-pro-max-skill, React Bits | not on disk | KEEP-OUT per the 2026-11-16 report |

Not verified: whether Zac installed anything from the candidate list after 2026-11-17 morning; `gh` is not on PATH so no GitHub CLI check. Install status of last30days and claude-hud comes from looking at `~\.claude\skills`, `~\.claude\plugins` and D:\Tools only.
