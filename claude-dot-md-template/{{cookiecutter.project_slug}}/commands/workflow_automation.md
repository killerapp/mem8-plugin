# Workflow Automation - GitHub Issues

Workflow automation for GitHub Issues using gh CLI.

## Overview

This command provides GitHub Issues workflow automation using labels and the gh CLI. GitHub Issues focus on simplicity and flexibility, making them accessible for most teams.

## Basic Workflow Commands

### Research Issues
Find and work on issues labeled `needs-research`:
```bash
gh issue list --label "needs-research" --limit 10
```

### Plan Issues  
Find and work on issues labeled `ready-for-plan`:
```bash
gh issue list --label "ready-for-plan" --limit 10
```

### Implementation Issues
Find and work on issues labeled `ready-for-dev`:  
```bash
gh issue list --label "ready-for-dev" --limit 10
```

### Review Issues
Find issues ready for review:
```bash
gh issue list --label "ready-for-review" --limit 10
```

## Workflow Progression

**Basic progression:**
1. `needs-triage` → Initial issue review
2. `needs-research` → Investigation required
3. `ready-for-plan` → Research done, needs implementation plan
4. `ready-for-dev` → Plan approved, ready for development
5. `in-development` → Active development work
6. `ready-for-review` → Code review needed

**Move issue through workflow:**
```bash
# Move from research to planning
gh issue edit ISSUE_NUMBER --remove-label "needs-research" --add-label "ready-for-plan"

# Move from planning to development
gh issue edit ISSUE_NUMBER --remove-label "ready-for-plan" --add-label "ready-for-dev"

# Start development
gh issue edit ISSUE_NUMBER --remove-label "ready-for-dev" --add-label "in-development"
```

## Issue Creation from Thoughts

**Create issue from thoughts document:**
1. Read the thoughts document thoroughly
2. Extract core problem and solution approach
3. Create issue with appropriate label:

```bash
gh issue create \
  --title "Implement feature X based on research" \
  --body "$(cat thoughts/shared/research/feature-x.md)" \
  --label "ready-for-dev"
```

## Integration with mem8 Commands

**Create worktree for issue:**
```bash
# Get issue number from GitHub
ISSUE_NUM=$(gh issue list --label "in-development" --assignee @me --json number --jq '.[0].number')

# Create worktree using mem8
mem8 worktree create #$ISSUE_NUM feature-branch-name
```

**Generate research metadata:**
```bash
mem8 metadata research "Issue 123: Feature X research"
```

## Simple Automation Examples

**Auto-assign based on labels:**
```bash
# Assign research issues to yourself
for issue in $(gh issue list --label "needs-research" --json number --jq '.[].number'); do
  gh issue edit $issue --add-assignee @me
done
```

**Daily workflow check:**
```bash
echo "=== Your assigned issues ==="
gh issue list --assignee @me

echo "=== Issues ready for review ==="
gh issue list --label "ready-for-review"
```

## Philosophy

GitHub Issues workflow automation focuses on:

- **Label-based states** for clear status progression
- **Simple CLI commands** via gh CLI
- **Transparency** - everyone can see and understand labels
- **Flexibility** - teams can adapt labels to their needs
- **Low barrier to entry** - no special training needed

This approach is sustainable and accessible for most development teams.