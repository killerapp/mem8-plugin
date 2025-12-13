#!/usr/bin/env python3
"""
Scan a project for CLI tool usage patterns.

Detects CLI tools used in:
- package.json (scripts)
- Makefile / justfile
- docker-compose.yml
- .github/workflows/*.yml
- shell scripts (*.sh)
- CLAUDE.md

Usage:
    python scan.py                     # Scan current directory
    python scan.py path/to/project     # Scan specific path
    python scan.py --json              # JSON output
    python scan.py --verbose           # Show where each tool was found
"""

import re
import sys
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Set, Optional


# CLI tools to look for
KNOWN_TOOLS = {
    # Tier 1
    'jq', 'rg', 'ripgrep', 'fd', 'fdfind', 'bat', 'batcat', 'ast-grep', 'sg',
    # Tier 2
    'yq', 'sd', 'fzf', 'delta', 'http', 'httpie', 'eza', 'gh',
    # Tier 3
    'tokei', 'hyperfine', 'dust', 'glow', 'procs',
    # Common
    'git', 'curl', 'wget', 'docker', 'docker-compose', 'kubectl', 'aws',
    'npm', 'yarn', 'pnpm', 'pip', 'pipx', 'cargo', 'go', 'python', 'node',
    # Build tools
    'make', 'just', 'cmake', 'gradle', 'maven',
    # Media
    'ffmpeg', 'ffprobe', 'convert', 'imagemagick',
}

# Patterns that suggest CLI usage
COMMAND_PATTERNS = [
    r'\b(jq)\s+[\'"]?[\.\[\$]',  # jq with filter
    r'\b(rg|ripgrep)\s+',        # ripgrep search
    r'\b(fd|fdfind)\s+',         # fd find
    r'\b(gh)\s+(issue|pr|repo|api)',  # gh CLI
    r'\b(docker)\s+(run|build|compose)',  # docker commands
    r'\b(ffmpeg)\s+-i',          # ffmpeg input
]


@dataclass
class ToolUsage:
    """Record of a tool being used."""
    tool: str
    file: str
    line: Optional[int] = None
    context: Optional[str] = None


@dataclass
class ScanResult:
    """Result of scanning a project."""
    path: str
    tools_found: List[str]
    usage: List[ToolUsage]
    files_scanned: int
    recommendations: List[str]


def scan_file(path: Path, content: str) -> List[ToolUsage]:
    """Scan a file for CLI tool usage."""
    usages = []
    lines = content.split('\n')

    for line_num, line in enumerate(lines, 1):
        # Skip comments in some contexts
        stripped = line.strip()
        if stripped.startswith('#') and not path.suffix in ['.yml', '.yaml']:
            continue

        # Check for known tools
        words = re.findall(r'\b([a-zA-Z][a-zA-Z0-9_-]*)\b', line)
        for word in words:
            word_lower = word.lower()
            if word_lower in KNOWN_TOOLS or word in KNOWN_TOOLS:
                usages.append(ToolUsage(
                    tool=word_lower,
                    file=str(path),
                    line=line_num,
                    context=stripped[:80] if len(stripped) > 80 else stripped
                ))

    return usages


def scan_package_json(path: Path) -> List[ToolUsage]:
    """Scan package.json scripts for CLI tools."""
    usages = []
    try:
        content = path.read_text()
        data = json.loads(content)
        scripts = data.get('scripts', {})

        for script_name, script_cmd in scripts.items():
            for tool in KNOWN_TOOLS:
                if re.search(rf'\b{tool}\b', script_cmd):
                    usages.append(ToolUsage(
                        tool=tool,
                        file=str(path),
                        context=f"scripts.{script_name}: {script_cmd[:60]}..."
                    ))
    except (json.JSONDecodeError, Exception):
        pass

    return usages


def scan_yaml(path: Path) -> List[ToolUsage]:
    """Scan YAML files for CLI tools."""
    usages = []
    try:
        content = path.read_text()
        usages.extend(scan_file(path, content))
    except Exception:
        pass
    return usages


def scan_makefile(path: Path) -> List[ToolUsage]:
    """Scan Makefile/justfile for CLI tools."""
    usages = []
    try:
        content = path.read_text()
        usages.extend(scan_file(path, content))
    except Exception:
        pass
    return usages


def scan_project(project_path: Path) -> ScanResult:
    """Scan a project directory for CLI tool usage."""
    all_usages: List[ToolUsage] = []
    files_scanned = 0

    # package.json
    pkg_json = project_path / 'package.json'
    if pkg_json.exists():
        all_usages.extend(scan_package_json(pkg_json))
        files_scanned += 1

    # Makefile / justfile
    for makefile in ['Makefile', 'makefile', 'justfile', 'Justfile']:
        mf = project_path / makefile
        if mf.exists():
            all_usages.extend(scan_makefile(mf))
            files_scanned += 1

    # docker-compose
    for dc in ['docker-compose.yml', 'docker-compose.yaml', 'compose.yml', 'compose.yaml']:
        dc_path = project_path / dc
        if dc_path.exists():
            all_usages.extend(scan_yaml(dc_path))
            files_scanned += 1

    # GitHub workflows
    workflows_dir = project_path / '.github' / 'workflows'
    if workflows_dir.exists():
        for wf in workflows_dir.glob('*.yml'):
            all_usages.extend(scan_yaml(wf))
            files_scanned += 1
        for wf in workflows_dir.glob('*.yaml'):
            all_usages.extend(scan_yaml(wf))
            files_scanned += 1

    # Shell scripts (top-level only)
    for sh in project_path.glob('*.sh'):
        try:
            all_usages.extend(scan_file(sh, sh.read_text()))
            files_scanned += 1
        except Exception:
            pass

    # CLAUDE.md
    claude_md = project_path / 'CLAUDE.md'
    if claude_md.exists():
        try:
            all_usages.extend(scan_file(claude_md, claude_md.read_text()))
            files_scanned += 1
        except Exception:
            pass

    # scripts/ directory
    scripts_dir = project_path / 'scripts'
    if scripts_dir.exists():
        for script in scripts_dir.glob('*'):
            if script.is_file() and script.suffix in ['.sh', '.py', '.js', '.ts']:
                try:
                    all_usages.extend(scan_file(script, script.read_text()))
                    files_scanned += 1
                except Exception:
                    pass

    # Deduplicate and get unique tools
    tools_found = sorted(set(u.tool for u in all_usages))

    # Generate recommendations based on what's found
    recommendations = generate_recommendations(tools_found)

    return ScanResult(
        path=str(project_path),
        tools_found=tools_found,
        usage=all_usages,
        files_scanned=files_scanned,
        recommendations=recommendations
    )


def generate_recommendations(tools_found: List[str]) -> List[str]:
    """Generate recommendations based on detected tools."""
    recommendations = []

    # If using curl for JSON APIs, recommend jq
    if 'curl' in tools_found and 'jq' not in tools_found:
        recommendations.append("You use curl - consider jq for JSON processing")

    # If using grep/find, recommend rg/fd
    if 'grep' in tools_found and 'rg' not in tools_found:
        recommendations.append("You use grep - consider ripgrep (rg) for faster search")
    if 'find' in tools_found and 'fd' not in tools_found:
        recommendations.append("You use find - consider fd for simpler syntax")

    # If using gh, recommend jq for --json output
    if 'gh' in tools_found and 'jq' not in tools_found:
        recommendations.append("You use gh CLI - combine with jq for powerful --json processing")

    # If using docker, recommend docker stats recipes
    if 'docker' in tools_found:
        recommendations.append("Docker detected - check recipes/devops/ for cleanup patterns")

    # If using git, recommend gh
    if 'git' in tools_found and 'gh' not in tools_found:
        recommendations.append("You use git - consider gh CLI for GitHub workflow automation")

    return recommendations


def format_result(result: ScanResult, verbose: bool = False) -> str:
    """Format scan result for display."""
    lines = []

    lines.append(f"# Project Scan: {result.path}")
    lines.append(f"Files scanned: {result.files_scanned}")
    lines.append("")

    lines.append("## CLI Tools Detected")
    if result.tools_found:
        for tool in result.tools_found:
            lines.append(f"  - {tool}")
    else:
        lines.append("  (none detected)")
    lines.append("")

    if verbose and result.usage:
        lines.append("## Usage Details")
        for usage in result.usage:
            loc = f":{usage.line}" if usage.line else ""
            lines.append(f"  - {usage.tool} in {usage.file}{loc}")
            if usage.context:
                lines.append(f"    {usage.context}")
        lines.append("")

    if result.recommendations:
        lines.append("## Recommendations")
        for rec in result.recommendations:
            lines.append(f"  - {rec}")
        lines.append("")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description="Scan project for CLI tool usage")
    parser.add_argument("path", nargs='?', default='.', help="Project path to scan")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed usage")
    args = parser.parse_args()

    path = Path(args.path).resolve()

    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)

    result = scan_project(path)

    if args.json:
        output = asdict(result)
        # Convert ToolUsage objects
        output['usage'] = [asdict(u) for u in result.usage]
        print(json.dumps(output, indent=2))
    else:
        print(format_result(result, args.verbose))


if __name__ == "__main__":
    main()
