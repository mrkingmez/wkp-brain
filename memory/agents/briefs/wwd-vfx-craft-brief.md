# Craft Brief: wwd-vfx

Written 2026-11-22 by wwd-vfx. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` part 1. Reviewer: wwd-director. Tool versions at time of writing: Adobe apps on this machine are 26.5 (toolkit file `.claude\agents\_spec\wwd-vfx-toolkit.md`, verified 2026-10-25); the ffmpeg docs retrieved were the live ffmpeg.org pages. Re-retrieve by 2027-02-20 (90 days) or when YouTube, Firefly or ffmpeg change.

Status: COMPLETE by count (6 retrieved primary sources, 0 community) but with two named holes: no Firefly maker page and no named motion designer could be retrieved. Everything about Firefly credit cost, start frames and durations stays UNSOURCED here. See "NOT RETRIEVED".

Tags used: SOURCED (quote from a page retrieved today), PROVEN (seen in our own logged outputs at least twice, path given), PROPOSED (our idea, untested, test named).

## 1. What world-class looks like in this craft
1. An end card is built around the end screen YouTube lays on top of it: the element zones are fixed, the card exists to frame them, and nothing the viewer must read sits on a zone. SOURCED (S1).
2. The card lives inside the real window: only the last 5 to 20 s of a video of 25 s or more carry an end screen, so a 12 s card is correct and a 25 s card is waste. SOURCED (S1).
3. Delivery matches the recording: same frame rate as the show, H.264, MP4. The show exports at 30 fps (probed 2026-11-22, A Knight's Tale final export, 1920x1080, r_frame_rate 30/1). SOURCED (S3) and PROVEN (ffprobe on the kit cards, 5 of 5 MP4 probed at 30/1).
4. Transparency is deliberate: ProRes 4444 can carry alpha, an opaque 4:2:2 card does not, and the MP4 is the safe copy because ProRes freezes on Zac's machine (his report, memory). SOURCED (S5) plus house rule.
5. Reveals and fades are built with exact-duration filters so the piece lands on the frame count the spec says (a 6.000 s sting is 180 frames at 30 fps). SOURCED (S4).
6. Anything the hosts edit is exposed as a template property (text field, color, slider), not baked into pixels. SOURCED (S6, 2017, old).
7. A sting is short and the hit lands early; the intro cap is 6 s (Zac, 2026-11-19, `memory\feedback-intro-length.md`). House rule, not a maker rule.
8. A credit-spending generation is the last step, after a free code-built or compositing route is ruled out, and is preceded by the cheapest test. Maker credit costs could not be retrieved, so cost is read at the Generate button (`memory\topics\firefly-models.md`).

## 2. Sources (retrieved 2026-11-22)

### S1 YouTube Help, "Add end screens to videos"
URL: https://support.google.com/youtube/answer/6388789  Retrieved: 2026-11-22 (WebFetch).
- "Your video has to be at least 25 seconds long to have an end screen."
- "End screens can be added to the last 5–20 seconds of a video."
- "You can add up to four elements to your end screen for videos with standard 16:9 aspect ratio."
- "End screen elements will show at the same time by default."
- "Viewers can't see your end screens in these places:" (mobile web except iPad, YouTube Music and Kids apps, Flash, 360 videos).
Changes our work: the 12 s card is inside the window; zones must be on screen from the card's first frame because the elements appear together; at most 4 zones. Tag SOURCED.

### S2 YouTube Help, "Add info cards to videos"
URL: https://support.google.com/youtube/answer/6140493  Retrieved: 2026-11-22 (WebFetch).
- "You can add up to 5 cards to one video."
- "Info cards can feature a video, playlist, channel, or link."
- "On mobile, viewers can see the card icon whenever the player controls are showing."
Changes: the WWD rule is exactly 3 cards in the first 3 minutes (house lock, `WWD\CLAUDE.md`), under the platform cap of 5. SOURCED for the cap, house rule for the 3.

### S3 YouTube Help, "YouTube recommended upload encoding settings"
URL: https://support.google.com/youtube/answer/1722171  Retrieved: 2026-11-22 (WebFetch).
- "Container: MP4"
- "Video codec: H.264"
- "Common frame rates include: 24, 25, 30, 48, 50, 60 frames per second (other frame rates are also acceptable)."
- "Content should be encoded and uploaded in the same frame rate it was recorded."
Changes: kit pieces are 30 fps to match the show. All 18 logged Veo clips are 24 fps (`data\firefly-prompt-guide\LESSONS.md`), so a generated clip placed on the 30 fps timeline is a conform decision for Premiere, flagged in the run sheet. SOURCED.

### S4 FFmpeg Filters Documentation (fade, drawtext)
URL: https://ffmpeg.org/ffmpeg-filters.html  Retrieved: 2026-11-22 (curl, text extracted, section 11.87 fade, drawtext).
- fade: "If set to 1, fade only alpha channel, if one exists on the input."
- fade: "At the end of the fade-out transition, the output video will be filled with the selected color."
- fade: "If both duration and nb_frames are specified, duration is used."
- drawtext: "The expressions which specify the offsets where text will be drawn within the video frame. They are relative to the top/left border of the output image."
Changes: a video fade-out ends in the fade color (black by default), so a card whose zones must stay visible to the last frame fades audio only (done in drill 1). SOURCED.

### S5 FFmpeg Codecs Documentation (ProRes, prores-ks)
URL: https://ffmpeg.org/ffmpeg-codecs.html  Retrieved: 2026-11-22 (curl, section 9.31).
- "Specify number of bits for alpha component."
- "Possible values are 0, 8 and 16."
- "Use 0 to disable alpha plane coding."
- profile list: proxy, lt, standard, hq, 4444, 4444xq.
Changes: the kit `.mov` cards probe as `prores yuv422p10le` (probed 2026-11-22 on `End Card - A Knights Tale.mov` and `Next Up - Percy Jackson Season 3.mov`), which has no alpha channel. Fine for opaque cards, but the spec line ".mov with alpha" is not true for them. Alpha pieces need `-profile:v 4444` and an alpha pixel format. SOURCED plus PROVEN (ffprobe).

### S6 Adobe blog, "Creating Motion Graphics templates in Adobe After Effects" (Adobe UK Team, 2017-09-22)
URL: https://blog.adobe.com/en/publish/2017/09/22/creating-motion-graphics-templates-in-adobe-after-effects  Retrieved: 2026-11-22 (WebFetch). Old (AE 14.2 era): a principle, not current steps.
- "In After Effects v14.2 or later, open “Essential Graphics”"
- "Click on “Solo Supported Properties”, then drag the supported properties into Essential Graphics,"
- "Anything that can be controlled by a text field, color picker, slider, or checkbox"
- "Use the “Set Poster Frame” button to have the poster frame set as your current position in the timeline"
Changes: a recurring kit piece with changing text (Next Up title and sub line) is a .mogrt candidate. PROPOSED. Test, free: export one Next Up .mogrt from After Effects 2026, change the title in Premiere's Essential Graphics panel, confirm it renders.

## NOT RETRIEVED
- NOT RETRIEVED: https://helpx.adobe.com/premiere-pro/using/work-with-motion-graphics-templates.html, HTTP 403 (WebFetch and curl with a browser user agent).
- NOT RETRIEVED: https://helpx.adobe.com/after-effects/using/creating-motion-graphics-templates.html and the uk copy, HTTP 403.
- NOT RETRIEVED: the Firefly partner-models video page (https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-non-adobe-models.html), the Firefly text-to-video page, the Generative credits FAQ, the Firefly video editor page and https://helpx.adobe.com/firefly/get-set-up/learn-the-basics/non-adobe-models-in-adobe-products.html, all HTTP 403. A web search returned summaries of these pages (start frame under the Frame option, credits per second, a forum post about Fast doubling from 80 to 160 credits). Those are search summaries, not retrieved page text, so none of it is used as fact here. Anyone needing Firefly credit or frame rules reads the panel at the Generate button, or asks the main session for a Chrome pull of the Adobe pages.
- NOT RETRIEVED: https://helpx.adobe.com/premiere-elements/using/designing-titles-tv.html (safe margins), HTTP 403. The 90 and 80 percent figures came from a vendor page named in a search result, not retrieved: COMMUNITY, so PROPOSED for web delivery.
- NOT RETRIEVED: a named motion designer with a dated tutorial. A search returned only Skillshare listings and a LottieFiles lesson that returned HTTP 404. No quote is claimed.
- Local inputs read, not counted as sources: `.claude\agents\_spec\wwd-vfx-toolkit.md` (2026-10-25), `memory\feedback-intro-length.md`, `memory\topics\firefly-models.md`, `data\firefly-prompt-guide\LESSONS.md` (2026-11-22).

## 3. What this changes in our work
- End cards are built for the end screen: 12 s (inside 5 to 20 s), at most 4 zones, zones drawn from frame 0, no text over a zone or its label (S1). The Vision Quest finale card breaks the no-overlap line (see the gap audit).
- Every kit piece is 30 fps, H.264 MP4, yuv420p (S3).
- Do not fade a card to black if a zone must stay visible to the last frame (S4).
- Do not promise alpha on a ProRes .mov unless the profile is 4444 and the probe shows an alpha pix_fmt (S5).
- Recurring text pieces become template candidates (S6, PROPOSED, free test named).
- Before any Firefly or Veo run: read the panel for cost, offer the cheapest model test first, tag every instruction PROVEN, SOURCED or PROPOSED. PROVEN Veo items exist only in `data\firefly-prompt-guide\LESSONS.md` F1 and F5 (a named thing gets drawn, left and right placement in text is ignored, both seen on 2 or more clips).

## 4. Open questions the sources did not answer
- Firefly: which models take an end frame, credit per second per model, duration list per model. Needs the Adobe helpx pages (403 to automated fetch).
- Whether safe margins matter for YouTube web delivery at all (a broadcast concept). Needs a retrieved Adobe or YouTube page.
- How YouTube sizes the real end screen elements on phone versus desktop. Needs a test upload as unlisted, Zac's step, free.
- Current best practice for a logo sting from a named motion designer.
