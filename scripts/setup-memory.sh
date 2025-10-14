#!/bin/bash
# setup-memory.sh - Initialize memory directory structure

MEMORY_DIR="memory"

# Check if memory directory already exists
if [ -d "$MEMORY_DIR" ]; then
  echo "✓ Memory directory already exists"
  exit 0
fi

echo "Creating memory directory structure..."

# Create directory structure
mkdir -p "$MEMORY_DIR"/{plans,research,prs,docs}

# Create README
cat > "$MEMORY_DIR/README.md" << 'EOF'
# Memory Directory

This directory stores persistent memory for your project:

- `plans/` - Implementation plans and technical designs
- `research/` - Research documents and findings
- `prs/` - Pull request descriptions and reviews
- `docs/` - Documentation and notes

## Usage

Use mem8 commands to create and manage memory:

```bash
/m8-plan          # Create implementation plan
/m8-research      # Research codebase or topic
/m8-implement     # Implement from plan
/m8-validate      # Validate implementation
```

## Commands

- `/m8-commit` - Create well-structured commits
- `/m8-debug` - Debug issues with memory context
- `/m8-describe-pr` - Generate PR descriptions
- `/m8-implement` - Implement from plans
- `/m8-local-review` - Set up review environments
- `/m8-plan` - Create implementation plans
- `/m8-research` - Research codebase
- `/m8-validate` - Validate implementations

For more information, see: https://github.com/killerapp/mem8
EOF

echo "✓ Memory directory created successfully"
echo ""
echo "Next steps:"
echo "  • Use /m8-research to explore your codebase"
echo "  • Use /m8-plan to create implementation plans"
echo "  • Run 'mem8 status' to verify setup"
