# CLI Tool Installation Guide

Platform-specific installation commands for all recommended tools.

## Table of Contents
- [Quick Install Scripts](#quick-install-scripts)
- [Package Manager Setup](#package-manager-setup)
- [Individual Tool Installation](#individual-tool-installation)

---

## Quick Install Scripts

### Linux (Ubuntu/Debian)

```bash
# Essential Tier 1 tools
sudo apt update && sudo apt install -y jq fd-find bat

# ripgrep
sudo apt install -y ripgrep

# fd is installed as fdfind on Debian/Ubuntu - create alias
sudo ln -sf $(which fdfind) /usr/local/bin/fd

# bat is installed as batcat on Debian/Ubuntu - create alias
sudo ln -sf $(which batcat) /usr/local/bin/bat

# yq (via snap or binary)
sudo snap install yq

# ast-grep (via cargo or binary)
cargo install ast-grep --locked
# Or download binary from https://github.com/ast-grep/ast-grep/releases
```

### macOS (Homebrew)

```bash
# Essential Tier 1 tools - all available via brew
brew install jq ripgrep fd bat yq ast-grep

# Tier 2
brew install sd fzf delta httpie eza

# Tier 3
brew install tokei hyperfine dust glow
```

### Windows (winget/scoop)

```powershell
# Using winget
winget install jqlang.jq BurntSushi.ripgrep.MSVC sharkdp.fd sharkdp.bat

# Using scoop (recommended for dev tools)
scoop install jq ripgrep fd bat yq ast-grep sd fzf delta
```

### WSL (Windows Subsystem for Linux)

```bash
# Use Linux instructions, but also consider:
# 1. Tools installed in Windows are NOT automatically available in WSL
# 2. Install separately in WSL for best performance
# 3. Can access Windows tools via /mnt/c/... but slower

# Fast path: use cargo for Rust tools
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
cargo install ripgrep fd-find bat ast-grep sd
```

---

## Package Manager Setup

### Homebrew (macOS/Linux)

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add to PATH (Linux)
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
```

### Cargo (Rust tools)

```bash
# Install Rust toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env

# Now install Rust-based tools
cargo install ripgrep fd-find bat ast-grep sd eza tokei hyperfine
```

### Scoop (Windows)

```powershell
# Install Scoop
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

# Add extras bucket for more tools
scoop bucket add extras
```

### pipx (Python tools)

```bash
# Install pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install Python CLI tools
pipx install httpie
pipx install csvkit
pipx install ruff
```

---

## Individual Tool Installation

### jq - JSON Processor

```bash
# Ubuntu/Debian
sudo apt install jq

# macOS
brew install jq

# Windows
winget install jqlang.jq
# or
scoop install jq

# Arch Linux
sudo pacman -S jq

# From source
git clone https://github.com/jqlang/jq.git && cd jq
autoreconf -i && ./configure && make && sudo make install
```

### ripgrep (rg) - Fast Search

```bash
# Ubuntu/Debian
sudo apt install ripgrep

# macOS
brew install ripgrep

# Windows
winget install BurntSushi.ripgrep.MSVC

# Cargo
cargo install ripgrep
```

### fd - File Finder

```bash
# Ubuntu/Debian (installed as fdfind)
sudo apt install fd-find
sudo ln -s $(which fdfind) /usr/local/bin/fd

# macOS
brew install fd

# Windows
scoop install fd

# Cargo
cargo install fd-find
```

### bat - Cat with Wings

```bash
# Ubuntu/Debian (installed as batcat)
sudo apt install bat
sudo ln -s $(which batcat) /usr/local/bin/bat

# macOS
brew install bat

# Windows
scoop install bat

# Cargo
cargo install bat
```

### yq - YAML Processor

```bash
# Ubuntu/Debian (via snap)
sudo snap install yq

# macOS
brew install yq

# Windows
scoop install yq

# Binary download
VERSION=v4.40.5
BINARY=yq_linux_amd64
wget https://github.com/mikefarah/yq/releases/download/${VERSION}/${BINARY} -O /usr/local/bin/yq
chmod +x /usr/local/bin/yq
```

### ast-grep (sg) - AST-Based Search

```bash
# macOS
brew install ast-grep

# Cargo (any platform)
cargo install ast-grep --locked

# npm
npm install -g @ast-grep/cli

# Binary download
# See https://github.com/ast-grep/ast-grep/releases
```

### sd - Modern sed

```bash
# macOS
brew install sd

# Cargo
cargo install sd

# Windows
scoop install sd
```

### fzf - Fuzzy Finder

```bash
# Ubuntu/Debian
sudo apt install fzf

# macOS
brew install fzf
$(brew --prefix)/opt/fzf/install  # Install shell integration

# Windows
scoop install fzf

# Git
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

### delta - Git Diff Viewer

```bash
# Ubuntu/Debian
sudo apt install git-delta

# macOS
brew install git-delta

# Cargo
cargo install git-delta

# Configure git to use delta
git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
```

### eza - Modern ls

```bash
# Ubuntu/Debian (22.04+)
sudo apt install eza

# macOS
brew install eza

# Cargo
cargo install eza

# Older: use exa
cargo install exa
```

### httpie / xh - HTTP Clients

```bash
# httpie (Python)
pipx install httpie
# or
brew install httpie

# xh (Rust - faster)
cargo install xh
# or
brew install xh
```

### tokei - Code Statistics

```bash
# macOS
brew install tokei

# Cargo
cargo install tokei

# Windows
scoop install tokei
```

### hyperfine - Benchmarking

```bash
# macOS
brew install hyperfine

# Cargo
cargo install hyperfine

# Ubuntu
sudo apt install hyperfine
```

### dust - Disk Usage

```bash
# macOS
brew install dust

# Cargo
cargo install du-dust

# Ubuntu (via cargo or download)
cargo install du-dust
```

### glow - Markdown Renderer

```bash
# macOS
brew install glow

# Ubuntu (via snap)
sudo snap install glow

# Windows
scoop install glow

# Go
go install github.com/charmbracelet/glow@latest
```

---

## Verification Commands

After installation, verify tools are working:

```bash
# Quick health check
for cmd in jq rg fd bat yq ast-grep sd fzf delta eza; do
  if command -v $cmd &>/dev/null; then
    echo "✅ $cmd: $(command -v $cmd)"
  else
    echo "❌ $cmd: not found"
  fi
done
```

## Troubleshooting

### Command not found after install

```bash
# Refresh shell
source ~/.bashrc  # or ~/.zshrc

# Check if in PATH
echo $PATH | tr ':' '\n' | grep -E "(cargo|local)"

# Add cargo to PATH if missing
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
```

### Permission denied

```bash
# Use user-local install instead of system-wide
cargo install <tool>  # Installs to ~/.cargo/bin/

# Or fix permissions
sudo chown -R $USER:$USER ~/.cargo
```

### WSL-specific issues

```bash
# If tools are slow, ensure they're installed IN WSL, not Windows
which rg  # Should show /usr/bin/rg or ~/.cargo/bin/rg, NOT /mnt/c/...

# For clipboard integration
sudo apt install xclip  # For X11
# or use win32yank for Windows clipboard
```
