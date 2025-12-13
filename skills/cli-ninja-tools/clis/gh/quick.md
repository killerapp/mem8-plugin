# GitHub CLI (gh) Quick Reference

**Check**: `gh --version`
**Install**: `brew install gh` | `apt install gh` | `scoop install gh`
**Auth**: `gh auth login`

## Top 10 Patterns

```bash
# 1. View issue with JSON output
gh issue view 123 --json title,body,state

# 2. Inline jq filtering
gh issue view 123 --json body --jq '.body'

# 3. List issues with labels
gh issue list --label "bug" --json number,title

# 4. Get PR files changed
gh pr view 123 --json files --jq '.files[].path'

# 5. Create PR with body
gh pr create --title "feat: add X" --body "## Summary"

# 6. Check CI status
gh pr checks

# 7. Clone with all branches
gh repo clone owner/repo -- --bare

# 8. View repo info
gh repo view --json name,description,stargazerCount

# 9. Run workflow
gh workflow run deploy.yml

# 10. API direct call
gh api repos/{owner}/{repo}/issues
```

## Essential Flags

| Flag | Purpose |
|------|---------|
| `--json fields` | Request JSON output |
| `--jq expr` | Apply jq filter inline |
| `--web` | Open in browser |
| `-R owner/repo` | Target different repo |

## Powerful: --json + --jq

```bash
# Extract URLs from issue body and comments
gh issue view 123 --json body,comments --jq '
  [.body, .comments[].body] | join("\n") |
  [match("https://[^\\s]+"; "g")] | map(.string) | unique | .[]
'

# Get comment authors
gh issue view 123 --json comments --jq '.comments[].author.login'

# Batch process issues
for issue in 191 239 150; do
  gh issue view $issue --json title --jq '.title'
done
```

## See Also

- [Full reference](reference.md)
- [gh+jq recipes](../../recipes/github/)
