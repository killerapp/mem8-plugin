@echo off
REM {{cookiecutter.project_name}} - Windows Sync Script
REM Syncs thoughts directory with git repository

echo Syncing {{cookiecutter.project_name}}...

REM Check if we're in a git repository
if not exist ".git" (
    echo Error: Not a git repository. Run 'git init' first.
    exit /b 1
)

REM Add all changes in thoughts directory
echo Adding changes...
git add thoughts/

REM Check if there are changes to commit
git diff --cached --quiet
if %errorlevel% == 0 (
    echo No changes to sync.
    exit /b 0
)

REM Get commit message from user or use default
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Update thoughts: %date% %time%

REM Commit changes
echo Committing changes...
git commit -m "%commit_msg%"

REM Push to remote if it exists
git remote | findstr origin >nul
if %errorlevel% == 0 (
    echo Pushing to remote...
    git push origin main
    if %errorlevel% == 0 (
        echo ✅ Thoughts synced successfully!
    ) else (
        echo ⚠️  Committed locally but failed to push to remote.
    )
) else (
    echo ⚠️  No remote repository configured. Changes committed locally only.
    echo To add remote: git remote add origin {{cookiecutter.shared_repo_url}}
)

echo.
echo Sync complete. Status:
git status --porcelain thoughts/