---
allowed-tools: Bash(mem8:*), Bash(git:*), Bash(mkdir:*), Bash(uv:*) 
argument-hint: [--repos repo1,repo2] [--web]
description: Set up AI memory management with multi-repo discovery
---

# AI Memory Setup

Set up mem8 memory management for this project and discover related repositories.

## Setup Process

1. Check if mem8 is installed:
!`which mem8 || echo "mem8 not found - install with: uv tool install mem8"`

2. Run quick setup:
!`mem8 quick-start $ARGUMENTS`

3. Verify setup:
!`mem8 status`

## Next Steps

- Use `mem8 search "query"` to find thoughts across repositories
- Launch web UI with `mem8 quick-start --web` for visual exploration
- Sync thoughts across team with `mem8 sync`
- Use `mem8 dashboard` to open the web interface anytime