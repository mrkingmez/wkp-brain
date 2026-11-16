# VERSION GAP METHOD

Created 2026-11-13 from Zac's order: "Be sure to tag the version trained on and then find a way to close the gap between the versions."
Applies to every skill, drill and tutorial the Animation department learns from. Our versions today: Blender 5.2.4, Unreal 5.8.4 (read from `LOCAL-PATHS.md`, update this line when they change).

## Why

Most good tutorials are older than the software we run. A skill built from one silently teaches menus, defaults and brush names that moved. The fix is not to avoid old videos, it is to say exactly which version taught what, and to carry a written list of what changed.

## The five rules

1. **Version tag on everything.** Every skill file, drill and tutorial note carries a block at the top:
   `TRAINED ON: <software> <version> (STATED or INFERRED, evidence) | VIDEO DATE | OUR VERSION: <x> | GAP: <releases between> | LAST CHECKED: <date> against <version>`.
   STATED means the maker said it (title, description, voice, on-screen). INFERRED means we worked it out from the upload date or UI, and the evidence is written down. If neither is possible, write NOT KNOWN and treat the whole source as unverified.
2. **One delta sheet per tutorial.** Stored in `D:\WKP\research\animation\` next to the tag. One row per step: the tutorial's step, status (PASS, CHANGED, NEW, FLAG, UNVERIFIED), what is true in our version, evidence (release note page, manual page, a headless or live check). Template is the table in `research\animation\2026-11-13-version-tags-and-delta-sheets.md`.
3. **Sources for deltas, in this order.** (a) Official release notes for every release between the tutorial and ours. Blender: `developer.blender.org/docs/release_notes/<version>/`, read the pages sculpt, modeling, user_interface, rendering, compositor, python_api, core, plus the Compatibility section of the index. Unreal: Epic's release notes per version and the feature's docs page with `?application_version=<ours>`. (b) The official manual for the feature. (c) A live check. Anything not found in (a) to (c) is marked UNVERIFIED, never guessed.
4. **Verification before trust, with honest levels.**
   - Blender: check in a scratch scene through the blender MCP following `blender-mcp-ops` (never touch Zac's objects). If the live link is down, a headless Blender (`blender -b --factory-startup`) can prove that an operator, modifier, property, node input, enum value or bundled asset exists and what its default is. It cannot prove menu paths or shortcuts, so those stay UI-UNVERIFIED until clicked live.
   - Unreal: docs first. The editor is opened only by Zac's instruction or when `ue-mcp-and-automation` allows a safe scripted check. Experimental plugins are never enabled without Zac's yes.
   - A status of PASS needs a named check. "Looks the same" is not a check.
5. **Close the gap in the skill, not only in the note.** A skill teaches OUR version. Where a delta row says CHANGED, the skill text uses the new name and path and adds one line "old videos call this X". Where a row says FLAG (paid file, paid software, unlogged license), the skill teaches the method and names the free route.

## When it gets re-checked

- **Trigger A, we update software.** Any change to the Blender or Unreal version in `LOCAL-PATHS.md`. Same day, animation-director reads the release notes for each skipped release, and re-runs the delta rows marked CHANGED, NEW or UNVERIFIED for every skill. Update LAST CHECKED. Only the changed rows are redone.
- **Trigger B, a bench misses a standard** that traces to a version difference. Fix the skill, add the delta row, date it (existing rule in `ANIMATION\CLAUDE.md`).
- **Trigger C, calendar.** Every Blender LTS or Unreal minor release, and at least once every 90 days, scan the release notes for new items touching skills in use. Add this to the Monday brief checks only if Zac wants it, otherwise animation-director does it when a job starts.
- **Trigger D, a tutorial is added.** No skill is written from a source without its tag block and delta sheet.

## Who does what

| Step | Owner |
|---|---|
| Tag block and delta sheet | animation-director (research and writing) |
| Live Blender checks | blender-asset-scout or builder bench, through animation-director, scratch scene only |
| Unreal live checks | ue-scene-builder, only when Zac allows opening the editor or a safe script |
| Gate | animation-director against STANDARDS.md: a skill or drill without a tag block fails the report line G.2 ("nothing is called done that was not looked at") |
| Decisions that cost money, licenses, experimental plugins | Zac, queued in DECISIONS.md |

## Drill and skill header (copy this)

```
TRAINED ON: Blender 4.3.1 (STATED, caption 00:00:18) | VIDEO 2024-12-20 | OUR VERSION: Blender 5.2.4 | GAP: 4.4, 4.5, 5.0, 5.1, 5.2
DELTA SHEET: research\animation\2026-11-13-version-tags-and-delta-sheets.md section 2.1
LAST CHECKED: 2026-11-13 against Blender 5.2.4 headless (API only, UI-UNVERIFIED rows listed in the sheet)
```

## Proposed skill and drill outline for what is approved so far (NOT yet written)

Zac still has to approve the boat and sci-fi ship picks (another agent's report: `research\animation\2026-11-13-boat-and-scifi-ship-picks.md`). The three skills named in `ANIMATION\CLAUDE.md` wait for that, and S1 and R1 (sculpting and retopology top picks) are not on the yes list yet. What can be outlined now:

**Skill 1, `blender-sculpting-and-retopo` (needs S1 and R1 for a full version).** From S2 alone: brush reference with the 5.2.4 names and the rename table, voxel remesh versus Dyntopo, Plane brush, cloth brush defaults, mask and face set tools, Multires. Retopology and baking cannot be written until R1 or an equivalent is approved. Tag S2 as 4.3.1, delta sheet 2.1.
- Drill 1.1 Brush tour: ico sphere, one stroke per brush family, record name and effect, 20 min. Pass: every brush found by its 5.2.4 name.
- Drill 1.2 Rock hill: sculpt a rock outcrop with Voxel remesh, Clay Strips, Crease Sharp, Plane, Smooth. Graded by STANDARDS A.4 (no loose geometry after remesh), A.10 (four angles).
- Drill 1.3 (needs R1) retopo the rock to under 5,000 tris and bake normals for Unreal.

**Skill 2, `blender-environment-landscapes`.** Two routes, both taught, per Zac's answer.
- Route A, experimental Mesh Terrain (L1, delta 2.2): Open World level, four plugins listed by Epic, Create Rectangle, Remesh and Tessellate modifiers, Weight Channels and the free material nodes, Convert tool for a Blender-sculpted terrain mesh. Needs Zac's yes to enable plugins in a live editor.
- Route B, classic Landscape (U1 chapters at 1:56:50 and 2:08:16, delta 2.5): Landscape mode, sculpt, layer info Advanced Weight Blending, Exclusive Paint Mode note.
- Blender side: sculpt or displace a terrain mesh in Blender, export, Convert in Mesh Terrain (route A) or use as a heightmap (route B). The Blender half has no approved video yet, so it comes from the S2 and R1 skills.
- Drill 2.1 Same hill in both routes at 1 km by 1 km, record triangle count, build time, painted layers. Compare. Graded by STANDARDS F.2 (8 GB VRAM) and F.4 (look at frames).

**Skill 3, `blender-architecture-and-vehicles`.** From H1 (cabin, chapter level until captions are pulled) and B1 (hull method: blueprint, silhouette block, mirror plus subdivision, base mesh plus details mesh, bevel weight, crease). Boat and ship picks join when approved.
- Drill 3.1 Cabin to H1's chapters at 5,000 tris or fewer, with door, roof, lantern.
- Drill 3.2 Hull from a side and top blueprint using B1's method, no jet parts, 30,000 tris hero limit.
- Drill 3.3 (after boat and ship approval) the approved boat or ship.

**Lighting and import (existing skills, tag them).** `ue-scene-lighting-render` gets U1's chapters for menus and U2 for principles, with delta 2.5 and 2.6. `ue-import-pipeline` is not replaced by U1, which only covers a plain FBX.

Each skill opens with the header above. Each drill lists its grade line from `STANDARDS.md`.

## Open flags for this method

1. H1 captions still to be pulled (rate limit).
2. Live Blender link was down when the Blender checks ran, so UI paths and shortcuts for S2, H1 and B1 need one live pass.
3. Licenses to read and log before any use: Poliigon files for B1, Sensei downloads for L1 and U1, Blender Guru blueprints.
4. Photoshop in B1 is paid, teach the Blender texture paint route or Zac does that step.
