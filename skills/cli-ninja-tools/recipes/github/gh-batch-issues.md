---
name: gh-batch-issues
description: Process multiple GitHub issues in batch with structured output
tools: [gh, jq]
tags: [github, batch, automation]
difficulty: intermediate
verified: true
---

# Batch Process GitHub Issues

## Problem

Need to extract information from multiple issues at once for reporting or analysis.

## Solution

```bash
# Get title and state for multiple issues
for issue in 191 239 150; do
  gh issue view $issue --json number,title,state --jq '"\(.number): \(.title) [\(.state)]"'
done
```

## How It Works

1. `for issue in ...` - Loop through issue numbers
2. `gh issue view $issue` - Fetch each issue
3. `--json number,title,state` - Request specific fields
4. `--jq` - Format inline

## Variations

### Export to JSON array
```bash
(
  echo "["
  for issue in 191 239 150; do
    gh issue view $issue --json number,title,state,labels
    echo ","
  done | sed '$ s/,$//'
  echo "]"
) | jq -s 'flatten'
```

### Get all issues with specific label
```bash
gh issue list --label "bug" --json number --jq '.[].number' | \
  while read num; do
    gh issue view $num --json title,assignees --jq '"\(.title) -> \(.assignees[].login // "unassigned")"'
  done
```

### Summarize labels across issues
```bash
gh issue list --limit 100 --json labels --jq '
  [.[].labels[].name] | group_by(.) |
  map({label: .[0], count: length}) | sort_by(-.count)
'
```

### Find issues without assignees
```bash
gh issue list --json number,title,assignees --jq '
  .[] | select(.assignees | length == 0) | "\(.number): \(.title)"
'
```

### Export issues to CSV
```bash
gh issue list --limit 50 --json number,title,state,createdAt --jq -r '
  .[] | [.number, .state, .createdAt, .title] | @csv
' > issues.csv
```

## Common Pitfalls

- **Rate limiting**: Add `sleep 0.5` for large batches
- **Pagination**: `gh issue list` returns 30 by default, use `--limit`
- **Empty arrays**: Use `// "none"` for fallback values

## See Also

- [gh quick reference](../../clis/gh/quick.md)
- [gh-extract-issue-urls](gh-extract-issue-urls.md)
