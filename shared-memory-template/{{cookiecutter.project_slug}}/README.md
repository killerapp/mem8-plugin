# {{cookiecutter.project_name}}

Shared memory repository for AI-assisted development and knowledge management.

## Structure

```
memory/
├── shared/                    # Team-wide documents
│   ├── plans/                # Implementation plans
│   ├── research/             # Research documents  
│   ├── tickets/              # GitHub issues (123.md)
│   ├── prs/                  # PR descriptions
│   └── decisions/            # Technical decisions
├── {{cookiecutter.username}}/                  # Personal memory
│   ├── tickets/              # Personal ticket copies
│   ├── notes/               # Personal notes
│   └── archive/             # Archived memory
├── global/                   # Cross-repository memory
│   └── shared/              # Global shared patterns
└── searchable/              # Unified search directory
    ├── shared/ -> ../shared/
    ├── {{cookiecutter.username}}/ -> ../{{cookiecutter.username}}/
    └── global/ -> ../global/
```

## Usage

### Creating Documents

**Research Documents:**
```bash
# Timestamped research files
memory/shared/research/YYYY-MM-DD_HH-MM-SS_topic.md
```

**Implementation Plans:**
```bash
# Descriptive plan names
memory/shared/plans/fix-authentication-flow.md
```

**Ticket References:**
```bash
# GitHub issue format
memory/shared/tickets/123.md
```

### Syncing Changes

{% if cookiecutter.include_sync_scripts %}
Use the provided sync scripts:
```bash
# Windows
./sync-memory.bat

# Unix/Linux
./sync-memory.sh
```
{% endif %}

Or manually with git:
```bash
git add memory/
git commit -m "Update memory: brief description"
git push origin main
```

## Integration

This memory directory integrates with:
- Claude Code `.claude` configurations
- GitHub issue tracking and PR workflows
- Cross-project knowledge sharing

## File Naming Conventions

- **Research**: `YYYY-MM-DD_HH-MM-SS_topic.md`
- **Plans**: `descriptive-name.md`
- **Tickets**: `123.md` (GitHub issue format)
- **PRs**: `{number}_description.md`
- **Notes**: Free-form naming

## Repository Integration

- **GitHub URL**: {{cookiecutter.shared_repo_url}}
- **Project Root**: {{cookiecutter.project_root}}
- **Username**: {{cookiecutter.username}}

## Searchable Directory

The `searchable/` directory contains links to all content for unified searching:
- Use grep, ripgrep, or IDE search across `searchable/`
- Always reference actual paths in documentation: `memory/shared/...`
- Links are maintained automatically