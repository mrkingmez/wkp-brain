# Move Dev Tools Off the USB Drive: Plan

Date: 2026-10-31. For: Zac. Status: plan only, nothing moved yet.

## Why we are doing this

Drive I: is the M.2 enclosure on USB (Realtek RTL9210B). Over the last 45 days Windows logged resets and failed writes on it. Right now Git, VS Code, Node and Android Studio all run from it. When the enclosure drops out, every program running from it hangs, the desktop locks, restart hangs, and you have to hit the reset button. The log shows those hard resets (18 unexpected shutdowns).

Fix: put the programs on the internal C: drive (224 GB free, these tools are about 7 GB). Keep I: for files only.

## What is on I: today

| Item | Where | Size | Needs moving |
|---|---|---|---|
| Node.js and npm | I:\ (drive root) | small | Yes |
| Git | I:\Git | 0.4 GB | Yes |
| VS Code | I:\Microsoft VS Code | 2.7 GB | Yes |
| Android Studio | I:\Android Studio Setup | 3.3 GB | Not now (Spark Capture is paused) |

Safe already, because they live on C:: your VS Code settings and extensions, your Git settings, your Claude Code settings, and the Claude Code program itself (it only runs on Node from I:).

Also pointing at I: and needing a fix: three PATH entries (`I:\`, `I:\Git\cmd`, `I:\Microsoft VS Code\bin`) and one setting, `CLAUDE_CODE_GIT_BASH_PATH`.

## Before you start (2 minutes)

1. Close VS Code, every Claude Code window and every terminal. Claude Code runs on the Node we are replacing, so do this part outside Claude Code.
2. Plug nothing new in. Leave the enclosure connected for now.

## Part 1a: Uninstall the three programs on I: FIRST

Why first: the installer finds the old copy and upgrades it in place on I:, it does not make a new one. This was tested on 2026-10-31: Git, Node and VS Code all stayed on I: (Git went 2.55 to 2.56, Node went to 26.13.0). Right now each program has exactly one entry, so there is no guessing which one is the I: copy.

1. Click **Start**, type `installed apps`, click **Installed apps**.
2. In the search box, type `Git`. Click the three dots next to **Git**, click **Uninstall**, click **Uninstall** again, click through the wizard.
3. Search `Node`. Click the three dots next to **Node.js**, click **Uninstall**, click **Yes** or **Next** through the prompts.
4. Search `Visual Studio Code`. Click the three dots next to **Microsoft Visual Studio Code (User)**, click **Uninstall**, click **Yes**.
5. Nothing will work in Claude Code or VS Code until Part 1b is done. That is expected.

## Part 1b: Install fresh copies on C:

1. Right-click the **Start** button, click **Terminal (Admin)**, click **Yes**.
2. Paste this line and press Enter. Wait for it to finish:
   `winget install --id Git.Git -e --source winget`
3. Paste this line and press Enter. Wait for it to finish:
   `winget install --id OpenJS.NodeJS.LTS -e --source winget`
4. Paste this line and press Enter. Wait for it to finish:
   `winget install --id Microsoft.VisualStudioCode -e --source winget`
5. If any step asks you to accept terms, type `Y` and press Enter.
6. Check each landed on C: by pasting this and pressing Enter:
   `Test-Path "C:\Program Files\Git","C:\Program Files\nodejs","$env:LOCALAPPDATA\Programs\Microsoft VS Code"`
   You want three lines that say `True`. If any says `False`, stop and tell me.
7. Close the terminal.

## Part 2: Point Windows at the new copies

1. Click **Start**, type `environment variables`, click **Edit the system environment variables**.
2. Click the **Environment Variables** button.
3. In the top box (User variables), click **Path**, then **Edit**.
   - Click the line `I:\Microsoft VS Code\bin`, click **Delete**. Click **OK**.
4. In the same top box, find `CLAUDE_CODE_GIT_BASH_PATH`, click **Edit**.
   - Change the value to `C:\Program Files\Git\bin\bash.exe`. Click **OK**.
5. In the bottom box (System variables), click **Path**, then **Edit**.
   - Click `I:\`, click **Delete**.
   - Click `I:\Git\cmd`, click **Delete**.
   - Click **OK**.
6. Click **OK** on the other windows to close them.

## Part 3: Check it worked (2 minutes)

1. Click Start, type `powershell`, open **Windows PowerShell** (normal, not admin).
2. Paste this and press Enter:
   `where.exe node git code claude`
3. Every line should start with `C:\`. If you see any line starting with `I:\`, stop and tell me.
4. Paste `node --version` then `git --version` then `claude --version`. All three should print a version number.

## Part 4: Clean up the old copies (I do this with you)

Tell me when Parts 1 to 3 are done. I will:
1. Confirm the three programs are gone from I: and registered only on C:.
2. Delete whatever the uninstallers left behind on I: (leftover Git, VS Code and Node folders, plus the loose Node files in the root: `npm`, `npx`, `corepack`, the `.cmd` and `.ps1` files, `node_modules`).
3. I only delete after Part 3 passes, and I list each item first.

## Part 5: Restart and settle

1. Restart the PC. GPU scheduling (already switched on) takes effect, and Windows starts with no program depending on I:.
2. Open VS Code and Claude Code once, to confirm your settings and extensions came through.
3. Leave I: for storage only (footage, backups, big files).

## Android Studio (later)

It still runs from I:. It is paused work (Spark Capture), so leave it alone and do not open it until it is moved. When Spark Capture restarts, reinstall to C: and delete the I: copy.

## If something goes wrong

- Parts 1a to 3 leave nothing to fall back on while you work, so do them in one sitting. Your VS Code settings, extensions, Git settings and Claude Code settings are on C: and are not touched by the uninstall.
- If Part 1b fails, tell me the exact message. The installers can be re-run, and the old programs can be reinstalled from winget if needed.
- Part 2 only edits PATH and one setting. Windows made a restore point earlier today (Before WKP PC fixes).

## After the move: watch the drive

For two weeks, check the system log for new resets on the enclosure. If the errors stop with no programs on it, the freezes were the programs hanging on a flaky drive. If errors continue, test the cable, a rear motherboard port, and enclosure heat. A free internal M.2 slot would be the safest home for anything that must run from a second drive. I have not checked whether your board has a free one.
