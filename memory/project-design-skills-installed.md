---
name: project-design-skills-installed
description: Taste and Impeccable design skills installed 2026-11-10, what was left out, and where the vetted sources live
metadata:
  type: project
---

Installed 2026-11-10 (Zac's yes) into `.claude\skills\`:
- `design-taste-frontend` = Leonxlnx/taste-skill v2.5.1, commit f6b7657, MIT, 35 MB, full folder. Its SKILL.md has a Stop hook that runs `scripts\gate.mjs` with node (local checks, headless Chrome on localhost, Overpass fetch only for map baking). Read, no network or exec found beyond that.
- `impeccable` = pbakaus/impeccable v4.8.2, commit f2baa41, Apache 2.0, 2.1 MB. LEFT OUT on purpose: the engine launcher (`scripts\impeccable`, `.cmd`) that downloads and runs a binary, its checksums file, and the repo's `.claude\settings.json` hooks (run on every edit and Stop). A WKP note at the top of its SKILL.md says to skip engine steps.

Vetted clones are in `D:\WKP\scratch\skill-vet\` (gitignored). Not installed: Playwright (later, needs a browser download and Zac's yes), Awesome Design, img2threejs. Skills load at the next session start. Rule behind the omission: no downloading or running executables without Zac's yes, see [[feedback-operating-procedure]].

**Why:** Zac asked for flashier dashboards (trading, agent network, fantasy).
**How to apply:** use these for dashboard builds; if Zac later says yes to the Impeccable engine, install it per its README and verify the checksums file.
