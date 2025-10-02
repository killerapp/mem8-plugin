# GitHub Issues - Issue Management

You are tasked with managing GitHub Issues, including creating issues from thoughts documents, updating existing issues, and following GitHub-based workflow patterns.

## Initial Setup

Verify that gh CLI is available:
```bash
gh --version
```

If not available, respond:
```
I need the GitHub CLI (gh) to help with issue management. Please install it:
- macOS: `brew install gh` 
- Windows: `winget install GitHub.cli`
- Linux: See https://cli.github.com/

Then authenticate with: `gh auth login`
```

## Workflow Labels

This command uses GitHub labels to represent workflow stages:
- `needs-triage` - Initial review needed
- `needs-research` - Investigation required
- `ready-for-plan` - Research complete, needs implementation plan
- `ready-for-dev` - Plan approved, ready for development
- `in-development` - Active development
- `ready-for-review` - PR submitted

## Action-Specific Instructions

### Creating Issues from Thoughts

1. **Locate and read the thoughts document**
2. **Analyze the document content** for core problem and implementation details
3. **Draft the issue summary** with clear title and description
4. **Create GitHub issue**:
   ```bash
   gh issue create --title "Title" --body "Description" --label "needs-triage"
   ```
5. **Update thoughts document** with issue reference

### Managing Issue Workflow

Update issue labels to represent workflow progression:
```bash
gh issue edit ISSUE_NUMBER --add-label "ready-for-dev" --remove-label "ready-for-plan"
```

Default to "needs-triage" for new issues and progress through workflow as appropriate.

### Common Commands

**List issues by label:**
```bash
gh issue list --label "needs-research" --limit 10
```

**View issue details:**
```bash
gh issue view ISSUE_NUMBER
```

**Add comment to issue:**
```bash
gh issue comment ISSUE_NUMBER --body "Comment text"
```

**Close issue:**
```bash
gh issue close ISSUE_NUMBER
```

## GitHub Issues Philosophy

GitHub Issues focus on simplicity:
- Use **labels** for status and categorization
- Use **milestones** for project organization
- Use **assignees** for responsibility
- Focus on **transparency** and ease of use

This makes GitHub Issues more accessible and easier to use for most teams.