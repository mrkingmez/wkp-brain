# Why We Can't Post WWD Shorts Through the Connectors, and How to Fix It

Prepared 2026-10-15 for Zac. Trigger: the five finished Other Mommy shorts could not be posted to YouTube, Instagram or Facebook from a Claude session, even though the accounts are connected.

## The short answer

The accounts are connected and working. The problem is not your logins and not the clips. The problem is that every connector I have runs on someone else's cloud servers, and those servers cannot read a file from your PC. Posting a video means moving the video file to the platform. Nothing I have can carry a file from `L:\` to Facebook, Instagram or YouTube.

This is a limit of how these connectors are built. Finding a different connector that takes a local file is a real fix, but there is a cheaper one that needs no new vendor, described at the end.

## What I tested on 2026-10-15

| Route | What I did | What happened | Verdict |
|---|---|---|---|
| Composio, Facebook | Listed your pages, then tried to schedule clip 1 on Winter Wolf's Den (page 104052046075172) with the local file path | Pages listed fine. The upload call rejected the path: it wants a file that was already staged on Composio's storage (an "s3key") or a public link, not a path on your PC | Connected, cannot take a local file |
| Composio, Instagram | Read the account info for winterwolfsden | Account reads fine (Creator account, 961 posts). Its publish call takes a public video link or a staged file | Connected, same file problem. Also no scheduling option, it publishes immediately only |
| Composio, YouTube | Asked which channel the connection controls | Google answered "quota exceeded" (HTTP 403). Quota is the daily allowance of API calls | Blocked right now. Resets around 3 AM ET, and quota is shared |
| OpusClip | Listed its connected accounts | YouTube, Instagram and all the Facebook pages are connected. But it only posts clips that live inside an OpusClip project, and it makes you approve each post in its own app | Would mean re-processing finished clips, which changes them |
| VidIQ | Listed YouTube and Instagram accounts | YouTube is signed in as Matt's account. No Instagram account connected. Its upload takes a public link only | Not usable |
| Chrome, YouTube Studio | Opened Studio in your Chrome | Redirected to "create a channel". The Google account in that Chrome does not manage the WWD channel (the WWD channel's connected login is Matt's) | Wrong account |
| Chrome, Meta Business Suite | Opened the Reel composer for Winter Wolf's Den plus winterwolfsden | The composer is correct, but its Add Video button opens a native file picker, which I cannot operate. The page exposes no hidden upload field I can reach. My upload tool also caps at 10 MB per call, and clip 1 is 12 MB | Cannot attach the file |
| Chrome, Messenger | Uploaded the EP116 transcript to Matt | Worked, because Messenger exposes a plain file field | Proof that browser upload works when the site exposes a file field |

## Why each one fails, in plain terms

1. **The cloud connectors never touch your hard drive.** Composio, OpusClip and VidIQ run on their servers. When I give them `L:\Winter Wolfs Den review show\...\clip1.mp4`, their server looks for that path on its own disk and finds nothing. They only accept (a) a file already stored on their cloud or (b) a link on the public internet that they can download from.
2. **Instagram makes this worse by design.** Instagram's standard publishing process asks Instagram's servers to fetch the video from a public link. Instagram's publishing interface also has no scheduled-post option in the form the connector exposes, so a timed post needs something on our side to fire it at the right minute.
3. **YouTube's daily quota is shared.** The YouTube connector uses one shared Google allowance. It was already used up when I tried. An upload costs a lot of that allowance, so even with a file path fixed we could hit this again.
4. **Meta's website does not let automation attach files.** Meta Business Suite hides its upload behind a native file picker. That is a browser limitation, not a Claude one.

None of this is a mistake in the clips, the captions or the accounts.

## The ways forward, ranked

### Option A (recommended): a small posting script that runs on your PC

A script in the WWD skills folder that reads the file from `L:\` and posts through the platforms' own official interfaces, with no connector in the middle. This is the only option where "any file, any time" is true, because the file never leaves your machine until it goes to the platform.

- **Facebook:** the Facebook Page video interface accepts a direct upload of a local file and supports a scheduled publish time. Winter Wolf's Den is already a page you manage (your Facebook connection shows manage-level access).
- **YouTube:** the official YouTube upload interface takes a local file and can set a publish time on upload. We would create our own Google Cloud project, so the quota is ours alone (the default allowance is enough for about six uploads a day, which fits one short a day plus the long review).
- **Instagram:** Meta documents a resumable upload for Reels that can take a local file. I have not tested it here, so treat it as to-verify before building. Because Instagram has no built-in schedule through this interface, the script would be run at 11:45 AM by Windows Task Scheduler, which needs the PC on at that time.

**What I need from you to build it:** (1) a Meta developer app and a long-lived access token for the Winter Wolf's Den page and the connected Instagram account, saved as environment variables (never in a file), (2) a Google Cloud project with the YouTube upload interface turned on, plus a one-time sign-in by whoever owns the WWD YouTube channel (Matt, or you if you are added as a manager), also stored as environment variables. I would walk you through each click.

**Cost:** free. **Risk:** Meta app review can add days if the app needs advanced permissions. Posting to your own page and account usually works in development mode, but confirm before promising a date.

### Option B: fix the connector route by staging files on a public link

Put each clip on a storage service that gives a direct public link (a cloud bucket, for example), and feed that link to the connectors. Facebook scheduling through the connector would then work today. Instagram works if the link is a clean direct MP4. YouTube still hits the shared quota problem.

- **Good:** uses accounts you have already connected. **Bad:** adds a hosting step and a place where unreleased clips sit on a public link. It also keeps the YouTube quota problem.

### Option C: switch to a scheduling tool built for creators

Tools like Buffer, Metricool, Publer and Later let you drag a file from your computer, schedule for all three platforms, and cover Instagram scheduling properly. I have not verified which of them have an interface I can drive, or which of them take a local file through an API rather than only through their website. Do not buy anything on my say-so. If you want this route I will research each one first and report back with the answers to: does it accept a local file, does it schedule Instagram Reels, does it have an API or connector I can operate, and what does it cost.

- **Good:** point and click for you, scheduling handled. **Bad:** monthly cost, and I may still be unable to operate it from here.

### Option D: keep posting by hand with the checklist

The Posting Checklist at the end of `Other Mommy (2026) - Shorts Captions.docx` gives a dated table and click-by-click steps for YouTube Studio and Meta Business Suite. About ten minutes of your time per clip across both tools. This works today and is now part of every review package.

## Recommendation

Do D today so Other Mommy's clips go out on schedule. Then build A, because it fixes the actual root cause (your files live on your PC) and removes both the vendor risk and the shared-quota risk. Hold C as the fallback if the Meta or Google setup turns out to be a time sink.

## What would make a "better connector" worth switching to

If you decide to look for a new connector instead, this is the test to give any candidate:

1. Does it take a file from the computer I am running on, not only a public link?
2. Does it schedule Instagram Reels, not only publish immediately?
3. Does it post to the Winter Wolf's Den page and winterwolfsden, and not mix them up with your other pages (the Facebook connection lists eight pages)?
4. Does it avoid a shared YouTube quota, or give us its own?
5. Can it run without an approval click in another app each time?

## Open questions for Zac

- Who should own the YouTube sign-in for the script, Matt or you as a channel manager?
- Do you want me to start the Option A setup walkthrough (Meta app first, since it also covers Instagram)?
- Should I research Option C and bring back verified answers before you decide?

## Facts I did not verify

- Whether the Instagram resumable upload works for the winterwolfsden Creator account. Meta documents it, but I did not test it.
- Whether Composio's staging could be fed from your PC through some other path. I found none in this session.
- The exact YouTube quota figures for a new Google Cloud project. The default allowance is publicly documented but I did not re-check it today.
