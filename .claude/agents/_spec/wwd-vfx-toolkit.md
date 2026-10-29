# WWD VFX Toolkit (verified inventory)

Dated 2026-10-25. Built by wwd-vfx for wwd-director. Reference file, NOT an agent definition (no frontmatter on purpose).

How it was verified: directory listings (ls, find), the P:\ index CSV counted with Python, ffprobe on the WWD Kit pieces, exe file versions, the Windows uninstall registry list, `pip list`, `node -v`, `where ffmpeg`, and reading script docstrings. Anything not seen with my own tools is marked "not verified". I cannot hear audio or run the main-session connectors.

Machine: MAIN DESKTOP, Windows 11, NVIDIA GeForce RTX 5060 (8151 MiB, driver 616.92, seen via nvidia-smi).

## 0. Headline findings

- Saber is NOT installed (only the installer zip sits on P:\). Vibrance.aex (Windows AE plugin) is NOT installed. VCOrb is "installed" only inside a stub folder for After Effects 2020, which has no AfterFX.exe, so it is not usable in AE 2026.
- Premiere Pro 2026, After Effects 2026, Audition 2026, Media Encoder 2026, Photoshop 2026 (all v26.5 except Photoshop 27.9) and DaVinci Resolve 20.2 are installed. Illustrator is NOT installed.
- No Remotion packages found on disk (skill exists, runtime does not). No opencv, moviepy, pydub, librosa, imageio in Python. All kit scripts run on Pillow, numpy, scipy plus ffmpeg.
- Most alpha kit pieces exist only as ProRes .mov (pixel format yuva444p12le). ProRes freezes on Zac's machine, and only 5 of the 40 .mov pieces have an MP4 twin. See section 4.3.
- P:\ is large: about 59k files in the walked folders. The P:\ index CSV (27,207 rows) covers only media types and skips WWD Kit, Texture, Color Training, Podcast and every .aep/.psd/.ffx/.look/.jpg/.pdf/.zip.

## 1. Owned asset library on P:\

### 1.1 Counts

Index CSV (D:\WKP\data\assets\p-drive-index.csv, 27,207 rows, columns FullName, Extension, Length) by top-level folder:

| Folder | Rows in index | Size |
|---|---|---|
| Sounds | 15,752 | 23.59 GB |
| AE Templets | 10,947 | 39.71 GB |
| Stock Footage | 187 | 25.58 GB |
| Tools | 321 | 9.80 GB |

Index by extension: .wav 15,368; .png 10,178; .mov 613; .mp4 500; .mp3 485; .mogrt 41; .cube 17; .prfpset 3; .aif 2.

Direct file counts (find, all file types, includes .DS_Store and __MACOSX junk):

| Folder | Files | Main types |
|---|---|---|
| P:\Tools | 1,330 | 739 psd, 196 mp4, 73 mov, 50 ffx, 42 gif, 28 pdf, 17 cube, 14 look |
| P:\AE Templets | 35,247 | 22,744 jpg, 10,443 png, 529 mov, 302 ai, 296 tga, 206 aep, 172 mp4, 62 mp3 |
| P:\Stock Footage | 334 | 133 mp4, 74 hdr, 60 jpg, 48 mov |
| P:\Texture | 540 | 387 tif, 102 jpg, 13 png, 10 hdr |
| P:\Color Training | 1,111 | 352 dng, 212 mov, 151 mp4, 70 cube, 32 mxf, 31 drx, 17 prproj |
| P:\Podcast | 1 | files.zip |
| P:\Sounds | 16,410 | 15,696 wav, 438 mp3, 136 pkf (peak files), 69 pdf, 2 rar |
| P:\WWD Kit | 101 | 40 mov, 25 wav, 19 mp3, 9 png, 8 mp4 |

Other P:\ root folders I only saw by name, not walked: 01 Warrior King Productions (Audio Projects, Video Project, 3d modeling, Davinic Resolve, Logo, Sports Editing and more), 03 Warrior King Publishing, Pitch Templates, Warrior King Productions.

### 1.2 P:\Tools packs

Plugin column: "none" = plain footage/presets that work in Premiere or AE with no third-party plugin.

| Pack (folder) | What it is for | Files and types | Plugin needed |
|---|---|---|---|
| 16 Free Transitions | AE transitions project (CS6 era) | 1 .aep, 1 pdf | none seen (not opened) |
| Action Pack Lite - RocketStock | Action stock: Burn, Carnage (blood hits), Collapse, Detonate, Fume, Ignite, Mojave, Ricochet (muzzle flashes, gunsmoke), Vapor | 22 mp4, 3 png | none |
| Aspect_Ratio_Pack | Letterbox bar overlays 1.85, 2.35, 2.40, 2.55, 2.75, 3.0 | 6 png, tutorial mp4 | none |
| Camera overlays | CCTV, Drone, DSLR Viewfinder, Video Camera, Video Chat | 6 mov, 2 mp4 | none |
| EDITH_FL | Marvel-style EDITH glasses HUD AE project and renders | 4 aep, 6 mov, 5 png, 1 psd | not verified (aep not opened) |
| IRONMANHUD_FL | Iron Man style HUD AE project, renders (3D sphere, face, Thanos) | 7 aep, 5 mov | not verified |
| SYMBIOTE_FL | Venom symbiote Cinema 4D scene and vein textures | 1 .c4d, 10 png, 2 jpg | Cinema 4D (installed, see 2.1) |
| STRIKE 1.0 | Photoshop layered strike/slash packs | 232 psd, 21 gif | Photoshop (installed) |
| VILLIAN 01 RF | Photoshop layered villain pack | 250 psd, 21 gif | Photoshop |
| ZOOM 01 | Photoshop layered zoom pack | 252 psd | Photoshop |
| Free+Lava+Burst+Pack | 10 Lava Burst + 10 Green Slime Burst clips | 20 mov | none |
| Free+Stylized+Blood+Pack | Blood 1 to 10 stylized splashes | 10 mov | none |
| Logo revels | Logo Freebie, 3 versions x base and top layer | 6 mov | none |
| Mixkit | Mixkit Premiere templates (Screen Split Vertical, 250, 262, 403, 404, 405, Wedding Invitation) | 6 prproj, 3 mogrt, 6 mp4 | Premiere |
| Nebula Freebie | 19 nebula/planet backgrounds | 19 mp4 | none |
| Volumetric Freebie | 14 light beam clips + 2 dust | 16 mp4 | none |
| PB - Action Hits Toolkit | Dirt (13), Spark (17), Smoke (2), Fantasy (5), Muzzle Flashes (3), Fantasy/SciFi Hit Toolkit (31) | 68 mp4, 3 png | none |
| PB - Anamorphic Lens Flares | 17 flare overlays | 17 mp4 | none |
| PB - Free Camera Shake Presets | 15 presets x 1080p and 4K (24/35/50/85 mm light/medium/heavy, Zoom Crazy/Slam/Slower) | 30 ffx | After Effects (also Premiere via copy, not tested) |
| PB - Space Kit | Atmospheres (13), Nebulas (13), Starfields (21) | 26 mp4, 21 jpg | none |
| PB - 17 FREE LUTs | Wanderlust LUTs (Basin, Boulder, Butte, Everest, Hopkins, LochNess, Oaxaca, Oslo, Phoenix, Pocatello, Prague, Reykjavik, SantaFe, Seattle, Stillwater, Tahoe, Thames) | 17 cube | none (Lumetri) |
| PremiumBeat Hollywood Lumetri Looks | 14 .look files (Amelia, Dr Oddlove, Furiosa, Hogwash Express, Illinois Jones, Knife Jogger, Magnificent West, Maximus, May Tricks, O Mother, RagingMule, Saving Bryan, The_Mars_Man, Versus) | 14 look | Lumetri (Premiere/AE) |
| PremiumGrades | 20 grade presets (e.g. Tokyo Rainstorm, Brooklyn B&W, Arizona Oasis) | 20 ffx | After Effects |
| PremiumBeat Movie Marketing Templates | Movie poster and 4K trailer rating PSDs + fonts | 2 psd, 8 otf, 5 ttf, 3 zip | Photoshop |
| Movie Poster Template - StudioBinder | Poster PSD with Montserrat and Tall Dark and Handsome fonts, samples | 1 psd, 2 zip fonts | Photoshop |
| Photobacks Snow Globe Template | Snow globe PSD + Henny Penny font | 1 psd, 1 otf | Photoshop |
| Transitions | Transition 1 to 16 | 16 mp4 | none |
| LUTS | Ground Control free camera-to-Rec709 LUT zips (D-Log, S-Log3, V-Log, BMD Film, CineLike-D and more) | 12 zip (not unzipped) | none (Lumetri) |
| vhs-assets | VHS grain, static accent, 4x3 frames, VHS Presets | 2 mp4, 2 png, 1 prfpset | Premiere |
| assets | Glitch Footage 01, placeholder | 1 mp4, 1 png | none |
| Free Animated Icon Sets | 20 pre-rendered icons (arrows, check, clock, email, heart and more) + AE project | 20 mov, 1 aep | none for mov |
| add_mesh_walls | Blender add-on scripts (walls mesh) | 3 py, 3 pyc | Blender (installed is 2.93, add-on compatibility not tested) |
| Jarle's Deadpool Camera Shake Presets.prfpset | Premiere camera shake preset file (1.6 MB) | 1 prfpset | Premiere |
| fredoka-one.zip | Fredoka One font | zip | none |
| Vibrance.aex | Windows AE plugin file, NOT installed (see section 1.5) | 648 KB | itself |
| Vibrance64.plugin | Mac bundle, unusable on Windows | 4 files | Mac only |
| VCOrb_1.0.0_Installer_x64.exe | Video Copilot Orb installer (4 MB) | exe | AE |
| README_LicenseAgreement.pdf, Read Me.txt | licenses | | |

P:\ root loose files: Saber_1.0.40_Installer_Win_2022.1.zip (contains Saber_1.0.40_Installer_x64_2022.exe), LUTS.zip (17 cube files seen in zip listing, e.g. MB CINE V2, AOD Expired Film, Neo 90's Action Film), HORIZON - CINEMATIC SOUNDS.zip (258 entries: Braams/Alarms, Hits and Booms, Pulses/Pads/Percussion, Risers, Swooshes, Construction Kits; not unzipped), Budget & Schedule Templates.zip (Budget Template.xlsx, Work Back Schedule.xlsx, Budget Assumptions docx), skills for claude.docx.

### 1.3 P:\AE Templets

206 .aep files (auto-saves included), 38 .mogrt, 1 .prfpset (Screen Shake Annoyed Editor.prfpset), 2 .prproj. About 85 top-level template folders. Top-level folders (aep count in brackets where more than one):

(Footage), 117203489-basketball-ball-logo, 169698120-american-football-logo-reveal.zip, 60002-3 / 60008-1 (2) / 60008-2 After Effects Project, After Effects, After Effects Files, Amazing Beasts, Ancient Shatter Indent, Atmospheric Intro After Effects Files, Audio React Ring, Automotive Showcase, BATMAN INTRO TEMPLATE BY SLIPAXFX, Block Titles, Bright Logo Intro, CINEMATIC MOOD, Cinematic Title Bars, Cinematic Trailer, Circle Logo, Clean Logo Reveal, Dark Cloud Environment, Dark Display, Dreamy logo, Egyptian Thrones, Epic Title Plates, Epic text in the heavens (2), Fantasy Credit Sequence Template 1 / 3 / 4, Fight Steel, Fly through clouds (2), Fonts, Future Grid Opener, Game Trailer, Glitch Logo (2), Groundbreaking, Grunge Highlights, Hammer Reveal, Heartbeat Trailer, Hi_tech Trailer, Logo Glitch, Luxury intro (2), Metal Edge, Movie Promo, Nature Slide FX, Photos Logo, Pre - Rendered Files, Project_10 (3), Quick Logo, Quick Titles, Reveal Titles, Science, Shades of Red, Sigil Logo Reveal, Social Media, Spooky Smoke Intro, Sports Card, Storm, The Game Channel Intro (2), The History Ident (2), The Storm, The-Order (3), Thriller, Transform the Grunge, Valentines-Day-Heart (3), Video Presentation Pro, Viking, Vintage Film Slide, Wall Collapse, Water Colors, Winter is here, Zoomness, whiteout, union-logo, ae-template-bright-logo-intro_zyvksp3x (2), after-effects-cs4-template-action-trailer_7kgILs1r (104 aep, 17,090 files, the biggest), after-effects-cs4-template-hi-tech-trailer_m1F3Dskr (2), business-corporate-digital-timeline-presentation-commercial-opener-modern-slideshow-intro-promo-display_HV_G3FbZe, sweet-memories-slideshow_HRVhDZUw, the-last-blood-titles-trailer-cinematic-opener-intro-abstract-particles-promo-modern_SPZdok1el (2), videoblocks-73-maps-and-geo-icons, videoblocks-dark-cinematic-title-intro, videoblocks-epic-particles-trailer, videoblocks-fire-and-crome-logo-fcpx (0 aep, FCPX), videoblocks-flicker-modern-corporate, videoblocks-night-of-horror-after-effects-template, videoblocks-premiere-pro-glitch-opener-vhs (0 aep, Premiere), videoblocks-short-modern-promo, videoblocks-simple-flash-logo, videoblocks-super-hero-logo-intro, videoblocks-youtuber-subscriber-pack (0 aep, mogrt/Premiere). Also loose: Preview.mp4, Sample.mp4, Readme.pdf, 7.png, SonduckLogo.png.

Third-party plugin dependency of the templates: I scanned the 206 .aep files for plugin name strings. Heuristic only (binary string search, can false-positive), not a confirmed dependency list: Optical Flares strings in 5 folders (Fly through clouds, Metal Edge, Quick Titles, The Storm, action-trailer); Trapcode Particular in 2 (Thriller, action-trailer); Red Giant/Magic Bullet/Universe in 5 (BATMAN INTRO, Egyptian Thrones, Science, The History Ident, action-trailer); a loose "BCC" string match in 23 folders (likely over-matching, not trusted). None of Optical Flares or Trapcode is installed here (see 2.3). So some templates may open with missing-effect warnings. Not tested by opening any.

Premiere motion graphics templates, installed (not on P:): C:\Users\kingz\AppData\Roaming\Adobe\Common\Motion Graphics Templates has 449 .mogrt files. Biggest groups by filename: FOUR Editors Title (71), 80's Film (20), TikTok (18), Youtube (16), Cinematic (15), Snapchat (10), Modern Text Animation (16 incl. RGB_), Corporate Lower Thirds (8), Callout (8), plus many Lower Third styles and Facebook/Instagram/X reveal and subscribe bars. P:\AE Templets also holds 38 "Like & Subscribe 1 to 19" .mogrt (two copies of 19).

### 1.4 Stock, textures, color training, podcast, sounds

| Folder | Content seen |
|---|---|
| P:\Stock Footage root | about 100 loose clips (133 mp4, 48 mov total in tree): aerials, castles, roller coasters, timelapse, space flights, fog, lightning, snow, fire balls, graveyard, police, alien eyes, glitch, Smoke_Loop.mov, rain alpha. Names ending __D are Videoblocks style downloads |
| Blood mist | 7 files: blood mist front.avi, side.avi, side2.avi (+ .sfk), Blood_Burst_10.mov |
| Green Screen | 8: Christmas TV studio sets (3), news TV studio sets (3), news-headline.mov, sports-studio-set.mov |
| HDI | 78 files: HDR environment maps (balcony, cave_wall and more) at 256p to 16k |
| Pictures | 63 stock stills (jpg/png) |
| Spark by RocketStock | 65 mp4 (Spark_1 and up) + license pdfs |
| P:\Texture | 540 files: 12_Seamless_Rock_Textures, Galaxy Pictures, Hdls, Pixar128 Library, TexturesCom (rock, wood, gravel, flames, fireworks, grunge, metal) 387 tif, 102 jpg |
| P:\Color Training | DaVinci Resolve training: 02_Cameras to 99_Bonus, NAB Resolve 16, 352 dng, 70 cube, 31 drx stills, Resolve 16 PDFs, .dra archives |
| P:\Podcast | files.zip only (TheLongGame pitch deck/script PDFs, STATIC podcast proposal) |
| P:\Sounds\Sound FX | 10,419 indexed rows. 179 loose files (mp3 and 5 YTDown mp4) + folders: Adobe (library, below), 15 Free Ambient Sound Effects (17), PB - Footstep SFX (46), PB - Sci-Fi UI Free SFX (32), Trailer_Construction_Lite_Version (21) |
| P:\Sounds\Music | 5,872 files: 5,646 under Music\adobe (genre folders such as Ambient, Blues, Classical&Orchestral, Corporate 15, Country, Disco, Funk&Rock, General 15; subfolders not all walked), 7 under Spanish, plus about 200 loose tracks (Videoblocks and BBC style names). Music is for intro and outro only per WWD rules |
| P:\Sounds rar files | FEP_ES_FoleySound.rar (1.08 GB), FEP_ES_SoundDesign.rar (38 MB), not extracted, contents not verified. Loose 02-twista-american_gangsta.mp3 (a commercial song, do not use) |

Adobe SFX library category folders under P:\Sounds\Sound FX\Adobe (file counts include any .pkf peak files):
Ambience_1 106; Ambience_2 99; Animals 181; Cartoon 286; Crashes 299; DC 10; DTMF 30; Drones 113; Emergency Effects 186; Fire and Explosions 137; Foley Footsteps 301; Foley 532; Horror 246; Household 608; Human Elements 533; Imaging Elements 149; Impacts 636; Industry 444; Liquid-Water 298; Multichannel 7; Multimedia 1,357; Noise 37; Production Elements 1,462; Science Fiction 283; Sports 338; Technology 280; Tests 6; Tones 57; Transportation 521; Underwater 114; Weapons 468; Weather 74.

Provenance warning: files named YTDown.com_YouTube_* (5 mp4 in Sound FX, 1 in Stock Footage) are YouTube downloads and several Music files look like commercial tracks. Zac says P:\ is everything he owns, but license for those items is not verified. Prefer the Adobe, PB, RocketStock, Videoblocks/Audioblocks-style named files.

### 1.5 Plugin dependency check

| Pack | Needs | Installed on this machine |
|---|---|---|
| Saber (P:\ root zip) | Video Copilot Saber, AE | NO. Only the installer zip is on P:\. No Saber file found in any Adobe folder |
| Vibrance.aex (P:\Tools) | Windows AE plugin | NO. Not in AE 2026 Plug-ins. (Adobe's built-in VariableVibrance.aex is a different effect.) Vibrance64.plugin is Mac only |
| VCOrb installer | Video Copilot Orb, AE | PARTIAL. VCOrb.aex exists only at C:\Program Files\Adobe\Adobe After Effects 2020\Support Files\Plug-ins\VideoCopilot\. The AE 2020 folder holds nothing else (no AfterFX.exe), so AE 2020 is not installed and VCOrb is not loaded by AE 2026. Copying it into AE 2026 was not tested |
| AE templates using Optical Flares or Trapcode Particular | Red Giant/Maxon Trapcode, Video Copilot Optical Flares | NO. Neither found in any Adobe plug-in folder or registry list |
| Element 3D | Video Copilot Element | NO. Not found |
| Sapphire, BorisFX, FilmConvert, Twixtor | Boris FX, FilmConvert, RE:Vision | NO. Not found in any scanned folder or registry |
| Magic Bullet Suite, Magic Bullet Looks, Neutrino | Red Giant (Maxon) | Registered as installed (Magic Bullet Suite x3, no version shown) and present at C:\Program Files\Red Giant\ (Magic Bullet runtimes 5.0, 24 LUTs, Looks presets, Neutrino 1.4 runtime). I found no host plugin files in the Adobe plug-in folders, so whether they appear in Premiere/AE: not verified |
| PB Camera Shake .ffx, PremiumGrades .ffx | After Effects | Yes, AE 2026 installed. Not opened to test |
| Hollywood Lumetri .look, .cube LUTs | Lumetri | Yes, built into Premiere and AE (Lumetri.aex, ApplyColorLUT.aex, LUTTransform.aex present) |
| Mixkit .prproj / .mogrt | Premiere | Yes. Not opened to test |
| EDITH_FL, IRONMANHUD_FL .aep | AE, plugins not verified | AE yes. Third-party needs not verified |
| SYMBIOTE_FL .c4d | Cinema 4D | Yes (2023 to 2026 and older, see 2.1) |
| STRIKE, VILLIAN, ZOOM PSDs, poster templates | Photoshop | Yes, Photoshop 2026 (27.9) |
| add_mesh_walls | Blender | Blender 2.93 only. Add-on compatibility not verified |

## 2. Software and plugins on this machine

### 2.1 Installed software (file version or registry DisplayVersion)

| Tool | Version seen | Path |
|---|---|---|
| Premiere Pro 2026 | 26.5.0 (exe 26.5.0.99) | C:\Program Files\Adobe\Adobe Premiere Pro 2026 |
| After Effects 2026 | 26.5 | C:\Program Files\Adobe\Adobe After Effects 2026 |
| After Effects 2020 | folder is a stub only (plug-in folder, no AfterFX.exe). Prefs for AE 17.0 still in AppData | C:\Program Files\Adobe\Adobe After Effects 2020 |
| Audition 2026 | 26.5.0 | C:\Program Files\Adobe\Adobe Audition 2026 |
| Media Encoder 2026 | 26.5.0 | C:\Program Files\Adobe\Adobe Media Encoder 2026 |
| Photoshop 2026 | 27.9 | C:\Program Files\Adobe\Adobe Photoshop 2026 (Photoshop 2021 folder exists, no exe) |
| Illustrator | NOT installed (only old settings folders in AppData) | n/a |
| Acrobat | 26.002.22031 | C:\Program Files (x86)\Adobe\Acrobat DC |
| Adobe Creative Cloud | 6.10.0.252 | |
| DaVinci Resolve | 20.2.3.6 (registry 20.2.30006), Blackmagic RAW 5.1 | C:\Program Files\Blackmagic Design\DaVinci Resolve |
| Cinema 4D | 2026.3.1, 2025.3.3, 2024, 2023, S22, R25, R21 | C:\Program Files\Maxon Cinema 4D <year> (2026 folder has Cinema 4D.exe and c4dpy.exe) |
| Blender | 2.93 (old) | C:\Program Files\Blender Foundation\Blender 2.93 |
| Red Giant | Magic Bullet Suite, Magic Bullet Looks, Neutrino 1.4 | C:\Program Files\Red Giant |
| OBS Studio | exe says 29.1.3, registry says 28.0.1 (mismatch, unresolved) | C:\Program Files\obs-studio |
| VLC | 3.0.23 | |
| Final Draft | 11.0.2.57 | |
| ffmpeg and ffprobe | 9.0-full_build-www.gyan.dev | C:\Users\kingz\AppData\Local\Microsoft\WinGet\Links\ (found by `where`) |
| Node.js / npm | v24.19.0 / 11.17.0 | global npm only has @anthropic-ai/claude-code |
| Python | 3.12.10 | C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe |

### 2.2 Python packages (pip list)

Present: Pillow 12.3.0, numpy 2.5.1, scipy 1.18.0, matplotlib 3.11.1, av (PyAV) 18.0.0, fonttools 4.63.0, pandas 3.0.5, pyarrow 25.0.1, python-docx 1.2.0, openpyxl 3.1.5, requests 2.34.2, scikit-learn 1.9.0, torch 2.11.0+cu128, torchaudio, torchvision, torchcodec 0.7.0 (broken here per memory), transformers 4.57.6, faster-whisper 1.2.1, whisperx 3.8.6, pyannote-audio 4.0.7.
Absent (searched, no match): opencv, moviepy, pydub, librosa, imageio, numba, pygame, skia, pycairo. Fonts used by scripts exist: C:\Windows\Fonts\impact.ttf, consolab.ttf, georgiab.ttf.
Remotion: no package folder found under D:\WKP or C:\Users\kingz (depth 4) and no package.json under D:\WKP (depth 3). Treated as not installed.

### 2.3 After Effects and Premiere plugins

- AE 2026 Plug-ins\Effects: 232 entries, all Adobe built-ins plus bundled partners: CycoreFXHD (CC Cycore effects, e.g. BurnFilm, Bubbles, BallAction), Keylight, mochaAE (Boris mocha), Cineware by Maxon (Cineware_AE_Effect, LiveLink, SceneLayer, Exporter), Film Stocks, Particle_Playground, Lightning, Shatter, Lens_Flare, Glow, Turbulent Displace, VR effects, Cryptomatte, Curl_Noise, 3D Camera Tracker, Lumetri. No Saber, Element, Optical Flares, Trapcode, Sapphire, BCC, or Video Copilot file. Extensions folder: Anywhere2, CEPManager, LocalizePresets, Renoir. AE Scripts folder has the stock Adobe scripts only.
- Premiere 2026 PlugIns\Common: FilmImpact folder with 110 .prm effects and transitions (3D Blinds, Cross Zoom, Film Dissolve, Glitch, Light Leaks, Whip, TV Power, VHS Damage, Wonder Glow, Zoom Blur and more), OpenEXR, Wraptor, VST3. That these are the "Modern transitions" in the Premiere Effects panel: not verified.
- No separate Premiere plug-in folder with third party items; C:\Program Files\Adobe\Common\Plug-ins\7.0\MediaCore holds only dummy.txt.
- Installed Premiere items in user profile: 449 mogrt (section 1.3). Roaming\Adobe\Common\LUTs\Technical has 0 files. No user Premiere preset files found under Documents\Adobe (folder does not exist).

### 2.4 Existing WWD After Effects and VFX files on L:

L:\Winter Wolfs Den review show\After Effects\ :
- burning logo.aep: 541,070 bytes, last written 2023-10-10 23:53. Read as binary strings (not opened in AE): built only from Adobe built-in effects (Fractal Noise, Turbulent Displace, Displacement Map, Glow, Tritone, Set Matte, Shift Channels, Solid Composite, Hue/Saturation, Easy Levels, Box and Gaussian Blur, Noise, Unsharp Mask, Invert, Geometry/Transform) plus CC Burn Film, CC Composite, CC Wide Time (Cycore). Layer or comp names seen: Embers, Fire Edge, Burn, "burn obj", "Darken Burn / Trans Matte". One footage reference: logo.png (from the older E:\ WWD Pictures folder). No third-party plugin strings seen, so it should open on this machine. Companion renders in the VFX folder: burning logo.mp4 (h264 1920x1080 24 fps, 5.0 s, with AAC audio stream) and burn with sound.mp4 (1920x1080, 3.65 s, AAC). Folder burning logo_AME holds tmpAEtoAMEProject-main comp.aep.
- Also there: Countdown.aep (144 KB, 2023-03-04) + Countdown_AME, breaking cards.aep (1.39 MB, 2023-05-16) + auto-saves, 078891681-breaking-news (+ zip, 116 MB), Christmas-lights-animation-by-rizatgraphics, TUT_SNOW_PARTICLES_01.

L:\Winter Wolfs Den review show\VFX\ (listing, 2023 to 2025 files): 321188048_5722990954464217_6549569409197845948_n.mp4, A few moments later.mp4, All Time Gross.mp4, Assult mode video.mp4 (+ png), Fail Vid Cut up.mp4, Final Thoughts.mp4 (+ png), Gran Turismo official trailer mp4, Hit that subscribe button.mp4, Issue a challenge.mp4, Knockout of the Day.mp4, Master Logo 2.mp4, Notification Bell.mp4, Opening Salvo.png, Out Like a Boss.mp4, Resillient Bastard.mp4, Secert Invastion logo.mp4, Showmeta.png / showmeta.mp4, Spoilers alert.mp4, spolier.mp4, Wise Words.mp4, Wizard world give away.mp4, artility.mp4, burn with sound.mp4, burning logo.mp4, countdown - openning 2_1.mp4 (260 MB), countdown - openning 3.mp4 (196 MB), rotaing coutdown for OBS.mp4 (641 MB), rotating logo.mp4, end.mp4, end for facebook Shorts.mp4, intell full.mp4, mission faild.mp4, Subscribe Button + Notification Bell (CT and CT al .mp4 + Alpha Channel folder), FILM+CRUX+Glitch+Transitions+Vol.+1 (folder), videohive-HHPfL9tV-awards-show-package (zip 955 MB + folder + license pdf/txt), DraftNight, WWSS, videoplayback (1) to (3).mp4. Contents of folders not walked. The Gran Turismo trailer is third-party footage, not an owned asset.

## 3. AI and connector tools (MAIN SESSION ONLY)

wwd-vfx has no generation tool and cannot call any item in this section. For any of these, WRITE THE REQUEST (tool, prompt, settings, reference file paths, expected output name) and return it to wwd-director so Jarvis can run it. Always say plainly that nobody can test a prompt without spending credits, and offer a cheap model, shortest duration, lowest resolution test first, or a code-built alternative.

| Tool | What it does | Who pays / cost | Status I could confirm |
|---|---|---|---|
| Adobe Firefly video (Generate video panel) | Models on Zac's panel (screenshot 2026-10-25, memory\topics\firefly-models.md): Adobe Firefly Video; Veo 3.1, Veo 3.1 Fast, Veo 3.1 Lite; Gemini Omni Flash; Kling 3.0, Kling 3.0 Omni, Kling 2.5 Turbo; Runway Gen-4.5; Luma Ray3.14, Ray3.14 HDR, Ray3, Ray3 HDR, Ray2. Settings: Model, Resolution, Aspect ratio, FPS, Duration, Audio; References > Frames (start frame upload); Advanced > Seed | Matt paid the extra credits. Per-generation credit cost by model: not verified | Menu is from Zac's photo, not from a live session. Which models accept an end frame: not verified, check the panel |
| Adobe for creativity connector (plugin adobe-for-creativity) | 15 skills found in the synced plugin folder: adobe (tour), adobe-anydocx, adobe-anyexcel, adobe-anypdf, adobe-anypptx, adobe-batch-edit-photos, adobe-create-pdfs-from-data, adobe-create-social-variations, adobe-design-from-template (Adobe Express templates), adobe-design-to-pdf, adobe-document-review, adobe-edit-quick-cut (highlight cut), adobe-fonts, adobe-resize-photos-and-videos, adobe-retouch-portraits | Cost or plan: not verified. Memory notes Adobe batch tools cap around 20 files and cannot auto-upload local files | Skill files exist at C:\Users\kingz\.claude\plugins\synced\<id>\adobe-for-creativity\skills\. Older copies sit in plugins\.trash and are not live. Not repo-level: none found under D:\WKP\.claude |
| Higgsfield MCP (claude.ai Higgsfield) | generate_image, generate_video, generate_audio, generate_3d, upscale, reframe, remove_background, relight, motion_control, presets, character sheets, AI Influencer | TASKS.md (checked 2026-09-14): balance 0 credits, free plan; no one-time packs; PLUS $49/mo (1,000 credits), ULTRA $129/mo (3,000), 3-day free trial 100 credits auto-renews to $49/mo. Current balance: NOT VERIFIED | Tool is listed in the session MCP instructions. Not called by me |
| ElevenLabs (claude.ai ElevenLabs) | creative_generate_image, creative_generate_video, creative_generate_speech, creative_edit_image, creative_transcribe_audio, creative_design_voice, creative_save_designed_voice, creative_list_voices, flows (creative_generate_in_flow), file upload for local assets | The session instructions say generation spends the user's credits. Plan, balance and per-item prices: not verified | Listed in session MCP instructions. Not called by me. Do not repeat a generation call to retry (second charge) |
| VidIQ | Skill wwd-vidiq-pull uses a 150 credit per month budget (resets the 11th); weekly pull costs 25. Generation tools exist and are FORBIDDEN in that job: vidiq_generate_thumbnail 22, vidiq_refine_thumbnail 22, vidiq_generate_music 25, vidiq_generate_video (expensive), vidiq_video_watch 25, vidiq_generate_clips 9 per minute, vidiq_compose, vidiq_voiceover_generate | VidIQ subscription, credits as above; who pays: not verified | Costs read from D:\WKP\.claude\skills\wwd-vidiq-pull\SKILL.md, not from the live tool |
| OpusClip | Clip extraction for Shorts/Reels. Zac's spec: WinterWolfsDen_OpusClip_Prompts_v1.docx on L:, "Opus Clip Prompt System v2.1" in WWD\CLAUDE.md. Shorts are now mostly built locally by wwd-review-pipeline shorts-factory.md and build_short.py | Cost: not verified | Whether an OpusClip connector is available this session: not verified |
| Canva | Only found: skill canva-creator (small-business plugin), which makes Canva social-post designs and stages HubSpot sends from an approved brief. It is a campaign tool, not a general video or motion tool | Plan: not verified | Skill file exists in the synced plugin folder. A live Canva connector this session: not verified |
| Suno | Music generation. No tool in this setup: Zac generates by hand (run sheets carry Suno prompts). Music is intro and outro only | Zac's own account, plan not verified | No Suno skill or connector found |
| Remotion | Skill remotion-motion-graphics exists at D:\WKP\.claude\skills\remotion-motion-graphics (SKILL.md, references\design-rules.md, references\motion-patterns.md, assets\theme.ts). Free React-to-video renderer | Free software. NOT installed: no remotion packages found, Node 24.19 and npm 11.17 are present so it could be installed with npm | Skill only, runtime not verified |

Other repo skills useful to the bench: wwd-review-photo-pull (kit scripts, sticker kit, run sheets, premiere-transitions.md), wwd-review-pipeline (shorts-factory.md, build_short.py, check_clip.py, word_times.py), wwd-broll-prep, wwd-audio-cut, wwd-video-transcriber, wwd-frostcast-chapters, no-ai-slop.

## 4. Existing Python kit scripts

Folder: D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\ (13 scripts, dated 2026-10-17 to 2026-10-25). All output 1920x1080. Descriptions are from each script's docstring and header.

### 4.1 Scripts

| Script | Renders | Outputs seen in P:\WWD Kit |
|---|---|---|
| make_arcade_kit.py | Street Fighter style arcade kit with original look: round cards (--only round), versus screen, health-bar tag stills and animated hit clips, combo counter, Continue card (--title, --sub, --name for any show), fireball, Watch Again | Street Fighter\: Round 1-3, Versus, Tags 1/2/3 PNG, Tags Intro, Hit - KingZ, Hit - Winter Wolf, Both Full Flash, Combo Counter, Continue - Clayface, Continue - Crystal Lake, Fireball, Watch Again. Title - Street Fighter.png origin not verified |
| make_pixel_fight.py | Two original 8-bit fighters trading blows on a 240x135 grid scaled up, transparent, hit sounds baked in | Street Fighter\Pixel Fight.mov |
| make_next_up.py | NEXT UP: TITLE end card, Impact type on black with scanlines, punch sound baked in | Cards\Next Up - Street Fighter.mov, Crystal Lake\Next Up - Vision Quest.mov (assumed from the script's job; run args not verified). Vision Quest\Next Up - Clayface (.mov and MP4) script: not verified |
| make_vq34_next_up.py | NEXT UP card drawn as an old computer monitor (green text, owned beep sounds), plus MP4 copy | Cards\Next Up - Vision Quest 3 and 4.mov and (MP4).mp4 |
| make_stickers.py | Reusable sticker kit: Wolfie Award Nominee (trophy plus fanfare) and rubber stamps Recommend Watch, Save Yourself the Time, Dumpster Fire, each with sound baked in and a PNG still | Stickers\ 4 mov + 4 png |
| make_blood_pour.py | Blood pour transition: sheet pours down, covers frame, slides off with drips, splash baked in. Cut on the printed cover frame | Transitions\Blood Pour.mov (1.8 s) |
| make_wk_kit_cl_vq.py | Crystal Lake and Vision Quest kit (--only cl_spoiler, cl_weird, vq_boot, vq_tags, vq_counter, vq_spoiler): Spoiler Alerts, That Was Weird, Weird Good, System Boot panel, five AI Tags, three Wrong Name Counters | Crystal Lake\ Spoiler Alert, That Was Weird, Weird Good. Vision Quest\ System Boot, Spoiler Alert, AI Tag DUM-E/EDITH/FRIDAY/JARVIS/U, Wrong Name Counter 1 Kevin, 2 David, 3 Dave |
| make_vq_cyberspace.py | Vision Quest opener v2: System Boot panel opens into a cyberspace world (neon grid, data towers, binary rain, VISIONQUEST title, flash out), 10 s | Vision Quest\System Boot - Cyberspace.mov |
| make_vq_firefly_opener.py | Vision Quest opener from Zac's Firefly boot and world clips with its own VISIONQUEST title (Firefly garbled the title), beeps, sweep, whoosh, flash out, 11.5 s | Vision Quest\Opener - Firefly.mov and (MP4).mp4 |
| make_cl_opening.py | Crystal Lake opening Option 1, fully code-built: night lake, canoe, poster erupts and drags girl under, 19.0 s | Crystal Lake\Opening - Lake Scare (Option 1).mov/.mp4 |
| make_cl_opening_firefly.py | Crystal Lake opening Option 2: Zac's five Firefly plates with the real poster composited on top, 19.0 s (imports helpers from make_cl_opening.py) | Crystal Lake\Opening - Lake Scare (Option 2 Firefly).mov/.mp4 |
| make_clayface_intro.py | Clayface silent intro, 15.5 s: push on premiere still, melt to clay, cracked face, red flash, poster slam. Needs the USE folder path and out path as args. Silent H.264 MP4 | Clayface\Clayface Intro - Silent (MP4).mp4 |
| make_clayface_logo_melt.py | Clayface logo sting: WWD logo PNG turns to brown clay, ripples, melts and drips off, 5 s, 24 fps, code-built, no credits. Writes a silent MP4 and a "(with sound)" MP4 with owned mud sounds | Clayface\Clayface Logo Melt.mp4 and (with sound).mp4. Clayface Logo - Brown Start Frame.png origin not verified |

Shared: make_arcade_kit.py is the helper module (W, H, FPS, blank, put, ease_out, render, flash) that make_wk_kit_cl_vq, make_vq_cyberspace, make_vq_firefly_opener, make_vq34_next_up and make_pixel_fight import. Sounds always load from P:\Sounds\Sound FX and the scripts assert the files exist. Rebuilding a piece overwrites it, so write to a new filename for anything Zac already used.

### 4.2 P:\WWD Kit inventory (ffprobe, 2026-10-25)

All 1920x1080. "Alpha" = ProRes pixel format yuva444p12le, meaning an alpha channel is in the file format. I did not pull frames to see transparent areas for this inventory.

- Cards\ : Next Up - Street Fighter.mov (4 s, ProRes 422, opaque, audio); Next Up - Vision Quest 3 and 4.mov (6 s) and (MP4).mp4 (6 s, h264, aac).
- Clayface\ : Clayface Intro - Silent (MP4).mp4 (15.5 s, no audio); Clayface Logo Melt.mp4 (5 s, no audio); Clayface Logo Melt (with sound).mp4 (5 s, aac); Clayface Logo - Brown Start Frame.png; Sounds\ (22 files: wet mud, squish, skin peel, body hit wet, rumble, whoosh, fire, splat).
- Crystal Lake\ : Spoiler Alert.mov (3.2 s alpha); That Was Weird.mov (2.8 s alpha); Weird Good.mov (2.8 s alpha); Next Up - Vision Quest.mov (4 s opaque); Opening Option 1 .mov and .mp4 (19 s); Opening Option 2 Firefly .mov and .mp4 (19 s); Sounds\ (11 files: water ambience, splashes, screams, hit thud, cymbal stab, underwater explosion).
- Stickers\ : Wolfie Award Nominee.mov (6 s alpha), Recommend Watch.mov, Save Yourself the Time.mov, Dumpster Fire.mov (4 s alpha each), each with a matching .png.
- Street Fighter\ : Round 1, 2, 3 (2.2 s alpha); Versus (3 s alpha); Tags Intro (1 s); Hit - KingZ (12-27) and Hit - Winter Wolf (15-17) (1.2 s); Both Full Flash (03-32) (1.2 s); Combo Counter (10 s); Fireball (1 s); Pixel Fight (4 s); Watch Again (3 s); Continue - Clayface and Continue - Crystal Lake (8 s opaque); Tags 1/2/3 PNG and Title - Street Fighter.png; Sounds\ (16 files).
- Transitions\ : Blood Pour.mov (1.8 s alpha).
- Vision Quest\ : AI Tag x5 (3.6 s alpha); Wrong Name Counter 1 to 3 (3.6 s alpha); Spoiler Alert.mov (3.2 s alpha); System Boot.mov (5 s alpha); System Boot - Cyberspace.mov (10 s alpha); Opener - Firefly .mov and (MP4).mp4 (11.5 s); Next Up - Clayface .mov and (MP4).mp4 (8 s).
- All .mov files have a pcm_s16le audio stream, so every piece ships with its sound baked in. I could not listen to any of it.

### 4.3 Gap flagged

ProRes freezes on Zac's machine (root rule: MP4 is the safe copy). Pieces with an MP4 twin: Next Up Vision Quest 3 and 4, Opening Option 1, Opening Option 2, Opener - Firefly, Next Up - Clayface (Vision Quest), plus the MP4-only Clayface intro and logo melt. About 35 .mov pieces (all stickers, Street Fighter pieces, Crystal Lake and Vision Quest tags, counters, Blood Pour) have NO MP4 copy. Alpha pieces cannot go to plain H.264 without a fill, so a safe-format answer needs a decision (for example WebM/VP9 alpha, PNG sequence, or a ProRes 4444 fix); I have not tested any of these. Flag for wwd-director.

## 5. Not verified

- Current Higgsfield credit balance and plan (last known 0, free plan, 2026-09-14 per TASKS.md).
- ElevenLabs, VidIQ, OpusClip, Canva, Adobe connector: plans, balances, per-generation prices, and whether each connector is live this session.
- Which Firefly models accept an end frame; credits per model; the menu comes from Zac's screenshot only.
- Whether Magic Bullet Suite / Looks / Neutrino appear as effects inside Premiere 2026 or AE 2026.
- Whether Optical Flares, Trapcode Particular or any other third-party plugin is needed by any given P:\AE Templets project (string scan only; no template opened in AE).
- Whether EDITH_FL, IRONMANHUD_FL, 16 Free Transitions and the other P:\Tools .aep files open cleanly in AE 2026.
- Whether the PB .ffx and Deadpool .prfpset presets load in Premiere 2026.
- Whether Premiere's FilmImpact set equals the Effects panel "Modern transitions".
- Contents of Music\adobe subfolders, the two Sounds .rar files, HORIZON, LUTS.zip (full), and Ground Control LUT zips beyond the listing above.
- License provenance of YTDown.com_YouTube_* files, loose commercial music tracks, and the Gran Turismo trailer on L:\...\VFX.
- Which args made Cards\Next Up - Street Fighter, Crystal Lake\Next Up - Vision Quest and Vision Quest\Next Up - Clayface, and the origin of Clayface Logo - Brown Start Frame.png and Title - Street Fighter.png.
- Alpha channel content (transparent regions) of every WWD Kit .mov; only the pixel format was probed.
- Whether VCOrb.aex works if copied into AE 2026 (not tested, not attempted).
- Mac-only Vibrance64.plugin has no use here.
- Audio quality of anything, including the baked-in sounds (I cannot hear audio).
- OBS version (exe 29.1.3 vs registry 28.0.1).
- Contents of P:\01 Warrior King Productions and sibling P:\ root folders; folders inside L:\...\VFX such as WWSS and DraftNight.
