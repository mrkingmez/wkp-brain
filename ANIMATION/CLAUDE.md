# ANIMATION: shared 3D department (Blender and Unreal)

Created 2026-10-31, Zac's call. This is a **shared department**, not a venture. Every director can order work from it. It answers to WKP (Zac, through Jarvis).

## Who is in it

| Agent | Section | Job |
|---|---|---|
| animation-director | Boss | Takes jobs from any director, plans, orders from its benches, gates the work against `STANDARDS.md`, sends it on. Also calls other departments like any director. |
| blender-asset-scout | Blender | Finds existing assets, reads and logs licenses, vets, imports. Free and licensed only. |
| blender-builder-props | Blender | Props, hard-surface, weapons, vehicles, environments. |
| blender-builder-characters | Blender | Characters, creatures, armor fitting, rigs, poses. |
| ue-scene-builder | Unreal | Projects, levels, lighting, materials, cameras, Sequencer, final renders. |
| ue-asset-integrator | Unreal | Blender to Unreal import: scale, collision, LODs, materials, validation. |

Benches are called only through animation-director. Specs in `.claude\agents\`.

## Training skills (`.claude\skills\`)

`blender-asset-quality`, `blender-character-craft`, `blender-asset-sourcing`, `blender-mcp-ops`, `ue-import-pipeline`, `ue-scene-lighting-render`, `ue-mcp-and-automation`. When a bench keeps missing the same standard, fix the skill and date the lesson.

## Mandate (Zac, 2026-11-01, LOCKED)

The Animation team does it ALL: sculpted characters and creatures, boats, houses and buildings, big landscapes, props, scenes. The team must learn to sculpt and model to a professional level, and it must be trained through skills until it can. It also looks for ready-made free assets first, and builds or adapts only what it cannot find. "I mean it all." If the team cannot reach Zac's bar with a method, it says so, finds a better method, and trains on it. It does not hand Zac weak work and does not hand the job back as "not possible."

Skills still to write (training gap found 2026-11-01): `blender-sculpting-and-retopo` (sculpt mode, brushes, multires, dyntopo, retopology, baking), `blender-environment-landscapes` (terrain, geometry nodes, scatter, large worlds for Unreal), `blender-architecture-and-vehicles` (houses, buildings, boats, hulls, interiors, modular kits). Wolf Warrior v1/v2 files deleted 2026-11-01 at Zac's order.

## Rules (locked 2026-10-31, Zac)

1. **Free only, ask first.** Nothing that costs money, credits or a subscription without Zac's yes and the exact price. Applies to assets, AI image-to-3D services and plugins.
2. **Standards gate.** animation-director checks every deliverable against `STANDARDS.md` before the requesting director sees it. Each side may send back once, then it goes to Zac with both versions (AGENT-NETWORK.md).
3. **Licenses logged** in `D:\WKP\data\assets\animation-asset-log.csv`. CC-BY-NC and unclear licenses are not usable.
4. **Versioned saves only.** `D:\Blender Projects\<Name> vN.blend`. Never overwrite a version. Never change or save over a scene or file the job did not create.
5. **No open network ports or third-party tools installed without Zac's yes.** Read the code and license first.
6. **Honesty.** Only measured numbers. "Not available" plus what is missing when a check could not run.
7. Decisions an agent cannot make go to `D:\WKP\logs\DECISIONS.md` as DECISION QUEUED.

## Pipeline decisions (Zac, 2026-11-01)

1. **No scratch-project test for now.** Nothing gets installed or run to test the Blender-to-Unreal pipeline until Zac asks.
2. **Free only.** The paid $14.99 Unreal Bridge fallback is OFF. Anything that costs money still goes to Zac first with the exact price.
3. **Third-party tools are allowed if they are free.** Rule 5 is relaxed for free tools only: read the code and license first, log the license, and still report what was installed. Ports (MCP 8000, Remote Execution 6766/6776, Web Remote Control 30010/30020) are covered by decision 4, not by this one.
4. **Epic's Unreal MCP plugin: auto-start OFF.** Zac said yes. If it is ever enabled, it is started by hand per session and stopped after, and the port is checked as loopback-only first.

## Tools and paths (this machine, also in LOCAL-PATHS.md)

- Blender 5.2.4 RC: `C:\Blender\5.2.4\blender.exe`. Render device OptiX on the RTX 5060 (saved).
- Blender MCP: addon "MCP for Blender" 1.8 on localhost:9876, server `mcp-for-blender` registered in Claude Code (user scope). Libraries (Poly Haven, Sketchfab, Poly Pizza) and 3D generators are OFF.
- Unreal Engine 5.8.4: `D:\Epic\UE_5.8`. Shader cache `D:\UE_DDC`. Projects `D:\Unreal Projects`.
- Blender files: `D:\Blender Projects\`.
- Scripts: `D:\WKP\ANIMATION\scripts\`. Logs: `D:\WKP\logs\animation-director.md`.

## Current state (update after each job)

- **2026-10-31:** department created. Skills being written from official docs. Blender-to-Unreal pipeline repo NOT chosen yet: candidates report at `D:\WKP\reports\animation\2026-10-31-Blender-UE-Pipeline-Candidates.md`, Zac picks. No agent can drive the Unreal Editor live yet (see `ue-mcp-and-automation`), so Unreal steps are scripts plus click steps for Zac.
- **2026-11-01, Zac REJECTED the Wolf Warrior: "it looked like crap, like someone who has never used Blender before would draw, that is way, way below the standard."** Do not save, ship, show to other directors, or use it as a benchmark. The method that made it (code-built Skin modifier blobs) is not good enough for characters. Characters need a different method before anything is shown to Zac again (see STANDARDS.md corrections).
- **Old note, superseded:** First test asset: Wolf Warrior with Sword, `D:\Blender Projects\Wolf Warrior with Sword v2.blend`. v2 body is a skin-modifier mesh with muscle masses. Known misses: head reads cartoonish, chest plate hidden, legs thin, tail straight, flat fur, does not match the reference face. AI image-to-3D would match better but costs credits (Higgsfield balance is 0, free plan). Zac chose the free hand-built route.
