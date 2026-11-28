# Leveling task: wwd-vfx

Wave 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-22 by chief-of-staff. Jarvis launches this as one job. Run as `wwd-vfx` (spec `D:\WKP\.claude\agents\wwd-vfx.md`), or through a general-purpose agent running that spec. Grader: qa-director (qa-media for the render check), never the agent itself.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\wwd-vfx.md` and `SOP\SOP-Output-Locations-and-Formats.md` before starting.

## Why this agent is wave 1
Builds end cards, Next Up cards, stings and the cold open with Firefly, After Effects and free tools. Every miss costs credits (the A Knight's Tale intro sting had to be 6 s or less, 11 to 12 s was way too long) or Zac's edit time.

## Step 1: Craft Brief (`memory\agents\briefs\wwd-vfx-craft-brief.md`)
Retrieve and quote (URL, retrieved date, verbatim quote). The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write NOT RETRIEVED for any page that cannot be fetched. Never fill from memory.
- Adobe After Effects user guide: expressions, essential graphics and .mogrt export (helpx.adobe.com)
- Adobe Premiere Pro help on motion graphics templates and export settings
- Adobe Firefly video help for the model that makes stings (start frame, duration, credit cost per generation)
- ffmpeg official documentation for filters used on cards (ffmpeg.org/ffmpeg-filters.html)
- YouTube Help: end screen and card specs and timing
- One or two named motion designers with dated tutorials on titles, end cards and logo stings
Target 5 to 10 retrieved sources, at most 2 community. Local material to read as input, not as proof: `.claude\agents\_spec\wwd-vfx-toolkit.md`, `memory\feedback-intro-length.md`, `P:\WWD Kit\Cards\`, `SOP\SOP-WWD-Review-Workflow.md`.

## Step 2: Gap audit (`memory\agents\briefs\wwd-vfx-gap-audit.md`)
Audit the End Card and Next Up cards for A Knight's Tale and Vision Quest (files in `P:\WWD Kit\Cards\`), the 6 s intro and 18 s outro cuts in `scratch\akt-music\`, and the cold open draft. Check duration, safe margins, end screen timing against YouTube Help, and credit use.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\wwd-vfx-drill-1.md`)
Free drill: build a 12 s end card and a 6 s sting from owned assets only (no credits) to a written spec with ffmpeg or After Effects. Criteria written before the run: (1) exact durations, (2) 1920x1080 at the show frame rate, (3) text inside safe margins, (4) end screen element zones match the YouTube Help spec quoted, (5) no video-model credits used (ledger shows $0 and 0 credits), (6) ffprobe output pasted, (7) every instruction tagged. Pass: 6 of 7, with 1, 4 and 5 CRITICAL.
Graded by qa-director (qa-media for the render check). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: End card, Next Up card, sting or intro cut, cold open shot list
6 to 12 yes or no items each. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (Part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; the failure entries opened (if any) in `memory\agents\failures\wwd-vfx.md`; the level the evidence supports (a proposal, the grader signs); a ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
