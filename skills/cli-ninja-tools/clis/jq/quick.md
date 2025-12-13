# jq Quick Reference

**Check**: `jq --version`
**Install**: `brew install jq` | `apt install jq` | `scoop install jq`

## Top 10 Patterns

```bash
# 1. Extract nested field
jq '.data[].name' response.json

# 2. Filter by condition
jq '.items[] | select(.status == "active")' data.json

# 3. Reshape structure
jq '{users: [.data[] | {id, name}]}' response.json

# 4. Convert to CSV
jq -r '.users[] | [.id, .name, .email] | @csv' users.json

# 5. Merge two files (second wins)
jq -s '.[0] * .[1]' base.json override.json

# 6. Sum values
jq '[.items[].amount] | add' ledger.json

# 7. Get unique values
jq '[.tags[]] | unique' posts.json

# 8. Group and count
jq 'group_by(.category) | map({cat: .[0].category, n: length})' items.json

# 9. Fallback for missing field
jq '.config.timeout // 30' config.json

# 10. Compact output (no whitespace)
jq -c '.' file.json
```

## Essential Flags

| Flag | Purpose |
|------|---------|
| `-r` | Raw output (no quotes) |
| `-c` | Compact (one line) |
| `-s` | Slurp (array of inputs) |
| `-e` | Exit 1 if output is null/false |

## Combining with Other Tools

```bash
# curl + jq: API response processing
curl -s api.example.com/users | jq '.data[].name'

# rg + jq: Search results as JSON
rg 'TODO' --json | jq 'select(.type == "match")'

# gh + jq: GitHub API filtering
gh issue view 123 --json body --jq '.body'
```

## See Also

- [Full reference](reference.md)
- [gh+jq recipes](../../recipes/github/)
