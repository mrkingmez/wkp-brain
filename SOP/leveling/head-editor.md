# Leveling task: head-editor

Wave 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-22 by chief-of-staff. Jarvis launches this as one job. Run as `head-editor` (spec `D:\WKP\.claude\agents\head-editor.md`), or through a general-purpose agent running that spec. Grader: qa-director (qa-media) and Jarvis spot-check, never the agent itself.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\head-editor.md` and `SOP\SOP-Output-Locations-and-Formats.md` before starting.

## Why this agent is wave 1
Sets the editing standard and QA of cuts. Godzilla pre-post fixes found a repeated picture and a 10.5 s black tail after the fact; all 8 reviews missed the -14 LUFS standard (Zac Style Sheet 2026-11-19).

## Step 1: Craft Brief (`memory\agents\briefs\head-editor-craft-brief.md`)
Retrieve and quote (URL, retrieved date, verbatim quote). The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write NOT RETRIEVED for any page that cannot be fetched. Never fill from memory.
- Adobe Premiere Pro help on export, color and audio workflows (helpx.adobe.com)
- EBU R128 and ITU-R BS.1770 loudness standards; YouTube Help loudness statement
- Walter Murch, In the Blink of an Eye, rule of six (retrieved text)
- Netflix or BBC technical delivery specifications (primary standards)
- Two named editors or channels with dated breakdowns of pacing, retention and cutaways
- YouTube Help or Creator Academy on retention analytics
Target 5 to 10 retrieved sources, at most 2 community. Local material to read as input, not as proof: `Post-Production\reports\Zac-Style-Sheet-2026-11-19.md`, `Post-Production\research\editing-study\`, `SOP\SOP-Editing-Department.md`.

## Step 2: Gap audit (`memory\agents\briefs\head-editor-gap-audit.md`)
Audit the head-editor notes on the A Knight's Tale stringout, the Style Sheet findings, and the Godzilla Minus Zero cut (repeated picture, black tail, loudness -24.7 LUFS). Which of those would a retrieved standard have caught before post?
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\head-editor-drill-1.md`)
Free drill: given 3 finished review videos on disk (Godzilla, Vision Quest 7, Vision Quest 8) run a pre-post QA with ffprobe and a loudness measure, and list defects. A known-defects list (repeated picture, black tail) is held by the grader and not shown. Criteria: (1) finds both known defects, (2) measures loudness with the command shown, (3) cites the loudness standard with quote, (4) no false claims about frames not looked at, (5) fix list ordered by Zac time, (6) every instruction tagged. Pass: 5 of 6, with 1 and 2 CRITICAL.
Graded by qa-director (qa-media) and Jarvis spot-check. Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Pre-post QA report, editing notes on a stringout, final export check
6 to 12 yes or no items each. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (Part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; the failure entries opened (if any) in `memory\agents\failures\head-editor.md`; the level the evidence supports (a proposal, the grader signs); a ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
