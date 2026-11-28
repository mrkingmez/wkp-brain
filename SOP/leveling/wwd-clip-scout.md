# Leveling task: wwd-clip-scout

Wave 2, batch 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-26 by chief-of-staff on Jarvis's order (Zac 2026-11-26: "Let's get them learning and growing"). Jarvis launches this as one job. Run as `wwd-clip-scout` (spec `D:\WKP\.claude\agents\wwd-clip-scout.md`), or through a general-purpose agent running that spec. Grader: qa-director (with qa-media re-running shot detection and frame strips), never the agent itself. Do NOT self-rate.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\wwd-clip-scout.md` (all lessons, including the 2026-11-26 standing rule on trying the other connected route) and `SOP\SOP-Output-Locations-and-Formats.md` before starting. Level starts at 0 Unrated (no brief, drill or signed evidence exists, checked 2026-11-26: no `wwd-clip-scout-craft-brief.md` in `memory\agents\briefs\`). Until a grader signs a drill PASS, outputs carry the line `UNDRILLED` and go through the director.

## Why this agent is in batch 1
Cuts the trailer and scene clips Zac drops under host lines. Lessons 2026-11-23: scene detection missed cuts on dark or fast footage (4 false spans), lightning flashes logged as cuts, word-position timing is an estimate, trailers gave 1 usable shot in 275 s while the Sneak Peek gave 4 of 5 clips. Clip rule: 6 to 8 s, 12 max, inside one shot (`memory\feedback-clip-length.md`).

## Step 0: Tool check (new, 2026-11-26)
Spec tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch. Needs ffmpeg and ffprobe via Bash (path in LOCAL-PATHS), Python312 with numpy, and yt-dlp for the official caption file (lesson 2026-11-23) although spec line 20 says it downloads nothing itself. Check: is yt-dlp present, and is the spec's no-download rule consistent with the caption-only fetch? Queue for a rule decision if not.
First line of every hand-back from this job: the tools actually available in the run, and any step that needed a tool the run did not have. A step that could not run is reported as NOT RUN, never skipped silently. If a tool or source fails, try the other connected route before escalating (standing rule, Zac 2026-11-26); never spoof headers or user agents.

## Step 1: Craft Brief (`memory\agents\briefs\wwd-clip-scout-craft-brief.md`)
Format and rules per SOP part 1: 5 to 10 primary sources, at most 2 community, each with URL or path, retrieved date and 1 to 3 VERBATIM quotes. Fewer than 5 retrieved means INCOMPLETE and no rating above Level 1. Tag every claim PROVEN, SOURCED, COMMUNITY or PROPOSED. The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write `NOT RETRIEVED: <url>, <reason>` for any page that cannot be fetched. Never fill from memory.
- ffmpeg documentation: scene detection filter, select, showinfo, libx264 (ffmpeg.org/ffmpeg-filters.html)
- PySceneDetect documentation (content and adaptive detectors, thresholds)
- US Copyright Office fair use page and the Stanford fair use project on length and amount
- YouTube Help on copyright claims and Content ID for trailer clips
- Studio press-kit terms for official trailers and clips
- Adobe Premiere Pro help on supported codecs (H.264 import)
Local material is input, not proof: `WWD\STANDARDS.md`, `memory\feedback-clip-length.md`, `WWD\reports\Percy-Jackson-S3-E1-2-Clip-Scout.md`.

## Step 2: Gap audit (`memory\agents\briefs\wwd-clip-scout-gap-audit.md`)
Audit only outputs that exist on disk, name each path, say where it departs from the Craft Brief and what it cost.
`Percy-Jackson-S3-E1-2-Clip-Scout.md`, `-Clip-Placements.md`, `Vision-Quest-8-Clip-Scout.md`, the A Knight's Tale clip set. For each: clips that crossed a shot edge, clips outside 6 to 12 s, clips with unverified identity, time lost to false detection.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\wwd-clip-scout-drill-1.md`)
Replay drill on footage already on disk, free. Grader picks a clip file the agent has not scouted and secretly marks 4 true shot edges and 2 flash frames. Agent returns a list of 3 clips of 6 to 8 s, each inside one shot, with in and out times and a 6 fps strip. Draft criteria: (1) all 3 clips inside one shot by the grader's edges, (2) flashes not logged as cuts, (3) length 6 to 8 s (12 max), (4) every candidate verified by a strip 0.5 s each side, (5) unnamed-actor shot held not cut, (6) timing stated as estimate, (7) instructions tagged. Pass: 6 of 7, with 1, 2 and 5 CRITICAL.
Graded by qa-director (with qa-media re-running shot detection and frame strips). The grader writes or sets at least one trap the agent has not seen (lesson from the studio-director and graphic-design drills: a drill the test taker designed proves little). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Clip list with timecodes, Premiere Ready conversion, Shot map.
6 to 12 yes or no items each, built from the brief and `memory\agents\failures\`. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; failure entries opened (if any) in `memory\agents\failures\wwd-clip-scout.md`; the level the evidence supports (a proposal, the grader signs); ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
