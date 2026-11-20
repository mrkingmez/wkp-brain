# Ian "The Wrench Turner" trailer, Draft 3.3: SFX cue sheet and mix notes (sound-designer, 2026-11-20)

Job from studio-director. Plan followed: REVISED beat sheet v2 in `2026-11-20-brief-draft3-3.md`. Paths from `2026-11-20-asset-list.md` (media-manager), plus an ls check on 2026-11-20 of the Adobe files marked (ls ok) and the 17 Made takes (all 17 listed on disk).

**Status: nothing heard, nothing rendered, nothing generated, nothing downloaded, $0 spent.** Every sound below is "not heard". Levels are starting gains for the first mix, not tuned by ear. Timings come from the brief's beat sheet, not from watching the picture, so nudge every hit by eye to the real frame. Music is a separate lane (music agent, file `2026-11-20-music.md` not present when I wrote this); I only mark where SFX need room.

## Paths used
- ROOT = `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\`
- SFX = `ROOT\Audio\Sound FX\` (project copies)
- MADE = `ROOT\Audio\Sound FX\Made\` (ElevenLabs takes of 2026-11-17)
- ADOBE = `P:\Sounds\Sound FX\Adobe\` (owned Adobe library, free to use per Zac 2026-11-17)

## Level convention
Gain in dB on the clip before the master stage (same convention as the 2026-11-17 sheet). There is no dialogue, so "relative" means relative to the air bed (-34) and to the music lane. Rule of thumb: the air bed is the floor, hard hits sit 14 to 18 dB above it, memory hits sit 4 dB under the present-day hits. Fades are in seconds. Pan: centre unless noted. For 9:16 and 16:9 the audio is identical, so one build serves both.

## Two sound worlds (the idea behind every cue)
- **Present** (under the car, the garage): dry, close, metal on concrete, a low air bed. Ratchet clicks are the signature.
- **Memory** (V4, R3, R3b): same sounds but washed. Low-pass at about 5 kHz, room reverb about 1.2 s decay at 30 to 35 percent wet, 4 dB lower, air bed ducked. Build the wash in Audition (Studio Reverb) or ffmpeg `aecho`; not heard.
- **Homecoming, brotherhood, sweetheart** (beats 6 to 8): no voices, no children, sparse. Each beat gets only the sounds named below.

## Cue table: 45 s (24 fps, times in seconds from 0)

| Cue | Time | Beat | File (exact path) | Source in/out | Gain dB | Fade | Notes |
|---|---|---|---|---|---|---|---|
| A1 | 0.00 to 3.30 | 1 Present air bed | ROOT\Audio\Sound FX\Ambience Parking Garage 01.wav | 0.0 to 3.3 | -34 | in 0.0 (hard start), out 1.0 from 3.0 into the dissolve | Floor of the present. Same file returns at A19. Low rumble, may feel large, not heard. |
| S1 | 0.00 | 1 Ratchet click on frame one | SFX\Industry Ratchet Clicking 01.wav | 0.0 to 0.55, full | -16 | none | Must start on frame 1, not at 0.04. Trim any leading silence. Pan centre. |
| S2 | 0.90 | 1 Ratchet turn | SFX\Industry Tool Ratchet Turn Single 01.wav | full 0.65 | -18 | none | Spacing slows slightly (0.9, 1.7, 2.4) so it reads as a tired hand, not a loop. |
| S3 | 1.70 | 1 Ratchet turn | SFX\Industry Tool Ratchet Turn Short 01.wav | full 0.35 | -18 | none | |
| S4 | 2.40 | 1 Last ratchet turn | SFX\Industry Tool Ratchet Turn Single 01.wav | 0.0 to 0.55 | -19 | out 0.1 at 2.95 | Tail must be gone by the 3.0 dissolve so nothing present leaks into the dream. |
| D1 | 3.00 to 4.20 | 2 Dream dissolve bridge | SFX\Industry Tool Wrench Socket Wrench Turning 01.wav | 0.0 to 1.1, pitch down 2 semitones, reverb 60 percent wet | -28 | in 0.3, out 0.8 | Optional "metal ring in the memory" at the dissolve. Cut if it reads as a gimmick. Not heard. |
| M0 | 3.00 to 6.50 | 2 Memory air | SFX\Ambience Parking Garage 01.wav, low-pass 3 kHz, reverb 35 percent | 10.0 to 13.5 (offset in so it is not the same audio as A1) | -38 | in 1.0, out 0.6 | Replaces A1 for the memory. Warm, not a different place. |
| M1 | 3.20 to 5.20 | 2 Ball rolls in (V4 ball enters at clip 1.0 s = timeline 3.2) | MADE\ballroll_long_6s.mp3 | 0.0 to 2.0, then cut | -20 | in 0.4, out 0.3 at 5.2 | The "dream with more room" cue: low-pass 5 kHz, reverb 1.2 s decay, 35 to 40 percent wet. Not heard. Use the 6 s file, the 1 s and 2 s takes are too short. |
| M2 | 5.20 | 2 Ball bumps the boot (V4 clip 3.0 s) | SFX\Sports Baseball Bounce On Cement 01.wav | 0.0 to 0.5, low-pass 1.2 kHz | -26 | out 0.2 | Stand-in. A ball on a boot is softer than a ball on cement. See gap G1. Same memory wash. |
| M3 | 5.30 to 6.50 | 2 Reverb tail | tail of M1 and M2 through the reverb | n/a | n/a | out 1.2 | Let the room ring once, then it hands to R3. |
| M4 | 7.60 | 3 R3 wrench passes up | SFX\Industry Tool Wrench Socket Wrench Turning 01.wav | 0.0 to 0.9 | -22 | out 0.2 | Memory wash. On the hand-off motion, check by eye. |
| M5 | 6.50 to 9.50 | 3 Memory air continues | M0 file, same offset continued | 13.5 to 16.5 | -38 | out 0.4 at 9.5 | |
| X1 | 10.25 | 4 R3 to R3b crossfade, midpoint (crossfade runs 9.5 to 11.0) | MADE\wrench_on_tray_take1.mp3 | trim to the first clink only, about 0.0 to 0.8 | -20 | out 0.3 | The single wrench clink. Not heard: confirm the take is one clink and not two before use. Alt if it fails: SFX\Industry Tool Wrench Set On Pavement 01.wav (0.36 s, rougher, pavement not tray), reverb 40 percent wet. One clink only, nothing else in the crossfade. |
| X2 | 11.00 to 12.00 | 4 Hold on R3b | M0 file | 16.5 to 17.5 | -40 | out 0.35 hard at 12.00 | Reverb tail from X1 may lap into the present for 0.2 s to bridge the cut. Not more. |
| A2 | 12.00 to 16.00 | 5 Present, arms drop, lying thinking | SFX\Ambience Parking Garage 01.wav | 0.0 to 4.0 (restart, or use 30.0 onward if a loop point shows) | -34 | in 0.2, out none, continues | Air only. No ratchet: "stop dead on the arm drop". Close and quiet. |
| S5 | 12.10 | 5 Creeper settles (optional) | MADE\creeper_take2.mp3 | 0.0 to 0.8 | -30 | out 0.3 | Optional, skip if it draws the ear off the face. 3 s take, only the first 0.8 s. Not heard. |
| H0 | 16.00 to 22.00 | 6 Outdoor air | ADOBE\Ambience_2\Ambience Wind Blowing Through Trees 01.wav | 5.0 to 11.0 | -34 | in 0.4, out 0.5 at 22.0 | Index-only, not probed or heard by me. Trees and wind, no crickets (daytime). A1 air bed OUT here (fade 0.2 at 16.0). |
| H1 | 16.00 to 17.70 | 6 Steps on the walk | ADOBE\Foley Footsteps\Foley Footstep Cleats Walking On Cement 01.wav (ls ok) | 0.0 to 1.8, low-pass 4 kHz | -26 | in 0.1, out 0.4 | Stand-in, cleats may read hard (not heard), see gap G2. Use under the push-in; stop before the hug. |
| H2 | 17.60 | 6 Screen door opens | ADOBE\Household\Household Door Open Screen Door 01.wav (ls ok) | 0.0 to 2.1 | -24 | out 0.3 | Hinged type. Land it just before the hug cue H3. |
| H3 | 18.20 | 6 Embrace, cloth only | ADOBE\Foley\Foley Cloth Hit And Short Rustle Cloth 05.wav (ls ok) | 0.0 to 3.0 | -22 | out 1.0 (gone by 21.2) | Stand-in, no hug file exists. Soft, no voice, no breath. Alt: Foley Cloth Flap Jacket 03.wav trimmed to a soft tail. |
| H4 | 20.80 | 6 Screen door closes soft | ADOBE\Household\Household Screen Door Close 02.wav (ls ok) | 0.0 to 1.3 | -28 | out 0.3 | Optional, drop if H3 and H2 feel busy. |
| B1 | 22.00 to 25.00 | 7 Brotherhood glimpse: crickets, nothing else | ADOBE\Ambience_2\Ambience Wind With Crickets 01.wav (ls ok) | 20.0 to 25.0 | -32 | in 0.5 at 21.8, out 0.4 at 25.0 | Near-silence beat. Outdoor air H0 and everything else OUT by 22.0. No hits, no cloth, no music if the music lane allows. Do not use the bullfrog file (reads as swamp). |
| F1 | 24.80 to 28.00 | 8 Sweetheart: fire crackle, low | ADOBE\Fire and Explosions\Fire Fireplace Pops Crackle 01.wav (ls ok) | 30.0 to 33.2, low-pass 3 kHz, high-pass 150 Hz | -30 | in 0.5 (pre-laps 0.2 s), out 0.4 at 28.0 | Fireplace sounds indoor, the filters push it distant and outdoor. Not heard. See gap G5. Crickets B1 fade under F1 by 25.3 (-38). No party murmur, no voices, no children. |
| U1 | 28.00 | 9 Duffel set down (on the cut) | ADOBE\Household\Household Bag Set Down Duffle 01.wav (ls ok) | 0.0 to 0.9 | -18 | out 0.2 | Land on the hard cut to R5, the push-in then lives in quiet. Alt: ADOBE\Sports\Sports Bag Duffle Bag Drop Cement Floor 01.wav (ls ok, 1.2 s, heavier on cement). |
| A3 | 28.00 to 38.00 | 9 to 11 Present air returns | SFX\Ambience Parking Garage 01.wav | 40.0 to 50.0 | -34 | in 0.3 at 27.9, out 1.0 at 38.0 | Continuous under garage and car beats. |
| U2 | 28.60 | 9 Gloves (optional) | none good | n/a | n/a | n/a | Gap G4. Leave silent unless the phone take exists. |
| U3 | 30.50 to 34.50 | 10 Garage at rest, slow swell | SFX\Ambience Auto Repair Shop 01.wav | 20.0 to 24.0 | -42 rising to -38 | in 1.5, out 0.5 | Layered under A3 for a little more room as the push-in closes on the car. Only a 4 dB swell. No door sound (the door is already open). |
| S6 | 34.50 | 11 Cut under the car, ratchet returns on the cut | SFX\Industry Ratchet Clicking 01.wav | full 0.55 | -16 | none | Same sound as S1 on purpose, it is the callback. Dry. |
| S7 | 35.40 | 11 Ratchet turn | SFX\Industry Tool Ratchet Turn Single 01.wav | full | -17 | none | Slightly warmer and steadier than the opening: shorter gaps (0.9). |
| S8 | 36.20 | 11 Ratchet turn | SFX\Industry Tool Ratchet Turn Short 01.wav | full | -17 | none | |
| S9 | 36.90 | 11 Wrench turning, longer | SFX\Industry Tool Wrench Socket Wrench Turning 01.wav | 0.0 to 1.1 | -18 | out 0.3 at 38.0 | The "working again" sound. Hard stop by 38.0 black. |
| T1 | 38.00 to 41.00 | 12 Black and final line | A3 tail only | n/a | -34 falling to -46 | out over 3.0 | Air bed fades slowly under the text. No hits. Music lane decides what else sits here. |
| E1 | 41.00 | 13 End card click | SFX\Industry Tool Ratchet Turn Short 01.wav | full 0.35 | -17 | none | One click as the cover lands. Place 0.05 s BEFORE the music chord so they do not smear. Not heard. |
| E2 | 41.00 to 44.00 | 13 End card air | A3 tail | n/a | -46 | out 3.0 | Quiet under the held chord, gone by 44.0. |

Sounds I considered and left out on purpose: Mustang starter and V8 idle takes (the brief has no start-up beat), car door takes (no arrival by car), garage door files (door never moves in this cut; V7's rise is the cover story's), and any bounce of a present-day ball (V2, 9Sa and R4 are out).

## Cue table: 15 s (3 beats plus card, same files and sounds, shorter)

| Cue | Time | Beat | File | Source in/out | Gain dB | Fade | Notes |
|---|---|---|---|---|---|---|---|
| A1s | 0.00 to 3.30 | 1 Present air | SFX\Ambience Parking Garage 01.wav | 0.0 to 3.3 | -34 | out 1.0 from 3.0 | Same as A1. |
| S1s | 0.00 | 1 Ratchet frame one | SFX\Industry Ratchet Clicking 01.wav | full | -16 | none | Frame one with the hook line. |
| S2s to S4s | 0.90, 1.70, 2.40 | 1 Ratchet turns | S2, S3, S4 from the 45 s table | as above | -18, -18, -19 | S4 out 0.1 at 2.95 | Identical to the 45 s so one build can be trimmed to either. |
| M0s | 3.00 to 9.50 | 2 Memory air | SFX\Ambience Parking Garage 01.wav, low-pass 3 kHz, reverb | 10.0 to 16.5 | -38 | in 1.0, out 0.4 | |
| M1s | 3.00 to 4.50 | 2 Ball already rolling (V4 starts at clip 1.5) | MADE\ballroll_long_6s.mp3 | 1.0 to 2.5 (start mid-roll) | -20 | in 0.3, out 0.3 at 4.5 | Memory wash. |
| M2s | 4.50 | 2 Boot bump | SFX\Sports Baseball Bounce On Cement 01.wav, low-pass 1.2 kHz | 0.0 to 0.5 | -26 | out 0.2 | Stand-in (G1). |
| M4s | 6.20 | 2 R3 wrench passes up (R3 runs 5.5 to 7.5) | SFX\Industry Tool Wrench Socket Wrench Turning 01.wav | 0.0 to 0.9 | -22 | out 0.2 | Memory wash. |
| X1s | 8.50 | 2 R3 to R3b crossfade midpoint (crossfade 7.5 to 9.5) | MADE\wrench_on_tray_take1.mp3 (first clink) | 0.0 to 0.8 | -20 | out 0.3 | Single clink. Same alt as X1. |
| A2s | 9.50 to 12.00 | 3 Back under the car, war line on screen | SFX\Ambience Parking Garage 01.wav | 0.0 to 2.5 | -34 | in 0.2 at 9.4, out 0.5 at 12.0 | Air only, no ratchet. Hard cut from memory at 9.5, X1 tail may lap 0.2 s. |
| E1s | 12.00 | End card click | SFX\Industry Tool Ratchet Turn Short 01.wav | full | -17 | none | 0.05 s before the chord. |
| E2s | 12.00 to 14.50 | End card air | A1s file tail | 0.0 to 2.5 | -44 | out 2.5 | Gone by 14.5. |

The 15 s has no homecoming, brotherhood, sweetheart, duffel or garage cues, so none of those files are needed for it.

## Fence check (sound)
- No voices anywhere: no breath, no hum, no sigh, no "mm". Beat 6 is steps, a screen door and cloth only.
- No child sound, laughter, playground, kid chatter or crowd bed. Do NOT use `ADOBE\Ambience_1\Ambience Children Group Playground Distant 01.wav`, `P:\Sounds\Sound FX\ab-f-031616-38698401_crowd-chatter-ambience-01.mp3`, `ADOBE\Ambience_2\Ambience Shopping Area With People Outdoors 01.wav`, or `P:\Sounds\Sound FX\night-woods-crickets-chirp-dog-bark-distant-traffic_My3yUc4d.mp3` (dog and traffic).
- Sweetheart beat has fire only, no party murmur.
- Memory ball sound is a ball only, no boy sound, no "kid laughs". R3 and R3b are hands and a wrench only.
- Reminder: the memory boy is allowed on screen, never as a sound. Garage room tone take `MADE\garage_room_tone_20s.mp3` was prompted with "distant dog", so it is NOT used in this sheet. Use it only if Zac listens first and finds it clean.

## Gaps (honest list, free fix first)
| # | Gap | Stand-in used | Free fix first | ElevenLabs prompt (NOT RUN, needs Zac's yes, cost not retrieved here) |
|---|---|---|---|---|
| G1 | A ball bumping a boot (M2, V4 at about 5.2 s in the 45 s) | Baseball Bounce On Cement 01, low-passed | Zac records on his phone: roll a baseball into a leather work boot on a concrete floor, five takes, close, quiet room, nobody talking | "A baseball rolls slowly across a concrete garage floor and bumps softly against a leather work boot, one dull leather thud, quiet room, close microphone, no voices, no music." (2 s) |
| G2 | Boots on a front walk, outdoors | Cleats On Cement 01 at -26, low-passed | Zac walks 15 s on a concrete walk or driveway in boots, phone held low, three takes | "A man in leather boots walking slowly on a concrete sidewalk to a house, calm steady steps, light breeze, no voices, no music." (4 s) |
| G3 | A real hug, cloth on cloth | Foley Cloth Hit And Short Rustle Cloth 05 | Zac and a family member hug in thick jackets with the phone held near, rustle only, nobody speaking (no children in the room) | "Two adults hug, heavy jacket cloth rustles and settles, soft pat on a shoulder, no voices, no breath, no music." (3 s) |
| G4 | Work gloves set on a bench | none, leave silent | Zac drops a pair of leather work gloves on a wood table, phone close, three takes | "A pair of leather work gloves set down on a wooden workbench, one soft leather slap, quiet garage, close microphone, no voices." (2 s) |
| G5 | Distant outdoor bonfire crackle | Fireplace Pops Crackle 01, filtered | Zac records a fire pit or grill from 3 m away, 20 s, nobody talking | "A distant outdoor bonfire at night, soft wood pops and low crackle, a little wind, no voices, no music, no people." (10 s) |
| G6 | Gloves also not in the library | n/a | covered by G4 | covered by G4 |

Outdoor air for beat 6 (`Ambience Wind Blowing Through Trees 01.wav`) came from the index only, I did not probe it. If it is bad on listening, ask media-manager for another outdoor Adobe bed.

Do not run any of these without Zac's yes. Cost per generation: not retrieved here (no credit read tool used). If any run, save into `MADE\` and never overwrite the 17 existing takes.

## Mix notes (plain words)
1. There is no dialogue. The ratchet is the voice of the piece. Build it first, alone, then add everything else.
2. The air bed is the floor at -34. Hard hits sit 14 to 18 dB above it. Memory hits sit 4 dB lower and washed.
3. Hits land on the frame of the action. S1 on frame 1 of V1, S6 on the first frame of the cut under the car, U1 on the cut to R5, E1 on the first frame of the card. Check each against the picture, not the timecode.
4. Silence is a cue. Beat 7 (22.0 to 25.0) carries crickets only. Beat 5 (12.0 to 16.0) carries air only. Do not fill them.
5. The ratchet stops dead before every dissolve and before the arm drop. No tail leaks across a dissolve except the planned memory reverb tail (X2, 0.2 s).
6. Music lane: leave it to the music agent. Requests from the SFX side: (a) no music under 0.0 to 3.0 so S1 to S4 and the hook line read, (b) music out or at its lowest on 22.0 to 25.0, (c) the held chord lands 0.05 s after E1 at 41.0, (d) music ducks 4 to 6 dB under U1 (28.0) if it is playing, (e) if a bed plays under beat 6 it must be under H1 to H3 by 8 to 10 dB.
7. If Ian says no to the brotherhood beat: H1 takes 22.0 to 25.0. Do not run crickets under H1 (daytime). Extend H0 and the cloth tail to 25.0 instead and drop B1.
8. 9:16 and 16:9 share one audio build. Check the 9:16 on a phone speaker, the ratchet and the duffel should still read; the -16 hits may need +2 dB if not. Not heard.
9. One change at a time when tuning. Save the first mix as the baseline (name it `Ian-Trailer-3-3-mix-v1`), compare each change to it, keep every version.
10. Work on copies. Never edit the source files in `SFX\` or `MADE\`. Build in `D:\WKP\scratch\` or the project folder.

## Loudness: Zac's standard, -14 LUFS integrated and -1 dBTP true peak
This is Zac's stated standard for the final export. I did not re-check any platform's current guidance this run (not needed to follow Zac's number, but not verified). The earlier sheet used a proposed -16 LUFS, superseded by -14.

Measure AFTER export, on the exported file, never on the project:

```
ffmpeg -nostats -i "<exported file.mp4>" -filter_complex ebur128=peak=true -f null -
```

Read the Summary block at the end of the output: `I:` is integrated LUFS (target -14.0), `LRA:` is loudness range, `True peak:` `Peak:` is dBFS true peak (target at or below -1.0). Run it on each of the four files (45 s and 15 s, each in 9:16 and 16:9). Cross-check with:

```
ffmpeg -i "<exported file.mp4>" -af loudnorm=print_format=json -f null -
```

Report `input_i`, `input_tp` and `input_lra` as measured. Not measured by me: no export exists yet.

Expect trouble: the SFX are sparse and the open and the brotherhood beat are near-silent, so reaching -14 LUFS integrated comes from the music and the final chord. A limiter at -1.5 dBTP before export keeps the true peak under -1.0 (the 2026-11-17 rough cut measured -0.95 dBTP and needed this). The ebur128 gate ignores very quiet passages, so integrated can read fine while the near-silence still sounds very quiet on a phone. After the music is chosen, re-balance with ONE change at a time and re-measure each time. Hand the exports to qa-director for the media check.

## Not verified
Nothing heard, played or watched. Every level, fade and timing is a starting value. Not probed: `Ambience Wind Blowing Through Trees 01.wav` (index only). Not checked by ear: whether `wrench_on_tray_take1.mp3` is a single clink, whether the boots, cloth and fire stand-ins read right, whether any Made take sounds right, whether any file hides a voice or a child. Beat 7 depends on Ian's yes. `2026-11-20-music.md` did not exist yet, so music placement is a lane only. No platform loudness guidance re-read. ElevenLabs credit balance not read, cost not retrieved.
