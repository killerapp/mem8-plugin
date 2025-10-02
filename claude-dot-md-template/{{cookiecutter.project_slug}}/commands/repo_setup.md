# Repository Setup - GitHub Integration

Set up GitHub repository integration for mem8 workflow.

## Initial Setup Steps

### 1. Verify GitHub CLI Authentication
```bash
gh auth status
```

If not authenticated:
```bash
gh auth login
```

### 2. Set Default Repository
Navigate to your project directory and set the default repository:
```bash
gh repo set-default
```

This will prompt you to select from detected repositories or enter manually.

### 3. Create Workflow Labels

Create the standard mem8 workflow labels:
```bash
gh label create "needs-triage" --color "d73a4a" --description "Needs initial review"
gh label create "needs-research" --color "fbca04" --description "Investigation required"
gh label create "ready-for-plan" --color "0e8a16" --description "Ready for implementation plan"
gh label create "ready-for-dev" --color "1d76db" --description "Ready for development"
gh label create "in-development" --color "5319e7" --description "Active development"
gh label create "ready-for-review" --color "f9d0c4" --description "Ready for code review"
```

### 4. Optional: Create Additional Labels
```bash
# Priority labels
gh label create "priority-high" --color "ff0000" --description "High priority issue"
gh label create "priority-medium" --color "ff9500" --description "Medium priority issue"  
gh label create "priority-low" --color "0e8a16" --description "Low priority issue"

# Type labels
gh label create "bug" --color "ff0000" --description "Something isn't working"
gh label create "enhancement" --color "84b6eb" --description "New feature or request"
gh label create "documentation" --color "f9d0c4" --description "Improvements or additions to documentation"

# Size labels (for estimation)
gh label create "size-xs" --color "c5def5" --description "Extra small task"
gh label create "size-s" --color "c5def5" --description "Small task"
gh label create "size-m" --color "c5def5" --description "Medium task"
gh label create "size-l" --color "c5def5" --description "Large task"
gh label create "size-xl" --color "c5def5" --description "Extra large task"
```

## Configuration Verification

### Test GitHub CLI Integration
```bash
# List current issues
gh issue list

# Create a test issue
gh issue create --title "Test Issue" --body "Testing GitHub CLI integration" --label "needs-triage"

# View the issue
gh issue list --limit 1

# Close the test issue
gh issue close $(gh issue list --limit 1 --json number --jq '.[0].number')
```

### Verify Repository Settings
```bash
# Check repository info
gh repo view

# Check if issues are enabled
gh api repos/:owner/:repo --jq '.has_issues'

# Check current labels
gh label list
```

## mem8 Integration Configuration

### Set up GitHub organization and repository in mem8 templates:
When running `mem8 init --interactive`, you'll be prompted for:
- GitHub organization/username: `{{cookiecutter.github_org}}`
- GitHub repository name: `{{cookiecutter.github_repo}}`

These will be used throughout the generated templates for consistent GitHub integration.

### Link with mem8 commands:
The repository setup enables:
- `mem8 worktree create` to work with GitHub issue numbers (123)
- `mem8 metadata research` to include GitHub repository context
- GitHub workflow commands to operate on your specific repository

## Troubleshooting

### GitHub CLI Not Found
```bash
# macOS
brew install gh

# Windows
winget install GitHub.cli

# Linux (Ubuntu/Debian)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

### Authentication Issues
```bash
# Clear existing authentication
gh auth logout

# Re-authenticate
gh auth login --hostname github.com --git-protocol https --web
```

### Labels Already Exist
If labels already exist, the `gh label create` commands will fail. You can either:
1. Skip creating existing labels
2. Update existing labels: `gh label edit "needs-triage" --color "d73a4a"`
3. Delete and recreate: `gh label delete "needs-triage" && gh label create "needs-triage" --color "d73a4a"`

## Repository Access Requirements

Ensure you have appropriate permissions:
- **Issues**: Read/Write access to create and manage issues
- **Labels**: Admin or Write access to create labels
- **Pull Requests**: Write access for workflow automation

For organization repositories, you may need to request these permissions from repository administrators.