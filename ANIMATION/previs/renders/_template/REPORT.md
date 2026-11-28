# Previs report: Template shot, two people and a prop

Built 2026-11-24. Gray layout only, fixes WHO STANDS WHERE, WHICH HAND, SCALE, CAMERA. It does not fix look.

Action: One sentence. One body, one object, one action.

## Camera

- ratio 16:9, 1280x720 px, lens 35 mm on a 36 mm sensor, HFOV 54.4 deg, VFOV 32.3 deg
- camera at [0.0, -4.0, 1.5] (height 1.50 m), looking at [0.0, 0.0, 0.876]

## Characters (read from the scene)

- **A**: 1.75 m, stand, facing 90 deg, 4.07 m from camera, seen from the side/three-quarter, body is 74% of frame height, head in frame True, feet in frame True
  - L hand (BLUE): on screen-left, 47% visible (hidden by PV_A_torso, PV_A_pelvis), holds nothing
  - R hand (RED): on screen-left, 47% visible (hidden by PV_A_farmR, PV_prop_cup), holds cup:center
- **B**: 1.62 m, stand, facing 270 deg, 4.08 m from camera, seen from the side/three-quarter, body is 68% of frame height, head in frame True, feet in frame True
  - L hand (BLUE): on screen-right, 84% visible (hidden by PV_B_farmL), holds nothing
  - R hand (RED): on screen-right, 53% visible (hidden by PV_B_torso, PV_B_pelvis), holds nothing

Closest hand to hand distances (m): A.R / B.L = 0.538; A.R / B.R = 0.721; A.L / B.L = 0.828; A.L / B.R = 0.838

## Card expectations

- PASS: both full-length in frame (head in frame True (need True); feet in frame True (need True))
- PASS: A's RIGHT hand holds the cup and it is visible (visible 47% (need 40); holds cup:center (need cup:center))

## Warnings from the scene

- A R hand (RED) holds cup:center but only 47% of it is visible to this camera, hidden by PV_A_farmR, PV_prop_cup
