# Starts the paper watcher with the three Alpaca variables copied from the User scope into this process.
# The Bash tool and older shells may not see user variables set after they started. Values are never printed.
# Usage:  powershell -File run_watcher.ps1 --smoke
#         powershell -File run_watcher.ps1 --counted --loop
foreach ($n in 'APCA_API_KEY_ID','APCA_API_SECRET_KEY','APCA_API_BASE_URL') {
    $v = [Environment]::GetEnvironmentVariable($n, 'User')
    if ($v) { [Environment]::SetEnvironmentVariable($n, $v, 'Process') }
}
$py = 'C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe'
& $py -I (Join-Path $PSScriptRoot 'run.py') @args
exit $LASTEXITCODE
