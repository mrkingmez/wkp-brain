# Media Map

Kept by `media-manager`. Human-readable index of where media, sounds, music, tools, plugins, LUTs, templates and kits live on every drive.
Created 2026-11-17. Source: `LOCAL-PATHS.md` plus `data\assets\p-drive-index.csv` (27,207 file rows, P: drive only, undated), then each folder checked on disk 2026-11-17 with a directory listing. Entry counts are top-level entries in that folder, not recursive, unless it says "indexed files".

How to use: run `python D:\WKP\.claude\skills\media-manager\scripts\find_asset.py <keywords>`. File-level search covers P: only (the CSV). Every other drive is folder level in this file.
Status column: VERIFIED = listed on disk 2026-11-17. NOT VERIFIED = taken from a doc, not checked. Licenses: "unknown" means nothing is recorded on disk. Do not assume a license from a folder name.

## 1. Drives at a glance

| Drive | What it is | Status |
|---|---|---|
| C: | System. Blender portable at `C:\Blender\5.2.4`. Python, ffmpeg, user settings | VERIFIED (Blender folder) |
| D: | Repo (`D:\WKP`), reports (`D:\WKP Reports`), ventures' source files, tools, Unreal, Blender projects | VERIFIED |
| E: | OLD archive. `01 Warrior King Productions Archive`, `03 My writing`, `04 Warrior King Desins` (retired), `Pictures - Video`. Do not touch. | VERIFIED (top level) |
| L: | WWD show media, Zac's writing, AI art, guides | VERIFIED |
| P: | Owned asset library and older WKP project folders. 27,207 files indexed | VERIFIED |

## 2. Sound effects, music (P:)

| What | Path | Count | License | Status |
|---|---|---|---|---|
| Sound FX root | `P:\Sounds\Sound FX` | 10,419 indexed files, mostly .wav | Adobe SFX library under `Adobe\` (Adobe license, owned via subscription, verify before client use). Loose mp3s: unknown | VERIFIED |
| Adobe SFX categories | `P:\Sounds\Sound FX\Adobe\<category>` (Sports, Industry, Household, Emergency Effects, Ambience_1, Ambience_2, Animals, Cartoon, Crashes, DC, DTMF, Drones, Fire and Explosions, more) | see index | Adobe | VERIFIED (sample) |
| Other SFX packs | `P:\Sounds\Sound FX\PB - Footstep SFX`, `PB - Sci-Fi UI Free SFX`, `15 Free Ambient Sound Effects` | | PremiumBeat free packs and others, terms unknown | VERIFIED |
| Foley and sound design archives | `P:\Sounds\FEP_ES_FoleySound.rar`, `P:\Sounds\FEP_ES_SoundDesign.rar` | not unpacked | unknown | VERIFIED (exist) |
| HORIZON cinematic sounds | `P:\HORIZON - CINEMATIC SOUNDS.zip` | not unpacked | unknown | VERIFIED (exists) |
| Music root | `P:\Sounds\Music` | 221 top-level, 5,332 indexed files | per track, mostly unknown. Ask `music` before any public use | VERIFIED |
| WWD music (L:) | `L:\Winter Wolfs Den review show\Muisc` (folder name misspelled on disk) | | unknown | VERIFIED |
| Ian trailer music candidates | `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Music` | 8 | `searching-for-hope`: no license file on disk. Alex Morgan FMA: CC BY, track page unchecked | VERIFIED (count) |
| Loose track | `P:\Sounds\02-twista-american_gangsta.mp3` | 1 | commercial track, do NOT use in any public video | VERIFIED |

## 3. Stock footage, templates, tools, plugins, LUTs (P:)

| What | Path | Count | License | Status |
|---|---|---|---|---|
| Stock footage | `P:\Stock Footage` | 107 top-level (.mov, .mp4 numbered clips), `Spark by RocketStock` 65, `Green Screen` 8 | clip-site numbered files, license unknown | VERIFIED |
| After Effects templates | `P:\AE Templets` (misspelled on disk) | large, 4,926-file trailer template, `Project_10`, `Hammer Reveal`, `Logo Glitch`, `The Storm`, `Winter is here`, `Cinematic Title Bars`, more | videoblocks style, license unknown | VERIFIED |
| Tools root | `P:\Tools` | 30+ packs | per pack, see README_LicenseAgreement.pdf in folder | VERIFIED |
| Action hits, space kit, flares, camera shake | `P:\Tools\PB - Action Hits Toolkit`, `PB - Space Kit`, `PB - Anamorphic Lens Flares`, `PB - Free Camera Shake Presets` | | PremiumBeat free | VERIFIED |
| LUTs (.cube) | `P:\Tools\PB - 17 FREE LUTs`, `P:\Tools\LUTS` (zip packs: Ground Control free LUTs for D-Log, S-Log3, V-Log, BMD Film, CineLike, Protune), `P:\Tools\PremiumGrades`, `P:\Tools\PremiumBeat Hollywood Lumetri Looks`, `P:\LUTS.zip` | 17 .cube files indexed | free packs, verify per pack | VERIFIED |
| Overlays and logo reveals | `P:\Tools\Camera overlays`, `Logo revels`, `Free+Lava+Burst+Pack`, `Free+Stylized+Blood+Pack`, `Volumetric Freebie`, `Nebula Freebie`, `Mixkit`, `Free Animated Icon Sets`, `16 Free Transitions`, `Transitions`, `Action Pack Lite - RocketStock`, `Aspect_Ratio_Pack` | | free packs, terms in each folder | VERIFIED |
| Hero HUD and FX packs | `P:\Tools\EDITH_FL`, `IRONMANHUD_FL`, `SYMBIOTE_FL`, `STRIKE 1.0`, `VILLIAN 01 RF`, `ZOOM 01` | | unknown | VERIFIED |
| Marketing templates | `P:\Tools\PremiumBeat Movie Marketing Templates`, `Movie Poster Template - StudioBinder`, `Photobacks Snow Globe Template`, `P:\Pitch Templates` (Broadcast_Long Form Documentary Pitch, Commericial Pitch, Standard Pitch), `P:\Budget & Schedule Templates.zip` | | unknown | VERIFIED |
| Plugins and installers | `P:\Tools\Vibrance.aex`, `Vibrance64.plugin`, `VCOrb_1.0.0_Installer_x64.exe`, `P:\Saber_1.0.40_Installer_Win_2022.1.zip` (Saber, Video Copilot) | | Saber and VC Orb are free from Video Copilot. Confirm before relying on that | VERIFIED (exist) |
| Premiere presets | `P:\Tools\Jarle's Deadpool Camera Shake Presets.prfpset`, `D:\Screen Shake Annoyed Editor.prfpset` | 3 .prfpset indexed | unknown | VERIFIED |
| Textures | `P:\Texture` | many, `12_Seamless_Rock_Textures`, `Galaxy Pictures`, loose jpg and png | unknown | VERIFIED |
| Color training | `P:\Color Training` (02_Cameras, 03_Color_Correction, 04_Shot_Matching, 05_Color_Grading, DaVinci Resolve 16 PDFs), duplicate at `P:\01 Warrior King Productions\Color Training` | | training material, personal use | VERIFIED |
| Podcast kit | `P:\Podcast\files.zip` | | unknown | VERIFIED |

## 4. WWD kit (P:\WWD Kit)

Built by `wwd-vfx` and `wwd-color`. Per show subfolder.

| Folder | Path | Entries | Status |
|---|---|---|---|
| Cards | `P:\WWD Kit\Cards` | 12 | VERIFIED |
| Stickers | `P:\WWD Kit\Stickers` | 8 | VERIFIED |
| Host tags | `P:\WWD Kit\Host Tags` | 5 | VERIFIED |
| Transitions | `P:\WWD Kit\Transitions` (Blood Pour.mov) | 1 | VERIFIED |
| Color (LUTs, UNTESTED per README) | `P:\WWD Kit\Color` (Clayface Bold and Safe .cube, WinterWolf-to-KingZ match .cube, README - UNTESTED.txt) | 9 | VERIFIED |
| Per show | `Clayface` 6, `Crystal Lake` 9, `Godzilla` 3, `Street Fighter` 19, `Veterans Day` 7, `Vision Quest` 16 | | VERIFIED |

## 5. WWD show media (L:)

| What | Path | Status |
|---|---|---|
| Show root | `L:\Winter Wolfs Den review show\` (43 entries) | VERIFIED |
| Finished videos | `...\Final` | VERIFIED |
| Raw footage per movie or show | `...\Raw Footage\<title>` (movie folders, plus USE subfolders for pictures) | VERIFIED |
| FrostCast | `...\Frost-Cast` (142 entries), raw audio `...\Frost-Cast\Raw Audio` | VERIFIED (root) |
| FrostCast audio cut docs | `...\Audio\podcast Frostcast audio files\` | NOT VERIFIED (from CLAUDE.md) |
| Den Files | `...\Den Files\EP 1` | VERIFIED |
| Other | `After Effects`, `Premerir` (misspelled), `VFX`, `Pictures`, `Badges`, `emoji`, `Sponsors`, `Software\Animated-Lower-Thirds`, `OBS records`, `WWD Social`, `2026 Short Series`, `New opening short`, `_voiceprints` (matt.npy, zac.npy) | VERIFIED |
| Voiceprints (current, all three voices) | `D:\WKP\voiceprints\` gitignored | NOT VERIFIED |
| Opus Clip work | `D:\WKP\WWD\opusclip\` | VERIFIED (parent) |
| Upload packages | `D:\WKP Reports\WWD Upload Packages\<Movie> Upload Package\` | NOT VERIFIED (parent only) |

## 6. Project folders by venture

| Venture | Path | Status |
|---|---|---|
| Ian Griffin "Wrench Turner" trailer (Studio job) | `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\` | VERIFIED |
| WKP video projects, older | `P:\01 Warrior King Productions\02 Video Project\` (AI Video Project, Caroral family interview, Coming Soon, New TPSH 2023, Paris Photo edit, TPSH, TPSH 2, 01 New Projects Temp, road.prproj, song.prproj) | VERIFIED |
| Other WKP folders on P: | `P:\01 Warrior King Productions\` (01 Audio Projects, 04 PodCast Zac's Film Odssey, 05 3d modeling, 06 Photo edits, 10 Sports Editing, Davinic Resolve, editing assets [Cap Cut, Davinvi, Filmorea, Permiere Pro], Logo, Steven Clip, Business) | VERIFIED |
| Publishing on P: | `P:\03 Warrior King Publishing`, `P:\Warrior King Productions` (empty) | VERIFIED (exist) |
| Old client and church work (archive) | `E:\01 Warrior King Productions Archive\` (02 Church Pod Cast, 03 CR Beer League, 04 New edits for pond5, 05 Coloring course, Beauty and the Beast, Father's Day Video, Mission Balitmore 2021, more) | VERIFIED (top level) |
| Old pictures and video | `E:\Pictures - Video` | VERIFIED (exists) |
| WWD (repo) | `D:\WKP\WWD\` | VERIFIED |
| Post-Production (repo) | `D:\WKP\Post-Production\` (CLAUDE.md, reports, writing-room) | VERIFIED |
| WKP Channel | `D:\WKP\WKP-CHANNEL\` | VERIFIED |
| RUBY TWO | `D:\WKP\Ruby-One\` (folder name on disk). `D:\WKP\RUBY-TWO` does NOT exist | VERIFIED (and the other name MISSING) |
| Shattered Empire canon | `D:\The Shaterred Empire Series` (misspelled on disk, 17 entries) and `D:\WKP\Shattered-Empire\` | VERIFIED |
| Stellar Dominion | `D:\Stellar Dominion` (9 entries), `D:\WKP\SCI-FI Novel\` | VERIFIED |
| Zac's writing | `L:\03 My writing` (35 entries), old copy `E:\03 My writing` | VERIFIED |
| Etsy art | `D:\04 New Warrior King Designs\` (27 entries; exports in `_Print Exports`) | VERIFIED |
| Kingdom Planners | `D:\05 Kingdom Planners` (8 entries) | VERIFIED |
| Cyber Security guides | `D:\WKP-Guides\` (17 entries) | VERIFIED |
| Transcription jobs | `D:\Transcription Jobs\` (client files, never commit) | VERIFIED |
| AI art | `L:\AI Art` | VERIFIED |
| Footage on D: | `D:\Video from 2026 Road Trip`, `D:\Vow renewal footage`, `D:\Utah Road Trip`, `D:\RazerCortexGameClips` | VERIFIED (exist, personal, not for jobs without Zac) |
| Adobe scratch | `D:\adobe scratch drive` | VERIFIED (exists). OFF LIMITS, Adobe is never touched |

## 7. 3D (Blender and Unreal)

| What | Path | Status |
|---|---|---|
| Animation department | `D:\WKP\ANIMATION\` (CLAUDE.md, STANDARDS.md, scripts, training) | VERIFIED |
| Blender | `C:\Blender\5.2.4\blender.exe` (28 entries in folder) | VERIFIED (folder; exe not run) |
| Blender projects | `D:\Blender Projects\` (empty 2026-11-17) | VERIFIED (0 entries) |
| Unreal Engine | `D:\Epic\UE_5.8` (8 entries) | VERIFIED |
| Unreal projects | `D:\Unreal Projects\` (empty 2026-11-17) | VERIFIED (0 entries) |
| Unreal shader cache | `D:\UE_DDC` (empty) | VERIFIED |
| 3D asset license log | `D:\WKP\data\assets\animation-asset-log.csv` | VERIFIED |
| Old 3D modeling | `P:\01 Warrior King Productions\05 3d modeling` | VERIFIED (exists) |

## 8. Scratch, deliverables, tools on D:

| What | Path | Status |
|---|---|---|
| Scratch (gitignored) | `D:\WKP\scratch\` (311 entries) | VERIFIED |
| Deliverables for Zac (.docx) | `D:\WKP Reports\<Deliverable Name>\<date> - <Name>.docx` (49 folders) | VERIFIED |
| Logs | `D:\WKP\logs\` | VERIFIED |
| Data drops | `D:\WKP\data\` and asset index `D:\WKP\data\assets\p-drive-index.csv` | VERIFIED |
| OpenMontage | `D:\Tools\OpenMontage` | VERIFIED |
| OpenWhispr | `D:\Tools\OpenWhispr` | VERIFIED |
| PC health | `D:\Tools\PCHealth` | VERIFIED |
| Voice Studio | `D:\Tools\Voice Studio` | VERIFIED |
| ffmpeg | `C:\Users\kingz\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe` (also on PATH) | NOT VERIFIED (from LOCAL-PATHS) |
| Python | `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe` | VERIFIED (ran the lookup script) |

## 9. Gaps and known problems

- P: file index is file level for P: only. L:, D: and E: have no file-level index yet. Building one is a media-manager task (read-only walk, writes only the CSV).
- Index has no date or hash. Re-run it when P: changes.
- Adobe SFX and most packs have no license file on disk. Treat "unknown" as not cleared for public use until `music` or `wwd-rights` says otherwise.
- Not verified: Premiere and Resolve install paths, plugin folders under Adobe, Lumetri preset folders, DaVinci Resolve LUT folder. Ask Zac or check on a live run.
- Folder spelling is wrong on disk in several places (Muisc, Premerir, Templets, Shaterred, Davinic, Desins). Use them exactly.
