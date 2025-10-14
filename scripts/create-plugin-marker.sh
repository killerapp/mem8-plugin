#!/bin/bash
# create-plugin-marker.sh - Create marker file to indicate plugin-based installation

CLAUDE_DIR=".claude"
MARKER_FILE="$CLAUDE_DIR/.mem8-plugin"

if [ ! -d "$CLAUDE_DIR" ]; then
  # Create .claude directory if it doesn't exist
  mkdir -p "$CLAUDE_DIR"
fi

# Create marker with metadata
cat > "$MARKER_FILE" << EOF
{
  "installed_via": "plugin",
  "plugin_version": "3.0.0",
  "installed_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "marketplace": "mem8-official"
}
EOF

echo "✓ Plugin marker created"
