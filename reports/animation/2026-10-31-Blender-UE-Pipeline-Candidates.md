# Blender to Unreal Engine pipeline candidates

Date: 2026-10-31. Requested by Zac for the Animation department. Read-only research: nothing was installed and no repo code was run. GitHub facts (license, dates, stars, releases) were pulled from the GitHub REST API on 2026-10-31. Vendor and Epic pages were read through web fetch. Where a source is a search summary and not a page I read, it is marked.

Target setup: Blender 5.2.4 RC (Windows x64), Unreal Engine 5.8.4 at D:\Epic\UE_5.8, RTX 5060, mcp-for-blender on localhost:9876 with Claude Code.

## Two different jobs

"Connect Blender and UE" is really two separate problems, and different tools solve each:

1. Moving content (meshes, rigs, animation, cameras, materials) from Blender into UE. Candidates 1 to 6.
2. Letting Claude drive Unreal the way it already drives Blender. Candidates 7 to 10.

Zac needs both. They do not conflict: Blender MCP uses port 9876, Epic's UE MCP uses 8000.

## Ranked table

| Rank | Name | Job | License | Last update | Blender 5.x | UE 5.8 | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Blender For UnrealEngine (xavier150) | Move content | GPL-3.0 | release 2026-07-22, commit 2026-10-08 | YES, 5.0 to 5.2 zip, "Support Blender 5.2" in 4.4.7 | YES, "Support Unreal Engine 5.8" in 4.4.6 | PRIMARY for content |
| 2 | Epic Unreal MCP (built into UE 5.8) | Claude drives UE | Ships with UE (Epic EULA, not checked) | 5.8.4 hotfix | n/a | YES, it is a 5.8 feature, marked Experimental | PRIMARY for Claude driving UE |
| 3 | ChiR24 Unreal_mcp (EngineWire) | Claude drives UE | MIT | release v0.6.0 2026-10-27, push 2026-10-30 | n/a | Claims 5.0 to 5.8 | Strong backup for driving UE |
| 4 | db-lyon ue-mcp | Claude drives UE | MIT | v1.4.11 2026-10-29 | n/a | Claims 5.8+ native toolset bridge | Watch list |
| 5 | Poly Hammer BlenderTools (Send to Unreal) | Move content | MIT | release 2025-11-23, commit 2026-05-27 | Partly: 5.0 prefs fix landed, CI tests only 4.2 | UNVERIFIED, CI tests only 5.4 | BACKUP for content |
| 6 | botero-dev bl_datasmith | Move whole scenes | AGPL for addon dir, mixed (SPDX NOASSERTION) | v1.1.12a 2026-02-10 | YES (v11 added 5.0) | NO build: release zips stop at UE 5.7 | Not yet |
| 7 | Unreal Bridge (Tachyon Studio, Superhive) | Move content | GPL-3.0-or-later, paid $14.99 | published about a month ago, v1.0.0 | YES, 3.3 to 5.2 | YES, 5.2 to 5.8 (vendor claim) | Paid alternative, young product |
| 8 | Blender To Unreal Live Link (Milad Kambari, Superhive) | Live sync | Not stated, paid $18 | March 2026 article | YES, 5.0+ | UNVERIFIED (says 5.5+) | Skip, no camera or animation |
| 9 | runreal/unreal-mcp | Claude drives UE | MIT | 2025-06-06 | n/a | UNVERIFIED | Abandoned (17 months) |
| 10 | tahooki/unreal-blender-mcp | Both ends via MCP | none | 2025-03-19 | UNVERIFIED | UNVERIFIED | Abandoned, no license, 21 stars |

Also seen and rejected: chongdashu/unreal-mcp (2110 stars, no license, last push 2025-04-22, abandoned), flopperam/unreal-engine-mcp (no license, README says it is now owned by Aura, a commercial product), legibleguy/unreal-blender-live-link (0 stars, no license, created 2026-05, too new to trust).

---

## 1. Blender For UnrealEngine Addons (xavier150)

- Repo: https://github.com/xavier150/Blender-For-UnrealEngine-Addons (owner xavier150)
- License: GPL-3.0 (GitHub API spdx_id). Default branch is `release`.
- Last release v4.4.8 on 2026-07-22. Last commit 2026-10-08. 2703 stars. Not archived. (GitHub API)
- Blender 5.x: the v4.4.8 release has a `blender_5.0-5.2.zip` asset, and the 4.4.7 notes say "New: Support Blender 5.2." (release API). Zac's 5.2.4 RC is a point-release of a supported line, but an RC build itself was not tested by me: UNVERIFIED for the RC.
- UE 5.8: the 4.4.6 notes say "New: Support Unreal Engine 5.8." (release API). Whether it works on 5.8.4 specifically is UNVERIFIED but 5.8 is named.
- What it does (README): exports static meshes, skeletal meshes, animations (NLA and actions), Alembic, collisions, sockets, splines, cameras, and Sequencer content. It generates Python import scripts you run inside Unreal, and it can put cameras, splines and sockets on the clipboard for pasting. Camera export includes cuts and lens data into a Level Sequence. Has a batch export of a whole scene and an error checker. It is a file export plus generated import script, not a live link.
- Install: unzip-free, install the matching `.zip` in Blender Preferences. Docs in the repo wiki.
- Account or payment: none. The author has a support/donation page, optional.
- Security: it generates Python scripts that you then run in Unreal (`py` command or the Python console). That is arbitrary code by design, but it is code you can read before running, and it opens no network port. No phone-home found in the README. I did not read the source.
- Fit for Zac: HIGH. Best match for what an animation department needs because it handles cameras, Sequencer and animation, not only meshes, and it explicitly tracks Blender 5.2 and UE 5.8. Its weakness is that it is a push-and-run workflow, not live sync.

## 2. Unreal MCP, built into Unreal Engine 5.8 (Epic)

- Docs: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor
- Owner: Epic Games. Announced in the 5.8 release post (https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274, dated 2026-06-17; latest hotfix listed is 5.8.4).
- License: ships with the engine, so the Unreal Engine EULA applies. I did not read the EULA, UNVERIFIED.
- Status: the doc page labels it Experimental, "many features are incomplete or missing," APIs and data formats "subject to change at any time."
- What it does: an MCP server inside the editor process. Plugins: Unreal MCP (internal name ModelContextProtocol), All Toolsets, Toolset Registry (auto), Terminal (optional). Default endpoint `http://127.0.0.1:8000/mcp`. In the console, `ModelContextProtocol.GenerateClientConfig ClaudeCode` writes `.mcp.json` into the project root, then launch Claude Code from there. Toolsets can be written in Python or C++.
- The doc page names only SceneTools, ActorTools, MaterialInstanceTools and ObjectTools as examples and does not document asset import or Sequencer toolsets. Third-party db-lyon claims 830 official tools on 5.8+, which suggests the registry is large, but that count is not from Epic's page.
- Account or payment: none.
- Security: Epic's own wording: "There is no authentication layer; the plugin is not safe to expose beyond the local machine." Binds loopback only and rejects non-loopback Origin headers. Auto-start is a setting, so leave it off unless in use.
- Fit for Zac: HIGH as the primary way Claude drives UE. Zero third-party code, version-matched to his engine. Risk is Experimental status.

## 3. ChiR24/Unreal_mcp, now branded EngineWire

- Repo: https://github.com/ChiR24/Unreal_mcp (owner ChiR24). Also npm `unreal-engine-mcp-server` and a Fab listing.
- License: MIT (GitHub API). 1000 stars. Release v0.6.0 on 2026-10-27, last push 2026-10-30. Not archived.
- UE 5.8: README badge and text say Unreal Engine 5.0 to 5.8 and show an Unreal Editor 5.8 screenshot. Still, screenshot-level evidence only, so treat as claimed, UNVERIFIED on 5.8.4.
- What it does: a native C++ editor plugin that serves MCP on `127.0.0.1:3000`, with one `unreal` tool fronting 450+ actions: actors, Blueprints, UMG, materials, Niagara, PCG, Level Sequences, cameras, Movie Render Queue, Take Recorder, PIE runs, screenshots, Python execution, packaging.
- Install: from Fab (no compiler) or build from source, which needs a C++ project (README). Then enable the plugin and turn on "Enable Native MCP Server," restart. Claude Code can connect over HTTP directly or through the npx stdio proxy.
- Account or payment: Fab listing exists, the README does not state its price. UNVERIFIED whether Fab is free. Source build is free.
- Security (README Security section): loopback only, per-project capability token at `<Project>/Saved/MCP/capability-token`, consent grant for destructive writes, asset paths limited to /Game, /Engine, /Script, /Temp, /Niagara, console commands that chain or quit the editor are blocked. It can run Python in the editor, so it executes arbitrary code by design. The README claims were not tested by me.
- Fit for Zac: HIGH as backup. Much larger action surface than Epic's experimental plugin, and it covers Level Sequences and Movie Render Queue, which the animation work needs. Third-party C++ plugin inside his engine is the trade.

## 4. db-lyon/ue-mcp

- Repo: https://github.com/db-lyon/ue-mcp. MIT, 462 stars, latest v1.4.11 on 2026-10-29, pushed 2026-10-31 (GitHub API).
- README: 30 category tools, 2114+ actions, a C++ bridge plugin deployed by `npx ue-mcp init`, and on UE 5.8+ it surfaces Epic's native toolset registry as `epic_*` actions. Detects Claude Code. Has `npx ue-mcp doctor`.
- UE 5.8: claimed by the README, UNVERIFIED by me.
- Security notes: `init` deploys and compiles a C++ plugin into the project and enables engine plugins, which modifies the project. Uses a WebSocket from a Node process to the editor. Auth model not read, UNVERIFIED.
- Fit: MEDIUM. Interesting because it wraps Epic's own toolsets, but it is the youngest of the three and does the most automatic project modification. Watch list.

## 5. Poly Hammer BlenderTools: Send to Unreal and UE to Rigify

- Repo: https://github.com/poly-hammer/BlenderTools (owner poly-hammer). Fork of Epic's repo, README says it is "maintained by @JoshQuake and volunteers... not affiliated with Epic Games."
- License: MIT, Copyright Epic Games 2020 to 2024 (LICENSE.md). 653 stars. Last release "Send to Unreal 2.6.7" on 2025-11-23. Last commit 2026-05-27. Not archived. (GitHub API)
- Blender 5.x: a Nov 2025 commit fixes addon preferences for Blender 5.0, and `__init__.py` on main declares minimum Blender 3.6 and version 2.6.9 (not yet released). The CI test matrix only lists Blender 3.6 and 4.2. So 5.x works at least at the preferences level, but 5.2 is UNVERIFIED.
- UE 5.8: CI only tests UE 5.3 and 5.4. The quickstart has a note for UE 5.5 and higher: set `Interchange.FeatureFlags.Import.FBX=False` in DefaultEngine.ini to use the legacy FBX importer. UE 5.8 is UNVERIFIED.
- What it does: one-click send of static meshes, skeletal meshes, animation sequences and grooms from an Export collection. Uses Unreal's Python Remote Execution.
- Install: Blender add-on zip, enable "Python Editor Script Plugin" and Remote Execution in UE. Remote execution uses UDP multicast and a TCP command channel (quickstart; the specific ports 6766 and 6776 appear on Unreal Bridge's page, not this one).
- Security: Python Remote Execution lets any local process that reaches that port run Python in the editor. Keep bind address at 127.0.0.1 (the doc's Windows default). No phone-home found.
- Docs site loads Google Analytics, which only affects someone reading the docs.
- Fit: MEDIUM, backup. Trusted lineage and MIT, but test coverage is two versions behind Zac's setup. No camera or Sequencer story in the README.

## 6. botero-dev/bl_datasmith (Blender Datasmith)

- Repo: https://github.com/botero-dev/bl_datasmith. Owner botero-dev (Andres Botero). This is also where the old 0xafbf/blender-datasmith-export repo redirects.
- License: the LICENSE.txt says files carry multiple licenses, the `addons/bl_datasmith` directory is AGPL. GitHub shows NOASSERTION. The Unreal-side plugin license was not read. UNCLEAR, do not redistribute without reading it.
- 512 stars, v1.1.12a on 2026-02-10, last commit 2026-02-10. Not archived.
- Blender 5.x: CHANGELOG v11 (2025-12-10) "Added support for Blender 5.0."
- UE 5.8: release zips stop at UE 5.7 (bl_datasmith-12-UE_5.7.zip). Nothing for 5.8. Could be rebuilt from source per BUILDING.md, but that is more work than the others.
- What it does: scene hierarchy, meshes, textures, material node graphs, instanced meshes, lights, cameras, object transform animation. Also imports Datasmith into Blender.
- Known gotcha from README: the `blender_curves` texture must be set to HDR uncompressed after import, or use the bundled Dataprep asset.
- Fit: LOW today. Right idea for whole-scene transfer, but no UE 5.8 build and a copyleft license.

## 7. Unreal Bridge (Tachyon Studio, Superhive)

- Page: https://superhivemarket.com/products/unreal-bridge/docs. Not a GitHub repo found by me. Paid: $14.99 one seat, 12 months of updates.
- License: GPL-3.0-or-later (vendor page). Version 1.0.0, published about a month ago, no exact date.
- Blender 3.3 to 5.2, UE 5.2 to 5.8, Windows only (vendor page). Vendor claim, not tested.
- One-way Blender to Unreal. Exports FBX to a staging folder and imports through Python Remote Execution, with an optional Live Sync. UDP 6766 discovery and TCP 6776 commands, localhost only. A "Do It For Me" button edits the `.uproject` and `Config/DefaultEngine.ini` and saves `*.tul-backup` first. Destinations forced under /Game.
- Fit: MEDIUM. The only commercial tool found that names UE 5.8 and Blender 5.2, but it is a month old with one version, and Zac asked for a GitHub repo. Nothing here beats candidate 1 on features.

## 8. Blender To Unreal Live Link (Milad Kambari, Superhive)

- Source: https://digitalproduction.com/2026/03/27/real-time-blender-to-unreal-live-link/ (article by Bela Beier) and the ArtStation page. $18. Blender 5.0+, UE 5.5+, Windows, both apps on one machine. No GitHub repo, license not stated.
- Sends selected objects or full scene, live sync, bakes complex materials to textures. Article does not mention cameras or animation.
- Fit: LOW. Meshes and materials only as far as I can see, closed source script files that run in both apps.

## 9. runreal/unreal-mcp

- https://github.com/runreal/unreal-mcp. MIT, 117 stars, release 0.1.1 on 2025-06-03, last push 2025-06-06. No push in about 17 months.
- Uses Unreal's Python Remote Execution, no plugin. Needs UE 5.4+ per a search summary (third-party listing). UE 5.8 UNVERIFIED.
- Fit: SKIP, abandoned by the 12-month rule.

## 10. tahooki/unreal-blender-mcp

- https://github.com/tahooki/unreal-blender-mcp. No license, 21 stars, last push 2025-03-19. Details only from lobehub mirror pages, not read from the repo.
- Claims an MCP hub with a Blender socket server (8400/8401) and an Unreal Python HTTP server (8500). That is a second Blender addon next to Zac's mcp-for-blender.
- Fit: SKIP. Abandoned, unlicensed, and it duplicates what he already has.

---

## What the built-in routes can do (not repos)

- UE 5.8 release notes show Interchange USD fixes in 5.8.1, 5.8.2 and 5.8.4 (MaterialX baking, USD pregen imports, skinned meshes, geometry caches). So USD import through Interchange is alive on 5.8. Source: the 5.8 release post above. The post says nothing about glTF or Blender.
- Poly Hammer's own docs say that from UE 5.5 the default Interchange FBX importer causes trouble for Send to Unreal and tell users to switch to the legacy FBX importer. That is a real friction point for any FBX based tool, including xavier150's, on a 5.8 project. UNVERIFIED whether xavier150's scripts hit the same issue (its 4.4.6 notes mention an `InterchangePipeline` fix for UE 5.0, so it uses Interchange at least partly).
- Blender-side USD, glTF and FBX export are built into Blender. I did not verify Blender 5.2 specifics.

---

## RECOMMENDATION

Primary pick, content pipeline: **xavier150 Blender For UnrealEngine Addons** (GPL-3.0, v4.4.8). It is the only free GitHub tool I found that names both Blender 5.2 and UE 5.8 in its release notes, it is actively committed (last commit 2026-10-08), and it covers cameras and Sequencer and animation, which is the work the Animation department will do.

Primary pick, Claude driving Unreal: **Epic's own Unreal MCP plugin** that ships with 5.8. No third-party code, version-matched, loopback only. Accept that Epic calls it Experimental.

Backup, content: **Poly Hammer Send to Unreal** (MIT). Best-known tool, live Python remote execution, but CI stops at Blender 4.2 and UE 5.4.

Backup, Claude driving Unreal: **ChiR24 Unreal_mcp / EngineWire** (MIT, v0.6.0, 2026-10-27). Bigger action surface including Level Sequences and Movie Render Queue, with a token and consent model. Use it if Epic's toolsets turn out too thin for sequencer work.

Suggested order of first test, when Zac says go: (1) enable Epic's Unreal MCP in a scratch UE 5.8 project and run `ModelContextProtocol.GenerateClientConfig ClaudeCode`; (2) install xavier150's `blender_5.0-5.2.zip` in a scratch Blender profile, export a cube, one rigged character with an action, and one camera; (3) check the Interchange FBX issue above on 5.8.4.

## Decisions for Zac

1. OK to run the first test above in scratch projects (nothing installed until he says yes)?
2. Is paying $14.99 for Unreal Bridge acceptable if xavier150's tool fails on 5.8.4, or GitHub-free-only?
3. Allow a third-party C++ plugin (EngineWire or ue-mcp) into the engine, or Epic's built-in only?
4. Keep Epic's MCP auto-start off by default (no authentication layer)? Recommended yes.

## What I could not verify

- That any tool works on Blender 5.2.4 RC and UE 5.8.4 specifically. Only version claims in release notes and vendor pages. Nothing was run.
- Epic's Unreal Engine EULA terms for the built-in MCP plugin, and which asset import and Sequencer toolsets it ships. The doc page does not list them.
- Whether Epic's Unreal MCP exposes import and Sequencer tools. db-lyon's count of 830 native tools is its own claim.
- Fab price and exact UE 5.8 build date for EngineWire.
- Source code of every candidate. I read READMEs, release notes, vendor pages and API metadata only, so "no phone-home" means none is stated, not that none exists.
- The Unreal-side license for bl_datasmith.
- Unreal Bridge's exact release date, source repo, and real-world quality. Blender To Unreal Live Link has no repo and no stated license.
- Whether the Interchange FBX default issue noted by Poly Hammer for 5.5+ still applies in 5.8.
- USD and glTF workflow details for Blender 5.2 to UE 5.8, which the general web search did not surface from Epic or Blender docs.
- Star counts and dates are as of 2026-10-31 and move daily.

## Sources

- https://github.com/xavier150/Blender-For-UnrealEngine-Addons (API: repo, releases v4.4.6 to v4.4.8)
- https://github.com/poly-hammer/BlenderTools (API: repo, releases, commits, tests.yml, quickstart.md, LICENSE.md)
- https://github.com/EpicGames/BlenderTools (API: repo moved from EpicGamesExt, last release 2023-11-09, a docs-only push 2026-09-03)
- https://github.com/ChiR24/Unreal_mcp (API and README)
- https://github.com/db-lyon/ue-mcp (API and README)
- https://github.com/botero-dev/bl_datasmith (API, README, CHANGELOG, LICENSE.txt)
- https://github.com/runreal/unreal-mcp, https://github.com/tahooki/unreal-blender-mcp, https://github.com/chongdashu/unreal-mcp, https://github.com/flopperam/unreal-engine-mcp (API)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor
- https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274
- https://superhivemarket.com/products/unreal-bridge/docs
- https://digitalproduction.com/2026/03/27/real-time-blender-to-unreal-live-link/
