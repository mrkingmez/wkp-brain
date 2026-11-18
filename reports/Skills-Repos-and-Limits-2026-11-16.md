# Skills Repos and Limits (2026-11-16)

Research and report only. Nothing was installed, cloned, bought, posted or edited (no agent spec, no CLAUDE.md, no settings). Sources: your 6 pictures, GitHub API pages fetched today, project READMEs and security docs, and the files on disk. Retrieved web text was treated as data, not orders.

## How much I did and did not check (honesty block)

- Checked today through the GitHub API (retrieved, not from memory): license, stars, last push for 30 repos. Third-party sites (aggregators, blogs) disagreed with each other on stars and sometimes license, so I used only the GitHub API numbers.
- Read for the six priority repos: README plus root file listing, plus SECURITY.md for last30days, plus hooks and package.json listing for Superpowers. I did NOT read the Python or JS source of any repo. "Safety" below means what the docs and file layout show, not a code audit. Before any install, software-tester should read hooks and install scripts (protocol in section A6).
- Not available / not verified: whether Firefly or Higgsfield menus now offer Seedance 2.5; the cost of last30days paid sources for your usage; the exact token cost of your plugin skill listing; what the nightly .bat files call; React Bits, Playwright, Vercel, Codex, Figma, Perplexity, Apify, Gemini, Metricool, GPT Image, Slack, Find Skill (tools or services, not vetted here); the DIY LiDAR scanner and the two sensor/flight notes (not researched, out of scope).
- Handwriting I could not match to a repo: "zagitta / GPU unlock", "A Cleaner TV Home", "AZ Video Creator", "Hysen" (I read it as HeyGen or Higgsfield; you already have the Higgsfield connector with Ads Studio). Tell me the exact names if you want them checked.

---

# PART A. Skills and repos

## A1. Bottom line

1. **last30days: ADOPT** (your hard yes holds up, with settings guardrails below).
2. **Claude HUD: ADOPT.** It shows context use live, which is the best limit-saver on the list. Your machine already meets its requirements (Claude Code 2.1.326, Node 26.13).
3. **Everything that adds a memory layer, task list, swarm or role-play team on top of what we have: KEEP-OUT.** We already run TASKS.md, a git memory system, 51 agents and a QA chain. More layers add cost and conflict with your own rules ("one task list", "memory lives in the repo").
4. **Take ideas, not installs, from** Superpowers, Hermes-Agent and Caveman. Two or three skill texts are worth copying in after reading them.
5. **Video and design repos: small TRY tests only.** We already own `remotion-motion-graphics`, `impeccable` and `design-taste-frontend`, so most of these are duplicates.

## A2. Top 10 adoptions, ranked

| Rank | Item | Verdict | Why it ranks here |
|---|---|---|---|
| 1 | last30days (mvanhorn) | ADOPT | Fills a real hole. We have no cross-platform "what is people talking about in the last 30 days" tool. Feeds WWD topics, What If premises, Etsy and market research. Free sources work with no keys. |
| 2 | Claude HUD (jarrodwatts) | ADOPT | Directly serves the limit rules. Context bar, rate-limit view, running agents. Read-only design with a permission-fenced Node process. |
| 3 | Superpowers, three skills only (verification-before-completion, writing-skills, systematic-debugging) | TRY | Supports Part C (self-test before "done"). Copy the skill text in after reading it. Do not install the plugin (SessionStart injection, heavy subagent workflow). |
| 4 | anatomy (wheresryan22) | TRY | Interactive isometric SVG diagrams. Strong fit for the Teacher course and for explainers. One test lesson. |
| 5 | Graphify (Graphify-Labs) | TRY (later) | Could make the 235k-word Shattered Empire canon queryable. Package only, skip its CLAUDE.md-editing install step (same warning as the 10-30 review). |
| 6 | Hallmark (Nutlope) | TRY | Anti-AI-slop design skill. A/B it against our `design-taste-frontend` on one page. If no clear win, drop it. |
| 7 | HyperFrames (HeyGen) | TRY | Agent-first HTML to MP4. One free test clip next to our Remotion skill. Good for cards and stings. |
| 8 | bang-motion (bangtutorial) | TRY | Single index.html openers, bumpers, kinetic type. Candidate for WWD stings. License MIT. |
| 9 | emilkowalski/skills | TRY (low) | UI motion polish for web pages. Only matters when we build sites (Teacher). |
| 10 | awesome-mcp-servers (punkpeye) | BOOKMARK | Lookup list only. Check it before building any connector ourselves. Zero install risk. |

## A3. Verdict table, priority six first

License, stars and last push are from the GitHub API today (2026-11-16 to 17).

| Repo | License | Stars | Last push | What it does | Safety read | Overlap with ours | Verdict |
|---|---|---|---|---|---|---|---|
| mvanhorn/last30days-skill | MIT | 68,279 | 2026-11-17 | Researches a topic across Reddit, X, YouTube, Hacker News, Polymarket, GitHub, TikTok, Instagram, Bluesky and more, ranks by real engagement, writes a brief | SECURITY.md is unusually detailed: no telemetry, keys read from env or a user config, project key files only load if you opt in, retrieved posts are fenced as data, browser cookies off by default. Cautions: no sandbox, runs subprocesses (node, yt-dlp, gh), first-run setup runs a pinned npm package (`@mvanhorn/printing-press-library@0.1.27`), a few lookups (Wikidata, Yahoo Finance, USPTO) are on by default with opt-outs, job lane can read pages whose robots.txt disallows them unless you set `LAST30DAYS_JOBS_RESPECT_ROBOTS=1` | None. market-research and VidIQ cover other ground. yt-dlp is already installed here | **ADOPT** |
| thedotmack/claude-mem | Apache-2.0 per LICENSE file, README and API (older third-party pages said AGPL, so check again if it matters) | 117,754 | 2026-11-17 | Hooks every tool use, a background worker summarizes sessions into SQLite plus Chroma, injects memory next session | Hooks on 9 events, a local HTTP worker, Bun and uv auto-install, a second "observer" model call that burns plan usage, analytics on by default (disable: `npx claude-mem telemetry disable`), optional cloud sync, 30-day trial that asks for a card. README gives no measured savings | Conflicts with our git memory (curated, human-readable, routing rules) and with the limit goal (extra model calls every session) | **KEEP-OUT** for the main repo. Revisit only as a scratch-repo test after the limit rules are working |
| eyaltoledano/claude-task-master | MIT plus Commons Clause (you cannot sell the software itself; building products with it is fine) | 28,363 | 2026-04-28 | PRD to task list, MCP server | Default loads 36 MCP tools (README: about 21,000 tokens of context; lean mode about 5,000). Needs its own API key unless run through Claude Code. 6 months since last push | Duplicates TASKS.md, which is the locked single task list | **KEEP-OUT** |
| obra/superpowers | MIT | 318,764 | 2026-11-03 | 14 skills: brainstorm, plans, TDD, debugging, verification, subagent-driven development, code review, writing skills | Root `package.json` has no scripts and no dependencies (retrieved). Has a `hooks/` folder with a `session-start` script that injects the bootstrap skill every session. Optional visual companion pings its website with the version (disable with `SUPERPOWERS_DISABLE_TELEMETRY`). Not source-audited | Built for coding. Our work is mostly content and ops. Its subagent-per-task mode is the expensive one | **TRY**, three skills only, copied in after reading, no plugin |
| remotion-dev/remotion | "Other" (Remotion License). Free for individuals, for-profit companies up to 3 employees, and non-profits. Company license needed above 3 employees. License changes in 5.0 | 73,734 | 2026-11-16 | React video | Standard npm toolchain | We already have `remotion-motion-graphics` | **Already ADOPTED** (skill). Re-check the license if WKP or WWD ever grows past 3 people |
| heygen-com/hyperframes | Apache-2.0 | 85,334 | 2026-11-17 | HTML, CSS and seekable animation rendered to MP4 with headless Chrome and ffmpeg, agent skills included | Needs Node 22+ and ffmpeg (both present). `npx skills add heygen-com/hyperframes` pulls skills from the repo. Not source-audited | Overlaps our Remotion skill but no React and no paid-license question | **TRY** (one test clip) |
| jarrodwatts/claude-hud | MIT | 29,220 | 2026-11-10 | Status line: context use, rate limits, tools, agents, todos | Per its README, logic runs in a Node process with a permission model that blocks spawning programs, reading credentials and writing outside its own folder. `--extra-cmd` is ignored unless you set an env var. Reads stdin, the transcript and git metadata. Needs Claude Code 2.1.260+ and Node 22.18+ (you have 2.1.326 and 26.13) | None | **ADOPT** |

## A4. The rest of your list

| Item | License | Stars | Last push | Verdict and reason |
|---|---|---|---|---|
| ruvnet/ruflo | MIT | 81,895 | 2026-11-16 | KEEP-OUT. Another multi-agent swarm harness. We already have an agent network. Large surface, little we would use. |
| wheresryan22/anatomy | MIT | 27,736 | 2026-10-18 | TRY (rank 4). |
| JuliusBrussee/caveman | Apache-2.0 | 120,799 | 2026-11-16 | KEEP-OUT as installed software. Its own page says "answer concisely" is the honest baseline and the rules add about 1,160 input tokens; the CLI sends usage stats by default; its Auto mode sends your prompts to its cloud. Take the idea: one line in CLAUDE.md asking for terse output (see rule L22). |
| DietrichGebert/ponytail | MIT | 192,302 | 2026-10-29 | KEEP-OUT. Makes coding agents write less code. We write little code. Its plugin runs hooks. |
| OpenHands/OpenHands | MIT | 93,615 | 2026-11-17 | KEEP-OUT. A software-dev agent platform. software-director covers our needs. |
| NousResearch/hermes-agent | MIT | 263,975 | 2026-11-17 | KEEP-OUT as a runtime. Its "agent that grows with you" idea is the pattern Part C borrows. |
| crewAIInc/crewAI | MIT | 61,003 | 2026-11-16 | KEEP-OUT. Python agent framework; our org chart already is the framework. |
| Aider-AI/aider | Apache-2.0 | 50,151 | 2026-05-22 | KEEP-OUT. Six months without a push, and Claude Code replaces it. |
| n8n-io/n8n | "Other" (fair-code, internal business use allowed, not for reselling) | 210,687 | 2026-11-17 | LATER. Self-hosted automation could run non-public data pulls. We already have scheduled tasks and Composio. Public posting stays Zac's gate. |
| langchain-ai/langgraph | MIT | 45,045 | 2026-11-16 | KEEP-OUT. Developer framework. |
| cloudflare/agentic-inbox | Apache-2.0 | 8,780 | 2026-04-23 | KEEP-OUT. Needs a Cloudflare account and hosting; Gmail connector already exists. One policy gives access to all mailboxes by design. |
| browser-use/browser-use | MIT | 121,251 | 2026-11-17 | KEEP-OUT. We have claude-in-chrome already logged into your sessions. |
| punkpeye/awesome-mcp-servers | MIT | 97,780 | 2026-11-17 | BOOKMARK (rank 10). |
| eyaltoledano/claude-task-master | see A3 | | | KEEP-OUT. |
| andrewyng/openworker | MIT | 19,397 | 2026-11-16 | KEEP-OUT. Desktop agent with your own API keys (you pay model costs). Duplicates Claude Code and Cowork. |
| garrytan/gstack | MIT | 141,833 | 2026-11-16 | KEEP-OUT. 23 role tools (CEO, designer, QA). Same job as our directors, built for software teams. Steal the retro and QA ideas if wanted. |
| Graphify-Labs/graphify | Apache-2.0 | 149,140 | 2026-11-16 | TRY later (rank 5). The earlier review said the same. Note the repo owner is Graphify-Labs (one directory pointed at safishamsi/graphify, I did not check that one). |
| Anil-matcha/Open-Generative-AI | MIT | 35,060 | 2026-11-16 | KEEP-OUT for now. Generation runs through a paid MuAPI gateway and it markets "no content filters", which is a rights risk for WWD. Local models are free but we have Firefly and Higgsfield. |
| elementalsouls/Claude-BugHunter | MIT | 7,615 | 2026-11-16 | KEEP-OUT for now. 82 offensive-security skills. Useful only with a target you own; CySA+ is punted. Never point it at anything that is not yours. |
| Nutlope/hallmark | MIT | 56,239 | 2026-11-11 | TRY (rank 6). |
| nextlevelbuilder/ui-ux-pro-max-skill | MIT | 150,511 | 2026-11-16 | KEEP-OUT. Third design skill on top of Taste and Impeccable. Three overlapping design skills fight each other. |
| emilkowalski/skills | MIT | 57,513 | 2026-11-15 | TRY (low). |
| React Bits | not checked | | | KEEP-OUT until someone checks the exact repo. Post only said "github.com/David...". |
| Impeccable, Taste skill | already installed | | | Keep. |

Services and tools I did not vet (not repos): Playwright, Vercel, Codex, Figma, GitHub CLI (not installed here: `gh` not on PATH), Perplexity, Apify, Gemini, Metricool, GPT Image, Slack, Find Skill, Node.js (installed, v26.13). Tell me which one you want checked and why.

## A5. The six video repos (picture 3)

| Repo | License | Stars | Created / last push | Verdict |
|---|---|---|---|---|
| CK42BB/vox-explainer-skill | MIT | 262 | 2026-07-11 | TRY only if the What If channel starts. Small, single author. |
| lintsinghua/paint-mv-skills | "Other" | 73 | 2026-09-25 / 09-29 | KEEP-OUT until the license is read. Watercolor music videos, not a WKP need. |
| aarontan-bot/hand-drawn-explainer | MIT | 0 | 2026-09-19 / 09-21 | KEEP-OUT. Zero stars, no description, created two months ago. Unvetted. |
| bangtutorial/bang-motion | MIT | 2,408 | 2026-09-05 / 09-15 | TRY (rank 8). |
| haidrrrry/claude-remotion-skill | MIT | 1,070 | 2026-06-13 / 08-12 | KEEP-OUT. We have our own Remotion skill. Skim its captions and sound design sections for ideas. |
| Vincentwei1021/video-shotcraft | Apache-2.0 | 20,702 | 2026-07-19 / 11-16 | LATER. Product promo videos from screenshots. Only matters if Kingdom Planners or a paid product comes back. |

The post these came from is a "comment 'repos' and I will send them" lead magnet. The repos are real, but the post is marketing, not evidence they beat what we have.

## A6. Pre-install protocol (applies to everything marked ADOPT or TRY)

1. Zac says yes to the exact item. No installs without it.
2. software-tester reads: `hooks/*`, `package.json` scripts (`preinstall`, `postinstall`), anything with `curl`, `fetch`, `eval`, `exec`, `Invoke-WebRequest`, base64, and every URL the code calls. Reports in plain words.
3. Pin to a commit or version, never `@latest` or a moving branch.
4. Install into a test copy first (scratch folder or a second Claude Code profile), run once, check what files it wrote and what network calls it made.
5. Check the plugin does not change `settings.json`, CLAUDE.md or hooks without showing the diff first.
6. Log it in `logs\agent-runs.md` and add one line to `reports\github-tools`.

## A7. How to set up the two ADOPT items (needs Zac's yes before any command runs)

**last30days.**
- Install (in Claude Code): `/plugin marketplace add mvanhorn/last30days-skill`, then install from that marketplace. Source repo: github.com/mvanhorn/last30days-skill.
- Run `--preflight` first. It shows what it will read and write without researching.
- Start with free sources only: Reddit, Hacker News, Polymarket, GitHub, YouTube through the yt-dlp already installed.
- Do NOT add ScrapeCreators, Brave, Perplexity, X API or Bright Data keys without Zac's yes and the cost. Those are pay-as-you-go.
- Leave browser cookies and Reddit login off. Set `LAST30DAYS_JOBS_RESPECT_ROBOTS=1`.
- Output goes to `Documents\Last30Days`. Move or point it to `D:\WKP\scratch` with `LAST30DAYS_MEMORY_DIR`. Never use `--publish` (public by default).
- Who uses it: tracking-director and market-research for WWD topic and Etsy trend checks, wkp-channel-director for What If premises. Its output is research, not copy, so it still goes through the writing room and slop gate before anything public.

**Claude HUD.**
- Install: `/plugin marketplace add jarrodwatts/claude-hud`, `/plugin install claude-hud`, `/reload-plugins`, `/hud`. It asks before changing the status line and can undo.
- It edits the status line setting in your user settings, so that is a settings change Zac approves.
- Leave `--extra-cmd` alone. Auto-update is off by default; keep it off.

---

# PART B. Limit rules rewritten for WKP

## B1. What loads at every session start (measured, bytes on disk today)

| File | Bytes | How it loads |
|---|---|---|
| CLAUDE.md | 24,908 | auto |
| ME.md | 4,525 | @import from CLAUDE.md |
| projects.md | 9,131 | @import |
| TASKS.md | 17,855 | @import |
| LOCAL-PATHS.md | 10,664 | @import |
| memory\MEMORY.md (junction target) | 7,856 | auto memory index |
| **Total** | **74,939** | about 75 KB, roughly 18,000 to 19,000 tokens (my estimate at 4 bytes a token, not measured) |

Also loaded each session but not measured exactly: the skills list (55 repo skills with 11,404 bytes of description lines, plus roughly 100 plugin skills from small-business, carta-investors, product-management, sp-global and Adobe that WKP does not use) and the agent list (51 agents, 23,273 bytes of description lines). Not available: the true token cost of those two lists.

My understanding, not tested here, is that subagents also receive CLAUDE.md and its imports, so every one of your 51 agents may start by paying for the same 75 KB. If so, trimming it saves on every agent call, not just on your own chat.

Other size facts worth knowing:
- `logs\DECISIONS.md` is 41,300 bytes (543 lines), `logs\agent-runs.md` 28,959. Any agent that reads either whole pays for it. Use `tail` or `grep`.
- Biggest skills: task-observer 45,023 bytes (only loaded weekly, good), design-taste-frontend 31,351, wwd-review-photo-pull 30,821, wwd-review-pipeline 27,782. These load only when called.
- Biggest agent specs: wwd-director 11,709, fantasy-football-director 9,635, wwd-vfx 9,220.
- Your user settings: default model `sonnet`, and `autoCompactWindow: 400000` for claude-sonnet-5-5. That lets a conversation grow very large before it compacts. See rule L9.
- Opus agents (6 of 51): clearance, devils-advocate, dialogue-doctor, fiction-director, originality, room-writer. These are the same agents the two-pass script gate calls, so a single script can run Opus 4 or more times.
- CLAUDE.md contains 40 corrupted dash characters (shown as "â€”"). Each takes 6 bytes instead of 1. Minor, fix while trimming.

## B2. What to trim, in order of savings

Target: from 75 KB down to about 30 KB. Saves about 45 KB (about 11,000 tokens) every session and every cold agent.

| Order | Change | Saves | Risk |
|---|---|---|---|
| 1 | TASKS.md: stop importing it. Keep only a 1.3 KB "Today and this week" block in the loaded path and read the rest on demand (`Read TASKS.md` when a task comes up, which CLAUDE.md already requires you to update). | about 16 KB | Low. Agents must read it when updating tasks. |
| 2 | projects.md: stop importing it. Its venture table is already in CLAUDE.md and half of it says "Needs a project file". Keep as a reference file. | about 9 KB | Low. |
| 3 | LOCAL-PATHS.md: split. Keep Core and Tools (about 2 KB) loaded; move WKD, Kingdom Planners, Shattered Empire, Stellar Dominion, eBay and Animation detail to read-on-demand. | about 7 KB | Low. Agents already "read LOCAL-PATHS.md, never hardcode". |
| 4 | CLAUDE.md: move the FrostCast Transcription Workflow section (4,790 bytes) into the `wwd-video-transcriber` skill or `WWD\CLAUDE.md`, shorten Review gates (4,127) to a 1 KB rule plus pointer, delete "Daily rhythm (old, kept for reference)" and the stale "Current state" block, compress Output document format (2,201). | about 10 to 12 KB | Medium. Moved text must stay reachable, and WWD director must read its own file. |
| 5 | MEMORY.md: five index lines exceed 300 characters. Cap every line at about 150 characters; detail already lives in topic files. | about 3 to 4 KB | Low. |
| 6 | Disable unused plugin skill packs (small-business, carta-investors, sp-global, product-management, cowork-plugin-management) in plugin settings. | skills-list size, not measured | Low. Re-enable any time. |

Do one change at a time and compare, per the Agent working standard: change 1 first, run a normal day, then 2. Measure with the HUD context readout at session start (before and after).

## B3. The 21 rules, sorted for WKP

Source: Instagram infographic by sarveshthakur.ai, Nov 2. It is a marketing graphic, not Anthropic documentation. I could not verify the savings from any rule; the mechanisms below are my understanding of how context and caching work, flagged where I am unsure.

| # | Original rule | WKP status |
|---|---|---|
| 1 | Medium effort, never Max | KEEP (L1) |
| 2 | Save your free reset for a bad day | N/A (reset policy not verified, no source in the picture) |
| 3 | Opus 5.5 in every chat, never Fable | ADAPT (L2). Your default is Sonnet; the picture says Opus. Zac picks, see L2 |
| 4 | Never switch models mid chat | KEEP (L3) |
| 5 | Never go back to an old chat, use a 10 line summary | ADAPT (L5). Conflicts with the saved "show session" resume habit |
| 6 | End quick questions with "No web search" | N/A for Claude Code, KEEP in claude.ai chats |
| 7 | Plan the deck in text, file last | KEEP (L8). This is your .md first, .docx once rule |
| 8 | Highlight the part to fix, do not redo | KEEP (L10) |
| 9 | Load apps on demand (connectors) | KEEP (L14) |
| 10 | Tell Claude to stop re-thinking (settings, instructions) | ADAPT (L22) |
| 11 | Crop screenshots, PDFs to text | KEEP (L17) |
| 12 | Pause every scheduled task you do not read | KEEP (L15). Concrete hit: `WKP-daily-brief` task is still enabled (TASKS.md) |
| 13 | Start every task with "ask me questions" | ADAPT (L7). Fire-and-forget conflicts with it |
| 14 | Put all asks in one message | KEEP (L6) |
| 15 | Speak, do not type, Wispr Flow | DONE. OpenWhispr works already (note: send Zac's voice rambles as one message) |
| 16 | Never correct Claude, edit your prompt | KEEP (L10) |
| 17 | One topic per chat | KEEP (L4) |
| 18 | Instructions under 2,000 words | KEEP and tighten (L11). Yours are about 12,000 words loaded |
| 19 | Upload reused files in a Project | N/A for Claude Code. In claude.ai, only for Teacher and Cowork work |
| 20 | In Claude Code: one task, then /clear | KEEP (L4) |
| 21 | Split the day into 3 sessions | ADAPT (L21). Your day is fragments |

## B4. The WKP rule set (L1 to L22)

Short enough to paste into CLAUDE.md as a 20-line block once trimmed. Zac decides which to lock.

**Model and effort**
- L1. Medium effort. Never Max. Higher only when Zac names a specific job.
- L2. Default model stays Sonnet for Ares and 45 of 51 agents. Opus stays on the six judgment agents (clearance, devils-advocate, dialogue-doctor, fiction-director, originality, room-writer). Fable only when Zac types the word in the prompt. DECISION FOR ZAC: the infographic says Opus for every chat; your own setting is Sonnet. Test one change: keep Sonnet for a week, compare send-back counts before moving anything.
- L3. Never switch model inside one session. Start a new session instead. (My understanding: a switch re-reads the whole history at full price.)
- L9. Test one change: lower `autoCompactWindow` from 400,000 toward 200,000 and compare, or run `/compact` yourself at about half of the HUD bar. Not tested; the compaction effect on cost is not verified here.

**Session hygiene**
- L4. One topic per session. Finish the task, then `/clear`. Long chains (Wednesday transcript chain, Monday brief) each get their own fresh session.
- L5. Do not resume a long old session. Ask for a 10-line summary written to a file, start a new session, paste it. Resume only when the session is short.
- L6. Put all asks in one message. Voice rambles are one message: say all of it, then send.
- L7. Ask-first only for NEW builds (a new tool, department, product). Routine runs (transcript chain, shorts, weekly packs) never ask, per the zero-question rule. Agents cannot ask anyway: they queue to DECISIONS.md.
- L8. Draft in .md first, build the .docx once at the end. Never re-render a deliverable for a typo; fix the .md and rebuild once.
- L10. To fix something, name the exact part and say "edit this part". Do not say "redo it". If a reply went the wrong way, rewind and edit your message instead of arguing with it (`/rewind`; my understanding, check it works on your version).
- L21. Natural session boundaries, not a clock: Monday brief, Wednesday night FrostCast chain, Thursday fantasy lock, Saturday wrap, one build session. Clear between them.

**Context size (the big lever for you)**
- L11. Auto-loaded memory budget: 30 KB total (CLAUDE.md under 12 KB, MEMORY.md under 4 KB). Anything over goes to read-on-demand files. Re-measure monthly with the command in B5.
- L12. No `@import` of any file over 3 KB. Imports load every session whether needed or not. TASKS.md, projects.md and LOCAL-PATHS.md come off the import list.
- L13. Agents never `Read` whole logs. `DECISIONS.md` and `agent-runs.md` are read with `tail -n 40` or `grep`. Big files are read by line range.

**Subagents**
- L16. Spawn an agent only for real parallel or isolated work. One director per job, benches only when the director needs them. Maximum 3 parallel agents unless Zac says otherwise. A one-line lookup is done inline.
- L17. QA runs once on the finished product, not after every step. The two-pass script gate stays (it is a locked rule) but both passes run in one `script-room` call so Opus is not reloaded for each.
- L18. Every agent job writes its ledger row with the token count from the task result. This is how we see what is expensive instead of guessing.

**Connectors and scheduled tasks**
- L14. Connectors load on demand. Disconnect what you do not use. In this session I see three ElevenLabs connectors (plain, 2, 3), Higgsfield, VidIQ, OpusClip, Gmail, Calendar, Composio, OpenWhisper, plus plugin packs for Shopify, Slack, Atlassian, Canva and 30 other vendors. Disconnect duplicates and any pack with no job in TASKS.md. Cost of the tool lists: not measured.
- L15. Audit scheduled tasks monthly: for each, name who reads the output. Disable `WKP-daily-brief` now (already retired in CLAUDE.md, still enabled per TASKS.md). The two nightly .bat files (`scripts\nightly.bat`, `scripts\nightly-system-check.bat`): I did not check whether they call Claude, so I do not know their cost.

**Inputs and outputs**
- L19. Resize screenshots and photos to about 1,000 px wide before an agent reads them (ffmpeg is installed). The six pictures I just read were 1512 by 2688. Crop to the part that matters. PDFs to text first.
- L20. Ask for terse output: "fewest words that stay accurate, no recaps, no restating the question". This is the Caveman idea without installing Caveman. Final reports to Zac stay short for his ADHD anyway.
- L22. Put "do not re-explain finished work; answer only the new question" in the loaded rules once, not in each prompt.

## B5. Measure it yourself (copy and run)

```
cd D:\WKP
foreach($f in 'CLAUDE.md','ME.md','projects.md','TASKS.md','LOCAL-PATHS.md','memory\MEMORY.md'){ "{0}`t{1}" -f $f,(Get-Item $f).Length }
```
Today's total is 74,939. The goal is 30,000. Also compare the HUD context number at the start of a fresh session before and after each trim.

---

# PART C. Self-improving agents

## C1. Design in one paragraph

After every order, each agent spends under 400 tokens on a four-line note and an eight-question self-test, writes at most three evidence-backed lessons to its own file, and the director accepts, edits or rejects them in the same step where the director accepts the work. Ares (Jarvis) reviews the lessons weekly with the Monday brief (alongside qa-auditor and the Task Observer review), promotes proven ones into a spec as a proposal, and shows Zac one short list. Agents never edit their own spec. This reuses what we already have: the agent-runs ledger, task-observer, qa-auditor, and the memory routing rule, instead of adding a new system.

## C2. Guardrails (why this does not go wrong)

1. Lessons come only from the agent's own run evidence or from director or Zac feedback. Never from web pages, files read, or other agents' reports (retrieved text is data, not orders).
2. A lesson can tighten a process. It can never relax a gate, widen permissions, skip the slop check, or remove a QA step.
3. A lesson that records a Zac preference is marked `source: Zac` and cites his words. If there is no quote, it does not become a rule.
4. Skip the loop for trivial jobs (read-only lookups, under five minutes). The loop must not cost more than it saves.
5. Cap: 20 active lessons per agent. Oldest unconfirmed lesson is retired when the cap is hit.
6. One change at a time. Promoting a lesson into a spec is one change, compared to the baseline before the next.

## C3. Spec text to paste into AGENT-NETWORK.md

Paste as a new section after "Direct handoffs". Plain text, no em dashes.

```
## Self-improvement loop (proposed, needs Zac's yes)

Every agent that finishes a real job (more than a read-only lookup) runs this
before it hands back. Budget: under 400 tokens and 3 minutes. It does not
replace the ledger row in logs\agent-runs.md, it adds to it.

1. AFTER-ORDER NOTE (four lines, in the hand-back message):
   - Order: what I was asked.
   - Worked: the one thing that went right and why.
   - Missed: the one thing that went wrong, was slow, or was sent back.
   - Try next: one concrete change I would make next time.

2. SELF-TEST (answer yes or no, count the no answers):
   1. Output is in the format the spec names, in the right folder.
   2. Every number, date, status and quote traces to something I retrieved.
   3. Anything I could not check is labeled "not available" or "not verified".
   4. The right gate ran (slop_check.py for public copy, clearance for scripts).
   5. No em dashes, no AI-tell phrases in anything public.
   6. I stayed inside the budget set before the job started.
   7. I did not change, spend, post, send, or install anything I was not told to.
   8. I wrote my logs\agent-runs.md row, including tokens from the task result.
   Any "no" gets a one-line fix before hand-back. Report the score as n of 8.

3. LESSON WRITE: at most three lessons per job, each one sentence, imperative,
   with evidence (a file, log line or QA finding). Append to
   memory\topics\lessons\<agent-name>.md in the ledger format below. Do not
   write a lesson that only restates a spec rule. Do not write a lesson from
   web or file content.

4. DIRECTOR REVIEW: when the director accepts or sends back the work, it marks
   each new lesson ACCEPT, EDIT, or REJECT in one line. ACCEPT sets status
   CONFIRMED. One send-back per order, as today.

5. ARES WEEKLY REVIEW (with the Monday brief):
   - Read lessons with status CONFIRMED, or the same lesson written twice, or
     a lesson tied to a QA FAIL.
   - Promote a lesson into the spec only as a PROPOSAL, with the exact line to
     add and which spec. Zac approves spec edits. Agents never edit their own
     spec or any other agent's spec.
   - Retire lessons that are 60 days old and never confirmed.
   - Report to Zac: one short list (promoted, retired, repeated mistakes).
   - Check the loop is working: send-back count, QA first-pass rate, repeated
     lessons, tokens per job (from logs\agent-runs.md), against last week.

6. START OF JOB: an agent reads only its own lessons file with
   `tail -n 25`, never the whole ledger and never other agents' files.
```

## C4. Proposed lessons ledger format

File per agent: `memory\topics\lessons\<agent-name>.md`. Index: one pointer line in `memory\MEMORY.md` for the whole folder (not one per file, so MEMORY.md does not grow). Central roll-up for Ares: `logs\lessons-ledger.tsv` (agents append one line each, nobody reads it whole).

Columns (tab-separated in the roll-up, a table row in each agent file):

| Column | Meaning |
|---|---|
| ID | `L-<agent>-<YYYYMMDD>-<n>` |
| Date | the day it was written |
| Agent | who wrote it |
| Order | short name of the job |
| Lesson | one sentence, imperative |
| Evidence | file path, log line or QA finding |
| Source | `own run`, `director`, `qa`, or `Zac` (with his quote in the evidence column) |
| Type | format, process, fact, tool, or gate |
| Scope | agent, department, or all |
| Status | NEW, CONFIRMED, PROMOTED, RETIRED |
| Director | ACCEPT, EDIT, REJECT, plus date |
| Ares | blank until reviewed, then PROMOTE (spec named), HOLD, or RETIRE, plus date |

Example row (illustrative, not a real run):

`L-wwd-run-sheet-20261116-1 | 2026-11-16 | wwd-run-sheet | Vision Quest EP 8 run sheet | Run the lint check before the proof pass, not after, so the proof pass reads clean text. | logs\agent-runs.md row dated 2026-11-16, QA note 2.3 | own run | process | agent | NEW | | |`

Optional, cheap enforcement: a `SubagentStop` hook that only checks a ledger row exists for the job and prints a warning if not. No model call, so no tokens. It changes settings, so it needs Zac's yes. Not tested here.

## C5. Pilot (so we learn before we roll to 51 agents)

- Pilot agents: script-room, wwd-run-sheet, tracking-director (all produce repeatable work and already log). Two weeks.
- Baseline first from what exists: QA PASS and FAIL counts in `logs\qa\`, send-backs, tokens per job in `logs\agent-runs.md`. If the baseline is thin, say "unguided" like the closed-loop rule.
- Success means: fewer repeated mistakes (same lesson written once, not twice), flat or lower tokens per job, QA first-pass rate not worse. If tokens per job rise with no quality gain, stop.
- Borrowed ideas: Hermes-Agent (agents that learn from their own runs), Superpowers `writing-skills` (test a skill on a real case before trusting it), our own task-observer (already does weekly friction review). The lessons file feeds task-observer's weekly pass instead of creating a competing system.

---

# PART D. Seedance 2.5 versus Veo 3.1 for your use

Evidence is mostly vendor or reseller writing. Treat all of it as claims. I did not run either model.

| Point | Seedance 2.5 | Veo 3.1 | Source and weight |
|---|---|---|---|
| Clip length | 4 to 30 seconds, any length | fixed 4, 6 or 8 seconds | Krea (a reseller, tests in Aug 2026, published 2026-09-05) |
| Resolution | 480p or 720p per Krea; "up to 4K" per OrcaRouter | 720p, 1080p, 4K | Sources conflict. Not verified |
| Aspect ratios | six, including 9:16, 16:9, 21:9, square | 16:9 and 9:16 | Krea |
| Audio | same-pass audio | same-pass audio, doubles the clip price; strong dialogue reputation | Krea, OrcaRouter |
| References | up to 30 images, 10 videos, 10 audio | image references | Krea. Matters for character consistency |
| Price | API from $0.0645 a second | 6 s silent $1.26, with audio $2.52; 8 s silent $1.68, with audio $3.36 | Krea. Another source: no USD price list, so not verified |
| Preference rankings | 1,474 (text-to-video) | 1,364 | Gradually (leaderboard figures, LMArena as quoted). Closest thing to independent. Seedance ahead |
| Availability in the US | consumer apps blocked in the US, Canada and Australia as of Aug 2026; reachable through gateways such as Krea; ByteDance international API "coming soon" at that date | callable with a US card; Firefly menu already has it | Techjack Solutions, 2026-08-06. May have changed. Not verified now |
| Rights and filters | aggressive filters after studio disputes (Disney, Paramount letters); no watermark or provenance feature documented | SynthID provenance | Techjack. Unverified whether 2.5 keeps the same filters |

**What matters for you.**
- **Book trailer (Ian, 9:16 and 16:9, 45 s and 15 s).** Veo 3.1 already works inside the Firefly account Matt paid for, outputs both ratios you need, and is the model the Draft 3.2 plan names. Seedance's edge (longer single takes, 30 reference images) helps character consistency, but you told me to stop buying video runs and finish with stills and push-ins. A new model means a new account, a gateway, and new cost.
- **Shorts.** WWD shorts are cut from real footage in Opus Clip. Neither model is part of that chain, so this comparison does not change Shorts.
- **WWD cold open and Warden shots (if generated).** Same logic as the trailer. Firefly holds Veo 3.1 and the commercially-safe positioning of its own models; Seedance comes with unresolved studio disputes and no provenance mark.

**Recommendation.** Stay on Veo 3.1 for now. No switch, no spend. If you later want a longer take or heavy reference-image consistency, run ONE test clip of Seedance through a gateway (Krea lists it) after Zac approves the exact cost, and judge only on the shot you need. Open items I could not verify: current US availability, a real USD price, whether 2.5 is capped at 720p, and whether Firefly or Higgsfield now list Seedance (a read-only model list check is possible, not run).

---

## What happens next (nothing runs until Zac says yes)

1. Decide L1 to L22 and the trim order (B2). Cheapest first win: stop importing TASKS.md and projects.md, and disable the `WKP-daily-brief` task.
2. Yes or no on installing last30days and Claude HUD under the A7 settings.
3. Yes or no on piloting the Part C loop with three agents.
4. A concern worth saying plainly: this list is long and your own rule is to finish what is in front of you. The two ADOPT items plus the trims are the whole high-value set. The rest can sit.
