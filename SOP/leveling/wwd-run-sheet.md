# Leveling task: wwd-run-sheet

Wave 2, batch 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-26 by chief-of-staff on Jarvis's order (Zac 2026-11-26: "Let's get them learning and growing"). Jarvis launches this as one job. Run as `wwd-run-sheet` (spec `D:\WKP\.claude\agents\wwd-run-sheet.md`), or through a general-purpose agent running that spec. Grader: qa-director (with qa-documents for the docx and lint output), never the agent itself. Do NOT self-rate.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\wwd-run-sheet.md` (all lessons, including the 2026-11-26 standing rule on trying the other connected route) and `SOP\SOP-Output-Locations-and-Formats.md` before starting. Level starts at 0 Unrated (no brief, drill or signed evidence exists, checked 2026-11-26: no `wwd-run-sheet-craft-brief.md` in `memory\agents\briefs\`). Until a grader signs a drill PASS, outputs carry the line `UNDRILLED` and go through the director.

## Why this agent is in batch 1
Owns the Edit Run Sheet Zac cuts from. Lessons 2026-11-23 show facts-file timecodes taken from the answering block instead of the claim block (Hades 22:20 not 22:24), a solo cam placed on a block marked for trimming, clip and picture on the same line, and the lint measuring only numbered file names until patched. Zac works in fragments of time (`memory\feedback-run-guide-not-straight-cuts.md`), so a weak sheet costs hours.

## Step 0: Tool check (new, 2026-11-26)
Spec tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch. Needs: Python with python-docx and the lint script (`.claude\skills\wwd-review-photo-pull\scripts\lint_run_sheet.py`) through Bash. No browser needed. Check: confirm Python312 path works with `-I` and that md_to_docx.py runs; report NOT RUN if not.
First line of every hand-back from this job: the tools actually available in the run, and any step that needed a tool the run did not have. A step that could not run is reported as NOT RUN, never skipped silently. If a tool or source fails, try the other connected route before escalating (standing rule, Zac 2026-11-26); never spoof headers or user agents.

## Step 1: Craft Brief (`memory\agents\briefs\wwd-run-sheet-craft-brief.md`)
Format and rules per SOP part 1: 5 to 10 primary sources, at most 2 community, each with URL or path, retrieved date and 1 to 3 VERBATIM quotes. Fewer than 5 retrieved means INCOMPLETE and no rating above Level 1. Tag every claim PROVEN, SOURCED, COMMUNITY or PROPOSED. The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write `NOT RETRIEVED: <url>, <reason>` for any page that cannot be fetched. Never fill from memory.
- Adobe Premiere Pro help: sequences, markers, transitions (helpx.adobe.com)
- YouTube Help: chapters, cards and end screen timing
- A named editor's dated piece on cutting to dialogue or podcast-to-video pacing (Walter Murch, "In the Blink of an Eye", only if a retrievable excerpt exists)
- Premiere Pro keyboard and nesting docs for the instructions Zac follows
- The lint script's own rules file as a local PROVEN source
Local material is input, not proof: `WWD\STANDARDS.md`, `SOP\SOP-WWD-Review-Workflow.md`, `memory\feedback-two-shot-base.md`, `memory\feedback-no-actor-tags.md`, `memory\feedback-clip-length.md`.

## Step 2: Gap audit (`memory\agents\briefs\wwd-run-sheet-gap-audit.md`)
Audit only outputs that exist on disk, name each path, say where it departs from the Craft Brief and what it cost.
`WWD\reports\Vision-Quest-8-Edit-Run-Sheet.md`, `A-Knights-Tale-Edit-Run-Sheet.md`, `Percy-Jackson-S3-E1-2-Edit-Run-Sheet.md` and `Godzilla-Minus-Zero-Edit-Run-Sheet.md`. Compare each to Zac's actual edit where a final transcript or export exists (A Knight's Tale: prep stringout vs final). Count lint failures, stops Zac moved, picture reuse, stops over 7 s.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\wwd-run-sheet-drill-1.md`)
Replay drill, free. Grader gives a 6 minute slice of a past transcript the agent has not worked, plus a picture list and clip list with traps: a facts file with a timecode that points at the answering block, one trim-recommended block, a picture reused, a 9 s hold, a clip and a picture on the same line, an actor-tag request. Agent builds the run sheet slice and runs the lint. Draft criteria: (1) lint exit clean, (2) every cut from the claim block, (3) no reuse, none over 7 s, (4) about half designed transitions with Cross Dissolve on 3 at most, (5) conditional stop marked on the trim block, (6) LIKE AND SUBSCRIBE stop present, no actor tags, (7) instructions tagged. Pass: 6 of 7, with 1, 2 and 3 CRITICAL.
Graded by qa-director (with qa-documents for the docx and lint output). The grader writes or sets at least one trap the agent has not seen (lesson from the studio-director and graphic-design drills: a drill the test taker designed proves little). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Edit Run Sheet (md and docx), Run sheet revision after a transcript change.
6 to 12 yes or no items each, built from the brief and `memory\agents\failures\`. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; failure entries opened (if any) in `memory\agents\failures\wwd-run-sheet.md`; the level the evidence supports (a proposal, the grader signs); ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
