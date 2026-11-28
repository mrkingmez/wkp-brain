# Failure entries: fantasy-football-director (DFS only)

Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` part 5. An entry stays OPEN until the Re-drill line is filled by a passed drill.

## 2026-11-22 | DFS Week 11 noon rerun, concentration after a QB change | cost: Zac's errand time before the 1:00 PM lock (his words), dollar cost NOT KNOWN
- What happened: noon build (`D:\Draft Kings\Week 11\sun\`, noon-v1) had McBride (ARI TE) in 4 of 7 lineups after Beck went OUT and Josh Johnson started (ARI implied 12.5). The note `Fantasy-Football\reports\Week11-DK-Noon-Rerun-2026-11-22-sun.md` told Zac to cut it by hand. The file was patched through noon-v2, patched-v3 and the final upload at 12:32 PM; the entered file has max count 3. Source: `memory\feedback-dfs-concentration-check.md`.
- What the maker's guidance said: no maker page covers this. Closest sourced principle: "The negative correlation is something we want to avoid within a lineup as it would reduce the overall variance." (Hunter, Vielma, Zaman, https://ar5iv.arxiv.org/html/1604.01455, retrieved 2026-11-22); a cap on one-player exposure is our own rule, not a source. Searched: DraftKings official rules (HTTP 403), NFL operations (404).
- What we did instead: shipped the build with the exposure named as a risk and left the fix to Zac.
- Root cause: skipped step. The concentration check lived in a lesson, not in a checklist, and the validator (`dk_validate.py`) does not count chalk or react to a QB change.
- Fix: pre-flight lineup and noon checklists written 2026-11-22 (`SOP\leveling\preflight\`); concentration table and QB-change list are mandatory items.
- Re-drill: drill-1 self-run 2026-11-22 FAILED criteria 1 and 2 (UNGRADED); re-run after the Week 12 slate. OPEN.
