# QA report: 2026-11-19 system reset

Verdict: PASS WITH NOTES. No blockers. Read-only check, nothing edited except this file. Benches not spawned (inline checks, $0).

## Checks asked

1. Contradictions with Zac-locked rules: none found. Details:
   - Raw-recording lock (WWD/CLAUDE.md line 20, item 4, 2026-10-18): SOP-WWD-Review-Workflow step 1 repeats it ("NO raw transcript"), step 2 works from the title only (trailers, stills), step 3 makes Zac's edited-cut transcript the trigger. Compliant.
   - Music intro and outro only (lock 2026-10-17): SOP-WWD "Rules that travel", SOP-Music step 3, music.md lesson. Compliant. Intro 6 s max matches memory\feedback-intro-length.md. Clips 6 to 8 s, 12 max matches feedback-clip-length.md and STANDARDS.md item 12.
   - Money and posting only to Zac: SOP-00 "What goes to Zac", SOP-WWD last rule, SOP-Music "Needs Zac's yes" column. Compliant. Zac is still the WWD editor (SOP-Editing "WWD rule", assistant-editor spec line 26). Compliant.
   - Shorts: WWD/CLAUDE.md line 73 and ruling 7 agree (5 max review, FrostCast cadence per 2026-11-11).
2. Paths in SOP-Output-Locations: all real folders exist except these (see notes N1, N2): `D:\WKP Reports\Saturday Wrap`, `D:\WKP Reports\System Reset` (the SOP lists both as "in use"), `D:\WKP\WKP-CHANNEL\reports`, `D:\WKP\reports\saturday`. The Saturday ones are plausible not-yet-created targets (first wrap not yet run). The rest verified: Asset Placement Run Sheets, WWD Upload Packages, WWD Shorts Copy, Music Prompts, FrostCast, Review Prep, Monday Brief, Ian Book Trailer, the three near-duplicate folders, P:\WWD Kit (Cards, Stickers, Transitions, Color), L: Raw Footage, FrostCast audio folder, Main Channel Theme.mp3, WWD\opusclip, Post-Production\reports, research, logs\qa, reports\monday, data\assets files, build_music_catalog.py, _spec\music-reference.md, all four logs.
3. Music claims trace: music-catalog.md counts 5684 + 105 + 8 + 5 = 5,802 files (matches SOP-Music line 10). Theme path and 117.2 s at catalog line 76 match the SOP-WWD claim. Catalog csv, build script present.
4. Em dashes: grep for U+2014 returned 0 in all six SOP files and music-researcher.md.
5. Rulings table. Winners backed by an explicit Zac instruction or a dated lock: 1 (Zac 2026-10-05), 2, 4, 5 (2026-10-14), 6 and 14 (2026-11-19 feedback files), 8, 10 (2026-10-18), 11 (root 2026-11-12), 7 (newest per case). Rulings 9, 12, 13, 15 are Jarvis-side merges, not Zac quotes, but do not override anything he locked. Ruling 3 is the weak one (N3).

## Other things verified
- Stringout A-Knights-Tale-PREP-Stringout-v1.mp4 (ffprobe): h264, 1920x1080, 30 fps, 2196.9987 s, 65,554,765 bytes, no audio stream. Matches the assembly plan's stated specs (duration, codec, size; plan says 65.55 MB). Not viewed or played by me.
- Plan file exists. `prep\` is the only new folder in the movie folder besides expected items.
- Spec edits: "Memory and learning (added 2026-11-19" section present in music, assistant-editor, head-editor, media-manager, wwd-director. music-researcher.md exists with spec header.
- memory\agents has 63 files. Spot-read music, wwd-director, assistant-editor: correct format, evidence cited, no spec-rule-only lessons. Root CLAUDE.md "SOPs" section present, "Deliverables" line corrected. STANDARDS.md line 12 corrected.

## Notes (none block)
- N1: SOP-Output "type folders in use" lists `System Reset` and `Saturday Wrap`, neither exists on disk. Fix: say "planned" or create on first use.
- N2: `WKP-CHANNEL\reports` and `reports\saturday` do not exist yet; treat as patterns, say so.
- N3: Ruling 3 "revise in place, no second dated copy" sits against root CLAUDE.md 2026-10-05 "every dated version inside" the type folder. The SOP's only source is the wwd-run-sheet spec (2026-10-26), not a Zac quote. Scope it to run sheets, or queue a one-line DECISION so a Zac-locked rule is not quietly narrowed.
- N4: SOP-Memory marks lessons "CONFIRMED" at seeding when they derive from locked rules. Acceptable, but seeded lessons citing a Zac lock are inferred, not new Zac statements.
- N5: Not verified: music-researcher content beyond the header, 60 of 63 lessons files, whether other agents' specs (62 total) all got the memory section, docx output (SOPs are .md internal, correct).
