# QA recheck: Percy Jackson S3 E1 and 2 Upload Package, 2026-11-27

Verdict: PASS WITH NOTES. The earlier blocker (24 lone-backtick paragraphs) is fixed. Nothing edited. Visual page render NOT AVAILABLE (no Word, LibreOffice or soffice), so layout was checked from the docx XML and text only. Drive N: not mounted, "no Drive copy" not verified. Scripts in D:\WKP\scratch\qa-pj2\.

## Prior blocker and notes, status
- B1 backticks: FIXED. docx has 0 backtick characters (219 paragraphs). md has 144 because they are its code fences, expected.
- N1 bullets: FIXED in spirit. The "IN THIS REVIEW" lines are literal "- " text now, but see new note A.
- N2 gate statement: FIXED. Header says script-room not launched, copy via copywriting, social-media, graphic-design under marketing-director. Pinned-Correction-DRAFT line 38 now says script-room wrote it and that script-room had no Agent tool. These two still differ in wording about script-room (one says not launched for the package, one says it wrote the draft). Not a contradiction, they are different files. Fine.
- N3 Mythomagic: FIXED. Draft and package 8.4 now say "in the books", mark what the episodes show as NOT RETRIEVED, and say pin only after a rewatch. The Atlas "General vs Bane of Olympus" line is now flagged LIKELY WRONG, confirm on a rewatch.
- N4: FIXED, slop_check result stated in the draft. I ran slop_check on the package md, exit 0.
- N5: FIXED. 29:18 chapter check now says "the villain-monologue block (about 2 s before 'you kept us safe')", no false quote.
- N6: FIXED. Facebook V2 slot now labeled "judgment slot, not in post-times.md".
- N7 to N11: carried, still true, none block.

## Checks you asked for
1. docx vs md: every non-fence md line (headings, paragraphs, paste blocks, both tables, flags, caption fix list) found in the docx text after normalising. The only "misses" are the 11 numbered Flag items, which Word numbers automatically through the ListNumber style (text itself is present). Flags 1 to 11 render as 1 to 11 in Word. PASS.
2. Backticks 0, em dashes 0, en dashes 0. PASS.
3. Tables intact: 2 tables, 11 rows (cards 1 header + 3, shorts 1 header + 6). PASS.
4. Placeholders: no TODO, TBD, FILL IN, XXX. "[VIDEO LINK]" appears twice, inside the Facebook paste blocks, intended for Zac to paste the live link. Not a defect.
5. Movie folder copy: `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\2026-11-27 - Percy Jackson S3 E1 and 2 Upload Package.docx` is byte-identical (50,917 bytes, md5 2f80fe4f35cbc442956312c3a915ac29, same as the Reports copy). Reports folder holds one file only. PASS.
6. slop_check on the md: exit 0 ("clean, mechanical pass only"). PASS.
7. Chapters: 14 entries including 00:00:00 Start, strictly increasing, last 00:29:18 (1758 s) inside 1882.47 s. Docx chapter list identical to md. First at 00:00:00. PASS.
8. Tags: 454 characters by len(), 23 tags, under 500. Same string is in the docx. PASS.
9. Hashtags: exactly 5 in Section 4, same five in the description, none channel-branded. PASS.
10. Claims without a source: no "verified" assertion without a named source in the text; the package marks the unretrieved items (hashtag volumes, credit cost, Mythomagic on screen, Clarisse in episode 2, Maine, Breaking Bad detail, release time of day) as NOT RETRIEVED, UNVERIFIED or NOT CHECKED. The header now says "I did not re-measure v8 loudness myself": I did, see below, and it matches. NOT VERIFIED list is honest (it also admits nobody has listened to v8 or the music). PASS.

## qa-media on v8 (ran myself, ffprobe and ffmpeg)
File: `...\EP 1 and 2\export\Percy-Jackson-S3-E1-2-Assembly-v8.mp4`, 1,990,772,019 bytes, written 2026-11-27 16:32.
- H.264, 1920x1080, 30 fps, 56,474 frames; AAC 48 kHz stereo; duration 1882.467 s (31:22.47). Matches the package header exactly.
- Loudness (ebur128): integrated -14.0 LUFS, true peak -1.3 dBFS (limit -1.0), LRA 5.9 LU. PASS on the standard.
- Black frames (blackdetect 0.1 s): only 0.13 s at 1864.467 and 0.17 s at 1870.433, i.e. fade-ins on the Next Up and end cards. None over 0.5 s, no black tail. PASS.
- Silence (-50 dB, 1 s): only the final 1.09 s, the end card fade-out. No dead air in the body.
- End card: frame at 1869.9 s is the Next Up card ("NEW REVIEW, COMING TO THE DEN"), frames at 1871.5 s and 1881.5 s are the end card ("THANKS FOR WATCHING", Latest Upload, Subscribe, Best For You boxes, FrostCast Wednesday 9 PM ET line). Transition at 1870.467 s = 31:10.47, matches "about 31:10.5" and package Section 7. Next Up starts 1864.467 (31:04.47), 6.0 s, matches.
- No Disney or streaming mark seen on the three frames viewed (end screen boxes empty by design, Zac places elements in Studio).

## Notes (none block)
A. The docx "IN THIS REVIEW" list (10 lines) and 27 other bullet lines carry a non-breaking space after the hyphen (37 NBSP total; md has 0). Pasting the description into YouTube brings an invisible NBSP, harmless to viewers but not identical to the md. Cleanest fix on next rebuild: plain space.
B. Package header still says v8 loudness was not re-measured by wwd-director; independently measured now (-14.0 LUFS, -1.3 dBTP). Update the line if the docx is rebuilt anyway.
C. Unchanged open items that belong to Zac, not defects: music origin of "Tide of Heroes" (Flag 2), AI box (3), CC BY credit block (4), clip C01 corner mark (5), nobody has listened to v8, Next Up title NOT KNOWN, card 3 (EP 122) and playlist IDs NOT KNOWN, post-times data 25 days old, inventory pull 35 views stale, WWD-2026-11-27-01 attorney question queued.
D. qa-media did not frame-scan the whole file for logos and did not listen to audio, so "no Disney mark" holds only for frames viewed. Chapter times were not re-audited by me (the 13 already checked in the first pass; the last four are arithmetic shifts for the v8 trim, and the v8 length matches).

## Result
PASS WITH NOTES. Ship to Jarvis. Package is ready for Zac subject to his own open flags in Section 9 (those block upload, not this QA).

Lessons file append not done (no edit tool). Lesson for Jarvis to add: after a docx rebuild, count characters above 0x7E, since fixing one defect can swap in another (NBSP after bullets); and measure loudness yourself even when the author reports it.
