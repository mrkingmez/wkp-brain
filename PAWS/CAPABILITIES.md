# Scout - Capabilities

## Fetch

**V1 - ships with the first build.**
Location search by filename, folder, and file date across a fixed set
of scoped locations. Not a full-drive search - scoped deliberately so
Scout never digs somewhere it wasn't meant to, and so results come
back fast.

Proposed default scope, NOT YET CONFIRMED:
D:\WKP, Documents, Downloads, Desktop, L:
Confirm or correct this list before building the index.

Trigger: "Scout, fetch the VA tracker" or equivalent, spoken or typed
in the companion app. Scout searches the scoped locations and either
surfaces the result on the companion app or opens it directly on the
PC.

**V2 - later upgrade, not required for v1.**
Content-aware search. Photo metadata (capture date, location if
present) for "find the picture from the PCS move" style requests
where the filename means nothing. Eventually genuine visual content
matching - understanding what's IN an image, not just what it's named
or when it was taken. Real engineering, sequenced after v1 proves the
concept works at all.

## Data management - new direction, not yet fully specced

Introduced 9 SEP 2026: physical media ports - SD card mentioned
specifically - so Scout can scan inserted storage, identify what's on
it, and sort files to where they belong. If it doesn't know where
something goes, it asks rather than guessing.

This is a real direction, not a locked spec. Before building it,
resolve:
- Which port - SD, USB-A, both.
- Read-only scan-and-suggest, or read-write move-and-file.
- Confirmation rule - the safe default is Scout NEVER moves or
  deletes a file without asking first, every time, no "trust me"
  mode. State this explicitly before writing a line of code for it.

## Connectivity

**PC** - solved already. Reads D:\WKP\dashboard\data\ directly. No
new work.

**Phone (Android)** - v1 feature. Companion app over WiFi or
Bluetooth. Two-way: receives Scout's status, and Scout can push
notifications back out. This is what makes Scout more than a
dashboard - it reaches the owner instead of waiting to be checked.

**Watch** - deferred deliberately. Its own project, not a v1 feature.
Ecosystem not yet chosen - Android is confirmed for phone, which
points toward Wear OS as the likely path, but this is not decided.
Pick one platform once Scout has proven itself worth wearing.
