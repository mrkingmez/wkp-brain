# LOCAL PATHS
Machine-specific paths only. Decisions go in CLAUDE.md.
Never hardcode a path that appears here into a script.
 
## MACHINE: MAIN DESKTOP (Windows 11)
 
### Core
repo             D:\WKP
scratch          D:\WKP\scratch          (gitignored)
logs             D:\WKP\logs
data             D:\WKP\data             (weekly performance drops)
skills           D:\WKP\.claude\skills
agents           D:\WKP\.claude\agents
user settings    C:\Users\kingz\.claude\settings.json
project settings D:\WKP\.claude\settings.json
 
### WWD
wwd formats      D:\WKP\WWD\formats
wwd source video L:\Winter Wolfs Den review show\
frostcast source L:\Winter Wolfs Den review show\Frost-Cast\
Audio		 L:\Winter Wolfs Den review show\Frost-Cast\Raw Audio

## Writing
MY Writing  L:\03 My writing

## Cyber Security
Cyber Secuirty   D:\WKP-Guides\

## Kingdom Planners
Kingdom Planners D:\05 Kingdom Planners
kingdom planners xlsx files (6 of 7 confirmed) = D:\05 Kingdom Planners\excel\files.zip
kingdom planners products = D:\05 Kingdom Planners\products  (empty as of 2026-09-24)
kingdom planners delivery = D:\05 Kingdom Planners\delivery  (empty as of 2026-09-24)
kingdom planners photos   = D:\05 Kingdom Planners\photos    (empty as of 2026-09-24)
(Corrected 2026-09-24 — the old `D:\Products\05 Kingdom Planners\...` paths do
not exist on this machine, confirmed by direct check. Complete Budget System's
.xlsx is not in the files.zip above or anywhere else found on C:/D:/E:/L: —
see Kingdom-Planners\CLAUDE.md Products table.)

## Spark Capture
Spark Capture (Android app scaffold): D:\WKP\spark-capture\

## PAWS
PAWS venture = D:\WKP\PAWS

 
## Tools
python           C:\Users\kingz\AppData\Local\Programs\
                 Python\Python312\python.exe
ffmpeg           FILL - run: where ffmpeg
pc health suite  D:\Tools\PCHealth
 
### Deliverables and media
reports/deliverables (ALL, locked 2026-10-05) = D:\WKP Reports\
                 One subfolder per deliverable type, each dated version
                 inside (YYYY-MM-DD - Name.docx). This is the one place
                 Zac looks for any report/guide/prep-batch going
                 forward - see root CLAUDE.md's "Output document format"
                 for the full rule. L:\ below is raw media/source only,
                 not where finished deliverables go anymore.
deliverables - OLD, superseded 2026-10-05 = L:\
                 (still correct for raw WWD source video/media, see WWD
                 section above - just not the deliverables doc location
                 anymore)
Guides/Referance  D:\WKP-Guides 

## WarriorKingDesigns (WKD)
wkd art root (REAL, going forward) = D:\04 New Warrior King Designs\
                 Zac's call 2026-10-03: this is the one real location
                 going forward, E:\ is being retired - see the E:\
                 status note below before removing anything, though.
                 Category subfolders: Christmas, Fantasy, Landscapes,
                 Military, Sci-FI, Sports, Thanksgiving, christian
                 (plus Logo Banner, Milkus, Mockups Christian - not
                 Etsy-line folders, leave alone). "Landscapes" as a
                 real source folder only ever existed here, never
                 under the old E:\ tree. Each category folder may
                 contain a \Used\ subfolder - those designs are
                 already listed, skip them when picking candidates.

wkd art root - RETIRED 2026-10-03 = E:\04 Warrior King Desins\Puzzles\Imagines
                 Zac's call: no longer the real location, D:\ above is.
                 **Fully verified clean before retiring, not just
                 assumed:** diffed every file in E:\ against D:\ across
                 all 4 categories E:\ ever had (christian, Christmas,
                 Fantasy, Military). Military/christian/Christmas were
                 already clean (D:\ had every file plus more). Fantasy
                 had a real gap — 31 files existed ONLY on E:\ (mostly
                 Firefly/ChatGPT generations from Aug 30 2025) — copied
                 into D:\04 New Warrior King Designs\Fantasy\ on
                 2026-10-03, re-diffed after copying, zero files
                 remain E:\-only. Nothing was deleted from E:\ itself
                 in this process, only copied additively; the E:\
                 folder structure still physically exists on disk if
                 anyone ever needs to double-check this again, it's
                 just no longer the path to use or document going
                 forward.
wkd delivery     D:\04 New Warrior King Designs\_Print Exports
                 (confirmed 2026-09-01, expanded 2026-10-03 — pre-existing
                 convention found on disk, not newly invented: one
                 subfolder per design with sized files, plus a
                 same-named .zip at the _Print Exports root. New line
                 batches get their own named subfolder under
                 _Print Exports, e.g. \christian\, \Military\,
                 \Landscapes\, to avoid colliding with older per-design
                 exports already sitting flat at the root. Older
                 root-level flat exports (most Military designs, 3
                 Landscape designs, 2 Christian designs) are PNG, 4
                 sizes, no A4/A3 — an earlier spec version, not
                 current-spec ready. Current spec (set 2026-09-01):
                 8x10/5x7/11x14/16x20/A4/A3, JPG, 300 DPI, in the
                 category subfolder.)
 
## RULES
- Read the section for the machine you are on.
- Scratch goes to the repo scratch folder. Never system Temp.
- Reusable scripts live in the owning skill's scripts\ folder.
- Every notepad or mkdir command must be preceded by its own
  cd /d command in the SAME message. Never assume you're still
  in the folder from a previous step.




