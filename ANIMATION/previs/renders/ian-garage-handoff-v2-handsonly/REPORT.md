# Previs report: Ian trailer: garage wrench hand-off, hands-only close (R3b framing)

Built 2026-11-24. Gray layout only, fixes WHO STANDS WHERE, WHICH HAND, SCALE, CAMERA. It does not fix look.

Action: The older man (father) lets go of the wrench at the TOP with his RIGHT hand. The young man (Brandon) takes it at the SHAFT BELOW with his RIGHT hand. A clear gap of air between the hands. Wrench vertical, jaw at the bottom.

## Camera

- ratio 9:16, 720x1280 px, lens 35 mm on a 36 mm sensor, HFOV 32.3 deg, VFOV 54.4 deg
- camera at [0.0, -0.7, 1.15] (height 1.15 m), looking at [0.0, 0.0, 0.98]

## Characters (read from the scene)

- **Brandon**: 1.80 m, stand, facing 90 deg, 0.80 m from camera, seen from the side/three-quarter, body is 242% of frame height, head in frame False, feet in frame False
  - L hand (BLUE): on screen-left, 0% visible, holds nothing, REACH SHORT by 0.02 m
  - R hand (RED): on screen-left, 74% visible (hidden by PV_Brandon_farmR), holds wrench:shaft
- **Father**: 1.74 m, stand, facing 270 deg, 0.81 m from camera, seen from the side/three-quarter, body is 228% of frame height, head in frame False, feet in frame False
  - L hand (BLUE): on screen-right, 0% visible, holds nothing
  - R hand (RED): on screen-right, 100% visible, holds wrench:top

Closest hand to hand distances (m): Brandon.R / Father.R = 0.174; Brandon.R / Father.L = 0.446; Brandon.L / Father.R = 0.781; Brandon.L / Father.L = 0.968

## Card expectations

- PASS: older hand at the TOP, from the right (visible 100% (need 60); on screen-right (need screen-right); holds wrench:top (need wrench:top))
- PASS: young hand at the shaft, from the left (visible 74% (need 60); on screen-left (need screen-left); holds wrench:shaft (need wrench:shaft))
- PASS: R3b is hands only, the card's negative field says 'face': no head in frame (head in frame False (need False))
- PASS: R3b is hands only: no head in frame (head in frame False (need False))
- PASS: R3b shows TWO hands only: Brandon's free LEFT hand must not be in frame (visible 0% (allowed up to 10))
- PASS: R3b shows TWO hands only: the father's free LEFT hand must not be in frame (visible 0% (allowed up to 10))

## Warnings from the scene

- Brandon L arm falls short of its target by 0.02 m (previs shows a straight arm)
- Brandon head is outside the frame
- Father head is outside the frame
