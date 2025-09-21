#!/bin/bash
# CLI Agent Template - Quick Install Script
# Usage: curl -sSL https://raw.githubusercontent.com/aget-framework/cli-agent-template/main/install.sh | bash

set -e

echo "╔════════════════════════════════════════╗"
echo "║     CLI Agent Template Installer      ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3.8+ and try again."
    exit 1
fi

# Determine target directory (current directory)
TARGET_DIR="${1:-$(pwd)}"

echo "📍 Target directory: $TARGET_DIR"

# Check if target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Target directory does not exist: $TARGET_DIR"
    exit 1
fi

# Create temporary directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "📥 Downloading CLI Agent Template..."

# Clone the repository to temp directory
if command -v git &> /dev/null; then
    git clone --quiet https://github.com/aget-framework/cli-agent-template.git "$TEMP_DIR/cli-agent-template"
else
    # Fallback to curl/wget if git is not available
    echo "Git not found, downloading as archive..."
    if command -v curl &> /dev/null; then
        curl -sL https://github.com/aget-framework/cli-agent-template/archive/main.tar.gz | tar xz -C "$TEMP_DIR"
        mv "$TEMP_DIR/cli-agent-template-main" "$TEMP_DIR/cli-agent-template"
    elif command -v wget &> /dev/null; then
        wget -qO- https://github.com/aget-framework/cli-agent-template/archive/main.tar.gz | tar xz -C "$TEMP_DIR"
        mv "$TEMP_DIR/cli-agent-template-main" "$TEMP_DIR/cli-agent-template"
    else
        echo "Error: Neither git, curl, nor wget is available."
        echo "Please install one of these tools and try again."
        exit 1
    fi
fi

echo "🔧 Installing template..."

# Run the installer
cd "$TEMP_DIR/cli-agent-template"
python3 installer/install.py "$TARGET_DIR" --template standard

echo ""
echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "  1. Review CLAUDE.md for available commands"
echo "  2. Tell your CLI agent to 'wake up' to start"
echo "  3. Customize patterns as needed"
echo ""
echo "For more information: https://github.com/aget-framework/cli-agent-template"