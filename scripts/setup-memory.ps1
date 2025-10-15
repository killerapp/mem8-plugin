# setup-memory.ps1 - Initialize memory directory structure (PowerShell)

$MEMORY_DIR = "memory"

# Check if memory directory already exists
if (Test-Path -Path $MEMORY_DIR) {
    Write-Host "✓ Memory directory already exists"
    exit 0
}

Write-Host "Creating memory directory structure..."

# Create directory structure
New-Item -Path $MEMORY_DIR -ItemType Directory -Force | Out-Null
New-Item -Path "$MEMORY_DIR/plans" -ItemType Directory -Force | Out-Null
New-Item -Path "$MEMORY_DIR/research" -ItemType Directory -Force | Out-Null
New-Item -Path "$MEMORY_DIR/prs" -ItemType Directory -Force | Out-Null
New-Item -Path "$MEMORY_DIR/docs" -ItemType Directory -Force | Out-Null

# Create README
@"
# Memory Directory

This directory stores persistent memory for your project:

- ``plans/`` - Implementation plans and technical designs
- ``research/`` - Research documents and findings
- ``prs/`` - Pull request descriptions and reviews
- ``docs/`` - Documentation and notes

## Usage

Use mem8 commands to create and manage memory:

``````bash
/mem8:plan          # Create implementation plan
/mem8:research      # Research codebase or topic
/mem8:implement     # Implement from plan
/mem8:validate      # Validate implementation
``````

## Commands

- ``/mem8:commit`` - Create well-structured commits
- ``/mem8:debug`` - Debug issues with memory context
- ``/mem8:describe-pr`` - Generate PR descriptions
- ``/mem8:implement`` - Implement from plans
- ``/mem8:local-review`` - Set up review environments
- ``/mem8:plan`` - Create implementation plans
- ``/mem8:research`` - Research codebase
- ``/mem8:validate`` - Validate implementations

For more information, see: https://github.com/killerapp/mem8
"@ | Out-File -FilePath "$MEMORY_DIR/README.md" -Encoding UTF8

Write-Host "✓ Memory directory created successfully"
Write-Host ""
Write-Host "Next steps:"
Write-Host "  • Use /mem8:research to explore your codebase"
Write-Host "  • Use /mem8:plan to create implementation plans"
Write-Host "  • Run 'mem8 status' to verify setup"
