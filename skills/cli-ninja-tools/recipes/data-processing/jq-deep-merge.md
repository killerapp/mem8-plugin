---
name: jq-deep-merge
description: Deep merge multiple JSON files with configurable override behavior
tools: [jq]
tags: [json, merge, config]
difficulty: intermediate
verified: true
---

# Deep Merge JSON Files

## Problem

Need to merge multiple JSON config files where later files override earlier ones (like environment-specific configs).

## Solution

```bash
# Merge two files (second overrides first)
jq -s '.[0] * .[1]' base.json override.json
```

## How It Works

1. `-s` (slurp) - Read all files into array
2. `.[0] * .[1]` - Deep merge using `*` operator
3. Later values override earlier ones recursively

## Variations

### Merge multiple files
```bash
jq -s 'reduce .[] as $item ({}; . * $item)' base.json dev.json local.json
```

### Merge arrays (combine, don't replace)
```bash
jq -s '.[0].items += .[1].items | .[0]' base.json additions.json
```

### Selective merge (only specific keys)
```bash
jq -s '.[0] * (.[1] | {database, cache})' base.json override.json
```

### Merge with null handling
```bash
jq -s '.[0] * (.[1] | del(.. | nulls))' base.json partial.json
```

### Preview differences before merge
```bash
diff <(jq -S '.' base.json) <(jq -S '.' override.json)
```

### Merge and output to file
```bash
jq -s '.[0] * .[1]' base.json override.json > merged.json
```

## Common Pitfalls

- **Array handling**: `*` replaces arrays entirely, doesn't merge elements
- **Null values**: Explicit nulls in override will set to null
- **Order matters**: Last file wins for conflicts

## See Also

- [jq quick reference](../../clis/jq/quick.md)
