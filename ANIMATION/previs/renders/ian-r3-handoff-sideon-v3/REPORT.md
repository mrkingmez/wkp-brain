# Previs report: Ian trailer R3 v3: wrench hand-off, side-on, two forearms, one wrench horizontal, gap between

Built 2026-11-25. Gray layout only, fixes WHO STANDS WHERE, WHICH HAND, SCALE, CAMERA. It does not fix look.

Action: The older man's right hand, from camera left, holds one wrench roughly horizontal by the handle with the open jaw pointing at an open palm that reaches in from camera right. A clear gap of air between wrench jaw and palm.

## Camera

- ratio 16:9, 1280x720 px, lens 85 mm on a 36 mm sensor, HFOV 23.9 deg, VFOV 13.6 deg
- camera at [0.0, -1.5, 1.0] (height 1.00 m), looking at [0.0, 0.0, 1.0]

## Characters (read from the scene)

- **Older**: 1.74 m, stand, facing 90 deg, 1.69 m from camera, seen from the side/three-quarter, body is 454% of frame height, head in frame False, feet in frame False
  - L hand (BLUE): on screen-left, 5% visible, holds nothing
  - R hand (RED): on screen-left, 68% visible (hidden by PV_Older_farmR, PV_prop_wrench), holds wrench:handle
- **Boy**: 1.75 m, stand, facing 270 deg, 1.69 m from camera, seen from the side/three-quarter, body is 457% of frame height, head in frame False, feet in frame False
  - L hand (BLUE): on screen-right, 42% visible, holds nothing
  - R hand (RED): on screen-right, 0% visible, holds nothing

Closest hand to hand distances (m): Older.R / Boy.L = 0.412; Older.R / Boy.R = 0.63; Older.L / Boy.L = 0.897; Older.L / Boy.R = 0.93

## Card expectations

- PASS: older hand holds the wrench, enters from camera left (visible 68% (need 60); on screen-left (need screen-left); holds wrench:handle (need wrench:handle))
- FAIL: receiving open palm enters from camera right (visible 42% (need 60); on screen-right (need screen-right))
- PASS: only two hands: older man's free hand out of frame (visible 5% (allowed up to 10))
- PASS: only two hands: boy's free hand out of frame (visible 0% (allowed up to 10))
- PASS: no faces (head in frame False (need False))
- PASS: no faces (head in frame False (need False))

## Warnings from the scene

- Older head is outside the frame
- Boy head is outside the frame
