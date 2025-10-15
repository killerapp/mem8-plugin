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
/mem8:plan          # Create implementation plan
/mem8:research      # Research codebase or topic
/mem8:implement     # Implement from plan
/mem8:validate      # Validate implementation
```

## Commands

- `/mem8:commit` - Create well-structured commits
- `/mem8:debug` - Debug issues with memory context
- `/mem8:describe-pr` - Generate PR descriptions
- `/mem8:implement` - Implement from plans
- `/mem8:local-review` - Set up review environments
- `/mem8:plan` - Create implementation plans
- `/mem8:research` - Research codebase
- `/mem8:validate` - Validate implementations

For more information, see: https://github.com/killerapp/mem8
EOF

echo "✓ Memory directory created successfully"
echo ""
echo "Next steps:"
echo "  • Use /mem8:research to explore your codebase"
echo "  • Use /mem8:plan to create implementation plans"
echo "  • Run 'mem8 status' to verify setup"
