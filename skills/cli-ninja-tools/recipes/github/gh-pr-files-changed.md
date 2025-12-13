---
name: gh-pr-files-changed
description: List files changed in a pull request with filtering options
tools: [gh, jq]
tags: [github, pr, code-review]
difficulty: beginner
verified: true
---

# List PR Files Changed

## Problem

Need to see which files were modified in a PR for code review or to understand scope of changes.

## Solution

```bash
# List all files changed in PR
gh pr view 123 --json files --jq '.files[].path'
```

## How It Works

1. `gh pr view 123` - Get PR details
2. `--json files` - Request only the files field
3. `--jq '.files[].path'` - Extract just the file paths

## Variations

### With change type (added/modified/deleted)
```bash
gh pr view 123 --json files --jq '.files[] | "\(.status)\t\(.path)"'
```

### Filter by extension
```bash
gh pr view 123 --json files --jq '.files[].path | select(endswith(".ts"))'
```

### Count files by directory
```bash
gh pr view 123 --json files --jq '
  [.files[].path | split("/")[0]] | group_by(.) |
  map({dir: .[0], count: length}) | sort_by(-.count)
'
```

### Get additions/deletions per file
```bash
gh pr view 123 --json files --jq '
  .files[] | "\(.additions)+/\(.deletions)- \(.path)"
'
```

### Only files with significant changes (>50 lines)
```bash
gh pr view 123 --json files --jq '
  .files[] | select(.additions + .deletions > 50) | .path
'
```

## Common Pitfalls

- **Large PRs**: GitHub API may truncate files list for very large PRs
- **Renamed files**: Check `.previousFilename` for moved files

## See Also

- [gh quick reference](../../clis/gh/quick.md)
- [jq quick reference](../../clis/jq/quick.md)
