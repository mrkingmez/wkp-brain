---
name: feedback-chrome-pc-browser-only
description: "Claude-in-Chrome must run on the Windows PC browser (Browser 2), never the Mac browser until Zac says the Mac is set up"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 04ea53d6-d9a5-414d-99de-ffddd1104116
  modified: 2026-11-27T02:43:39.654Z
---

Zac 2026-11-26: Never use the Mac browser until he says it is set up and ready.

**Why:** Two Chrome extensions are connected to his account: a macOS one (not set up, signed out of Facebook) and his Windows PC (the one he actually uses and is logged into). The session defaulted to the Mac, so Facebook looked signed out for several turns and he got angry.

**How to apply:** Before any browser task, call list_connected_browsers and make sure the in-use browser is the Windows, isLocal one. If not, select_browser on the Windows one (it was deviceId 761e3ae3-fb06-4a4e-8291-b1af7b4bd80c on 2026-11-26, recheck). Never select the macOS browser. Related: [[feedback-lead-decide-autonomy]].
