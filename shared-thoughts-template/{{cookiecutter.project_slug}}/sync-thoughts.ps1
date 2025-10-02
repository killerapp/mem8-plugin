# {{cookiecutter.project_name}} - PowerShell Sync Script
# Syncs thoughts directory with git repository

param(
    [string]$Message = ""
)

Write-Host "Syncing {{cookiecutter.project_name}}..." -ForegroundColor Green

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Error "Not a git repository. Run 'git init' first."
    exit 1
}

# Add all changes in thoughts directory
Write-Host "Adding changes..."
git add thoughts/

# Check if there are changes to commit
$changes = git diff --cached --name-only
if (-not $changes) {
    Write-Host "No changes to sync." -ForegroundColor Yellow
    exit 0
}

# Show what will be committed
Write-Host "Changes to be committed:" -ForegroundColor Cyan
git diff --cached --name-status thoughts/

# Get commit message
if (-not $Message) {
    $Message = Read-Host "Enter commit message (or press Enter for default)"
    if (-not $Message) {
        $Message = "Update thoughts: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    }
}

# Commit changes
Write-Host "Committing changes..."
git commit -m $Message

# Push to remote if it exists
$remotes = git remote
if ($remotes -contains "origin") {
    Write-Host "Pushing to remote..."
    try {
        git push origin main
        Write-Host "✅ Thoughts synced successfully!" -ForegroundColor Green
    }
    catch {
        Write-Warning "Committed locally but failed to push to remote."
    }
}
else {
    Write-Warning "No remote repository configured. Changes committed locally only."
    Write-Host "To add remote: git remote add origin {{cookiecutter.shared_repo_url}}" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Sync complete. Status:" -ForegroundColor Green
git status --porcelain thoughts/