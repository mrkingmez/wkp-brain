# Leveling task: music

Wave 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-22 by chief-of-staff. Jarvis launches this as one job. Run as `music` (spec `D:\WKP\.claude\agents\music.md`), or through a general-purpose agent running that spec. Grader: qa-director with qa-documents for license records, never the agent itself.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\music.md` and `SOP\SOP-Output-Locations-and-Formats.md` before starting.

## Why this agent is wave 1
Every music request goes here. Music cost Zac time and risk: the Ian trailer pick needed a license receipt, an Alex Morgan track was dropped because it was labeled AI generated, the ElevenLabs music Individual Use question is open, and the intro sting must be 6 s or less.

## Step 1: Craft Brief (`memory\agents\briefs\music-craft-brief.md`)
Retrieve and quote (URL, retrieved date, verbatim quote). The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write NOT RETRIEVED for any page that cannot be fetched. Never fill from memory.
- Pixabay Content License page (pixabay.com/service/license-summary)
- YouTube Help on Content ID, reuse and copyright claims on music
- YouTube Audio Library terms
- ElevenLabs terms and music license pages (commercial use, Individual Use question)
- Adobe SFX library license terms Zac already uses
- Suno terms (which plan allows commercial use), only to document why it is not used
- One named music supervisor or editor with a dated piece on picking and cutting music to picture
Target 5 to 10 retrieved sources, at most 2 community. Local material to read as input, not as proof: `SOP\SOP-Music-Department.md`, `.claude\agents\_spec\music-reference.md`, `data\assets\music-catalog.md`, `memory\feedback-intro-length.md`.

## Step 2: Gap audit (`memory\agents\briefs\music-gap-audit.md`)
Audit the Ian trailer music recommendation (`Post-Production\reports\Ian-Wrench-Turner-Trailer-Draft3-3.md` Appendix E), the A Knight's Tale sound plan (`WWD\reports\A-Knights-Tale-Sound-Plan.md`), the ElevenLabs month plan, and the catalog. Where did a license claim rest on memory instead of a retrieved page?
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\music-drill-1.md`)
Free drill: pick music for a 45 s trailer and a 6 s sting from free licensed sources only. Deliver 3 options each with the license page retrieved, quote, URL, date, Content ID status, a saved receipt path, and cut points. Criteria: (1) license text quoted from the retrieved page, (2) no track labeled AI generated slipped in, (3) sting 6 s or less, (4) receipt saved and path given, (5) Content ID risk stated with source, (6) every claim tagged. Pass: 5 of 6, with 1, 2 and 4 CRITICAL.
Graded by qa-director with qa-documents for license records. Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Music pick card with license receipt, sting or intro cut, ElevenLabs sound request
6 to 12 yes or no items each. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (Part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; the failure entries opened (if any) in `memory\agents\failures\music.md`; the level the evidence supports (a proposal, the grader signs); a ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
