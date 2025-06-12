pip install -r requirements.txt
winget install poppler 

# may need to run this a couple of times as pwsh needs to restart

try {
    # Get full path to pdfinfo.exe
    $pdfinfoPath = (Get-Command pdfinfo).Source
    $pdfinfoDir = Split-Path $pdfinfoPath

    # Get existing user PATH
    $currentUserPath = [Environment]::GetEnvironmentVariable("Path", "User")

    # Only add if it's not already included
    if ($currentUserPath -notlike "*$pdfinfoDir*") {
        $newUserPath = "$currentUserPath;$pdfinfoDir"
        [Environment]::SetEnvironmentVariable("Path", $newUserPath, "User")
        Write-Host "`n✅ Added to user PATH: $pdfinfoDir" -ForegroundColor Green
        Write-Host "🔁 Please restart your terminal or IDE to apply the change."
    } else {
        Write-Host "`nℹ️ Already in user PATH: $pdfinfoDir" -ForegroundColor Yellow
    }
} catch {
    Write-Host "`n❌ Error: Could not find 'pdfinfo'. Make sure Poppler is installed and pdfinfo is available in this shell." -ForegroundColor Red
}
