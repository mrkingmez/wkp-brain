# Leveling task: qa-media

Wave 2, batch 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-26 by chief-of-staff on Jarvis's order (Zac 2026-11-26: "Let's get them learning and growing"). Jarvis launches this as one job. Run as `qa-media` (spec `D:\WKP\.claude\agents\qa-media.md`), or through a general-purpose agent running that spec. Grader: qa-director (director grades its own bench, SOP part 3) with qa-auditor as second reader, never the agent itself. Do NOT self-rate.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\qa-media.md` (all lessons, including the 2026-11-26 standing rule on trying the other connected route) and `SOP\SOP-Output-Locations-and-Formats.md` before starting. Level starts at 0 Unrated (no brief, drill or signed evidence exists, checked 2026-11-26: no `qa-media-craft-brief.md` in `memory\agents\briefs\`). Until a grader signs a drill PASS, outputs carry the line `UNDRILLED` and go through the director.

## Why this agent is in batch 1
Every export is checked by this bench before Zac sees it. Real lessons on file: ebur128 on stereo of a dual-mono voice reads 3 dB higher than the mono downmix (2026-11-26), wrong-speaker windows must be computed not trusted from a plan file, a bare `\a` in a Windows path became a BEL character. A QA bench that misses a defect is worse than none, so this one gets a planted-defect drill.

## Step 0: Tool check (new, 2026-11-26)
Spec tools: Read, Write, Glob, Grep, Bash (no Edit, no web). Needs ffprobe, ffmpeg and Python312 with numpy via Bash. Check the paths in LOCAL-PATHS work and that `scratch\qa\` exists (create on first use). Known limit: cannot listen, so every audio claim is a measurement only; say so in the report.
First line of every hand-back from this job: the tools actually available in the run, and any step that needed a tool the run did not have. A step that could not run is reported as NOT RUN, never skipped silently. If a tool or source fails, try the other connected route before escalating (standing rule, Zac 2026-11-26); never spoof headers or user agents.

## Step 1: Craft Brief (`memory\agents\briefs\qa-media-craft-brief.md`)
Format and rules per SOP part 1: 5 to 10 primary sources, at most 2 community, each with URL or path, retrieved date and 1 to 3 VERBATIM quotes. Fewer than 5 retrieved means INCOMPLETE and no rating above Level 1. Tag every claim PROVEN, SOURCED, COMMUNITY or PROPOSED. The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write `NOT RETRIEVED: <url>, <reason>` for any page that cannot be fetched. Never fill from memory.
- ffmpeg documentation: ebur128, loudnorm, blackdetect, freezedetect, silencedetect, signalstats
- EBU R128 and ITU-R BS.1770 (the standards)
- YouTube Help on loudness normalization
- YouTube Help on recommended upload encoding settings (resolution, frame rate, codec, bitrate)
- Netflix partner help or BBC technical delivery standard on QC defect classes (black, freeze, loudness)
- A named engineer's dated piece on automated video QC
Local material is input, not proof: `.claude\agents\qa-media.md`, `logs\qa\2026-11-26-percy-v3.md`, `WWD\reports\A-Knights-Tale-Stringout-QA-2026-11-19.md`, `WWD\STANDARDS.md`.

## Step 2: Gap audit (`memory\agents\briefs\qa-media-gap-audit.md`)
Audit only outputs that exist on disk, name each path, say where it departs from the Craft Brief and what it cost.
`logs\qa\2026-11-26-percy-v3.md`, `A-Knights-Tale-Stringout-QA-2026-11-19.md`, `logs\qa\2026-11-17-vision-quest-8-upload-package.md`, `logs\qa\2026-11-20-ian-draft3-3.md`. For each: checks run, checks the spec lists but the report omits, any defect Zac or a later pass found that the report passed.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\qa-media-drill-1.md`)
Planted-defect drill, free. qa-director builds 6 short test files in scratch with ffmpeg (the agent does not see the recipe): one clean file; one at -24 LUFS; one with a 10 s black tail; one with a repeated segment; one with no audio stream; one at the wrong resolution or frame rate. Agent checks all six against the WWD standards and reports. Draft criteria: (1) all 5 defects found, (2) clean file passes with no false alarm, (3) numbers within 0.5 LU and 0.1 s of the grader's measure, (4) each finding names the command used, (5) states what was not verified (listening), (6) report only, no file edited, (7) instructions tagged. Pass: 6 of 7, with 1, 2 and 6 CRITICAL.
Graded by qa-director (director grades its own bench, SOP part 3) with qa-auditor as second reader. The grader writes or sets at least one trap the agent has not seen (lesson from the studio-director and graphic-design drills: a drill the test taker designed proves little). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: QA report on an export, Loudness and black tail check.
6 to 12 yes or no items each, built from the brief and `memory\agents\failures\`. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; failure entries opened (if any) in `memory\agents\failures\qa-media.md`; the level the evidence supports (a proposal, the grader signs); ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
