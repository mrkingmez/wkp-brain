# Previs report: Ian trailer R3 v4: BOY hands wrench to OLDER MAN lying on a creeper under a low car; floor-level side-on camera

Built 2026-11-25. Gray layout only, fixes WHO STANDS WHERE, WHICH HAND, SCALE, CAMERA. It does not fix look.

Action: The older man lies on his back on a creeper under a low car. Only his open left hand and forearm reach out from beneath the rocker panel, palm up, from camera left. The boy sits on the floor at camera right and his one hand holds the wrench by the handle, jaw first toward the palm. A clear gap of floor-level air between jaw and palm. The car sits on the ground, nobody stands.

## Camera

- ratio 16:9, 1280x720 px, lens 85 mm on a 36 mm sensor, HFOV 23.9 deg, VFOV 13.6 deg
- camera at [0.18, -0.1, 0.12] (height 0.12 m), looking at [0.18, 2.5, 0.14]

## Characters (read from the scene)

- **Older**: 1.74 m, lie, facing 0 deg, 2.32 m from camera, seen from the back, body is 263% of frame height, head in frame False, feet in frame False
  - L hand (BLUE): on screen-left, 100% visible, holds nothing
  - R hand (RED): on screen-left, 0% visible, holds nothing
- **Boy**: 1.30 m, sit, facing 270 deg, 2.84 m from camera, seen from the side/three-quarter, body is 196% of frame height, head in frame False, feet in frame False
  - L hand (BLUE): on screen-right, 84% visible (hidden by PV_prop_wrench), holds wrench:handle
  - R hand (RED): on screen-right, 0% visible, holds nothing, REACH SHORT by 0.03 m

Closest hand to hand distances (m): Older.L / Boy.L = 0.425; Older.L / Boy.R = 1.122; Older.R / Boy.L = 1.635; Older.R / Boy.R = 2.352

## Card expectations

- PASS: older man's open palm enters from camera left (visible 100% (need 60); on screen-left (need screen-left))
- PASS: boy's hand carries the wrench from camera right (visible 84% (need 50); on screen-right (need screen-right); holds wrench:handle (need wrench:handle))
- PASS: only two hands: older man's free hand out of frame (visible 0% (allowed up to 10))
- PASS: only two hands: boy's free hand out of frame (visible 0% (allowed up to 10))
- PASS: man's face not in frame (head in frame False (need False))
- PASS: man's face not seen through the gap under the car (head visible 0% (allowed up to 0))
- PASS: boy's face not in frame (head in frame False (need False))

## Warnings from the scene

- Boy R arm falls short of its target by 0.03 m (previs shows a straight arm)
- Older head is outside the frame
- Boy head is outside the frame
