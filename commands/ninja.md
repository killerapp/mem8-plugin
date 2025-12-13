---
allowed-tools: Read, Write, Bash, Task, WebSearch
description: CLI tool workflows - discovery, documentation, and recipe creation
argument-hint: [init|document|recommend|create-recipe]
---

# CLI Ninja Workflows

CLI tool discovery, documentation, and recipe creation. Access the cli-ninja-tools skill.

## Usage

```
/ninja init          - Scan project, recommend CLI patterns
/ninja document      - Document a CLI tool or recipe you discovered
/ninja recommend     - Analyze codebase for CLI tool opportunities
/ninja create-recipe - Deep-dive 2+ CLIs to create new recipes
```

## Mode: init

Scan project and recommend relevant CLI patterns.

**Steps**:
1. Run `python3 skills/cli-ninja-tools/scripts/scan.py --json`
2. Run `python3 skills/cli-ninja-tools/scripts/discover.py --missing --tier 1`
3. Load relevant recipes from `skills/cli-ninja-tools/recipes/`
4. Present recommendations with platform-specific install commands
5. Offer to add "## CLI Tricks" section to CLAUDE.md

## Mode: document

Help document a CLI tool or multi-tool recipe.

**If documenting a single CLI**:
1. Run `{cli} --help` to understand capabilities
2. Check if `skills/cli-ninja-tools/clis/{cli}/quick.md` exists
3. Create or extend following the template
4. Offer to save to skill or project CLAUDE.md

**If documenting a recipe (2+ CLIs)**:
1. Capture the command pipeline
2. Decompose each component
3. Generate recipe following `skills/cli-ninja-tools/recipes/TEMPLATE.md`
4. Validate: `python3 skills/cli-ninja-tools/scripts/validate.py recipe.md`
5. Save to appropriate category in `skills/cli-ninja-tools/recipes/`

## Mode: recommend

Analyze codebase and recommend CLI tools.

**Steps**:
1. Run `python3 skills/cli-ninja-tools/scripts/discover.py --json`
2. Run `python3 skills/cli-ninja-tools/scripts/scan.py --json`
3. Read `skills/cli-ninja-tools/clis/_index.md` for tool repertoire
4. Correlate project patterns with available recipes
5. Generate prioritized recommendations

## Mode: create-recipe

Deep-dive into 2+ CLIs to discover powerful combinations.

**Dispatch the recipe-creator agent**:

Use Task tool with `mem8:recipe-creator` subagent:
- Provide the CLI tools to explore
- Optionally specify a use case or existing recipe to extend
- Agent will deep-dive each CLI and propose new recipes

**Example**:
```
Explore how gh, jq, and rg can work together for GitHub issue management
```

## Skill Reference

The cli-ninja-tools skill contains:
- `clis/` - Per-CLI documentation (jq, rg, fd, gh, ffmpeg, ast-grep)
- `recipes/` - Multi-CLI combinations by category
- `scripts/` - discover.py, scan.py, validate.py

## Quick Access

```bash
# Check what tools are installed
python3 skills/cli-ninja-tools/scripts/discover.py --tier 1

# Scan project for CLI usage
python3 skills/cli-ninja-tools/scripts/scan.py

# Validate a recipe
python3 skills/cli-ninja-tools/scripts/validate.py recipes/github/my-recipe.md
```
