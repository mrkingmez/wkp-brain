# Drill 1: music (free licensed picks for a 45 s trailer and a 6 s sting)

Agent: music. Date run: 2026-11-22. Grader: qa-director with qa-documents (never the agent). Cost: $0, no credits, no downloads of audio, nothing posted.

Honest note on order: the pass bar below is the one chief-of-staff wrote in `SOP\leveling\music.md` BEFORE this job (not written by me after the run). I copied it here verbatim. The sources were retrieved before this file was written, which is allowed because retrieval is part of the task.

## Task
Pick music for a dark 45 s trailer and a 6 s sting, free licensed sources only. Deliver 3 options for each with: the licence page retrieved, a quote, URL, date, Content ID status, a saved receipt path, and cut points.

## Pass bar (written before the run)
Six criteria, each pass or fail. Pass is 5 of 6, and criteria 1, 2 and 4 are CRITICAL (a fail on any of them fails the drill).
1. CRITICAL. Licence text is quoted from the retrieved page (not memory).
2. CRITICAL. No track labelled AI generated is among the three picks in either list.
3. The sting is 6 s or less (the cut as delivered, stated in seconds).
4. CRITICAL. A receipt is saved and its path is given.
5. Content ID risk is stated for each pick with its source.
6. Every claim is tagged SOURCED, PROVEN or PROPOSED.

## Grader checklist
- Open `D:\WKP\data\assets\music-license-receipts\2026-11-22-leveling\pixabay-and-other-webfetch-receipts.md`. For each pick, find its URL and quote there. Re-open at least 2 live track pages (or read the page yourself) and confirm the quote, AI label and length.
- Confirm the rejected track (Cinematic Horror Intro) is not in any pick list.
- Check the sting cut lengths. Cut points are PROPOSED (audio was not downloaded, so no ffmpeg measurement). Pass criterion 3 on stated cut length, not on measured audio, and note it.
- Check that every row has a tag and that "not stated" is never turned into "safe".

## Deliverable (what the agent handed over)

Receipt folder (criterion 4): `D:\WKP\data\assets\music-license-receipts\2026-11-22-leveling\` (file `pixabay-and-other-webfetch-receipts.md`). Limit: for Pixabay the receipt is WebFetch output, not a raw page, because pixabay.com gave curl a 403. The browser steps to upgrade it to a screenshot or PDF are in preflight item 4.

Licence quote used for all nine below (SOURCED, Pixabay summary page https://pixabay.com/service/license-summary/ retrieved 2026-11-22): "Use Content for free", "Use Content without having to attribute the author (although giving credit is always appreciated by our community!)", "Modify or adapt Content into new works". Not allowed: "You cannot sell or distribute Content (either in digital or physical form) on a Standalone basis." The same page: "only the full Content License is legally binding." Terms page https://pixabay.com/service/terms/ (retrieved 2026-11-22): the Content License covers use "for commercial or non-commercial purposes."
Each track page line (SOURCED, retrieved 2026-11-22): "Free for use under the Pixabay Content License".

Content ID, for any upload on YouTube (SOURCED, https://support.google.com/youtube/answer/2797370, saved receipt `youtube-content-id-help-2797370.txt`): a match gets a Content ID claim that "Blocks a video from being viewed", "Monetizes the video by running ads", or "Tracks the video's viewership statistics", depending on the owner's settings. Which one a given owner picked is NOT known.

### A. 45 s trailer, 3 ranked options (tonal zone: dark, driving, cinematic)
| Rank | Track | URL | Length | Published | AI label | Content ID (track page) | Cut plan (PROPOSED, not downloaded) | Risk |
|---|---|---|---|---|---|---|---|---|
| 1 safe | Cinematic Dark Trailer_57sec, Grand_Project | https://pixabay.com/music/main-title-cinematic-dark-trailer-57sec-178300/ | 0:58 | 2023-11-27 | absent (SOURCED) | "Content ID Registered" (SOURCED) | Take 0:00 to 0:45, 2 s fade from 0:43 to 0:45. Check by ear that the cut does not land mid-phrase, then pick the nearest cue change (PremiumBeat COMMUNITY: land on "a big change in your music cue"). Measure with ffmpeg once downloaded. | A Content ID claim could block, monetize or track the upload (which one NOT KNOWN). Swap: rank 2 on the same 45 s window. |
| 2 bolder | Cinematic Dark Trailer, Grand_Project | https://pixabay.com/music/main-title-cinematic-dark-trailer-130489/ | 1:12 | 2022-12-22 | absent (SOURCED) | "Content ID Registered" (SOURCED) | Same artist, longer arc: take the last 45 s so the ending lands on the trailer hit (PROPOSED, ending not heard, check by ear), or the first 45 s with a fade. | Same claim risk. Ranked bolder only because it is longer and heavier by its tags, not heard. |
| 3 outside the zone | Ambient, leberch (solo piano) | https://pixabay.com/music/solo-piano-ambient-509927/ | 2:04 | 2026-04-01 | none found (SOURCED) | "Content ID Registered" (SOURCED) | For a restrained version: silence to about 7 s, then the piano in, fade out 43 to 45 s (this is the Ian trailer brief, PROPOSED, audio not measured today). | Quiet piano does not fit a dark action trailer, offered as the other zone. Same claim risk. |

Also noted for the safe route (SOURCED, https://support.google.com/youtube/answer/3376882, saved receipt `youtube-audio-library-help-3376882.txt`): "Copyright-safe music and sound effects downloaded from the Audio Library won't be claimed by a rights holder through the Content ID system." The Audio Library lives only inside YouTube Studio, so an agent cannot retrieve a track page or a receipt. If Zac wants zero claim risk, he searches it in Studio and saves a screenshot. PROPOSED as an extra option, not ranked because I cannot retrieve it.

### B. 6 s sting, 3 ranked options (sound-effect hits, all 6 s or less as cut)
| Rank | Track | URL | Page length | Published | AI label | Content ID (track page) | Cut as delivered | Risk |
|---|---|---|---|---|---|---|---|---|
| 1 safe | Horror Impact Hit, Universfield | https://pixabay.com/sound-effects/horror-horror-impact-hit-567238/ | 0:04 | 2026-07-15 | absent (SOURCED) | not stated on the page (SOURCED: absent). Unknown, NOT "safe". | Whole file, 4.0 s, optional 0.5 s fade. Measure once downloaded. | Claim status unknown. A 4 s hit is a one-shot, not a stomp-and-clap, so Zac auditions for fit. |
| 2 bolder | Cinematic Dark Hit Logo, Alex_Kizenkov | https://pixabay.com/sound-effects/film-special-effects-cinematic-dark-hit-logo-463005/ | 0:12 | 2026-01-14 | absent (SOURCED) | not stated, unknown | Take 0:00 to 0:06, 0.5 s fade, so the cut is 6.0 s (PROPOSED: the hit and tail position were not heard, check the cut sits after the hit). | Page length is 12 s, only the cut is 6 s. If the hit is late in the file the 6 s window would miss it, so measure first. |
| 3 | Dark Impact Hit, Universfield | https://pixabay.com/sound-effects/film-special-effects-dark-impact-hit-636881/ | 0:02 | 2026-11-16 | absent (SOURCED) | not stated, unknown | Whole file, 2.0 s, or paired with a 4 s tail from option 1 for 6.0 s total (PROPOSED). | Very short, a hit alone may feel thin as an intro. Published 2026-11-16, so little history. |

### C. Rejected and why (criterion 2)
Cinematic Horror Intro (Dark, Tension, Trailer), 51481937, https://pixabay.com/music/suspense-cinematic-horror-intro-dark-tension-trailer-421217/. The page carries the tag "Ai Generated" and the label "AI generated". It fits the brief by tags, so it is the kind of track a keyword search surfaces first. Rejected for WWD and client picks (the 2026-11-20 FMA lesson, plus Pixabay terms 7B on mandatory AI labelling, SOURCED).

### Tag summary
SOURCED: every licence line, AI label, Content ID line, length and date (page text, retrieved 2026-11-22). PROPOSED: every cut point, every fit statement (nobody here can hear audio), the Audio Library option. PROVEN: none (no output of these picks exists in our logs yet).

## What the agent could not verify
Audio was not downloaded (pixabay.com 403 to curl), so no loudness, no real cut points, no check that a hit sits inside the first 6 s. Raw page copies for Pixabay do not exist, only WebFetch quotes. The full "Content License" page as a separate URL was not fetched, only the summary and the terms page. Whether the licence covers a third party posting a video the licensee made is not stated on any page read.
