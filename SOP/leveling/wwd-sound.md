# Leveling task: wwd-sound

Wave 2, batch 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-26 by chief-of-staff on Jarvis's order (Zac 2026-11-26: "Let's get them learning and growing"). Jarvis launches this as one job. Run as `wwd-sound` (spec `D:\WKP\.claude\agents\wwd-sound.md`), or through a general-purpose agent running that spec. Grader: qa-director (with qa-media re-measuring loudness), never the agent itself. Do NOT self-rate.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\wwd-sound.md` (all lessons, including the 2026-11-26 standing rule on trying the other connected route) and `SOP\SOP-Output-Locations-and-Formats.md` before starting. Level starts at 0 Unrated (no brief, drill or signed evidence exists, checked 2026-11-26: no `wwd-sound-craft-brief.md` in `memory\agents\briefs\`). Until a grader signs a drill PASS, outputs carry the line `UNDRILLED` and go through the director.

## Why this agent is in batch 1
Owns sound matching and loudness for every review. `memory\agents\wwd-sound.md` has no real-job lesson yet (the Lessons header is empty, checked 2026-11-26), which means no learning has been recorded. TASKS 2026-11-20 states all 8 reviews miss the -14 LUFS standard, and Godzilla Minus Zero measured -24.7 LUFS (`TASKS.md`). Sound-plan hygiene already cost a rebuild (A Knight's Tale plan sat in scratch).

## Step 0: Tool check (new, 2026-11-26)
Spec tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch. Needs ffmpeg ebur128 and a read of the P: sound index (`data\assets\p-drive-index.csv`). Check: confirm the agent can run ebur128 per section (stereo vs mono lesson from qa-media 2026-11-26: a dual-mono voice reads 3 dB higher on stereo).
First line of every hand-back from this job: the tools actually available in the run, and any step that needed a tool the run did not have. A step that could not run is reported as NOT RUN, never skipped silently. If a tool or source fails, try the other connected route before escalating (standing rule, Zac 2026-11-26); never spoof headers or user agents.

## Step 1: Craft Brief (`memory\agents\briefs\wwd-sound-craft-brief.md`)
Format and rules per SOP part 1: 5 to 10 primary sources, at most 2 community, each with URL or path, retrieved date and 1 to 3 VERBATIM quotes. Fewer than 5 retrieved means INCOMPLETE and no rating above Level 1. Tag every claim PROVEN, SOURCED, COMMUNITY or PROPOSED. The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write `NOT RETRIEVED: <url>, <reason>` for any page that cannot be fetched. Never fill from memory.
- YouTube Help on loudness normalization (the official statement of the playback level and how it adjusts)
- EBU R128 and ITU-R BS.1770 (the standards themselves, or the EBU tech document)
- ffmpeg ebur128 filter documentation
- Adobe Premiere Pro help: Essential Sound, ducking, loudness
- Adobe stock and SFX library license terms Zac relies on
- A named audio engineer's dated piece on dialogue-first podcast and video mixing
Local material is input, not proof: `SOP\SOP-Music-Department.md`, `WWD\reports\Godzilla-Sound-Cue-Sheet.md`, `WWD\reports\A-Knights-Tale-Sound-Plan.md`, `WWD\reports\Percy-Jackson-S3-E1-2-Sound-Pull.md`, `memory\feedback-intro-length.md`.

## Step 2: Gap audit (`memory\agents\briefs\wwd-sound-gap-audit.md`)
Audit only outputs that exist on disk, name each path, say where it departs from the Craft Brief and what it cost.
The three sound files above plus the A Knight's Tale rights note (loose mp3 flags). Count: levels given as fact when only proposed, loudness targets missing, sounds with no license note, cues with no source path.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\wwd-sound-drill-1.md`)
Replay drill, free. Grader supplies a past export slice the agent has not measured and a 12-cue list with traps: one cue whose file does not exist on P:, one loose mp3 with no license, one cue that would sit over a voice, trailer audio unmuted. Agent returns a sound plan and measured numbers. Draft criteria: (1) per-section LUFS and true peak match the grader's own measure within 0.5 LU, (2) -14 LUFS and -1 dBTP target stated with the source quote, (3) trailer audio muted rule applied, (4) missing and unlicensed files flagged by path, (5) levels tagged PROPOSED unless used in a finished cut, (6) plan saved to `WWD\reports\<Movie>-Sound-Plan.md`, (7) instructions tagged. Pass: 6 of 7, with 1, 2 and 4 CRITICAL.
Graded by qa-director (with qa-media re-measuring loudness). The grader writes or sets at least one trap the agent has not seen (lesson from the studio-director and graphic-design drills: a drill the test taker designed proves little). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Sound plan, Loudness and mix check report.
6 to 12 yes or no items each, built from the brief and `memory\agents\failures\`. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; failure entries opened (if any) in `memory\agents\failures\wwd-sound.md`; the level the evidence supports (a proposal, the grader signs); ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
