# References: ue-mcp-and-automation

Researched 2026-10-31. Nothing was installed, launched or enabled.

## Epic official documentation
- https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes (experimental MCP plugin entry, Python Optional properties, BatchProcessLibrary::RunBatch)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python (enable plugin, -ExecutePythonScript, -run=pythonscript, startup scripts, ExecCmd warning; does not cover remote execution)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-api-http-reference-for-unreal-engine (PUT remote/object/call, Beta caution; ports/flags not on this page)

## Read directly from the installed engine (VERIFIED-5.8)
- D:\Epic\UE_5.8\Engine\Plugins\Experimental\ModelContextProtocol\ModelContextProtocol.uplugin and Source\ModelContextProtocolEngine\Public\ModelContextProtocolSettings.h (path /mcp, port 8000, auto-start false, tool search true)
- D:\Epic\UE_5.8\Engine\Plugins\Experimental\ModelContextProtocol\Source\ModelContextProtocol\Private\ModelContextProtocolServer.cpp (Origin validation, no auth found)
- D:\Epic\UE_5.8\Engine\Plugins\Experimental\ToolsetRegistry\ToolsetRegistry.uplugin, Experimental\Toolsets\ (toolset list), Experimental\AIAssistant\AIAssistant.uplugin, Experimental\Toolsets\MCPClientToolset\MCPClientToolset.uplugin
- D:\Epic\UE_5.8\Engine\Plugins\Experimental\PythonScriptPlugin\ (PythonScriptPlugin.uplugin default off; PythonScriptPluginSettings.h/.cpp remote execution settings; Content\Python\remote_execution.py endpoints; PythonScriptPlugin.cpp -ExecutePythonScript=)
- D:\Epic\UE_5.8\Engine\Plugins\VirtualProduction\RemoteControl\Source\RemoteControlCommon\Public\RemoteControlSettings.h (ports 30010/30020, bind 0.0.0.0) and WebRemoteControl source (-RCWebControlEnable, -RCWebInterfaceEnable)

## Community and secondary (not installed, not endorsed)
- https://github.com/runreal/unreal-mcp (MIT, last push 2025-06-06, Python Remote Execution based; README security warning)
- https://github.com/chongdashu/unreal-mcp (no license detected, last push 2025-04-22)
- https://github.com/kvick-games/UnrealMCP (no license detected, last push 2025-06-22)
- https://github.com/flopperam/unreal-engine-mcp (no license detected, last push 2026-06-26, now vendor-owned)
- https://github.com/radial-hks/MCP-Unreal-Server (no license detected on GitHub, last push 2025-04-12)
- https://github.com/atomantic/UEMCP (MIT, last push 2026-10-21)
- GitHub repository API (api.github.com/repos/...) for license, push date, stars, queried 2026-10-31
- https://cryptobriefing.com/unreal-engine-5-8-mcp-server-support/ and https://ground.news/article/epic-games-just-took-a-big-step-toward-ai-built-games-with-unreal-engine-58_e80d79 (news coverage of the 5.8 MCP plugin and Claude Code demo, secondary)
- https://www.fab.com/listings/651ed47d-db10-4dfa-9a6c-b8080d0d6b8e (third-party "Unreal MCP Setup Assistant" listing; source of the 127.0.0.1:8000/mcp endpoint claim and required plugin list, unverified against Epic)

## Not found
- Epic documentation page for the 5.8 Unreal MCP plugin setup (search returned none).
- Epic page for Python Remote Execution settings.
- Whether the MCP HTTP listener binds loopback only: check with netstat after enabling.
