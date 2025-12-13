# Contributing Recipes

How to add new CLI recipes to the cli-ninja-tools skill.

## Quick Contribution

1. Create recipe following [TEMPLATE.md](TEMPLATE.md)
2. Place in appropriate category directory
3. Update `_index.md` with new entry
4. Submit PR to mem8-plugin

## Quality Checklist

Before submitting:

- [ ] Recipe uses 2+ CLI tools together
- [ ] Commands tested and working
- [ ] All template sections filled
- [ ] Frontmatter complete (name, description, tools)
- [ ] File named with kebab-case: `action-description.md`
- [ ] Added to `_index.md`

## Recipe Categories

| Category | Directory | Examples |
|----------|-----------|----------|
| GitHub workflows | `github/` | gh + jq patterns |
| Data transformation | `data-processing/` | jq, yq, csv tools |
| Code analysis | `code-analysis/` | rg, ast-grep patterns |
| DevOps/containers | `devops/` | docker, kubectl |
| Media processing | `media/` | ffmpeg, imagemagick |

## What Makes a Good Recipe

**Good**:
- Solves a real problem
- Combines tools in non-obvious way
- Token-efficient (short but complete)
- Tested on real data

**Avoid**:
- Single-tool patterns (those go in `clis/*/quick.md`)
- Overly specific to one project
- Long explanations (keep it terse)
- Untested commands

## Local Development

Add personal recipes to:
```
~/.claude/skills/cli-ninja-local/recipes/
```

These won't be submitted upstream but extend your skill locally.

## Validation

Before PR, validate format:
```bash
python scripts/validate.py recipes/category/your-recipe.md
```

## Example PR

```
feat(recipes): add gh-extract-issue-urls recipe

- Extracts URLs from GitHub issue body and comments
- Uses gh + jq for token-efficient API access
- Includes variations for filtering specific domains

Tested on: Ubuntu 24.04, macOS
```
