# Leveling task: wwd-rights

Wave 2, batch 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-26 by chief-of-staff on Jarvis's order (Zac 2026-11-26: "Let's get them learning and growing"). Jarvis launches this as one job. Run as `wwd-rights` (spec `D:\WKP\.claude\agents\wwd-rights.md`), or through a general-purpose agent running that spec. Grader: qa-director (with qa-claims re-fetching license pages and qa-documents for the risk note), never the agent itself. Do NOT self-rate.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\wwd-rights.md` (all lessons, including the 2026-11-26 standing rule on trying the other connected route) and `SOP\SOP-Output-Locations-and-Formats.md` before starting. Level starts at 0 Unrated (no brief, drill or signed evidence exists, checked 2026-11-26: no `wwd-rights-craft-brief.md` in `memory\agents\briefs\`). Until a grader signs a drill PASS, outputs carry the line `UNDRILLED` and go through the director.

## Why this agent is in batch 1
Writes the fair use and clearance risk note before every package. Real catches and gaps on file: A Knight's Tale final cut flagged 17 loose or audioblocks files with no license record; Vision Quest 8 has pictures with no source page and a CC BY-SA question left open; the Adobe MUSIC tree is not covered by Zac's SFX-library call (lesson 2026-11-23). Longer clips (6 to 12 s) raise exposure (`memory\feedback-clip-length.md`).

## Step 0: Tool check (new, 2026-11-26)
Spec tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch. Needs live page fetch for licence terms (WebFetch) and frame viewing (Bash, ffmpeg, Read of images). No browser needed except for pages WebFetch cannot reach; if one is blocked, say which route was tried next. Flags risk, never legal advice.
First line of every hand-back from this job: the tools actually available in the run, and any step that needed a tool the run did not have. A step that could not run is reported as NOT RUN, never skipped silently. If a tool or source fails, try the other connected route before escalating (standing rule, Zac 2026-11-26); never spoof headers or user agents.

## Step 1: Craft Brief (`memory\agents\briefs\wwd-rights-craft-brief.md`)
Format and rules per SOP part 1: 5 to 10 primary sources, at most 2 community, each with URL or path, retrieved date and 1 to 3 VERBATIM quotes. Fewer than 5 retrieved means INCOMPLETE and no rating above Level 1. Tag every claim PROVEN, SOURCED, COMMUNITY or PROPOSED. The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write `NOT RETRIEVED: <url>, <reason>` for any page that cannot be fetched. Never fill from memory.
- US Copyright Office, Fair Use Index and Circular 33 or the fair use overview page
- Stanford Copyright and Fair Use Center, fair use factors
- YouTube Help: copyright claims, Content ID, fair use explanation
- Creative Commons BY-SA 4.0 legal code and the official FAQ on share-alike scope (the open Vision Quest 8 attorney question)
- Adobe stock and SFX licence terms; Pixabay Content License summary
- YouTube Help on altered or synthetic content disclosure
Local material is input, not proof: `WWD\reports\A-Knights-Tale-Rights-Note.md`, `Vision-Quest-8-Rights-Note.md`, `Percy-Jackson-S3-E1-2-Rights-Note.md`, `data\assets\p-drive-index.csv`, `memory\topics\marketing-sponsors.md`.

## Step 2: Gap audit (`memory\agents\briefs\wwd-rights-gap-audit.md`)
Audit only outputs that exist on disk, name each path, say where it departs from the Craft Brief and what it cost.
The three rights notes above and `Godzilla-Minus-Zero-Rights-Note.md`. For each: claims resting on memory not a retrieved page, flags raised late, flags Zac later had to resolve, counts that did not match the final export.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\wwd-rights-drill-1.md`)
Replay drill, free. Grader builds a 10-item asset list from a past project with traps: a CC BY-SA photo with no credit line, a loose mp3 with encoder=Google tags, an Adobe MUSIC file, a 14 s clip, an AI-made intro, a picture from the wrong series. Agent returns a risk note with HIGH, MEDIUM and LOW counts and the exact fix per item. Draft criteria: (1) all 6 traps caught, (2) each licence claim quoted from a retrieved page with URL and date, (3) total clip seconds and risk level stated, (4) AI-made items flagged until Zac confirms, (5) states risk not legal advice, (6) counts marked "verify against the export", (7) instructions tagged. Pass: 6 of 7, with 1, 2 and 4 CRITICAL.
Graded by qa-director (with qa-claims re-fetching license pages and qa-documents for the risk note). The grader writes or sets at least one trap the agent has not seen (lesson from the studio-director and graphic-design drills: a drill the test taker designed proves little). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Fair use risk note, Rights re-check after a cut change.
6 to 12 yes or no items each, built from the brief and `memory\agents\failures\`. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; failure entries opened (if any) in `memory\agents\failures\wwd-rights.md`; the level the evidence supports (a proposal, the grader signs); ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
