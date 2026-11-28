# Previs report: Ian trailer: garage wrench hand-off (R3b geometry, previs)

Built 2026-11-24. Gray layout only, fixes WHO STANDS WHERE, WHICH HAND, SCALE, CAMERA. It does not fix look.

Action: The older man (father) lets go of the wrench at the TOP with his RIGHT hand. The young man (Brandon) takes it at the SHAFT BELOW with his RIGHT hand. A clear gap of air between the hands. Wrench vertical, jaw at the bottom.

## Camera

- ratio 9:16, 720x1280 px, lens 40 mm on a 36 mm sensor, HFOV 28.4 deg, VFOV 48.5 deg
- camera at [0.0, -2.0, 1.25] (height 1.25 m), looking at [0.0, 0.0, 1.1]

## Characters (read from the scene)

- **Brandon**: 1.80 m, stand, facing 90 deg, 2.05 m from camera, seen from the side/three-quarter, body is 98% of frame height, head in frame True, feet in frame False
  - L hand (BLUE): on screen-left, 53% visible (hidden by PV_Brandon_torso, PV_Brandon_pelvis), holds nothing
  - R hand (RED): on screen-left, 68% visible (hidden by PV_Brandon_farmR, PV_prop_wrench), holds wrench:shaft
- **Father**: 1.74 m, stand, facing 270 deg, 2.05 m from camera, seen from the side/three-quarter, body is 94% of frame height, head in frame True, feet in frame False
  - L hand (BLUE): on screen-right, 100% visible, holds nothing
  - R hand (RED): on screen-right, 100% visible, holds wrench:top

Closest hand to hand distances (m): Brandon.R / Father.R = 0.174; Brandon.R / Father.L = 0.446; Brandon.L / Father.R = 0.494; Brandon.L / Father.L = 0.689

## Card expectations

- PASS: older hand at the TOP, from the right (visible 100% (need 60); on screen-right (need screen-right); holds wrench:top (need wrench:top))
- PASS: young hand at the shaft, from the left (visible 68% (need 60); on screen-left (need screen-left); holds wrench:shaft (need wrench:shaft))
- FAIL: R3b is hands only, the card's negative field says 'face': no head in frame (head in frame True (need False))
- FAIL: R3b is hands only: no head in frame (head in frame True (need False))

## Warnings from the scene

- none
