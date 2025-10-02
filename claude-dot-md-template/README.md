# Claude AI Memory Template

Cookiecutter template for generating `.claude` directory configurations.

## Quick Start

```bash
# Install cookiecutter
uv tool install cookiecutter

# Generate with defaults
cookiecutter claude-dot-md-template --output-dir out

# Interactive mode
cookiecutter claude-dot-md-template
```

## Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `project_name` | Claude AI Memory | Display name for the configuration |
| `project_slug` | .claude | Output directory name |
| `include_agents` | true | Include agent definitions |
| `include_commands` | true | Include command definitions |
| `workflow_provider` | github | Workflow provider (github, linear, none) |
| `include_workflow_automation` | standard | Workflow automation level (standard, advanced, none) |
| `include_web_search` | true | Include web search researcher agent |
| `default_tools` | Read, Grep, Glob, LS | Default tools for agents |
| `repository_path` | /shared/ | Path for shared repository data |

## Generated Structure

```
.claude/
├── agents/
│   ├── codebase-analyzer.md      # Analyzes implementation details
│   ├── codebase-locator.md       # Finds files and components
│   ├── github-workflow-agent.md  # GitHub workflow automation (optional)
│   └── web-search-researcher.md  # Web research specialist (optional)
└── commands/
    ├── commit.md                  # Git commit workflow
    ├── create_plan.md            # Implementation planning
    ├── github_issues.md          # GitHub Issues management (optional)
    └── workflow_automation.md    # Workflow automation (optional)
```

## Customization

### Command Line Options
```bash
# Configure with Linear workflow provider and no automation
cookiecutter claude-dot-md-template \
  --no-input \
  --output-dir my-config \
  -f workflow_provider=linear \
  -f include_workflow_automation=none
```

### Post-Generation
The template includes a post-generation hook that:
- Removes optional files based on configuration
- Cleans up empty directories
- Validates the generated structure

## Adding New Templates

1. Add markdown files to `{{cookiecutter.project_slug}}/agents/` or `/commands/`
2. Use Jinja2 variables: `{{ cookiecutter.variable_name }}`
3. Wrap optional content in `{% if cookiecutter.condition %}`
4. Update `hooks/post_gen_project.py` for conditional file removal