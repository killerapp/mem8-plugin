# Top CLI Tools for AI-Assisted Development

Curated list of CLI tools that dramatically enhance AI agent capabilities. Organized by category with availability check commands.

## Table of Contents
- [Text & Data Processing](#text--data-processing)
- [Search & Navigation](#search--navigation)
- [Code Analysis & Transformation](#code-analysis--transformation)
- [Version Control & Collaboration](#version-control--collaboration)
- [System & Process Management](#system--process-management)
- [Network & HTTP](#network--http)
- [File & Archive Operations](#file--archive-operations)
- [Development Utilities](#development-utilities)

---

## Text & Data Processing

### Essential (Install First)

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **jq** | `jq` | `jq --version` | JSON parsing, filtering, transformation. Critical for API responses. |
| **yq** | `yq` | `yq --version` | YAML/XML/TOML processing. Essential for config files. |
| **sd** | `sd` | `sd --version` | Modern sed replacement. Simpler regex syntax for text replacement. |
| **ripgrep** | `rg` | `rg --version` | Ultra-fast text search. 10-100x faster than grep. |

### Advanced

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **gawk** | `gawk` | `gawk --version` | Pattern scanning and processing. Complex text transformations. |
| **miller** | `mlr` | `mlr --version` | CSV/JSON/tabular data like awk but structured. |
| **xsv** | `xsv` | `xsv --version` | Fast CSV toolkit. Indexing, slicing, stats. |
| **dasel** | `dasel` | `dasel --version` | Query/modify JSON/YAML/TOML/XML with single syntax. |
| **htmlq** | `htmlq` | `htmlq --version` | HTML parsing like jq. CSS selectors for extraction. |
| **pup** | `pup` | `pup --version` | HTML stream processor. DOM queries via CLI. |
| **csvkit** | `csvstat` | `csvstat --version` | CSV utilities: stats, convert, grep, join. |

---

## Search & Navigation

### Essential

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **fd** | `fd` | `fd --version` | Fast file finder. Simpler syntax than find. |
| **fzf** | `fzf` | `fzf --version` | Fuzzy finder. Interactive filtering for any list. |
| **bat** | `bat` | `bat --version` | Cat with syntax highlighting and git integration. |
| **eza/exa** | `eza` or `exa` | `eza --version` | Modern ls with colors, git status, tree view. |

### Advanced

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **broot** | `broot` | `broot --version` | Interactive tree navigator with fuzzy search. |
| **zoxide** | `zoxide` | `zoxide --version` | Smart cd that learns your habits. |
| **tree** | `tree` | `tree --version` | Directory tree visualization. |
| **ncdu** | `ncdu` | `ncdu --version` | Interactive disk usage analyzer. |
| **dust** | `dust` | `dust --version` | Intuitive disk usage (du replacement). |
| **duf** | `duf` | `duf --version` | Disk usage with nice formatting. |

---

## Code Analysis & Transformation

### Essential

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **ast-grep** | `ast-grep` or `sg` | `ast-grep --version` | AST-based code search/transform. Language-aware refactoring. |
| **tree-sitter** | `tree-sitter` | `tree-sitter --version` | Parser generator for syntax trees. Foundation for AST tools. |
| **tokei** | `tokei` | `tokei --version` | Code statistics by language. Fast line counting. |
| **cloc** | `cloc` | `cloc --version` | Count lines of code, comments, blanks. |

### Language-Specific

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **shellcheck** | `shellcheck` | `shellcheck --version` | Shell script static analysis. Catches common bugs. |
| **shfmt** | `shfmt` | `shfmt --version` | Shell script formatter. |
| **prettier** | `prettier` | `prettier --version` | Multi-language code formatter. |
| **black** | `black` | `black --version` | Python code formatter. |
| **ruff** | `ruff` | `ruff --version` | Fast Python linter (replaces flake8, isort, etc). |
| **eslint** | `eslint` | `eslint --version` | JavaScript/TypeScript linter. |
| **biome** | `biome` | `biome --version` | Fast JS/TS/JSON formatter and linter. |

---

## Version Control & Collaboration

### Essential

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **git** | `git` | `git --version` | Version control. Foundation for all dev work. |
| **gh** | `gh` | `gh --version` | GitHub CLI. Issues, PRs, actions, repos from terminal. |
| **delta** | `delta` | `delta --version` | Beautiful git diff viewer with syntax highlighting. |

### Advanced

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **lazygit** | `lazygit` | `lazygit --version` | TUI for git. Visual staging, commits, branches. |
| **tig** | `tig` | `tig --version` | Text-mode git interface. Log, diff, blame viewer. |
| **git-absorb** | `git-absorb` | `git absorb --version` | Auto-fix commits. Distributes changes to right commits. |
| **git-branchless** | `git-branchless` | `git branchless --version` | Stacked diffs workflow. |
| **glab** | `glab` | `glab --version` | GitLab CLI. Like gh but for GitLab. |

---

## System & Process Management

### Essential

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **htop** | `htop` | `htop --version` | Interactive process viewer. Better than top. |
| **procs** | `procs` | `procs --version` | Modern ps replacement. Colored, searchable. |
| **bottom/btm** | `btm` | `btm --version` | System monitor TUI. CPU, mem, network, disk. |

### Advanced

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **hyperfine** | `hyperfine` | `hyperfine --version` | Command benchmarking. Compare performance. |
| **watchexec** | `watchexec` | `watchexec --version` | Run commands on file changes. |
| **entr** | `entr` | `echo test \| entr echo ok` | Run commands when files change. Simpler than watchexec. |
| **parallel** | `parallel` | `parallel --version` | Run commands in parallel. Massive speedups. |
| **xargs** | `xargs` | `xargs --version` | Build commands from stdin. Batch processing. |
| **pv** | `pv` | `pv --version` | Pipe viewer. Progress bars for streams. |

---

## Network & HTTP

### Essential

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **curl** | `curl` | `curl --version` | HTTP client. Universal API testing. |
| **httpie** | `http` | `http --version` | User-friendly HTTP client. Pretty output. |
| **wget** | `wget` | `wget --version` | Download files. Recursive, retry support. |

### Advanced

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **curlie** | `curlie` | `curlie --version` | httpie-like syntax with curl power. |
| **xh** | `xh` | `xh --version` | Fast HTTP client written in Rust. |
| **doggo** | `doggo` | `doggo --version` | DNS lookup client. Human-friendly output. |
| **mtr** | `mtr` | `mtr --version` | Network diagnostic (traceroute + ping). |
| **bandwhich** | `bandwhich` | `bandwhich --version` | Bandwidth utilization by process. |
| **gping** | `gping` | `gping --version` | Ping with graph visualization. |

---

## File & Archive Operations

### Essential

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **tar** | `tar` | `tar --version` | Archive creation/extraction. |
| **gzip/gunzip** | `gzip` | `gzip --version` | Compression utility. |
| **unzip** | `unzip` | `unzip -v` | ZIP extraction. |
| **7z** | `7z` | `7z --help` | Universal archive tool. |

### Advanced

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **zstd** | `zstd` | `zstd --version` | Fast compression. Better ratio than gzip. |
| **pigz** | `pigz` | `pigz --version` | Parallel gzip. Multi-core compression. |
| **ouch** | `ouch` | `ouch --version` | Unified compress/decompress. Auto-detects format. |
| **rsync** | `rsync` | `rsync --version` | Efficient file sync. Delta transfers. |
| **rclone** | `rclone` | `rclone --version` | Sync to cloud storage (S3, GCS, etc). |

---

## Development Utilities

### Essential

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **make** | `make` | `make --version` | Build automation. Standard for many projects. |
| **just** | `just` | `just --version` | Modern command runner. Simpler than make. |
| **docker** | `docker` | `docker --version` | Containerization. Isolated environments. |
| **uv** | `uv` | `uv --version` | Fast Python package manager. |

### Advanced

| Tool | Command | Check | Why AI Needs It |
|------|---------|-------|-----------------|
| **direnv** | `direnv` | `direnv --version` | Per-directory environment variables. |
| **mise/rtx** | `mise` | `mise --version` | Polyglot tool version manager. |
| **asdf** | `asdf` | `asdf --version` | Version manager for many languages. |
| **task** | `task` | `task --version` | Task runner. YAML-based alternative to make. |
| **navi** | `navi` | `navi --version` | Interactive cheatsheet navigator. |
| **tldr** | `tldr` | `tldr --version` | Simplified man pages with examples. |
| **charm/gum** | `gum` | `gum --version` | Shell script UI toolkit. Pretty prompts. |
| **glow** | `glow` | `glow --version` | Markdown renderer for terminal. |
| **fx** | `fx` | `fx --version` | Interactive JSON viewer. |

---

## Priority Recommendation Matrix

### Tier 1: Install These First (Maximum AI Impact)
1. **jq** - JSON is everywhere
2. **ripgrep (rg)** - Faster code search = faster AI
3. **fd** - Find files without remembering arcane syntax
4. **bat** - Syntax highlighting makes reading easier
5. **ast-grep** - Language-aware code transformations

### Tier 2: High Value
6. **yq** - YAML configs are everywhere
7. **sd** - Text replacement without sed's quirks
8. **fzf** - Interactive filtering for any workflow
9. **delta** - Better git diffs
10. **httpie/xh** - API testing made easy

### Tier 3: Nice to Have
11. **eza** - Pretty directory listings
12. **tokei** - Quick codebase stats
13. **hyperfine** - Performance benchmarking
14. **dust** - Disk usage analysis
15. **glow** - Render markdown in terminal
