# A Knight's Tale (2001) review: free intro and outro music from what Zac already owns

Date: 2026-11-19. Prepared by the music agent for Jarvis and Zac.
Scope: free only. Nothing bought, nothing generated, nothing downloaded, nothing moved on P:. Test mixes live in `D:\WKP\scratch\akt-music\`.

**Honesty note: I cannot hear audio.** Every description of a file comes from its file name or from measurements (length, loudness, peak, and a loudness curve in small time slices). Zac has to listen before anything goes in the edit.

## 1. The short answer

| Use | Best free pick | File | Length | Measured level |
|---|---|---|---|---|
| Intro sting | Layered mix built from Adobe Audition sound effects and loops already on P: | `D:\WKP\scratch\akt-music\intro-6s.wav` | 6.00 s exactly | -14.05 LUFS, true peak -1.58 dBTP |
| Outro under the thank-you | Same layers, longer, ends on a held horn and guitar chord | `D:\WKP\scratch\akt-music\outro-18s.wav` | 18.00 s (I chose 18 s, inside the 15 to 20 s range) | -14.03 LUFS, true peak -1.53 dBTP |
| Outro, pre-lowered | Same outro already turned down 18 dB, drop straight under the voice | `D:\WKP\scratch\akt-music\outro-18s-under-voice.wav` | 18.00 s | -32.03 LUFS, true peak -19.53 dBTP |

Numbers above are from ffmpeg loudnorm (measure only) run on the finished files. ffmpeg ebur128 gave the same picture: intro -14.2 LUFS, peak -1.6; outro -13.9 LUFS, peak -1.5.

Every layer in both mixes is from Adobe's own sound libraries on P: (the Adobe Audition sound effects and the Adobe loop folders). No Storyblocks-style files and no rock-the-crowd.mp3 are used, because those have no license proof on disk.

**One line per use:**
- **6 s intro:** use `intro-6s.wav` (owned Adobe layers, free, no credit line). If Zac wants a real composed track instead, the next free try is Adobe Firefly's music generator on the free daily allowance (see Section 6), not ElevenLabs.
- **Outro:** use `outro-18s.wav` and set it 18 dB under the voice in Premiere (or drop in `outro-18s-under-voice.wav`). Fallback: a YouTube Audio Library track filtered to "Attribution not required".

## 2. What Zac should listen for (I cannot)

1. **Does the stomp pattern sound like the famous stomp-stomp-clap song?** I built it to be different on purpose: 120 BPM (the film's song sits around 81 BPM), three stomps per bar with a late second stomp (beats 1, 2-and, 4) and claps on beats 3 and 4-and. If it still reads as that song to his ear, say so and I change the pattern.
2. **Is the guitar in tune with the horns?** The guitar loop, the power chords and the horn files are all labeled "E" in their file names. I did not check pitch. Listen at 4.0 s in the intro and at 10 s and 13 s in the outro.
3. **Does the crowd sound like an arena or like a bullfight with a Spanish feel?** The outro crowd bed is Adobe "Human Crowd Bull Fight 02". The name worries me a little. Swap to "Human Crowd Hooray Continuous 01" if it sounds wrong.
4. **Do the claps sound like a dance-music clap?** They are from Adobe's "Trance Elements" folder. If too electronic, swap for "Human Crowd Golf Clapping 02" (a real crowd clap).
5. **Limiter pumping.** Both files run through a brickwall limiter to reach -14 LUFS with true peak under -1. Listen for the crowd ducking on each stomp.
6. **The end of the intro.** The hit lands at 4.0 s and everything fades from 4.9 s to 6.0 s. Check it does not sound chopped.

## 3. Owned library search (Step 1)

Searched `D:\WKP\data\assets\p-drive-index.csv` (27,207 files) for stomp, clap, boots on wood, crowd, cheer, roar, war drum, horn, fanfare, medieval, arena, guitar, power chord, tournament. Nothing on P: is named "medieval", "tournament", "joust" or "knight" except one Templar chant video rip (see below).

### Strong candidates found (all measured with ffmpeg)

| File (under P:\Sounds\) | Length | Loudness | Peak | Use | License note on disk? |
|---|---|---|---|---|---|
| Sound FX\Adobe\Human Elements\Human Crowd Stomping Feet 02.wav | 11.8 s | not measured whole | | real crowd stomps, steady pulse about every 0.8 s (from loudness curve). I cut one stomp out and reuse it. | No file. Adobe Audition SFX, license read on Adobe's page (Section 5) |
| Sound FX\Adobe\Human Elements\Human Crowd Cheer 04.wav | 13.6 s | | | cheer swells up by about 1.5 s, peaks near 2 s | same |
| Sound FX\Adobe\Human Elements\Human Crowd Hooray 04.wav | 1.7 s | | | short cheer burst for the button | same |
| Sound FX\Adobe\Human Elements\Human Crowd Hooray Continuous 01.wav | 17.0 s | | | alternate outro crowd bed | same |
| Sound FX\Adobe\Human Elements\Human Crowd Bull Fight 02.wav | 26.8 s | | | arena crowd with big roars near 13 s and 20 s | same |
| Sound FX\Adobe\Foley Footsteps\Foley Footstep Cowboy Boots Jump On Hollow Wood Surface Single 01.wav | 0.62 s | -20.9 LUFS | -1.5 dBFS | boot on hollow wood | same |
| Sound FX\Adobe\Foley Footsteps\Foley Footstep Cowboy Boots Jump On Wood Boardwalk Single 01.wav | 0.68 s | -21.4 | -4.5 | second boot for doubling | same |
| Sound FX\Adobe\Foley\Foley Table Fist Hits Hollow Wood Table 08.wav | 0.68 s | -22.0 | -3.4 | wood thump under the stomp | same |
| Music\adobe\Drum One Shots\...\StereoFloorTom01.wav | 2.9 s | | | war-drum weight under each stomp | No file. Adobe loop folder, see Section 5 caveat |
| Music\adobe\Drum One Shots\...\StereoKick01.wav, BrightCrash01.wav | 0.5 s, 7.2 s | | | button hits | same caveat |
| Music\adobe\Techno&Dance1\Trance_Elements_91BPM\Claps.wav, VerbClaps.wav | 1.3 s each | -22.4, -27.3 | -5.7, -4.8 | single clap at the start of each file | same caveat |
| Music\adobe\Funk&Rock2\Heavy_Rock_Guitar_120BPM\GrindChords1-E.wav | 2.00 s (one bar at 120 BPM) | | | the rock-guitar nod | same caveat |
| Music\adobe\Funk&Rock1\Brit_Stack_OneShots\BritOneShotsMajor\BritStackChord01-E.wav, BritStackChord25-E.wav | 2.2 s | | | held E guitar chord, no natural decay (I fade it) | same caveat |
| Music\adobe\Classical&Orchestral\Horns_E_80BPM\HornsE05.wav, HornsE06.wav, HornsE04.wav | 1.5 s, 3 s, 3 s | -13.1 (E05) | -1.8 | horn hit and held horn chord | same caveat |
| Music\rock-the-crowd.mp3 | 175.8 s | -7.4 LUFS | +1.1 dBTP | full owned track (from name, not heard) | **No license file on disk.** Not used |
| Music\rock-guitar_f1HxpNS_.mp3 | 6.1 s | -14.5 | -3.1 | guitar riff, pulse about 120 BPM | **No license file.** Storyblocks-style name. Not used |
| Music\extreme-rock-guitar-loop-2_M1A66rHu.mp3 | 15.4 s | -10.0 | -1.5 | guitar loop | **No license file.** Not used |
| Music\tribal-drum-dramatic-chase-loop-120-bpm_f1MZCCN_.mp3 | 8.1 s | -8.3 | +0.2 | drum loop | **No license file.** Not used |
| Music\cinematic-drums-choir-voices_MyYKaSSO.mp3 | 31.0 s | -15.9 | -2.5 | drums and choir | **No license file.** Not used |
| Sound FX\crowd-cheer-baseball-game_z1IbPhE_.mp3, crowd-cheers-and-whistles_MyWbxfVu.mp3, crowd-battle-cry-charge-scream_MJPHZu4_.mp3 | 24.0 s, 3.3 s, 14.2 s | -16.3, -15.0, -16.9 | -0.1, 0.0, -8.6 | crowd | **No license file.** Storyblocks-style names. Not used in the final mixes |
| Music\Le chant des templiers Chants of The Knights Templar FULL HD.mp3 | 188 MB | | | named like a YouTube video rip | **Do not use.** No license, looks ripped |

**License files on disk:** none. A search of the index for license, readme, terms, .txt, .pdf, .rtf and .htm under P:\Sounds returned nothing. So:
- Adobe Audition SFX folders (Human Elements, Foley, Foley Footsteps and the rest): Adobe's own page states the license (Section 5), and Zac cleared the Adobe SFX library on 2026-11-17.
- Adobe music loop folders (`P:\Sounds\Music\adobe\`): almost certainly Adobe's Audition loop content, but the Adobe page I read covers the sound effects only and does not mention loops. Not verified from an Adobe page.
- Files with the 8-character code at the end of the name (for example `_z1IbPhE_`) follow the Storyblocks/Audioblocks naming style. No receipt or plan proof on disk. Same open question as the Vision Quest note (TASKS: "confirm the Audioblocks-style sound files came from a paid plan").
- rock-the-crowd.mp3: no license on disk.

## 4. The sound recipes (Step 2)

Grid: 120 BPM, one beat = 0.5 s, one bar = 2.0 s. The Adobe guitar loop is exactly one bar at 120 BPM, which is why I picked this tempo.

**One "stomp" =** boot on hollow wood (0 dB) + boardwalk boot 18 ms later (-2 dB) + fist on wood table 9 ms later (-4 dB) + floor tom (-6 dB) + one cut crowd stomp (first 0.6 s of Human Crowd Stomping Feet 02, +2 dB in the intro, fade 0.4 to 0.6 s).
**One "clap" =** Claps.wav (0 dB) + VerbClaps.wav 12 ms later (-3 dB).
**One bar =** stomp at 0.0, stomp at 0.75 (-1 dB), clap at 1.0, stomp at 1.5, clap at 1.75 (-1 dB).

### Intro sting, 6.0 s (`intro-6s.wav`)
| Time | What plays | Level |
|---|---|---|
| 0.00 | Crowd Cheer 04 from its 1.2 s point, fade in 0.2 s | -4 dB |
| 0.00 to 2.00 | Bar 1 of stomps and claps | as above |
| 2.00 to 4.00 | Bar 2 of stomps and claps, plus GrindChords1-E guitar | guitar -6 dB |
| 4.00 | THE HIT: stomp (+1 dB), crowd stomp (+3 dB), kick (-2), crash (-6), BritStackChord01-E power chord (-1, fades 1.2 to 2.1 s), HornsE05 horn (-3), Hooray 04 crowd burst (-3) | |
| 4.90 to 6.00 | Whole mix fades out | |
| 6.00 | Hard stop. File ends at exactly 6.000 s | |

### Outro, 18.0 s (`outro-18s.wav`)
| Time | What plays | Level |
|---|---|---|
| 0.00 | Crowd Bull Fight 02 bed, fade in 1.5 s, runs the whole outro | -8 dB |
| 0.00 to 2.00 | Bar of stomps only, no claps, quieter | -4 dB |
| 2.00 to 10.00 | Four bars of stomps and claps, guitar loop on every bar | stomps -2 dB, guitar -8 dB |
| 10.00 | Button: stomp, crash (-8), BritStackChord25-E (-4, fades 1.4 to 2.15 s), HornsE06 (-3) | |
| 11.00, 12.00 | Slowing single stomps, getting quieter | -3, -5 dB |
| 13.00 | Resolve: last stomp, kick (-4), HornsE04 held horns (-2), BritStackChord01-E (-5, fades 0.6 to 2.1 s), Crowd Cheer 04 from its 1.0 s point (-6) | |
| 15.00 to 18.00 | Whole mix fades out (3 s) | |
| 18.00 | End. Under-voice version is silent from about 17.5 s | |

### Loudness step
Mixed with no normalize (amix normalize=0), measured, then: linear gain to -14 LUFS, upsample to 192 kHz, brickwall limiter at -1.6 dBFS sample peak, back to 48 kHz, 24-bit WAV. Remeasured and corrected the gain up to three times. The under-voice outro is the finished outro with a further -18 dB.

Raw mix before the loudness step (ffmpeg loudnorm measure): intro -13.54 LUFS, +0.22 dBTP (over, so the limiter was needed); outro -15.42 LUFS, +0.19 dBTP.

**On "-18 dB under voice":** I read it as the music sitting 18 dB below the voice. If the voice is at -14 LUFS, the outro under it lands near -32 LUFS, which is what the pre-lowered file is. If that is too quiet for his ear, use `outro-18s.wav` and set clip gain somewhere between -12 and -18 dB in Premiere.

### Exact commands
- Rebuild everything with one command:
  `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe -I D:\WKP\scratch\akt-music\build_akt.py`
  Every layer, offset and level is written out in that script (lists `intro()` and `outro()`), so one number can be changed and the mix rebuilt.
- The full ffmpeg mix commands it runs (one input per layer: 50 for the intro, 123 for the outro) are saved word for word in `D:\WKP\scratch\akt-music\ffmpeg-commands.txt`. Each input gets this chain, for example the guitar in the intro:
  `[N:a]aresample=48000,aformat=channel_layouts=stereo,volume=-6dB,adelay=2000:all=1[aN]`
  then all layers go into
  `amix=inputs=50:normalize=0:duration=longest,apad=whole_dur=6.0,atrim=0:6.0,afade=t=out:st=4.9:d=1.1`
- Loudness step (gain value differs per file, the script computes it):
  `ffmpeg -i _intro-6s-raw.wav -af "volume=<gain>dB,aresample=192000,alimiter=limit=0.8318:attack=1:release=60:level=false,aresample=48000" -c:a pcm_s24le intro-6s.wav`
- Measure:
  `ffmpeg -i intro-6s.wav -af loudnorm=I=-14:TP=-1:print_format=json -f null -`

Nothing was copied to `P:\WWD Kit\A Knights Tale\Sounds\` because this job was read-only outside scratch. Once Zac approves, copy the two WAVs there.

## 5. Free and license-clear sources (Step 3)

**Adobe Audition sound effects (what the mixes use).** Adobe's download page, retrieved 2026-11-19 (adobe.com/products/audition/offers/AdobeAuditionDLCSFX.html), says Creative Cloud "includes thousands of uncompressed, royalty-free audio sound effects", and that "you may use, display, modify, reproduce, and distribute the associated Content File", but "you may not distribute the Content File on a standalone basis", subject to the EULA. Bundles listed include Human Elements, Foley, Foley Footsteps, Sports and Impacts, all of which are on P:. Using them inside a YouTube video fits that wording. Posting the raw sound alone would not. The page does not mention the music loops, so the loop license is not verified from Adobe.

**YouTube Audio Library.** YouTube help page answer 3376882, retrieved 2026-11-19: the library is in YouTube Studio; Partner Program creators "can monetize videos" that use it; downloaded tracks are not claimed by Content ID; Creative Commons tracks need a credit in the description; standard-license tracks can be filtered for "Attribution not required". So yes, Zac can use it on his own channel. **Track names not retrieved:** the library is behind a YouTube Studio sign-in, so I could not pick tracks. Zac's route: YouTube Studio, Audio Library, filter Genre Rock or Cinematic, filter "Attribution not required", search "stomp", "anthem", "arena".

## 6. Other AI music makers vs ElevenLabs (Zac's question: "is there another AI to make music?")

Short answer: **yes, and the best free one for Zac is probably Adobe Firefly's music generator**, because Adobe's own page says it is free with an Adobe account (a small daily allowance) and that the output is royalty-free and commercially safe. Everything else either blocks downloads on free, or bans commercial use on free.

| Tool | Free plan (downloads, commercial, credit) | Cheapest paid | OK on a monetized YouTube review? | Runs locally free on RTX 5060 + 32 GB? | Source, retrieved 2026-11-19 |
|---|---|---|---|---|---|
| **ElevenLabs Music** | 10k credits a month. **Downloads: "Not permitted."** Commercial use permitted except film, TV, radio and studio games, but credit required ("denote Eleven Music"). Without downloads the free plan is no use for an edit. | **Starter: $1 first month, then $6 a month** (30k credits, 30 min of music downloads a month, "Music commercial use", no credit needed). Music costs 900 credits per minute, so 30k credits is about 33 min | Paid: yes under "online" use, film/TV excluded. Whether a YouTube video counts as "film" is not stated. Not verified | No | elevenlabs.io/pricing; elevenlabs.io/music-terms (last updated 09 October 2026) |
| **Suno** | 50 credits a day, **"No monthly song downloads"**, **"No commercial rights."** | **Pro $8 a month billed yearly ($96 a year)**, $10 struck through, 20 downloads a month, commercial use rights | Paid: commercial rights. Free: no. Zac's plan is lapsed | No | suno.com/pricing |
| **Udio** | **Not verified.** Official pricing and terms pages load by script and showed nothing. Third-party blogs say free is non-commercial and that downloads were switched off on 2025-10-29, with no sign they are back | Not verified (blogs say $10 a month Standard) | Not verified, do not use | No | udio.com/pricing, udio.com/terms-of-service (empty to my fetch tool); blogs listed in Sources |
| **Stable Audio (web, stableaudio.com)** | **Not verified.** Official page empty to my fetch tool. Third-party captures conflict: most say Free is "Personal, non-commercial use" | Not verified (one review says Solo $12 a month is the first commercial plan) | Not verified | Web version no | stableaudio.com/pricing (empty to my tool) |
| **Stable Audio Open 1.0 (local)** | Free model. **License: Stability AI Community License: free commercial use for anyone under USD $1M annual revenue, and you own the outputs** (stability.ai/license) | $0 | Yes by the license, Content ID not addressed | **Yes, likely.** 1B parameters, up to 47 s, 44.1 kHz stereo. VRAM need not stated on the model page. Model page says it "is better at generating sound effects and field recordings than music" and needs prompt work. Honest read: fine for crowd and stomp textures, weak for a rock anthem. Gated download on Hugging Face (accept terms). Not installed | huggingface.co/stabilityai/stable-audio-open-1.0; stability.ai/license |
| **ACE-Step v1 3.5B (local)** | Free model, **Apache 2.0** license | $0 | License allows it. Model card asks not to pass AI music off as human-made | **Probably**, full songs, but VRAM not stated on the card (only speed on 4090/3090). Card admits "gacha-style" results that swing with the seed | huggingface.co/ACE-Step/ACE-Step-v1-3.5B |
| **Meta MusicGen (local)** | Weights are **CC-BY-NC 4.0: non-commercial. Not usable** on a monetized channel | n/a | **No** | Would run, but license rules it out | huggingface.co/facebook/musicgen-medium |
| **YouTube Audio Library** | Free in YouTube Studio, monetizable, not claimed by Content ID, credit only for CC tracks | $0 | **Yes** | n/a | support.google.com/youtube/answer/3376882 |
| **YouTube AI music tools** | Two tools in news reports: a "Replace song" generator that only appears on a video with a music claim (makes 4 instrumentals, no prompt), and a prompt-based "Music Assistant" in Creator Music for some Partner Program creators. **No official YouTube help page found**, so access and terms for Zac's channel are not verified. Check YouTube Studio, Audio Library, for a Music Assistant tab | $0 | Not verified | n/a | news only (techcrunch.com 2025-04-10, tubefilter.com 2026-05-04) |
| **Adobe Firefly (Generate music / Generate Soundtrack)** | Adobe page: "you can use the Adobe Firefly AI music generator for free with an Adobe account", "free daily generations", "royalty-free, fully licensed and safe for commercial projects", 5 s to 5 min. Daily free count not stated. Whether free-tier tracks can be downloaded: not stated | Firefly Standard $9.99 a month (up to 100 min of music) | Adobe says commercially safe. Content ID not addressed | No | adobe.com/in/products/firefly/features/ai-music-generator.html; adobe.com/products/firefly/plans.html |
| **Firefly on Zac's current plan** | Memory says Zac's Firefly credits are at zero (2026-11-17). The free daily allowance may still apply, not verified. Adobe's credit help page returned 403, so whether his plan includes music is **not verified** | | | | helpx.adobe.com (403) |
| **vidIQ music** | vidIQ's own credits page lists "Music, per track, 25 credits", but only in the vidIQ MCP credit table. Free plan 150 credits a month, Pro 1,000. **Music license and download rules not found**, plan prices not on that page | not retrieved | Not verified | No | support.vidiq.com/en/articles/13928456-features-credits-by-plan |

**Recommendation, free first:**
1. Use the owned Adobe mixes now (license read, $0).
2. If he wants a composed track: Adobe Firefly free daily music generation, after he confirms in the app that the free tier allows download. That is a generation on his account, so Jarvis brings it to him first.
3. If he will pay: ElevenLabs Starter ($1 first month, then $6) or Suno Pro ($8 a month billed yearly) are the cheapest paid routes with commercial rights. Spend decision already queued as WWD-2026-11-19-02.

## 7. What I could not verify
- Any sound. I cannot hear. All "sounds like" lines are from names and measurements.
- Pitch of the guitar, chords and horns (labeled E by file name only).
- License of the Adobe music loop folders (Adobe page covers SFX only).
- License of every Storyblocks-style file, rock-the-crowd.mp3, and the Templar chant rip (no proof on disk).
- YouTube Audio Library track names (sign-in wall), and YouTube's AI music tools from an official page.
- Udio and Stable Audio web plans from their own pages (pages empty to my tool).
- vidIQ music license and plan prices; Firefly free-tier download rule and Zac's plan access to music.
- Whether ElevenLabs counts a YouTube review as "film" under its exclusion.

## Sources (all retrieved 2026-11-19)
- [ElevenLabs pricing](https://elevenlabs.io/pricing)
- [ElevenLabs music terms](https://elevenlabs.io/music-terms)
- [Suno pricing](https://suno.com/pricing)
- [YouTube Audio Library help](https://support.google.com/youtube/answer/3376882)
- [Adobe Audition sound effects download and license](https://www.adobe.com/products/audition/offers/AdobeAuditionDLCSFX.html)
- [Adobe Firefly AI music generator](https://www.adobe.com/in/products/firefly/features/ai-music-generator.html)
- [Adobe Firefly plans](https://www.adobe.com/products/firefly/plans.html)
- [Stable Audio Open 1.0 model card](https://huggingface.co/stabilityai/stable-audio-open-1.0)
- [Stability AI license](https://stability.ai/license)
- [ACE-Step v1 3.5B model card](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B)
- [MusicGen medium model card](https://huggingface.co/facebook/musicgen-medium)
- [vidIQ features and credits by plan](https://support.vidiq.com/en/articles/13928456-features-credits-by-plan)
- Third-party, not official: [Udio pricing 2026 (activepieces)](https://www.activepieces.com/blog/udio-pricing-2026-plans-credits-and-free-tier), [Is Stable Audio worth it (techpresso)](https://academy.techpresso.co/reviews/is-stable-audio-worth-it), [YouTube AI music tool (TechCrunch)](https://techcrunch.com/2025/04/10/youtube-rolls-out-a-free-ai-music-making-tool-for-creators), [YouTube royalty-free music test (Tubefilter)](https://www.tubefilter.com/2026/05/04/youtube-ai-tool-royalty-free-music-resolve-content-id/)
