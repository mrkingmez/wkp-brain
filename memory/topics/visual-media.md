# Visual Media / Framing Preferences

## Edge-to-edge over letterbox, except for vertical content [2026-08-24]
When fitting a still image into a fixed video frame (e.g. 1920x1080 B-roll),
Zac wants landscape/square source images cover-cropped to fill the frame
completely, edge to edge, no black bars — even though this trims some
content off the sides/top/bottom. Only portrait/vertical sources (movie
posters, key art, anything taller than wide) get pillarboxed with black
bars on the sides, because cropping those into a landscape frame would cut
off way too much.

**Why:** Went through two iterations on the Den Files EP1 B-Roll pass before
landing here. First pass cover-cropped everything and zoomed in too tight on
some images ("too zoomed in to make out what they are"). Second pass padded
everything with black bars to avoid any cropping — Zac called it "close
enough" but wanted less black space. Final rule: edge-to-edge is the
priority; only exempt vertical content where cropping would be destructive,
not just imperfect.

**How to apply:** Default to this rule for any future image-to-fixed-frame
resize task — Etsy listing prep, thumbnails, other WWD B-Roll — not just
[[wwd-broll-prep]]. If a specific landscape/square source is losing
something important to the crop (small/low-res source, tight composite),
flag it and ask rather than silently accepting or silently switching to
pillarbox. Full mechanics and the reference implementation live in the
wwd-broll-prep skill (`D:\WKP\.claude\skills\wwd-broll-prep\`).
