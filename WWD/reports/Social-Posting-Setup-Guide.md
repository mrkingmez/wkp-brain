# Social Posting Setup Guide (one time)

Goal: let a script on your PC post a short from `L:\` to Winter Wolf's Den on Facebook, Instagram and YouTube. Written 2026-10-15. The script is `D:\WKP\.claude\skills\wwd-review-pipeline\scripts\post_short.py`. It passed a dry run (sends nothing) but has not touched a live account yet. Menu names on Meta and Google change often, so if a button is called something slightly different, tell me what you see.

Never paste a token or secret into chat. Put them only where this guide says.

## Part 1: Facebook and Instagram (Meta)

Do this signed in as you, the person who manages the Winter Wolf's Den page.

1. Go to developers.facebook.com and sign in. If it asks you to register as a developer, accept (it is free).
2. Click My Apps, then Create App. Name it `WWD Poster`. Pick the use case "Other", then app type "Business". Finish creating it.
3. In the app dashboard, left menu, Settings, then Basic. Copy the App ID. Click Show beside App Secret and copy that too. Keep this page open.
4. Go to developers.facebook.com/tools/explorer (Graph API Explorer). Top right, pick `WWD Poster` as the app.
5. Click Permissions and add all of these: pages_show_list, pages_manage_posts, pages_read_engagement, instagram_basic, instagram_content_publish, business_management.
6. Click Generate Access Token. Facebook asks which pages and which Instagram account to allow. Choose Winter Wolf's Den and winterwolfsden. Approve.
7. Copy the token the Explorer shows (it is short-lived, about an hour).
8. Open PowerShell and run these three lines, pasting your own values in place of the three dots:

```
$env:META_APP_ID="..."
$env:META_APP_SECRET="..."
$env:META_SHORT_TOKEN="..."
```

9. Then run:

```
& "C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe" "D:\WKP\.claude\skills\wwd-review-pipeline\scripts\meta_token_setup.py"
```

It should print "Saved for page ... and Instagram ...". It stores the long-lived page token on your PC. It prints no secret.

If step 9 says no Instagram account is linked: in Meta Business Suite, Settings, Accounts, Instagram accounts, connect winterwolfsden to the Winter Wolf's Den page, then run step 9 again.

Possible snag: while the app is in development mode it only works for people with a role on the app, which is you. That is fine for posting to your own page. If Meta asks for App Review for a permission, tell me, because that changes the timeline.

## Part 2: YouTube (Google)

The Google account that signs in must own or manage the Winter Wolf's Den channel. Right now the channel is tied to Matt's login, so either Matt does steps 1 to 5 (about ten minutes) or Matt first adds you as a manager under YouTube Studio, Settings, Permissions.

1. Go to console.cloud.google.com and sign in.
2. Top bar, project picker, New Project, name it `WWD Poster`, Create.
3. Left menu, APIs and Services, Library. Search `YouTube Data API v3`, open it, click Enable.
4. APIs and Services, OAuth consent screen. Choose External, fill in the app name (`WWD Poster`) and your email, save. Under Test users, add the Google account that manages the channel.
5. APIs and Services, Credentials, Create Credentials, OAuth client ID, Application type Desktop app, Create. Click Download JSON. Save the file to `D:\WKP\scratch\yt_client.json`.
6. In PowerShell run:

```
setx YT_CLIENT_SECRETS "D:\WKP\scratch\yt_client.json"
```

7. The first time a YouTube post runs, a browser window opens. Sign in as the channel owner or manager and click Allow. After that it remembers.

This project has its own YouTube allowance, so the shared quota problem goes away. The default is about 10,000 units a day and an upload costs about 1,600, so roughly six uploads a day. Check that number in the Google console under Quotas before relying on it.

## Part 3: Test before the real week

Use one clip, post it as private or schedule it a day out, and check it landed. I run these for you once the guide is done:

1. Dry run for all three (sends nothing).
2. Facebook, one clip scheduled.
3. YouTube, one clip scheduled, confirm it shows Scheduled in Studio.
4. Instagram, one clip. The Instagram step has the least proof behind it, so it gets tested first by hand.

## What the script cannot do

Instagram does not let a script schedule a post. For Instagram the script waits until the time you give and then publishes, so the PC has to be on. Or it is launched by Windows Task Scheduler at 11:45 AM. If the PC is off, the Instagram post does not go out. Facebook and YouTube schedule on their own servers and do not need the PC on.
