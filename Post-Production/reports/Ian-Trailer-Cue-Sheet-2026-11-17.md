# Ian trailer cue sheet and first sound pass (2026-11-17)

## Status in one paragraph
ElevenLabs generation was NOT run. This agent session had no ElevenLabs tools (no tool search, no creative_* tools exposed), so usage could not be read and no duration setting could be found. Credits spent in this run: 0. Credits used before: about 650 (Zac's figure, not re-read). The 12 existing takes are untouched. The first sound pass uses the owned Adobe library, the owned music and a few of the existing takes. Nothing was listened to by an agent. Cue timing is from the build script (build_rough.py), not from watching the picture.

## Existing ElevenLabs takes (ffprobe)
| File | Length s | Verdict |
|---|---|---|
| ballroll_take1 / take2 | 2 / 1 | Too short, needs about 6 s. Regenerate |
| handgrab_take1 / take2 | 1 / 2 | take2 used on 9Sa, plausible length |
| creeper_take2 | 3 | Used in 9:16 pass, short of the 5 s asked |
| mustang_starter_take1 / take2 | 2 / 1 | Too short (6 s asked). Library Model A false start used as stand-in |
| v8_idle_take1 / take2 | 3 / 1 | Too short (8 s asked), not used |
| cardoor_take1 / take2 | 1 / 2 | Not used (no coming-home shot in either cut) |
| wrench_on_tray_take1 | 2 | Fine length, not used (no tray shot) |

## Still to generate (for Zac or the next run, with ElevenLabs tools loaded)
Re-run: ball roll (6 s), Mustang starter (6 s), V8 idle (8 s). Never run before: photo rustle, garage room tone, ratchet (skip, library has Industry Ratchet Clicking 01, Turn Single, Turn Short, all used), cello note, piano chord (skip likely: owned music folder has a low-note-free piano bed and beautiful-way-to-end chord, used for the end card). Photo rustle and garage room tone remain needed. Find the duration setting with creative_get_model_schema for eleven_text_to_sound_v2 before spending anything. Space calls out for the free-plan rate limit and poll status, never retry a started call.

## Cue sheet A: Ian-Trailer-Rough-Cut-16x9 (timeline from build script, 37.5 s)
Shots: V2 0-5, V1 5-8.5, R3 still 8.5-12.5, scarred workbench still 12.5-16, V7 16-20.5, 9Sa 20.5-25.5, R1 still 25.5-28.5, black line 28.5-32.5, cover card 32.5-37.5. Levels are pre-mix gain in dB; the whole mix is then normalized.
| Cue | Time s | Description | File | Gain dB | Fade | Notes |
|---|---|---|---|---|---|---|
| A1 | 0 to 37.5 | Garage air bed | Ambience Parking Garage 01.wav (Adobe) | -34 | in 1, out 2 | Continuous, very low |
| A2 | 1.0, 1.9, 2.7 | Ratchet clicks under V2 | Industry Tool Ratchet Turn Single 01 (x2), Turn Short 01 | -18 | none | Stop dead on the arm drop; arm-drop frame not checked, nudge by eye |
| A3 | 3.5 | Ratchet click | Industry Ratchet Clicking 01 | -17 | none | Same note |
| A4 | 6.0, 7.4 | Ball bounce, far, off screen | Sports Baseball Bounce On Cement 01 (lowpass 2.5 kHz) | -26, -29 | none | Second quieter |
| A5 | 9.0 | Wrench handoff on R3 | Industry Tool Wrench Socket Wrench Turning 01 | -18 | none | |
| A6 | 11.2 | Wrench set down | Industry Tool Wrench Set On Pavement 01 | -20 | none | Cleaner tray take still wanted |
| A7 | 12.5 to 16 | Dust and open air | hollow-strong-open-air-wind-looping (owned) | -32 | in 1, out 1 | |
| A8 | 16.2 | Garage door rises on V7 | Household Garage Door Open 01 (first 4.3 s) | -20 | out 1.5 | |
| A9 | 18.0 | Starter that will not catch (stand-in) | Ford Model A False Start Mic In Rear 01 (first 2.8 s) | -24 | in 0.3, out 0.8 | Sounds like a 1930s Ford, replace with real V8 or a regenerated Mustang starter |
| A10 | 21.4 | Hand takes the ball (9Sa) | Made\handgrab_take2.mp3 (ElevenLabs, 2 s) | -16 | none | Not listened |
| A11 | 7.0 to 26.0 | Piano bed, out at the hand-on-ball beat | Music\searching-for-hope_MyqQQIru.mp3 | -21 | in 3, out 3.5 | Silence 0 to 7 per plan |
| A12 | 32.5 to 37.5 | Held chord on end card | Music\beautiful-way-to-end_fJxxL8B_.mp3 (first 5 s) | -19 | in 0.2, out 2 | |
Black line 28.5-32.5 carries only the air bed. No child voice or kid sound anywhere.

## Cue sheet B: Ian-Cover-Story-Animatic-9x16 (15.67 s)
Shots: V7 0-3.5, cover push-in 3.5-5.5, V1 5.5-9.5, old picture 9.5-12.5, cover end card 12.5-15.5.
| Cue | Time s | Description | File | Gain dB | Fade | Notes |
|---|---|---|---|---|---|---|
| B1 | 0 to 15.6 | Air bed | Ambience Parking Garage 01 | -34 | in 0.5, out 1.5 | |
| B2 | 0.2 | Garage door rises | Household Garage Door Open 01 (first 3.5 s) | -18 | out 1 | |
| B3 | 5.7 | Creeper rolls | Made\creeper_take2.mp3 (ElevenLabs, 3 s) | -20 | out 0.3 | Not listened |
| B4 | 8.8 to 12.8 | Memory music on the old picture | Music\blurred-memories_GJRG9HNu.mp3 | -21 | in 1.5, out 1.5 | Past archive material, no fence issue |
| B5 | 10.0 | Soft keys and cloth | Impact Cloth Hit Pocket With Keys 03 | -24 | none | Optional, drop if it reads as a coming-home cue |
| B6 | 12.5 to 15.7 | Held chord on end card | beautiful-way-to-end (first 3.2 s) | -19 | in 0.2, out 1.5 | |

## Loudness
Target is a PROPOSAL, platform guidance not re-checked this run: about -16 LUFS integrated, true peak at or below -1.5 dBTP for the pass (ceiling -1 dBTP). Mix used one-pass ffmpeg loudnorm (I=-16, TP=-1.5, LRA=11), then re-measured with the same filter (input values):
| File | Integrated LUFS | True peak dBTP | LRA |
|---|---|---|---|
| Ian-Trailer-Rough-Cut-16x9-v2-sound.mp4 | -15.49 | -0.95 | 16.2 |
| Ian-Cover-Story-Animatic-9x16-v2-sound.mp4 | -14.70 | -1.47 | 6.8 |
The 16:9 true peak (-0.95) is just over the -1 ceiling, and its LRA is wide because of the silent open. Fix in the real mix: add a limiter at -1.5 dBTP or lower the chord by 2 dB. Left as is for the rough pass.

## Mix notes
Dialogue: none in either cut. Music enters at 7 s in the 16:9 and leaves before the hand-on-ball beat so the grab is heard. SFX hits are placed on cut points from the script timeline, not checked against frames. Air bed sits under everything at about -34 dB. If the ball bounce reads too clear, drop it 4 dB.

## Files
Video: P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut\Ian-Trailer-Rough-Cut-16x9-v2-sound.mp4 and Ian-Cover-Story-Animatic-9x16-v2-sound.mp4 (v1 untouched, video stream copied, audio AAC 192k 48 kHz). Build script: D:\WKP\scratch\ian\sound\mux.py. Video lasts 38.125 s vs audio 37.5 s on the 16:9 (audio ends 0.6 s early).
