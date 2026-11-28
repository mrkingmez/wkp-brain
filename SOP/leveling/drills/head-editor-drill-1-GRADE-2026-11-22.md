# GRADE: head-editor drill 1, independent re-run

Grader: qa-director, 2026-11-22. Not the agent. Standard: `SOP\SOP-Agent-Leveling.md` part 3. Pass bar: `head-editor-drill-1.md` (6 criteria, pass 5 of 6, criteria 1 and 2 CRITICAL). Agent result graded: `head-editor-drill-1-result-2026-11-22.md`.

## What I re-ran (own commands, own scratch folder `D:\WKP\scratch\qa-level\`, 2026-11-22)
- ffprobe on all 3 files: H.264 1920x1080 30 fps plus AAC, durations 1733.600, 1435.533, 1666.900 s.
- Loudness: `ffmpeg -hide_banner -nostats -i <file> -vn -af ebur128=peak=true -f null -`
- Black: `ffmpeg -i <file> -vf blackdetect=d=0.4:pix_th=0.10 -an -f null -` (0.4 s threshold, the agent used 0.5)
- Repeats: my OWN script `rep2.py` (not the agent's `rep.py`): 1 fps, 48x27 grey frames, cutaway = correlation to median under 0.6, flagged pairs 10 s or more apart with correlation over 0.985.
- Frames pulled with ffmpeg and viewed by me: Godzilla at 1536 s and 1575 s, 13.1 s, 1730 s; Vision Quest EP 8 at 1286 s and 1296 s (sheet `D:\WKP\scratch\qa-level\sheet.png`).

## Results
| File | Integrated | LRA | True peak | Black found |
|---|---|---|---|---|
| Godzilla | -24.7 LUFS | 7.8 | -2.4 | 12.93 to 13.43 s (0.5 s); 1723.07 to 1733.57 s (10.5 s) |
| VQ EP 7 | -22.8 LUFS | 7.2 | -1.7 | 17.80 to 18.37 s; 1433.87 to 1435.5 s (1.63 s) |
| VQ EP 8 | -21.2 LUFS | 7.8 | +0.1 | 14.57 to 15.13 s; 1664.47 to 1666.87 s (2.4 s) |
Every number equals the agent's table. Godzilla repeated picture found by my method at 1534 to 1539 s and again at 1573 to 1577 s (correlation 0.9996, 30 matching frames). I viewed 1536 s and 1575 s: the same picture (a flying boat over a ruined city with a clock tower), so confirmed by eye. I viewed 13.1 s and 1730 s: both black frames. The Godzilla 0.5 s black at 12.93 s is real black, whether intended is still unknown.

## Per criterion
| # | Criterion | Mark | Evidence |
|---|---|---|---|
| 1 | CRITICAL, both Godzilla defects by measurement, within 2 s | PASS | Repeat 1534 to 1539 and 1573 to 1577 (agent 1534.0 to 1539.5 and 1572.5 to 1577.5), black tail 1723.07 to end (identical) |
| 2 | CRITICAL, loudness for 3 videos, command printed | PASS | Command printed in the result, all 3 numbers reproduce to the decimal |
| 3 | Standard quoted with URL, date and limits | NOT RE-VERIFIED | I have no web fetch tool here. I did not re-retrieve the EBU, ITU or YouTube-figure pages, so the verbatim quotes are unchecked. The "what the quote does not prove" paragraph is sound on its face |
| 4 | No unmeasured claims | PASS | Result says frames not viewed and audio not heard, and nothing contradicted what I saw |
| 5 | Fix list ordered by Zac time | PASS | Order stated, one action per fix |
| 6 | Instructions tagged | PASS | Every fix carries PROPOSED or SOURCED |

Total: 5 of 5 criteria I could re-check pass, criteria 1 and 2 pass, criterion 3 not re-verified (6 of 6 only if the quotes are good). The bar needs 5 of 6: met without criterion 3.

## Verdict: PASS (qa-director, 2026-11-22), with these limits
- Replication, not discovery: the agent had the Style Sheet, and so did the numbers. My repeat check used a different method and agrees, which is the independent part.
- Method weakness seen: my repeat script flagged near-static host-cam frames in Vision Quest EP 8 (1277 to 1297 s, correlation 0.986 to 0.994). I viewed 1286 s and 1296 s: both host cam, a false positive, not a repeated picture. The agent's own script reported none for EP 7 and EP 8, which is consistent. Neither method was checked for missed repeats of a differently framed picture.
- I did not listen to any audio and did not view the whole of any video.
- Not in the drill and not checked: pre-flight checklist use (no ticked checklist in the result file).
