# WWD Director Memory

Index of operational learnings for the wwd-director role. Details live in
this same folder. Read this at session start when relevant.

- [Missing skills](missing_skills.md) — wwd-video-upload-package and wwd-shorts-clip-factory don't exist on this machine; hand-build from format spec, don't re-discover, see WWD-2026-08-31-01
- [Raw capture files](raw_capture_files.md) — Raw Footage .m4v/.aac pairs can be unmuxed/mid-export; wait for the real Premiere .mp4 export instead of fighting raw streams
- [Bash quoting](bash_quoting.md) — no trailing backslash before a closing quote in paths; write PowerShell scripts to .ps1 files, never inline -Command with $ variables
