# Recipe Index

Multi-CLI combinations for common workflows. Each recipe uses 2+ tools together.

## Categories

### GitHub (`github/`)
| Recipe | CLIs | Purpose |
|--------|------|---------|
| [gh-extract-issue-urls](github/gh-extract-issue-urls.md) | gh, jq | Extract URLs from issues/comments |
| [gh-pr-files-changed](github/gh-pr-files-changed.md) | gh, jq | List files changed in PR |
| [gh-batch-issues](github/gh-batch-issues.md) | gh, jq | Process multiple issues |

### Data Processing (`data-processing/`)
| Recipe | CLIs | Purpose |
|--------|------|---------|
| [jq-deep-merge](data-processing/jq-deep-merge.md) | jq | Merge JSON files with override |
| [rg-json-output](data-processing/rg-json-output.md) | rg, jq | Search results as structured data |

### Code Analysis (`code-analysis/`)
| Recipe | CLIs | Purpose |
|--------|------|---------|
| [rg-todo-report](code-analysis/rg-todo-report.md) | rg, jq | TODO/FIXME summary |

### DevOps (`devops/`)
| Recipe | CLIs | Purpose |
|--------|------|---------|
| [docker-cleanup-all](devops/docker-cleanup-all.md) | docker | Clean all Docker resources |
| [docker-stats-json](devops/docker-stats-json.md) | docker, jq | Container stats as JSON |

### Media (`media/`)
| Recipe | CLIs | Purpose |
|--------|------|---------|
| [ffmpeg-compress-video](media/ffmpeg-compress-video.md) | ffmpeg | Compress video for web |
| [ffmpeg-extract-thumbnail](media/ffmpeg-extract-thumbnail.md) | ffmpeg | Extract frame as thumbnail |

## Using Recipes

1. Check prerequisites: each recipe lists required CLIs
2. Copy the command pipeline
3. Adapt to your use case
4. Consider adding variations to your project's CLAUDE.md

## Contributing

Found a useful CLI combination? See [CONTRIBUTING.md](CONTRIBUTING.md) to add it.
