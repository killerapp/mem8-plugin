# mem8 Official Templates

Official template repository for [mem8](https://github.com/killerapp/mem8) - Memory management CLI for team collaboration.

This repository contains cookiecutter templates that can be used with `mem8 init` to set up Claude Code workspaces with intelligent agents, workflow automation, and shared knowledge repositories.

## 📦 Available Templates

### claude-config
Claude Code workspace integration with agents and workflow commands.

**What's included:**
- 🤖 7 specialized agents (codebase-analyzer, memory-locator, web-search-researcher, etc.)
- 📝 15+ workflow commands (commit, create_plan, describe_pr, etc.)
- 🔧 GitHub/Linear workflow integration
- 🧠 Memory-aware development workflows

### memory-repo
Shared knowledge repository structure for team collaboration.

**What's included:**
- 📁 Organized directory structure for plans, research, decisions
- 🔄 Git-based sync scripts (bash, PowerShell, batch)
- 👥 Multi-user support with personal namespaces
- 🔗 Symbolic link support for shared memory

### full
Complete setup combining both claude-config and memory-repo.

## 🚀 Usage

### Using with mem8 CLI

#### Use as default for all projects
```bash
# Set this repo as your default template source
mem8 templates set-default killerapp/mem8-templates

# Now all init commands use these templates
mem8 init
```

#### One-time use
```bash
# Use for a single init
mem8 init --template-source killerapp/mem8-templates
```

#### Use specific Git ref or branch
```bash
# Use a specific version/tag
mem8 init --template-source killerapp/mem8-templates@v2.10.0

# Use a development branch
mem8 init --template-source killerapp/mem8-templates@feature/new-agents
```

### Validation

Validate this template source before using:

```bash
mem8 templates validate --source killerapp/mem8-templates
```

List available templates:

```bash
mem8 templates list --source killerapp/mem8-templates
```

## 🛠️ Toolbelt Manifest

Workspace templates seed a `.mem8/toolbelt.json` file that lists core, recommended, and optional CLI tools for Windows 11+, macOS, and modern Linux environments. The manifest lets `mem8 doctor` audit local installs without acting as a package manager, so teams can keep requirements centralised while developers install tools by hand. Update the manifest in your fork to publish organisation-specific defaults that every new project inherits.

## 🔧 Customization

### Fork This Repository

1. Fork this repository to customize templates for your organization
2. Modify templates in `claude-dot-md-template/` and `shared-memory-template/`
3. Update `mem8-templates.yaml` manifest with your changes
4. Use your fork:

```bash
mem8 init --template-source YOUR_ORG/mem8-templates
```

### Local Development

Clone and use locally for faster iteration:

```bash
git clone https://github.com/killerapp/mem8-templates.git
cd mem8-templates

# Edit templates...

# Test your changes
mem8 init --template-source ./
```

## 📋 Manifest Format

The `mem8-templates.yaml` manifest describes available templates:

```yaml
version: 1
source: "."  # Relative path to templates directory

templates:
  template-name:
    path: "template-directory"
    type: "cookiecutter"
    description: "Template description"
    variables:
      key: "default value"
```

### Supported Template Types
- `cookiecutter`: Cookiecutter-based templates
- `composite`: Meta-template that uses multiple templates

## 🌐 External Template Sources

mem8 supports multiple source formats:

| Format | Example | Description |
|--------|---------|-------------|
| GitHub shorthand | `org/repo` | Most concise |
| GitHub with ref | `org/repo@v1.0.0` | Specific version |
| GitHub with subdir | `org/repo#subdir=templates` | Templates in subdirectory |
| Git URL | `https://github.com/org/repo.git` | Full Git URL |
| Local path | `/path/to/templates` or `./templates` | Local filesystem |

## 🤝 Contributing

Contributions welcome! Please:

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Test with `mem8 templates validate --source ./`
5. Submit a pull request

## 📄 License

Apache-2.0 - see [LICENSE](LICENSE) for details.

## 🔗 Related

- [mem8](https://github.com/killerapp/mem8) - Main CLI tool
- [Claude Code](https://claude.ai/code) - AI-powered development environment
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) - Template engine

## 💬 Support

- 📖 [Documentation](https://github.com/killerapp/mem8#readme)
- 🐛 [Report Issues](https://github.com/killerapp/mem8/issues)
- 💡 [Feature Requests](https://github.com/killerapp/mem8/issues)
