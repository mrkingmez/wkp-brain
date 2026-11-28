# Craft Brief: head-editor

Written 2026-11-22 by head-editor (leveling job, SOP-Agent-Leveling.md). Reviewer: studio-director (not yet reviewed). Tool versions: Premiere Pro 2026 and 2027 both installed on Zac's machine, Adobe help for either NOT RETRIEVED (see below). Re-retrieve by 2027-02-20 or on a new Premiere or FFmpeg release.

Method note: pages were read with WebFetch, which returns quotes extracted by a small model, not the raw page. Every quote below is as returned and marked "as returned". Where the fetch returned a binary PDF or an empty shell the source is NOT RETRIEVED. Caption files from earlier phase-A study are local files pulled 2026-11-19 and 2026-11-20 (yt-dlp captions, auto captions unless noted), quoted from the file.

## 1. What world-class looks like (5 to 10 sentences, each tied to a source)
1. A cut is chosen by emotion first, story second, rhythm third (S4, COMMUNITY secondary on Murch).
2. A cut lands where the thought ends, because that is where the viewer's own blink falls (S4).
3. YouTube's own retention report is read for dips (abandon or skip) and spikes (rewatch), and the first 30 s is its own measured number (S1, SOURCED).
4. The first 30 s gets the most work, and pace stays steady after it (S7, practitioner).
5. Cutaway inserts run 2 to 5 s, too short feels chaotic, too long boring (S8, practitioner).
6. Loudness is measured against a stated standard, never guessed: EBU R128 is -23 LUFS +/- 0.5 LU (S2, SOURCED), BS.1770 defines the measurement (S3, SOURCED). YouTube publishes no number (S5, S6).
7. For YouTube the working number is -14 LUFS, a third-party measured figure (S5, COMMUNITY practitioner), so state it as a house standard, not Google's rule.

## 2. Sources (8 retrieved, 2 community counted, 4 NOT RETRIEVED)

### S1. YouTube Help, "Audience retention" (key moments) PRIMARY
URL: https://support.google.com/youtube/answer/9314415 | retrieved 2026-11-22
- "Dips mean that viewers are abandoning or skipping at that specific part of your video." (as returned)
- "Intro tells you what percentage of your audience still watched your video after the first 30 seconds." (as returned)
- "Spikes appear when more viewers are watching, rewatching, or sharing those parts of your video." (as returned)
- "When the line on the chart is flat, it means viewers are watching that part of your video from start to finish." (as returned)

### S2. EBU R128 publication page PRIMARY
URL: https://tech.ebu.ch/publications/r128 | retrieved 2026-11-22
- "Recommendation to use an average programme loudness of -23 LUFS and the 'Loudness Range' and 'Maximum True Peak Level' descriptors." (as returned)
- "Target level (-23 LUFS) tolerances restricted to +/- 0.5 LU." (Version 3.0 entry, June 2014, as returned)
- The page gave no true peak number. The R128 PDF at https://tech.ebu.ch/docs/r/r128.pdf was fetched but came back as a compressed binary stream: PDF text NOT RETRIEVED, so -1 dBTP is NOT sourced here.

### S3. ITU-R BS.1770 recommendation page PRIMARY
URL: https://www.itu.int/rec/R-REC-BS.1770 | retrieved 2026-11-22
- Title: "Algorithms to measure audio programme loudness and true-peak audio level" (as returned). Version listed BS.1770-5, approved 11/2023, status in force.
- Only the title, version and status were returned, no measurement detail. It shows the standard exists and what it covers.

### S4. Walter Murch on blinks and the first criterion, via PremiumBeat COMMUNITY (secondary quoting Murch)
URL: https://www.premiumbeat.com/blog/when-and-where-to-make-the-cut-inspired-by-walter-murchs-in-the-blink-of-an-eye/ | retrieved 2026-11-22
- "Is it true to the emotion of the moment?" (Murch's first criterion, weighted 51 percent by this article, as returned)
- "every time he or she has a new whole thought or emotion" (the moment a person blinks, as returned)
- "Your job is partly to anticipate, partly to control the thought processes of the audience" (as returned)
- A web search the same day found the ordering emotion 51, story 23, rhythm 10, eye-trace 7, plane 5, space 4 repeated across StudioBinder, No Film School and a Texas wiki, none quoting the book. The book itself is NOT RETRIEVED, so the percentages are COMMUNITY.

### S5. Ian Shepherd, Production Advice, "YouTube loudness" PRACTITIONER (named mastering engineer), counts as community
URL: https://productionadvice.co.uk/youtube-loudness/ | post dated 2015-03-17, updated, page footer 2026, retrieved 2026-11-22
- "Louder songs are turned down" (as returned)
- An update says YouTube's earlier reference "was closer to -13, and didn't use LUFS," but "they changed this in 2019 and have been using exactly -14 LUFS since then." (as returned)
- The page does not say quieter videos are turned up. Whether a -22 LUFS video gets boosted is NOT answered.

### S6. Frame.io Workflow Guide, "Loudness for YouTube" (Adobe-owned, footer 2021) PRACTITIONER
URL: https://workflow.frame.io/guide/loudness-for-youtube | no date shown, retrieved 2026-11-22
- "YouTube doesn’t release exact values, but YouTube tends to shoot for -12 to -14 LUFS." (as returned)
- "aiming for a specific integrated loudness doesn’t work, reliably." (as returned)
- It does not mention true peak and does not say quiet videos are boosted.

### S7. Nate Curtiss, "7 YouTube Editing Tips to Instantly Boost Retention", 2024-03-01 PRACTITIONER
Source: caption file `D:\WKP\scratch\editor-study\yt\txt\ODRJkEGTI_U.txt`, https://www.youtube.com/watch?v=ODRJkEGTI_U , pulled 2026-11-19 (auto captions)
- "it's called frontloading your video which means that you'll first want to pay special attention and put more work into the first 30 seconds or so of your video we keep the pace of our videos pretty similar throughout the entire thing"
(sponsored by CapCut, software version not named)

### S8. Katie Steckly, "The Ultimate Guide to Editing B-Roll For YouTube", 2025-02-12 PRACTITIONER
Source: caption file `D:\WKP\scratch\editor-study\yt\txt\pW4WBaIGqqg.txt`, https://www.youtube.com/watch?v=pW4WBaIGqqg , pulled 2026-11-19 (auto captions)
- "generally you should aim for your B-roll clips to be somewhere between like two and five seconds long. If they're too short, it feels chaotic, but if they're too long, it starts to feel a bit boring."

### NOT RETRIEVED
- NOT RETRIEVED: https://helpx.adobe.com/in/media-encoder/desktop/encoding-and-exporting/automatic-loudness-correction.html, HTTP 403. A search snippet (not a retrieval) says the page lists ATSC A/85, EBU R128 and ITU BS.1770-3 with only BS.1770-3 allowing a custom target. Treat as PROPOSED until a retrieval works.
- NOT RETRIEVED: https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/edit-loudness-meter-settings.html, HTTP 403.
- NOT RETRIEVED: https://helpx.adobe.com/premiere-pro/using/loudness-normalization.html, HTTP 403.
- NOT RETRIEVED: Netflix Sound Mix Specifications, the old URL redirects to https://studiopartner.netflix.net/studio/branded-sound-mix-spec-and-best-practices which returned only "Knowledge Hub". A search summary gave -27 LKFS dialogue gated, +/- 2 LU and -2 dBTP, but that is a search summary and not the page, so it is not used.
- NOT RETRIEVED: https://www.studiobinder.com/blog/what-is-a-jump-cut-definition/, HTTP 404 (guessed URL).
- Murch's book text, BBC delivery spec, FFmpeg ebur128 docs: not attempted this run.

## 3. What this changes in our work
- Every export check prints the ffmpeg ebur128 command and the integrated LUFS and true peak, then compares to the house standard of -14 LUFS and -1 dBTP in `WWD\STANDARDS.md`, tagging it a house standard, not a Google rule (S5, S6, S2).
- Never write "YouTube will boost it" or "YouTube will turn it down" as fact for a quiet export: S5 says loud is turned down, nothing retrieved says quiet is turned up (S5, S6).
- Notes on cutaways are checked against 2 to 5 s and Zac's own 7 s rule, reported as two separate lines (S8).
- Notes about the opening treat the first 30 s as the measured Intro number in YouTube Studio, and say the Intro value was not pulled when it was not (S1, S7).
- Fix notes cite what a dip or spike would mean only after Zac reads Studio retention, never predict a dip (S1).
- A cut note names the emotion or thought it serves before the rhythm reason (S4, COMMUNITY).
- Any Adobe menu step carries PROPOSED until a retrieved Adobe page or Zac's screenshot confirms it (Adobe pages NOT RETRIEVED).

## 4. Open questions the sources did not answer
- Does YouTube raise a -22 LUFS upload to -14 on playback? S5 and S6 do not say. Test: upload unlisted at two levels and read Stats for Nerds "content loudness". Needs Zac, no cost, not run.
- The EBU true peak limit number (R128 PDF unreadable).
- Premiere 2026 or 2027 Loudness Normalization menu wording and whether it reaches -14 without pumping.
- What the real Intro retention is on WWD reviews (no VidIQ or Studio pull).
- Whether the 60-second rule in the Style Sheet raises retention (PROPOSED, untested).
