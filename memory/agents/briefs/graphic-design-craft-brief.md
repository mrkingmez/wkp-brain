# Craft Brief: graphic-design (image and video prompting, thumbnails, listing and social art)

Written 2026-11-22 by graphic-design. Tool versions at retrieval: Veo 3.1 family, Kling 4.0 and 3.0, Runway Gen-4.5, Luma Ray3.14, Seedance 2.5, Flux 3 Video, Adobe Firefly (Image model and Video model as of the Adobe Learn pages, undated). Re-retrieve by 2027-02-20 or when a tool ships a new version. Status: COMPLETE (more than 5 retrieved primary sources, 3 community lines marked). Full source list with every quote and its retrieval method is `D:\WKP\data\firefly-prompt-guide\SOURCES-2026-11-22.md` (ids G1 to G5, A1 to A5, K1 to K3, R1 to R3, L1 to L3, B1, F1 to F4). This brief adds the non-video sources, ids Y1, E1, C1, and the image-side reading. "Fetcher" means a small model read the page and returned an extraction, I did not see the raw page.

## 1. What world-class looks like here
1. A pro writes the picture in the maker's own template and order, in positive observable words (G2, A1, R1, B1).
2. A pro never names what to avoid in the main prompt, because the models draw it (G1, R2, K1, L1, B1, C1).
3. A pro lets the start frame carry geometry and identity and writes motion only (R2, F3, K1).
4. A pro keeps one body, one object, one action per clip and cuts instead of stacking beats (F4, B1).
5. A pro gives contact and landing shots a first and a last frame (G2, F3, L1, K1).
6. A pro never asks a model for text, a logo or numerals and composites them (B1 text FAQ; PROVEN in our F3).
7. A pro builds to the platform spec before generating: aspect, size, safe zones, crop (Y1, E1).
8. A pro drafts cheap, records every setting and changes one thing per retry (A1, L1, R2).

## 2. Sources, retrieved quotes (new today are marked NEW; older ones are the 2026-11-22 set and their quotes sit in SOURCES)
- G1 Vertex AI Veo prompt guide, retrieved 2026-11-22 (fetcher): "Describe what you don't want to see." and "We recommend that you use separate sentences in your prompt to describe the audio."
- G2 Google Cloud blog, Ultimate prompting guide for Veo 3.1, Oct 15 2025, retrieved 2026-11-22: "[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]"; "In your prompt, describe the transition and the audio you want."
- G3, G4 Vertex AI Veo 3.1 model page and first/last frame page, retrieved 2026-11-22: "Video lengths: 4, 6, or 8 seconds; reference image to video only supports 8 seconds."; "You provide up to three images of a single person, character, or product."
- A1 Adobe Learn, Create AI video with text prompts, retrieved 2026-11-22: "Shot type description + character + action + location + aesthetic."; "At this time, you can only select one option for camera motion, but you can always call out another in the prompt."
- A2 Adobe Learn, Generate images from text, retrieved 2026-11-22 and again 2026-11-22 (second pass, NEW details): "write clear and descriptive prompts that describe what you want to see"; "No need for command words like create, make, or imagine."; "longer prompts aren't always better"; Composition Reference "controls how subjects are arranged in the frame", Style Reference "controls the look and feel"; effects dropdowns are Color and tone, Lighting, Camera angle; Content type Photo is for a photorealistic image.
- A3 Adobe AI prompt guide page: labels Subject, Background, Image type, Style, Colour, Lighting, Action. "Be specific."
- K1 Kling 4.0 user guide (partial): "Only two types of negative instructions are truly necessary: no subtitles and no background music."
- R1, R2 Runway help and Academy (R1 raw): "Describe what you want to see rather than what you don't want."; "Effective image to video text prompts focus almost exclusively on motion."; "Starting simple lets you add one element at a time and see what each change does."
- L1 Luma Ray3.14 field guide (maker text for Ray lines): "Negative prompting is counterproductive."; "With keyframes: describe only what CHANGES, don't redescribe static elements".
- B1 BytePlus Seedance 2.5 guide, last updated Nov 19 2026 (raw): "Use positive descriptions whenever possible."; "If too much content is packed into a given time range, the result may contain excessive cuts or omit parts of the plot."
- F3, F4 Black Forest Labs: "your image sets the opening frame and the prompt drives the motion."; "Keep each beat achievable [em dash in the source text] two or three for a 5-second clip."
- Y1 NEW, YouTube Help, custom thumbnails (support.google.com/youtube/answer/72431), retrieved 2026-11-22 (fetcher): "try to upload a thumbnail with an aspect ratio of 16:9"; "2 MB for video thumbnails or 10 MB for podcasts" (mobile); "a minimum width of 640 pixels for videos"; formats "such as JPG or PNG"; Community Guidelines apply to every thumbnail.
- E1 NEW, Etsy Help Center, How to Take Great Listing Photos (help.etsy.com article 115015663347), retrieved 2026-11-22 (fetcher): "We recommend your listing photos have a width and height of at least 2000 pixels or more."; "The first photo in a listing should be horizontal (landscape) or square."; "Make sure the most important part of the item is focused in the center."; "Position your image so your subject is clear in all 3 views used across Etsy."
- C1 NEW, COMMUNITY, Adobe Community thread "Negative prompting" (community.adobe.com/ideas/p-negative-prompting-1480264), retrieved 2026-11-22 (fetcher): Sep 18, 2025 reply, "Right now, the model doesn't understand negative prompts, so adding it to a prompt will add it to your image."; Mar 1, 2025: "The model does not understand the concept of a word being negated by the word in front of it."; May 12, 2026: "You now can accomplish this with prompt to edit." The posters are Adobe Community members or experts, one badge says not an Adobe employee. COMMUNITY, counts toward the 2 community cap. The same Sep 18 reply goes on to suggest a parameter written "[avoid=xxx]"; whether it works is UNTESTED and is a one-try test for Zac. A web search the same day also returned a July 2026 community reply saying Firefly text-to-image and video do not support negative prompting, search snippet only, SNIPPET.

NOT RETRIEVED today, do not summarize from memory: Adobe helpx pages on Firefly video frames, camera and partner models (HTTP 403, A4); Adobe Firefly Prompt Guide 2026 PDF (over size, A5); Adobe learn pages "generate images with reference images" and "style reference" (HTTP 404, tried today); Adobe aspect ratio and Firefly Image model naming; Meta (Facebook, Instagram) image-size help page (fetch returned no body text); Runway image-to-video guide (R3); Luma help (L3); Kling, Runway and Luma model-specific pages on the Firefly partner menu.

## 3. What this changes in our work
- No negatives in a main prompt, for any model, image or video (G1, R2, K1, L1, B1, C1). The old Ian chain doc and the AKT image prompts (scratch\akt\akt-prompts.md) put "no text, no letters, no logos, no clouds, no birds" in the MAIN prompt, and the chain doc depends on a negative box that no Adobe page documents. Image prompts carry no negatives. A box or the "[avoid=xxx]" parameter (C1, UNTESTED) is a one-try test for Zac, never a dependency (C1, A2).
- The image order is subject, background, then style, colour, lighting (A3, A2). Short is better (A2). Cap new image prompts at 100 words.
- Text, logos, numerals: composited, never generated (B1 FAQ plus our F3).
- Specs go on the card with the source: YouTube 16:9, under 2 MB on mobile (Y1); Etsy landscape or square, 2000 px, subject centered with room to crop (E1). Firefly output size is NOT VERIFIED and Zac checks the download.
- Contact and handoff shots: two clips and a cut, or first and last frames (F3, G2).
- Edit-in-place beats re-roll for a still that is nearly right: Adobe's own staff pointer is prompt to edit (C1, May 12 2026, COMMUNITY).

## 4. Tag status of every old tip (checked against the retrieved sources)
SOURCED: no negatives, positive observable words, template order, motion-only with a start frame, 2 to 3 beats, first and last frame, 720p drafts (L1, COMMUNITY for the cost claim). PROVEN in our logs: F1 negation drew the thing (5 clips), F3 logo drawn wrong (2 of 2), F8 to F10 handoff failed (6 of 6), F5 and F11 geometry only holds in a start frame. PROPOSED, untested: "Composition reference at 50 percent" (A2 says a strength slider exists, no midpoint is given), "Style reference carries grade and grain", "same seed across tiers", Firefly End slot exposure, Seedance and Flux tier choices, "Veo 3.1 Fast cheaper" (Luma's opinion).

## 5. Open questions the sources did not answer
- Which Firefly Image model name Zac's account offers and its output pixel size (panel only).
- Whether the "[avoid=xxx]" parameter (C1, Sep 18 2025) works on the current Image model, and whether Generate image has a Negative or Exclude box now (A2 silent, C1 says the model does not understand negatives).
- End-frame slot per partner model, seed field, credit cost (panel and Zac only).
- Meta, Instagram, TikTok image size and safe zones (Meta page returned nothing).
- Any maker rule on left and right or on which hand (none exists, so geometry stays in the start frame).
- Whether Composition reference works on the current Image model (only COMMUNITY reports that it is ignored, C1 thread list, titles only).
