---
name: media-manager
description: Find any owned video, sound effect, music track, LUT, template, plugin or kit on Zac's drives. Use when anyone asks "where is the", "do we have a sound of", "find me a whiteboard whoosh", or needs an exact path. Searches the P: drive file index and the media map. Read-only, never moves or deletes.
---

# media-manager lookup

## Run it

```
C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\.claude\skills\media-manager\scripts\find_asset.py <keywords> [--max N] [--ext wav,mp3] [--map-only] [--index-only]
```

- Every keyword must appear in the path, any order, any case. `baseball bounce` finds `Sports Baseball Bounce 01.wav`.
- Two sources. (1) `D:\WKP\data\assets\p-drive-index.csv`, file level, P: drive only (about 27,200 files). (2) `D:\WKP\data\assets\media-map.md`, folder level, every drive.
- Each hit shows the exact path, extension, size, and whether it is still on disk now.
- Zero hits: try a shorter or synonym keyword (door, gate, garage), then `--map-only` for the folder, then walk the folder with Glob. If still nothing, say "not found on P:" and name which drives were not searched at file level (L:, D:, E:).

## Rules

- Read-only. Never move, copy, rename or delete a file unless Zac or a director asked for that exact action.
- Always give the exact path. Add the license note if the media map has one. "License unknown" is a real answer, say it.
- Do not report a file you did not see in a result. If the index and disk disagree, say so.
- Rebuild the index only on request (a read-only walk of P:, writes only the CSV).
- Adobe and its folders are off limits to change.
