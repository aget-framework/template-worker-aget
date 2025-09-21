#!/usr/bin/env python3
"""
Tests for session protocol functionality
"""

import sys
import os
from pathlib import Path
import subprocess
import tempfile
import shutil

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_wake_command_exists():
    """Test that wake command is callable"""
    result = subprocess.run(
        [sys.executable, 'scripts/session_protocol.py', 'wake'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Wake Up" in result.stdout
    assert "Ready for tasks" in result.stdout


def test_session_protocol_imports():
    """Test that session protocol can be imported"""
    from scripts import session_protocol
    assert hasattr(session_protocol, 'wake')
    assert hasattr(session_protocol, 'wind_down')
    assert hasattr(session_protocol, 'sign_off')


def test_wake_output_format():
    """Test that wake produces expected output format"""
    result = subprocess.run(
        [sys.executable, 'scripts/session_protocol.py', 'wake'],
        capture_output=True,
        text=True
    )

    # Check for expected elements
    assert "📍" in result.stdout  # Location marker
    assert "📦" in result.stdout  # Patterns marker
    assert "📄" in result.stdout  # Templates marker
    assert "✅" in result.stdout  # Ready marker


def test_invalid_command():
    """Test that invalid command returns error"""
    result = subprocess.run(
        [sys.executable, 'scripts/session_protocol.py', 'invalid'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 1
    assert "Unknown command" in result.stdout


def test_pattern_detection():
    """Test that patterns are detected correctly"""
    # Create a temporary patterns directory
    with tempfile.TemporaryDirectory() as tmpdir:
        patterns_dir = Path(tmpdir) / 'patterns'
        patterns_dir.mkdir()

        # Create pattern subdirectories
        for pattern in ['session', 'housekeeping']:
            (patterns_dir / pattern).mkdir()
            (patterns_dir / pattern / 'README.md').touch()

        # Run wake in the temp directory
        original_cwd = os.getcwd()
        try:
            os.chdir(tmpdir)
            result = subprocess.run(
                [sys.executable, Path(original_cwd) / 'scripts' / 'session_protocol.py', 'wake'],
                capture_output=True,
                text=True
            )

            # Should detect the patterns we created
            assert "session" in result.stdout or "housekeeping" in result.stdout

        finally:
            os.chdir(original_cwd)


if __name__ == '__main__':
    # Simple test runner for manual testing
    import pytest
    pytest.main([__file__, '-v'])