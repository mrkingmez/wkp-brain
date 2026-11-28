# Lens cheat sheet (previs)

Sensor width 36 mm (full frame). Blender fits the sensor to the LONGER side of the frame (sensor_fit AUTO), so in 9:16 the 36 mm runs up and down. Numbers are computed by `gen_lens_sheet.py`, not typed.

Distance column: metres from the camera to a standing 1.75 m person so the whole body fits with a 10 percent margin, and to frame a head-and-shoulders (0.60 m tall) with 10 percent margin.

| Lens mm | Long-edge FOV deg | 16:9 vertical FOV deg | Full body 16:9 (m) | Full body 9:16 (m) | Head and shoulders 16:9 (m) | Head and shoulders 9:16 (m) | Use |
|---|---|---|---|---|---|---|---|
| 14 | 104.3 | 71.7 | 1.3 | 0.7 | 0.5 | 0.3 | ultra wide, interiors, distortion at edges |
| 18 | 90.0 | 58.7 | 1.7 | 1.0 | 0.6 | 0.3 | very wide, tight rooms, vehicles interior |
| 24 | 73.7 | 45.7 | 2.3 | 1.3 | 0.8 | 0.4 | wide establishing, handheld feel |
| 28 | 65.5 | 39.8 | 2.7 | 1.5 | 0.9 | 0.5 | wide, street level, group of people in a room |
| 35 | 54.4 | 32.3 | 3.3 | 1.9 | 1.1 | 0.6 | the everyday cinema lens, our default habit |
| 50 | 39.6 | 22.9 | 4.8 | 2.7 | 1.6 | 0.9 | natural, close to what the eye sees, medium shots |
| 85 | 23.9 | 13.6 | 8.1 | 4.5 | 2.8 | 1.6 | portrait, close-ups, flattens depth |
| 100 | 20.4 | 11.6 | 9.5 | 5.3 | 3.3 | 1.8 | tight close-up, inserts, hands |
| 135 | 15.2 | 8.6 | 12.8 | 7.2 | 4.4 | 2.5 | very tight, compressed depth, far inserts |

## Heights and angles

| Camera height (m) | Reads as |
|---|---|
| 0.3 to 0.6 | low angle, looks up at people, floor and legs, hero or threat |
| 1.2 to 1.4 | seated eye level or chest height, neutral for seated people |
| 1.5 to 1.7 | standing eye level, neutral |
| 2.5 to 4 | high angle, shows layout and who stands where, small or weak feel |
| 20 and up, straight down | plan view, use it for who stands where (the previs makes this automatically with --plan) |

## Reading the numbers

- A longer lens makes the same distance look tighter and flattens depth. A wider lens needs less distance and bends the edges.
- Previs lens numbers are GEOMETRY. An image or video engine reads 'a 35 mm lens' as a mood word and will not match the exact field of view. Use the previs to settle framing and who stands where, then write the framing in plain words (shot size, angle, which side) in the prompt.
- Keep one lens habit across a sequence (playbook B3). If the previs shot list mixes 24 and 85 mm without a reason, ask why.
