# mem8 Claude Code Plugin

Official Claude Code plugin for [mem8](https://github.com/killerapp/mem8) - memory-augmented development workflows.

## What is mem8?

mem8 enhances Claude Code with persistent memory and structured workflows:

- **8 workflow commands** for planning, research, implementation, and validation
- **6 specialized agents** for codebase analysis and research
- **Persistent memory** across sessions via the `memory/` directory
- **Team distribution** through `.claude/settings.json`

## Installation

### Step 1: Install mem8 CLI (Recommended)

For full functionality including search, sync, and diagnostics:

```bash
# Install with uv (fast, modern Python package manager)
uv tool install mem8
```

:::tip Don't have uv?
Install it first:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
:::

Verify CLI installation:

```bash
mem8 --version
mem8 status
```

### Step 2: Install Plugin

Add mem8 marketplace and install the plugin:

```bash
/plugin marketplace add killerapp/mem8-plugin
/plugin install mem8@mem8-official
```

The `memory/` directory will be created automatically.

### Team Installation

For automatic installation across your team, add to `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "mem8": {
      "source": {
        "source": "github",
        "repo": "killerapp/mem8-plugin"
      }
    }
  },
  "enabledPlugins": ["mem8@mem8-official"]
}
```

When team members trust the repository, mem8 installs automatically.

## Plugin Contents

### Commands (8 total)

```
commands/
├── commit.md         # Create well-structured commits
├── debug.md          # Debug issues with memory context
├── describe-pr.md    # Generate PR descriptions
├── implement.md      # Implement from plans
├── local-review.md   # Set up review environments
├── plan.md          # Create implementation plans
├── research.md      # Research codebase
└── validate.md      # Validate implementations
```

### Agents (6 total)

```
agents/
├── codebase-analyzer.md       # Deep code analysis
├── codebase-locator.md        # Find relevant files
├── codebase-pattern-finder.md # Discover patterns
├── memory-analyzer.md         # Deep memory analysis
├── memory-locator.md          # Find relevant memory
└── web-search-researcher.md   # Web research
```

### Memory Directory Structure

Created automatically during plugin installation:

```
memory/
├── plans/       # Implementation plans and technical designs
├── research/    # Research documents and findings
├── prs/         # Pull request descriptions and reviews
└── docs/        # Documentation and notes
```

## Usage

### Getting Started

```bash
# Research your codebase
/mem8:research

# Create an implementation plan
/mem8:plan

# Implement the plan
/mem8:implement memory/plans/your-plan.md

# Validate implementation
/mem8:validate memory/plans/your-plan.md
```

### Check Status

```bash
# View plugin status and available commands
mem8 status

# Detailed view with paths
mem8 status --detailed
```

## Plugin Architecture

### Manifest Structure

The plugin is defined by:

- `.claude-plugin/plugin.json` - Plugin metadata and configuration
- `.claude-plugin/marketplace.json` - Marketplace catalog definition
- `hooks/hooks.json` - Post-install automation hooks
- `scripts/` - Cross-platform setup scripts

### Post-Install Hooks

The plugin automatically runs:

1. **setup-memory** - Creates `memory/` directory structure
2. **create-plugin-marker** - Creates `.claude/.mem8-plugin` marker for detection

Scripts support Linux/macOS (bash), Windows (batch), and PowerShell.

## Customization

### Fork & Modify

1. Fork this repository
2. Modify commands, agents, or hooks
3. Update `.claude-plugin/plugin.json` version
4. Distribute via your own marketplace:

```bash
/plugin marketplace add YOUR_ORG/mem8-plugin
/plugin install mem8@your-marketplace
```

### Local Development

```bash
git clone https://github.com/killerapp/mem8-plugin.git
cd mem8-plugin

# Test changes locally
/plugin install file://$(pwd)@mem8-official
```

## Requirements

- Claude Code (latest version)
- Git (for memory directory initialization)

## Support

- Documentation: https://github.com/killerapp/mem8
- Issues: https://github.com/killerapp/mem8/issues
- Plugin docs: https://docs.claude.com/docs/claude-code/plugins

## Version

Current version: **3.0.0** (Plugin-based architecture)

## License

MIT License - See LICENSE file for details
