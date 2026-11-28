# Previs report: WWD cold open shot 1: Warden at his post, radio voice (TEST BLOCKING, not approved)

Built 2026-11-24. Gray layout only, fixes WHO STANDS WHERE, WHICH HAND, SCALE, CAMERA. It does not fix look.

Action: Shot 1 of Cold-Open-Shot-List.md: WARDEN at his post, radio voice reaching out. Blocking is a previs test written by animation, not Zac's approved design. The Warden's look is still a blocker, so this tests layout only: seated at a desk, LEFT hand holds a handheld mic near his mouth, RIGHT hand rests on the radio dial, he looks toward the lens.

## Camera

- ratio 16:9, 1280x720 px, lens 50 mm on a 36 mm sensor, HFOV 39.6 deg, VFOV 22.9 deg
- camera at [-0.478, -2.25, 1.3] (height 1.30 m), looking at [0.0, 0.0, 1.15]

## Characters (read from the scene)

- **Warden**: 1.78 m, sit, facing 180 deg, 2.41 m from camera, seen from the front, body is 187% of frame height, head in frame True, feet in frame False
  - L hand (BLUE): on screen-right, 95% visible (hidden by PV_prop_mic), holds mic:center
  - R hand (RED): on screen-left, 84% visible (hidden by PV_blk_radio, PV_prop_dial), holds dial:center

Closest hand to hand distances (m): 

## Card expectations

- PASS: face is in frame and turned to the lens (head in frame True (need True); facing dot 0.98 (need 0.60))
- PASS: LEFT hand holds the mic and we can see it (visible 95% (need 70); holds mic:center (need mic:center))
- PASS: RIGHT hand on the radio dial and we can see it (visible 84% (need 50); holds dial:center (need dial:center))
- PASS: mic hand reads on the right of frame (his left, seen from the front) (on screen-right (need screen-right))
- PASS: no hand drawn over the face (hand over face False (need False))

## Warnings from the scene

- none
