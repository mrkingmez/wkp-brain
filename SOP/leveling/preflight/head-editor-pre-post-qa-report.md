# Pre-flight: Pre-post QA report (head-editor)

Built 2026-11-22 from `memory\agents\briefs\head-editor-craft-brief.md` and the Godzilla pre-post misses (repeated picture, 10.5 s black tail, -24.7 LUFS). Paste this into the hand-back with each item ticked and a one-line proof. One unticked item and the report does not go to Zac.

1. [ ] The exact file path and its duration from ffprobe are written at the top, and the file is the final export, not a raw or draft.
2. [ ] The loudness command is printed in full (`ffmpeg -i <file> -vn -af ebur128=peak=true -f null -`) with integrated LUFS and true peak read from its Summary block.
3. [ ] The loudness is compared to the house standard (-14 LUFS, -1 dBTP, `WWD\STANDARDS.md`) and labelled a house standard, with the retrieved quote and URL from the brief; no line says Google requires it.
4. [ ] A black-frame check ran (`blackdetect`) and every black stretch over 1 s is listed with start and length; a tail over 3 s is flagged.
5. [ ] A repeated-picture check ran by method (script path named) and every pair is listed with both times, or "none found by this method" with the method's limit (misses repeats under a different crop).
6. [ ] A silence check ran and its threshold is stated (a -45 dB threshold cannot see pauses filled with room tone).
7. [ ] Every statement about picture or sound is marked measured, viewed (frame time named), or "not viewed" / "not heard".
8. [ ] Fix list is ordered, the order rule is stated (pre-post blockers first), and each fix is one action with a timecode.
9. [ ] Every instruction to Zac carries PROVEN, SOURCED or PROPOSED; Adobe menu clicks are PROPOSED unless a retrieved page or Zac's screenshot backs them.
10. [ ] No em dashes, and nothing in the report promises a retention result.
