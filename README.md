# mem8 Official Templates

Official cookiecutter templates for [mem8](https://github.com/killerapp/mem8).

## Installation

```bash
uv tool install mem8
```

## Templates

### claude-config
`.claude/` workspace with agents and commands.

```
.claude/
├── agents/          # 7 specialized agents
│   ├── codebase-analyzer.md
│   ├── codebase-locator.md
│   ├── codebase-pattern-finder.md
│   ├── memory-analyzer.md
│   ├── memory-locator.md
│   └── web-search-researcher.md
└── commands/        # 8 workflow commands
    ├── m8-commit.md
    ├── m8-debug.md
    ├── m8-describe-pr.md
    ├── m8-implement.md
    ├── m8-local-review.md
    ├── m8-plan.md
    ├── m8-research.md
    └── m8-validate.md
```

### memory-repo
Shared knowledge repository structure.

```
memory/
├── shared/          # Team documents
│   ├── plans/
│   ├── research/
│   ├── prs/
│   └── decisions/
├── {username}/      # Personal space
└── searchable/      # Unified search via symlinks
```

### full
Both claude-config + memory-repo combined.

## Usage

### Set Default

```bash
mem8 templates set-default killerapp/mem8-templates
mem8 init
```

### One-Time Use

```bash
mem8 init --template-source killerapp/mem8-templates
```

### Specific Version

```bash
mem8 init --template-source killerapp/mem8-templates@v2.10.0
```

### Validation

```bash
# Validate before use
mem8 templates validate --source killerapp/mem8-templates

# List templates
mem8 templates list --source killerapp/mem8-templates
```

## Customization

### Fork & Modify

```bash
# Use your fork
mem8 init --template-source YOUR_ORG/mem8-templates
```

### Local Development

```bash
git clone https://github.com/killerapp/mem8-templates.git
cd mem8-templates
# Edit templates...
mem8 init --template-source ./
```

## Template Sources

| Format | Example |
|--------|---------|
| GitHub shorthand | `org/repo` |
| With version | `org/repo@v1.0.0` |
| With subdirectory | `org/repo#subdir=templates` |
| Git URL | `https://github.com/org/repo.git` |
| Local path | `/path/to/templates` or `./templates` |

## Manifest Format

`manifest.yaml` describes available templates:

```yaml
version: 1
source: "."

templates:
  template-name:
    path: "template-directory"
    type: "cookiecutter"  # or "composite"
    description: "Template description"
    variables:
      key: "default value"
```

## Toolbelt

Templates include `.mem8/toolbelt.json` listing core/recommended CLI tools. `mem8 doctor` audits installs without acting as package manager. Fork to publish org-specific defaults.
