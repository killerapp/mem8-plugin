#!/usr/bin/env python3
"""
Discover CLI tools available in the current environment.

Scans PATH for known power tools and reports availability,
versions, and recommendations for missing essentials.

Usage:
    python discover_tools.py [--json] [--tier TIER] [--missing-only]

Examples:
    python discover_tools.py                    # Full report
    python discover_tools.py --json             # JSON output for processing
    python discover_tools.py --tier 1           # Only essential tools
    python discover_tools.py --missing-only     # Show what to install
"""

import subprocess
import sys
import json
import platform
import argparse
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict
from pathlib import Path


@dataclass
class Tool:
    """Definition of a CLI tool."""
    name: str
    command: str
    check_cmd: str
    tier: int  # 1=essential, 2=high-value, 3=nice-to-have
    category: str
    description: str
    install: Dict[str, str]  # platform -> install command


@dataclass
class ToolStatus:
    """Status of a tool in the current environment."""
    name: str
    command: str
    available: bool
    version: Optional[str]
    path: Optional[str]
    tier: int
    category: str
    description: str
    install_cmd: Optional[str]


# Curated tool database
TOOLS: List[Tool] = [
    # Tier 1: Essential
    Tool("jq", "jq", "jq --version", 1, "data",
         "JSON processor - parse, filter, transform JSON",
         {"linux": "sudo apt install jq", "macos": "brew install jq", "windows": "scoop install jq"}),
    Tool("ripgrep", "rg", "rg --version", 1, "search",
         "Ultra-fast text search - 10-100x faster than grep",
         {"linux": "sudo apt install ripgrep", "macos": "brew install ripgrep", "windows": "scoop install ripgrep"}),
    Tool("fd", "fd", "fd --version", 1, "search",
         "Fast file finder - simpler syntax than find",
         {"linux": "sudo apt install fd-find && sudo ln -sf $(which fdfind) /usr/local/bin/fd",
          "macos": "brew install fd", "windows": "scoop install fd"}),
    Tool("bat", "bat", "bat --version", 1, "view",
         "Cat with syntax highlighting and git integration",
         {"linux": "sudo apt install bat && sudo ln -sf $(which batcat) /usr/local/bin/bat",
          "macos": "brew install bat", "windows": "scoop install bat"}),
    Tool("ast-grep", "ast-grep", "ast-grep --version", 1, "code",
         "AST-based code search and transformation",
         {"linux": "cargo install ast-grep --locked", "macos": "brew install ast-grep",
          "windows": "cargo install ast-grep --locked"}),

    # Tier 2: High Value
    Tool("yq", "yq", "yq --version", 2, "data",
         "YAML/XML/TOML processor - like jq but for YAML",
         {"linux": "sudo snap install yq", "macos": "brew install yq", "windows": "scoop install yq"}),
    Tool("sd", "sd", "sd --version", 2, "text",
         "Modern sed replacement - simpler regex syntax",
         {"linux": "cargo install sd", "macos": "brew install sd", "windows": "scoop install sd"}),
    Tool("fzf", "fzf", "fzf --version", 2, "search",
         "Fuzzy finder - interactive filtering for any list",
         {"linux": "sudo apt install fzf", "macos": "brew install fzf", "windows": "scoop install fzf"}),
    Tool("delta", "delta", "delta --version", 2, "git",
         "Beautiful git diff viewer with syntax highlighting",
         {"linux": "sudo apt install git-delta", "macos": "brew install git-delta",
          "windows": "scoop install delta"}),
    Tool("httpie", "http", "http --version", 2, "network",
         "User-friendly HTTP client - pretty output",
         {"linux": "pipx install httpie", "macos": "brew install httpie", "windows": "pipx install httpie"}),
    Tool("eza", "eza", "eza --version", 2, "view",
         "Modern ls with colors, git status, tree view",
         {"linux": "cargo install eza", "macos": "brew install eza", "windows": "cargo install eza"}),

    # Tier 3: Nice to Have
    Tool("tokei", "tokei", "tokei --version", 3, "code",
         "Fast code statistics by language",
         {"linux": "cargo install tokei", "macos": "brew install tokei", "windows": "cargo install tokei"}),
    Tool("hyperfine", "hyperfine", "hyperfine --version", 3, "benchmark",
         "Command benchmarking tool",
         {"linux": "cargo install hyperfine", "macos": "brew install hyperfine",
          "windows": "cargo install hyperfine"}),
    Tool("dust", "dust", "dust --version", 3, "system",
         "Intuitive disk usage analyzer",
         {"linux": "cargo install du-dust", "macos": "brew install dust", "windows": "cargo install du-dust"}),
    Tool("glow", "glow", "glow --version", 3, "view",
         "Render markdown in terminal",
         {"linux": "sudo snap install glow", "macos": "brew install glow", "windows": "scoop install glow"}),
    Tool("procs", "procs", "procs --version", 3, "system",
         "Modern ps replacement - colored and searchable",
         {"linux": "cargo install procs", "macos": "brew install procs", "windows": "cargo install procs"}),

    # Common tools (often pre-installed)
    Tool("git", "git", "git --version", 1, "vcs",
         "Version control - foundation for all dev work",
         {"linux": "sudo apt install git", "macos": "brew install git", "windows": "winget install Git.Git"}),
    Tool("gh", "gh", "gh --version", 1, "vcs",
         "GitHub CLI - issues, PRs, actions from terminal",
         {"linux": "sudo apt install gh", "macos": "brew install gh", "windows": "winget install GitHub.cli"}),
    Tool("curl", "curl", "curl --version", 1, "network",
         "HTTP client - universal API testing",
         {"linux": "sudo apt install curl", "macos": "brew install curl", "windows": "built-in"}),
    Tool("docker", "docker", "docker --version", 2, "container",
         "Containerization - isolated environments",
         {"linux": "see docker.com", "macos": "brew install --cask docker", "windows": "winget install Docker.DockerDesktop"}),
]


def get_platform() -> str:
    """Detect current platform."""
    system = platform.system().lower()
    if system == "darwin":
        return "macos"
    elif system == "windows":
        return "windows"
    else:
        return "linux"


def check_tool(tool: Tool) -> ToolStatus:
    """Check if a tool is available and get its version."""
    try:
        # Try to run the version command
        result = subprocess.run(
            tool.check_cmd.split(),
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            # Extract version from output
            output = result.stdout.strip() or result.stderr.strip()
            version = output.split('\n')[0] if output else "available"

            # Get path
            which_result = subprocess.run(
                ["which", tool.command] if get_platform() != "windows" else ["where", tool.command],
                capture_output=True,
                text=True,
                timeout=5
            )
            path = which_result.stdout.strip().split('\n')[0] if which_result.returncode == 0 else None

            return ToolStatus(
                name=tool.name,
                command=tool.command,
                available=True,
                version=version,
                path=path,
                tier=tool.tier,
                category=tool.category,
                description=tool.description,
                install_cmd=None
            )
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
        pass

    # Tool not available
    plat = get_platform()
    return ToolStatus(
        name=tool.name,
        command=tool.command,
        available=False,
        version=None,
        path=None,
        tier=tool.tier,
        category=tool.category,
        description=tool.description,
        install_cmd=tool.install.get(plat, tool.install.get("linux", "See documentation"))
    )


def discover_all() -> List[ToolStatus]:
    """Discover all tools in the database."""
    return [check_tool(tool) for tool in TOOLS]


def format_report(statuses: List[ToolStatus], missing_only: bool = False) -> str:
    """Format a human-readable report."""
    lines = []

    # Group by tier
    for tier in [1, 2, 3]:
        tier_name = {1: "Essential", 2: "High Value", 3: "Nice to Have"}[tier]
        tier_tools = [s for s in statuses if s.tier == tier]

        if missing_only:
            tier_tools = [s for s in tier_tools if not s.available]

        if not tier_tools:
            continue

        lines.append(f"\n## Tier {tier}: {tier_name}")
        lines.append("")

        for s in tier_tools:
            if s.available:
                lines.append(f"  ✅ {s.name} ({s.command})")
                lines.append(f"     {s.version}")
            else:
                lines.append(f"  ❌ {s.name} ({s.command})")
                lines.append(f"     {s.description}")
                lines.append(f"     Install: {s.install_cmd}")
        lines.append("")

    # Summary
    available = len([s for s in statuses if s.available])
    total = len(statuses)
    lines.insert(0, f"# CLI Tool Discovery Report")
    lines.insert(1, f"Platform: {get_platform()} | Available: {available}/{total}")
    lines.insert(2, "")

    return "\n".join(lines)


def get_recommendations(statuses: List[ToolStatus], count: int = 3) -> List[ToolStatus]:
    """Get top N tool recommendations to install."""
    missing = [s for s in statuses if not s.available]
    # Sort by tier (lower = more important)
    missing.sort(key=lambda x: x.tier)
    return missing[:count]


def main():
    parser = argparse.ArgumentParser(description="Discover CLI tools in your environment")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3], help="Filter by tier")
    parser.add_argument("--missing-only", action="store_true", help="Show only missing tools")
    parser.add_argument("--recommend", type=int, metavar="N", help="Show top N recommendations")
    args = parser.parse_args()

    statuses = discover_all()

    # Filter by tier if specified
    if args.tier:
        statuses = [s for s in statuses if s.tier == args.tier]

    # JSON output
    if args.json:
        output = {
            "platform": get_platform(),
            "tools": [asdict(s) for s in statuses],
            "summary": {
                "available": len([s for s in statuses if s.available]),
                "missing": len([s for s in statuses if not s.available]),
                "total": len(statuses)
            }
        }
        if args.recommend:
            output["recommendations"] = [asdict(s) for s in get_recommendations(statuses, args.recommend)]
        print(json.dumps(output, indent=2))
    elif args.recommend:
        recs = get_recommendations(statuses, args.recommend)
        print(f"# Top {len(recs)} Recommended Tools to Install\n")
        for i, s in enumerate(recs, 1):
            print(f"{i}. **{s.name}** ({s.command})")
            print(f"   {s.description}")
            print(f"   ```")
            print(f"   {s.install_cmd}")
            print(f"   ```\n")
    else:
        print(format_report(statuses, args.missing_only))


if __name__ == "__main__":
    main()
