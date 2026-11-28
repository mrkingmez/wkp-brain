# Leveling task: wwd-director

Wave 2, batch 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-26 by chief-of-staff on Jarvis's order (Zac 2026-11-26: "Let's get them learning and growing"). Jarvis launches this as one job. Run as `wwd-director` (spec `D:\WKP\.claude\agents\wwd-director.md`), or through a general-purpose agent running that spec. Grader: Jarvis (directors are graded by Jarvis per SOP part 3), with qa-director as second reader of the grader-set traps, never the agent itself. Do NOT self-rate.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\wwd-director.md` (all lessons, including the 2026-11-26 standing rule on trying the other connected route) and `SOP\SOP-Output-Locations-and-Formats.md` before starting. Level starts at 0 Unrated (no brief, drill or signed evidence exists, checked 2026-11-26: no `wwd-director-craft-brief.md` in `memory\agents\briefs\`). Until a grader signs a drill PASS, outputs carry the line `UNDRILLED` and go through the director.

## Why this agent is in batch 1
Routes every WWD and FrostCast job and runs the Wednesday chain. 2026-11-18 to 2026-11-26 lessons show repeat misses: the Drive-mirror order was never written down (2026-11-20), a handoff said Sea of Monsters for Season 3 (it is Titan's Curse), 4 speaker labels where the handoff said 1, a stray `.claude\agent-memory` folder created in a movie folder, Shorts copy written blind with a wrong "fight", caption builds dropping the first word. Source: `memory\agents\wwd-director.md`, `logs\wwd-director.md`.

## Step 0: Tool check (new, 2026-11-26)
Spec tools: Read, Write, Edit, Glob, Grep, Bash, Agent (no browser, no web; spec line 74 says Jarvis does the Messenger send). Check: does every step the spec assigns to this agent have a tool? Known gap to confirm: the Messenger send to Matt, Opus API calls (Bash with OPUS_API_KEY) and any picture-pull routing must name who holds the browser.
First line of every hand-back from this job: the tools actually available in the run, and any step that needed a tool the run did not have. A step that could not run is reported as NOT RUN, never skipped silently. If a tool or source fails, try the other connected route before escalating (standing rule, Zac 2026-11-26); never spoof headers or user agents.

## Step 1: Craft Brief (`memory\agents\briefs\wwd-director-craft-brief.md`)
Format and rules per SOP part 1: 5 to 10 primary sources, at most 2 community, each with URL or path, retrieved date and 1 to 3 VERBATIM quotes. Fewer than 5 retrieved means INCOMPLETE and no rating above Level 1. Tag every claim PROVEN, SOURCED, COMMUNITY or PROPOSED. The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write `NOT RETRIEVED: <url>, <reason>` for any page that cannot be fetched. Never fill from memory.
- Anthropic subagent and Claude Code docs on delegation and tool scoping (docs.claude.com or code.claude.com, the page on subagents)
- YouTube Help: upload requirements, chapters, end screens, cards, AI-content disclosure
- Opus Clip API docs (which endpoints exist, the `clip-projects` listing lesson)
- One named producer or showrunner workflow source with a dated piece on production tracking and handoff checklists
- YouTube Creator Academy or Help on Shorts specs
Local material is input, not proof: `WWD\CLAUDE.md`, `WWD\STANDARDS.md`, `SOP\SOP-WWD-Review-Workflow.md`, `SOP\SOP-Editing-Department.md`, `memory\topics\wwd-skill-formats.md`.

## Step 2: Gap audit (`memory\agents\briefs\wwd-director-gap-audit.md`)
Audit only outputs that exist on disk, name each path, say where it departs from the Craft Brief and what it cost.
Last 5 to 10 real chains: `WWD\reports\Percy-Jackson-S3-E1-2-*` (the 2026-11-23 chain), `A-Knights-Tale-Upload-Package.md`, `FrostCast-Tuesday-Intel-2026-11-24.md`, the EP 122 audio cut and shorts plan, `logs\wwd-director.md`. For each: wrong handoff facts accepted, steps skipped, checks run late, Zac time cost.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\wwd-director-drill-1.md`)
Routing drill, free, no posting. The grader writes 6 handoff messages with traps the agent has not seen, each answerable from files on disk: (a) a season or title mismatch against an official source, (b) a speaker-count mismatch, (c) a request to run a raw-footage transcript pull (locked against, `memory\feedback-no-raw-review-transcripts.md`), (d) a Drive mirror ask with no instruction from Zac, (e) a step that needs a browser the director lacks, (f) a spend or public-post step. Agent returns, per message, the ordered worker chain, the check run before each hand-off, and what goes to Zac. Draft criteria for the grader to finalize: (1) every trap caught, (2) route order matches the SOP-WWD-Review-Workflow, (3) money and posting stopped, (4) browser-less step handed to a named holder, (5) fact claims sent through fact-research, (6) each instruction tagged, (7) UNDRILLED-aware wording. Pass: 6 of 7, with 1, 3 and 4 CRITICAL.
Graded by Jarvis (directors are graded by Jarvis per SOP part 3), with qa-director as second reader of the grader-set traps. The grader writes or sets at least one trap the agent has not seen (lesson from the studio-director and graphic-design drills: a drill the test taker designed proves little). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Wednesday chain hand-back, Upload package, Shorts plan and approved-copy set, Worker handoff message.
6 to 12 yes or no items each, built from the brief and `memory\agents\failures\`. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; failure entries opened (if any) in `memory\agents\failures\wwd-director.md`; the level the evidence supports (a proposal, the grader signs); ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
