# WWD Color Reference (what the owned color material is)

Dated 2026-10-25. Reference file, NOT an agent definition. Written by wwd-director for wwd-color. Source: directory walks of P:\Color Training, P:\Tools, P:\LUTS.zip (zip listing only, nothing extracted). I did not open any .dra project, play any .mov, or read the PDFs, so what each folder "teaches" is inferred from folder names, file names and file types. Anything not seen is marked.

Resolve Color Training is a DaVinci Resolve 16 era course (NAB Resolve 16, Qazi style). Zac's Resolve is the FREE version, confirmed 2026-10-25.

## P:\Color Training

| Folder | What is in it | What it teaches (inferred from names) |
|---|---|---|
| 02_Cameras | 02_Cameras.dra project; Canon LUTs (2 cube: Canon Log2 and Log3 to BT709); zzCamera LUTs and a duplicate zzFCM_Camera LUTs: Arri (.dat), BMPCC4K, Canon, DJI (4 cube), Panasonic (V-Log to V-709), RED (IPP2 Rec709), Sony (4 S-Log3 cube), Technicolor CineStyle; zzLUT location.png | Turning log camera footage into Rec709 with a camera LUT. Useful as a technical (camera to display) LUT bank, not as a look |
| 03_Color_Correction | 03_Color Correction.dra project only | Primary correction: exposure, white balance, contrast, saturation order. Project not opened |
| 04_Shot_Matching | 04_Shot_Matching.dra, U-SONY-S-LOG2-V3-LTR.cube, theqazman_nodes_1.8.1 (.dpx and .drx) | Matching shots to each other. The .drx is a Resolve grade stills file (a node tree), not loadable in Premiere. Not parsed |
| 05_Color_Grading | 05_Color_Grading.dra; Reference Stills with Movies, Commercials, Music Videos (jpg plus .drx pairs, 26 .drx across the course) | Look building. Movie stills are named for the films they come from (Sicario, Atomic Blonde, La La Land among them), so these are grade targets to study. They are studio frames, use as reference only, never ship |
| 06_Studio_Setup | LG OLED calibration PDFs, a Resolve keyboard shortcut text file, a Stream Deck profile | Monitor and room setup. Relevant to the caution that Zac's screen differs from anyone else's |
| 07_Freelance | 2019 and 2020 Color Reel .mov | Instructor reels. Show what finished work looks like. Not played |
| 91_YouTube | 6 .dra projects: Grading YOUR Footage Planet X, How to Grade a Wedding Video, How to get the Joker look Part 1, James Bond look, John Wick look, Commercial vs Film Grading | Look recipes tied to specific films. Study the approach, do not copy a look |
| 99_Bonus | The Most Profitable Color Grading Training.dra with 8-bit footage.mov, Clean White.mov, Creamy Film Look.mov, Scopes.mov | Business and workflow tips, scopes, a film look demo. Not played |
| Conform Pt3 | XXIO 2020 color trace and pre-conformed EDL projects, an EDL, "xxio 90 to color.mov" | Conform (moving an edit from the edit app to Resolve). Not needed for WWD |
| NAB Resolve 16, Next To You, Life on the Line, XXIO_2020 | Course projects with camera original footage (Chicago, Chinatown, Graffiti, Hotel Lobby clips) | Practice footage for the course. Next To You has Color, Music and a Premiere Pro Project folder |
| 10_XXIO_2020.dra.zip and other .dra.zip | Zipped copies of course projects | Duplicates |
| DaVinci-Resolve-16-Color-Correction.pdf, DaVinci-Resolve-16_Beginners-Guide.pdf | Blackmagic manuals | Reference. Resolve 16 menus differ from Resolve 20 in places |
| __MACOSX | Mac resource junk, ignore | n/a |

The .dra files are Resolve disk archives. Opening them needs Resolve and imports a whole project. Free Resolve can import a .dra, but this was not tested.

## LUT packs

- P:\Tools\PB - 17 FREE LUTs: 17 .cube Wanderlust LUTs (Basin, Boulder, Butte, Everest, Hopkins, LochNess, Oaxaca, Oslo, Phoenix, Pocatello, Prague, Reykjavik, SantaFe, Seattle, Stillwater, Tahoe, Thames). Look LUTs. Wanderlust License and Guide.pdf sits beside them (license terms not read).
- P:\Tools\LUTS: 12 Ground Control zips (camera to Rec709: D-Log, S-Log3, V-Log, BMD Film, CineLike-D, Protune, Slog2, plus Reign Sample and Warm Sample looks). Not unzipped.
- P:\LUTS.zip: 8 look LUTs, each also as a 33 point version: MB CINE V2, MB CINE Subtle, MB CINE V2 EXTRA CON, AOD LOG Warm, AOD Expired Film, Neo 90's Action Film, Fuel Standard Cine Punch, Fuel Indigo Cine Sat Punch. Listing only, not extracted.
- P:\Tools\PremiumBeat Hollywood Lumetri Looks: 14 .look files (Lumetri look files named for fictional film parodies). Premiere only.
- P:\Tools\PremiumGrades: 20 After Effects .ffx grade presets.
- Red Giant Magic Bullet Suite and Looks are registered as installed (C:\Program Files\Red Giant, 24 LUTs and Looks presets seen). Whether they show up in Premiere 2026 is not verified.

## Rules for using this material

- Study to learn technique. A look built for the show is made from numbers (see wwd-color.md), not by renaming a pack LUT.
- Extract any zip to D:\WKP\scratch\, never into the repo.
- Reference stills from films are for looking at only. Do not copy them into any deliverable.
