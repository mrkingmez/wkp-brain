# Leveling task: assistant-editor

Wave 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-22 by chief-of-staff. Jarvis launches this as one job. Run as `assistant-editor` (spec `D:\WKP\.claude\agents\assistant-editor.md`), or through a general-purpose agent running that spec. Grader: head-editor for craft, qa-director for the file checks, never the agent itself.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\assistant-editor.md` and `SOP\SOP-Output-Locations-and-Formats.md` before starting.

## Why this agent is wave 1
Builds run sheets, sound pulls and rough cuts that Zac edits from. Zac works in fragments of time (feedback-run-guide-not-straight-cuts), so a weak run sheet costs him real hours. Ian trailer v5 still needed fixes (lopsided blur bars).

## Step 1: Craft Brief (`memory\agents\briefs\assistant-editor-craft-brief.md`)
Retrieve and quote (URL, retrieved date, verbatim quote). The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write NOT RETRIEVED for any page that cannot be fetched. Never fill from memory.
- Adobe Premiere Pro help: sequences, nested timelines, markers, export and audio loudness (helpx.adobe.com)
- EBU R128 and ITU-R BS.1770 loudness references, plus YouTube Help on loudness (our lock is -14 LUFS, verify what YouTube states)
- ffmpeg documentation: loudnorm, concat, scale and pad filters
- Walter Murch, In the Blink of an Eye (retrievable excerpts or interview), cutting priorities
- One or two named editors with dated Premiere workflow tutorials on assembly and J and L cuts
- Netflix or BBC delivery specs for audio and picture, as a primary standard
Target 5 to 10 retrieved sources, at most 2 community. Local material to read as input, not as proof: `SOP\SOP-Editing-Department.md`, `Post-Production\reports\Zac-Style-Sheet-2026-11-19.md`, `memory\feedback-sound-pull.md`, `D:\WKP Reports\Asset Placement Run Sheets\`.

## Step 2: Gap audit (`memory\agents\briefs\assistant-editor-gap-audit.md`)
Audit the A Knight's Tale PREP stringout (plan `WWD\reports\A-Knights-Tale-Prep-Assembly-Plan.md`, QA report `A-Knights-Tale-Stringout-QA-2026-11-19.md`) and the Ian trailer v1 to v5 files and gap list. Compare to the head-editor notes (22 gaps over 20 s) and to Zac's final export when it exists.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\assistant-editor-drill-1.md`)
Replay drill, free: given the finished Vision Quest EP 8 transcript and 31 pictures, build the run sheet, then compare to the one already shipped (`D:\WKP Reports\Asset Placement Run Sheets\2026-11-17 - Vision Quest EP 8 Edit Run Sheet.docx`) and to the style sheet. Criteria written before the run: (1) every picture stop has a timecode that lands on the spoken line in the transcript, (2) no picture used twice, (3) sound pull folder matches the run sheet, (4) lint passes, (5) gaps listed with durations, (6) loudness and black tail checks listed, (7) every instruction tagged. Pass: 6 of 7, with 1 and 2 CRITICAL.
Graded by head-editor for craft, qa-director for the file checks. Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Edit run sheet, prep stringout, sound pull folder, rough cut with gap list
6 to 12 yes or no items each. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (Part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; the failure entries opened (if any) in `memory\agents\failures\assistant-editor.md`; the level the evidence supports (a proposal, the grader signs); a ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
