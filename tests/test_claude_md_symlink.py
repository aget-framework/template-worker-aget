"""
CLAUDE.md Symlink Contract Test

Validates that CLAUDE.md exists as a symlink to AGENTS.md for
backward compatibility with older Claude Code versions.

Pattern: L98 (Agent Creation Lessons)
Requirement: New Agent Creation Policy (Step 2a)
"""

import pytest
from pathlib import Path


def test_claude_md_exists():
    """CLAUDE.md file must exist in root directory."""
    claude_md = Path("CLAUDE.md")
    assert claude_md.exists(), \
        "CLAUDE.md not found. Run: ln -s AGENTS.md CLAUDE.md"


def test_claude_md_is_symlink():
    """CLAUDE.md must be a symlink, not a regular file."""
    claude_md = Path("CLAUDE.md")

    if not claude_md.exists():
        pytest.skip("CLAUDE.md does not exist")

    assert claude_md.is_symlink(), \
        "CLAUDE.md exists but is not a symlink. " \
        "Remove it and run: ln -s AGENTS.md CLAUDE.md"


def test_claude_md_points_to_agents_md():
    """CLAUDE.md symlink must point to AGENTS.md."""
    claude_md = Path("CLAUDE.md")

    if not claude_md.exists():
        pytest.skip("CLAUDE.md does not exist")

    if not claude_md.is_symlink():
        pytest.skip("CLAUDE.md is not a symlink")

    target = claude_md.resolve().name
    assert target == "AGENTS.md", \
        f"CLAUDE.md points to {target}, expected AGENTS.md. " \
        f"Fix: rm CLAUDE.md && ln -s AGENTS.md CLAUDE.md"


def test_agents_md_exists():
    """AGENTS.md must exist (target of CLAUDE.md symlink)."""
    agents_md = Path("AGENTS.md")
    assert agents_md.exists(), \
        "AGENTS.md not found. Cannot create CLAUDE.md symlink without target."


def test_symlink_not_broken():
    """CLAUDE.md symlink must not be broken (target must exist)."""
    claude_md = Path("CLAUDE.md")

    if not claude_md.exists():
        pytest.skip("CLAUDE.md does not exist")

    if not claude_md.is_symlink():
        pytest.skip("CLAUDE.md is not a symlink")

    # Try to resolve the symlink
    try:
        resolved = claude_md.resolve(strict=True)
        assert resolved.exists(), \
            f"CLAUDE.md symlink is broken (points to non-existent file)"
    except (FileNotFoundError, RuntimeError) as e:
        pytest.fail(f"CLAUDE.md symlink is broken: {e}")


def test_backward_compatibility_note():
    """AGENTS.md should mention CLAUDE.md symlink for backward compatibility."""
    agents_md = Path("AGENTS.md")

    if not agents_md.exists():
        pytest.skip("AGENTS.md does not exist")

    content = agents_md.read_text()

    # Check for backward compatibility note
    has_note = (
        "CLAUDE.md" in content and
        ("symlink" in content.lower() or "backward" in content.lower())
    )

    if not has_note:
        pytest.warn(
            UserWarning(
                "AGENTS.md should mention CLAUDE.md symlink for backward compatibility. "
                "Add note like: '**Note**: CLAUDE.md is a symlink to this file for backward compatibility.'"
            )
        )
