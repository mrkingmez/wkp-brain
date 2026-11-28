# W1 torn-photo rip (heartbreak beat 8, 25.0 to 28.0 s)
Renderer: rip.py (Python, Pillow, numpy, ffmpeg; free). 1920x1080, 24 fps, 3.0 s silent. Contain-fit with blurred fill (blurred copy of the same still, dimmed), never cropped.
Real clip: render_real.bat v2   (python rip.py --a W1a-together.png --b W1b-caught.png --out <Rough Cut>\...-v2-silent.mp4)
Props: --seed (tear shape), --tear-x (0 to 1, where the tear starts), --slope (lean), --jag (roughness), --hold 1.2, --rip 0.7, --total 3.0, --shake 14, --no-dust.
Tip: tear-x 0.5 runs through Brandon's face in W1a; try --tear-x 0.62 or a new --seed to split the couple instead.
Sound cue (for sound-designer, not heard): one real paper-tear at 1.2 s (about 0.3 s, fast start), small shake thump, low fire crackle continues underneath the whole 3 s, no voices.
Premiere fallback: W1a clip then W1b with a Barn Doors Wipe (Effects > Video Transitions > Wipe > Barn Doors), 0.6 s, centered on the cut.
9:16 later: render 1080x1920 plate, contain-fit blurred fill, vertical tear becomes a diagonal slope 0.25 with the halves falling left and right; needs W and H constants changed in rip.py.

## v2 center tear (2026-11-25, Zac: v1 "really bad, should look like ripping it down the middle")
Renderer: rip_center.py (imports helpers from rip.py; v1 rip.py unchanged). Run render_real.bat (auto-versions: next free vN, now v2-center, next run v3). Optional arg forces a number.
Timing: hold A 1.2 s, crack zips top to bottom 0.3 s, halves hinge on their OUTER edge (perspective swing to 15 degrees) and slide fully out left and right by 2.0 s, B flat to 3.0 s. Tear at tear-x 0.5, jag 14 px, no slope. Tear runs through the blurred bands. Shake only on the first crack (about 0.15 s). Dust 40 flecks + 5 bits.
Sound cue update (for sound-designer, not heard): zipper-like paper tear 0.4 s starting at the first crack (1.2 s), small thump on the crack, then two paper whooshes, left (about 1.45 s) then right, panned L and R, fading as the halves leave (done by 2.0 s). Fire crackle continues underneath.

## v3 paper rip (2026-11-25, Zac: "think of ripping paper down the middle")
Renderer: rip_paper_v3.py (Python, numpy, opencv-python-headless, ffmpeg; free; no Adobe). Chosen over Blender and three.js because it renders per frame in about 45 s, reuses the contain-fit and torn-edge helpers, and gives true mesh bending without a scene setup.
Run: python rip_paper_v3.py --a W1a-together.png --b W1b-caught.png --out <Rough Cut>\Ian-Trailer-W1-Rip-3s-16x9-v3-paper-silent.mp4 [--frames-dir DIR]. contact_sheet.py FRAMES OUT.png first last cols makes the contact sheet. Output is v3-paper, v1 and v2 untouched.
Beat: hold A 1.2 s, hands-grab tremor 0.2 s (tiny flutter and bend), crack travels top to bottom 0.57 s while the halves fan open into a V (hinge on outer edge, curl toward camera, perspective), 0.03 s tension, snap at 2.0 s (jerk), halves fly out with shutter blur and are gone by about 2.25 s, B settles to 3.0 s.
Sound cue (for sound-designer, not heard): paper tear starting at 1.4 s ramping with the crack (0.55 s), creak of tension 1.97 to 2.0 s, one small fiber snap at 2.0 s with a thump, two paper whooshes L then R, fire crackle underneath.
Tear is at x 0.5: Brandon's face is nearly split in the open V (right edge of his face), check with --tear-x.
