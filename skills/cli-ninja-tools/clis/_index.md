# CLI Reference Index

Quick reference for CLI power tools organized by tier.

## Tier 1: Essential (Install First)

Maximum AI productivity boost. Install all 5.

| CLI | Command | Check | Purpose | Quick Ref |
|-----|---------|-------|---------|-----------|
| jq | `jq` | `jq --version` | JSON processing | [quick](jq/quick.md) |
| ripgrep | `rg` | `rg --version` | Fast code search | [quick](rg/quick.md) |
| fd | `fd` | `fd --version` | File finder | [quick](fd/quick.md) |
| bat | `bat` | `bat --version` | Cat + syntax highlighting | - |
| ast-grep | `sg` | `sg --version` | AST-based refactoring | [quick](ast-grep/quick.md) |

```bash
# Check all Tier 1
for cmd in jq rg fd bat sg; do command -v $cmd &>/dev/null && echo "OK $cmd" || echo "MISSING $cmd"; done
```

## Tier 2: High Value

| CLI | Command | Check | Purpose | Quick Ref |
|-----|---------|-------|---------|-----------|
| yq | `yq` | `yq --version` | YAML processing | - |
| gh | `gh` | `gh --version` | GitHub CLI | [quick](gh/quick.md) |
| sd | `sd` | `sd --version` | Text replacement | - |
| fzf | `fzf` | `fzf --version` | Fuzzy finder | - |
| delta | `delta` | `delta --version` | Better git diffs | - |

## Tier 3: Specialized

| CLI | Command | Purpose | Quick Ref |
|-----|---------|---------|-----------|
| ffmpeg | `ffmpeg` | Media processing | [quick](ffmpeg/quick.md) |
| httpie | `http` | HTTP client | - |
| tokei | `tokei` | Code stats | - |
| hyperfine | `hyperfine` | Benchmarking | - |
| dust | `dust` | Disk usage | - |

## Quick Install

### macOS
```bash
brew install jq ripgrep fd bat ast-grep yq gh sd fzf git-delta
```

### Ubuntu/Debian
```bash
sudo apt install jq ripgrep fd-find bat
cargo install ast-grep --locked
```

### Windows (Scoop)
```bash
scoop install jq ripgrep fd bat ast-grep yq gh sd fzf delta
```

## Loading Strategy

1. Start with `quick.md` files (~50 lines each)
2. Load `reference.md` only for advanced usage
3. Check `../recipes/` for multi-tool combinations
