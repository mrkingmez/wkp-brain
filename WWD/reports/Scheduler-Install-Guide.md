# Scheduler v2: Install and Weekly Use

Files: `D:\WKP\WWD\opusclip\scheduler\Code.gs` and `Index.html`
Approved copy (when the writing room finishes): `D:\WKP\WWD\opusclip\EP119-approved-copy.json`

## Part 1. One-time install (about 10 minutes)

### A. Get a new Opus Clip API key
1. Open Opus Clip in your browser and sign in.
2. Go to your account settings and find the API keys page.
3. Delete the old key (the one that was pasted into the script). This is the one pasted into our chat.
4. Create a new key. Copy it. Do not paste it into chat or into any file.

### B. Open your scheduler project
1. Go to script.google.com and sign in with the Google account that owns the scheduler.
2. Click your scheduler project (Winter Wolf Den Scheduler) to open the editor.

### C. Put the new key in safely
1. In the left bar, click the gear icon, Project Settings.
2. Scroll down to Script Properties and click Add script property.
3. In the Property box type: OPUS_KEY
4. In the Value box paste the new key.
5. Click Save script properties.

### D. Replace the code
1. In the left bar click Editor (the angle brackets icon), then click the file Code.gs.
2. Click inside the code, press Ctrl+A to select all, press Delete.
3. On your computer open `D:\WKP\WWD\opusclip\scheduler\Code.gs` in Notepad. Press Ctrl+A, Ctrl+C.
4. Back in the editor click inside the empty Code.gs and press Ctrl+V.
5. Press Ctrl+S to save.
6. In the left file list click the file named Index (Index.html). Select all and delete.
7. Open `D:\WKP\WWD\opusclip\scheduler\Index.html` in Notepad. Ctrl+A, Ctrl+C.
8. Paste it into the Index file in the editor. Ctrl+S to save.

### E. Publish the new version
1. Top right, click Deploy, then Manage deployments.
2. Click the pencil icon (Edit) on your existing deployment.
3. Under Version click the dropdown and pick New version.
4. Execute as: Me.
5. Who has access: set it to Only myself.
6. Click Deploy. Keep the same web app link.

### F. Quick test (schedules nothing)
1. Open your scheduler link. The page header should say Opus Clip Scheduler v2.
2. In the purple box paste P3110504VBE4 and click Load Episode. You should see "Godzilla UNLEASHES..." and 46 clips found.
3. If you see "OPUS_KEY is missing", redo step C.
4. If Google asks you to authorize the script, click Review permissions, pick your account, Advanced, Go to (project name), Allow.

## Part 2. Schedule EP119 (after the writing room finishes)

1. Open `D:\WKP\WWD\opusclip\EP119-approved-copy.json` in Notepad. Ctrl+A, Ctrl+C.
2. Open the scheduler, choose the EP119 project in the dropdown.
3. Start date: pick the Thursday that starts the week (Thursday 2026-11-05).
4. Click Load Clips from This Project.
5. Click inside the Approved copy box and press Ctrl+V. The line under it should say Matched 31 of 46 clips.
6. Check the Copy column: the 31 scheduled clips should say APPROVED.
7. Check the boxes under Platforms (YouTube, Instagram, Facebook) and leave "YouTube: one a day only" ticked.
8. Look at the schedule tab. Move any Vision Quest spoiler clips to later days by unticking them first if the plan puts them too early (Claude will list which clips are spoilers).
9. Click Auto-Schedule Selected Platforms. A panel appears in the middle of the page. Read it, then click YES, GO. (Claude can do steps 1 to 9 for you in Chrome. Say "go" in chat and Claude clicks YES, GO.)
10. Watch the Activity Log tab. Every line should start with OK. Any FAIL line, tell Claude.

## Part 3. Every week after this

1. Download the episode. Claude runs the transcript, chapters, audio cut and the Messenger send.
2. Upload the video to Opus Clip (your saved settings apply). Tell Claude when it finishes.
3. Claude reads the clips, writes the copy through the writing room, and hands you the JSON file.
4. You repeat Part 2.

## Undo

Click Cancel All Scheduled For This Project at the bottom of the page. It works even after you reload the page.
