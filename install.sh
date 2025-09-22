#!/bin/bash
# CLI Agent Template Installer
# Universal installer that works with curl or direct execution
# Usage: curl -sSL https://raw.githubusercontent.com/USER/REPO/main/install.sh | bash
#    or: ./install.sh

set -e  # Exit on error

# Configuration with sensible defaults
GITHUB_USER="${GITHUB_USER:-aget-framework}"
REPO_NAME="${REPO_NAME:-cli-agent-template}"
BRANCH="${BRANCH:-main}"
INSTALL_DIR="${1:-.}"
TEMPLATE="${2:-standard}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
print_error() {
    echo -e "${RED}❌ Error: $1${NC}" >&2
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ️  $1${NC}"
}

# Phase 1: Prerequisites Check
check_prerequisites() {
    print_info "Checking prerequisites..."

    # Check Python 3.8+
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed"
        exit 1
    fi

    python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    if (( $(echo "$python_version < 3.8" | bc -l) )); then
        print_error "Python 3.8+ required (found $python_version)"
        exit 1
    fi
    print_success "Python $python_version detected"

    # Check Git (optional but recommended)
    if command -v git &> /dev/null; then
        print_success "Git detected"
    else
        print_info "Git not found (optional but recommended)"
    fi

    # Check target directory
    if [ ! -d "$INSTALL_DIR" ]; then
        print_error "Target directory $INSTALL_DIR does not exist"
        exit 1
    fi

    if [ ! -w "$INSTALL_DIR" ]; then
        print_error "No write permission for $INSTALL_DIR"
        exit 1
    fi
    print_success "Target directory verified"

    # Check for conflicts
    if [ -f "$INSTALL_DIR/AGENT.md" ] && [ ! -L "$INSTALL_DIR/CLAUDE.md" ]; then
        print_info "Existing AGENT.md found - will backup if needed"
    fi
}

# Phase 2: Download and Install
download_and_install() {
    print_info "Downloading CLI Agent Template..."

    # Create temporary directory
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT

    # Download repository
    cd "$TEMP_DIR"
    if command -v git &> /dev/null; then
        git clone --quiet --depth 1 --branch "$BRANCH" \
            "https://github.com/${GITHUB_USER}/${REPO_NAME}.git" template
    else
        # Fallback to curl/wget for tarball
        ARCHIVE_URL="https://github.com/${GITHUB_USER}/${REPO_NAME}/archive/refs/heads/${BRANCH}.tar.gz"
        if command -v curl &> /dev/null; then
            curl -sL "$ARCHIVE_URL" | tar xz
        elif command -v wget &> /dev/null; then
            wget -qO- "$ARCHIVE_URL" | tar xz
        else
            print_error "Neither git, curl, nor wget found. Cannot download."
            exit 1
        fi
        mv "${REPO_NAME}-${BRANCH}" template
    fi

    print_success "Repository downloaded"

    # Run Python installer
    cd template
    print_info "Installing template: $TEMPLATE"

    # Create manifest for tracking
    echo "# Installation Manifest - $(date)" > "$TEMP_DIR/install_manifest.txt"
    echo "# This file tracks what was installed for potential rollback" >> "$TEMP_DIR/install_manifest.txt"

    # Run the Python installer and capture output
    if python3 installer/install.py "$INSTALL_DIR" --template "$TEMPLATE" 2>&1 | tee "$TEMP_DIR/install_log.txt"; then
        print_success "Installation completed"

        # Parse installed files from log
        grep -E "(Creating|Copying|Installing)" "$TEMP_DIR/install_log.txt" | \
            sed 's/.*[Creating|Copying|Installing] //' >> "$TEMP_DIR/install_manifest.txt"

        # Copy manifest to target
        cp "$TEMP_DIR/install_manifest.txt" "$INSTALL_DIR/.install_manifest"
    else
        print_error "Installation failed"
        exit 1
    fi
}

# Phase 3: Post-Install Verification
verify_installation() {
    print_info "Verifying installation..."

    cd "$INSTALL_DIR"
    VERIFY_FAILED=0

    # Check core files exist
    for file in "AGENT.md" "scripts/session_protocol.py" "scripts/housekeeping_protocol.py"; do
        if [ ! -f "$file" ]; then
            print_error "Missing: $file"
            VERIFY_FAILED=1
        fi
    done

    # Check CLAUDE.md symlink or copy
    if [ ! -e "CLAUDE.md" ]; then
        print_error "CLAUDE.md not created"
        VERIFY_FAILED=1
    fi

    # Test basic command
    if python3 scripts/session_protocol.py status &> /dev/null; then
        print_success "Session protocol verified"
    else
        print_error "Session protocol test failed"
        VERIFY_FAILED=1
    fi

    # Test Python imports
    if python3 -c "import scripts.session_protocol" &> /dev/null; then
        print_success "Python imports verified"
    else
        # This is okay - scripts might not be a package
        print_info "Scripts run as standalone (not as package)"
    fi

    return $VERIFY_FAILED
}

# Phase 4: Rollback on Failure
rollback_installation() {
    print_error "Installation verification failed. Rolling back..."

    if [ -f "$INSTALL_DIR/.install_manifest" ]; then
        while IFS= read -r file; do
            if [[ ! "$file" =~ ^# ]] && [ -n "$file" ]; then
                rm -f "$INSTALL_DIR/$file" 2>/dev/null || true
            fi
        done < "$INSTALL_DIR/.install_manifest"
        rm "$INSTALL_DIR/.install_manifest"
    fi

    print_info "Rollback completed"
}

# Phase 5: Success Report
report_success() {
    echo ""
    echo "════════════════════════════════════════════════════════════"
    print_success "CLI Agent Template installed successfully!"
    echo "════════════════════════════════════════════════════════════"
    echo ""
    echo "📁 Installation location: $INSTALL_DIR"
    echo "📦 Template type: $TEMPLATE"
    echo ""
    echo "🚀 Next steps:"
    echo "   1. Open your CLI coding agent (Claude, Cursor, Aider, etc.)"
    echo "   2. Tell it to: \"wake up\""
    echo "   3. The agent will read AGENT.md and be ready to help"
    echo ""
    echo "📚 Available commands:"
    echo "   • wake up         - Start a session"
    echo "   • wind down       - Save work and create session notes"
    echo "   • sign off        - Quick commit and push"
    echo "   • sanity check    - Run diagnostics"
    echo "   • housekeeping    - Clean up project files"
    echo ""
    echo "💡 For more information:"
    echo "   • Read: $INSTALL_DIR/AGENT.md"
    echo "   • Docs: $INSTALL_DIR/docs/"
    echo ""
}

# Main execution
main() {
    echo "CLI Agent Template Installer v1.0"
    echo "=================================="
    echo ""

    # Run installation phases
    check_prerequisites
    download_and_install

    if verify_installation; then
        report_success
    else
        rollback_installation
        exit 1
    fi
}

# Handle both piped and direct execution
if [ -t 0 ]; then
    # Direct execution
    main "$@"
else
    # Piped from curl
    # Save script and execute
    SCRIPT_TEMP=$(mktemp)
    cat > "$SCRIPT_TEMP"
    bash "$SCRIPT_TEMP" "$@"
    rm "$SCRIPT_TEMP"
fi