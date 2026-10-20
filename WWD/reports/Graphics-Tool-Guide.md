# WWD Graphics Tool Guide: Python, After Effects, or Firefly

**Written 2026-10-18.** For deciding how to make stickers, cards, transitions and other video graphics for Winter Wolf's Den reviews.

---

## 1. How the current kit was made (the free way)

Everything in `P:\WWD Kit\` was built on your own computer. No connectors, no subscriptions, no credits.

| Tool | What it does |
|---|---|
| Python 3.12 | Runs the scripts |
| Pillow | Draws text, shapes, textures and shading, one frame at a time |
| NumPy and SciPy | Math for grunge noise, rough brush edges and blood drip shapes |
| ffmpeg | Stitches frames into a video with a see-through background and mixes in sound |
| Claude Code | Writes and runs the scripts |

Source files: fonts already on your PC (plus the bundled Poppins), your own trophy picture and fanfare sound from the Award Show stuff folder, and your owned sound library on the P: drive.

Not used: Higgsfield, Firefly, Suno, ElevenLabs, Canva, Adobe, or any website.

| Kit piece | Finished clip | Script |
|---|---|---|
| Stamps (Recommend Watch, Save Yourself the Time, Dumpster Fire) | `P:\WWD Kit\Stickers\` | `make_stickers.py` |
| Wolfie Award Nominee | `P:\WWD Kit\Stickers\` | `make_stickers.py` |
| Next Up card | `P:\WWD Kit\Cards\` | `make_next_up.py` |
| Blood Pour transition | `P:\WWD Kit\Transitions\` | `make_blood_pour.py` |

Scripts live in `D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\`. To change one, tell Claude "rebuild the stickers" or say what to tweak (word, color, speed).

---

## 2. What each option can and cannot do

### Python scripts (free, current default)
- **Good at:** flat graphics with exact text, simple motion (slams, fades, wipes), anything reused every review, anything that needs to be fast and repeatable.
- **Weak at:** photoreal texture, organic motion, polished 3D-looking effects.
- **Cost:** nothing.
- **Who runs it:** Claude, fully.

### Adobe After Effects
- **Good at:** polished, layered motion. Clean text, glow, shatter, particles, camera moves, channel intro and outro, lower thirds. Easy to tweak by hand later.
- **Weak at:** takes more of your time unless a template already exists.
- **Cost:** your Adobe subscription.
- **Who runs it:** you. Claude cannot click through After Effects. Claude can write a script (`.jsx`) that builds the comp, and you run it with **File > Scripts > Run Script File**, then export.
- **Head start:** the P: drive already holds After Effects templates (`.mogrt` and AE projects) and blood and lava packs under Tools and AE Templets.

### Adobe Firefly (and stock footage)
- **Good at:** photoreal or organic looks. Blood, fire, smoke, creepy backgrounds, thumbnail art.
- **Weak at:** exact text (it misspells and drifts), transparent backgrounds, getting the same result twice.
- **Cost:** Firefly credits on your plan.
- **Who runs it:** you, by pasting prompts Claude writes. An Adobe connector exists in Claude Code but is not signed in. Signing in has to be done by you, because Claude cannot enter passwords.

---

## 3. When to use which

**Use Python when:**
1. It is a reusable kit piece used every review (stamps, stickers, end cards).
2. It is flat graphics with exact text.
3. It is a short drop-in clip, roughly 1 to 3 seconds.
4. It needs to be fast, offline and free, with the title swapped per movie.

**Use After Effects when:**
1. It has to look polished and is the face of the channel (intro, outro, animated logo, lower third).
2. It has several moving parts at once, or camera moves, glow, shatter or particles.
3. You will want to tweak timing and colors yourself.
4. A template on the P: drive already does most of the work.

**Use Firefly or stock footage when:**
1. It needs real-looking footage or art (blood, fire, smoke, backgrounds, thumbnails).
2. Drawing it with code would look fake. The current blood pour is the example.
3. It is a one-off with no exact text to get right.

### Quick size test

| Job | Best tool |
|---|---|
| Under 3 seconds, text and shapes | Python (free) |
| Reused every video | Python, built once |
| 5 to 15 seconds, several moving parts | After Effects |
| Needs photoreal or organic texture | Firefly or P: drive footage |
| Channel intro or outro seen by every viewer | After Effects (worth the time) |

---

## 4. Default rule going forward

Claude starts with Python or your P: drive packs. Claude only suggests After Effects or Firefly when the free version would look cheap, and says why before building anything.

---

## 5. Open choices for Zac

1. **Blood pour:** redo it with real blood footage from the P: drive packs, or try a Firefly clip? (Real footage is likely to beat the drawn version.)
2. **Stickers:** keep the Python versions, or have Claude write an After Effects script so you can tweak them by hand?
3. **Firefly from Claude Code:** do you want the Adobe connector signed in so Claude can drive it, or keep pasting prompts yourself?
