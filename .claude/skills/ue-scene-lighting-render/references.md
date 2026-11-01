# References: ue-scene-lighting-render

Researched 2026-10-31 for Unreal Engine 5.8.4 on RTX 5060 8 GB.

## Epic official documentation
- https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes (Lumen Lite beta, Accumulation DOF, Movie Render Graph production ready, MRQ audio)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine (Lumen setup, software vs hardware, post process settings, emissive, 100,000 instance note)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine (Nanite limits, VSM interaction)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-queue-in-unreal-engine (page body did not load through the fetch tool; MRQ values here are community and prior-version knowledge, labeled)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-using-command-line-arguments-in-unreal-engine (body did not load; flags confirmed from engine source instead)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects (M_, MI_, LS_, HDR_ prefixes)

## Read directly from the installed engine (VERIFIED-5.8)
- D:\Epic\UE_5.8\Templates\TP_BlankBP\Config\DefaultEngine.ini (VSM on, static lighting off, DX12, SM6)
- D:\Epic\UE_5.8\Templates (template list incl. TP_PhotoStudioBP, TP_ME_CineBP)
- D:\Epic\UE_5.8\Engine\Config\BaseScalability.ini (GlobalIlluminationQuality @0..@3, Lumen Lite style medium GI settings)
- D:\Epic\UE_5.8\Engine\Plugins\MovieScene\MovieRenderPipeline\Source (command line flags: -LevelSequence=, -MoviePipelineConfig=, -MoviePipelineLocalExecutorClass=, -MoviePipelineClass=, -MovieSceneCaptureType=, -MovieSceneCaptureManifest=, -ExecutorPythonClass=)

## Secondary
- https://www.seeles.ai/resources/blogs/unreal-engine-5-8-ai-game-development-workflow (coverage of 5.8 features, news-level only)

## Not verified
- MRQ spatial/temporal sample counts and the cvar tuning values: community practice, test per scene.
- Exposure EV100 numbers, light intensity numbers: practical starting points, not from a single Epic page.
- Default tone mapper in 5.8, Substrate default, stat nanite availability: UNVERIFIED.
