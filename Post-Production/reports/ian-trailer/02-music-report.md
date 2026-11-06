# The Wrench Turner trailer: Music Report (02)

Date: 2026-11-04. Author: music agent. For: marketing-director, then studio-director and Zac.
Job: 56 s vertical book trailer, paid client job (Ian Griffin), client posts it on YouTube Shorts, Instagram, TikTok and Facebook.
Brief: quiet, garage ambience carries the first half, one sustained instrument or very sparse bed, a swell only at the present-day beat, cut to silence on the tap. No solo acoustic guitar, no rotor sounds, no big hits.

Honesty notes up front
- I cannot hear audio. "Fit" below comes from file names, ID3 tags, and ffmpeg measurements (length, loudness, 5 s energy windows). Every fit claim is "from the file name and measurements, not heard." Zac auditions.
- No owned track has a license record on disk. For client work posted on four platforms, every owned track is UNKNOWN or UNVERIFIED until Zac produces proof of where it came from.
- Nothing was bought, signed up for, posted, sent or pushed.

---

## 1. Owned library audit (P:\Sounds\Music)

Scope: 5,872 files under the folder (about 220 loose mp3 at the top level, the rest is the Adobe pack in `adobe\`). Index: `D:\WKP\data\assets\p-drive-index.csv` (path, ext, bytes only, no license column). I measured about 35 name-based candidates, not all 5,872 files. Loose mp3s at the top level carry no license papers. Earlier project note (`.claude\agents\_spec\wwd-vfx-toolkit.md` line 124) already warns that provenance is not verified and several look commercial.

### Provenance by file-name pattern (what is known, what is not)
| Pattern | What it suggests | License status for client work |
|---|---|---|
| `audioblocks-*`, and `name_AbCdEfGh.mp3` with a random 8 char suffix (many files, some tagged with artist names like neilcross, juanmares, psmithp) | Looks like Storyblocks/Audioblocks downloads, 2016 to 2017 file dates. A guess from the pattern, not proven. | UNKNOWN. Storyblocks' own license page (below) says perpetual use is "No" for Individual and Small Business plans and "Yes" for Business, while also saying work "published during your time as a member" is covered forever. The page does not resolve it. A trailer published in 2026 by a client is almost surely outside any 2016/2017 membership. Treat as NOT cleared. |
| `bcc-*`, `jdi-*`, `ssm-*`, `luk-*`, `bbc-*` | Library-style prefixes, source unknown. `jdi-0414-eb-min-sad-cinematic-piano` has ID3 tag "MUSIC DESIGN BY JASON INC" in artist/title/copyright. | UNKNOWN. A copyright tag is not a license. |
| `bensound-*` | Bensound free downloads. | UNKNOWN. Bensound's free tier is commonly attribution-required, I did not retrieve its terms. Not recommended for a client job. |
| `Wedding Day Love Songs...`, `Le chant des templiers...FULL HD`, `Beethoven`, `Mozart`, etc. | Looks like YouTube rips or third-party recordings. | NOT cleared. Do not use. |
| `adobe\...` (Ambient, Classical&Orchestral, etc.) | Adobe Audition/Premiere bundled loops. | Adobe says bundled sounds and loops are royalty-free; use is under the EULA and the readme in each library download; main stated limit is no standalone redistribution. I could not find a current Adobe statement that names client work. LIKELY OK, not confirmed (see section 2). |
| `Raw Rehearsal Room.mp3`, `Track.mp3` (Sep 10 2026 file dates), `Spellbound`, `Inspired`, `Carpe Diem`, `Frolic`, `Whispering Stream`, `Nineties Pad` | Mixed. Two are recent Zac files, others unknown. | UNKNOWN. Not measured as candidates. |

### Measured candidates (ffprobe length, ebur128 integrated loudness, 5 s RMS windows)
All unheard. "Shape" is the RMS envelope in dBFS over time.

| # | File (full path) | Length | LUFS | Shape (measured) | Fit, from name and measurement | License for client work |
|---|---|---|---|---|---|---|
| 1 | `P:\Sounds\Music\jdi-0414-eb-min-sad-cinematic-piano.mp3` | 1:22.3 | -16.1 | Starts quiet (-23), first lift at 15 s (-15), second lift near 35 to 45 s, decays to -55 by 80 s | Best SHAPE match: quiet start, a swell, then a natural decay to silence. Name says sad cinematic piano (piano is allowed, guitar is not). Risk: unknown if it has strings or drums. | UNKNOWN (tag "Music Design by Jason Inc") |
| 2 | `P:\Sounds\Music\bereaved_zkMX98Su.mp3` | 3:47.4 | -20.2 | Quiet and even, -30 to -18, small peaks near 60 s | Quiet, sustained feel by level. Tag: artist psmithp, title "Bereaved". 3:47 means you take a 30 s slice. | UNKNOWN (Audioblocks-style suffix) |
| 3 | `P:\Sounds\Music\forgotten_zkzScHSu.mp3` | 2:26.7 | -23.1 | Very flat, -23 to -29, almost no swell | Good as a bed that stays out of the way, will NOT swell by itself, you automate the swell. Encoded by Adobe Systems tag, source still unknown. | UNKNOWN |
| 4 | `P:\Sounds\Music\forgotten-remastered_zyG8iSS_.mp3` | 2:38.6 | -20.1 | Not windowed | Remaster of #3, not heard. | UNKNOWN |
| 5 | `P:\Sounds\Music\november.mp3` | 3:32.1 | -21.5 | Quiet, slow build to -20 near 90 s | Very quiet, long. No tags. | UNKNOWN |
| 6 | `P:\Sounds\Music\in-remembrance_zkuEpeH_.mp3` | 1:00.9 | -19.8 | -30 rising to -20 by 20 s, then steady, hard stop at the end (-100) | Right length for the whole trailer. Name suggests a memorial tone, a funeral beat only. Ends with a clean cut, which suits a "cut to silence" if the cut lands on the tap. | UNKNOWN |
| 7 | `P:\Sounds\Music\reprieve_MkOQiBH_.mp3` | 49.7 s | -19.5 | Flat -23 to -20 | Short and level, not heard. Encoded by Adobe Systems. | UNKNOWN |
| 8 | `P:\Sounds\Music\searching-for-hope_MyqQQIru.mp3` | 2:01.1 | -18.2 | Moves between -17 and -29, some swells | Tag lists "flowing, spacious, pure, emotional, innocent, romance, piano" (artist neilcross). Romance tag is a tone risk for a war and funeral story. | UNKNOWN |
| 9 | `P:\Sounds\Music\somber-ceremony_G13__zBd.mp3` | 1:00.9 | -16.5 | Flat -18, ends -55 | Name says ceremony, a flag or funeral read the writing room wanted to avoid. Louder and flat, no swell. | UNKNOWN |
| 10 | `P:\Sounds\Music\bcc-031814-slow-and-somber-haunted-piano-notes-157.mp3` | 3:10.9 | -18.2 | Steady 190 s crescendo, -34 to -17 | Has a swell shape, but "haunted" is a horror cue (our Clayface pick). Wrong genre signal for a family and war story. | UNKNOWN |
| 11 | `P:\Sounds\Music\mysterious-cave-ambiance-3.mp3` | 4:09.8 | -24.6 | Very quiet and flat | An ambience bed, could sit under the garage half. Cave reverb may read wrong in a garage. Not heard. | UNKNOWN (Adobe Media Encoder tag only) |
| 12 | `P:\Sounds\Music\i-miss-you_M15wABS_.mp3` | 1:33.4 | -13.6 | Not windowed | Tag: piano, strings, romantic, sentimental. Loud and sentimental, wrong register. | UNKNOWN |

Not fitting (name and loudness): every `epic-*`, `heroic-*`, `triumphant-*`, `inspiring-*`, `anthem-*`, horror, rock, hip-hop, and `solace-acoustic-guitar-piano` (guitar, banned by the writing room), `ssm-102518-a-moment-to-worry` (15.5 s, -13.4 LUFS, too short and loud), `personal-effect` (-8.1 LUFS, too hot), `beautiful-way-to-end` (21 s, -12.2 LUFS).

### Adobe pack candidates (the only owned material with a published license statement)
Files are loops and stems, not songs. Length measured with ffprobe.
| Path | Length | Use |
|---|---|---|
| `P:\Sounds\Music\adobe\Ambient\Pads_51BPM\StrngPad03.wav` | 14.1 s | Sustained string pad, loop 4 times for a 56 s bed |
| `...\Ambient\Pads_51BPM\StrngPad01.wav`, `StrngPad02.wav` | 9.4 s each | Pad alternates |
| `...\Ambient\Pads_51BPM\OrgnPad01.wav` to `03` | 4.7 s | Organ pads, short, likely too church-like |
| `...\Ambient\Chamber_Strings_60BPM\ChamStr01-D.wav`, `ChamStr05-D.wav` (14 files in folder) | 8.0 s | Chamber strings in D, same key as each other so they can layer |
| `...\Classical&Orchestral\Lush_String_Eb_80BPM\LushEb01.wav` | 12.0 s | Lush strings, Eb key (do not mix with D files without checking) |
| `...\Classical&Orchestral\Arco_Eb_80BPM\ArcoEb01.wav` | 3.0 s | Bowed note one-shot, could be the swell accent |
Cost of using these: Zac builds a bed by looping and layering, and must check key match by ear. Benefit: the licensing story is the cleanest of anything owned.

### Verdict on owned music
- Best fit by shape: #1 (sad piano), then #6 (60 s memorial piece with a clean end).
- Best fit by license risk: the Adobe pads and strings, once the readme/EULA is checked.
- Not one loose mp3 can be called cleared. If the client later gets a claim, WKP is on the hook.

---

## 2. Licensed and free options (what I actually read)

| Source | Key license line | URL | Client use on four platforms | Not verified |
|---|---|---|---|---|
| Pixabay (music) | Grant: "royalty-free right to download, use, copy, modify or adapt the Content", "for commercial or non-commercial purposes". Prohibits selling it standalone and using it "in any immoral or illegal way". The summary page says you can use content "without having to attribute the author." | https://pixabay.com/service/terms/ and https://pixabay.com/service/license-summary/ | Allowed in principle. Neither page mentions client work, Content ID or any platform by name. | Content ID behavior (the terms do not mention it); whether a given track is AI-generated (Pixabay requires uploaders to tick an "AI-generated" box, so filter and read the track page); no specific tracks retrieved |
| YouTube Audio Library | "Only music and sound effects from the Audio Library are known to YouTube to be copyright-safe." CC tracks need credit in the description; standard-license tracks do not ("Attribution not required" filter). | https://support.google.com/youtube/answer/3376882 | Official page does not say whether use off YouTube or in client work is allowed ("can't give legal guidance"). Third parties disagree. Do not rely on it for Instagram, TikTok or Facebook without the per-track check. | Per-track licenses; off-YouTube use |
| Mixkit (Stock Music Free License) | Mixkit's own info page: "Allows use in commercial projects (YouTube videos, social media marketing, online ads, music videos)... No attribution required." Restriction: "Items cannot be resold in their original form." | https://mixkit.co/llm-info/ (the full license text at https://mixkit.co/license/ did not load in my fetch) | Looks allowed for social marketing. Client work and Content ID not addressed in what I could read. | Full license text |
| Free Music Archive | License is per track. Example I read: Maarten Schellekens, "Sax and Piano (free track)" is "CC0 1.0 Universal License", no credit required, 1:34. Another piano and cello track I saw is CC BY-NC-ND (NOT usable commercially). | https://freemusicarchive.org/music/maarten-schellekens/public-domain-1/sax-and-piano-free-track | CC0 tracks are the safest free class. Filter hard for CC0 or CC BY and read each page. The Schellekens track is sax, not a fit. | No CC0 cello or low-piano track found yet; FMA terms-of-use URL returned 404 |
| Storyblocks (what Zac may already own from 2016 to 2017) | Table: perpetual use "No" for Individual and Small Business, "Yes" for Business. Text: "Anything you create and publish during your time as a Storyblocks member will be covered by our license - forever." Individual license: one person, one YouTube channel. | https://www.storyblocks.com/license | NOT cleared. Page does not address client work and does not resolve its own contradiction. | Zac's account type, dates, any license certificates |
| Adobe (Audition/Premiere bundled loops) | Adobe: royalty-free, subject to the EULA and readme, no standalone redistribution. | https://www.adobe.com/products/audition/offers/audition-dlc | Likely fine inside a finished trailer. Client work not named anywhere I found. | Current EULA text, readme in the library download |
| Epidemic Sound | Official pricing page text I retrieved: "All of our plans include unlimited downloads and usage"; "Ad campaigns are allowed only on the Pro or Enterprise plan." Prices did not render. | https://www.epidemicsound.com/pricing/ | Third-party reviews say the Creator plan excludes client work and that Pro is the freelancer tier. | Exact prices: **not retrieved** (third-party figures conflict, so I am not quoting any) |
| Artlist | Official page returned 403. Third-party aggregators say the Social plan excludes client work and a Pro license covers it. | https://artlist.io/page/pricing | Social plan: not for client work (third-party). | Exact prices: **not retrieved** |

Plain read: three free sources (Pixabay, Mixkit, FMA CC0) have license text that allows commercial use without credit, but none of what I could read names client work or Content ID. For a paid client job, the careful move is to save a dated screenshot of the track page and the license page for each track used (the cue sheet below has a "proof saved" column for this).

A free-generator path exists but is thin: see section 3.

---

## 3. Suno and generator prompts

### Suno terms (official, retrieved 2026-11-04 from https://suno.com/terms, effective Sept 3, 2026, revised Aug 10, 2026)
- Paid tiers: "Suno hereby assigns to you all of its right, title and interest in and to any Output owned by Suno", "provided such Output will remain subject to these Terms of Service including any applicable commercial use restrictions." Commercial exploitation applies "solely to the extent it adheres to Suno's Conditions of Access and Use", and only for Output downloaded "through an approved channel."
- Free and basic tiers: use limited to "your lawful, personal and non-commercial purposes."
- No guarantee: Suno "makes no representation or warranty to you that any copyright will vest in any Output", and disclaims non-infringement. Users indemnify Suno.
- Do not remove "fingerprint, watermark or metadata Suno appends to an Output."
- Pricing page (https://suno.com/pricing, retrieved today): Pro $8 per month billed yearly ($96/year), or $10 monthly; Premier $24 per month billed yearly ($288/year), or $30 monthly. Pro: 2,500 credits per month; Premier: 10,000. Commercial rights listed for both. Free: 50 credits per day, no commercial rights listed.
- Not confirmed: whether "commercial use" under Suno's terms extends to a trailer owned by a third-party client (the client posts it; WKP is the maker). I did not find a Suno statement on delivering Output to a client. Put it in the client's written agreement. Content ID can still flag AI music (community guidance, not tested). Zac's plan lapsed 2026-10-26, so anything made now on the free tier is non-commercial. Keep proof of plan and creation date.

### Three Suno prompts. ONLY IF SUNO CREDITS RETURN (needs a paid plan first, decision WRENCH-2026-11-04-01)
Method notes (community guides, not official, see `_spec\music-reference.md`): main genre and mood first in the Style box, 4 to 8 descriptors, positive replacement for each exclusion, section tags only in Lyrics box for an instrumental. Nobody can test these without Zac's credits. Sliders are starting points, not tested.
Length target for all three: ask for 60 to 75 s of music so the swell lands near 43 s and you cut the tail in the edit. Suno often runs long, so plan to trim at the tap.

**Prompt A, sustained cello (lower creative risk)**
- Instrumental mode: ON
- Style box: `Solo bowed cello, long sustained notes, sparse warm pad underneath, 56 BPM, D minor, intimate and quiet, grief and memory, slow swell near the end, long reverb tail, instrumental`
- Lyrics box: `[Intro: single low sustained note, very quiet] [Verse: slow cello line, sparse] [Build: gentle swell, pad rises] [Outro: hold final note and stop]`
- Exclude: `acoustic guitar, drums, vocals`
- Sliders to try: Style Influence about 65, Weirdness about 25.

**Prompt B, low piano and pad (lower creative risk, second)**
- Instrumental mode: ON
- Style box: `Soft felt piano, low register, slow sparse notes with long silences, warm analog pad, 60 BPM, minor key, tender and restrained, quiet cinematic, instrumental`
- Lyrics box: `[Intro: pad only, very quiet] [Verse: single low piano notes, wide spacing] [Build: one soft swell, pad opens] [Outro: piano note rings out and ends]`
- Exclude: `acoustic guitar, percussion, vocals`
- Sliders: Style Influence about 65, Weirdness about 30.

**Prompt C, bowed vibraphone (bolder)**
- Instrumental mode: ON
- Style box: `Bowed vibraphone, warm sustained pad, slow glass harmonica shimmer, 52 BPM, minor key, hushed and aching, ambient score, one long swell then stillness, instrumental`
- Lyrics box: `[Intro: soft bowed tone] [Verse: sustained vibraphone, no rhythm] [Build: shimmer rises, pad swells] [Outro: sudden stillness]`
- Exclude: `guitar, drums, vocals`
- Sliders: Style Influence about 55, Weirdness about 45. (Bowed vibraphone and glass harmonica are "untested" Suno words in our reference.)

**2 to 3 try plan:** (1) Prompt A, generate 2 variations, pick any with no vocals and no guitar. (2) If it drifts to guitar or drums, run B. (3) If both sound generic, run C with Weirdness raised. Check each for ghost vocals and for a swell that arrives too early. Edit the swell to 0:43 and cut at the tap. Stop after about 6 generations total.
Never include a living artist, a named song or a film score in a prompt (house rule).

### Free generator path (one prompt): YouTube Create / Dream Track (Lyria)
Search result (secondary coverage, not an official YouTube page): Dream Track lets US creators make instrumental clips for Shorts, with the 2023 pilot capped near 30 s, plus longer clips in the YouTube Create app. Another guide says Google has not published a commercial licensing page for Lyria 3 Pro output, so client use is UNCONFIRMED and the output carries a SynthID watermark. Whether Zac's account has the feature and whether it is free for him: not available to me. Check the live app before relying on it.
Prompt to paste if it is there: `Quiet instrumental, sustained cello and warm pad, slow, sorrowful but gentle, sparse, builds very slowly and ends on one held note, no guitar, no drums, no vocals.`
Treat as a sketch tool for timing, not a delivery track, until the commercial terms are read.

---

## 4. Cue sheet template (56 s master)

The guide's beats are written for a 60 s master (`Ian-Wrench-Turner-Trailer-Guide.md`). Times below are the writing room's plan scaled to 56 s, so nudge once the cut is locked. Only music and the key sound cues are listed. Garage ambience and SFX belong to wwd-vfx, listed as placeholders.

| Cue | Time (56 s) | What plays | Source | License | Proof saved Y/N |
|---|---|---|---|---|---|
| A1 | 0:00 to 0:28 | Garage room tone, ball bounce, ratchet click, lamp buzz, engine that never quite starts. No music. | wwd-vfx, `P:\Sounds\Sound FX\` (not audited by music) | TBD (SFX not reviewed by me) | N |
| M1 | 0:26 to 0:40 | Music enters very low under the hospital beat (-30 LUFS-ish feel), one sustained pad or single cello or piano note | See ranked picks | TBD | N |
| M2 | 0:40 to 0:46 | Slow rise to the swell, peak at the present-day beat as grown Brandon is under the old car | Same track, fader automation | TBD | N |
| X1 | about 0:46 to 0:47 | Ball taps his shoulder. Hard cut of music to true silence (no fade, no tail) | Sound design, one soft tap | Owned or recorded | N |
| S1 | 0:47 to 0:56 | Silence plus faint room tone, back cover line cards, end card. No sting. | wwd-vfx | TBD | N |
| ALT | any | A final soft single tone under the end card only if the client asks for one | Adobe `ArcoEb01.wav` (3.0 s) | LIKELY OK, readme not read | N |

Mix notes: report the final mix loudness with ebur128. Platforms normalize differently and I did not retrieve platform specs, so I am not stating a target number. The owned candidates above range from -16 to -25 LUFS before any mix.
Proof to save per track: screenshot of track page, screenshot of license page with date, download receipt or order number, and the filename.

---

## 5. Ranked pick

Constraints: client work, four platforms, nothing owned is cleared, no spend allowed without Zac.

1. **First choice: build the music from the Adobe pad and strings loops** (`StrngPad03.wav` looped, with `ChamStr01-D.wav` / `ChamStr05-D.wav` layered, and `ArcoEb01.wav` for the swell accent). Rights are the best documented of anything on disk (royalty-free per Adobe, readme and EULA to confirm), it is a sparse sustained bed by nature, and it never has a vocal or guitar. Cost: Zac hand-builds and automates the swell, and it may sound like a library pad. Check the readme in the Adobe download and the key match (D vs Eb) by ear.
2. **Second choice: `P:\Sounds\Music\jdi-0414-eb-min-sad-cinematic-piano.mp3`**, best natural shape (quiet start, swell, decay to silence in 82 s), but license is UNKNOWN. Use only if Zac can show where it came from (decision WRENCH-2026-11-04-03). Run alongside this: Zac auditions Pixabay and Mixkit for "ambient piano" and "cello" and FMA with the CC0 filter, and saves dated screenshots of the license pages for the one he picks.
3. **Fallback: silence-forward trailer.** Garage ambience carries nearly the whole run, one very quiet pad from the Adobe loops only under 0:40 to 0:46, hard cut on the tap. The writing room's own note allows "silence into the tap," so this still fits the brief.
4. **"Nothing fits" plan:** (a) Do not use any unknown loose mp3, even if it is perfect. (b) Offer Ian the fallback above. (c) If Zac wants a real score, the two honest paid routes are a one-month Suno Pro ($8 yearly price or $10 monthly, retrieved today) with the three prompts above, or a paid library plan that explicitly covers client work (Epidemic Pro or Artlist Pro tier, prices not retrieved). Both are Zac's spend decisions. (d) Put a one-line rights clause in the client agreement saying who is responsible for platform claims.

---

## Decisions queued (D:\WKP\logs\DECISIONS.md)
- WRENCH-2026-11-04-01: Suno renewal (spend), only if Zac wants the Suno path.
- WRENCH-2026-11-04-02: Paid music library for client work (spend), prices not retrieved.
- WRENCH-2026-11-04-03: Can any owned loose mp3 be used for the client? Zac to show provenance, or accept none.

## What I could not verify
- Anything about how any track sounds.
- Provenance of every loose mp3 on P:.
- Storyblocks status of Zac's account and whether the 2016 to 2017 downloads are covered.
- Full text of Mixkit's license, Adobe's current EULA and per-library readme, FMA terms of use.
- Epidemic and Artlist prices and exact client-work wording.
- Whether Suno's commercial terms cover a track delivered to a third-party client.
- Whether YouTube Create / Dream Track is available and cleared for commercial or client use.
- Platform loudness targets for the four platforms.
