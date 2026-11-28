# Leveling task: fantasy-football-director

Wave 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-22 by chief-of-staff. Jarvis launches this as one job. Run as `fantasy-football-director` (spec `D:\WKP\.claude\agents\fantasy-football-director.md`), or through a general-purpose agent running that spec. Grader: qa-director with tracking-director for the numbers, never the agent itself.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\fantasy-football-director.md` and `SOP\SOP-Output-Locations-and-Formats.md` before starting.

## Why this agent is wave 1
DFS side: Zac enters real entry fees (7 lineups at $7 for Week 11). Concentration and noon-check misses cost him (feedback-dfs-concentration-check, feedback-noon-check-is-ff-job, project-dfs-learning-goal). Agents never enter lineups or spend.

## Step 1: Craft Brief (`memory\agents\briefs\fantasy-football-director-craft-brief.md`)
Retrieve and quote (URL, retrieved date, verbatim quote). The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write NOT RETRIEVED for any page that cannot be fetched. Never fill from memory.
- DraftKings official rules, scoring and contest pages, plus lineup upload and entries template help (draftkings.com help center)
- FanDuel equivalent rules pages if the FanDuel side is used
- Published DFS research by named practitioners with dated posts on tournament leverage, ownership, correlation and stacking
- Academic work on GPP lineup optimization (Hunter, Vielma and Zaman, integer programming for daily fantasy; retrieve the abstract and the key section)
- nflverse documentation for the data already on disk (nflverse.com)
- NFL official injury report rules and timing (operations.nfl.com)
Target 5 to 10 retrieved sources, at most 2 community. Local material to read as input, not as proof: `Fantasy-Football\dfs\`, `memory\feedback-dfs-concentration-check.md`, `memory\feedback-refresh-before-sims.md`, `memory\project-dfs-learning-goal.md`, `Fantasy-Football\LOG.md`.

## Step 2: Gap audit (`memory\agents\briefs\fantasy-football-director-gap-audit.md`)
Audit Week 10 and Week 11 DFS builds (files in `Fantasy-Football\reports\` and `data\ff-simulator\`) and the DraftKings results where recorded: concentration in 3+ lineups, Q-tagged players, QB-change handling, how the lineup sets compared to the friend's lines. Use only results on disk, else NOT AVAILABLE.
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\fantasy-football-director-drill-1.md`)
Free replay drill: take a past slate whose results are on disk. Build lineups from only the information available at lock, then grade against actual points. Criteria written before the run: (1) refresh checks done and logged (stats, odds, injuries, starting QBs), (2) no chalk player in 3+ lineups unless justified, (3) late-swap rule applied at the noon rerun, (4) lineup file passes the DK template check, (5) the drill reports its own projected-versus-actual error with numbers from files, (6) no entry made and no money spent, (7) every claim tagged. Pass: 6 of 7, with 1, 2 and 6 CRITICAL. This is a process benchmark, not a promise of winning: variance is large and one slate proves little, so repeat on 3 past slates before Level 3.
Graded by qa-director with tracking-director for the numbers. Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: DFS lineup file and doc, noon rerun note, weekly learning ledger entry
6 to 12 yes or no items each. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (Part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; the failure entries opened (if any) in `memory\agents\failures\fantasy-football-director.md`; the level the evidence supports (a proposal, the grader signs); a ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
