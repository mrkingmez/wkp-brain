# Vision Quest EP 8 finale end card (2026-11-15)

Built by wwd-vfx. $0, code only, owned sounds only. Nothing posted.

**Concept.** The hosts do not name a next review and there is no season 2, so no "Next Up: title" card. The VQ-OS review monitor from the Next Up cards runs a SESSION END screen: SERIES VISION QUEST, STATUS FINALE COMPLETE, THANKS FOR WATCHING, two end-screen tile boxes, a subscribe ring, then "NEXT: FROSTCAST, LIVE WEDNESDAYS 9 PM ET" and "SEE YOU IN THE NEXT ONE, WHATEVER IT MAY BE" (the hosts' own close). The monitor powers down in the last second (CRT collapse, LED goes red).

**Recipe**
- Script: `D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\make_vq8_end_card.py` (uses `make_arcade_kit.py` render helper; look follows `make_vq8_next_up.py`).
- Command: `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe make_vq8_end_card.py` (about 2 to 3 minutes).
- Fonts: Consolas Bold, Impact (Windows system fonts). No studio art.
- Sounds (all owned, `P:\Sounds\Sound FX\Adobe\`): Digital Computer Beeps Static 01, Arcade Game Buttons Single 01 (typing ticks), Digital Glitch 01, Electrical Power Down 01. No music.
- Outputs in `P:\WWD Kit\Cards\`: `End Card - Vision Quest Finale.mov` (ProRes 422 HQ, opaque like the other Next Up cards), `End Card - Vision Quest Finale (MP4).mp4`, `End Card - Vision Quest Finale.png` (settled frame).

**Spec.** 12.0 s, 1920x1080, 30 fps, stereo 48 kHz.

**Edit placement.** Left tile 190..830 x 420..780, right tile 1090..1730 x 420..780, subscribe ring centre (960, 600), radius 90 (canvas px). Tile labels: LATEST UPLOAD, BEST FOR YOU (standard YouTube element types). No Vision Quest playlist exists (video-inventory.md), so no playlist tile. Boxes are drawn from 1.0 s; start the YouTube elements at about 3 s into the card and run them to about 0.5 s before the end. The power-down starts at 10.6 s.

**YouTube rules.** End screen length 5 to 20 s, up to 4 elements, video at least 25 s. From several web guides only, no official Help page retrieved. Check YouTube Studio on upload.

**Not verified.** Audio was not listened to. Real YouTube element placement was not tested in Studio.
