# ARES Dashboard Plan

Date: 2026-11-16. Author: software-director. Status: PLAN plus a static mockup. Nothing built, installed, renamed, deployed or pushed.

Mockup: `D:\WKP\ARES\mockup\index.html` (double-click to open in any browser, no server needed).

## 1. Purpose

Zac is commander in chief. Ares is his 5-star General, the command layer that used to be called Jarvis. The dashboard is the General's home screen: one dark, glowing page on his own PC that answers five questions at a glance.

1. Is the system healthy (system check color)?
2. What needs me (decisions queue, tasks waiting on Zac)?
3. What is each agent and venture doing?
4. How are the numbers (weekly pulls, fantasy, paper trading)?
5. How much of my limit have I burned?

It reads files that already exist. It does not run agents, post, spend, or change anything. Read-only in v1.

## 2. Reference look (viewed)

`D:\WKP\Trading bot look, example..png` is a phone screenshot of a "Grok Bot terminal depth desk": near-black navy page, cyan glow on key numbers, thin cyan-bordered panels with tiny spaced capital labels, a big account figure with small stats row under it (trades, win, mult, start), a 2-column grid of agent status tiles with a live dot each (SCAN, RISK, SIZE, EXEC, EXIT, LOG), a session stats list, a semicircle gauge (79, "buyers lead"), a clock top right, and cyan/pink bar and depth charts. The mockup keeps that language: navy panel, cyan edge, mono labels, glow on the one number that matters per card, a gauge, tile grid, clock.

Design guidance used: `design-taste-frontend` and `impeccable` are both installed (impeccable without its engine, per its install note, so no launcher was run). Both are aimed at app/dashboard "Operate" surfaces mostly as restraint: one system, equal edges, plain labels, real data not decoration. Applied: one accent color, status colors only for status, plain English card titles, no stock photos, no invented numbers. Not run: the taste gate script (needs a browser pass). That is a Step 1 item.

## 3. Screens

| # | Screen | What it shows | Source on disk | Exists now |
|---|---|---|---|---|
| 1 | Command (home) | System color, agent tile grid, decisions gauge, top tasks, numbers snapshot, clock | all below, summarized | mockup built |
| 2 | Ventures | Each venture, state (ACTIVE, HOLD, ACTIVE-UNSCHEDULED, DORMANT), last log line, next step | `CLAUDE.md` status block, `projects.md`, each venture `CLAUDE.md`, `logs\*-director.md` | yes |
| 3 | Agents | 52 specs, which ran lately, last run row, tokens | `.claude\agents\*.md`, `logs\agent-runs.md`, `logs\*.md` | yes |
| 4 | Tasks | Live table of TASKS.md, filter by status (Waiting on Zac first) | `TASKS.md` (markdown tables) | yes |
| 5 | Decisions | Open items with ID, blocked, options, recommendation | `logs\DECISIONS.md` (33 headers, 28 OPEN by a grep count today, parser must confirm) | yes |
| 6 | Numbers | Weekly pulls, change vs last week, "not available" where absent | `data\weekly-YYYY-MM-DD.md` (8 files, latest 2026-11-13), `data\etsy-manual-*.md` (latest 2026-08-20, stale) | yes |
| 7 | Calendar | WWD recording, releases, deadlines | No calendar file on disk. Options in section 6 | NO |
| 8 | Token and limit meter | Tokens used today and this week, by session | Claude Code session logs under `C:\Users\kingz\.claude\projects\D--WKP\*.jsonl` (usage fields per message, to be verified in Step 5) | partly |
| 9 | Fantasy | Week lineups, friend compare, sim summaries | `data\dfs-friend\*.csv`, `data\ff-simulator\`, `Fantasy-Football\cards\` | yes |
| 10 | Trading paper log | Paper trades, equity curve, watch-week score | No paper-trade log exists yet (watch week not run). `Investing\wkt-locked-rules.md` has the rules only | NO |
| 11 | System | Nightly check detail, backups flag, disk flag | `logs\system-check\latest.txt`, dated reports | yes |

Honesty rule on every card: if the file is missing or stale, the card says "not available" and names the missing file. Cards show the file's date.

## 4. Data sources already on disk (verified this run)

- `TASKS.md`, `logs\DECISIONS.md`, `logs\agent-runs.md`, `logs\system-check\latest.txt` (today: YELLOW, I: drive disk events, D:\WKP Reports not in git)
- `data\weekly-2026-09-18.md` through `weekly-2026-11-13.md` (WWD: 744 subs, 1,398 views over 6 days vs 4,370 prior 7 days)
- `data\dfs-friend\` (our three lineups, friend lineups, slate CSVs), `data\ff-simulator\`, `data\ff-play-sim\`
- `.claude\agents\` (52 specs), `.claude\skills\` (trader-* skills, no trade log)
- `WWD\data\post-times.md`, `WWD\data\video-inventory.md`
- `C:\Users\kingz\.claude\projects\D--WKP\` session `.jsonl` files (token data candidate)

Not on disk: calendar, paper-trade log, plan-limit number, live agent "running" state.

## 5. Stack (free, local, Windows PC, Mac viewing)

- Server: Python 3.12 standard library only (`http.server` plus `json`). Zero installs, zero cost. Already at `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe`.
- Parsers: small Python modules, one per source (tasks, decisions, weekly, system-check, agent-runs, usage). Each returns JSON plus the file date. Unit tests with real files and a deliberately broken file.
- Front end: plain HTML, CSS and a little vanilla JS. No framework, no build step, no CDN, no web fonts (system mono stack), so it works offline and nothing leaves the machine. Charts are inline SVG.
- Refresh: page fetches `/api/<card>` every 30 s. Files are re-read on request.
- Mac view: Tailscale is already installed on the PC (`C:\Program Files\Tailscale`). Bind the server to 127.0.0.1 only, then expose with `tailscale serve` to the tailnet. Zac's Mac must be on the same tailnet (install status of the second machine is still "Check" in TASKS.md). Never Tailscale Funnel (public), never 0.0.0.0.
- Location of code: `D:\WKP\software\ares\` (software-engineer rule). Plan and mockup stay in `D:\WKP\ARES\`.
- Cost to run: $0. No account, no API key.

Alternatives rejected: Node/React (needs build tooling, more surface), Streamlit or Grafana (new installs, heavier, less control of the look), a cloud host (data leaves the machine).

## 6. Decisions Zac needs to make

1. Calendar source. (a) a hand-edited `ARES\calendar.md` Ares reads, free, simplest, recommended for v1; (b) Google Calendar through the existing connector, but connectors run inside Claude, not from a plain local server, so it would need a pull job that writes a file; (c) skip. Recommendation: (a), then a pull job later.
2. Mac access: yes or no. If yes, the Mac must join Tailscale (free tier). No other setup.
3. Name of the page: "ARES". Confirm the rename scope in section 9 before any file is touched.
4. Token meter honesty: the plan limit is not readable from disk. v1 shows tokens used from local session files only. A real "percent of limit" is not available unless Zac types his limit in a config line. Zac's call.

No money, deploy or publish decision is involved in v1.

## 7. Security

- Local only. Server binds 127.0.0.1. Mac access only through Tailscale, which is private to Zac's devices. No port forwarding, no Funnel.
- Read-only. No write endpoints. No buttons that run agents or commands in v1.
- Allowlist of files. The server serves only parser output for named files. No directory browsing. Paths from the browser are never used to open files (no path traversal).
- No secrets shown. Never read `.env`, user env vars, `settings.json` tokens, `HF_TOKEN`, `OPUS_API_KEY`, `EBAY_*`, the trader-broker config, or the King Debt Planner (personal, never in repo). A redaction filter masks strings that look like keys before output.
- No personal data beyond what Zac already keeps in repo logs. Fantasy and DFS card shows lineups only.
- Child-safety rules do not apply (no minor touches it). The Teacher site stays a separate thing.
- Test pass (software-tester) before Zac uses it: secrets grep, traversal attempts, bind address check, dependency check (stdlib only).

## 8. Build order (small steps, each tested)

1. Static home page polish from the mockup: taste/impeccable checks in a real browser at desktop and 390 px phone width. No server.
2. Server skeleton on 127.0.0.1 plus `/api/health`. Test: refuses traversal, only localhost.
3. Tasks parser from `TASKS.md` plus Tasks screen. Test on real file and a broken table.
4. Decisions parser plus gauge (replaces the grep count). Agents screen from `.claude\agents` and `agent-runs.md`.
5. Token meter: inspect the session `.jsonl` format first, read-only, report what fields exist. Build only what the file proves.
6. Numbers screen from `data\weekly-*.md` with week-over-week and "not available" handling.
7. System card from `logs\system-check\`. Ventures screen.
8. Fantasy screen from `data\dfs-friend` and `ff-simulator`.
9. Calendar (per decision 1) and Trading panel (empty state until a paper log exists).
10. software-tester full pass, then qa-director, then `tailscale serve` instructions for the Mac, then a start-up shortcut (Zac runs it himself).

Each step ends with real test output logged to `logs\software-director.md`. No step before Zac's gate on step 1 (the look).

## 9. Where "Jarvis" appears (LIST ONLY, nothing renamed)

Scope: `D:\WKP`, excluding `.git`, `_archive`, `scratch`. Counts are occurrences from a ripgrep count today (330 occurrences in 112 files).

Operating files that define the role (rename here first, highest meaning):
- `CLAUDE.md` (13), `AGENT-NETWORK.md` (9), `TASKS.md` (1), `BUILD-QA-AND-SOFTWARE-DEPARTMENTS.md` (36)
- `memory\MEMORY.md` (3), `memory\topics\wkp-ops.md` (3), `memory\topics\automation-vision.md` (1), `memory\feedback-operating-procedure.md` (2), `memory\feedback-agent-authority.md` (1), `memory\feedback-own-the-operation.md` (1), `memory\feedback-take-initiative.md` (1), `memory\feedback-opus-clips-settled.md` (1), `memory\project-ian-trailer-free.md` (1)

Agent specs, `.claude\agents\` (22 files, behavior-bearing: these tell agents who to report to):
`wwd-director` (4), `fiction-director` (8), `marketing-director` (6), `qa-auditor` (4), `fantasy-football-director` (4), `shattered-empire-director` (3), `military-scifi-director` (3), `wwd-vfx` (2), `wwd-color` (2), `studio-director` (2), `software-director` (2), `script-room` (2), `qa-director` (2), `paws-director` (2), `kdp-director` (2), `etsy-director` (2), `ebay-researcher` (2), `animation-director` (2), `wwd-run-sheet` (1), `tracking-director` (1), `music` (1), and `_spec\wwd-vfx-toolkit.md` (1)

Skills, `.claude\skills\`: `wkp-update\SKILL.md` (1), `wkp-daily-brief\SKILL.md` (1, retired skill), `ff-simulator\SKILL.md` (1), `fantasy-football-data\players-cache-details.json.bak` (1). Also `design-taste-frontend\assets\photos\photos.json` (7): almost certainly a photo list, not our role name, check before any replace.

Scripts that execute the name (functional risk, test after any change):
- `scripts\nightly.bat` line 4 and `scripts\nightly-system-check.bat` line 8: `claude -p "Use jarvis to roll up ..."`. Lowercase. There is no agent file named jarvis in `.claude\agents`, so this is a prompt phrase, but confirm before editing.

Logs (history, normally leave as written): `logs\wwd-director.md` (17), `logs\script-room.md` (7), `logs\DECISIONS.md` (6), `logs\marketing-director.md` (3), `logs\animation-director.md` (3), `logs\jarvis-delegation.md` (2, and the FILE NAME itself contains Jarvis, referenced in CLAUDE.md), `logs\agent-runs.md` (2), `logs\fantasy-football-director.md` (1), `logs\studio-director.md` (1), `logs\qa\*` (3 files, 1 each), `Shattered-Empire\logs\director.md` (2)

Venture and report files: `Post-Production\CLAUDE.md` (1), `Post-Production\reports\Ian-Wrench-Turner-Trailer-Draft3-2.md` (1), `ANIMATION\CLAUDE.md` (1), `WWD\STANDARDS.md` (1), `Fantasy-Football\CLAUDE.md` (2), `Fantasy-Football\SCAFFOLD_HANDOFF.md` (4), `SCAFFOLD-HANDOFF-FANTASY-WK1.md` (2), `Fantasy-Football\reports\` (3 across 2 files), about 10 WWD report files (`WWD\reports\Vision-Quest-*` about 31 across 5 files, Comic-Series-* 4 files, OpusClip-Affiliate-Push-Packet 2, Godzilla-Minus-Zero-Copy-Draft 2, Patrick-Stewart-Tribute-Captions 1), `reports\workflow-map\2026-11-12-workflow-map.md` (3), `reports\fable-scan\2026-11-10-fable-scan.md` (5), `research\` (about 8 files: wwd ep120 fact check, voiceprints, cmmc-l1, fantasy cfb data sources 3, brand-kits, tools notebook list), `sleep work  document for 16 November.md` (1, untracked)

Data files (data, not role references, DO NOT bulk-replace): `data\ff-simulator\*.csv` and `data\ff-play-sim\*.csv`, `Fantasy-Football\fixes-2026-11-10\` caches and dataset. These contain Jarvis as a PLAYER name (for example "Jarvis Brownlee" in the backtest CSV). A blind find-and-replace would corrupt them.

Outside the repo, not scanned in detail: `C:\Users\kingz\.claude\settings.json` and user skills showed no match in a quick search. Scheduled tasks (`WKP-daily-brief`, Monday brief, system check) were not inspected and may carry the name in their prompts. Memory index lives under `C:\Users\kingz\.claude\projects\D--WKP\memory` (junction to the repo `memory\`).

Scoping advice for Zac's decision: rename in three passes. (1) the role definition files and agent specs, (2) scripts and scheduled-task prompts, (3) leave logs, reports, research and data as history. Never touch the CSV player names. Keep `logs\jarvis-delegation.md` as-is or rename the file and fix the CLAUDE.md reference in the same step.

## 10. Risks and known limits

- The mockup is a static picture. Agent running/idle dots are sample state (tagged SAMPLE). Real values on the page are tagged REAL and were copied from repo files on 2026-11-16.
- Decision counts (28 OPEN of 33) come from a grep, not a parser. The Step 4 parser may differ.
- Token meter source format not yet inspected. Limit percent may be impossible.
- Calendar and trading panels have no data today.
- Markdown parsers break when file formats change. Mitigation: tests plus a visible "could not read" state, never a guess.
- Taste/impeccable browser gate and phone-width check not run yet.

## 11. Verification done this run

- Viewed the reference image.
- Counted Jarvis with ripgrep (330 in 112 files), grouped by hand, checked the two .bat lines and the player-name data hits by listing.
- Counted `.claude\agents` files (52), read `latest.txt`, `weekly-2026-11-13.md`, DECISIONS header counts.
- Mockup contains no network calls, no external fonts, no secrets, and no em dashes.
- NOT done: browser render screenshot, slop_check on mockup copy, scheduled task inspection, qa-director pass (this is a plan, QA before build).
