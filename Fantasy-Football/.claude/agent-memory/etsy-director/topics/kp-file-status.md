---
name: kp-file-status
description: Which Kingdom Planners product files actually exist on disk, as of 2026-09-24
metadata:
  type: project
---

## Complete Budget System (flagship, 16 tabs) is missing, confirmed 2026-09-24

Kingdom-Planners\CLAUDE.md lists it as "Ready," but it is not on disk. Checked
every LOCAL-PATHS.md location plus a full scan of C:, D:, E:, and L: drives
for this product and every drive-wide search for `*budget*.xlsx` /
`*Complete-Budget*`. Nothing. `C:\Users\kingz\Downloads\Kingdom Planners -
Handoff Document.md` explains why: it was built in a web chat session and
saved to that session's `/mnt/user-data/outputs/`, never downloaded to
permanent storage. That's the same failure mode root CLAUDE.md's file
retention rule was written to prevent ("five Kingdom Planners spreadsheets
were lost exactly that way").

**Why this matters:** don't write listing copy, tab enumeration, or a photo
spec for this product from the CLAUDE.md description alone. The description
there is a plan, not verified content, and other CLAUDE.md product
descriptions turned out to be stale when checked against real files (see
below). Complete Budget System needs the actual file back (Zac re-pulling it
from the original chat, or a rebuild) before any real work can happen on it.

## The other 6 products are real and confirmed

Live at `D:\05 Kingdom Planners\excel\files.zip`: Debt-Freedom-Planner.xlsx,
Deployment-Pay-Budget-Planner.xlsx, PCS-Moving-Budget-Planner.xlsx,
Road-Trip-Planner.xlsx, Terminal-Leave-ETS-Transition-Planner.xlsx,
VA-Disability-Claim-Tracker.xlsx. Opened every tab of every file with
openpyxl before writing anything about them.

**Two of CLAUDE.md's pre-existing product descriptions didn't match the real
files** when checked: Road Trip Planner's CLAUDE.md description mentioned a
separate 20-stop Lodging Planner tab, a separate Stops & Attractions tab, a
pie chart, and a built-in mileage-deduction calculator — none of that exists
in the real file (real tabs: Start Here, Trip Setup, Route Planner, Budget,
Daily Log, Packing List, Vehicle Prep). Terminal Leave's CLAUDE.md
description said "6-month transition budget" — the real file's Transition
Timeline tab is 12 months. Both corrected in Kingdom-Planners\CLAUDE.md
2026-09-24, sourced from actually opening the files.

**How to apply:** before writing any KP listing copy, marketing material, or
photo spec, open the real .xlsx and read the actual tab names and Start Here
text — don't trust a prior CLAUDE.md description at face value, even one
written confidently as "Ready." Formulas were also scanned for
Sheets-breaking functions (XLOOKUP, FILTER, UNIQUE, LET, SORT, SEQUENCE,
LAMBDA, TEXTJOIN, IFS, SWITCH) across all 6 confirmed files: none found,
which is a good sign for the "works in Excel and Google Sheets" claim but
still not the same as an actual open-in-Sheets test, which hasn't happened.

Related: [[kp-skills]]
