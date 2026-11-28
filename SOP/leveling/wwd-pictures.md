# Leveling task: wwd-pictures

Wave 2, batch 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-26 by chief-of-staff on Jarvis's order (Zac 2026-11-26: "Let's get them learning and growing"). Jarvis launches this as one job. Run as `wwd-pictures` (spec `D:\WKP\.claude\agents\wwd-pictures.md`), or through a general-purpose agent running that spec. Grader: qa-director (with qa-media for the perceptual-hash re-run), never the agent itself. Do NOT self-rate.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\wwd-pictures.md` (all lessons, including the 2026-11-26 standing rule on trying the other connected route) and `SOP\SOP-Output-Locations-and-Formats.md` before starting. Level starts at 0 Unrated (no brief, drill or signed evidence exists, checked 2026-11-26: no `wwd-pictures-craft-brief.md` in `memory\agents\briefs\`). Until a grader signs a drill PASS, outputs carry the line `UNDRILLED` and go through the director.

## Why this agent is in batch 1
Zac's own complaint on creation (2026-10-26): same picture twice as different numbers, pictures that do not fit the scene. 2026-11-26: the Percy Jackson S3 missing-picture follow-up could not run the browser step at all because the run had no claude-in-chrome tool (`logs\agent-runs.md` 2026-11-26). Lessons show repeats: scratch deletion denied twice (REPEAT), a retyped-ID 404 rate of 5 of 44, season mismatch.

## Step 0: Tool check (new, 2026-11-26)
Spec tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch. The spec's own skill (`.claude\skills\wwd-review-photo-pull\SKILL.md` line 37) says it needs `mcp__claude-in-chrome__*` (navigate, javascript_tool, find, read_page, browser_batch). CONFIRMED GAP: the tool is not in the spec list. Step 0 for this agent: state at once whether claude-in-chrome is callable and run `list_connected_browsers` first; if not callable, name the other route (press kits via WebFetch, TMDb CDN, iTunes API) and what could not be pulled. Fix queued in `logs\DECISIONS.md` (TOOLS-2026-11-26-01).
First line of every hand-back from this job: the tools actually available in the run, and any step that needed a tool the run did not have. A step that could not run is reported as NOT RUN, never skipped silently. If a tool or source fails, try the other connected route before escalating (standing rule, Zac 2026-11-26); never spoof headers or user agents.

## Step 1: Craft Brief (`memory\agents\briefs\wwd-pictures-craft-brief.md`)
Format and rules per SOP part 1: 5 to 10 primary sources, at most 2 community, each with URL or path, retrieved date and 1 to 3 VERBATIM quotes. Fewer than 5 retrieved means INCOMPLETE and no rating above Level 1. Tag every claim PROVEN, SOURCED, COMMUNITY or PROPOSED. The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write `NOT RETRIEVED: <url>, <reason>` for any page that cannot be fetched. Never fill from memory.
- TMDb API docs on images and image sizes (developer.themoviedb.org)
- IMDb help on image and photo galleries and terms for use of images
- Disney or studio press-site media-kit terms for stills
- US Copyright Office or Stanford Fair Use project page on fair use factors for reviews and commentary
- Pillow docs on resize and thumbnail (contain/fit rule) and a perceptual-hash reference (dHash write-up by a named author, dated)
- Wikimedia Commons reuse and attribution guidance (CC BY-SA, for the Vision Quest 8 photo)
Local material is input, not proof: `WWD\STANDARDS.md`, `.claude\skills\wwd-review-photo-pull\SKILL.md`, `memory\topics\visual-media.md`, `memory\feedback-secondary-pictures.md`.

## Step 2: Gap audit (`memory\agents\briefs\wwd-pictures-gap-audit.md`)
Audit only outputs that exist on disk, name each path, say where it departs from the Craft Brief and what it cost.
`WWD\reports\Percy-Jackson-S3-E1-2-Picture-Pull.md`, `-Picture-Fit.md`, `-Initial-Pull-Report.md`, the A Knight's Tale USE folder tags, `Vision-Quest-8-Edit-Run-Sheet.md` picture section (pictures 14, 20, 21, 23, 24, 27 with no source page recorded). Count duplicates, untagged identifications, missing source URLs, picture-to-line mismatches.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\wwd-pictures-drill-1.md`)
Replay drill on a USE folder already on disk, free, nothing posted. The grader (qa-director via qa-media) plants 3 near-twin pairs (cropped or recolored copies) and 2 wrongly labeled pictures in a COPY of a past USE folder in scratch, with a past transcript. Agent returns the tag file, dup report and fit table. Draft criteria: (1) all 3 planted twins found with the hash numbers, (2) both mislabels caught with what the picture shows, (3) every tag has a source URL or says not available, (4) fit table quotes the transcript line, (5) no picture over 7 s or reused, (6) tool availability stated first and unavailable routes reported NOT RUN, (7) every instruction tagged. Pass: 6 of 7, with 1, 2 and 6 CRITICAL.
Graded by qa-director (with qa-media for the perceptual-hash re-run). The grader writes or sets at least one trap the agent has not seen (lesson from the studio-director and graphic-design drills: a drill the test taker designed proves little). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Picture pull and tag file, Duplicate report, Fit table against the transcript.
6 to 12 yes or no items each, built from the brief and `memory\agents\failures\`. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; failure entries opened (if any) in `memory\agents\failures\wwd-pictures.md`; the level the evidence supports (a proposal, the grader signs); ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
