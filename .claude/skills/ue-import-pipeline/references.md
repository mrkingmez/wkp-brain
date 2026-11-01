# References: ue-import-pipeline

Researched 2026-10-31 for Unreal Engine 5.8.4 (install at D:\Epic\UE_5.8) and Blender 5.2.4.

## Epic official documentation
- https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes (5.8 notes: Interchange, uFBX, USD, MRQ, Python, Data Validation)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/interchange-framework-in-unreal-engine (Interchange overview only, short page)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine (UCX/UBX/USP/UCP, sockets, LODs, pivot, FBX 2020.2)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine (Convert Scene, Force Front XAxis, Convert Scene Unit, Transform Vertex to Absolute)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects (prefix table; no texture suffix or folder rules)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine (Nanite limits)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python (Python plugin, -ExecutePythonScript, -run=pythonscript)

## Read directly from the installed engine (VERIFIED-5.8)
- D:\Epic\UE_5.8\Engine\Build\Build.version (5.8.4)
- D:\Epic\UE_5.8\Engine\Plugins\Interchange\Runtime\Interchange.uplugin (EnabledByDefault true)
- D:\Epic\UE_5.8\Engine\Plugins\Interchange\Runtime\Config\DefaultInterchange.ini (glTF material parents, redirects)
- D:\Epic\UE_5.8\Engine\Plugins\Editor\DataValidation\DataValidation.uplugin (default on)
- D:\Epic\UE_5.8\Engine\Plugins\Animation\IKRig\IKRig.uplugin (default on)
- D:\Epic\UE_5.8\Engine\Plugins\Experimental\PythonScriptPlugin\ (default off; -ExecutePythonScript= parsed in PythonScriptPlugin.cpp)
- D:\Epic\UE_5.8\Templates\TP_BlankBP\Config\DefaultEngine.ini (r.AllowStaticLighting=False, DX12, SM6)

## Not fetched or unverified
- Blender 5.2.4 export dialog labels (Blender MCP was not connected during research). Property names come from the long-stable bpy.ops.export_scene.fbx API; confirm in the UI.
- Which importer is default for .fbx in a fresh 5.8 project: not stated in any page reached.
- Texture suffix and folder conventions: community practice, Epic's naming page does not define them.
