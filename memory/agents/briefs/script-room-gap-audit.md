# Gap audit: script-room

2026-11-22, script-room. Outputs audited, all read on disk this run: `logs\script-room.md` (rows 2026-11-10, 11-17, 11-19, 11-20 x2, 11-21), `D:\WKP\Post-Production\projects\ian-trailer\dialogue-01.md`, `originality-01.md`, `clearance-02.md`. NOT read this run: words-draft-01/02, dialogue-02, originality-02, clearance-01, words-final (so findings below rest on the three bench notes and the log, not on the drafts themselves).

Den Files EP 1 "Fire in the Sky" script: NO PRIOR OUTPUT. Glob over D:\WKP for Fire-in/Walton file names found nothing; TASKS.md says it needs two logged passes and none is in `logs\script-room.md` (confirmed: no Fire in the Sky row). It may exist outside the repo (Drive or L:), not checked. The audit of that script is therefore not done.

## Departures from the Craft Brief and cost

| Output | Gap vs brief | Cost |
|---|---|---|
| Ian 3.3, dialogue-01 (Ask-Ian text) | Items read like a checklist, three questions stacked, colon-led labels, item 8 says "your call" twice (repeated thought, S1 Mazin). Caught only by the bench, not by the drafting step. | Rework in pass 2 (roughly 25 min for both passes per log). No credit cost. |
| Ian 3.3, originality-01 | The 15 s cut drifted to the generic veteran skeleton again, same note as 2026-11-10. A repeat of the same failure across drafts. No retrieved source on tagline originality exists; the check was a web search. | Second rework of the same shape. Memory had the note, the draft did not use it. |
| Ian 3.3, clearance-02 | Checks written too narrow (Ford/Mustang only, missed B1 tailgate). Paste risk: instruction inside the paste block. Not a craft-source gap, a checklist gap. | Findings reached Zac as open STOPs, one conditional STOP on C2 until Ian replies. |
| Log row 2026-11-20 pass 2 | slop_check first run exit 1 (two hits) caught only at the final step. | Minor rerun. |
| Log rows 2026-11-11, 11-12, 11-17, 11-21 | Pass 2 not re-read by originality or clearance, slop_check not run (no Bash), benches not spawned. Gate 2 requires two full passes; several rows record one pass or a partial pass. | Gate not fully met, owed items left on the board. |
| All rows | No instruction is tagged PROVEN, SOURCED or PROPOSED. No pass logs name which retrieved source forced a change. | Part 7 of the SOP fails for every past output. |
| Spine | No row shows a one-sentence spine or thesis written before drafting (S4, PROPOSED). | Not measured. |

## Top 3 gaps by cost
1. Gate 2 not met in practice: pass 2 benches skipped or partial (4 log rows) because the run had no Bash or no Agent tool. Cost: owed items cascade to marketing and Zac. Fix: refuse to log "PASS 2 of 2" unless benches re-read the revision; state tool limits at the top (lesson 2026-11-21 already says this).
2. The same generic-shape drift repeats (2026-11-10 then 2026-11-20 on the Ian cutdowns): the lesson sits in a memory file and not in a drafting step. Fix: pre-flight item that names the genre-shelf test before the bench runs.
3. Dialogue written as a checklist or with repeated thoughts (Ask-Ian items). Fix: Mazin repetition test (S1) as a pre-flight item before benches.
