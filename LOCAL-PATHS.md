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
kingdom planners products = D:\Products\05 Kingdom Planners\products
kingdom planners delivery = D:\Products\05 Kingdom Planners\delivery
kingdom planners photos   = D:\Products\05 Kingdom Planners\photos

## Spark Capture
Spark Capture (Android app scaffold): D:\WKP\spark-capture\

 
## Tools
python           C:\Users\kingz\AppData\Local\Programs\
                 Python\Python312\python.exe
ffmpeg           FILL - run: where ffmpeg
pc health suite  D:\Tools\PCHealth
 
### Deliverables and media
deliverables     L:\
Guides/Referance  D:\WKP-Guides 

## WarriorKingDesigns (WKD)
wkd art root     E:\04 Warrior King Desins
wkd puzzle art   E:\04 Warrior King Desins\Puzzles\Imagines
                 (subfolders: christian, Christmas, Fantasy, Military)
wkd delivery     D:\04 New Warrior King Designs\_Print Exports
                 (confirmed 2026-09-01 — pre-existing convention found on
                 disk, not newly invented: one subfolder per design with
                 sized files, plus a same-named .zip at the _Print Exports
                 root. New line batches get their own named subfolder
                 under _Print Exports, e.g. \christian\, to avoid
                 colliding with older per-design exports already at the
                 root. Older root-level exports (Military, some
                 Landscapes/Christian) are PNG, 4 sizes, no A4/A3 — an
                 earlier spec version. Current spec (set 2026-09-01):
                 8x10/5x7/11x14/16x20/A4/A3, JPG, 300 DPI.)
 
## RULES
- Read the section for the machine you are on.
- Scratch goes to the repo scratch folder. Never system Temp.
- Reusable scripts live in the owning skill's scripts\ folder.
- Every notepad or mkdir command must be preceded by its own
  cd /d command in the SAME message. Never assume you're still
  in the folder from a previous step.




