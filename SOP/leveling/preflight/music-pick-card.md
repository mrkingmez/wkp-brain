# Pre-flight: music pick card with license receipt

Owner: music. Created 2026-11-22 from `memory\agents\briefs\music-craft-brief.md` and the gap audit. Run before hand-back, paste into the hand-back with each item ticked and a one-line proof. One unticked item and the card does not go to Zac. Director spot-checks 1 in 3.

1. [ ] Three ranked picks (safe, bolder, outside), all in one tonal zone, each with a one-line reason and a risk. Proof: the card table. (Berklee, Hunter George)
2. [ ] Each pick's licence line is quoted from the INDIVIDUAL track page, with URL and retrieved date. Not the album, not the search page, not memory. Proof: quote and date in the card.
3. [ ] The terms or full licence page is cited, not only a summary page ("only the full Content License is legally binding"). Proof: URL of the terms page and a quote.
4. [ ] A receipt path is on disk (page text, screenshot or PDF) and the file exists. If only tool-quoted text exists, say so, and list the exact browser steps for Zac to save a screenshot. Proof: `Test-Path` or ls output.
5. [ ] AI label read on each track page and stated (present, absent). Any "AI generated" tag means REJECT for WWD and client work. Proof: the line from the page.
6. [ ] Content ID stated per pick with its source, and the three outcomes named (blocks, monetizes, tracks). "Not stated on the page" is written as "unknown", never "safe". Proof: page line plus the YouTube Content ID help URL.
7. [ ] Credit line: "none required" only where the page says so. CC BY tracks carry the exact credit text. Proof: the quote.
8. [ ] Cut points: length as delivered is in seconds. Measured with ffmpeg if the file exists, otherwise marked PROPOSED, not measured. Sting 6 s or less. Loudness measured (ebur128) or marked NOT MEASURED. Proof: the command output or the label.
9. [ ] A swap track is named on the same cue times (takedown or claim). Proof: the swap row.
10. [ ] Owned tracks are labelled "owned, license unproven" unless a receipt is on disk. Adobe loops are not called license-clear on the strength of the SFX page. Proof: catalog `source_guess` column quoted.
11. [ ] Every instruction handed to Zac is tagged SOURCED, PROVEN or PROPOSED, and any PROPOSED step has its cheapest test. Proof: the tags in the card.
12. [ ] Music is intro or outro only, never a bed under the talk (WWD rule, locked 2026-10-17), and the pick is copied to `P:\WWD Kit\<show>\Sounds\` for a WWD job. Proof: path.
