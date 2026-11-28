# SOP: Agent Leveling

Created 2026-11-22 by chief-of-staff on Jarvis's order. Trigger: Zac is angry that the agents are "level one" and said growing agents were supposed to be real. Evidence: graphic-design wrote beginner Firefly prompts that failed (`D:\WKP\data\firefly-prompt-guide\LESSONS.md`, `D:\WKP\data\firefly-prompt-log\README.md`; Zac spent about 2,000 credits on one sting, his figure).

What exists today: a lessons file per agent (`memory\agents\<agent>.md`), read before a job and appended to after. That records what went wrong. It does not make an agent expert. This SOP adds the missing part: study the maker's own guidance, test against it, prove it in a drill before real work, and keep a rating that needs evidence.

This SOP adds to `SOP-Agent-Memory-and-Learning.md`. It does not replace it. Where they differ on leveling, this one wins.

## The seven parts

### 1. Craft Brief (one per agent)
File: `D:\WKP\memory\agents\briefs\<agent>-craft-brief.md`. Written by the agent (or a general-purpose agent running its spec), reviewed by its director.

Contents, in order:
1. What world-class looks like in this craft: 5 to 10 plain sentences, each tied to a source below.
2. 5 to 10 primary sources. Primary means the maker's docs (the tool's own guide, API reference, release notes, official help pages), the standard or specification itself, and named top practitioners (published work, talks, tutorials with a date). Forum posts and listicles are COMMUNITY and count at most 2 of the 10.
3. For each source: URL or file path, retrieved date, and 1 to 3 short VERBATIM quotes (marked with quotation marks) that change how the agent works. A quote not copied from the retrieved page is invalid.
4. "What this changes in our work": a short list, each line naming the source it comes from.
5. Open questions the sources did not answer (so nobody fills the gap from memory).

Rules:
- Retrieve, do not recall. If a page cannot be fetched (blocked, paywall, 429), write `NOT RETRIEVED: <url>, <reason>` and do not summarize it from memory. Fewer than 5 retrieved sources means the brief is INCOMPLETE and the agent cannot rate above Level 1.
- Tag every claim PROVEN (seen working in our own logged outputs at least twice), SOURCED (a quote from a retrieved primary source), COMMUNITY, or PROPOSED (our idea, untested).
- Briefs go stale. Re-retrieve after 90 days, or sooner when the tool ships a new version (note the version in the brief header).
- Shared craft knowledge that already exists (`.claude\agents\_spec\*-reference.md`, `data\firefly-prompt-guide\`) is input, not a substitute. Check it against the retrieved sources and mark each tip PROVEN, SOURCED or PROPOSED.

### 2. Gap audit
File: `D:\WKP\memory\agents\briefs\<agent>-gap-audit.md`. Take the agent's last 5 to 10 real outputs (reports, prompts, run sheets, lineups, scripts, from `D:\WKP Reports\`, the venture folders and `logs\`). For each, list where it departs from the Craft Brief and what that cost (Zac time, credits, a rework, a QA FAIL). Use only outputs that exist on disk and name the path. No outputs on disk: write "no prior output" and skip to the drill. The audit ends with a ranked list of the 3 gaps that cost the most.

### 3. Drill (graded benchmark, before real work)
File: `D:\WKP\SOP\leveling\drills\<agent>-drill-<n>.md` (the task, the pass bar, the grader's checklist) and the result beside it with the date.

- The drill is a realistic task where the answer can be checked without spending money or posting anything. Free tools, local files, dry runs, replays of a past job where the outcome is already known (for example: write the Firefly prompt for a shot whose clips are already on disk, then compare to what the clips showed).
- The pass bar is written BEFORE the run: numbered criteria, each pass or fail, with a threshold (for example 8 of 10, and no fail on a criterion marked CRITICAL).
- The grader is NOT the agent: qa-director (or its named bench) for most agents, the director for QA agents, Jarvis for directors. The grader signs with name and date.
- The drill must be run before the agent touches real work in the areas the drill covers. Until then the agent works only under the director's review, and its output carries the line `UNDRILLED`.
- A failed drill is re-run after the gap is fixed and the Craft Brief updated. Re-run after any real-job failure in that craft too (part 5). Keep every attempt, pass or fail.
- Drills that would need credits or money are not run. The drill is designed around free proxies, and any real spend still needs Zac's yes with the exact cost.

### 4. Pre-flight checklist (per output type)
File: `D:\WKP\SOP\leveling\preflight\<output-type>.md`, one per type the agent ships to Zac (for example: Firefly prompt card, run sheet, lineup file, music pick, script, package). 6 to 12 items, each a yes or no that can be checked by looking at the file, built from the Craft Brief and the failure ledger. Examples of the kind of item: "every instruction is tagged PROVEN, SOURCED or PROPOSED", "no negative described as a thing to avoid inside the positive prompt (it primes it)", "start frame, model tier and settings are written down", "slop_check exit 0".

The agent runs the checklist before hand-back and pastes it into the hand-back with each item ticked and a one-line proof. One unticked item means the output does not go to Zac. The director spot-checks 1 in 3.

### 5. Failure loop (root cause, not a note)
Any failed job (Zac says it failed, QA FAIL, a rework, credits spent for no usable result, a wrong number shipped) opens an entry in `D:\WKP\memory\agents\failures\<agent>.md` within the same turn the failure is known:

```
## YYYY-MM-DD | <job> | cost: <time, credits, reruns, as retrieved or "NOT KNOWN">
- What happened: <facts, file paths>
- What the maker's guidance said: <verbatim quote with URL and retrieved date, or "no source found, searched: ...">
- What we did instead: <the exact prompt, setting or step>
- Root cause: <one sentence: gap in knowledge, skipped checklist item, untested instruction, wrong tool, bad input>
- Fix: <change to Craft Brief, checklist item added, drill added or re-run>
- Re-drill: <drill id, date, result>   (the entry stays OPEN until this line is filled)
```

The one-line lesson in `memory\agents\<agent>.md` still gets written, and it points at this entry. Two entries with the same root cause: the director edits the spec (existing rule), and the agent's level drops one step until a drill passes. Failures are never closed by an agent without a passed re-drill.

### 6. Level rating
File: `D:\WKP\memory\agents\LEVELS.md`. One row per agent spec. Owner of the file: chief-of-staff updates it on evidence handed over by directors and qa-director.

| Level | Name | Evidence required |
|---|---|---|
| 0 | Unrated | nothing yet (every agent starts here) |
| 1 | Novice | spec exists, lessons file exists. Works only under review, outputs carry UNDRILLED |
| 2 | Competent | Craft Brief COMPLETE (5+ retrieved sources), gap audit done, pre-flight checklist in use, AND one drill graded PASS by someone other than the agent (raised 2026-11-22, Zac OK) |
| 3 | Proficient | passed one graded drill, and 3 real jobs since with no failure entry and every instruction tagged |
| 4 | Advanced | Level 3, plus passed a harder drill, plus 10 real jobs with at most one low-cost failure, root-caused and re-drilled |
| 5 | Expert | Level 4, plus a drill an outside benchmark or the maker's own published example can verify, plus 90 days with no repeat failure. Zac's own words (or a QA-director sign-off citing results) required |

Rules:
- No self-rating. The agent may propose, a grader signs. A row needs a date, the evidence path (drill result, QA log, job paths) and who signed.
- A level is a ceiling for autonomy: Level 1 to 2 output is reviewed by the director before it reaches Zac. Level 3 and above may go to qa-director directly. Anything that spends credits or money stays a Zac yes at every level.
- Levels fall: a repeat failure, a stale Craft Brief (over 90 days), or a new tool version with no brief update drops the level one step until fixed.
- Honesty: no level above 1 is written without the evidence path being read and confirmed on disk by whoever writes the row.

### 7. Proven, sourced or proposed (stakes rule)
Every instruction an agent hands to Zac, or to another agent for use against credits or money, carries one tag:

- PROVEN: worked at least twice in our own logged outputs. Cite the log or clip paths.
- SOURCED: from a retrieved primary source. Cite URL, date and the quote.
- PROPOSED: our idea or a community tip, not tested. Say so in plain words and say what the test is.

Where the stakes are credits (Firefly, Veo, ElevenLabs, Higgsfield, Opus) or money (any purchase, any DFS entry fee), an agent never gives Zac an untested set of steps as if it works. PROPOSED instructions must come with the cheapest test that would prove them, and Zac is shown the exact cost before any run. An output with an untagged instruction fails pre-flight.

## Waves
- Wave 1: agents whose failures cost Zac time or credits. Run first, one launch file each in `D:\WKP\SOP\leveling\<agent>.md`.
- Wave 2: the rest, by department, after wave 1 produces its first passed drill (so the drill format is proven on a real case before copying it 55 times).
- The plan and current status per agent live in `memory\agents\LEVELS.md`.

## Budgets and limits
- Retrieval uses free pages only. No paid tools, no sign-ups, no posting, no spend. Credits-based tools are studied from docs, never run for a drill without Zac's yes and the exact cost.
- One agent leveling job at a time per craft, one change at a time (agent working standard): fix one gap, re-run the drill, compare to the saved result.
- Each leveling job writes the usual ledger row in `logs\agent-runs.md` and states the budget first.

## Who does what
| Step | Owner |
|---|---|
| Launch the job | Jarvis, from `SOP\leveling\<agent>.md` |
| Craft Brief, gap audit, checklist | the agent (or a general-purpose agent running its spec) |
| Review of the brief | the agent's director |
| Drill grading | qa-director (or named bench), never the agent |
| LEVELS.md rows | chief-of-staff, on signed evidence |
| Failure entries | the agent, the director checks they are root-caused |
| Level 5 | Zac's words or qa-director sign-off citing results |
