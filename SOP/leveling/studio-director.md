# Leveling task: studio-director

Wave 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-22 by chief-of-staff. Jarvis launches this as one job. Run as `studio-director` (spec `D:\WKP\.claude\agents\studio-director.md`), or through a general-purpose agent running that spec. Grader: Jarvis (director level) with qa-director, never the agent itself.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\studio-director.md` and `SOP\SOP-Output-Locations-and-Formats.md` before starting.

## Why this agent is wave 1
Gates every video production package (client work, trailers, short films). The Ian trailer package passed gates yet the secret was misread twice (drafts 3.1 and 3.2) and credits ran to zero before shots were done.

## Step 1: Craft Brief (`memory\agents\briefs\studio-director-craft-brief.md`)
Retrieve and quote (URL, retrieved date, verbatim quote). The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write NOT RETRIEVED for any page that cannot be fetched. Never fill from memory.
- Adobe Premiere Pro and After Effects help: project organization and handoff (helpx.adobe.com)
- Production management references: Producers Guild or similar published workflow guides, or a named producer's dated breakdown of pre-production for a micro-budget short
- Netflix or BBC delivery specifications (as the quality gate for a final package)
- A named animation or VFX studio's dated description of its pipeline
- Published resource on clearance and E and O basics (to know what to ask a lawyer)
- YouTube Help on AI-generated content disclosure (relevant to Ian and WWD)
Target 5 to 10 retrieved sources, at most 2 community. Local material to read as input, not as proof: `logs\studio-director.md`, `Post-Production\reports\Ian-Wrench-Turner-Trailer-Draft3-3.md`, `memory\project-ian-trailer-settled.md`, `memory\project-ian-trailer-secret.md`.

## Step 2: Gap audit (`memory\agents\briefs\studio-director-gap-audit.md`)
Audit the Ian trailer production chain: brief reading (the secret), gates run (`logs\qa\2026-11-20-ian-draft3-3.md`), credit planning before generation, point-man handoffs. Which gate would a retrieved production standard have added?
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\studio-director-drill-1.md`)
Free drill: given a one paragraph client brief with a planted trap (a fact that must not be revealed and a missing license), produce a production package plan. Criteria written before the run: (1) finds the planted trap and fences it, (2) names the point man and the order of departments, (3) credit and money plan with exact cost left as NOT RETRIEVED until read, (4) rights and AI disclosure items listed, (5) gates sequence with who signs, (6) every instruction tagged. Pass: 5 of 6, with 1 and 3 CRITICAL.
Graded by Jarvis (director level) with qa-director. Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Studio production package, point-man assignment, gate sign-off record
6 to 12 yes or no items each. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (Part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; the failure entries opened (if any) in `memory\agents\failures\studio-director.md`; the level the evidence supports (a proposal, the grader signs); a ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
