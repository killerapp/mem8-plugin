# fd Quick Reference

**Check**: `fd --version`
**Install**: `brew install fd` | `apt install fd-find` | `scoop install fd`

Note: On Debian/Ubuntu, the binary is `fdfind`. Create symlink: `sudo ln -sf $(which fdfind) /usr/local/bin/fd`

## Top 10 Patterns

```bash
# 1. Find by extension
fd -e ts -e tsx

# 2. Find specific filename
fd -g 'package.json'

# 3. Find with regex
fd '.*\.test\.(js|ts)$'

# 4. Find and execute command
fd -e py -x black {}

# 5. Delete matching files
fd -e pyc -x rm {}

# 6. Exclude directory
fd 'test' --exclude node_modules

# 7. Find large files (>10MB)
fd --size +10m

# 8. Find recently modified (last 24h)
fd --changed-within 24h

# 9. Find empty directories
fd --type d --empty

# 10. Find hidden files too
fd -H 'config'
```

## Essential Flags

| Flag | Purpose |
|------|---------|
| `-e ext` | Filter by extension |
| `-g pattern` | Glob pattern |
| `-t f/d` | Type: file or directory |
| `-x cmd` | Execute command |
| `-H` | Include hidden |
| `-I` | No ignore (.gitignore) |
| `--exclude` | Exclude pattern |
| `--size +/-N` | Size filter |
| `--changed-within` | Time filter |

## Find and Process

```bash
# Format all Python files
fd -e py -x black {}

# Run tests on changed files
fd -e test.ts --changed-within 1h -x npx jest {}

# Count lines in all JS files
fd -e js -x wc -l {} | awk '{sum+=$1} END {print sum}'
```

## See Also

- [Full reference](reference.md)
