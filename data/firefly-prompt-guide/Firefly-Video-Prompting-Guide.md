# Firefly Video Prompting Guide

> **2026-11-22: SUPERSEDED in part.** The working standard is now `STANDARD.md` (rules R1 to R17, per-engine templates, pre-flight checklist, settings.txt format) with sources in `SOURCES-2026-11-22.md` and the audit in `AUDIT-2026-11-22.md`. This file is kept for its engine notes and the Ian worked examples, but where it disagrees with STANDARD.md, STANDARD.md wins. Known stale lines here: the Ian "V" prompts in section 5 were never run and contain wording the lint rejects (for example "does not hit"); "Seedance" has since been read from ByteDance's own guide; the pre-flight list in section 6 is replaced by the 13-point list in STANDARD.md.

Built 2026-11-18 by graphic-design. Read-only research, nothing generated, no credits spent. Audience: Jarvis, graphic-design, wwd-vfx, any agent writing a Firefly or video-model prompt for Zac. Companion files: `QUICK-CARD.md` (one page, read it before every prompt) and `LESSONS.md` (what actually happened on Zac's clips, read it second).

## How to read the tags

Every tip ends in one tag. Trust them in this order.

- **[M:Sx]** MAKER-DOCUMENTED. It comes from the engine maker's own page (source id in the list below). I read the page myself unless the source line says "snippet only".
- **[C:Cx]** COMMUNITY. A blog, host site, forum or a third party describing the engine. Useful, not authoritative. Source id in the list below.
- **[U]** UNTESTED. My inference or standard editing practice. It has not been run on Zac's account. Treat as a try, and log the result in LESSONS.md.

Rule for the agent writing a prompt: a [U] tip is a hypothesis. When it works or fails on a real clip, add a row to LESSONS.md and the tip gets promoted or struck.

## Sources

Maker pages I read in full or in part:

- S1 Google Cloud, Veo prompt guide (Vertex AI): https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide
- S2 Google Cloud blog, "The ultimate prompting guide for Veo 3.1" (Oct 15 2025): https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- S3 Google AI Studio video docs (Gemini Omni Flash spec, Veo 3.1 Gemini API preview shutdown notice): https://aistudio.google.com/docs/video
- S4 Kling AI, prompt guide: https://kling.ai/blog/kling-ai-prompt-guide
- S5 Runway Academy prompt guide (Gen-4.5, text to video and image to video): https://academy.runwayml.com/prompt-guide
- S6 Luma, Video Models Field Guide (published Feb 27 2026): https://lumalabs.ai/learning-hub/luma-video-models-guide-ray3.14-veo-sora-kling-compared . This is Luma's own page. Its Ray3 and Ray3.14 sections count as maker-documented. Its sections about Veo, Sora and Kling are Luma's opinion of other companies' engines, so I tag those [C:S6].
- S7 Adobe Firefly help pages. Adobe's help site returned HTTP 403 to every direct fetch (WebFetch and curl). I did NOT read these pages. Everything tagged [M:S7] comes from search-engine summaries of the pages, "snippet only". Pages: https://helpx.adobe.com/firefly/work-with-audio-and-video/work-with-video/generate-videos-using-non-adobe-models.html and https://helpx.adobe.com/firefly/web/firefly-video-editor/generate-videos/generate-videos-with-pika-22.html
- S9 Luma help center, "How do I use Ray3 prompting effectively" (the fetch 404'd, quoted in a search summary, snippet only): https://lumaai-help.freshdesk.com/support/solutions/articles/151000223059-how-do-i-use-ray3-prompting-effectively-
- S8 Runway help center, Gen-4.5 section (snippet only, the page 403'd): https://help.runwayml.com/hc/en-us/sections/47297541368595-Gen-4-5

Community and third-party:

- C1 fal.ai, Kling 3.0 prompting guide (fal hosts Kling, it is not the maker): https://blog.fal.ai/kling-3-0-prompting-guide
- C2 Atlabs, Veo 3.1 prompting guide: https://www.atlabs.ai/blog/veo-3.1-prompting-guide-every-feature-explained-with-copy-paste-prompts
- C3 Runware, Gemini Omni Flash prompting guide (quotes Google's own guide, original not retrieved): https://runware.ai/docs/models/google-gemini-omni-flash-1-1/guides/prompting
- C4 invideo, "why do AI video models struggle with physical contact" (a vendor that resells these models, promotional): https://invideo.io/faq/why-do-ai-video-models-struggle-with-physical-contact/
- C5 Physion-Eval benchmark paper (search summary only, not opened): https://arxiv.org/pdf/2603.19607.pdf
- C6 Magic Hour, "How to fix faces and hands in AI video" (search summary only, not opened): https://magichour.ai/blog/how-to-fix-ai-video-faces-and-hands
- C7 Atlas Cloud, Kling 2.5 Turbo image-to-video API docs: https://www.atlascloud.ai/fr/models/kwaivgi/kling-v2.5-turbo-pro/image-to-video
- C8 Higgsfield and Veed guides on Kling Turbo start and end frames (search summary only): https://higgsfield.ai/blog/A-Guide-to-Kling-Turbo-Start-End-Frame
- C10 Atlas Cloud, Kling 4.0 physics-bugs checklist (search summary only): https://www.atlascloud.ai/blog/tips/kling-4.0-ai-video-physics-bugs-and-motion-deformation
- C11 DEV Community, Veo 3.1 developer guide (search summary only): https://dev.to/akaranjkar08/veo-31-developer-guide-timestamp-prompting-multi-shot-video-and-full-api-june-2026-3l5i
- C12 Scenario, Veo 3.1 essentials (search summary only): https://help.scenario.com/articles/1049410120-veo-3-1-the-essentials
- C9 Runware and Morphic guides for Gemini Omni Flash 1.1 and 1.2 (search summaries only): https://morphic.com/resources/how-to/gemini-omni-flash-1-2-guide

## What I could NOT retrieve

- Adobe's own pages (403). Firefly-specific facts below are snippet-level.
- Any Adobe credit table. See "Credit math".
- A Kling 3.0 maker guide with left/right, physics or negative-prompt rules (the kling.ai page has none).
- Any maker guidance on left versus right or which hand, from any engine. Zero. Everything on hands is [C] or [U].
- A maker guide for Veo 3.1 Fast, Veo 3.1 Lite, Kling 2.5 Turbo, Ray2, Runway's audio, or Firefly Video's own audio.
- Any maker statement on seeds. Google's prompt guide does not mention seeds. Runway and Kling pages did not either. Seed behavior is UNTESTED everywhere.
- Per-model clip durations as they appear in Firefly's panel. Read the panel.

## 1. The five rules that apply to every engine

1. **Say what you want to see, never what you do not.** Google says avoid "no" and "don't", list the unwanted thing as a noun, or describe the positive scene. [M:S1] Google's own example: "a desolate landscape with no buildings or roads" rather than "no man-made structures". [M:S2] Runway: "Describe what you want to see rather than what you don't want." [M:S5] Luma: Ray is a positive-only model, negative prompting is counterproductive. [M:S6]
2. **Name the exact picture, remove ambiguity.** Runway says the model "interprets your words more literally" and lacks a colleague's shared context. [M:S5] "A beautiful landscape" fails because it is ambiguous, "wrench in his right hand" does not. [M:S5, applied by me, U for the wrench]
3. **One action per clip.** Google: sequencing actions works, but subtle change works best in short clips. [M:S1] Atlas Cloud's advice: test one primary action and one contact chain per take. [C:C10] A benchmark paper reports that 83.3 percent of exocentric and 93.5 percent of egocentric generated videos had at least one visible contact, force, timing or causality violation, so contact is the weak spot for every engine, not just Zac's. [C:C5 search summary, figures not checked in the paper] A clip that holds hand-on-wrench AND ball-rolls-to-boot is two jobs. Make two clips. [U]
4. **Over-specifying hurts.** Runway: extremely complex multi-paragraph prompts "reduce the room for creative freedom", the model "struggles to honor every detail simultaneously". [M:S5] Luma: about 100 words, present tense, action-focused. [M:S6] Aim for 40 to 100 words, one block, no stacked adjectives.
5. **Change one thing per try.** Runway: start simple and add one element at a time to see what each change does. [M:S5]

## 2. Engine by engine

For every engine: what it is called in Firefly, the structure it answers to, then the eleven things Zac needs. "Panel" means read it in Firefly's settings panel, it is the truth for that day.

### 2.1 Firefly Video (Adobe first-party)

Structure. Adobe recommends covering visual style, shot size, camera angle and camera motion, says the model takes prompts literally so specificity helps, and says each generation starts from scratch with no memory of earlier instructions. [M:S7 snippet only]

- Camera panel controls: Shot size, Camera angle (aerial, eye level, high, low, top down) and Motion presets (zoom in, move left and right, tilt up and down, static, handheld). Only one motion preset can be picked, but another move can be named in the prompt. If nothing is picked or written, the camera has no prescribed move. [M:S7 snippet only]
- Keep the panel controls and the prompt text aligned, they can send mixed signals. [M:S7 snippet only]
- Frames: adding a first frame turns off Shot size and Camera angle. Adding an end frame turns off the Motion options. A first frame is needed before an end frame. [M:S7 snippet only]
- Left and right and which hand: no guidance found. "Move left and right" is a camera preset, not a subject instruction. Use a start frame. [U]
- Small object contact and rolling or bouncing: no guidance found. Use the end-frame method in section 4. [U]
- One action or several: not stated. One. [U]
- Duration, resolution, fps: read the panel.
- Negative language: not stated by Adobe in what I retrieved. Use positive phrasing like every other engine. [U]
- Audio: not retrieved. Treat as silent unless the panel shows an Audio switch on, and add sound in the edit. [U]
- Seed: Advanced > Seed is in Zac's panel (memory file, screenshot 2026-10-25). Behavior untested. [U]
- Text in video: do not rely on it, put text on in code or Premiere (house rule, memory `feedback-code-made-art.md`).

Commercially safe positioning: Adobe's own model, per Zac's menu note (memory `firefly-models.md`). Use it when the client or the license question matters. [U on how it behaves for physics]

### 2.2 Veo 3.1, Veo 3.1 Fast, Veo 3.1 Lite (Google)

Structure Google gives: **[Cinematography] + [Subject] + [Action] + [Context] + [Style and ambiance]**, then audio in its own sentences. [M:S2] Components: subject, action, scene or context, visual style. You do not need every element. [M:S1]

Copy-paste skeleton (mine, built on the formula): `Locked-off medium shot. A man in a black tee lies on a red creeper under a red Mustang. In his right hand, the hand nearest the camera, he holds a wrench and turns it slowly overhead. Garage, warm caged work lamp, concrete floor. Gritty film look, shallow depth of field. SFX: ratchet clicks. Ambient noise: low garage hum.` [U for how well it holds, M:S2 for the format]

- Left versus right, which hand: Google's guides say nothing. A community guide's own examples name the side and the action, for example "A hand enters from the left, picks it up slowly". [C:C2] A fixed start frame is the strongest control. [U]
- Small object contact, rolling, bouncing: no maker guidance. Community vendor reports that Veo often softens or blocks force on a person, so outputs show objects stopping short or resolving without contact, and advises rewording around inanimate objects. [C:C4] That matches "ball hits the toe instead of resting against the foot", though the match is my reading, not proven. [U]
- Camera moves: Google lists angles (eye-level, low, high, bird's-eye, worm's-eye, Dutch, close-up, over-the-shoulder, POV) and moves (static, pan, tilt, dolly, truck, pedestal, zoom, crane, aerial, handheld, whip pan, arc). A zoom changes focal length, a dolly moves the camera. [M:S1] Some advanced angles and lenses are "not officially supported" and results vary. [M:S1]
- One action versus several: Google supports sequencing and timestamp prompts like `[00:00-00:02] ... [00:02-00:04] ...` to direct several shots in one generation. [M:S2] Fewer segments is safer on an 8 second clip. [U]
- Start and end frames: First and Last Frame is a Veo 3.1 feature, upload both images and describe the transition and the audio in the prompt. [M:S2] In Firefly, Veo 3.1 Frames accepts a start frame, an end frame, or both. [M:S7 snippet only] A developer guide says the first frame is respected strongly and the last frame is a guide, not a hard constraint. [C:C11, secondhand] Whether Fast and Lite take an end frame in Firefly: NOT VERIFIED, check the panel.
- Reference images ("Ingredients to Video"): refer to each image by its role in the prompt, for example "Using the provided images for the detective, the woman, and the office setting...". [M:S2] Limit is up to three images per most sources. [C:S6] One guide says you choose first frame OR reference images in one request, not both. [C:C12] Not verified for Firefly.
- Duration: 4, 6 or 8 seconds. [M:S2] Panel decides.
- Negative language: no "no X" phrasing. [M:S1, M:S2] C2 adds that Veo "responds much better to descriptions that make the unwanted element naturally absent", for example describe a clean frame with no overlays instead of "no text on screen". [C:C2]
- Audio: say clearly you want audio and use separate sentences. Dialogue in quotes, `SFX:` for effects, `Ambient noise:` for the room. [M:S1, M:S2] Luma's field guide adds that Veo audio quality is inconsistent. [C:S6]
- Seeds and iteration: Google does not mention seeds. A third party suggests testing on Veo 3.1 Fast (about 70 percent cheaper and twice as fast by their numbers) and then re-running the same seed and prompt on Standard for the final. [C:S6] Whether the same seed gives the same shot across Fast and Standard is UNTESTED. [U]
- Text in video: Adobe's page (snippet) says for Veo 2 and 3 put the text in double quotes. Do not lean on it for 3.1, burn text in the edit. [M:S7 snippet only]
- Gemini API shutdown notice: Google says the Veo 3.1 Preview models in the Gemini API were shut down on October 22 2026 and point to Gemini Omni Flash. [M:S3] That is the Gemini API, not Firefly. Veo 3.1 is still on Zac's Firefly menu as of 2026-11-18 (memory `firefly-models.md`). Watch for it leaving the menu. [U]
- Veo 3.1 Lite: no maker page retrieved. Assume the same prompt rules, check results. [U]

### 2.3 Gemini Omni Flash

Facts from Google's own doc page: up to 15 seconds with native audio, text, image and video inputs, character consistency across up to 6 reference images, multi-turn conversational editing and extension via the Interactions API. [M:S3] Those editing and extension modes are on Google's API. Whether Firefly exposes them: NOT VERIFIED, read the panel.

- Structure: Runware quotes Google's guide as saying that with Gemini Omni you do not have to be as prescriptive as with other video models, and says it reads cinematic camera vocabulary directly. [C:C3] Describe the whole scene: subject, action, setting, lighting, camera. [C:C9] State the purpose up front (promo, social clip, story scene). [C:C9]
- Shot cuts: version 1.2 uses "Cut to" to mark new shots. [C:C3] Avoid it. Zac wants one-action takes. [U]
- Left versus right, contact physics, negative language, seeds: no guidance retrieved. An invideo test of 30+ Omni Flash outputs put complex physics prompts at about 50 percent, and suggests running several takes and keeping the one where the physics holds. [C:C4] That is a vendor claim. [C]
- Start and end frames: image inputs and references exist per Google. A literal start-frame or end-frame slot for Firefly: NOT VERIFIED.
- Audio: generates synchronized sound, so audio direction belongs in the prompt. [C:C3]

### 2.4 Kling 3.0, Kling 3.0 Omni, Kling 2.5 Turbo

Structure: kling.ai says strong prompts start with subject, action, setting, camera language, lighting, mood. "Strong cinematic prompts are built from clear scene direction rather than secret formulas." Prefer specific over vague ("swirling blue energy particles with an ethereal glow", not "magic"). [M:S4] A host guide orders it Scene, Characters, Action, Camera, Audio and Style. [C:C1]

- Start frame: Adobe's Firefly page says a first frame is mandatory to start a Kling generation. [M:S7 snippet only] Kling treats the input image as an anchor and preserves identity, layout and text from the source. Describe how the scene evolves from it, subtle movement, camera move, environmental change. [C:C1]
- Left versus right, which hand: not in the maker page, its only example is a "subtle pan right". [M:S4] Name the hand AND fix it in the start frame. [U]
- Small object contact and physics: no maker physics section. The page's rule: describe what viewers can see, "Visible motion language is safer and clearer than internal technical claims". [M:S4] Verbs the camera can see: "rolls slowly, slows, stops". [U]
- Camera moves: name framing, angle or move (close-up, wide, low angle, push-in, pan, tilt, tracking). A push-in is written "The camera slowly pushes toward the subject." Pacing words (slow, steady, quick) must tie to visible behavior. [M:S4] Specify camera behavior over time (tracking, freezing, panning). [C:C1]
- One versus several actions: Kling 3.0 has Multi-Shot, up to 6 shots in one output. Automatic Multi-Shot lets the model pick angles. Custom Multi-Shot sets each shot's content, duration, size and move, and the page says define the setting first, then order the shots (`[Shot 1: Wide shot]`). [M:S4] [C:C1 for the 6 shot limit] For a single clean action use a single shot. [U]
- End frame: Kling 2.5 Turbo supports a first and last image and interpolates between them, per API docs. [C:C7] Firefly passes a start frame to Kling (mandatory). Whether Firefly offers an end frame for Kling 3.0, Omni or 2.5 Turbo: NOT VERIFIED, check the panel.
- Duration: Kling 3.0 produces 3 to 15 seconds per one third-party guide, and "up to 15 seconds" per another host. [C:C1] Read the panel. Kling's page says to "specify shot duration within the supported generation length". [M:S4]
- Negative language: the kling.ai page does not discuss it, its samples end in positive style tags. [M:S4] Use positive phrasing. [U]
- Audio: Native Audio in Kling VIDEO 3.0 and 3.0 Omni, dialogue, ambience and effects in one pass, clear speaker labels, describe the location and acoustic detail plainly. [M:S4] Give each speaker a unique name and tie dialogue to a visible action. [C:C1]
- Seeds: not documented. [U]
- Text in video: Kling keeps text from a start image per one host. [C:C1] Still burn text in the edit.
- 3.0 Omni: described as multimodal video and audio with scene understanding in Zac's menu. kling.ai says use high-quality reference images or video elements when a character or prop must stay recognizable, and keep that description steady while the scene or camera changes. [M:S4]
- 2.5 Turbo: no maker guide found. Third parties stress a clean start frame (it sets pose, camera, light, composition) and the same light and ratio in both frames. [C:C8] Fast and cheap for drafting. [U]

### 2.5 Runway Gen-4.5

Structure Runway gives: text to video `[Camera] shot of [a subject/object] [action] in [environment]. [Supporting descriptions]`. Image to video `The camera [motion] as the subject [action]. [Additional descriptions]`. You do not need a rigid formula, structure matters less than clarity. [M:S5]

- Image to video: the image carries composition, subject, lighting and style, so the prompt should "focus almost exclusively on motion" and not re-describe what is in the image. Refer to characters and objects with general language ("the man", "the ball") to isolate them. [M:S5] Describe visuals only when introducing something not in the image, a dramatic change, a transformation or an interaction between two elements. [M:S5] A ball interacting with a boot is an interaction, so describe the interaction. [U]
- Hands: Runway warns that visual artifacts such as blurry hands or faces in the input image "may be intensified" once the image becomes video. Start frame must be clean. [M:S5]
- Implied motion trap: input images with motion blur, mid-action poses or directional lines carry implied motion, and prompting against it takes more iterations. Runway's example removes dust and blur from the image before it works. [M:S5] A still of a ball already mid-roll with blur will fight a prompt that says it rests. [U]
- Sequential prompting: natural language ("X, then Y, finally Z") or rough timestamps `[00:01] X occurs. [00:03] Y occurs.` Make sure the sequence fits the duration, use a higher duration for complex sequences. [M:S5]
- Unwanted cuts: raise the duration first, then add the continuity phrase "Continuous shot" (Runway's exact wording has one more adjective, our slop list bans it). [M:S5]
- Minimal camera motion: "The locked-off camera remains perfectly still." "Minimal subject motion only." Then stabilize in the editor. [M:S5]
- Camera moves: use plain camera sentences ("The camera slowly pushes in", "Whip pan to...", "Handheld camera:", "Natural camera shake."). [M:S5]
- Longer sequences: extract the last frame of a finished clip and use it as the image input for the next generation, then trim the shared frame in the edit. [M:S5]
- Negative language: positive phrasing, avoid conflicting instructions, avoid ambiguous or conceptual language. [M:S5]
- Start and end frames: Runway's help center lists Gen-4.5 as Text to Video and Image to Video only. [M:S8 snippet only] That suggests no end-frame slot for Gen-4.5. Not verified in Firefly, check the panel.
- Duration and resolution: not retrieved, read the panel.
- Audio: not retrieved. Assume no sound, add it in the edit. [U]
- Seeds and iteration: Runway frames iteration as a conversation, start simple, add one change. [M:S5] Seed not mentioned.
- Left versus right, small object physics: nothing in Runway's guide. [U]

### 2.6 Luma Ray (Ray3.14, Ray3.14 HDR, Ray3, Ray3 HDR, Ray2)

Luma's own field guide. Template: `Create a video of [SUBJECT] [MID-ACTION VERB] in [SETTING], [SECONDARY MOTION/CONSEQUENCE], [CAMERA MOVEMENT if any], [LIGHTING/MOOD].` [M:S6] About 100 words, action-focused, present tense. [M:S6]

- DO: mid-action verbs ("running", not "begins to run"). Include secondary consequences (dust kicked up, reflections, cloth movement). Be specific about camera ("camera dollies forward", "slow pan right"). [M:S6] Describe temporal movement, what happens as the scene progresses. [M:S6]
- DON'T: "vibrant", "whimsical", "hyper-realistic", "beautiful", "amazing", "stunning", and "begins to" or "starts to". Do not over-describe static elements. [M:S6]
- Positive only. Negative prompting is counterproductive. [M:S6]
- Keyframes: Ray3.14 and Ray3 support a start frame and an end frame. With keyframes describe only what CHANGES, do not redescribe the static elements. [M:S6] That is the exact tool for "ball ends resting against the boot". Whether Firefly passes an end frame to Luma: NOT VERIFIED, check the panel.
- Draft cheaply: Luma says use 720p for iteration and 1080p for finals, it saves time and credits. Luma's help page says Draft mode has full access to Ray3's understanding, use the same detailed prompt style in Draft and Hi-Fi. [M:S9 snippet only]
- Durations from Luma's field guide: 5 or 10 seconds text to video, image to video 5 seconds on Ray3.14. [M:S6] Panel decides.
- Audio: Ray3.14 and Ray3 have no native audio. [M:S6] Add sound in the edit.
- Ray3 (non-14): character reference support if you must keep a face across shots, prompt describes the scene and action only. [M:S6]
- Left versus right, which hand, small-object contact: no maker guidance. [U]
- Seed: not documented in what I retrieved. [U]
- Ray2 and the HDR variants: no separate guide retrieved. Assume the Ray rules above. [U]
- HDR/EXR: for color grading pipelines, available only at 540p and 720p and only for text to video and image to video. [M:S6] Skip unless grading an HDR sequence.

## 3. Cross-engine workflow

### 3.1 The cheap-test-then-final ladder

1. **Concept pass on the cheapest model in the same family as the final.** Veo 3.1 Lite or Fast, Kling 2.5 Turbo, Luma at 720p/Draft. [M:S6 for the Luma 720p rule, C:S6 for the others] Shortest allowed duration. Goal: does the model understand the idea at all (hand side, contact). It is a prompt test, not a pretty-picture test. [U]
2. **Fix the start frame before any more video.** If the draft shows the wrong hand, the problem is almost always upstream, in the still (next section). [U]
3. **One variable per try.** Change the prompt text OR the start frame OR the model OR the duration. Never two. Log each try in the log folder. [M:S5 for the principle]
4. **Fixed seed while testing the prompt.** If the panel shows a seed, set a number, keep it, and change only the words. If the output barely changes, the seed is locking too much, then change one more thing. Whether a seed holds across prompt edits or across Fast versus Standard: UNTESTED. Log what you see. [U]
5. **Final on the target model, target resolution, once.** Run the final prompt exactly as it passed the draft. Expect a different clip from a different model even with the same seed. [U]
6. **Stop rule: three tries, then change the design.** Three attempts with the same intent that fail the same way means the shot is wrong for the engine. Move to the shot-design tricks below, do not buy a fourth. [U] This is the fix for a nine re-render clip.

### 3.2 Building a start-frame still with the exact pose

When: use it whenever the failure is "wrong hand", "wrong side", "wrong foot", "wrong who is where", or anything that is a static arrangement. A video model inherits structure from the first image. Community guides: for image to video, let the image define appearance and use the prompt to direct motion, and if the hand is wrong in the still, rewriting the motion prompt probably will not correct it. [C:C6, search summary] Runway says the same about the image carrying the setup. [M:S5]

How:
1. Generate the still in Firefly Image (Zac clicks, graphic-design writes the prompt). Name the hand and the side in plain words, camera-relative: "his right hand, the hand nearest the camera, holds a combination wrench at the open-end". Add the foot placement: "left boot toe pointing up toward the car, right knee bent, the heel resting on the concrete". [U]
2. Check the still before using it: which hand is nearest the camera, count the fingers, check the wrench in the correct hand, boot sides. Do not pass a still with blurry hands to a video model, the artifacts get worse. [M:S5]
3. Remove implied motion from the still: no motion blur, no ball mid-air, no dust streaks, unless the prompt describes exactly that motion. [M:S5]
4. Load as References > Frames > start frame. Prompt describes motion only, short: "The man slowly turns the wrench overhead. The camera stays locked." [M:S5, U for wording]
5. For a contact shot, make a second still of the END state (ball resting touching the boot) and use it as the end frame on engines where the panel shows an end-frame slot. Prompt describes the roll between the two. [M:S2 for the method on Veo 3.1, M:S6 for Ray]
6. Aspect ratio of the still must match the clip ratio you will generate. [U]

### 3.3 Shot-design tricks that hide model weakness

All [U]. Standard editing practice, not engine documentation, none run on Zac's account yet.

1. **Cut on the moment of contact.** Show the ball rolling in from the left (clip A), cut to a tight clip of the boot with the ball already resting against it (clip B). The model never has to render the touch. Two easy clips beat one hard clip.
2. **Frame out the contact point.** Shoot from low behind the foreground (the car's tire, the jack stand, the creeper wheel) so the toe-ball touch happens behind something. The model then has no wrong detail to render.
3. **Make contact a stop, not a hit.** Ask for a ball that rolls slowly and comes to rest, with no impact moment. Resting contact is a lower bar than a bump.
4. **Short clips.** Ask for 4 or 5 seconds, use 3. Subtle change works best in short clips. [M:S1]
5. **Pre-cut the shot.** Use the last frame of clip A as the start frame of clip B. [M:S5 for the extract-last-frame method]
6. **One hand per clip, shown from one side.** Do not show both hands working. If the wrong hand comes out, check if the shot is symmetric (no text, no horse emblem, no plate, no logo) and flip it horizontally in Premiere. Never flip a shot with the Mustang emblem, a plate or any lettering in view. Cheap, but check first.
7. **Cut away on the hand.** Keep the wrench hand at the edge of the frame or in shadow when the story beat is the face or the ball.
8. **Over-the-shoulder or POV frames** hide which hand is where better than a clean profile. [M:S1 lists both framings]
9. **Audio sells contact.** A soft thud or a leather scuff laid in the edit makes a half-seen touch read as a touch. Add it in Premiere from the Adobe SFX library. See the Ian sound packet.

## 4. Credit math

I could not retrieve Adobe's own credit table (the Adobe help pages returned 403). Third-party write-ups quote per-second rates that disagree with one another, one source for the same model gives 20, another 10, community threads report 40 for 4 seconds and 80 to 160 for 8 seconds on Veo 3.1 Fast, and Adobe's Firefly community has a bug thread titled "Veo models list incorrect credit cost when two keyframes are added" (title only, not opened). I am not putting numbers in this guide.

What Zac does: read the credit readout on the Generate button for the exact model, resolution, duration and audio setting BEFORE clicking, and re-read it after adding an end frame, adding audio or changing the resolution. Write that number in `settings.txt` in the log folder. Zac's pool is 11,000 credits a month (4,000 plus 7,000, memory `firefly-models.md`) and the balance read zero on 2026-11-17, so check the account page first.

## 5. Worked example: Ian Griffin "Wrench Turner" trailer clips

Source for the shots: `D:\WKP\Post-Production\reports\Ian-Trailer-Asset-Review-and-Cover-Opener-2026-11-16.md`, Section 1 table. I do not have the old prompts (Zac supplies those). Every prompt below is a rewrite from the shot descriptions, UNTESTED. Raw footage is at `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Raw Footage`. Spoiler fence (draft 3.2 Section 0): no child in present-day shots, no family words. Nothing below breaks it.

Decision that must be made before any prompt is run: **which side of the man faces the camera.** The prompts assume his RIGHT side faces the camera, so his right hand is the hand nearest the camera. If you want the left, swap the words, do not leave it open.

### V1 (man on a creeper under the red Mustang, works a wrench overhead, then lowers it to his chest)

Failure seen: wrong hand on the wrench. Cause guess: the prompt never fixed the side, the model picked one. [U]

Rewrite (start-frame route, recommended): first build a start still (3.2) of the man lying on the red creeper, camera at floor level looking at his right side, right hand raised holding the wrench on the open-end, left arm resting on his chest. Then the video prompt, any engine that takes a start frame:

`The camera stays locked. The man turns the wrench slowly overhead with his right hand, the hand nearest the camera. After about two seconds his arm comes down and the wrench rests on his chest. He lies still and looks up at the car. Warm caged work lamp light, dust in the air.`

If no start frame (text only, Veo 3.1, Luma Ray3.14 style):

Veo skeleton: `Locked-off low side shot at floor level. A man in a black tee and jeans lies on a red creeper under a red Mustang, his right side toward the camera. His right hand, the one nearest the camera, holds a wrench overhead and turns it slowly. Then the arm lowers and the wrench rests on his chest. Garage, caged work lamp, concrete floor. Gritty film look, shallow depth of field. SFX: slow ratchet clicks that stop. Ambient noise: low garage hum.` [M:S2 format, U]

Luma skeleton: `A man in a black tee lying on a red creeper under a red Mustang, turning a wrench overhead with his right hand nearest the camera, then lowering it to his chest, dust floating in the caged lamp light, locked camera, warm low lighting.` [M:S6 template, U]

Do: ONE motion (turn then lower), the sides named once. Do not: "his arm" without a side, "begins to turn", "no left hand".

### V2 (nose-on Mustang, worn ball enters from the left, rolls to the middle then toward camera)

Worked as shot per the review. Keep it. Safety rewrite if it must be re-rolled: `Locked-off wide shot, the red Mustang seen nose-on on jack stands in a garage. A worn baseball enters from the left edge of the frame and rolls slowly across the concrete floor toward the middle, slowing as it goes. Soft garage light, dust. SFX: a quiet rolling sound on concrete.` [U] Directions are screen-relative ("from the left edge of the frame") so there is only one reading. [U, C:C2 uses the same phrasing]

### V4 (ball rolls in and bumps the boot, wanted: rests against the foot, not the toe)

Failure seen: ball hits the toe. This is the contact case. Per the review plan V4 is cut, but it is the best test bed for the contact tips, so here is the method. [U]

1. Stills: start still with the ball at the left, boots sticking out from under the car; end still with the ball resting against the outer side of the left boot, level with the middle of the foot, touching the leather. Same framing, same light.
2. Video, Veo 3.1 with first and last frame (or Luma Ray3.14 with keyframes if the panel offers an end frame): `The ball rolls slowly from the left, losing speed, and comes to rest touching the side of the boot. The camera stays locked. Dust drifts in the warm low sun.` Describe only what changes between the frames. [M:S6 and M:S2 for the method]
3. If no end frame is offered: `A worn baseball rolls slowly across the concrete from the left of the frame and stops against the outside edge of a brown boot, level with the laces. The boot does not move.` Positive end state, no "does not hit". [M:S1 for no negation, U]
4. If still wrong after three tries: shot-design trick 1 and 2 above. Cut on the contact.

### V7 (canvas-covered coupe, garage door rises, dust rolls through, sun floods the car)

The review marked it strong. If re-rolled: `Locked-off wide shot inside a dim garage. A canvas dust cover over a coupe. The garage door rises slowly, sunlight pours in, dust clouds drift across the floor and settle on the cover. Warm light, high contrast. SFX: a rolling garage door, then quiet. Ambient noise: faint wind.` [M:S2 audio format, U]

### 9Sa (worn ball on concrete, a dirty hand enters upper left at 2 s, closes around it, lifts)

Hands are the failure risk (review Section 5). One hand, one action. Start from a still of the ball with the car out of focus. `The camera stays locked on the ball. From the upper left of the frame a hand in a black sleeve reaches in, the fingers close around the baseball, and it lifts out of frame.` [U] Name no second hand, no finger counts in the motion prompt, put the clean hand in the start still, and check frame by frame (as the review says) before using.

## 6. Pre-flight checklist (run before handing any prompt to Zac)

1. Which engine, which tier (draft or final)? One purpose per clip.
2. Is the side or hand named in camera-relative words, and is it fixed in a start frame if it matters?
3. Is the end state written as a positive, concrete picture (resting against the heel, not "does not hit the toe")?
4. One action only. Under 100 words. No banned words (Luma list). No "begins to".
5. Camera sentence written, or "locked-off" written. No panel preset fighting the text.
6. Duration is the shortest that holds the beat.
7. Audio: the engine has it or it does not. If it does not, plan the sound in the edit.
8. Is there an end-frame slot for this model in the panel? If the contact is the failure, use it.
9. Settings written down: model, resolution, ratio, fps, duration, audio, seed, start frame file, credit readout.
10. LESSONS.md read. Do not repeat a failed phrase.
