---
name: ue-scene-lighting-render
description: How to create, light, shoot and render scenes in Unreal Engine 5.8 on an 8 GB RTX 5060 and get the best final image. Use for new project settings (template, Lumen vs baked, Nanite, Virtual Shadow Maps, hardware ray tracing, DX12 SM6, scalability), outdoor and interior lighting rigs (Directional Light, Sky Atmosphere, SkyLight, Exponential Height Fog, post process exposure), master materials, CineCamera and depth of field, Sequencer, Movie Render Queue or Movie Render Graph settings for stills and video, turntables and three-point character showcase rigs, performance profiling (stat unit, stat gpu), packaging, and the finished-shot quality checklist. Written for the ue-scene-builder agent.
---

# ue-scene-lighting-render

Owner: ue-scene-builder. Engine 5.8.4 at `D:\Epic\UE_5.8`. Hardware: RTX 5060 (8 GB VRAM class), driver 621.01, 32 GB RAM, Ryzen 7 8700F, Windows 11. Projects `D:\Unreal Projects`. Shader/derived data cache `D:\UE_DDC` (env var `UE-LocalDataCachePath`; do not move it). Free tools only; ask Zac before any spend or download.

Evidence tags: VERIFIED-5.8 (read from the install or 5.8 notes), DOC-5.x (Epic docs from an earlier 5.x), COMMUNITY (widely repeated practice), UNVERIFIED (could not confirm for 5.8; test on a throwaway scene).

Rules: do not open the editor without a task; do not edit `D:\Epic\UE_5.8`; write scene notes and settings dumps to `D:\WKP\scratch\`; deliverables per `LOCAL-PATHS.md` and `D:\WKP Reports\`. Anything that opens a network port is Zac's yes first (see `ue-mcp-and-automation`).

---

## 1. New project settings for this GPU

### Template
- Cinematic/showcase work: start from the Blank template (`TP_Blank` or `TP_BlankBP` exist in 5.8, VERIFIED-5.8). Its `DefaultEngine.ini` already sets `r.AllowStaticLighting=False`, `r.Shadow.Virtual.Enable=1`, `DefaultGraphicsRHI=DefaultGraphicsRHI_DX12`, and D3D12 targeted shader format `PCD3D_SM6` (VERIFIED-5.8).
- Alternate: `TP_PhotoStudioBP` for product/character look-dev (exists in 5.8 Templates list, VERIFIED-5.8; contents untested, UNVERIFIED), `TP_ME_CineBP` for cinematic work (UNVERIFIED contents).
- Project creation: Blueprint (no code), Starter Content off, Raytracing off in the wizard if offered, Target Platform Desktop, Quality Maximum. Name with no spaces.

### Project Settings to confirm (Edit > Project Settings > Engine > Rendering)
| Setting | Value | Why |
|---|---|---|
| Default RHI | DirectX 12 | VERIFIED-5.8 template default; required for SM6 features. |
| Shader Model | SM6 (D3D12 Targeted Shader Formats = SM6) | Needed for Nanite and Lumen on current paths. Remove SM5 to cut shader compile time and disk. |
| Dynamic Global Illumination Method | Lumen | DOC-5.x |
| Reflection Method | Lumen | DOC-5.x |
| Generate Mesh Distance Fields | on | Required by software Lumen (DOC-5.x). |
| Use Hardware Ray Tracing when available | OFF | See section 2. |
| Support Hardware Ray Tracing | OFF at creation | Turning it on adds shader permutations and BVH memory. |
| Shadow Map Method | Virtual Shadow Maps | Template default. |
| Allow Static Lighting | off | Lumen-only project (`r.AllowStaticLighting=False`). |
| Nanite | on (default) | See ue-import-pipeline section 6 for eligibility. |
| Anti-Aliasing Method | Temporal Super Resolution (TSR) | Best quality; MSAA not supported with Nanite (DOC-5.x). |
| Auto Exposure | per scene (section 5) | |

Config lines (project `Config/DefaultEngine.ini`, `[/Script/Engine.RendererSettings]`):
```
r.GenerateMeshDistanceFields=True
r.DynamicGlobalIlluminationMethod=1
r.ReflectionMethod=1
r.Shadow.Virtual.Enable=1
r.AllowStaticLighting=False
r.RayTracing=False
```
(`r.DynamicGlobalIlluminationMethod=1` and `r.ReflectionMethod=1` mean Lumen; names are long-standing 5.x cvars; confirm in the Details panel, UNVERIFIED value mapping in 5.8.)

---

## 2. Lumen vs baked, Lumen Lite, hardware ray tracing

- Dynamic (Lumen): default for new projects; no lightmaps, no bake wait, works with moving lights (DOC-5.x). Choose this.
- Baked (Lightmass/GPU Lightmass): only for tiny VRAM targets or heavily static archviz; needs lightmap UVs and Allow Static Lighting. Do not use here.
- Lumen Lite (Beta): 5.8 adds a medium-quality GI mode using Irradiance Fields with Probe Occlusion, roughly twice as fast as high quality; default on handheld consoles, supported on PC (VERIFIED-5.8 release notes). In the installed `BaseScalability.ini`, `GlobalIlluminationQuality@1` (Medium) sets `r.Lumen.FinalGatherMethod=0` (Irradiance Volume), `r.LumenScene.SurfaceCache.AtlasSize=2048`, `r.Lumen.TraceMeshSDFs.Allow=0`, `r.Lumen.HardwareRayTracing.HitLighting.Allowed=0` (VERIFIED-5.8). Quality `@2` (High) switches to `FinalGatherMethod=1` with Screen Probe Gather, atlas 3584, downsample 32 (VERIFIED-5.8).
- Use: Scalability GI Quality 2 (High) for stills and interactive look-dev; Quality 3 (Epic) and Cinematic (`@Cine`) only for final renders (section 7), where VRAM is spent once per render.
- Hardware ray tracing (HWRT): OFF by default. Reasons on this card (COMMUNITY plus DOC-5.x tradeoffs): (1) BVH and hit-lighting memory pushes an 8 GB card into spill; (2) Epic notes scenes above 100,000 instances pay large scene-update cost (DOC-5.x); (3) software Lumen with Detail Tracing already looks right for Zac's scenes; (4) more shader permutations and compile time. Turn HWRT on only for a specific shot where reflections on glass/water are wrong, and only for the final render.
- Software ray tracing mode: Detail Tracing (per-mesh SDF, best) for hero shots; Global Tracing (fastest) for large worlds (DOC-5.x).

### Post Process Volume Lumen settings (DOC-5.x; ranges in the editor)
| Setting | Start value | Raise when |
|---|---|---|
| Lumen Scene Lighting Quality | 1 | Indirect light looks blotchy: 2 |
| Lumen Scene Detail | 1 | Small props missing from GI: 2 |
| Final Gather Quality | 1 | Noise in shadows: 2 to 4 (GPU cost) |
| Max Trace Distance | 20,000 | Light leaks in caves/large rooms: raise; too small leaks light (DOC-5.x) |
| Reflections > Quality | 1 | Mirror look needs: 2 |
| Lumen Scene Lighting Update Speed | 1 | Fast lighting changes: 2 to 4 |
| Skylight Leaking | 0 | Light bleeding in sealed interior: lower sky contribution instead of raising this |

Rules from Epic: emissive materials light the scene through Final Gather at no extra cost, but tiny bright emissive areas cause noise, so use real lights for small hot sources (DOC-5.x). Lights with Static mobility are not supported with Lumen (DOC-5.x). Global lighting changes (turning off the sun) take seconds to settle; wait before capture.

---

## 3. Memory budget for 8 GB VRAM

Targets (COMMUNITY, adjust after profiling):
- Textures: stay under about 3.5 GB resident. Use 2K for props, 4K only for hero characters and landscape detail. Keep Texture Streaming on (`r.TextureStreaming=1`), pool `r.Streaming.PoolSize=3000` (MB) as a starting point.
- Virtual Shadow Maps: leave on; if the pool warning appears set `r.Shadow.Virtual.MaxPhysicalPages` lower (UNVERIFIED default in 5.8) or reduce the number of shadow-casting local lights.
- Lumen Scene: keep Surface Cache atlas at the scalability value; do not raise `r.LumenScene.SurfaceCache.AtlasSize` manually beyond 3584 without profiling (VERIFIED-5.8 default for High).
- Screen percentage: editor viewport 100% with TSR upscaling from 67% while building; final render at 100% (section 7).
- Light count: at most 4 shadow-casting dynamic lights in frame for interactive work; unlimited for final if stat gpu is fine.
- Viewport: keep one viewport, Realtime on only when needed. Close the Content Browser sidebar thumbnails at 8 GB when streaming stalls.
- Scalability (editor top-right Settings > Engine Scalability Settings): Epic (3) for look-dev when stat unit shows frame under 33 ms; High (2) if above; Cinematic for renders. Scalability groups from `BaseScalability.ini`: ViewDistance, AntiAliasing, Shadow, GlobalIllumination, Reflection, PostProcess, Texture, Effects, Foliage, Shading, Landscape (names VERIFIED-5.8 in part: ViewDistanceQuality, ShadowQuality, GlobalIlluminationQuality exist with `@0..@3` and `@Cine`).

---

## 4. Lighting rules

### Outdoor (day or dusk) rig, in this order
1. Directional Light (the sun). Mobility Movable. Intensity (Lux) 8 to 10 for noon, 3 to 5 for golden hour. Light Source Angle 0.5357 (real sun). Atmosphere Sun Light on, index 0. Temperature off (let atmosphere color it). Cast Shadows on, Cast Cloud Shadows if clouds are used.
2. Sky Atmosphere. Defaults fine. Rotate the Directional Light to set time of day (pitch -10 to -20 degrees for golden hour, -45 to -60 for midday).
3. SkyLight. Mobility Movable, Real Time Capture on, Source Type SLS Captured Scene. Intensity 1. Add a Volumetric Cloud (optional, GPU cost) and Height Fog.
4. Exponential Height Fog. Fog Density 0.01 to 0.03, Start Distance 0 to 500, Volumetric Fog on for god rays (costs GPU; budget 1 to 2 ms). Directional Inscattering Color matches sun.
5. Post Process Volume, Infinite Extent (Unbound) on. Exposure: Metering Mode Manual for stills and sequences (see section 5).

### Interior rig
- Sun + Sky through windows, Rect Lights at windows (Source Width/Height matching the opening, Intensity 5 to 20 cd), plus a low-intensity SkyLight. Add Lumen-friendly walls at least 10 cm thick (COMMUNITY), no gaps at corners.
- Use Rect Lights and Spot Lights with Inverse Squared Falloff on and physical units (cd/lumens), not arbitrary values.
- Avoid dozens of small point lights. Merge into a few rect/spot lights plus emissive.

### Showcase (studio) rig
See section 9.

### Common errors
| Symptom | Fix |
|---|---|
| Whole scene bright white or crushed | Set exposure manually (section 5). |
| Light leaking indoors | Thicker walls, close meshes, lower Skylight intensity, keep distance fields on. |
| Flickering GI | Raise Final Gather Quality or lower Update Speed; check emissive hot spots. |
| Shadows blotchy | Enable Virtual Shadow Maps, check light Source Angle/Radius, avoid two overlapping Directional Lights. |
| Fog invisible | Enable Volumetric Fog on the Exponential Height Fog and raise Extinction Scale slightly. |

---

## 5. Exposure and post process

- Auto Exposure fights cinematic work. For any rendered shot set Post Process Volume > Exposure > Metering Mode = Manual, then Exposure Compensation (EV100): 13 to 14 for bright sun, 9 to 10 for interiors, 5 to 7 for night. With Manual metering, Exposure Compensation acts as absolute EV100 (DOC-5.x behavior; verify on a test frame).
- Alternative: Min/Max EV100 both equal.
- Tone mapper: leave defaults (ACES-style Filmic in 5.x; the rendering pipeline may use AgX/other options in 5.8, UNVERIFIED). Do not stack grading until exposure is right.
- Bloom: Intensity 0.3 to 0.675 (default 0.675). Lens Flare off unless wanted. Vignette 0.2 to 0.4. Film Grain 0 to 0.1 for slight texture. Chromatic Aberration 0 to 0.2.
- Motion Blur: on for video (Amount 0.5), off for stills.
- Color grading: use Global Gamma/Saturation sparingly; do final look in Resolve/Premiere with a LUT if needed.

---

## 6. Materials

- One master material per surface class: `M_Master_Opaque`, `M_Master_Masked`, `M_Master_Glass`. All textures and scalar/vector inputs exposed as parameters. Every object uses a `MI_` instance (Epic prefixes `M_`, `MI_`).
- Keep instruction count low: check Window > Shader Complexity or Material Editor > Stats; aim under 200 pixel shader instructions for background, under 400 for hero (COMMUNITY).
- Prefer Opaque and Masked. Translucent blend mode costs overdraw and is not supported by Nanite (DOC-5.x). Use Dithered Opacity or Masked for foliage.
- Avoid: Custom expression nodes on Nanite meshes, large World Position Offset on Nanite meshes, multiple unique full materials per prop, 4K textures on small props.
- Use Substrate materials only if enabled in the project; 5.8 interchange imports use Substrate glTF parents (`/InterchangeAssets/gltf/Substrate/M_GLTF`, VERIFIED-5.8). Substrate on/off project default in 5.8: UNVERIFIED. Do not mix.
- Texture streaming: leave sRGB and compression per ue-import-pipeline section 8.

---

## 7. Sequencer and Movie Render Queue

### Sequencer set-up
1. Content Browser > Cinematics > right-click Animation > Level Sequence (`LS_<ShotName>`).
2. Add a CineCamera Actor (Place Actors > Cinematic > Cine Camera Actor), add it to the sequence as a Camera Cut track binding.
3. Frame rate 24 fps for cinematic, 30 or 60 for web/social. Playback range: set exactly; Work Range same.
4. Keyframe the camera (transform), focal length and focus distance if animating.
5. Lock the viewport to the camera (Pilot) and enable Safe Frames (Show > Safe Frames).

### Movie Render Queue (Window > Cinematics > Movie Render Queue)
The Movie Render Graph is Production Ready in 5.8 and new features are graph-only (VERIFIED-5.8 release notes); the classic Movie Render Queue config still works. Use the graph for new work; the classic settings below map to the same concepts.

| Setting | Stills (hero frames) | Video |
|---|---|---|
| Output > Resolution | 3840x2160 (or 7680x4320 via High Resolution tiling) | 1920x1080 or 3840x2160 |
| Output format | PNG (8-bit) or EXR (16-bit, for grading) | EXR sequence or PNG sequence, encode with ffmpeg |
| Anti-Aliasing > Spatial Sample Count | 8 to 16 | 1 to 4 |
| Anti-Aliasing > Temporal Sample Count | 1 to 16 (more for motion blur) | 4 to 8 |
| Anti-Aliasing > Override Anti-Aliasing | None (use accumulated samples; disables TSR) | Temporal Super Resolution off |
| Warm Up Frame Count | 32 | 32 |
| Render Warm Up Count / Engine Warm Up | 64 | 32 to 64 |
| Deferred Rendering > Use 32-bit... | on for EXR | on for EXR |
| Console Variables (below) | yes | yes |
| Motion Blur | off | on |

Values are DOC-5.x and COMMUNITY conventions; the accumulated-sample model (Spatial x Temporal samples) is documented, the counts are tuning advice. For limited VRAM, render 1080p, then upscale or tile.

Console variables to add under Console Variables:
```
r.ScreenPercentage 100
r.Lumen.ScreenProbeGather.FullResolutionJitterWidth 0.5
r.Lumen.ScreenProbeGather.DownsampleFactor 4
r.LumenScene.SurfaceCache.AtlasSize 3584
r.Nanite.MaxPixelsPerEdge 0.5
r.Shadow.Virtual.ResolutionLodBiasDirectional -1
r.Streaming.FullyLoadUsedTextures 1
r.Streaming.MipBias 0
r.MotionBlur.Quality 4
sg.GlobalIlluminationQuality 3
sg.ShadowQuality 3
sg.PostProcessQuality 3
```
The Lumen and Nanite cvar names above are real 5.x names (Lumen ones also appear in 5.8 BaseScalability.ini, VERIFIED-5.8 for `r.Lumen.ScreenProbeGather.DownsampleFactor` and `r.LumenScene.SurfaceCache.AtlasSize`); the exact best value is a tuning choice, test on one frame.

Output file name format: `{sequence_name}/{shot_name}.{frame_number}` (tokens documented for MRQ, DOC-5.x). Output directory: `D:\Unreal Projects\<P>\Saved\MovieRenders\` or a path under `D:\WKP\scratch\renders\`.

Disk and time: EXR 4K frame is 30 to 60 MB; budget disk before rendering a sequence.

### Rendering from the command line (flags confirmed in 5.8 source)
Flags parsed in MovieRenderPipeline source (VERIFIED-5.8): `-LevelSequence=`, `-MoviePipelineConfig=`, `-MoviePipelineLocalExecutorClass=`, `-MoviePipelineClass=`, `-MovieSceneCaptureType=`, `-MovieSceneCaptureManifest=`, `-ExecutorPythonClass=`.
```
"D:\Epic\UE_5.8\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" "D:\Unreal Projects\<P>\<P>.uproject" /Game/Maps/L_Main -game -windowed -ResX=1920 -ResY=1080 -NoLoadingScreen -notexturestreaming -unattended -LevelSequence="/Game/Cinematics/Sequences/LS_Turntable" -MoviePipelineConfig="/Game/Cinematics/Presets/MPC_Final" -MoviePipelineLocalExecutorClass=/Script/MovieRenderPipelineCore.MoviePipelinePIEExecutor -forcelogflush
```
Executor class path and the need for `-notexturestreaming`: DOC-5.x / COMMUNITY, UNVERIFIED in 5.8. `-ResX/-ResY/-windowed/-NoLoadingScreen` are standard engine flags. Do not run until the caller approves launching the editor; first run it on a 10-frame range.

### Encoding
EXR/PNG sequence to MP4: `ffmpeg -framerate 24 -i frame.%04d.png -c:v libx264 -crf 14 -pix_fmt yuv420p out.mp4` (ffmpeg path in LOCAL-PATHS.md). ProRes 4444 for editing in Premiere (note: ProRes froze on Zac's machine in earlier WWD work, use H.264 MP4 unless told otherwise).

---

## 8. Cameras

CineCamera Actor settings (DOC-5.x):
- Sensor: Filmback preset "Super 35mm 16:9" for film look; "Digital Film" for general; aspect 16:9.
- Focal length: 24 mm environment, 35 mm general, 50 mm portrait/character, 85 to 135 mm hero close-up, 14 to 18 mm dramatic wide. Keep character shots at 50 mm or longer to avoid distortion.
- Aperture (f-stop): f/2.8 to f/4 for shallow DOF, f/8 to f/11 for deep focus.
- Focus: Manual Focus Distance with a Tracking Focus target on the subject; check with Show > Camera Debug / Focus Plane. Use "Draw Debug Focus Plane" while setting.
- Depth of field cost: Cinematic DOF is costly; in MRQ use accumulation. 5.8 adds Accumulation Depth of Field in the Movie Render Graph (rendered from multiple aperture viewpoints, cost linear in sample count, VERIFIED-5.8 release notes).
- Composition: rule of thirds, eye line at upper third, leave look room, subject separation from background by light or DOF.

---

## 9. Character and creature showcase

### Turntable
- Place the model on a floor plane (`SM_Plane`, 10 m x 10 m, neutral gray M_Matte, roughness 0.8).
- Parent the mesh to an empty Actor (`BP_TurntablePivot`) at the mesh center on the floor. In the Level Sequence, rotate the pivot yaw 0 to 360 across the shot range with Linear interpolation (set tangents to Linear, not Auto) so speed is constant.
- Length: 10 s at 24 fps = 240 frames loops cleanly; render 241 frames and drop the last or set range to 0..239.
- Camera: static CineCamera 50 mm, f/4, 3/4 view, slightly above eye level. For full-body creatures use 35 mm further back.
- Lighting: three-point rig below + faint SkyLight with an HDRI (`HDR_` asset, from a free source such as Poly Haven after license check; ask Zac before downloading anything).
- Capture: Movie Render Queue per section 7. Also render a flat gray-material pass for clay look (Show > Visualize > or a M_Clay override) when asked.

### Three-point rig (Rect Lights)
| Light | Position (relative to subject, facing it) | Intensity | Notes |
|---|---|---|---|
| Key | 45 degrees to camera side, 30 to 45 degrees up | 10 cd | Source Width 100, Height 100 cm, soft shadows (Source Width larger = softer) |
| Fill | opposite side, 20 degrees up | 3 to 4 cd (about 1:3 ratio to key) | Cool tint (6500 to 7500 K) |
| Rim/Back | behind and above, opposite the key | 8 to 12 cd | Warm or strong cool for separation; watch fireflies on glossy surfaces |
Optional 4th: bounce/kicker low at floor level with 1 to 2 cd.
Set Lights to Movable, Cast Shadows on, Use Inverse Squared Falloff on, Temperature on, Virtual Shadow Maps handle the rest.

Hair/fur and eyes: Epic's hair needs Groom plugin enabled; eyes need a refractive eye material; both are heavy on 8 GB, UNVERIFIED budget. Test at 1080p first.

---

## 10. Performance profiling

Console commands in the editor (`~` or Cmd field), all long-standing (DOC-5.x):
- `stat fps`, `stat unit` (Frame, Game, Draw, GPU ms). Targets: Frame under 16.6 ms (60 fps) interactive, under 33 ms acceptable for look-dev.
- `stat gpu` shows per-pass GPU ms. Look for: Lumen scene/gather, Shadow depths (VSM), BasePass, Translucency, PostProcessing.
- `stat scenerendering`, `stat streaming`, `stat nanite` (UNVERIFIED availability in 5.8).
- `ProfileGPU` (or Ctrl+Shift+, in the editor) captures one frame.
- `r.ScreenPercentage 67` to test whether GPU or CPU bound.
- Visualizations: Viewport > Lit > Optimization Viewmodes (Shader Complexity, Light Complexity, Quad Overdraw) and Show > Visualize > Nanite (clusters, triangles, overdraw).
- Unreal Insights (`Engine\Binaries\Win64\UnrealInsights.exe`): trace with `-trace=cpu,gpu,frame` for deep dives; read-only on the install.

Reading the numbers: if GPU ms exceeds Game and Draw, the scene is GPU bound; check Lumen and VSM first, then translucency. If Draw is high, reduce unique materials and non-Nanite draw calls.

Typical wins on 8 GB: lower GI quality one step, cap Max Trace Distance, replace translucent glass with masked, cut 4K textures to 2K, reduce VSM shadow-casting local lights, turn off volumetric fog during blocking.

---

## 11. Packaging notes (only if a runtime build is asked for)

- Rendering stills/video does not need packaging; render from the editor or command line.
- Package a Windows build: Platforms > Windows > Package Project (`Saved\StagedBuilds`). Disk 5 to 30 GB. First cook is slow; the DDC at `D:\UE_DDC` speeds repeats.
- Settings: Build Configuration Shipping, Full Rebuild off, Use Zen Store default; Project Settings > Packaging > Include Prerequisites on.
- Do not package or ship without Zac's go; list asset licenses first (Fab/Quixel content has per-seat terms, check before public builds).

---

## 12. Quality checklist for a finished shot

Scene:
- [ ] Scale sanity: door about 200 cm, human about 175 cm, ground at Z=0.
- [ ] All meshes use `MI_` instances; no default grid material; no missing-texture checker.
- [ ] Nanite on/off decided per asset; no translucent Nanite.
- [ ] No black or orphan shadow areas; no light leaks; no flicker over the shot range.
- [ ] Lighting reads: key/fill/rim or sun/sky direction clear; shadows sensible; one dominant light.
- [ ] Exposure manual; no auto-exposure pumping in the sequence.

Camera:
- [ ] Focal length, aperture and focus distance set and noted.
- [ ] Subject sharp at the focus plane; background DOF intentional.
- [ ] Safe frames respected; horizon level; no clipping through geometry.

Render:
- [ ] MRQ preset saved (`MPC_...`) with resolution, AA counts, warm up, console variables.
- [ ] Test render of frame 0, middle, last at final settings; no ghosting, no TSR smear, no NaN black pixels.
- [ ] Output format and path correct; file count equals frame count.
- [ ] Loudness/audio not part of the render unless asked.

Log in `D:\WKP\scratch\` or the delivery doc: engine 5.8.4, scene name, light list with values, post process values, camera data, MRQ settings, render time per frame, peak VRAM, stat gpu top 3 passes, UNVERIFIED items hit.
