#!/usr/bin/env python3
"""
Validate CLI recipe files for completeness and format.

Checks:
- YAML frontmatter format and required fields
- Required sections (Problem, Solution, How It Works)
- Code blocks present
- Tool names in frontmatter

Usage:
    python validate.py recipe.md           # Single file
    python validate.py recipes/            # Directory (recursive)
    python validate.py --strict recipe.md  # Fail on warnings too
    python validate.py --json recipe.md    # JSON output
"""

import sys
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Optional, Tuple


@dataclass
class ValidationResult:
    """Result of validating a recipe file."""
    path: str
    valid: bool
    errors: List[str]
    warnings: List[str]


def parse_frontmatter(content: str) -> Tuple[Optional[dict], str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content

    try:
        # Simple YAML parsing for frontmatter (no external deps)
        frontmatter = {}
        for line in parts[1].strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                # Handle lists like [gh, jq]
                if value.startswith('[') and value.endswith(']'):
                    value = [v.strip() for v in value[1:-1].split(',')]
                # Handle booleans
                elif value.lower() in ('true', 'false'):
                    value = value.lower() == 'true'
                frontmatter[key] = value
        return frontmatter, parts[2]
    except Exception as e:
        return None, content


def validate_recipe(path: Path, strict: bool = False) -> ValidationResult:
    """Validate a single recipe file."""
    errors = []
    warnings = []

    try:
        content = path.read_text()
    except Exception as e:
        return ValidationResult(str(path), False, [f"Cannot read file: {e}"], [])

    # Check frontmatter
    frontmatter, body = parse_frontmatter(content)

    if frontmatter is None:
        errors.append("Missing or invalid YAML frontmatter")
    else:
        # Required fields
        required = ['name', 'description', 'tools']
        for field in required:
            if field not in frontmatter:
                errors.append(f"Missing required field: {field}")

        # Validate name format (kebab-case)
        if 'name' in frontmatter:
            name = frontmatter['name']
            if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', str(name)):
                errors.append(f"Invalid name format: '{name}' (use kebab-case)")

        # Validate tools is a list
        if 'tools' in frontmatter:
            if not isinstance(frontmatter['tools'], list):
                errors.append("'tools' should be a list, e.g., [gh, jq]")
            elif len(frontmatter['tools']) < 2:
                warnings.append("Recipes typically use 2+ tools")

        # Validate difficulty if present
        if 'difficulty' in frontmatter:
            valid = ['beginner', 'intermediate', 'advanced']
            if frontmatter['difficulty'] not in valid:
                errors.append(f"Invalid difficulty: '{frontmatter['difficulty']}' (use: {valid})")

    # Check required sections
    required_sections = ['## Problem', '## Solution', '## How It Works']
    for section in required_sections:
        if section not in body:
            errors.append(f"Missing required section: {section}")

    # Check for code blocks
    if '```' not in body:
        errors.append("No code examples found (missing ``` blocks)")

    # Recommended sections (warnings)
    recommended = ['## Variations', '## Common Pitfalls']
    for section in recommended:
        if section not in body:
            warnings.append(f"Consider adding: {section}")

    # Check See Also section
    if '## See Also' not in body:
        warnings.append("Consider adding: ## See Also with links to CLI quick refs")

    valid = len(errors) == 0
    if strict and len(warnings) > 0:
        valid = False

    return ValidationResult(str(path), valid, errors, warnings)


def validate_directory(path: Path, strict: bool = False) -> List[ValidationResult]:
    """Validate all recipe files in a directory."""
    results = []

    # Skip index and template files
    skip_names = {'_index.md', 'TEMPLATE.md', 'CONTRIBUTING.md'}

    for md_file in path.rglob('*.md'):
        if md_file.name in skip_names:
            continue
        results.append(validate_recipe(md_file, strict))

    return results


def format_result(result: ValidationResult) -> str:
    """Format a validation result for display."""
    lines = []

    if result.valid and not result.warnings:
        lines.append(f"✅ {result.path}")
    elif result.valid:
        lines.append(f"⚠️  {result.path}")
    else:
        lines.append(f"❌ {result.path}")

    for error in result.errors:
        lines.append(f"   ERROR: {error}")
    for warning in result.warnings:
        lines.append(f"   WARN:  {warning}")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description="Validate CLI recipe files")
    parser.add_argument("path", nargs='?', default='.', help="File or directory to validate")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    path = Path(args.path)

    if path.is_file():
        results = [validate_recipe(path, args.strict)]
    elif path.is_dir():
        results = validate_directory(path, args.strict)
    else:
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)

    if not results:
        print("No recipe files found")
        sys.exit(0)

    if args.json:
        output = {
            "results": [asdict(r) for r in results],
            "summary": {
                "total": len(results),
                "valid": len([r for r in results if r.valid]),
                "invalid": len([r for r in results if not r.valid]),
                "with_warnings": len([r for r in results if r.warnings])
            }
        }
        print(json.dumps(output, indent=2))
    else:
        for result in results:
            print(format_result(result))
            print()

        # Summary
        valid = len([r for r in results if r.valid])
        total = len(results)
        print(f"Validated {total} files: {valid} valid, {total - valid} invalid")

    # Exit with error if any invalid
    if any(not r.valid for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
