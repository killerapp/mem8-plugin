---
name: gh-extract-issue-urls
description: Extract all URLs from GitHub issue body and comments
tools: [gh, jq]
tags: [github, url-extraction, api]
difficulty: intermediate
verified: true
---

# Extract URLs from GitHub Issues

## Problem

Need to extract all URLs (screenshots, videos, links) from a GitHub issue including all comments for review or processing.

## Solution

```bash
# Basic: Get all URLs from issue body and comments
gh issue view 123 --json body,comments --jq '
  [.body, .comments[].body] | join("\n") |
  [match("https://[^\\s\"<>]+"; "g")] | map(.string) | unique | .[]
'
```

## How It Works

1. `--json body,comments` - Request structured JSON with body and all comments
2. `--jq` - Apply jq filter inline (no pipe needed, more efficient)
3. `join("\n")` - Combine body and all comment bodies into single string
4. `match(pattern; "g")` - Find all regex matches globally
5. `unique | .[]` - Deduplicate and output one per line

## Variations

### Filter specific domains (screenshots, videos)
```bash
gh issue view 123 --json body,comments --jq '
  [.body, .comments[].body] | join("\n") |
  [match("https://(prnt\\.sc|screenrec\\.com|www\\.loom\\.com)/[A-Za-z0-9_/-]+"; "g")] |
  map(.string) | unique | .[]
'
```

### With author attribution
```bash
gh issue view 123 --json comments --jq '
  .comments[] | {author: .author.login, urls: [.body | match("https://[^\\s]+"; "g")] | map(.string)}
'
```

### Batch multiple issues
```bash
for issue in 191 239 150; do
  echo "=== Issue #$issue ==="
  gh issue view $issue --json body,comments --jq '
    [.body, .comments[].body] | join("\n") |
    [match("https://[^\\s]+"; "g")] | map(.string) | unique | .[]
  '
done
```

## Common Pitfalls

- **Escaping in jq**: Double-escape backslashes (`\\s` not `\s`)
- **Empty results**: Issue might have no URLs - handle with `// empty`
- **Rate limiting**: For many issues, add `sleep 0.5` between calls

## See Also

- [gh quick reference](../../clis/gh/quick.md)
- [jq quick reference](../../clis/jq/quick.md)
