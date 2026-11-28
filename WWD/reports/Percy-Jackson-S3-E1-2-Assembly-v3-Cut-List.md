# Percy Jackson S3 Eps 1 and 2: Assembly v3 cut list (2026-11-26)

File: `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\export\Percy-Jackson-S3-E1-2-Assembly-v3.mp4` (v1 and v2 untouched).
Phone copy: same folder, `Percy-Jackson-S3-E1-2-Assembly-v3-240p-phone.mp4` (426x240).
Measured: 1920x1080, 30 fps, H.264, 56,504 frames, 31:23.47, AAC 48 kHz stereo. Whole file -14.0 LUFS, -1.3 dBTP. No black frames, no silence over 2 s. One freeze report at 13:37.8, which is the 6 s Artemis still (expected).

## What changed from v2
1. Intro: Zac's approved Firefly title (8.0 s, own music and WWD logo) replaces Trident Tide. Host voiceover runs over it as audio only. Poster follows (5 s), then 0.8 s final-frame hold, then cams. The title file itself has built-in letterbox bars (source, not mine).
2. Cams: 248 shots following the speaker from the two isolated mic tracks (WW cam 1143 s, KingZ cam 564 s, two-shot 144 s). Cut leads the speaker by 4 frames, shots under 1.2 s absorbed, fast back and forth and both-talking moments held on the two-shot. Longest single cam hold 59 s. The two-shot is the raw StreamYard scene, so it carries the Winter Wolf's Den banner.
3. Pictures: 29 run-sheet pictures plus 7 from the new pull (book cover, Lightning Thief and Sea of Monsters posters, Tyson S2, Clarisse S2, sea cow D23 teaser frame, Zoe Nightshade). 35 total, none repeated, longest 6.0 s. Atlas, Oracle S3, Chiron S3, Clarisse S3, Mr. D S3 and the quest group are NOT on disk (walls, no captioned still).
4. Clips: C01 (7 s, Sneak Peek) and new C02 (8 s, Curse Teaser 1.0 to 9.0 s, one shot, on "holding the world up"). C02 who-is-this is unproven: the scout could not say if the strainer is Luke. Zac or wwd-clip-scout check, swap or drop. The clip-scout order for more clips was denied by the permission layer, so no other footage was downloaded.
5. Transitions: hard cuts for cams, 4-frame (0.13 s) dissolves on pictures. No zoom-settle.
6. Sound: music, effects and voice are separate stems in `D:\WKP\scratch\pj-edit\stems_v3\` (voice.wav, music.wav, sfx.wav). Swap a track and rebuild with `python D:\WKP\scratch\pj-edit\remix_v3.py <intro file> <outro file>`. Effects are normalized to -12 dBFS peak before the mix (v2 effects were near inaudible). Rimshot on "Nobody died" at -6 dBFS peak. Whoosh on each new picture.

## Loudness by layer (ffmpeg ebur128, pre-limiter stems plus the effective gain of the final mix, so approximate)
| Section | Voice | Music | Effects | Final mix |
|---|---|---|---|---|
| Intro 0 to 2 s | -10.0 | -37.3 | none | -10.0 LUFS |
| Intro 2 to 8 s | -13.3 | -18.6 | none | -13.0 LUFS |
| Speech 0:08 to 1:00 | -13.2 | none | none | -13.2 LUFS |
| Speech 5 to 10 min | -13.7 | none | -18.0 | -13.7 LUFS |
| Speech 20 to 25 min | -13.9 | none | -21.5 | -13.9 LUFS |
| Outro cards (18 s) | none | -15.0 | none | -15.0 LUFS, -4.1 dBTP |
| Whole file | -14.0 | -16.1 | -19.5 | -14.0 LUFS, -1.3 dBTP |

Voices are the loudest layer, music sits about 5 LU under the voice in the intro, effects are accents under the voice. NOT HEARD by me. Numbers only.

## Verified by frames
Contact sheet of 36 frames across the cut (cams alternate, pictures and the poster land), intro first 16 s at 2 fps, and 9 spot frames (book cover, Lightning Thief, Tyson, Clarisse, sea cow, Zoe, C02, cams). Not viewed: every cut, the rest of the pictures, the card sections beyond a frame check.

## Not verified or open
- Audio never heard. Cam sync checked by waveform correlation earlier, not by eye on every cut.
- Stand-ins for Zac's Spoiler Alert and Like and Subscribe clips (not on disk).
- Music licence for the ElevenLabs outro, picture rights (Disney press, posters, teaser corner marks), clearance not run.
- Next Up card is the generic one.
- qa-director pass not run on v3.
