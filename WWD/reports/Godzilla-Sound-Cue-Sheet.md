# Godzilla Minus Zero: Sound Pack and Cue Sheet

**Built 2026-11-07 by wwd-vfx.** Owned sounds only, nothing downloaded, nothing spent. No music (Zac picked it). All files are copies in `P:\WWD Kit\Godzilla\Sounds\` (originals untouched in `P:\Sounds\Sound FX\`). Builder script: `D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\make_godzilla_sound_pack.py`.

**I cannot hear audio.** File choices come from the file names, ffprobe durations, and measured loudness and peak positions (ffmpeg volumedetect and an envelope scan). Levels are starting points, set them by ear in Premiere.

## Read first: timecodes

- Timecodes below are the **cut's own** timecodes from `Godzilla Minus Zero -  Review - All Hail the King!.txt` (ends 00:28:28:29).
- The video file in the folder (`...All Hail the King!.mp4`, 46:16.1) is NOT that cut. It is the raw recording: frames show a 30-second countdown and the FrostCast countdown logo at the start, then the two-cam layout, and the speech runs on past 28:29. I did not use it for timing.
- Where a line sits inside a long transcript block, I estimated the second from word count and mark it **(est)**. Accuracy about plus or minus 3 seconds. Scrub to the spoken word.
- The cut has no gap for a logo sting (hook block 00:00:00 to 00:00:22:03, next line 00:00:22:09). If Zac ripple-inserts the 6 to 8 s sting, add its length to every later time. If it overlays on V2, no change.
- Spoiler Alert (`P:\WWD Kit\Crystal Lake\Spoiler Alert.mov`, 3.2 s) and Recommend Watch (`P:\WWD Kit\Stickers\Recommend Watch.mov`, 4.0 s) both have sound baked in (ffprobe shows an audio stream). No extra sound for those.

---

## Part A: Logo sting sounds (foot squashes the Winter Wolf logo)

Companion to `Godzilla-Logo-Squash-Firefly-Prompt.md`. All times are relative to **T**, the frame where the foot touches the badge. Scrub the Firefly clip, mark T, place everything from it. With an 8 s clip T is probably near 4 s. With 6 s, drop the first step.

All files are in `P:\WWD Kit\Godzilla\Sounds\`.

### A1. Rumble bed
- T-4.3 to T+2.5, fade in over 2 s, fade out over the last 1.5 s, about -24 dB rising to -18 dB.
- `ST2 stomp layer 3 sub rumble (use first 4 s) - Drone Production Element Imaging Deep Subsonic Rumble Bass 02.wav` (60.06 s, trim to about 7 s). Mean -15.5, max -1.0.

### A2. Giant footsteps, a few approaching
- Use `ST1b three approaching steps (cut 0.75 to 3.35 s of huge-monster-steps-looping).wav` (2.60 s, derived by me from the loop with 30 ms fade in and 0.3 s fade out). Steps land at about 0.20, 1.05 and 1.95 s inside the clip (scanned peaks).
- Place the clip so it starts at T-2.9. The steps then land at T-2.7, T-1.85, T-0.95. The next step would land at T, which is the stomp, so the rhythm holds.
- Volume ramp: -26 dB, -20 dB, -14 dB (each step louder as it nears).
- Source loop if more steps are wanted: `ST1 steps loop - huge-monster-steps-looping_z1N35r4d.mp3` (8.88 s, strong steps near 0.95, 1.8, 2.7, 3.65, 4.5, 5.35, 6.25 s). Mean -9.0, loud, so pull it down.

### A3. The stomp (layer all five at T)
- `ST2 stomp layer 2 blast impact - Production Element Title Transition Blast Impact 01.wav` (2.02 s) at T, -6 dB. Sharp front edge.
- `ST2 stomp layer 1 blast debris - Explosion Blast Debris Large 01.wav` (7.25 s, main boom at 0.15 s) start at T-0.15, -8 dB.
- `ST2 stomp layer 4 dark thud - hit-thud-dark_GkAfpDV_.mp3` (4.00 s, peak at 0.05 s) at T, -8 dB.
- `ST2 stomp layer 5 concrete drop - Impact Concrete Drop On Concrete Single 02.wav` (1.16 s, quiet, mean -31.9) at T, +6 dB gain, then -10 dB.
- The sub rumble from A1 swells under it: raise it to -12 dB from T to T+1.5.
- Optional: high-pass the debris layer at 80 Hz if it muddies the thud.

### A4. Cracking and breaking
- `ST4 crack 1 brick building - Crash Brick Building 01.wav` (3.33 s, hits at 0.15 and 1.1 s): start at T-0.10, -12 dB. This is the main break, the second hit at T+1.0 reads as the ground splitting further.
- `ST4 crack 4 concrete smash - Crash Concrete Smashing Through Wood Debris On Pavement Short 01.wav` (2.35 s, quiet, mean -29.3) at T+0.05, +6 dB gain, then -12 dB.
- `ST4 crack 2 rock drop - Crash Rock Drop On Wood Debris 01.wav` (0.78 s) at T+0.35, -14 dB, for debris chunks.
- `ST4 crack 3 glass crack (thin) - Crash Glass Crack 03.wav` (1.16 s, mean -34.1, very thin) at T+0.15, -20 dB. Only a sharp "tick" layer.

### A5. Squash and crunch (foot grinding the badge flat, T to T+1.2)
- `ST5 squash 1 car crushing - Crash Car Crushing 01.wav` (7.05 s, crunches near 0.8 and 1.2 s): start at T-0.5 so the crunches fall at T+0.3 and T+0.7, -12 dB. Trim to 2 s and fade.
- `ST5 squash 2 crane crush - Crash Crane Crush Car 01.wav` (5.41 s, long groan): start at T+0.2, -18 dB, pitch down 20 percent.
- `ST5 squash 3 tin crush rubble - Foley Tin Crush Rubble 01.wav` (2.42 s, quiet) at T+0.6, +6 gain then -14 dB.
- `ST5 squash 4 glass crunch - Crash Glass Crunching On Pavement 01.wav` (1.39 s) at T+0.9, -18 dB.
- `ST5 squash 5 body stomp - Horror Body Stomp 03.wav` (1.45 s) at T, -14 dB, the soft "meat" under the impact. Skip it if it sounds like a body.

### A6. Roar (as the foot lifts away, T+1.1)
- Main: `ST3 roar main dragon roars - wild-beast-roars-dragon_zJy_cB4u.mp3` (9.14 s). Roar peaks at about 0.7 s, then a bigger run from 6.4 to 7.7 s. Cut source 6.2 s to 9.14 s, place at T+1.1, -10 dB. Pitch down 20 percent.
- Layer: `ST3 roar layer grizzly (pitch down) - Animal Mammal Carnivore Grizzly Bear Roar 02.wav` (1.37 s) at T+1.15, pitch down 40 percent, -14 dB.
- Layer: `ST3 roar layer dragon growl - Horror Dragon Growl 01.wav` (7.80 s) from 0.5 s, at T+1.1, -16 dB, low-pass at 3 kHz for chest.
- Optional top: `ST3 roar layer beast screech - Horror Beast Screech 01.wav` (3.94 s, peaks 1.9 s) at T+1.2, -20 dB, high-passed, pitch down 15 percent.
- Optional: `ST3 roar layer tiger (pitch down) - Animal Mammal Carnivore Cat Tiger Roar 01.wav` (1.21 s).
- Keep the roar about 4 dB under the stomp. It is the second beat.

### A7. Dust settling and clean hold
- `ST6 settle debris tail - Explosion Building Demolition Debris 02.wav` (13.55 s, hit at 0.25 s then a long tail). Start it so the hit is gone: cut source from 1.0 s, place at T+0.3, -20 dB fading to nothing by the end of the clip. Last second of the sting nearly silent for the title.

### A8. Sting verdicts (honest)
- Footsteps: GOOD. `huge-monster-steps-looping` is a real giant-step loop.
- Stomp: GOOD as a layered build. No single owned giant-foot hit with ground shake exists, the five layers make one.
- Roar: PARTIAL. Dragon roars and big cat roars layered and pitched down. Nothing owned is a kaiju roar, and I avoided trying to match any film's signature roar.
- Cracking: PARTIAL. Brick building collapse and concrete smash carry it. No owned long ground-splitting crack. The glass crack is too thin to lead.
- Squash and crunch: GOOD. Car crushing and crane crush are close to a heavy metal and concrete crunch.

### A9. MISSING for the sting (ready-to-paste generation prompts)

Zac has two free-trial AI tools that can generate. Use text-to-sound-effect mode, do not spend credits on paid tiers. I have no generation tool and none of these prompts has been tested.

1. **Kaiju roar** (the biggest gap). Prompt: `Colossal reptilian monster roar, deep guttural bellow rising into a long metallic shriek, huge chest resonance, echoing across a city at night, no music, no voices, no background.` Length 6 to 8 seconds. Make 2 to 3 takes. Layering: put the generated roar on top, and tuck the owned dragon roar under it at -10 dB for chest weight. Pitch down 10 percent if it sounds small.
2. **Ground cracking and splitting under heavy weight.** Prompt: `Thick concrete and asphalt cracking and splitting under crushing weight, deep fracture, rumble, then small chunks falling and skittering, no music, no voices.` Length 3 to 4 seconds. Layering: lay it over the brick building break from A4 at T.
3. **Single giant foot stomp with ground shake (optional upgrade).** Prompt: `One enormous heavy footstep landing on pavement, huge low-frequency boom, ground shake, debris falling after, no music.` Length 3 seconds. Replaces layers 2 and 4 in A3 if it sounds better, keep the sub rumble.

---

## Part B: Whole-video cue list (timeline order)

Baseline: **no music under the talk, no ambience bed under the conversation.** Cues are short, on the hosts' own jokes or on the creature talk. Heavy human scenes stay dry. File names begin with the prefix shown in `P:\WWD Kit\Godzilla\Sounds\`.

Levels are relative to the hosts' voices at normal level. Voices stay on top.

**00:00:00 (start of hook) | "Toho just brought the King of Monsters home to Japan..."**
- Distant roar, far away. `ST3 roar main dragon roars - wild-beast-roars-dragon_zJy_cB4u.mp3`, use the first roar (source 0.5 to 2.5 s), low-pass at 1.5 kHz, -28 dB, fade out under the voice. Optional.

**00:00:13 to 00:00:15 (est) | "Let's find out now."**
- Logo sting goes here if Zac wants it at the natural beat. Part A sounds. Zac decides placement.

**00:00:16 (est) | "Another day, another Japanese city destroyed, King."**
- `VD distant bomb - Explosion Distant Bomb 01.wav` (4.53 s), -24 dB, start on "destroyed". Add `VD city sirens - city-street-sirens-2_fyW5nW4u.mp3` (3.14 s) at -30 dB under it.

**00:04:41 | Spoiler Alert ("we are going to show you a spoiler alert right now," 00:04:40:06 to 00:04:45:29)**
- Drop `P:\WWD Kit\Crystal Lake\Spoiler Alert.mov` starting on "spoiler". Sound baked in, nothing to add. The next line after the countdown starts 00:04:46:03.

**00:05:58 (est) | "Big Green ... with the electrical shit"**
- `VD electric sizzle - electric-sizzle_zyuNWG4u.mp3` (3.71 s, very quiet, mean -30.5), +6 gain, -20 dB. Optional.

**00:06:08 (est) | "And he comes up out of the water" (block 00:05:56:29 to 00:06:15:27)**
- `VD water surge - Liquid Water Water Splash Wave 11.wav` (4.78 s, surge peaks at 0.6 s, quiet, mean -30.5), +8 gain, -16 dB. Layer a low roar: source 0.5 to 2.5 s of `ST3 roar layer dragon growl - Horror Dragon Growl 01.wav` at -22 dB.

**00:07:10 (est) | "the fighter pilots out there" (block 00:06:48:01 to 00:07:14:03)**
- `VD plane flyby - Transportation Plane Flyby 04.wav` (16.19 s, engine pass builds to a peak near 8.5 s). Use source 4 to 11 s, fade in and out, -22 dB. Optional.

**00:10:08 to 00:11:00 | Hiroshima and medical clinic flashback talk, "gut churning"**
- NO cue. Leave dry. Heavy human scene, no gags.

**00:14:20 (est) | "hot on the tails and shooting them down" (block 00:14:05:09 to 00:14:30:01)**
- `VD wwii machine gun - gun-machine-gun-automatic-303-caliber-vickers-burst-close-perspective_Myp7JqE_.mp3` (3.08 s, four bursts), -20 dB, one burst only, then plane flyby from 00:07:10 again, source 4 to 8 s, -26 dB.

**00:18:09 (est) | "Godzilla powers up the ray, Doctor Noda is like, too soon, junior" (block 00:18:05:12 to 00:18:28:06)**
- `VD heat ray charge - Science Fiction Sci-Fi Electronic Energy Pulse Low 01.wav` (5.04 s, pulses loud from 0.45 s), start on "powers up", -22 dB, fade by "too soon".

**00:18:55 (est) | "chanting for Van Damme at the end of Kickboxer ... Super Saiyan moment" (block 00:18:46:25 to 00:19:05:16)**
- `VD crowd cheer - crowd-cheers-and-whistles_MyWbxfVu.mp3` (3.27 s), -24 dB, on "chanting". Optional, a joke cue.

**00:20:30 (est) | "stomp in the city" (block 00:20:12:22 to 00:20:32:27, last words)**
- One giant step, from `ST1 steps loop - huge-monster-steps-looping_z1N35r4d.mp3`, source 0.6 to 1.8 s (step lands near 0.95 s), -18 dB, plus one quick growl from the roar at -26 dB. Joke cue.

**00:20:36:11 to 00:20:39:12 | "Where's the money coming from? I don't know."**
- `VD crickets - Ambience Night Crickets And A Bullfrog 01.wav` (90.11 s, use 2 to 3 s), -22 dB, fades out on Zac's "Hey, it's creating jobs, though." (00:20:36:11 start of his line).
- A rimshot would fit "creating jobs." See MISSING in Part C.

**00:21:00 to 00:21:20 | "a couple of jackasses talking behind us for a solid two hours" (block 00:20:55:16 to 00:21:20:05)**
- `VD crowd chatter bed - ab-f-031616-38698401_crowd-chatter-ambience-01.mp3` (60.09 s, very low, mean -32.5), use 20 s, fade in and out, -30 dB. Optional.

**00:22:34 (est) | "Godzilla just straight up rips his head off" (block 00:22:32:07 to 00:22:36:17)**
- `VD wet rip - Horror Scary Skin Rip Wet 01.wav` (0.81 s, very quiet, mean -35.2), +14 gain, -16 dB. Keep it brief. Gory but the hosts are laughing, matches the tone. Optional, drop if it feels like too much.

**00:22:40 (est) | "he cut it off with his tail and then it bit his arm" (block 00:22:36:19 to 00:22:41:10)**
- `VD bone crunch - Horror Scary Bone Crunch 01.wav` (3.39 s, very quiet, mean -35.7), use first 0.8 s, +14 gain, -18 dB. Optional.

**00:22:46 (est) | "rips his own arm off, get back in the fight" (block 00:22:44:27 to 00:22:52:00 includes the next line)**
- `VD bone tear - Horror Scary Bone Tear Wet 02.wav` (3.34 s, quiet, mean -37.2), use first 1 s, +14 gain, -18 dB. Optional.

**00:22:50 (est) | "pimp smack him with it"**
- `VD smack - punch-face-hard_f1oeQhNO.mp3` (0.58 s), -14 dB. Joke cue.

**00:23:14 (est) | "you just hear them in the background fighting" (block 00:23:06:03 to 00:23:24:23)**
- `VD distant boom - Explosion Distant 01.wav` (1.99 s), -28 dB, plus the roar growl at -32 dB. Sounds "off screen". Optional.

**00:24:27 | "gravity beams" (block 00:24:25:03 to 00:24:25:01 Zac "Beam thing"; Matt "Do gravity beams sick dude" at 00:24:25:03)**
- `VD gravity or ray beam - Science Fiction Sci-Fi Electronic Distorted Energy Beam 242.wav` (2.81 s, hits at 0.35 s), -22 dB.

**00:24:31 (est) | "buried Godzilla with rubble" (block 00:24:25:03 to 00:24:35:15)**
- `VD rubble crash - Explosion Building Demolition Debris 01.wav` (10.27 s, hit at 0.2 s, long tail), -18 dB, cut the tail to 3 s with a fade.

**00:24:43 (est) | "kicked his feet up like the cat or dog does" (block 00:24:40:07 to 00:24:52:22; Zac's line 00:24:35:17 to 00:24:40:05 is the earlier one)**
- `VD dirt dig - Foley Grass And Mud Dig With Hands Short 01.wav` (2.94 s), -20 dB. Joke cue.

**00:25:16 to 00:26:00 | Professor Noda sacrifice, "the gut punch of the movie"**
- Dry. Optional barely audible `VD heartbeat slow - heartbeat-slow_M1Vtl3VO.mp3` (61.01 s) from 00:25:50 to 00:26:00 (est), -34 dB, fade in and out. Taste call, skip if Zac wants silence. No jokes here.

**00:26:06:29 | "Yeah. Shoot." then "Newsflash. Should have been your first plan." (00:26:07:15)**
- `VD missile whoosh - Weapon Missile 01.wav` (0.86 s), -16 dB, at 00:26:06:29 on "Shoot".
- `VD record scratch - record-scratch_zkkU_2VO.mp3` (0.63 s), -18 dB, at 00:26:07:15 on "Newsflash". Joke cue.

**00:26:24 (est) | "I have to give it four" (Zac's rating, block 00:26:18:00 to 00:26:39:21)**
- `VD rating hit - Production Element Title Transition Blast Impact 02.wav` (1.65 s), -14 dB, on "four". No score text added on screen by this kit.

**00:26:50 (est) | "three and a half giant kaiju footprints out of five" (block 00:26:40:13 to 00:26:58:01)**
- Three stomps then a smaller half stomp. Use `ST1b three approaching steps (cut 0.75 to 3.35 s of huge-monster-steps-looping).wav` (steps at 0.20, 1.05, 1.95 s in the clip), -18 dB, lined up so they land on "three and a half giant kaiju footprints". Add a fourth, smaller step: the first step of the clip again, -26 dB, high-passed at 300 Hz (a "half" stomp). Gag cue.

**00:27:23 (est) | "That's a hearty endorsement from both of us" (block 00:27:18:22 to 00:27:35:27)**
- Optional sticker `P:\WWD Kit\Stickers\Recommend Watch.mov`. Sound baked in. Zac decides, it is only used where a host says it.

**00:27:33 (est) | "Mechagodzilla coming your way"**
- `VD mecha whirr - monster-whirr_zk8RqSV_.mp3` (5.98 s), source 0.5 to 3 s, -22 dB, plus `VD mecha metal hit - hit-metal-hard_M1WQr3Eu.mp3` (3.92 s) at the word "Mechagodzilla", -18 dB. Stand-in until a real mech sound exists. Joke cue.

**00:27:46 to 00:27:52 | Post-credits audio gag: "bigger footsteps and a giant, like, giant roar" (Zac, 00:27:45:22 to 00:27:51:23)**
- Best cue in the video, it is the hosts' own description.
- Footsteps: `ST1 steps loop - huge-monster-steps-looping_z1N35r4d.mp3` (8.88 s), start at 00:27:46:00 and run to 00:27:50:00, ramp from -30 dB to -16 dB, ending on the word "roar".
- Roar: `ST3 roar main dragon roars - wild-beast-roars-dragon_zJy_cB4u.mp3`, source 6.2 to 9.14 s, on "giant roar" (about 00:27:49:20, est), -12 dB, pitch down 15 percent, fade under Matt's "It's that Ultrasaurus" at 00:27:51:25.

**00:28:16 | "Mechagodzilla coming your way, dude" (00:28:16:03)**
- Repeat the Mechagodzilla cue, quieter: whirr -26 dB and one metal hit -22 dB. Optional.

**00:28:23 to 00:28:28 | "Give the people a bye people", "cut this out", "No, leave that in"**
- NO cue. Raw banter as recorded, no bleeping. Zac's outro music takes it.

### Tone check
- Heavy-human segments left dry: 00:10:08 to 00:11:00 (Hiroshima), 00:25:16 to 00:26:05 (Noda).
- Joke cues sit on lines the hosts say as jokes: 00:20:30, 00:20:36, 00:22:50, 00:24:43, 00:26:07, 00:26:50, 00:27:33.
- Gore-sound cues at 00:22:34 to 00:22:46 are on creature talk the hosts laugh at. All three are optional.

---

## Part C: Whole-video MISSING list

1. **A kaiju roar** (the Part A gap, also used at 00:00, 00:06:08, 00:20:30, 00:27:49). Stand-in is the owned dragon roar layered with big cat roars. Generation prompt is in A9.
2. **A rimshot or "ba-dum-tss" for "Hey, it's creating jobs, though" (00:20:39).** The only rimshot in the library is `YTDown.com_YouTube_Comic-Rimshot_Media_9CdVTCDdEwI_001_360p.mp4`. It is a YouTube download with no license note, so I did not use it. Options: skip it, or generate. Prompt: `Classic comedy rimshot, snare roll then cymbal crash, dry, no room, 2 seconds.` Length 2 s.
3. **A Mechagodzilla sound (servo whine plus metal roar), 00:27:33 and 00:28:16.** Stand-in is `monster-whirr` plus `hit-metal-hard`. Prompt: `Giant robot monster roar, metal grinding scream with servo whine and hydraulic hiss, huge and mechanical, no music, no voices.` Length 4 to 5 s.
4. **A dedicated ground crack and a single giant foot hit.** Prompts in A9. The video's one-off stomp at 00:20:30 uses the step loop and works without them.
5. **Real ambience under the whole video.** Not needed, none was asked for, talk stays clean.

Nothing else is missing. Atomic ray and gravity beam are covered by owned sci-fi energy files, plane and WWII machine gun by owned files, wet gore by owned Horror files.

---

## File list (exact paths, real durations from ffprobe)

Folder: `P:\WWD Kit\Godzilla\`

- `Godzilla Logo - Black Start Frame.png` (1920x1080 RGB)
- `Sounds\` holds 47 files. Start with the files named in this sheet. Durations:
  - ST1 steps loop 8.88 s, ST1b three approaching steps 2.60 s
  - ST2 blast debris 7.25 s, blast impact 2.02 s, sub rumble 60.06 s (use about 7 s), dark thud 4.00 s, concrete drop 1.16 s
  - ST3 dragon roars 9.14 s, dragon growl 7.80 s, grizzly roar 1.37 s, tiger roar 1.21 s, beast screech 3.94 s
  - ST4 brick building 3.33 s, rock drop 0.78 s, glass crack 1.16 s, concrete smash 2.35 s
  - ST5 car crushing 7.05 s, crane crush 5.41 s, tin crush rubble 2.42 s, glass crunch 1.39 s, body stomp 1.45 s
  - ST6 debris tail 13.55 s
  - VD (video): distant bomb 4.53 s, distant boom 1.99 s, city sirens 3.14 s, water surge 4.78 s, electric sizzle 3.71 s, plane flyby 16.19 s, WWII machine gun 3.08 s, heat ray charge 5.04 s, ray beam 2.81 s, crowd cheer 3.27 s, crickets 90.11 s, crowd chatter 60.09 s, wet rip 0.81 s, bone crunch 3.39 s, bone tear 3.34 s, smack 0.58 s, rubble crash 10.27 s, dirt dig 2.94 s, heartbeat 61.01 s, missile whoosh 0.86 s, record scratch 0.63 s, rating hit 1.65 s, mecha whirr 5.98 s, mecha metal hit 3.92 s, gong (optional, unused above) 5.09 s

Originals: `P:\Sounds\Sound FX\` (loose mp3s and `Adobe\` subfolders, paths as in the file names).

## Not verified

- Nothing was heard. Levels and trims come from file names, durations and measured loudness and peak positions.
- Timecodes marked est come from word counts inside long transcript blocks.
- The squash start frame and every Firefly prompt are untested (credits).
