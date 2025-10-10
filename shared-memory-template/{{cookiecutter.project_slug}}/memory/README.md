# Memory

Organizational memory for {{cookiecutter.project_name}} development context and knowledge.

## Structure

```
memory/
├── plans/          # Implementation plans and architecture docs
├── prs/            # Pull request descriptions and documentation
└── research/       # Research notes and analysis
```

## Usage

This memory directory is designed to work as a git submodule or standalone directory for project knowledge management.

### Adding Content

**Implementation Plans:**
```bash
memory/plans/feature-name.md
```

**Research Documents:**
```bash
memory/research/YYYY-MM-DD_topic.md
```

**PR Descriptions:**
```bash
memory/prs/{number}_description.md
```

## Git Submodule Setup (Recommended)

For shared organizational memory across projects:

```bash
# Remove local memory directory
rm -rf memory

# Add as submodule
git submodule add https://github.com/your-org/memory.git memory

# Initialize
git submodule update --init --recursive
```

## Purpose

- **Shared Knowledge**: Centralize development context
- **Version Control**: Track evolution of plans and decisions
- **Collaboration**: Enable team-wide knowledge sharing
- **AI Context**: Provide searchable context for AI assistants

## Integration

Works seamlessly with:
- Claude Code `.claude` configurations
- mem8 CLI tools
- GitHub PR workflows
- Cross-project knowledge sharing
