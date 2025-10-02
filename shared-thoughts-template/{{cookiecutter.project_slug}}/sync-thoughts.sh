#!/bin/bash
# {{cookiecutter.project_name}} - Unix/Linux Sync Script
# Syncs thoughts directory with git repository

set -e

echo "Syncing {{cookiecutter.project_name}}..."

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "Error: Not a git repository. Run 'git init' first."
    exit 1
fi

# Add all changes in thoughts directory
echo "Adding changes..."
git add thoughts/

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to sync."
    exit 0
fi

# Get commit message from user or use default
read -p "Enter commit message (or press Enter for default): " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Update thoughts: $(date)"
fi

# Commit changes
echo "Committing changes..."
git commit -m "$commit_msg"

# Push to remote if it exists
if git remote | grep -q origin; then
    echo "Pushing to remote..."
    if git push origin main; then
        echo "✅ Thoughts synced successfully!"
    else
        echo "⚠️  Committed locally but failed to push to remote."
    fi
else
    echo "⚠️  No remote repository configured. Changes committed locally only."
    echo "To add remote: git remote add origin {{cookiecutter.shared_repo_url}}"
fi

echo ""
echo "Sync complete. Status:"
git status --porcelain thoughts/