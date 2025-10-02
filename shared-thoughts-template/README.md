# Shared Thoughts Template

Cookiecutter template for creating a shared thoughts repository structure based on patterns found in AI-assisted development workflows.

## Quick Start

```bash
# Install cookiecutter if needed
uv tool install cookiecutter

# Generate with default configuration
cookiecutter shared-thoughts-template --config-file thoughts-config-default.yaml

# Interactive mode
cookiecutter shared-thoughts-template
```

## Features

- **Structured thoughts directory** with shared, personal, and global sections
- **Searchable directory** with automatic symlinks/junctions for unified searching
- **Git integration** with automatic repository initialization
- **Cross-platform sync scripts** (Windows .bat, Unix .sh, PowerShell .ps1)
- **Configurable options** for different team setups

## Generated Structure

```
thoughts/
├── shared/                    # Team-wide documents
│   ├── plans/                # Implementation plans
│   ├── research/             # Research documents  
│   ├── tickets/              # GitHub issues (123.md)
│   ├── prs/                  # PR descriptions
│   └── decisions/            # Technical decisions
├── {username}/               # Personal thoughts (configurable)
│   ├── tickets/              # Personal ticket copies
│   ├── notes/               # Personal notes
│   └── archive/             # Archived thoughts
├── global/                   # Cross-repository thoughts
│   └── shared/              # Global shared patterns
└── searchable/              # Unified search directory
    ├── shared/ -> ../shared/
    ├── {username}/ -> ../{username}/
    └── global/ -> ../global/
```

## Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `project_name` | Shared Thoughts Repository | Display name |
| `project_slug` | thoughts | Directory name |
| `username` | vaski | Personal directory name |
| `github_org` | your-org | GitHub organization |
| `github_repo` | thoughts | Repository name |
| `project_root` | C:/Users/vaski/projects | Base project directory |
| `include_searchable_links` | true | Create searchable symlinks |
| `sync_method` | git | Sync mechanism |
| `include_sync_scripts` | true | Generate sync scripts |

## Usage Examples

### With Configuration File
```bash
cookiecutter shared-thoughts-template --config-file thoughts-config-default.yaml --output-dir ~/projects
```

### Custom Configuration
```bash
cookiecutter shared-thoughts-template \
  --no-input \
  username=alice \
  github_org=mycompany \
  project_root=/home/alice/projects
```

## Integration with Claude Code

This template is designed to work with the `claude-dot-md-template` and follows the patterns referenced in:

- **thoughts-locator** agent - for finding documents
- **thoughts-analyzer** agent - for analyzing content  
- Various commands that reference `thoughts/shared/`, `thoughts/{user}/`, etc.

## Sync Scripts

The generated repository includes three sync scripts:

- `sync-thoughts.bat` - Windows batch script
- `sync-thoughts.sh` - Unix/Linux shell script  
- `sync-thoughts.ps1` - PowerShell script

All scripts:
- Add changes from the `thoughts/` directory
- Prompt for commit message (with default)
- Commit and push to remote if configured
- Show status after sync

## File Naming Conventions

- **Research**: `YYYY-MM-DD_HH-MM-SS_topic.md`
- **Plans**: `descriptive-name.md`
- **Tickets**: `123.md` (GitHub issue format)
- **PRs**: `{number}_description.md`

## Searchable Directory

The `searchable/` directory uses:
- **Symlinks** on Unix/Linux systems
- **Directory junctions** on Windows (requires appropriate permissions)

This allows unified searching across all thought categories while maintaining the organized structure.

## Post-Generation Setup

The template automatically:
1. Creates directory structure with proper `.gitkeep` files
2. Sets up searchable directory links/junctions
3. Initializes git repository
4. Creates initial commit
5. Configures remote if URL provided

## Requirements

- **cookiecutter** - Template engine
- **git** - Version control (optional)
- **Windows**: Administrator privileges may be needed for directory junctions
- **Unix/Linux**: Standard symlink permissions