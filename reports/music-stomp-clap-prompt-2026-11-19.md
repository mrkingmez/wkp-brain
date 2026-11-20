# Music: stomp and clap tournament anthem, ElevenLabs Music prompts

Date: 2026-11-19. Bench: music. For: A Knight's Tale (2001) WWD review, intro and outro (Zac, relayed by Jarvis).
Status: prompts only. Nothing generated, no credits spent. Spend needs Zac's yes (WWD-2026-11-19-02).

## What I could and could not check

- The ElevenLabs connector tools (creative_get_model_guide, get_model_schema) are NOT exposed to this agent. I could not call them. Every setting below comes from ElevenLabs' public docs, fetched 2026-11-19:
  - Compose API reference: https://elevenlabs.io/docs/api-reference/music/compose (official)
  - Music overview: https://elevenlabs.io/docs/overview/capabilities/music (official)
  - Music prompting best practices: https://elevenlabs.io/docs/overview/capabilities/music/best-practices (official)
  - Music terms: https://elevenlabs.io/eleven-music-model-specific-terms (official, "Last updated: 09 October 2026")
- What the web app or the connector shows on screen is not verified. The connector's own setting names may differ from the API names below.
- I cannot hear audio. Nothing here has been tested. Zac auditions.

## WWD fit (from the repo)

- Music is intro and outro only, never a bed under the talk (WWD CLAUDE.md, locked 2026-10-17).
- Past WWD music briefs used about 15 s intro and about 20 s outro (Street Fighter run sheet). Here: intro 12 s, outro 18 s.
- Levels (WWD STANDARDS.md): music about -18 dB under voice, full only on a silent open or close. Export -14 LUFS integrated, true peak -1 dB.
- The A Knight's Tale run sheet: the cut opens on speech at 00:03, so the intro either plays before the first word (add 12 s of picture up front) or sits at -18 dB under it. The outro goes under KingZ's thank-you at about 36:16 at -18 dB, full only after the last word. That is why the outro starts sparse and gets big late.
- Generated music usually comes out hot. For scale, the owned track `P:\Sounds\Music\rock-the-crowd.mp3` measured -7.4 LUFS integrated, +1.1 dBTP true peak, 175.8 s (ffmpeg ebur128, 2026-11-19). Measure every kept ElevenLabs file the same way and pull the gain down.

## Settings (from the API docs, apply the same in the app or connector if it shows them)

| Setting | Intro | Outro | Long build |
|---|---|---|---|
| model_id | music_v2_5 | music_v2_5 | music_v2_5 |
| music_length_ms (length) | 12000 (12 s) | 18000 (18 s) | 60000 (60 s) |
| force_instrumental | true | true | true |
| output_format | WAV if offered, else mp3_48000_192 | same | same |
| store_for_inpainting | true (lets you redo only the ending later) | true | true |

Notes from the docs: length limits read 3 s to 5 min on the overview page and 3,000 to 600,000 ms in the API reference (they conflict, both cover these lengths). `seed` cannot be combined with a text prompt. `force_instrumental` only works with a text prompt. The default model is still the deprecated music_v1, so set music_v2_5 on purpose. With force_instrumental on, the crowd shouts may come out thin or missing; see the shout option below.

## 1. BEST: the matched pair (paste each into its own generation)

Same tempo, same beat, same key, same four-note horn call in both. The intro is tight and ends on a hit. The outro is broad and resolves.

### Intro, 12 s, title "Lances Up Intro"

```
Instrumental only. Medieval tournament crowd anthem intro, 108 BPM, 4/4, G Dorian. Start with just boots stomping on hollow wooden bleachers and big hand claps from a rowdy arena crowd. Beat pattern every bar: stomp on 1, stomp on the and of 2, clap on 3, two quick boot taps on 4. Big outdoor arena reverb, claps close and dry. At 4 seconds bring in deep war drums and taiko-style frame drums doubling the stomps, plus a low hurdy-gurdy drone on G. At 7 seconds two natural horns play a short rising four-note fanfare call. At 12 seconds end on one huge unison hit of drums, horns and a crowd roar, then hard stop to silence. Raw, rowdy, festive. No electric guitar, no singing, no lyrics, no piano, no synths.
```

### Outro, 18 s, title "Lances Up Outro"

```
Instrumental only. Medieval tournament victory anthem outro, 108 BPM, 4/4, G Dorian resolving to a G major final chord. Start sparse with boots stomping on wooden bleachers and hand claps: stomp on 1, stomp on the and of 2, clap on 3, two quick boot taps on 4, big outdoor arena reverb. At 4 seconds add war drums and a soft hurdy-gurdy drone. At 7 seconds warm low brass and natural horns play a broad, slower version of a short rising four-note fanfare call, answered by one bright high trumpet. At 13 seconds the stomping drops out, the horns hold, and the music resolves on a long sustained G major chord with a distant cheering crowd, ringing out to silence by 18 seconds. Triumphant, warm, celebratory. No electric guitar, no singing, no lyrics, no synths.
```

## 2. ALTERNATE A: long build, 60 s, title "Lances Up Build"

For a Shorts hype bumper or a trailer-style build, or to cut a matching intro and outro from one file. Never under the review talk.

```
Instrumental only. Cinematic medieval tournament build, 108 BPM, 4/4, G Dorian, 60 seconds. 0 to 10 seconds: just boots stomping on wooden bleachers and hand claps, stomp on 1, stomp on the and of 2, clap on 3, two quick boot taps on 4, big arena reverb. 10 to 25 seconds: add war drums, taiko-style frame drums and a hurdy-gurdy drone on G. 25 to 40 seconds: natural horns play a short rising four-note fanfare call, low brass answers, snare rolls build. 40 to 52 seconds: full ensemble, the fanfare repeats higher with bright trumpets and a crowd roar. 52 to 56 seconds: everything stops except one held horn note. 56 to 60 seconds: final unison hit of drums and brass, then hard stop. No electric guitar, no singing, no lyrics, no synths.
```

## 3. ALTERNATE B (bolder): anachronism intro, 12 s, title "Lances Up Loud"

The film's joke is modern rock in a medieval arena. This keeps that joke with a guitar that plays the horn call, not a solo. Higher risk of sounding like the original, so run the ear check hard.

```
Instrumental only. Medieval tournament meets gritty modern rock, 108 BPM, 4/4, G Dorian. Start with boots stomping on wooden bleachers and claps: stomp on 1, stomp on the and of 2, clap on 3, two quick boot taps on 4. At 3 seconds war drums and a full rock drum kit enter together. At 6 seconds a distorted electric guitar and natural horns play the same short rising four-note fanfare call in unison, chunky and rhythmic, no guitar solo. End at 12 seconds on one huge hit with a crowd roar, hard stop. No singing, no lyrics, no synths.
```

## Crowd shout option (any prompt above)

Turn force_instrumental OFF and swap the last sentence's "no singing, no lyrics" for: `Wordless crowd shouts only: a gang shout of "HUP" on beat 3 of every bar, no sung melody, no other words.` The model may still add words. If it does, drop that take. If you want a real chant, use an original two-word one: `"LANCES UP"` shouted on beat 3, nothing else. Do not use any word or line from the original song.

## Uses in one line each

- WWD intro or sting: the Intro (12 s) or the Bolder intro.
- Hype bumper for Shorts: the first 6 to 10 s of the Long build, or the Intro.
- Trailer-style build: the Long build (60 s).

## Try plan (2 or 3 tries, untested until Zac has credits)

1. Generate the Outro first (it carries the motif), then the Intro. Keep the take whose horn call is clearest.
2. If intro and outro horn calls do not match, generate the Long build once and cut both from it: the intro from 0 to 10 s plus the 56 to 60 s hit, the outro from the 40 to 56 s stretch with a fade on the held horn. Or use inpainting on a stored track to redo one section.
3. If the beat collapses into a plain two-stomps-and-a-clap, add "never two stomps in a row, the second stomp is late" and lower the crowd, or switch to Alternate A.

## Difference plan (what keeps it from being a copy)

The original is recognized by its groove (two stomps then a clap, in a two-beat cycle), its slow tempo, the bare body-percussion arrangement, the solo chanted vocal over it, and the lead guitar solo at the end.

| Element | Original (what I found) | Ours |
|---|---|---|
| Tempo | About 81 BPM, also listed as 162 double time (SongBPM, AcousticBrainz, Karaoke-Version; not measured by me, I cannot hear) | 108 BPM. Keep anything you try between 104 and 112, away from 76 to 88 and 155 to 170 |
| Beat pattern | Stomp, stomp, clap, rest, repeating every two beats (common description, not measured) | One four-beat cycle: 1 stomp, 2 rest, and-of-2 stomp (late), 3 clap, 4 two quick boot taps. Never two stomps back to back |
| Key and mode | Sources conflict: D major, D minor or E minor | G Dorian, outro resolves to G major |
| Instruments | Stomps, claps, voice, then electric guitar | Boots on wood, war drums, taiko-style frame drums, hurdy-gurdy drone, natural horns, low brass, trumpet. No guitar in the main pair |
| Hook | Chanted vocal line and a guitar solo | A short rising four-note horn call, ours only |
| Vocals | Lead vocal chant with a big group refrain | None, or a wordless "HUP", or our own "LANCES UP" |
| Ending | Abrupt stop after the guitar | Intro: unison hit. Outro: held G major chord with crowd |

## Rights note (plain words, not legal advice)

- A stomp and clap feel, a slow heavy beat, or arena reverb is not protected by itself. What draws trouble is a close copy of the whole package: same groove, same tempo, same sparse arrangement, a chant that tracks the original. That can bring a Content ID match, a manual claim, or a similarity complaint even when no note was copied.
- After generating, Zac compares by ear against the original. Reject a take if any of these show up:
  1. Tap at 81 BPM. If the stomps lock to two-stomps-then-clap every two beats, reject.
  2. A single voice chanting or singing over bare stomps and claps.
  3. A short chant that lands its last word on the clap.
  4. A screaming lead guitar over continued stomping, then a sudden stop.
  5. Any melody you can hum along to from the original.
  6. A friend who has not been told names the song within 5 seconds.
- ElevenLabs terms (fetched 2026-11-19, page dated 09 October 2026, official):
  - Prompts may not name any artist (living or dead), song title, album, publisher or label, or use a distinctive portion of any song's lyrics (Section 2.1). Our prompts name none.
  - Free plan: individual use, no downloads, attribution required ("denote Eleven Music when distributing"). Starter and up: no attribution required.
  - Media rights on Free through Business: "All online and offline commercial use permitted, except film, TV, radio, and Studio Games." Includes syncing to video (Section 4.8(d)). The terms do not name YouTube; I did not verify whether ElevenLabs treats a YouTube review as "online" use, it reads that way but is not stated.
  - No indemnity and no copyright guarantee. Section 3.1: you are responsible for reviewing Output for clearance before you publish.
  - A web search summary showed an older November 2025 version with stricter tier rules. I did not open that page. The October 2026 page is the one I read.
- Zac's ElevenLabs plan tier is not known to me. A Free-plan take cannot be downloaded at all. Confirm the plan before any generation (WWD-2026-11-19-02).

## Filing, if Zac keeps a take

- Master: `P:\Sounds\Music\ElevenLabs\2026-11-DD - Lances Up Intro - ElevenLabs music_v2_5.wav` (same pattern for Outro, Build, Loud). New subfolder, so it never overwrites a track already used.
- Copy for the edit: `P:\WWD Kit\A Knights Tale\Sounds\` (folder does not exist yet).
- Proof file next to each master, same name plus `.license.txt`: date made, plan tier on that date, model, the exact prompt, settings, generation link.
- Index line for `D:\WKP\data\assets\p-drive-index.csv` (fill in real bytes after download):
  `"P:\Sounds\Music\ElevenLabs\2026-11-DD - Lances Up Intro - ElevenLabs music_v2_5.wav",".wav","<bytes>"`
- Owned fallback if no credits: `P:\Sounds\Music\rock-the-crowd.mp3` (name only, not heard, no license file on disk, -7.4 LUFS, +1.1 dBTP, so at least -10 dB of gain cut is needed).
