# Mac Setup Guide: Tailscale Is On, Now Make the Mac a Second WKP Machine

Written 2026-11-16 for Zac. Follows the 2026-10-10 Tailscale Setup Guide. Print it, check the boxes with a pen.

## Where you are right now
- Tailscale is installed on the Mac and shows connected in the Tailscale admin page. Good. That was the hard part.
- Still to do, in order: (1) prove the Mac and the Windows PC can see each other, (2) keep the Mac awake, (3) turn on remote access, (4) put Claude Code and the repo on it, (5) decide what work to hand it.
- Do one Part at a time. Each Part stands alone. You can stop after any Part and nothing is broken.

## Two things this guide does NOT know
- Which macOS version the Mac runs. Part 0 finds out in 30 seconds.
- Whether the Mac is a laptop or a desktop, and whether its chip is Apple Silicon or Intel. Part 0 finds out too.
- Menu names change between macOS versions. Where a name differs, the guide gives the name for each version. If a screen does not match, stop and tell Claude what you see.

---

## Part 0: Find out what Mac you have (2 minutes)
- [ ] 1. On the Mac, click the **Apple logo** in the top-left corner of the screen.
- [ ] 2. Click **About This Mac**.
- [ ] 3. Write down these lines, exactly as shown:
  - **Chip** (says "Apple M1" or "M2" or "M3" or "M4", OR says "Processor: Intel ..."). Write it here: ______________
  - **Memory**: ______________
  - **macOS version** (says Ventura 13, Sonoma 14, Sequoia 15, or Tahoe 26): ______________
  - Model name (MacBook Air, MacBook Pro, Mac mini, iMac): ______________
- [ ] 4. Close the window.

Which Part 2 section you use depends on the macOS line. Circle it on this page now.

---

## Part 1: Confirm the Mac and the Windows PC see each other

### 1A. Find the Mac's Tailscale name and number
- [ ] 1. On the Mac, look at the **top-right of the screen** (the menu bar, near the clock). Click the **Tailscale icon** (a small dotted pattern of dots).
- [ ] 2. At the top of the menu you see the Mac's name and a number starting with `100.`. Write both down.
  - Mac name: ______________
  - Mac 100. number: ______________
- [ ] 3. If you cannot find the icon, open the Tailscale admin page instead: on any computer go to `login.tailscale.com/admin/machines`, sign in with Google, and read the Mac's row.

### 1B. Find the Windows PC's name and number
- [ ] 1. On the Windows PC, look in the bottom-right, near the clock. Click the small **up arrow** if you do not see the Tailscale icon.
- [ ] 2. Right-click the Tailscale icon. The top of the menu shows this PC's name and a `100.` number. Write them down.
  - PC name: ______________
  - PC 100. number: ______________

### 1C. Check both are on the SAME account
- [ ] 1. Go to `login.tailscale.com/admin/machines`.
- [ ] 2. You should see **both** machines in one list with green dots. If the Mac is there but the PC is not, you signed in with different accounts. Fix by logging out of the wrong one and signing in with the same Google account on both.

### 1D. Ping from the Windows PC to the Mac
- [ ] 1. On the Windows PC click **Start**, type `cmd`, press **Enter**.
- [ ] 2. Type `ping ` (with a space), then the Mac's `100.` number, press **Enter**.
  - Example: `ping 100.101.102.103`
- [ ] 3. Four lines starting with **Reply from** means it works.
- [ ] 4. **Request timed out** means not yet. Most common cause: the Mac is asleep. Wake it by pressing a key, wait 10 seconds, try again. Part 2 fixes the sleeping for good.
- [ ] 5. Try the name too: `ping ` followed by the Mac's Tailscale name. If the number works but the name does not, the name feature (MagicDNS) is off or you mistyped. Use the number. It is fine.

### 1E. Ping from the Mac to the Windows PC
- [ ] 1. On the Mac press **Command + Space** (the Spotlight search box opens).
- [ ] 2. Type `Terminal` and press **Return**. A window with text opens.
- [ ] 3. Type `ping -c 4 ` (with a space), then the PC's `100.` number, press **Return**.
  - The `-c 4` makes it stop after four tries. Without it the Mac pings forever (press **Control + C** to stop).
- [ ] 4. Lines that say **64 bytes from** mean it works.
- [ ] 5. If this one fails but 1D worked, the Windows firewall is blocking pings. Fix, on the PC: click **Start**, type `Windows Defender Firewall`, press Enter, click **Allow an app or feature through Windows Defender Firewall**, make sure **Tailscale** is checked, click **OK**, try again.

**Part 1 is done when both pings work.** Write today's date here: ____________

---

## Part 2: Stop the Mac from sleeping and from auto-locking

### What you want, in plain words
- The Mac stays awake all day and all night so you can reach it from the PC over Tailscale.
- It does NOT lock itself. **You** lock it by hand when you walk away.
- The screen itself can still go dark to save power. A dark screen is fine. A sleeping Mac is not.

### The honest security tradeoff, read this before you change anything
1. **A Mac that never auto-locks stays open to anyone who walks up to it.** If your wife, a guest or a repair person touches the keyboard, they are in your account, with your files and your logged-in sessions. You said you will lock it yourself. That is a real plan, but it only works if you actually do it. Lock with **Control + Command + Q** (hold all three, it locks instantly).
2. **Remote access and the lock screen are separate.** You can still reach a locked Mac over Tailscale with the SSH method in Part 3. A locked Mac is still awake and still on the network.
3. **FileVault is the disk encryption.** Check it: **System Settings > Privacy & Security > FileVault**. If it is ON (and it should be on a laptop), then after any restart the Mac sits at a login screen waiting for your password BEFORE Tailscale or anything else starts. That means after a power cut or an update restart, **you cannot reach the Mac until someone types the password at the keyboard.** Do not turn FileVault off to fix this. Turning it off means anyone who steals the Mac can read the drive. Accept that after a restart, someone has to log in once.
4. **Auto-login** (the Mac logs itself in at power on) cannot be used while FileVault is on. Another reason to leave FileVault on and accept the one manual login after a restart.
5. Tailscale on the Mac only runs while you are logged in to your account on that Mac. I have not verified whether the standalone app also connects at the login screen, so assume it does not.

**My recommendation:** leave FileVault on, set the Mac to stay awake, set the lock delay to the longest your macOS offers, and lock by hand with Control + Command + Q.

### 2A. First, is it a laptop or a desktop?
- Laptop (MacBook): use the **Battery** items below.
- Desktop (Mac mini, iMac, Mac Studio): use the **Energy** items below.

### 2B. Keep it awake: the main switch (pick your macOS version)
Open **System Settings**: click the **Apple logo**, then **System Settings**.

**macOS Tahoe 26 and Sequoia 15 (desktop Mac):**
- [ ] 1. In the left list click **Energy**.
- [ ] 2. Turn ON **Prevent automatic sleeping when the display is off**.
- [ ] 3. Turn ON **Wake for network access** if you see it.
- [ ] 4. Turn ON **Start up automatically after a power failure** if you see it. (After a power cut the Mac turns itself back on. With FileVault on it still waits at the login screen.)

**macOS Tahoe 26 and Sequoia 15 (laptop):**
- [ ] 1. In the left list click **Battery**. Click **Options** (bottom right, may be a small button).
- [ ] 2. Turn ON **Prevent automatic sleeping on power adapter when the display is off**. If you do not see it, see 2E below.
- [ ] 3. Turn ON **Wake for network access** if you see it.
- Keep the Mac **plugged in** the whole time. A laptop on battery will still sleep to protect the battery.

**macOS Sonoma 14 (laptop):**
- [ ] 1. Click **Battery**, then **Options**. Turn ON **Prevent automatic sleeping on power adapter when the display is off**.
- [ ] 2. If the choice is not there, click **Displays**, scroll down, click **Advanced...**, and look for the same wording.

**macOS Sonoma 14 (desktop) and Ventura 13 (desktop):**
- [ ] 1. Click **Energy Saver**. Turn ON **Prevent automatic sleeping when the display is off**. Turn ON **Wake for network access**.

**macOS Ventura 13 (laptop):**
- [ ] 1. Click **Displays**, scroll down, click **Advanced...**, turn ON **Prevent automatic sleeping on power adapter when the display is off**. (Ventura keeps this one here, not under Battery.)

### 2C. Set the screen to go dark but NOT lock, then stop the screen saver (all versions)
- [ ] 1. In System Settings click **Lock Screen** in the left list.
- [ ] 2. **Start Screen Saver when inactive:** set to **Never**. (Ventura calls the page Lock Screen too. Older wording was Desktop and Screen Saver.)
- [ ] 3. **Turn display off on power adapter when inactive** (Tahoe/Sequoia/Sonoma wording, may say "on battery" for the battery line): set to **10 minutes** or longer. A dark screen is OK. If you want it never to go dark at all, pick **Never**, but a screen that is always on wears out sooner.
- [ ] 4. **Require password after screen saver begins or display is turned off:** this is the auto-lock. Click the menu and pick the **longest** time, or **Never** if the menu offers it. Newer macOS versions top out at hours, not never. Pick the biggest one shown.
- [ ] 5. If you pick anything other than Immediately, a window may pop up warning about your login. Click **Turn Off Lock** or **OK**. It is asking whether you understand the security tradeoff above. You do.

### 2D. Lock it by hand (practice now)
- [ ] 1. Hold **Control + Command + Q**. The screen locks right away.
- [ ] 2. Type your password to get back in.
- You can also click the **Apple logo** then **Lock Screen**.

### 2E. Lid closed and always on: the Terminal way (only if you need it)
Skip this if the Mac is a desktop, or if you only leave the lid open.

A MacBook sleeps when you close the lid, even plugged in, unless an external screen, keyboard and mouse are attached (that is "clamshell mode"). If you want the lid closed with nothing attached and still reachable, you need Terminal. These are normal Apple commands, but they change power settings, so write them down so you can undo them.

Open Terminal: **Command + Space**, type `Terminal`, press **Return**.

**Look at the current settings first (changes nothing):**
```
pmset -g
```
Write down the numbers next to `sleep`, `displaysleep` and `disablesleep` so you can restore them.

**Never sleep while plugged in, screen can still go dark after 10 minutes, wake for network:**
```
sudo pmset -c sleep 0
sudo pmset -c displaysleep 10
sudo pmset -c womp 1
```
It asks for your Mac password (the cursor does not move while you type, that is normal) then press Return.
- `-c` means "only while on the charger". Battery settings are left alone, which is the safe way.

**Lid closed and still awake (laptops only):**
```
sudo pmset -a disablesleep 1
```
- This is a known setting that keeps a laptop awake with the lid shut. I could not confirm in this session that it still behaves on the newest macOS or on every chip, so test it: close the lid, wait 2 minutes, ping the Mac from the PC.
- **Heat warning:** a closed MacBook has less airflow. Never leave it closed in a bag, on a bed or on a couch cushion. Put it on a hard surface with space around it.

**Undo (put it back):**
```
sudo pmset -a disablesleep 0
```
and rerun the `sleep` and `displaysleep` lines with the numbers you wrote down.

### 2F. caffeinate: the temporary version, no settings changed
`caffeinate` keeps the Mac awake only while a command runs. When you close it, everything goes back to normal. Good for a test or one long job.
- [ ] 1. In Terminal type: `caffeinate -dims` and press **Return**.
- [ ] 2. The cursor sits there doing nothing. That means it is working. The Mac will not sleep until you press **Control + C** or close that Terminal window.
- Flags in plain words: `d` keeps the display on, `i` stops idle sleep, `m` keeps the disk on, `s` stops sleep on power adapter.
- To keep the Mac awake only while one job runs: `caffeinate -i python3 myscript.py`. It ends when the script ends.

### 2G. Test that it worked
- [ ] 1. Leave the Mac alone for **30 minutes** with the screen dark.
- [ ] 2. From the Windows PC, ping the Mac's `100.` number (Part 1D). Replies mean sleep is fixed.
- [ ] 3. If it times out, repeat 2B and check that the Mac is plugged in.

---

## Part 3: Remote Login (SSH) and Screen Sharing, only over Tailscale

### What these two are
- **Remote Login (SSH)** lets you type commands on the Mac from the PC. Best choice for running Claude Code on the Mac from your desk. The PC already has it built in.
- **Screen Sharing** lets you see and click the Mac's screen from the PC.

### The honest limit on "only over Tailscale"
The Mac has no setting that says "SSH only on the Tailscale network." Remote Login listens on the Mac's home network too, so another device at home could reach it. What keeps it away from the open internet:
1. **Never forward a port on your router.** If you never did, the internet cannot reach it.
2. **Allow only your own user** (step 3A).
3. **Use a long password** on that Mac account.
Tailscale's own SSH feature is not available in the Mac app version, so we use the Mac's normal Remote Login. That is fine.

### 3A. Turn on Remote Login
- [ ] 1. System Settings, then click **General** in the left list, then **Sharing**.
- [ ] 2. Turn ON **Remote Login**.
- [ ] 3. Click the small **(i)** button next to it.
- [ ] 4. Under **Allow access for**, pick **Only these users**. Click the **+** and add **your own Mac user**. Remove "Administrators" or "All users" if listed.
- [ ] 5. Click **Done**.
- [ ] 6. Write down the Mac username. In Terminal type `whoami` and press Return. Username: ______________

### 3B. Test it from the Windows PC
- [ ] 1. On the PC click **Start**, type `PowerShell`, press **Enter**.
- [ ] 2. Type `ssh ` then your Mac username, an `@` sign, then the Mac's `100.` number. Example: `ssh zac@100.101.102.103`. Press **Enter**.
- [ ] 3. First time it asks "Are you sure you want to continue connecting". Type `yes`, press Enter.
- [ ] 4. Type your Mac password (nothing shows while you type) and press Enter.
- [ ] 5. A line ending in `%` means you are in the Mac. Type `exit` to leave.

### 3C. Turn on Screen Sharing
- [ ] 1. System Settings, **General**, **Sharing**.
- [ ] 2. Turn ON **Screen Sharing**. (Tahoe and Sequoia show it as its own switch. If it is greyed out and says **Remote Management** is on, turn Remote Management OFF first. You cannot have both.)
- [ ] 3. Click the **(i)** button next to it.
- [ ] 4. Under **Allow access for**, pick **Only these users** and add your own user.
- [ ] 5. Click **Computer Settings...** if you see it. Turn ON **VNC viewers may control screen with password** and set a password you will remember. Write it here later, not on this page. Without this, the free Windows viewer in step 3D cannot connect.
- [ ] 6. Click **Done**.

### 3D. Connect to the Mac's screen from the Windows PC
Windows has no built-in way to open a Mac screen. You need a free viewer. Ask Claude to pick and verify one with you before you download, because downloads need your yes. Common free choices are RealVNC Viewer and TigerVNC.
- Connect to the Mac's `100.` number, port default, and use the VNC password from 3C step 5.
- **Tailscale is what protects this.** Do not forward port 5900 on your router, ever.
- If the screen shows the lock screen, you can type your password into it from the PC. That works.

### 3E. Mac-to-PC (the other direction)
Windows 11 **Home** cannot be controlled with Remote Desktop (see the 2026-10-10 guide). SSH into the PC is a different feature and is not set up. Do not worry about this direction. Work from the PC toward the Mac.

**Part 3 is done when you can SSH in from the PC.**

---

## Part 4: Claude Code and the repo on the Mac

### 4A. Install Claude Code
- [ ] 1. Open Terminal (**Command + Space**, `Terminal`, **Return**).
- [ ] 2. Paste this one line and press **Return**:
```
curl -fsSL https://claude.ai/install.sh | bash
```
- This is Claude's own installer from the official docs. It needs no extra programs. The Mac must be on macOS 13 (Ventura) or newer, per the current official instructions. If your Part 0 version is older than 13, stop and tell Claude.
- [ ] 3. **Close Terminal and open a new one** (the install changes your path, a new window picks it up).
- [ ] 4. Type `claude --version` and press **Return**. A version number means it is installed.
- [ ] 5. Type `claude` and press **Return**. A browser window opens. Click **Continue** and sign in to your Claude account. Come back to Terminal.

### 4B. Install Git
- [ ] 1. In Terminal type `git --version` and press **Return**.
- [ ] 2. If a box pops up asking to install **command line developer tools**, click **Install**, click **Agree**, and wait (it can take 10 to 20 minutes). Then type `git --version` again.

### 4C. Sign in to GitHub and clone wkp-brain
The repo is private, so the Mac has to prove it is you.
- [ ] 1. Easiest route: install the GitHub tool called `gh`. It needs Homebrew, the Mac's tool installer. Ask Claude before this step. Claude will check the current Homebrew install line with you so you are not pasting a stranger's script.
- [ ] 2. After `gh` is installed, type `gh auth login` and press **Return**. Choose **GitHub.com**, **HTTPS**, say **Yes** to authenticate Git, choose **Login with a web browser**. Copy the 8-character code, press Return, paste the code in the browser, click **Authorize**.
- [ ] 3. Pick the folder. Recommended: your home folder, so the repo is `~/WKP`. Type:
```
cd ~
gh repo clone YOUR-GITHUB-NAME/wkp-brain WKP
```
Replace `YOUR-GITHUB-NAME` with the account that owns the repo (the repo page address is `github.com/<name>/wkp-brain`). The last word, `WKP`, names the folder on the Mac.
- [ ] 4. Check it: type `ls ~/WKP` and press Return. You should see `CLAUDE.md`, `ME.md`, `TASKS.md` and more.

**Never copy the repo from the Windows PC over Tailscale.** GitHub is the source of truth. Also: **do not use Google Drive** for any of it.

### 4D. Add the Mac block to LOCAL-PATHS.md
Rule from the root CLAUDE.md: LOCAL-PATHS.md is per machine, so the Mac block is rebuilt from the Mac, never copied from the Windows block.
- [ ] 1. In Terminal, run each of these and write down what they print:
  - `pwd` while inside `~/WKP`: ______________
  - `which python3`: ______________
  - `which ffmpeg` (may print nothing, that means not installed): ______________
  - `which git`: ______________
  - `which claude`: ______________
- [ ] 2. In the Mac's `~/WKP` folder, start Claude: type `cd ~/WKP` then `claude`.
- [ ] 3. Tell Claude: "Add a new section to LOCAL-PATHS.md for this Mac. Use the values I wrote on the Mac Setup Guide. Do not copy the Windows paths." Then answer with your numbers.
- [ ] 4. The new section should look like this (the example uses a made-up username):
```
## MACHINE: MAC (macOS <version>, <chip>)

### Core
repo             /Users/<you>/WKP
scratch          /Users/<you>/WKP/scratch   (gitignored)
logs             /Users/<you>/WKP/logs
python           <result of: which python3>
ffmpeg           <result of: which ffmpeg, or "not installed">
claude           <result of: which claude>

### Notes
Tailscale name   <Mac name>   100.x.x.x
Reach it with    ssh <user>@<100.x number>
Sleep settings   see reports/Mac-Setup-Guide.md Part 2
No L:, P:, D: drives here. Raw media lives on the Windows PC.
```
- [ ] 5. Keys and tokens (Hugging Face and others) go in as environment variables on the Mac, typed by you. Never in a file in the repo.
- [ ] 6. Before you commit: ask Claude to show the change first. Then tell it to commit and push. This means the Windows PC sees the Mac block after the next `git pull`. Reminder: Windows block stays untouched.
- [ ] 7. Back on the Windows PC, run `git pull`. If the Mac block shows up in LOCAL-PATHS.md, both machines are in sync.

### 4E. Update TASKS.md
This guide covers the TASKS.md row "Tailscale and second machine". When Parts 1 to 4 are done, ask Claude to change it to Done and note the Mac's name and the date. Do not do it before they are true.

---

## Part 5: What extra power does the Mac add?

### Be straight about the starting point
Your Windows PC has an **RTX 5060 NVIDIA graphics card**. A lot of the heavy WKP tools are written for NVIDIA cards (CUDA). Macs do not have CUDA. So the Mac is **not** a faster copy of the PC. It is a **second pair of hands** that can run things at the same time.

### The question for Tuesday
Tell Claude the answers from Part 0. The answer changes the list below, because:
- **Apple Silicon (M1 to M4):** good, quiet and efficient. It has its own graphics engine (Metal). Most modern tools run well on it.
- **Intel Mac:** older. Slower, runs hot, and software support is being dropped. Some newer tools will not run on it at all.

**Ask on Tuesday: "Which chip, how much memory, how much free disk, and is it a laptop or desktop?"** Answers: Chip ______ Memory ______ Free disk ______ Laptop or desktop ______.

### Good jobs to hand it (works on either chip)
- Running **Claude Code agents** on repo work at the same time as the PC. Research, drafts, document building, QA checks, fantasy football sims (the Python ones that only use the CPU).
- Long **ffmpeg conversions** such as proxy files and format changes. Slower on Intel.
- The **nightly system check** from a second machine (TASKS.md says to add a block to machines.json for it).
- Always-on **watchers and scheduled scripts** once it never sleeps. Anything that touches money (trading) stays your call.
- A **backup copy of the repo** that it keeps pulling from GitHub.

### Maybe, depending on chip (to be checked before you count on them)
- **Transcription.** The current `transcribe.py` is built for the NVIDIA GPU and uses voiceprints that live only on the PC (gitignored, local only). On an Apple Silicon Mac there are Mac-native transcription tools, but they would need testing and the speaker labeling would need work. **Verdict: keep FrostCast transcription on the PC.** The Mac could do plain, no-speaker-label transcripts for the Fiverr side business if Claude tests it first.
- **Blender renders.** Blender runs on Apple Silicon Macs and can use the Metal graphics engine, but your scenes, assets and the Blender MCP setup are on the PC. Newer Blender versions may drop Intel Macs. I have not verified which versions. The PC with OptiX will likely finish faster. A Mac can still render a **second queue** while the PC renders another, if the files are copied across.
- **Unreal Engine 5.8.** Needs a strong Apple Silicon Mac and a lot of memory. I have not verified the requirement. Do not plan on it for this Mac until you know the chip and memory.

### Poor jobs for it
- Anything that needs your Adobe tools (Premiere, After Effects). Leave Adobe alone.
- Big raw video that lives on the PC's `L:` drive. Moving it over the network is slow, and it is not what the Mac is for.
- Anything that needs voiceprints or the Hugging Face models until someone sets them up on the Mac deliberately.

### Simple next step
After Part 4, hand the Mac one small job as a test, such as having Claude on the Mac run the fantasy football sim while the PC does something else. If it works, move up from there.

---

## Troubleshooting
- **Ping works but SSH says "Connection refused":** Remote Login is off or the Mac username is wrong. Redo 3A.
- **SSH says "Permission denied":** wrong password or your user is not on the Allow list. Redo 3A step 4.
- **Mac vanishes from the Tailscale list every night:** it is sleeping. Redo Part 2, make sure it is plugged in.
- **Mac vanished after a restart or update:** FileVault is waiting at the login screen. Someone has to type the password once at the Mac.
- **Tailscale icon missing on the Mac:** click the **Apple logo, System Settings, General, Login Items**, and make sure Tailscale is allowed to run in the background.
- **Two Tailscale apps on the Mac:** Tailscale says do not install both the App Store version and the downloaded standalone version. If you see two, ask Claude which to remove before you delete anything.
- **Something does not match this page:** do not guess. Stop and tell Claude what the screen says.

## What I could not verify
- The exact menu wording on your macOS version (checked against Apple's Mac User Guide search results only, not on a real Mac). Wording above covers Ventura to Tahoe, but the Battery and Displays locations may differ by model.
- That `pmset disablesleep 1` still works on the newest macOS and on every chip.
- Whether the Mac Tailscale app connects before login.
- Whether any Windows VNC viewer works with Apple's Screen Sharing on your exact version. Claude will check before you download one.
- The current Homebrew install line. Claude checks it with you in Part 4C.
- Blender and Unreal Mac requirements for the versions you run.
- Tailscale's free plan limits. Check `tailscale.com/pricing`.

## Sources checked 2026-11-16
- Apple Mac User Guide, Energy settings: https://support.apple.com/en-in/guide/mac-help/mchle41a6ccd
- Apple Mac User Guide, Lock Screen settings: https://support.apple.com/guide/mac-help/mchlp1168/26/mac/26
- Tailscale on macOS (Standalone vs App Store, SSH note): https://tailscale.com/docs/concepts/macos-variants
- Claude Code setup (install command, macOS 13+): https://code.claude.com/docs/en/setup
- MacRumors, stop Mac sleeping with display off: https://www.macrumors.com/how-to/stop-mac-sleeping-when-display-off/
