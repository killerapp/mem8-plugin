# Recipe Template

Copy this template when creating new recipes.

---

```markdown
---
name: recipe-name-kebab-case
description: One-line description of what this does
tools: [cli1, cli2]
tags: [category, keyword]
difficulty: beginner|intermediate|advanced
verified: true|false
---

# Recipe Title

## Problem

What problem does this solve? When would you use this?

## Solution

```bash
# Main command pipeline
command1 | command2 | command3
```

## How It Works

1. `command1` - What the first command does
2. `command2` - What gets piped to the second command
3. `command3` - Final transformation

## Variations

### Variation 1: With filtering
```bash
# Modified version for specific use case
```

### Variation 2: Different output
```bash
# Another variation
```

## Common Pitfalls

- **Pitfall 1**: Explanation and how to avoid
- **Pitfall 2**: Another common mistake

## See Also

- [cli1 quick reference](../clis/cli1/quick.md)
- [Related recipe](../recipes/category/related.md)
```

---

## Frontmatter Fields

| Field | Required | Values | Description |
|-------|----------|--------|-------------|
| `name` | Yes | kebab-case | Unique identifier |
| `description` | Yes | string | One-line summary |
| `tools` | Yes | list | CLI tools used |
| `tags` | No | list | Discovery keywords |
| `difficulty` | No | beginner/intermediate/advanced | Complexity level |
| `verified` | No | true/false | Has been tested |

## Guidelines

1. **Keep it terse**: 30-80 lines total
2. **Show the pipeline first**: Users want to copy-paste
3. **Explain each step**: But briefly
4. **Include variations**: Common modifications
5. **Note pitfalls**: Save users debugging time
6. **Cross-reference**: Link to CLI quick refs
