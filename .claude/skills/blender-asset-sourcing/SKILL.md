---
name: blender-asset-sourcing
description: How the asset-scout agent finds existing 3D models, textures and HDRIs properly for Zac's Animation department, and records exactly what license each came with. Use whenever someone needs a ready-made model, prop, character, rig, texture, HDRI or environment instead of building one, says "find an asset", "is there a free model of", "search Poly Haven or Sketchfab", "can we use this model", "license", "attribution", "CC0", "CC-BY", or "import_asset". Covers where to look, license reading, the blender MCP search_assets and import_asset tools, vetting, the attribution log CSV, and the free-only spend rule.
---

# Blender asset sourcing

Verified 2026-10-31: MCP tool schemas read directly; addon status could NOT be read this session because Blender was not running (handshake failed, so every library showed "unknown"). Zac told us polyhaven, sketchfab and polypizza are all switched off in his setup; that is taken as given, not re-verified. Sources in references.md.

## 1. The two hard rules

1. **Free and properly licensed only.** Anything that costs money, credits, a subscription, or a paid API call goes to Zac first with the exact price, the seller, and the license. Do not click Buy, do not top up, do not start a trial. No exceptions, including "just 1 credit".
2. **Every asset used gets a log line** in `D:\WKP\data\assets\animation-asset-log.csv` before it is used in a deliverable. No log line, no use.

If a license is unclear, treat it as not allowed and ask Zac. Never assume.

## 2. WKP use cases decide which license works

WKP content is commercial (monetized YouTube, Etsy, sponsored work, client jobs). So:

| License | Use in WKP | Obligation |
|---|---|---|
| CC0 / Public Domain | Yes | None. Logging the source anyway. |
| CC-BY (any version) | Yes | Credit the creator: title, author, license, link. Put it in the video description or credits and in the log. |
| CC-BY-SA | Ask Zac | ShareAlike can force the same license onto the result. Not safe for combined works. |
| CC-BY-ND | Ask Zac | No derivatives: any modification of the model (rescale is fine, edits are not) is out. |
| CC-BY-NC / NC-SA / NC-ND | NO | Creative Commons: NC prohibits uses "primarily intended for commercial advantage or monetary compensation". WKP is a business. Reject. |
| Sketchfab "Standard" license (free models) | Ask Zac | Read the terms on the model page; Sketchfab says NoAI tag stays enforceable on Standard-licensed downloads. |
| Fab "Standard License" free assets | Ask Zac | Epic staff say it permits commercial use; the EULA is the binding text (forum posts only, UNVERIFIED). Tiers by revenue (Personal under 100k USD) are community-reported, UNVERIFIED. |
| "Editorial" license | NO | Cannot be used in commercial projects. |
| "Personal use only", "no commercial", or no license shown | NO | Reject. |
| Unknown / ripped from a game or film | NO | Copyright risk. Reject. |

Clauses to look for on every page:
- "No AI" / NoAI tag: the author prohibits generative-AI use. WKP builds animation by hand, but if the asset gets fed into an AI image or video tool (e.g. as a reference for Firefly or Higgsfield), that may violate it. Log it as `noai=yes` and do not use such an asset in any AI step.
- "Created with AI" tag: generated model, copyright status uncertain. Prefer other assets.
- Trademarked characters, logos, real people, branded products: not covered by a CC license even if the mesh is CC0. Skip them.
- Texture packs inside the model may carry a different license than the mesh.

Copy the exact license text or name and the URL into the log. Do not paraphrase the license name ("free to use" is not a license).

## 3. Where to look (in order)

1. **Poly Haven** (polyhaven.com): HDRIs, PBR textures, realistic models, all CC0, no attribution required (credit appreciated). Their license page says assets may be used "for any purpose". Best first stop for lighting and surfaces. Trust: high.
2. **Blender Studio** (studio.blender.org characters and assets): production-grade rigged characters (Rain, Snow, Huginn, Einar/Alpha, Vincent, Dog, Cat and others). Pages show CC-BY with a required credit line, e.g. "Snow Rig (CC) Blender Foundation | studio.blender.org". Some entries (Dog, Cat) may need a Blender Studio subscription for the download (user comment, UNVERIFIED). A subscription costs money, so it goes to Zac first. Trust: high for rig quality.
3. **Poly Pizza** (poly.pizza): stylised low-poly, CC0 or CC-BY per model; includes the Google Poly archive (mostly CC-BY). The blender tool supports `licence="CC0"` or `"CC-BY"` filter. Check each model page; poly.pizza's own license page could not be fetched (UNVERIFIED).
4. **Sketchfab** (sketchfab.com): huge, mixed quality, mixed licenses. Filter to "Downloadable". Per-model license: CC0, CC-BY, CC-BY-SA, CC-BY-ND, CC-BY-NC variants, or Standard. Use the license filter in the search. Treat as the riskiest source; read each page.
5. **Fab** (fab.com, Epic): free assets under CC-BY or Fab Standard License; NoAI tag exists. Assets tend to be built for Unreal. Free monthly packs are fine if the listing shows price zero and the license.
6. **Other CC0 sources** (check each site's license page before first use, all UNVERIFIED this session): ambientCG (CC0 textures), Kenney.nl (CC0 game assets), Quaternius (CC0 low-poly characters and props), OpenGameArt (mixed, check each), BlenderKit (free tier exists but some assets need a subscription; ask Zac).
7. Blendswap and itch.io free assets: mixed; many are CC-BY-NC. Reject unless the page shows an allowed license.

## 4. The blender MCP tools

`search_assets` (verified from the tool schema):
- `source`: `polyhaven`, `sketchfab`, `polypizza`.
- `query`: plain words. `asset_type` (polyhaven only): `hdris`, `textures`, `models`, `all`. `category` (path for polyhaven e.g. "Metal/Sheet & Corrugated", comma list for sketchfab, name for polypizza). `attributes` (polyhaven filters; unknown key returns the valid keys). `min_size_m` (polyhaven: minimum real-world size). `licence` (polypizza only: "CC0" or "CC-BY"). `animated` (polypizza only). `limit`. `previews` (thumbnails for first N, max 6; polyhaven and sketchfab).
- Returns each asset's id for `import_asset`.

`import_asset` (verified from the tool schema):
- `source`, `id` (sketchfab UID), `asset_type` (polyhaven, required), `target_size` in metres of the largest dimension (required for sketchfab, recommended for polypizza; library models arrive at arbitrary scale), `apply_to` (polyhaven textures: object names to receive the material, otherwise the material is unused and lost on save), `resolution` (1k, 2k, 4k, 8k; 1k to 2k for background, 4k for close-ups), `file_format`.
- After import: read the reported world bounding box, size it, put it on the ground, `look` at it.

Status in Zac's setup: all three libraries are OFF (Zac's statement). `get_addon_status` shows `libraries` on or off and `generators`. If a library is off:
- Do not try to enable it from code. Tell Zac: "Open Blender > Preferences > Add-ons > Interface: Blender MCP (the addon panel), switch on <library>". Some sources need an API key (Sketchfab needs a token, UNVERIFIED which of the three need keys; ask Zac to click and see). Wait for his OK.
- Meanwhile, search the web through browser or WebFetch for the asset page, read the license, and put it in the shortlist for Zac.
- Manual route when a library is off: download the file (only if the license passes and it is free) into `D:\WKP\assets\animation\<source>\<name>\` with the license text saved beside it as `LICENSE.txt` and the page URL in `SOURCE.txt`; then import via `bpy.ops.wm.obj_import` / `import_scene.gltf` / `import_scene.fbx` in a scratch scene. Confirm that path with Zac the first time (not established in LOCAL-PATHS.md).

`generate_3d` is NOT sourcing. It is the AI generator tool and may cost credits; see `blender-character-craft` section 11 and ask Zac first.

## 5. Vetting checklist (run on every candidate before importing into a deliverable)

Page check (before download):
- [ ] License is allowed per section 2. Copy exact text and URL.
- [ ] Creator named. Original page, not a re-upload of someone else's work.
- [ ] Not a trademark/IP character, not scanned from a real person without release.
- [ ] Price is zero (not "free trial", not "free with subscription").
- [ ] Not tagged NoAI if any AI step is planned.
- [ ] File format fits: `.blend`, `.glb/.gltf`, `.fbx`, `.obj`.

File check (after import to a TEST_ or scratch scene, never into Zac's scene):
- [ ] Dimensions: real-world metres correct (`target_size` used). Door about 2.0 m, human 1.8, cup 0.1.
- [ ] Tris within the budget for its use (see `blender-asset-quality`): background under 1,500, prop under 5,000, hero prop under 30,000.
- [ ] Textures present and load (no pink or black), power-of-two, correct colour spaces, normal map convention OpenGL vs DirectX noted.
- [ ] Run `audit_asset.py` (blender-asset-quality) and paste numbers.
- [ ] Rigged models: bones named sensibly, root at origin, weights complete, no extra junk, deforms in extreme poses (shoulder up, knee bent). Check `get_scene_info` weights field.
- [ ] File hygiene: no hidden junk objects, no unrelated cameras or lights, no `.001` names, scale 1, no external file dependencies missing.
- [ ] Looks right from 3 angles with `look` and does not clash with the project's style.

Verdict: ACCEPT / ACCEPT WITH FIXES (list) / REJECT (reason). Never import anything into the project scene without the verdict.

## 6. Attribution log

File: `D:\WKP\data\assets\animation-asset-log.csv`. The header row exists; append one row per asset. Use Python's `csv` module so commas in titles are quoted. Dates `YYYY-MM-DD`.

Header:
`date_logged,asset_name,source,source_url,creator,license,license_url,attribution_required,attribution_text,commercial_ok,noai_tag,price_paid,file_path,used_in_project,vetted_by,verdict,notes`

Rules:
- `attribution_text` is the exact credit line to paste in descriptions, e.g. `Snow Rig (CC) Blender Foundation | studio.blender.org`.
- `price_paid` must be `0`. A non-zero value means Zac approved a purchase; put his message date in `notes`.
- `commercial_ok` is `yes` or `no`. `no` rows are logged to prevent re-use.
- Rows are never deleted. Rejected assets stay with `verdict=REJECT`.
- The producing agent copies every `attribution_text` into the deliverable's description file so credits are not lost.

## 7. Spend rule (restated)

Free and properly licensed only. A price, a credit, a subscription, an API paid tier: stop and send Zac one message with: asset or service, exact price, what it unlocks, license, and a free alternative if any. Do not buy first and report after. Do not use `generate_3d` without his OK.

## 8. Output to the requesting agent

```
REQUEST: <what was asked>
SHORTLIST (max 5): name | source | url | license | attribution needed | tris | size | verdict
RECOMMENDED: <one> because <reason>
LOG ROWS ADDED: <n>
OPEN: anything needing Zac (library switched off, price, unclear license)
```
