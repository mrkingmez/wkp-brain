# Craft Brief: assistant-editor

Written 2026-11-22 by assistant-editor (leveling job, `SOP\SOP-Agent-Leveling.md`). Review owner: studio-director. Tool versions at retrieval: local ffmpeg 9.0 (gyan.dev full build, `ffmpeg -version` 2026-11-22), ffmpeg docs page as served 2026-11-22, EBU R 128-2023, ITU-R BS.1770-5 (11/2023). Stale after 2027-02-20 or on a new ffmpeg or Premiere major version.

Status: COMPLETE by the SOP count (5 retrieved sources, 4 primary and 1 community) but THIN on Premiere and editing craft. Adobe help, the YouTube loudness page, Netflix and BBC delivery specs and Murch's own text could not be retrieved (list at the bottom). Nothing below about those comes from memory.

## 1. What good looks like in this craft (each line tied to a source)
1. A run sheet or stringout is measured against a loudness standard with a gated, true-peak aware meter, not by ear. (S2, S3)
2. Loudness is a programme-level number plus a true-peak ceiling, so both go on every check list. (S2)
3. Our -14 LUFS lock is a house lock for YouTube. The only loudness target in the retrieved primary sources is -23.0 LUFS (broadcast). So -14 stays a Zac lock, tagged PROPOSED against any outside standard until the YouTube page is retrieved. (S2, S4)
4. Scale with contain and fit, never crop, is a real ffmpeg option, not a trick. (S1)
5. Concatenated segments must match in streams and formats, so every stringout segment is built the same way before joining. (S1)
6. Black tails and dead air are found with a detector, not by scrubbing. (S1)
7. The export spec Zac uploads to is the maker's published one: H.264, progressive, 48 kHz, source frame rate kept. (S4)
8. A cut is chosen on more than one criterion at once (Murch's "rule of six"), so a pacing note from us names the criterion it serves. (S5, COMMUNITY)

## 2. Sources (retrieved 2026-11-22, free pages only)

### S1 ffmpeg Filters Documentation (maker docs). SOURCED
URL: https://ffmpeg.org/ffmpeg-filters.html (HTTP 200, 1.75 MB, read as text)
Quotes (verbatim):
- loudnorm: "EBU R128 loudness normalization. Includes both dynamic and linear normalization modes."
- loudnorm: "In dynamic mode, to accurately detect true peaks, the audio stream will be upsampled to 192 kHz."
- loudnorm: "Use the -ar option or aresample filter to explicitly set an output sample rate."
- loudnorm integrated target: "Range is -70.0 - -5.0. Default value is -24.0." and true peak "Range is -9.0 - +0.0. Default value is -2.0."
- loudnorm linear: "measured_thresh must all be specified."
- scale: "Enable decreasing or increasing output video width or height if necessary to keep the original aspect ratio."
- concat: "segments must have the same number of streams of each type"
- blackdetect: "Detect video intervals that are (almost) completely black."
- tpad: "Temporarily pad video frames."

### S2 EBU R 128-2023 (the standard). SOURCED
URL: https://tech.ebu.ch/docs/r/r128.pdf (HTTP 200, 5 pages, read with pdftotext)
Quotes (verbatim):
- "that the Programme Loudness Level shall be normalised to a Target Level of -23.0 LUFS."
- "that the True Peak Level of a programme shall not exceed -1 dBTP (dB True Peak)"
- "that in special cases the Programme Loudness Level may be normalised to a Target Level lower than -23.0 LUFS on purpose."

### S3 ITU-R BS.1770-5 (the measurement algorithm). SOURCED
URL: https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf (HTTP 200, 2 MB, pdftotext)
Quotes (verbatim):
- "gating of 400 ms blocks (overlapping by 75%), where two thresholds are used:"
- "the first at -70 LKFS;"
- "the second at -10 dB relative to the level measured after application of the first threshold."

### S4 YouTube Help, recommended upload encoding settings (maker docs). SOURCED
URL: https://support.google.com/youtube/answer/1722171?hl=en (HTTP 200, read by me with curl after a web-fetch agent read it first)
Quotes (verbatim, each confirmed present in the page text):
- "Audio codec: AAC-LC or Opus or Eclipsa Audio"
- "Sample rate: 48kHz"
- "Progressive scan (no interlacing)"
- "same frame rate it was recorded"
The page does not mention loudness or LUFS (checked by search of the text).

### S5 Wikipedia, Walter Murch. COMMUNITY (secondary, counts toward the 2 community cap)
URL: https://en.wikipedia.org/wiki/Walter_Murch (HTTP 200)
Quote (verbatim): "One of his most praised techniques he refers to as "the rule of six" referring to the six criteria in a film that he examines when making a cut."
Limit: the six criteria themselves are NOT in the page text I read. Do not list them from memory.

## 3. What this changes in our work
- Every loudness line on a run sheet gives measured integrated LUFS and true peak, and says which target it is judged against. Source: S2, S3. Tag: SOURCED for the method.
- Keep the -14 LUFS and -1 dBTP lock for YouTube exports, but label it "Zac's lock, YouTube page not retrieved". The -1 dBTP part matches S2. The -14 LUFS part has no retrieved source. Source: S2, S4. Tag: PROPOSED until retrieved.
- Measure with `ffmpeg -i <file> -vn -af ebur128=peak=true -f null -` (the meter ebur128 is not quoted from the docs page I retrieved, the quoted loudnorm doc is the nearest evidence, so the ebur128 command is PROVEN only by our own use: drill 1 result, 2026-11-22) . Source: S1 plus our logs.
- Black tail check uses blackdetect on the last 20 s. Source: S1. Tag: SOURCED, PROVEN by drill 1.
- Stringout and plan segments are built to one format before concat (same size, fps, pixel format, no audio). Source: S1 (concat). Tag: SOURCED, PROVEN by the A Knight's Tale stringout QA (frame count 65,910 matched).
- Export-spec line on every package: H.264 progressive, AAC-LC, 48 kHz, source frame rate kept. Source: S4.
- Pacing notes name the criterion served and stay tagged PROPOSED. Source: S5.

## 4. Open questions the sources did not answer
- Does YouTube's help text state -14 LUFS? Page not retrieved (404 at two URLs tried).
- Exact Premiere 2026 and 2027 menu paths for markers, nested sequences, Essential Sound loudness (Adobe returned 403 to curl and to the web-fetch agent).
- Netflix and BBC audio delivery numbers (not retrieved).
- Murch's six criteria and their weights (primary text not retrieved).
- ffmpeg `ebur128` filter text and `xfade` and `tpad stop_mode` details: found in our own logs (PROVEN) but I did not quote the docs for them.

## 5. NOT RETRIEVED
- https://helpx.adobe.com/premiere-pro/using/markers.html, nested-sequences.html, audio-loudness.html, export-settings-reference-premiere-pro.html: HTTP 403 Access Denied.
- https://support.google.com/youtube/answer/9314492, answer/7050148, answer/6039468: served the "page can't be found" page (404).
- https://partnerhelp.netflixstudios.com/hc/en-us/articles/360001794307 and 215758617: JavaScript shell or a different article (Timed Text Style Guide), no sound mix text.
- https://partners.bbc.co.uk/delivery/technical-specs: connection failed (HTTP 000).
- https://www.aes.org/technical/documentDownloads.cfm?docID=731: HTTP 403.
- Murch's In the Blink of an Eye: Wikipedia "In the Blink of an Eye" is a disambiguation page, no text.
Next retrieval attempt: ask Zac for a Premiere help PDF export or use a browser-capable agent, then add S6 and S7.

## 6. Local input (not proof)
`SOP\SOP-Editing-Department.md`, `memory\agents\assistant-editor.md` lessons (ffmpeg tpad, xfade, frame counts: PROVEN by two or more logged jobs), `Post-Production\reports\Zac-Style-Sheet-2026-11-19.md` (not re-read this job).
