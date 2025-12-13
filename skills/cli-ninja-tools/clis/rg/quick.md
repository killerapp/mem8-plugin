# ripgrep (rg) Quick Reference

**Check**: `rg --version`
**Install**: `brew install ripgrep` | `apt install ripgrep` | `scoop install ripgrep`

## Top 10 Patterns

```bash
# 1. Basic search with context
rg 'pattern' -A 3 -B 1

# 2. Search specific file types
rg 'import.*React' --type ts

# 3. Exclude directories
rg 'TODO' --glob '!node_modules' --glob '!dist'

# 4. Find function definitions
rg '^(export\s+)?(async\s+)?function\s+\w+' --type js

# 5. Count matches per file
rg 'console\.log' --count --type js

# 6. List only filenames
rg -l 'deprecated' --type py

# 7. Case insensitive
rg -i 'error'

# 8. Fixed string (no regex)
rg -F 'user.name'

# 9. JSON output for processing
rg 'TODO' --json | jq 'select(.type == "match")'

# 10. Multiline search
rg -U 'class \w+.*\n.*constructor' --type ts
```

## Essential Flags

| Flag | Purpose |
|------|---------|
| `-A N` | N lines after match |
| `-B N` | N lines before match |
| `-C N` | N lines context (both) |
| `-l` | Files with matches only |
| `-c` | Count matches |
| `-i` | Case insensitive |
| `-F` | Fixed string (literal) |
| `-U` | Multiline mode |
| `--type X` | File type filter |
| `--json` | JSON output |

## Search and Replace

```bash
# Preview changes
rg 'oldName' -l | xargs -I {} sh -c 'echo "=== {} ===" && sd -p "oldName" "newName" {}'

# Apply changes
rg 'oldName' -l | xargs sd -i 'oldName' 'newName'
```

## See Also

- [Full reference](reference.md)
- [rg+jq recipes](../../recipes/data-processing/)
