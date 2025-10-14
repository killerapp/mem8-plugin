@echo off
REM setup-memory.bat - Initialize memory directory structure (Windows)

set MEMORY_DIR=memory

REM Check if memory directory already exists
if exist "%MEMORY_DIR%" (
    echo ✓ Memory directory already exists
    exit /b 0
)

echo Creating memory directory structure...

REM Create directory structure
mkdir "%MEMORY_DIR%\plans" 2>nul
mkdir "%MEMORY_DIR%\research" 2>nul
mkdir "%MEMORY_DIR%\prs" 2>nul
mkdir "%MEMORY_DIR%\docs" 2>nul

REM Create README
(
echo # Memory Directory
echo.
echo This directory stores persistent memory for your project:
echo.
echo - `plans/` - Implementation plans and technical designs
echo - `research/` - Research documents and findings
echo - `prs/` - Pull request descriptions and reviews
echo - `docs/` - Documentation and notes
echo.
echo ## Usage
echo.
echo Use mem8 commands to create and manage memory:
echo.
echo ```bash
echo /m8-plan          # Create implementation plan
echo /m8-research      # Research codebase or topic
echo /m8-implement     # Implement from plan
echo /m8-validate      # Validate implementation
echo ```
echo.
echo For more information, see: https://github.com/killerapp/mem8
) > "%MEMORY_DIR%\README.md"

echo ✓ Memory directory created successfully
echo.
echo Next steps:
echo   • Use /m8-research to explore your codebase
echo   • Use /m8-plan to create implementation plans
echo   • Run 'mem8 status' to verify setup
