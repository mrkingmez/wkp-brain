# WWD Director Log

Format: ## YYYY-MM-DD HH:MM | TYPE | subject | elapsed

Log archived at 549 lines on 2026-09-24 per the 500-line rule. Prior
entries (2026-08-20 through 2026-09-12) now live in
`logs\wwd-director-2026-Q3.md`.

### 2026-09-24 11:03 - EP113 transcription, chapters, and audio cut
**Status:** BLOCKED (Messenger send to Matt could not run - tool unavailable this session; all other steps DONE)
**Trigger:** "Zac just said the new FrostCast episode is downloaded" - run the full FrostCast Transcription Workflow end to end.
**Classification:** FrostCast (no transcript existed yet - raw video only).
**Elapsed:** ~35-40 min (audio extract + GPU transcription ~22 min, transcript read + chapters + audio cut build the rest).

**Actions taken:**
- Located the episode via the WWD calendar convention, not by asking: `L:\Winter Wolfs Den review show\Frost-Cast\EP 113\` (EP112 was transcribed 9/16, EP113 was next scheduled 9/23, file on disk dropped 9/24) - confirmed EP113, "Does anyone care about the Avengers Encore?", 2.59 GB, 74:34 raw runtime.
- Extracted mono 16kHz WAV via `extract_audio.sh` to `D:\WKP\scratch\EP113.wav`.
- Confirmed `voiceprints\` still doesn't exist on this machine (matches standing TASKS.md/memory gap - never enrolled). Ran `transcribe.py` anyway per established precedent (EP106/EP110/EP111/EP112 all shipped this way) - launched detached on GPU (RTX 5060), HF_TOKEN resolved fine despite a casing mismatch in the shell env (`HF_Token` vs `HF_TOKEN` - Windows env vars are case-insensitive, Python confirmed it resolves).
- Transcription completed clean, exit code 0, 2.8 min diarization stage, 3 speaker clusters, all UNMAPPED (Guest/Unknown [1]/[2]/[3] - expected, voiceprints not enrolled). Full 1,355-line, 74:21-runtime transcript written to `L:\Winter Wolfs Den review show\Frost-Cast\EP 113\Does anyone care about the Avengers Encore_ _ FrostCast Episode 113 (1)_transcript.txt`.
- Read the full transcript end to end (not skimmed). Note for context, not flagged as a problem: Zac/KingZ was out sick this episode - Matt/Winter Wolf hosted solo with Gabby/Oracle filling in; King is referenced throughout but never speaks on mic.
- Built the chapter list by hand per `wwd-frostcast-chapters` rules (subject-change boundaries, chronological not thematic, HH:MM:SS, starts 00:00:00 - Start): 14 entries covering MCU fandom talk, the Doomsday/Endgame Encore debate, Resident Evil (the episode's main review block), Transformers' 40th anniversary tribute, the animation-quality tangent, and King's 48-Hour Film Festival win. Full list below.
- Built the audio cut document per `wwd-audio-cut` (chronological alternating Start/Cut list, cold open pulled from inside the episode, hard rule against cutting mid-thought or breaking continuity respected). Identified 7 clean, self-contained cuts (chat-reading asides, a mispronunciation bit, a repeated audience check-in, one technical aside) totaling 1:28. Finished runtime lands at ~1:12:53 - **above the 55-70 min target**, flagged plainly in the doc rather than force-cutting real commentary, since this episode runs dense and on-topic almost wall to wall with no single large freeform tangent to remove (same call made on EP110's audio cut).

**Chapters (14, embed-ready):**
```
00:00:00 - Start
00:03:28 - MCU Fandom Check: Loki, Hawkeye, Ms. Marvel
00:08:57 - Doomsday Homework and Endgame Encore Debate
00:14:36 - Favorite Rewatch Scenes: Two Towers and More
00:17:46 - Doomsday Presales and Weekend Box Office
00:23:49 - Resident Evil: First Impressions
00:33:34 - Resident Evil: Tone, Comedy, and Horror Balance
00:39:14 - Resident Evil Box Office and Cregger's Exit
00:44:51 - Cregger's Filmography: Barbarian and Weapons
00:49:39 - The Burroughs and Spielberg's Next Project
00:51:26 - Transformers 40th and the Peter Cullen Tribute
00:58:00 - Why Animation Got Worse: CGI Shortcuts
01:03:00 - King's 48 Hour Film Festival Win
01:13:07 - Wrap-Up and a Heat Editing Tease
```

**Deliverables:**
- Transcript: `L:\Winter Wolfs Den review show\Frost-Cast\EP 113\Does anyone care about the Avengers Encore_ _ FrostCast Episode 113 (1)_transcript.txt`
- Chapters: listed above, not yet saved as a standalone file (no upload package was requested this run - only the standing transcription workflow) - ready to hand to `wwd-video-upload-package` when that runs.
- Audio cut: `L:\Winter Wolfs Den review show\Audio\podcast Frostcast audio files\FrostCast ep 113 2026-09-24.md`

**Flags for Zac:**
- **Messenger send to Matt did NOT run.** This session's toolset has no `claude-in-chrome`/browser-automation access (confirmed - not in the available tool list, not listed under this session's MCP servers), so steps 6b-6e (navigate to Messenger, attach the transcript file, send, screenshot-confirm) could not be attempted. Nothing was faked - the transcript itself is real and saved at the path above, ready to attach the moment a session with browser access picks this up. Per root CLAUDE.md: "If Chrome/the claude-in-chrome extension isn't available... flag it back to Zac rather than silently skipping the transcript delivery." Re-run this step from a Claude Code/Cowork session that has `claude-in-chrome` loaded.
- Speakers came back Guest/Unknown [1]/[2]/[3] - same standing gap as every prior episode (voiceprints never enrolled). Zac was Guest/Unknown [1] in the small handful of lines where a second/fourth cluster briefly speaks; Matt is the dominant Guest/Unknown [1] cluster throughout, Gabby is Guest/Unknown [3].
- Audio cut finished runtime (~1:12:53) is above the 55-70 min target - see the flag inside the cut doc itself for why (dense, on-topic episode, no large removable tangent this week).
- No upload package or shorts were run this session - the standing transcription workflow (transcript + chapters + audio cut + Messenger send) is what was asked for. Say the word if Zac wants the full `wwd-video-upload-package`/shorts chain run next.

## 2026-10-06 - Heat (1995) First Watch upload pipeline
Ran wwd-review-pipeline. Package (.md/.docx), AUDIO mp3 (35:25, matches source), 6 Shorts (1 ready, 5 held) in L:\Winter Wolfs Den review show\Raw Footage\Heat\. Speaker map reversed vs skill default (S1=KingZ, S2=Winter Wolf). Flags in package Section 12.

### 2026-10-11 - Other Mommy (2026) review intake
**Status:** DONE (photo stage); transcript stage pending
**Trigger:** "we are doing a review on Other Mommy", recording tonight, release Tue 10/13
**Classification:** Review (intake)
**Actions taken:** TMDb 1400837 confirmed. Calendar: added "Other Mommy - Record Review" (Sun 10/11 7-9 PM ET) and "Other Mommy - Review Release" (Tue 10/13 all-day) to Winter Wolf's Den calendar. Pulled 17 backdrops + 6 poster candidates, filtered to 15 (1 poster, 13 stills, 1 promo portrait), resized to 1920x1080 RGBA PNG in USE\, verified, deleted originals. Skill, director routing, and Premiere transition reference updated.
**Deliverables:** L:\Winter Wolfs Den review show\Raw Footage\Other Mommy (2026)\USE\ (15 PNGs); source list D:\WKP\scratch\other-mommy_urls.txt
**Flags for Zac:** Set is 15 not 18 (brand-new release, IMDb has no extra stills). Placement report waits on the edited transcript.

### 2026-10-12 - Carrie (2026 series) review intake
**Status:** DONE (intake). Step 8 pending transcript.
**Trigger:** "today we are doing a review video on Carrie series, recording today release thursday"
**Classification:** Review (intake)
**Actions taken:** Title resolved to TMDb tv/288673 (Prime Video, premiered 2026-10-07). Calendar entries added on thewinterwolfsden@gmail.com: Record Review Mon 10/12 7 to 9 PM ET (time assumed from usual pattern), all-day Review Release Thu 10/15. Pulled 33 backdrops + 19 posters, curated to 1 poster + 17 stills, resized to 1920x1080 RGBA PNG in USE (verified, transparent padding), originals deleted.
**Deliverables:** L:\Winter Wolfs Den review show\Raw Footage\Carrie (2026 series)\USE\1-18.png ; source list D:\WKP\scratch\carrie_urls.txt
**Flags for Zac:** record time assumed; awaiting edited transcript for placement report.

### 2026-10-21 - FrostCast EP117 show prep
**Status:** DONE (all 9; topics 1, 5, 8 built from best-guess readings, marked READ AS)
**Trigger:** Run wwd-show-prep on Matt's EP117 list, topics 2, 3, 4, 6, 7, 9
**Classification:** Other (show prep, single skill)
**Actions taken:** Read list image; 3 research desks via general-purpose agents (Doomsday/Narnia, Clayface/DC villains, anthology/Crawlers). Crawlers verified as a real 2026 film (Oct 16, Roadside/Saban). Docx built from md.
**Deliverables:** D:\WKP Reports\FrostCast\2026-10-21 - FrostCast EP117 Show Prep.docx and Part 2; md at D:\WKP\WWD\reports\FrostCast-EP117-Show-Prep.md and -Part-2.md
**Flags for Zac:** Topics 1 (read as Wonder Woman/Arjona), 5 (Alcock Instagram deletions plus Gunn Threads reply; no Gunn Instagram post found), 8 (assumed Narnia) are guesses, Zac to confirm. Check Clayface critic aggregate before recording (opens Oct 23). Many trade originals paywalled, items marked via. Joker 2019 gross, Narnia and Doomsday budgets unverified. Devils-advocate review not run (time).
**Docx note:** original EP117 docx files were open in Word (locked), so the all-9-topics versions were saved as '... v2.docx' beside them.

### 2026-10-25 - wwd-vfx bench agent created
**Status:** DONE
**Trigger:** Zac via Jarvis: new bench agent wwd-vfx to own the WWD edit kit
**Classification:** Other (agent setup)
**Actions taken:** wrote .claude/agents/wwd-vfx.md; added routing paragraph to wwd-director.md; added bench line to AGENT-NETWORK.md; added TASKS.md row
**Deliverables:** D:\WKP\.claude\agents\wwd-vfx.md
**Flags for Zac:** agent loads at next session start; not committed or pushed

### 2026-10-25 21:37 - wwd-vfx toolkit inventory and creative charter
**Status:** DONE
**Trigger:** Zac via Jarvis: wwd-vfx must know every VFX tool and toolset (Order 1), and be creative, not copy others (Order 2)
**Classification:** Other (agent setup)
**Elapsed:** about 12 minutes
**Actions taken:** tasked wwd-vfx (Agent tool, bench was loaded) to build the verified inventory; spot-checked it (Adobe install folders, no Saber file, no em dashes); added "Creative charter" section and a toolkit read-first line to wwd-vfx.md
**Deliverables:** D:\WKP\.claude\agents\wwd-vfx-toolkit.md; D:\WKP\.claude\agents\wwd-vfx.md (edited)
**Flags for Zac:** Saber and Optical Flares/Trapcode not installed; ~35 alpha .mov kit pieces have no MP4 twin (ProRes freezes on his machine), needs a format decision; Remotion runtime not installed; connectors are main-session-only. Not committed or pushed. Devils-advocate review not run (reference file, not a shipped deliverable).

### 2026-10-25 - [wwd-director, doing wwd-color first job] wwd-color bench created, LUT scripts and Clayface looks
**Status:** DONE
**Trigger:** Zac via Jarvis: create wwd-color bench, then first job (two scripts, Clayface safe and bold LUTs)
**Actions taken:** wrote wwd-color.md and _spec\wwd-color-reference.md; routing added to wwd-director.md, AGENT-NETWORK.md, wwd-vfx.md; TASKS.md row added. wwd-color not loadable this session, so director ran the first job. make_look_lut.py and match_shots_lut.py built and tested on real Clayface trailer and host webcam frames (cube order verified against ffmpeg lut3d). WebSearch was not available to me, so no web color research was done.
**Deliverables:** P:\WWD Kit\Color\ (Clayface Safe, Clayface Bold, Match WinterWolf cam to KingZ cam, all 2026-10-25); D:\WKP Reports\Color LUT How-To\2026-10-25 - Color LUT How-To.docx; strips in D:\WKP\scratch\color\
**Flags for Zac:** check skin tones on your own screen; look research needs a session with web search; devils-advocate review not run

### 2026-10-25 - wwd-color sandbox test
**Status:** QUEUED
**Trigger:** Zac (via Jarvis): wwd-color must not be tested on production, run a sandbox test on unrelated material.
**Classification:** Edit kit / color request (wwd-color bench)
**Elapsed:** in progress
**Actions taken:** Wrote P:\WWD Kit\Color\README - UNTESTED.txt (3 LUTs from 2026-10-25 untested, not approved). Added TASKS.md WWD row, In Progress. Handed sandbox test (6 tests, inputs only P:\Color Training and P:\Stock Footage, outputs only D:\WKP\scratch\color-test\) to wwd-color via Agent tool.
**Deliverables:** pending, none yet
**Flags for Zac:** LUTs untested until results are reviewed. Devils-advocate review not applicable (internal test).

### 2026-10-25 - wwd-color sandbox test RESULT
**Status:** DONE (results back, Zac review pending)
**Trigger:** same as entry above.
**Classification:** Edit kit / color request
**Elapsed:** not timed
**Actions taken:** wwd-color ran 6 tests on P:\Color Training and P:\Stock Footage only, outputs in D:\WKP\scratch\color-test\. Found and fixed a major bug in make_look_lut.py: skin hue center was 123 deg (vectorscope) but code uses atan2(Q,I) where skin is near 0, so the skin mask was always 0 and skin protection never worked in any preset, including the three 2026-10-25 LUTs (left untouched, still UNTESTED, recommend rebuild). Added --auto-levels, --neutral, accent controls, --source fit for --reference, warnings in match_shots_lut.py. Whole-frame matching works when content matches (dE2000 4.0 to 2.5, 4.8 to 2.2, 4.0 to 1.7); skin-only needs --region. Fixed 3 wrong click steps in Color-LUT-How-To.md. Built Ledger Safe/Bold sandbox looks (refs Se7en, Fargo, Fight Club). Review: devils-advocate not run (internal test).
**Deliverables:** scripts make_look_lut.py, match_shots_lut.py (.claude\skills\wwd-review-photo-pull\scripts\), WWD\reports\Color-LUT-How-To.md, scratch D:\WKP\scratch\color-test\ (strips, Ledger LUTs). Not committed.
**Flags for Zac:** Eyes needed on skin (Ledger Bold especially) and on real webcam footage, banding. Rebuild Clayface/Match LUTs after skin fix? Adobe docs returned 403, wording from search summaries. D:\WKP Reports\Color LUT How-To\ docx is stale vs fixed md.

### 2026-10-25 22:50 - Color LUT How-To docx regenerated
**Status:** DONE | **Trigger:** Zac: regenerate docx from fixed md | **Classification:** Review (wwd-color support)
**Actions taken:** md_to_docx.py run on WWD\reports\Color-LUT-How-To.md, zero em or en dashes in output. No LUTs rebuilt or touched (Zac declined), monitor and webcam checks declined, LUTs stay UNTESTED. No commit.
**Deliverables:** D:\WKP Reports\Color LUT How-To\2026-10-25 - Color LUT How-To.docx

### 2026-10-26 21:10 - [wwd-vfx] Medieval host name tags (KING-Z, Winter Wolf)
**Status:** DONE (audio unheard)
**Trigger:** Zac via wwd-director: two host tags like the Vision Quest AI tags, medieval fantasy.
**Actions taken:** New script make_host_tags_medieval.py (reuses make_arcade_kit helpers, old script untouched). Rendered 2 tags, 108 frames, 3.6 s, 1920x1080 30fps. ffprobe and frame checks at 0.1, 0.4, 0.6, 1.0, 1.6, 2.6, 3.55 s done. Sounds copied to Host Tags\Sounds with CUES.txt.
**Deliverables:** P:\WWD Kit\Host Tags\Host Tag - KING-Z.mov, Host Tag - Winter Wolf.mov (alpha), plus "(MP4 green).mp4" each. Script D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\make_host_tags_medieval.py
**Flags for Zac:** audio not heard by me (howl segment unverified); MP4 has no alpha so it is on chroma green; sub lines are my picks, Zac to confirm.

## 2026-10-26 wwd-rights: Clayface (2026) final export rights gate
- Status: DONE, overall FLAG (risk flag, not legal advice). Trigger: wwd-director handoff.
- Actions: frame-sampled `Clayface Review-.mp4` (22:40.67), scene-change timing on every non-host segment, ffprobe on trailer copies and logo files, read run sheet, index, scripts. Scratch: D:\WKP\scratch\rights\.
- Findings: trailer runs at 275.5, 407.1, 447.3 (not on sheet), 458.4, 680.8, 683.0 (back to back with 680.8), 1283.0 to 1290.2 (7.2 s, over 4 s, scalpel shot reused). Stop 23 clip not in export. Premiere Ready trailer copies still carry AAC audio. Logo sting in the video is NOT the code-built one (opening logo.mp4 and Thanks for watching.mp4 carry encoder=Google, 8 s, 24 fps).
- Flags: could not verify audio muting, music, or SFX by ear. wwd-rights.md was read at D:\WKP\.claude\agents\wwd-rights.md (D:\WKP\WWD\formats\wwd-rights.md does not exist).

### 2026-10-26 21:55 - Clayface (2026) review pipeline
**Status:** DONE (with rights FLAGS for Zac)
**Trigger:** Zac says the Clayface review is finished, run wwd-review-pipeline held to STANDARDS.md.
**Classification:** Review
**Elapsed:** about 25 min
**Actions taken:** ffprobe final cut 22:40.67 and matched `Clayface Review final.txt` by Whisper word times (match within about 1 s, 2 speaker labels: Winter Wolf 79 blocks, KingZ 58); the 16.6 s gap to the last transcript line is the logo sting plus Thanks for watching end card. Silence map and word times on the export. AUDIO mp3 192k 22:40.67. 5 shorts built per shorts-factory (captions, hook, cover, frames viewed, edges checked); Short 3 rebuilt after wwd-rights found back-to-back trailer clips in its first window. Public copy via marketing-director (copywriting, social-media, no-ai-slop). wwd-rights run (FLAG). Chapters (13), 460-char tags (python verified), 5 hashtags, thumbnail, cards, end screen, posting windows written. Frames of the end show NO Next Up card for Vision Quest 3 and 4. devils-advocate not run this pass (not requested; flagged).
**Deliverables:** `D:\WKP\WWD\reports\Clayface-Upload-Package.md`; `D:\WKP Reports\WWD Upload Packages\Clayface Upload Package\2026-10-26 - Clayface Upload Package.docx` (copy in the Clayface folder); `...\Clayface\AUDIO\Clayface.mp3`; `...\Clayface\shorts\` (5 clips + covers). TASKS.md: Clayface row updated, "Post Clayface shorts" added (2026-10-29).
**Flags for Zac:** title pick; 2 card destinations; release date; end-screen tiles; Next Up card missing from export; trailer rights problems in the export (11:21 back to back, 21:23 run 7.2 s, unlisted 07:27 clip, muting unverified); music license record; AI logo sting and end card disclosure; garbles listed in package Section 12. SET REMINDER 2026-10-29 for "Post Clayface shorts" (main session, no scheduler here). Run sheet and its docx not touched.

### 2026-10-27 - Vision Quest eps 3 and 4 first-transcript intake and Edit Run Sheet
**Status:** DONE (sheet built; pictures thin, end card open)
**Trigger:** Jarvis: Zac's first edit transcript for Vision Quest eps 3 and 4 is in, run intake and Edit Run Sheet, near 35 to 40 stops.
**Classification:** Review
**Elapsed:** about 20 min
**Actions taken:** wwd-pictures: tagged 38 pics (3 added from TMDb, 36 to 38), dHash check vs eps 1-2 and within set, 0 twins (5 false positives eyeballed); only 10 usable (OK/OK-MEDIUM), 22 UNVERIFIED not placed. wwd-clip-scout: 2 clips (1.2 s and 1.9 s), muted copies made (Premiere Ready copies carried AAC), frame-checked. wwd-run-sheet: 24 stops, 10 pictures, 2 clips, 3 solo cams, 6 of 12 designed transitions, 3 Cross Dissolves. Director proof: lint rerun PASS, zero em dashes. wwd-rights and wwd-sound passes NOT yet run. devils-advocate not run.
**Deliverables:** `D:\WKP\WWD\reports\Vision-Quest-3-4-Edit-Run-Sheet.md`; `D:\WKP Reports\Asset Placement Run Sheets\2026-10-27 - Vision Quest 3 and 4 Edit Run Sheet.docx`; `...\Vision Quest ep 3 and 4\USE\pictures-tags.md`, `timeline-placements.md`; muted trailers in `Video Clips\Premiere Ready\`.
**Flags for Zac:** END CARD undecided; sheet is 24 stops (verified-picture limit); kit request Wrong Name Counter Series Tally (wwd-vfx, not built); Disney+ corner bug on trailer clips and Tommy ID in clip B visual only (needs wwd-rights); garbles "Kingsley" at 0:00 and "Cynthia Zoid" 13:37; date-sensitive lines 18:18 to 18:41; sound picks chosen by filename, not heard. DECISION QUEUED WWD-2026-10-27-01.

### 2026-10-28 23:35 - Vision Quest eps 3 and 4 DRAFT video render
**Status:** DONE (draft for Zac to scrub, not final)
**Trigger:** Zac: follow the Vision Quest run document and create the video, he adds the logo card after the hook. Mid-run: end card = Next Up Vision Quest 5 and 6; trim the stale Tuesday line.
**Classification:** Review (build from run sheet)
**Elapsed:** about 40 min
**Actions taken:** Read Zac's Premiere project copy (scratch only, original untouched), sequence "Vision Quest EP 3 and 4 review - NO AUDIO" gives 3 clips from the Synced files (hook, one 14.5 s cut, one 60 s cut). Whisper word times on the mixed cams for every search phrase. Built Next Up Vision Quest 5 and 6 card (make_vq56_next_up.py, frame checked). Trimmed the stale Tuesday passage: render 18:18.40 to 18:37.63 (19.23 s, between "still a watch" and "I get two episodes", 20 ms audio fades). Rendered with ffmpeg h264_nvenc, 10 composite/cam pieces, 10 pictures, 2 muted trailer clips (delogo on the Disney+ bug), 4 stickers, 8 sound cues, end card. Audio: cams mix, compressor, loudnorm -14 LUFS two-pass. FCP7 XML written. wwd-sound run (cues, loudness), wwd-rights run (note at WWD\reports\Vision-Quest-3-4-Rights-Note.md). devils-advocate not run (draft for Zac to scrub).
**Deliverables:** L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 3 and 4\Vision Quest EP 3 and 4 Review - DRAFT for Zac.mp4 (19:05.5, 1920x1080 30 CFR, 34365 frames, -14.0 LUFS, TP -1.4) and the same name .xml (xmeml, untested in Premiere). Card: P:\WWD Kit\Cards\Next Up - Vision Quest 5 and 6 (MP4).mp4 (+ .mov). Build scripts in D:\WKP\scratch\vq34build\.
**Flags for Zac:** LOGO CARD goes at 00:15.067 (frame 452, clean cut after "Come take a look", next word "All right guys"). Firefly opener left out (8.6 s from "situation is heating up" to the cut, opener is 11.5 s). Wrong Name Counter left out (not built, tally choice open). No music (Zac adds intro/outro). Stuck StreamYard caption "Grandfather is the fun one." on the KingZ tile in the composite for the whole video. Composite vs cam video offset: 0 to 1 frame early, about 3 frames after render time 9:06 (source 32:50); automated lip-sync test inconclusive, check by eye. Pictures 19, 21, 27 not source-verified (rights note). Spoiler Alert sticker was 2 to 3 dB over the voices, lowered 4.5 dB and re-mastered. Join at 18:18.4 needs a human ear. Transitions in the render are ffmpeg approximations of the Premiere Modern transitions. Garbles "Kingsley" and "Cynthia Zoid" are transcript errors, whisper hears KingZ in the audio.

### 2026-10-29 - Vision Quest eps 5 and 6 pre-record prep
**Status:** DONE (picture set thin, 4 stills; clips not downloaded)
**Trigger:** Jarvis: pre-record prep for Vision Quest eps 5 and 6, record Fri 2026-10-30; verify real air dates and titles, do not trust the calendar.
**Classification:** Review (pre-record intake)
**Elapsed:** about 25 min
**Actions taken:** wwd-pictures: verified facts (air Tue 2026-10-27, ep 5 "Firewall" 48 min, ep 6 "Deadlock" 57 min, per Wikipedia + TMDb; director Natali and writers Monfette/Falsetti Wikipedia only), pulled 6 TMDb stills, 2 were twins of eps 3-4 pictures and moved to USE\_unverified, 4 kept in USE (1920x1080 RGBA), IMDb per-actor galleries blocked (403, no Chrome). wwd-clip-scout: 2 Marvel promos (22 s, 24 s) listed as links only, nothing downloaded, no frames checked; titles also confirmed by bamsmackpow; air date confirmed by Marvel's own description. wwd-vfx: kit check, nothing built; System Boot.mov stale ("EPISODES 1 + 2" baked in), Cyberspace version, Spoiler Alert, 5 AI tags and Firefly opener reusable; Wrong Name Counter series tally still unbuilt. Brief written.
**Deliverables:** `D:\WKP\WWD\reports\Vision-Quest-5-6-Prep.md`; `D:\WKP Reports\Review Prep\2026-10-29 - Vision Quest 5 and 6 Prep.docx`; `...\Vision Quest ep 5 and 6\USE\` (4 PNGs, pictures-tags.md, _unverified\); `D:\WKP\scratch\vq56_urls.txt`. Devils-advocate review not run (prep brief, internal).
**Flags for Zac:** CALENDAR NEEDED: none new (main session already set 10/30). Wrong Name Counter continue-or-fresh; what comes after for end card; yes/no to download 2 promos; Chrome session for IMDb actor stills; confirm record time; director/writer credits single-source; scout's trailer ID sXkmgmbkoE is 10 chars, recheck before use.

## 2026-10-29 17:15 - Vision Quest 5 and 6 picture pull + promos (Jarvis, scheduled job)
- IMDb ep 5 (tt38934491) and ep 6 (tt38934495) galleries pulled via Chrome in-page fetch. 20 tagged stills checked, 11 added to USE as 5 to 15, 9 skipped as dHash 0 repeats of eps 1-2 / 3-4 or of this set. USE = 15. Originals deleted. pictures-tags.md rewritten with IMDb caption tags.
- Promos r4lYJ9xKttU and R9T7U5y3_C0 downloaded with yt-dlp, converted to muted H.264 30 fps in Video Clips. Both vertical 1080x1920. Devil on His Shoulder has a Disney+ bug and burned captions.
- Prep brief md + docx updated (D:\WKP Reports\Review Prep\2026-10-29 - Vision Quest 5 and 6 Prep.docx).

## 2026-10-29 wwd-rights: Vision Quest 3 and 4 FINAL cut rights check
- Status: done. Trigger: wwd-director request.
- Actions: frame-scanned final (19:17.9) at opening, 478.9-480.3, 605.6-608.2, end cards; corner-crop contact sheets for Disney+ bug; compared 795 s still to USE folder.
- Deliverable: WWD\reports\Vision-Quest-3-4-Rights-Note.md (FINAL section added in place).
- Flags: opening flash 0-1.8 s has unblurred Disney+ bug (15 of 16 samples); Ultron and pool clips clean; still 37.png does not match its pictures-tags row; muted audio and music source unverified; Firefly opener needs AI disclosure; end card black from about 1153.5 s.

### 2026-10-29 21:00 - Vision Quest eps 3 and 4 FINAL cut review pipeline
**Status:** DONE (with rights and export FLAGS for Zac)
**Trigger:** Jarvis: Zac's final cut is exported, run the full wwd-review-pipeline.
**Classification:** Review
**Elapsed:** about 55 min
**Actions taken:** ffprobe final 19:17.90 (1920x1080 30 fps H.264+AAC). Transcribed the final cut with wwd-video-transcriber (GPU, 2 speakers, 231 lines). Silence map (185 gaps) and Whisper word times. Frame checks: opening is about 1.8 s unblurred trailer flash (Disney+ bug) then the Firefly opener, logo burn about 12.9 to 17.3 s, hosts at about 23 s; Next Up 5+6 card IS in the export (19:01 to 19:07), Thanks card 19:07 to 19:13, then 4.9 s of black; stuck caption "Grandfather is the fun one." still in. 1 fps scan found 2 trailer clips (about 07:59, 10:06). AUDIO mp3 192k 1157.9 s. 5 shorts built per shorts-factory (clips 1 to 5, heads and tails checked with check_clip, clips 4 and 5 re-rendered after head words fixed, frames viewed). Public copy via marketing-director (copywriting, social-media) plus a manual no-ai-slop pass. wwd-rights final note run (FLAG). Chapters (14), 479-char tags (python verified), 5 hashtags, cards, end screen, posting windows written. devils-advocate not run.
**Deliverables:** `D:\WKP\WWD\reports\Vision-Quest-3-4-Upload-Package.md`; `D:\WKP Reports\WWD Upload Packages\Vision Quest 3 and 4 Upload Package\2026-10-29 - Vision Quest 3 and 4 Upload Package.docx` (copies md + docx in the show folder); `...\Vision Quest ep 3 and 4\AUDIO\Vision Quest Ep 3 and 4.mp3`; `...\shorts\` (5 clips + covers); transcript `Vision_Quest_EP_3_and_4_review_transcript.txt`; rights note updated in place. TASKS.md: row updated, "Post Vision Quest (eps 3 + 4) shorts" added (2026-11-01).
**Flags for Zac:** title pick; 2 card destinations; release date; opening trailer flash with unblurred Disney+ bug (cut it); 4.9 s black tail; stuck caption; music and opener audio source unnamed; tick AI disclosure; row 37 tag mismatch. SET REMINDER for "Post Vision Quest shorts" (main session, no scheduler). No calendar adds.

### 2026-10-31 - wwd-run-sheet: Vision Quest eps 5 and 6 Edit Run Sheet v1
**Status:** DONE (lint PASS, opener/logo order and tail placement open for Zac)
**Trigger:** wwd-director handoff, Edit Run Sheet for Vision Quest 5 and 6 with a 5 s logo slot after the hook (LOGO_SECONDS constant, two time columns).
**Actions taken:** read STANDARDS, WWD CLAUDE, eps 3-4 sheet, 720-line transcript, pictures-tags. Pulled frames from both promos with ffmpeg (0.25 s, 0.1 s, then single frames at each edge) to find shot edges. Checked search words are unique in the transcript, sound and kit paths exist, hash check on USE (0 pairs). Generator script `D:\WKP\scratch\vq56\build.py` (change LOGO_SECONDS, re-run). No lint change needed, two-time-column heading works as is.
**Deliverables:** `D:\WKP\WWD\reports\Vision-Quest-5-6-Edit-Run-Sheet.md`; `D:\WKP Reports\Asset Placement Run Sheets\2026-10-31 - Vision Quest 5 and 6 Edit Run Sheet.docx`; md copy in the show folder.
**Flags:** opener plus logo order; no Wrong Name Counter placed (open question); transcript tail after the goodbye (27:54 to 31:05) holds the spoiler line and the card position; promo B Disney+ bug cropped out (wwd-rights); Matt's promised van clip (20:53) not in folder; "Kingsley" here is Ben Kingsley, not a garble; garble list with timecodes in the sheet.

### 2026-10-31 - [wwd-vfx] Next Up card, Vision Quest ep 7 only
**Status:** DONE
**Trigger:** wwd-director: schedule changed, ep 7 drops next week, ep 8 the week after.
**Actions taken:** Copied make_vq78_next_up.py to make_vq7_next_up.py, text changed to EPISODE 7 (terminal lines say EPISODE 7 FOUND, STATUS READY). Same owned sounds. Rendered, deleted the stray .mov intermediate. Frames at 0.5, 2.5, 5.0 s checked, no "8" or "Finale". Old 7+8 card and script untouched.
**Deliverables:** P:\WWD Kit\Cards\Next Up - Vision Quest 7 (MP4).mp4 (6.000 s, video+audio); script D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\make_vq7_next_up.py
**Flags for Zac:** audio not heard (cannot listen).

## 2026-10-31 wwd-run-sheet: Vision Quest 5 and 6 Edit Run Sheet v2 (in place)
**Status:** DONE
**Trigger:** wwd-director: Zac's answers (opener already in cut, logo 5.0 s confirmed, no Wrong Name Counter, tail is Zac's, schedule ep 7 next week, cams synced).
**Actions taken:** Edited md directly (build.py is now stale, do not regenerate from it). Removed opener stop, Spoiler Alert stop, tail items, Wrong Name Counter, opener/logo order question, unsynced-cam and schedule flags. Logo slot is stop 1. End card now stop 24 at 27:54, `P:\WWD Kit\Cards\Next Up - Vision Quest 7 (MP4).mp4` (verified on disk, 6.0 s). CAM stops got in/out/length. Van clip placeholder note added at 20:53 (no clip). Stops renumbered 26 to 24.
**Deliverables:** md `D:\WKP\WWD\reports\Vision-Quest-5-6-Edit-Run-Sheet.md` (copy in show folder); docx `D:\WKP Reports\Asset Placement Run Sheets\2026-10-31 - Vision Quest 5 and 6 Edit Run Sheet.docx`.
**Checks:** lint RESULT: PASS (stops 24, cross dissolves 2, designed 7 of 14, trailer clips 2, 2.5 s). Paths exist, 12 pictures none twice, no em dashes, times in order.
**Flags:** cannot hear audio or open Premiere.

### 2026-11-01 19:20 - Vision Quest eps 5 and 6 FINAL cut review pipeline
**Status:** DONE (with rights and export FLAGS for Zac)
**Trigger:** Zac: final transcript and final render are in the show folder, run wwd-review-pipeline.
**Classification:** Review
**Elapsed:** about 25 min
**Actions taken:** ffprobe final 28:09.03 (1920x1080 30 fps H.264+AAC), file size stable across two reads. Read the Premiere final transcript (612 lines, labeled Winter Wolf / KingZ, HH:MM:SS:FF). Silence map (511 gaps) and Whisper word times (5,574 words), chapters spot-checked against Whisper. AUDIO mp3 192k 1689.03 s (matches). 5 finished shorts rendered with build_short.py (44.4, 39.3, 49.3, 46.4, 40.3 s), first and last words checked with check_clip.py, frames and covers viewed. 14 chapters from transcript timecodes. Copy: marketing-director wrote title, description pieces, FB/IG V1 and V2 and 5 short captions to writing-room rules (its own report: copywriting and social-media were not launched as separate desks), wwd-director corrected short 1, 4 and V2 copy against the clips and ran the no-ai-slop rules by hand (no em dashes, handles only, no verdict; the skill file was not invoked). wwd-rights: FLAG (see below). Package md + docx built.
**Deliverables:** `D:\WKP\WWD\reports\Vision-Quest-5-6-Upload-Package.md`; `D:\WKP Reports\WWD Upload Packages\Vision Quest 5 and 6 Upload Package\2026-11-01 - Vision Quest 5 and 6 Upload Package.docx`; copies in the show folder; `AUDIO\Vision Quest Ep 5 and 6.mp3`; `shorts\clip1_tony_stark_origin`, `clip2_bones_should_break`, `clip3_my_hacks_have_hacks`, `clip4_not_your_fathers_vision`, `clip5_creepiest_scene` (.mp4 + _cover.png) in the show folder; rights note `D:\WKP\WWD\reports\Vision-Quest-5-6-Rights-Note.md`; copy working file `D:\WKP\scratch\vq56final\copy_final.md`.
**Review gate:** devils-advocate not run (standard format, no new idea).
**Flags for Zac:** title pick; 2 card destinations; release date (before Tue 11/3 or the "episode seven next week" line goes stale); opening flash 11.3 to 14.7 s has the Disney+ logo unblurred (cut it); Promo B (954 to 956 s) still shows its title text, re-crop; 3 pictures with no recorded source (top hat man 263 s, `lisa taken over.jpg` from `_unverified` 1086 s and the first 4 s of Short 5, red-arrow street frame 1265 s); picture 1 up 8.8 s; stuck tile captions "Strings..." and "This isn't goodbye, its see you later." in the video and all shorts; Next Up Vision Quest 7 card sits mid-goodbye at 27:44 to 27:50; "Kingsley and I" in the hook; listen check for trailer audio; opener/Next Up audio source and any music unnamed; tick altered-or-synthetic for the Firefly opener; calendar needs ep 7 on 11/3 and ep 8 the week after (calendar tool failed auth before); shorts reminder not set (no scheduler tool, main session to set it).

### 2026-11-05 - Godzilla Minus Zero review intake
**Status:** DONE (pictures PARTIAL)
**Trigger:** Zac sees it Thu 11-05, records Fri 11-06. Review intake, prep brief, TASKS row draft.
**Classification:** Review
**Elapsed:** about 20 min
**Actions taken:** Folder created `Raw Footage\Godzilla Minus Zero\USE\`. TMDb 403 (Cloudflare), IMDb 202 empty (WAF), no browser tool, so no stills pulled. Poster only from the Rotten Tomatoes one-sheet (675x1000), resized to `USE\1.png` 1920x1080 RGBA contain, original deleted, source list `scratch\godzilla_minus_zero_urls.txt`. Prep brief from Wikipedia and live RT page (RT critics 90% on 98, runtime 2h15m, R, wide Nov 6, audience score not available).
**Deliverables:** `D:\WKP\WWD\reports\Godzilla-Minus-Zero-Prep.md`; `D:\WKP Reports\Review Prep\2026-11-05 - Godzilla Minus Zero Prep.docx`.
**Review gate:** devils-advocate not run (standard review format).
**Flags for Zac:** CALENDAR NEEDED (record Fri 11-06 evening, release TBD). NEEDS BROWSER PULL: 17 stills via IMDb/TMDb in Chrome (main session). Metacritic 75 only from Wikipedia.

### 2026-11-07 13:10 - Godzilla Minus Zero review pipeline (PARTIAL, blocked on export)
**Status:** BLOCKED (package text DONE, audio and shorts not run)
**Trigger:** Zac: run the full wwd-review-pipeline on the final cut and its Premiere transcript.
**Classification:** Review
**Elapsed:** about 25 min
**Actions taken:** ffprobe of the "final cut" mp4: 2776.1 s (46:16), vs transcript last block 00:28:28:29. Sampled frames and a GPU Whisper pass on the mp4: countdown at start, intro clip chatter, pre-show banter, review begins about 12:30, spoiler-card take after the sign-off. It is the raw StreamYard recording, not the edit. STOPPED audio extraction and Shorts (cutting from it would be wrong). Built package text from the 640-line transcript: 2 titles, description with QUICK ANSWERS, 13 chapters (draft timeline), tags 490 chars (python-verified), 5 hashtags, 3 cards from video-inventory, end screen, post sequence with 3 time options per day type (release date unknown, Sun 11/8 and Mon 11/9 given), FB and IG posts, 6 Shorts candidate windows (not cut), flags, caption fix list. Public copy: marketing-director routed copywriting (title, description) and social-media (FB, IG), edited by marketing-director, rules applied by hand. wwd-rights ran on the stills (note in WWD\reports\Godzilla-Minus-Zero-Rights-Note.md).
**Deliverables:** `D:\WKP\WWD\reports\Godzilla-Minus-Zero-Upload-Package.md`; `D:\WKP Reports\WWD Upload Packages\Godzilla Minus Zero Upload Package\2026-11-07 - Godzilla Minus Zero Upload Package.docx`; copies (.md, .docx) in the movie folder; copy draft `WWD\reports\Godzilla-Minus-Zero-Copy-Draft.md`; rights note. No AUDIO mp3, no shorts.
**Review gate:** devils-advocate not run (standard format). Formal no-ai-slop skill pass not run (rules applied by hand, grep: zero em dashes). Owed by main session.
**Flags for Zac:** NEED THE EDIT EXPORT from Premiere (then audio, 5 Shorts, chapter re-time, card and rights check on render). Rights FAILS in USE: 10 named PNGs have no recorded source, wig clip-art picture is not from the film, dr noda pc1 and bw pc 2 are identical, three extra key-art images, a collage, (c) Toho mark on 4.png and 7.png. Release date, title pick, EP119 card swap. Garbles and on-air budget guess held out of copy. Ratings said on air, not used anywhere.

### 2026-11-07 13:10 - [wwd-vfx] Godzilla Minus Zero: logo squash Firefly prompt + sound pack
**Status:** DONE (nothing generated, nothing spent)
**Trigger:** Zac via wwd-director, two deliverables for the Godzilla Minus Zero review
**Actions taken:** Read burning logo clip (frames viewed) and Clayface docs, built black start frame, wrote 3 prompts + avoid list. Copied 47 owned sounds (incl. one derived 3-step clip) to P:\WWD Kit\Godzilla\Sounds\, ffprobed. Wrote sting sound plan and whole-video cue sheet from the cut transcript. Script make_godzilla_sound_pack.py.
**Deliverables:** D:\WKP\WWD\reports\Godzilla-Logo-Squash-Firefly-Prompt.md and Godzilla-Sound-Cue-Sheet.md; docx in D:\WKP Reports\Godzilla Minus Zero\ and \Godzilla Sound Pack\; P:\WWD Kit\Godzilla\
**Flags for Zac:** Prompts untested (credits). The mp4 in the folder is the raw 46:16 recording with a countdown, not the cut; timings come from the transcript, many marked est. No owned kaiju roar, ground crack, rimshot or mech sound (prompts written).

### 2026-11-07 13:40 - Godzilla Minus Zero Edit Run Sheet
**Status:** DONE (pictures and sting PARTIAL)
**Trigger:** Zac: build the Edit Run Sheet for Godzilla Minus Zero, per current format, with sting, sound cues, rights fixes, missing pictures, clips, Next Up note, garbles.
**Classification:** Review
**Elapsed:** about 40 min
**Actions taken:** Read STANDARDS, transcript, rights note, sound cue sheet, tags, Street Fighter and Clayface sheets. Viewed all 21 USE pictures and 9 loose files (contact sheets). Hash check (dup_check2): 1 of 21 flagged (Noda pair). IMDb 202 empty and TMDb 403 again from this agent, no browser, so the fresh pull was NOT done. wwd-clip-scout: 1 clip verified and written (dogfight, IMAX trailer, 1.1 s, muted), Ghidorah, gravity beam and first attack not offered. I drafted the sheet myself (wwd-run-sheet bench not used for the build), lint PASS: 41 stops, 18 pictures all different, 1 clip, 2 Cross Dissolves, 11 of 19 stops designed, longest hold 6 s. wwd-rights and wwd-sound launched for check lines.
**Deliverables:** `D:\WKP\WWD\reports\Godzilla-Minus-Zero-Edit-Run-Sheet.md`; `D:\WKP Reports\Asset Placement Run Sheets\2026-11-07 - Godzilla Minus Zero Edit Run Sheet.docx`; copy `USE\timeline-placements.md`; `USE\tags.md` extended; `Video Clips\GMZ_dogfight_IMAXtrailer_kw0YhiqOPFg_f1309-1335_muted.mp4`.
**Review gate:** devils-advocate not run (standard format, no new idea).
**Flags for Zac:** NEEDS CHROME PULL (missing pictures list in the sheet, main session). Next Up card: ask what comes next. Sting clip not made (Firefly credits). OK the scratch trailer download in D:\WKP\scratch\gmz\ (official channel, not pre-approved). wig dropped, 7 pictures unsourced and flagged. Claims: emperor, ships and Russia, budget guess. Sound cue sheet times differ from the transcript at spoiler card, sticker and rating foot (sheet follows the transcript).

### 2026-11-07 23:30 - Godzilla Minus Zero FINAL CUT pipeline
**Status:** DONE
**Trigger:** Zac via Jarvis: final cut landed, finish the review pipeline, new titles, copy from Copy-Final.
**Classification:** Review
**Elapsed:** several hours
**Actions taken:** 2-speaker transcript (402 lines, labels inferred); 13 chapters re-timed; AUDIO mp3 (1733.6 s); 5 finished Shorts + covers (loudnorm, QC frames, check_clip); rights frame check, Noda duplicate claim corrected; package rebuilt from marketing-director copy (no-ai-slop passed), zero em dashes.
**Deliverables:** WWD\reports\Godzilla-Minus-Zero-Upload-Package.md; movie folder package md/docx, AUDIO, shorts\ incl. Shorts Captions md/docx; D:\WKP Reports\WWD Upload Packages\Godzilla Minus Zero Upload Package\2026-11-07 - ... (final cut).docx (dated file locked by Word).
**Review gate:** devils-advocate not run (standard format).
**Flags for Zac:** loudness -24.7 LUFS / TP -2.4 not fixed (shorts about -15); about 18 s trailer footage, 5.1 s clip over 4 s rule; AI logo sting disclosure; Dr. Dune / Charles Magneto audio in Short 3; release date, title pick, card links, EP119 card swap; 10 unsourced pictures.

### 2026-11-09 18:05 - Vision Quest ep 7 review intake, edit-prep (raw-recording run sheet)
**Status:** DONE (edit-prep side), end card OPEN
**Trigger:** Zac edits Vision Quest ep 7 tonight, run the review intake, transcript plus Edit Run Sheet.
**Classification:** Review
**Elapsed:** about 15 min (transcription 3.5 min on GPU)
**Actions taken:** wwd-video-transcriber on the raw mp4 (42:55, --num-speakers 2, 739 lines); speakers mapped to the cams by loudness (Speaker 1 = KingZ, Speaker 2 = Winter Wolf), relabeled; run sheet v1 built by hand (9 stops, 2 pictures, 3 CAM, 1 sticker, 1 gag sound, logo slot, end card OPEN); lint PASS (stops 9, 0 cross dissolves, 1 of 2 picture stops designed). wwd-run-sheet bench not launched (I built it directly from the spec). devils-advocate not run (internal run sheet).
**Deliverables:** transcript `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\EP 7\Vision Quest Review EP 7_transcript.txt`; `D:\WKP\WWD\reports\Vision-Quest-7-Edit-Run-Sheet.md`; `D:\WKP Reports\Asset Placement Run Sheets\2026-11-09 - Vision Quest EP 7 Edit Run Sheet.docx`; TASKS.md row added.
**Flags for Zac:** all sheet times are RAW-recording times; cams are about 7 s shorter than the main file, sync first; end card for episode 8 does not exist (NEEDS WWD-VFX: "NEXT UP / VISION QUEST / EPISODE 8 // FINALE"); only 2 of 5 USE pictures verified (1, 2, 3 untagged, left out); main session to pull more pictures per the gap list in the sheet; raw 00:00 to 00:24 movie-quote montage unclear; opener assumed already in Zac's cut; no calendar or posting actions taken.
2026-11-10 wwd-rights: Vision Quest EP7 final export rights note written, WWD/reports/Vision-Quest-7-Rights-Note.md. Verdict FLAG.

### 2026-11-10 21:45 - Vision Quest EP 7 review pipeline (final cut)
**Status:** DONE (fixes owed by Zac before upload)
**Trigger:** Jarvis: run wwd-review-pipeline on VQ EP 7, final cut is in
**Classification:** Review
**Elapsed:** about 35 min
**Actions taken:** Copied final export (23:55.5, 1920x1080 30fps H.264/AAC, size stable) into EP 7 folder as `... FINAL export.mp4`, original left in Godzilla Minus Zero folder. Loudness measured: -22.8 LUFS, TP -1.7 dBFS (about 8.8 dB under -14); a quick loudnorm fix hit +1.1 dBFS true peak, deleted, not offered. Transcribed the export (GPU, 2 speakers, 270 lines, Guest/Unknown labels). Frame scan of export: opener 0-11.5 s, 2.7 s Disney+ footage with unblurred bug 11.5-14.2 s, logo sting to 18.4 s, 8 pictures, 3 solo cams, Spoiler Alert and Wolfie stickers, Thanks card at 23:47.8 (no Next Up ep 8 card). Audio mp3 built (1435.53 s). 5 finished shorts built (21.9/24.3/48.2/49.7/48.3 s), edge-checked, frames viewed, clip 5 captions cleaned. Copy via marketing-director (copywriting + social-media desks); script-room NOT run as separate pass (stated in package). wwd-rights note written (verdict FLAG). Package md + docx built, 14 chapters, tags 464 chars verified, 5 hashtags, 3 cards from video-inventory, post sequence with 3 time options each.
**Deliverables:** D:\WKP\WWD\reports\Vision-Quest-7-Upload-Package.md; D:\WKP Reports\WWD Upload Packages\Vision Quest 7 Upload Package\2026-11-10 - Vision Quest 7 Upload Package.docx; copies in L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\EP 7\; AUDIO\Vision Quest Ep 7.mp3; shorts\clip1-5 (+covers); transcript; D:\WKP\WWD\reports\Vision-Quest-7-Rights-Note.md
**Flags for Zac:** Disney+ bug block 11.5-14.2 s (cut or blur); 3 unsourced pictures (in shadow client, the client, Rocketman); CC BY-SA Spader credit; AI disclosure; unnamed music/sound sources; song mention 4:48-4:58; stale lines 22:36-22:43 and EP120 line; loudness -22.8 LUFS; no ep 8 end card (NEEDS WWD-VFX); video-inventory not refreshed (VidIQ credits 0 until 11-11). TASKS row and 3 reminder dates for shorts (Thu 11/12 to Mon 11/16) NEEDED by main session (director has no scheduler). Devils-advocate pass not run (fast turn, same format as VQ 5-6).

### 2026-11-10 22:30 - FrostCast EP120 show prep
**Status:** DONE
**Trigger:** Jarvis: build EP120 show prep from Matt's list (recording Wed 11/11 9 PM, Veterans Day)
**Classification:** FrostCast show prep (no transcript step)
**Elapsed:** about 15 min
**Actions taken:** Read topic photo (7 topics, clear). Three fact-research agents with live web research (Gunn/Wolverine/Driver; Blade Runner 2099/monsters/Nolan; Jimmy/Veterans Day). Prep built in wwd-show-prep format with OBSERVED/SECONDARY/NOT AVAILABLE labels. Zero em dashes checked by grep. devils-advocate not run (internal prep sheet).
**Deliverables:** D:\WKP\WWD\reports\FrostCast-EP120-Show-Prep.md; D:\WKP Reports\FrostCast\2026-11-10 - FrostCast EP120 Show Prep.docx
**Flags for Zac:** Gunn news broke 11/9, recheck the morning of the show; Jimmy RT score not retrievable, Odyssey current gross unpinned; Variety/THR/CBC text blocked, headlines only. Not committed or pushed. Not sent to Matt.

2026-11-10 EP120 prep revised in place: Matt out, panel is KingZ and Oracle. Angles rebalanced, confirm lists redone, docx regenerated. Not committed.

2026-11-10 EP120 prep revised in place: Matt out, panel is KingZ and Oracle. Angles rebalanced, confirm lists redone, docx regenerated. Not committed.
