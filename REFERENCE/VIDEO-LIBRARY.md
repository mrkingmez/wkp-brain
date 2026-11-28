# VIDEO-LIBRARY

Built 2026-11-21 by chief-of-staff for Zac's project board order. The full machine-readable table is `VIDEO-LIBRARY.csv` (same folder, 291 rows). **Owner: media-manager.** Add a row when a video goes live or is finalized, and every Wednesday after the FrostCast chain. Chief-of-staff checks it weekly.

## Read this first: how far to trust it
- **Seed data is STALE.** The review, FrostCast (EP 69 to 118) and Shorts rows come from `WWD/data/video-inventory.md`, a one-time VidIQ pull dated 2026-11-02 and 2026-11-03. Nobody owned updating it, which is how EP 118 was called "newest" on the A Knight's Tale package when EP 121 was already recorded.
- Rows built from disk or TASKS.md say so in `date_basis` and `source`.
- **A YouTube ID that is not on disk is written NOT KNOWN. Never guess one.** Zac pastes links for EP 119, 120, 121, Vision Quest 7 and 8, Godzilla and A Knight's Tale, then media-manager fills the ID column.
- "Live status NOT VERIFIED" means a file exists and a package or TASKS note exists, but no source says it was published.
- Titles for EP 119 to 121 come from the downloaded file names (the live titles), so they should match YouTube, but this was not checked against YouTube.

## Columns
title, series, episode, date, date_basis, status, youtube_id, local_path, upload_package_path, source, notes

## URL pattern
`https://www.youtube.com/watch?v=<ID>`. Shorts: `https://www.youtube.com/shorts/<ID>`.

## Latest FrostCast (read from disk 2026-11-21, EP 122 added 2026-11-25 by wwd-director)
| EP | Recorded | Title (from file name) | ID |
|---|---|---|---|
| 122 | Wed 2026-11-25 | The Doomsday hype is REAL / Hunger Games not starved at Box Office | NOT KNOWN |
| 121 | Wed 2026-11-18 | The name's Edwa-- er Bond / Snyderverse 2.0 | NOT KNOWN |
| 120 | Wed 2026-11-11 | James Gunn is James GONE | NOT KNOWN |
| 119 | Wed 2026-11-04 | Godzilla UNLEASHES on the Box Office | NOT KNOWN |
| 118 | published 2026-10-29 | James Gunn fires back after Clayface "Flop" | kYsixGzX3PQ |

Next: **EP 123, Wed 2026-12-02, 9 PM** (every Wednesday; calendar NOT VERIFIED). Newest FrostCast ID we hold is EP 118, so any card 3 must say "newest not in inventory" and use the real latest episode number above.

## In production or just finished (not in the live list)

| title | series | date | status | youtube_id |
|---|---|---|---|---|
| Godzilla UNLEASHES on the Box Office / FrostCast Episode 119 | FrostCast | 2026-11-04 | Recorded; live status NOT VERIFIED | NOT KNOWN |
| Vision Quest Review EP 7 | WWD Vision Quest review | NOT KNOWN | Finished and uploaded per TASKS.md; publish date and ID NOT VERIFIED | NOT KNOWN |
| Vision Quest Review EP 8 (finale) | WWD Vision Quest review | 2026-11-19 | Live (Zac, 2026-11-19) | NOT KNOWN |
| Godzilla Minus Zero Review - All Hail the King! | WWD review | NOT KNOWN | Upload package built; posted or not NOT VERIFIED (TASKS.md still lists release date and posting as open) | NOT KNOWN |
| A Knight's Tale (first watch review) | WWD review | NOT KNOWN | LIVE on YouTube per Zac 2026-11-21, posts scheduled by Zac. Export 36:36.7 on disk, AUDIO mp3 and 5 Shorts built, none scheduled by agents | NOT KNOWN |
| Den Files EP 1: Fire in the Sky | Den Files | 2026-11-22 | NOT RECORDED. Script drafted (v3). Not released. The old 2026-10-01 target passed. | n/a |


## Ian trailer cuts (non-WWD, Studio job)
Six newest cuts listed in the CSV with paths. Older v1 to v3 cuts are in `P:/01 Warrior King Productions/02 Video Project/Ian's Book Trailers/Rough Cut/`. Status: working cuts, nothing delivered, Ian posts.

## WWD reviews, commentary and Vision Quest (stale pull, newest first)

| date | series | title | youtube_id | upload_package_path |
|---|---|---|---|---|
| 2026-11-02 | WWD Vision Quest review | Vision Quest Review Eps 5 and 6: Who Is the Client? Did It Rewrite Tony Stark'S Genius? | YWRdI5A_cdw | PKG/Vision Quest 5 and 6 Upload Package/2026-11-01 - Vision Quest 5 and 6 Upload Package.docx |
| 2026-10-31 | WWD Vision Quest review | Vision Quest Review: Did the Show Play Ultron Too Early? | RWzwu6eS3rY | PKG/Vision Quest 3 and 4 Upload Package/2026-10-29 - Vision Quest 3 and 4 Upload Package.docx |
| 2026-10-27 | WWD review | Clayface (2026) Review: A Revenge Tale, Who Is on the Kill List? | vOeZNpWPV10 | PKG/Clayface Upload Package/2026-10-26 - Clayface Upload Package.docx |
| 2026-10-24 | WWD Vision Quest review | Is the MCU Back? Vision Quest Review: Who Steals Episodes 1 and 2, Spader or Bettany? | s9tvpaPKDBA | PKG/Vision Quest Upload Package/2026-10-23 - Vision Quest Upload Package.docx |
| 2026-10-21 | WWD review | Crystal Lake Series Review: That Was Weird or Weird Good? Does Jason Really Need an Origin Story? | tU_d49ta-vs | PKG/Crystal Lake Upload Package/2026-10-21 - Crystal Lake Upload Package.docx |
| 2026-10-20 | WWD review | Street Fighter (2026) Review: Nostalgia done right? | rU72L1R7ZY4 | PKG/Street Fighter Upload Package/2026-10-19 - Street Fighter Upload Package.docx |
| 2026-10-18 | WWD review | Carrie (2026) Review: Mike Flanagan's Carrie Is a Top Show of 2026 | OQIgysPt5pQ | PKG/Carrie (2026) Upload Package/2026-10-17 - Carrie (2026) Upload Package.docx |
| 2026-10-14 | WWD review | Other Mommy (2026) Review: WTF happened? (SPOLIERS) | GR7A4iRlNao | PKG/Other Mommy (2026) Upload Package/2026-10-14 - Other Mommy (2026) Upload Package.docx |
| 2026-10-07 | WWD review | Heat (1995) First Watch Review: Why Winter Wolf Says They Cannot Make Movies Like This Anymore! | CbXSuRQvdoo | PKG/Heat Upload Package/2026-10-07 - Heat Upload Package.docx |
| 2026-09-12 | WWD review | Terminator 2: Judgment Day Review: Does This 90s Classic Hold Up? | sfTT-aERFEc | PKG/Terminator 2 Upload Package/2026-09-12 - Terminator 2 Upload Package.docx |
| 2026-09-07 | WWD review | The Whisper Man (2026) Review: Netflix's Temu Silence of the Lambs. | kzQibNjH48g | PKG/The Whisper Man Upload Package/2026-09-06 - The Whisper Man Upload Package.docx |
| 2026-09-01 | WWD review | Good Boy (2025) Review: The $70K Horror Movie Filmed From a Dog's POV | K89XHcRL9n4 | PKG/Good Boy (2025) Upload Package/2026-09-24 - Good Boy (2025) Upload Package.docx |
| 2026-08-18 | WWD review | End of Oak Street Review (2026) - The Dinosaurs Deserved Better / Reaction and Review | ME0mpezCXuM | none on disk |
| 2026-08-13 | WWD review | Point Break - First Watch, 35 Years Late / Reaction and Review | lCLZrz5C2r8 | none on disk |
| 2026-08-12 | WWD review | The Last House (2026) Netflix Review: Stop Watching At The 40 Minute Mark | RdVLW9ljuP4 | PKG/The Last House Upload Package/2026-09-24 - The Last House Upload Package.docx |
| 2026-08-03 | WWD review | Spider-Man Brand New Day Review: The MCU Is Finally Back | LhANB5v98ag | none on disk |
| 2026-07-29 | WWD review | Christopher Nolan's The Odyssey Review - An Epic That Isn't | YhpyI-oOpV0 | none on disk |
| 2026-07-26 | WWD commentary | Remember Blade? / Ryan Gosling IS the MCU's Ghostrider | f2tdRJQMSHo | none on disk |
| 2026-07-25 | WWD commentary | Clayface Could Change the DCU, And It's Not About Batman | 3KwoiS1w0AE | none on disk |
| 2026-07-21 | WWD review | Evil Dead Burn Review / Just More of the Same! | oigskWNAzzI | none on disk |
| 2026-07-17 | WWD review | 12 Monkeys (2015) Season 1 Review / Time Travel Paradoxes Done Right | ZVo2cND2mjw | none on disk |
| 2026-07-11 | WWD review | Widow's Bay Review - Apple TV's Best New Horror Comedy / Series Review | GsJMowQiCT4 | none on disk |
| 2026-07-08 | WWD review | Evil Dead Rise Review: Is It Worth It Before Evil Dead Burn? | WWEzJ1n6UY8 | none on disk |
| 2026-07-05 | WWD review | Supergirl (2026) Review: The Comic Beat the Movie, Here's Why! | U8k3qVoX-ZE | none on disk |
| 2026-06-15 | WWD review | Disclosure Day 2026 Review - Is Spielberg Really Back? | C5Yxi2Pm2k8 | none on disk |
| 2026-06-07 | WWD review | Masters of the Universe 2026 Review - He-Man Understood the Assignmen | NBPCx_n8mu0 | none on disk |
| 2026-06-06 | WWD review | Spider-Noir Series (2026) Review - MCU Should Be Taking Notes. | Oi8yISIGfJI | none on disk |
| 2026-06-02 | WWD review | Backrooms (2026) Full Review - Liminal Horror or Just Boring? | g2Z9mEM9Tg8 | none on disk |
| 2026-05-31 | WWD review | Spider-Noir Episode 1 Review - Marvel's best isn't the MCU... | 3X--pFROvsE | none on disk |
| 2026-05-26 | WWD review | Star Wars Mando and Grogu Review - Fun or Forgettable? | dn_Dg6VXsZs | none on disk |
| 2026-05-25 | WWD review | Fury 2014 Review - Best War Movie Ever Made? Honest Take / Memorial Day | WUY6xYy0zFQ | none on disk |
| 2026-05-24 | WWD review | Passenger 2026 Review - Haunted House on Wheels Honest Take | SxcVNpcXQHc | none on disk |
| 2026-05-19 | WWD review | Obsession (2026) A New Genesis of Horror? Review | Bm57nryaMfg | none on disk |
| 2026-05-18 | WWD commentary | Punisher: One Last Kill - Did the MCU Finally Get Frank Castle Right? BREAKDOWN | Bl-_L0lhFYQ | none on disk |
| 2026-05-12 | WWD review | Stranger Things Tales from 85 Review - Canon Breaks, Bad Animation and Honest Take | 2jTyIgXBXJk | none on disk |
| 2026-05-11 | WWD review | Mortal Kombat II Review: Kano Steals the Show Again / Breakdown | DKcyGy3Ia5g | none on disk |
| 2026-05-05 | WWD review | Hokum (2026) Recap and Review / Ending Explained / Is Adam Scott Horror Icon? | TfCw5u5ozz8 | none on disk |
| 2026-04-13 | WWD review | Big Trouble in Little China / It's all in the reflexes [Review] | 9oufvQRZhl8 | none on disk |
| 2026-04-10 | WWD review | DareDevil Born Again S2xEP 4 / Recap and Review | c9kI3aEu-k8 | none on disk |
| 2026-04-06 | WWD review | Daredevil Born Again S2 E2-3 Recap and Review / Kingpin Trial Breakdown + Muse Theory | MNxGiqoVM44 | none on disk |
| 2026-03-27 | WWD review | Daredevil Born Again Season 2 Ep 1 recap and review | k6tmI8lQHEw | none on disk |
| 2026-03-26 | WWD review | Project Hail Mary Recap and Review / Ending Explained + Adaptation Breakdown (2026) | Jf4LLCK70so | none on disk |
| 2026-03-17 | WWD review | Undertone (2026) Horror Movie Recap and Review / Ending Explained + Sound Design Breakdown | UY5YFV5dt0U | none on disk |
| 2026-03-04 | WWD review | Scream 7: Scares or Snores? [Review] | bV5iLitwlDI | none on disk |
| 2026-02-23 | WWD RetroWatch | Dragonheart (1996) / RETROwatch [REVIEW] | M284bgKjOew | none on disk |
| 2026-02-09 | WWD review | Fallout Season 2 Finale Explained | RSuCR1QQ1kw | none on disk |
| 2026-02-08 | WWD review | Wonder Man Review: Marvel's Most Human Show Yet or Another Miss? | 7B1LJmhfOYM | none on disk |
| 2026-02-02 | WWD review | Fallout S2 Ep 7 Review / Cold-Fusion, Deathclaw Showdown and Lucy's Moral Test | MGBM0EQJk-g | none on disk |
| 2026-01-27 | WWD review | Fallout Season 2 Ep 6 Review | S_axu6GSo8E | none on disk |
| 2026-01-26 | WWD review | Percy Jackson Season 2 Finale Review | txYiPEe2Axc | none on disk |


`PKG/` = `D:/WKP Reports/WWD Upload Packages/`.

## FrostCast EP 69 to 118 (stale pull)

| episode | date | title | youtube_id |
|---|---|---|---|
| 118 | 2026-10-29 | James Gunn fires back after Clayface "Flop" / FrostCast Episode 118 | kYsixGzX3PQ |
| 117 | 2026-10-22 | Supergirl is Super OVER IT / FrostCast Episode 117 | kDruxzJffNI |
| 116 | 2026-10-15 | MCU is (maybe) back with VisionQuest / Crystal Lake is almost here / Episode 116 | aWlD-14TOvk |
| 115 | 2026-10-08 | Did Amazon Prime hit with Carrie 2026? / The Batman 2 on HOLD? / Episode 115 | JJrECo2y9zk |
| 114 | 2026-10-01 | This is not, CANNOT be The Way / Episode 114 | 5uic8suLRrk |
| 113 | 2026-09-24 | Does anyone care about the Avengers Encore? / Episode 113 | Odf-DCtiK9I |
| 112 | 2026-09-17 | Resident Evil Creeps back into the Box Office / Episode 112 | WG_ijLGBtOw |
| 111 | 2026-09-10 | Spider-man cancelled BEFORE Rings of Power?? / Episode 111 | Q1RV2WW8O5w |
| 110 | 2026-09-03 | Gunn killed Lanterns / Episode 110 | CHDOw5FS0C0 |
| 109 | 2026-08-27 | NOOO!! RIP Dolly Parton and Tim Curry / WB merger puts DCU on HOLD / Episode 109 | 5mP1cHtSd_A |
| 108 | 2026-08-20 | We say goodbye to Hayden Panitierre / Did Disney cook at D23? / Episode 108 | 6riQCMJZ7RU |
| 107 | 2026-08-13 | Will Disney deliver at D23? / New STAR WARS revealed? / Episode 107 | foA0LKMTz_I |
| 106 | 2026-08-06 | Spider-man DOMINATES the Box Office / Episode 106 | ymuV2j6vJDg |
| 105 | 2026-07-30 | Spiderman Swings Past Nolan's Odyssey / Episode 105 | -iaf3GCn6Ds |
| 104 | 2026-07-23 | DOOMSDAY TRAILER has arrived! / Odyssey Box Office Breakdown / Episode 104 | I5CdyOrJuX8 |
| 103 | 2026-07-16 | Nolan's Odyssey: Epic film or Epic FLOP? / RIP Sam Neill / Episode 103 | _JFT98wjoHY |
| 102 | 2026-07-09 | Nostalgia has grown POWERFUL / Ep. 102 | c14vzAysWi4 |
| 101 | 2026-07-02 | The FINAL Supergirl video / DCU going down in FLAMES / Ep. 101 | GEw9PiPDJ7Q |
| 100 | 2026-06-25 | We made it to 100!! / Also, Supergirl sucks / Episode 100 | Xzi4IHDlMrg |
| 99 | 2026-06-18 | Did the DELAY hurt House of the Dragon? / Ep. 099 | fPkKirh2l3A |
| 98 | 2026-06-11 | The World has MOVED ON / Ep. 098 | w9aLJ3qsq_0 |
| 97 | 2026-06-04 | Star Wars Starfighter is already a lost cause / Ep. 097 | lart9kziuBo |
| 96 | 2026-05-28 | Mandalorian MISFIRES / Ep. 096 | LEGRq_k6Goc |
| 95 | 2026-05-21 | Mortal Kombat 2 DEAD? / Ep.095 | PhTirprt-WE |
| 94 | 2026-05-14 | Does Hollywood hate optimism? / Video Game films will save movie industry / Ep. 094 | EsYgt46UqAU |
| 93 | 2026-05-07 | Daredevil Born Again Season 2 FINALE / Mortal Kombat 2 drops this week / Ep. 093 | 6aieBojhzjM |
| 92 | 2026-04-30 | We have a special guest... / Daredevil Born Again S2xE7 REVIEW / Ep. 092 | xbnKNBneC9U |
| 91 | 2026-04-23 | New York is ready to EXPLODE! / Endgame Re-release ahead of Doomsday / Ep. 091 | NJvED71Qlq8 |
| 90 | 2026-04-16 | Was That REALLY the Watcher in Daredevil?! / FrostCast 90 | Qph8c1HfjLE |
| 89 | 2026-04-09 | Is Anyone Watching Daredevil Born Again? / Maul returns in Shadowlord / Ep. 089 | om2hzai2qxo |
| 88 | 2026-04-02 | Expecto Disastrous!! Harry Potter Series First Look / Ep. 088 | x5hKLKIhSJs |
| 87 | 2026-03-26 | Daredevil is born again... again / Super Mario to make $3 Trillion? / Ep. 087 | K7R0Q-LPvik |
| 86 | 2026-03-19 | Horror Kills the Oscars / Ep. 086 | 2fUk9Nm8wtk |
| 85 | 2026-03-12 | The Box Office left The Bride! at the altar / Ep. 085 | qRZparfgSlw |
| 84 | 2026-03-05 | Doomsday PLOT LEAKS / Paramount slays Netflix / Horror is about to EAT / Ep. 084 | JQdLBuT6ce0 |
| 83 | 2026-02-26 | Where is Scream 7 going? / More Andor... Sorta / Sony rebooting Spidey? / 083 | 9OinS0b2thA |
| 82 | 2026-02-19 | Another Mando Trailer? / DCU closes a Gunn favorite project / 082 | LocP3km1WUA |
| 81 | 2026-02-12 | Does Disney HATE Mando and Grogu? / More fantasy on streaming / Ep. 081 | 0N4SupcElqA |
| 80 | 2026-02-05 | Markiplier Movie Weirdness / Brandon Sanderson saves Fantasy? / Ep. 080 | BYBIh78-lwM |
| 79 | 2026-01-29 | A NEW New Hope? / Frankenstein is the next Bond? / 079 | fu6eF8DX2bY |
| 78 | 2026-01-22 | Ding, Dong, the Witch is Gone / Episode 78 | RRou20XuoR4 |
| 77 | 2026-01-15 | Duffer Bros had NO plan?? / Ep. 077 | 0e-PWMhXu2U |
| 76 | 2026-01-09 | 2026 HYPE list / Conformity Gate COPIUM / Kennedy OUT at LucasFIlms / Ep.076 | bA9cbGvSg_k |
| 75 | 2026-01-01 | 1st Annual Frozen Wolfie Awards / We Say GOODBYE to 2025 / Ep. 075 | qLE6LZ2PrFA |
| 74 | 2025-12-25 | Our Nominations for the Best of 2025 / Robin Hood / Force Awakens turns TEN! / Ep. 074 | S5jKfRPDMKo |
| 73 | 2025-12-18 | Fallout BLASTS back onto Amazon Prime [Season 2 Episode 1 Review] / Ep. 073 | 4kSjgMYsLQc |
| 72 | 2025-12-11 | The END of Movie Theatres? / It: Welcome To Derry Episode Seven REVIEW / Ep. 072 | zp2jM4_xxWU |
| 71 | 2025-12-04 | Are you excired for Avatar: Fire and Ash? / Ep. 071 | g2loH1Lj3qA |
| 70 | 2025-11-27 | Stranger Things reaches PEAK HYPE / Pennywise REVEALED in IT: Welcome to Derry / Ep. 070 | 0eFI7_dmovI |
| 69 | 2025-11-20 | Looking back at Stranger Things / Are you ready for the FINAL season? / Ep. 069 | 9KcR26FtWFc |


## Shorts (partial: only 100+ view Shorts were ever stored)

| date | title | youtube_id |
|---|---|---|
| 2026-10-30 | Rest in Peace, Sir Patrick Stewart (1940-2026) / Winter Wolf's Den say Goodbye and Thank you! | rJ0lhmWrPLc |
| 2026-10-24 | Call of Duty's Reported $1.2 BILLION Budget Has Gamers Stunned | v0BmrD94kow |
| 2026-10-25 | How Black Adam Derailed Henry Cavill's Superman Return | p1aeyKBIuFQ |
| 2026-10-26 | Clayface Could Tease Batman in a Post-Credit Scene | XREBD-cjGSQ |
| 2026-10-24 | Jared Leto's Joker Looked Bold, but Failed on Screen | a04fAlylNAo |
| 2026-10-23 | Tom Hardy's Bane Makes Batman and Robin's Look Goofy | PPUO6Fof6iM |
| 2026-10-25 | Green Lantern's Best Oath, and Sinestro's Yellow Ring | ACyowndKvSs |
| NOT KNOWN | (title not pulled) | 0pDGh6482XA |
| NOT KNOWN | (title not pulled) | ajOuGj-vgW4 |
| NOT KNOWN | (title not pulled) | CbEZ0KYmBTM |


## Not listed here as rows
- FrostCast EP 1 to 68: folder-only rows in the CSV (no title, ID or date).
- Older finished files in `L:/Winter Wolfs Den review show/Final/`: one CSV row each (series "WWD archive"), publish status NOT VERIFIED.
- FrostCast EP 119 to 121 Shorts families: Opus projects P3111203h4MR (EP 120, 59 posts) and P31119047Y39 (EP 121, 63 posts). Per-clip titles are in `WWD/opusclip/EP120-approved-copy.json` and `EP121-approved-copy-v2.json`. Per-clip YouTube IDs NOT KNOWN.
- Vision Quest and review Shorts families: packages in `D:/WKP Reports/WWD Upload Packages/` (`... Shorts Captions` docx), IDs NOT KNOWN except the few in the Shorts table.
- What If, Hidden Hinge, AAR Commander (WKP Channel), RUBY TWO: no finished videos exist. Not seen in any source.
- Thumbnails, covers and kit videos (intros, outros, end cards in `P:\WWD Kit\`): assets, not videos. See `data/assets/media-map.md`.
