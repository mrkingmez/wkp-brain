# Leveling task: media-manager

Wave 2, batch 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-26 by chief-of-staff on Jarvis's order (Zac 2026-11-26: "Let's get them learning and growing"). Jarvis launches this as one job. Run as `media-manager` (spec `D:\WKP\.claude\agents\media-manager.md`), or through a general-purpose agent running that spec. Grader: qa-director (with qa-documents checking the license notes), never the agent itself. Do NOT self-rate.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\media-manager.md` (all lessons, including the 2026-11-26 standing rule on trying the other connected route) and `SOP\SOP-Output-Locations-and-Formats.md` before starting. Level starts at 0 Unrated (no brief, drill or signed evidence exists, checked 2026-11-26: no `media-manager-craft-brief.md` in `memory\agents\briefs\`). Until a grader signs a drill PASS, outputs carry the line `UNDRILLED` and go through the director.

## Why this agent is in batch 1
Answers every "where is the" and "do we have a" and keeps the media map and VIDEO-LIBRARY. Lessons show path misses: finished exports live in each movie folder not `...\Final` (2026-11-20), the Made SFX folder was checked late, a Muisc folder is empty. Owner of `REFERENCE\VIDEO-LIBRARY.md` and the library rule: YouTube ID NOT KNOWN until Zac pastes the link.

## Step 0: Tool check (new, 2026-11-26)
Spec tools: Read, Write, Edit, Glob, Grep, Bash (no web needed). Check that Bash can list L:, P:, N: and E: (E: opens read only), and that `data\assets\media-map.md`, `p-drive-index.csv` and `music-catalog.md` are readable. Report any drive not mounted as NOT AVAILABLE with the drive letter.
First line of every hand-back from this job: the tools actually available in the run, and any step that needed a tool the run did not have. A step that could not run is reported as NOT RUN, never skipped silently. If a tool or source fails, try the other connected route before escalating (standing rule, Zac 2026-11-26); never spoof headers or user agents.

## Step 1: Craft Brief (`memory\agents\briefs\media-manager-craft-brief.md`)
Format and rules per SOP part 1: 5 to 10 primary sources, at most 2 community, each with URL or path, retrieved date and 1 to 3 VERBATIM quotes. Fewer than 5 retrieved means INCOMPLETE and no rating above Level 1. Tag every claim PROVEN, SOURCED, COMMUNITY or PROPOSED. The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write `NOT RETRIEVED: <url>, <reason>` for any page that cannot be fetched. Never fill from memory.
- Adobe Premiere Pro help on project organization, bins and Media Browser
- A named post-production or DAM source on file naming and asset logs (dated)
- Adobe stock and SFX library license page (what the note on each file should say)
- Pixabay Content License summary (for the license note format)
- YouTube Help on video IDs and URLs (for the library rule)
- The Premiere project panel and proxy documentation only if it changes how paths are recorded
Local material is input, not proof: `data\assets\media-map.md`, `data\assets\music-catalog.md`, `REFERENCE\VIDEO-LIBRARY.md`, `REFERENCE\README.md`, `LOCAL-PATHS.md`, `SOP\SOP-Editing-Department.md`.

## Step 2: Gap audit (`memory\agents\briefs\media-manager-gap-audit.md`)
Audit only outputs that exist on disk, name each path, say where it departs from the Craft Brief and what it cost.
Last real lookups and asset lists: `media-map.md`, the Ian Draft 3.3 asset list, the Percy Jackson sound pull, VIDEO-LIBRARY rows added after FrostCast EP 121 and EP 122. Count wrong paths, missing license notes, stale rows (older than 7 days).
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\media-manager-drill-1.md`)
Lookup drill, free. Grader asks 10 questions it can answer from disk: 6 findable items (a sound, a LUT, a kit piece, a finished export, a FrostCast chapter file, a VIDEO-LIBRARY row), 2 items that do not exist (must answer NOT FOUND and name where it looked), 1 with two copies (must pick and say which), 1 where a moved folder makes the media map stale (must catch it). Draft criteria: (1) every path exists when the grader opens it, (2) NOT FOUND answers name the places searched, (3) license note on each item or flagged unknown, (4) stale map line caught, (5) no file moved, renamed or deleted, (6) no invented YouTube ID, (7) instructions tagged. Pass: 6 of 7, with 1, 2 and 5 CRITICAL.
Graded by qa-director (with qa-documents checking the license notes). The grader writes or sets at least one trap the agent has not seen (lesson from the studio-director and graphic-design drills: a drill the test taker designed proves little). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Asset list for an edit, VIDEO-LIBRARY row, Media map update.
6 to 12 yes or no items each, built from the brief and `memory\agents\failures\`. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; failure entries opened (if any) in `memory\agents\failures\media-manager.md`; the level the evidence supports (a proposal, the grader signs); ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
