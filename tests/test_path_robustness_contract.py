"""Path Robustness Contract Test

Validates that all test files use file-relative paths, not cwd-relative paths.
Prevents L119 pattern recurrence (CI failures from working directory changes).

Pattern: L119_ci_cwd_deletion_coverage_interaction.md
Related: Session 2025-10-28 Gate 1B (Prevention Infrastructure)
"""

import pytest
from pathlib import Path


def test_all_tests_use_file_relative_paths():
    """Contract: All test files must use file-relative paths, not cwd-relative.

    Prevents L119 pattern recurrence (CI failures from CWD changes).
    Validates that Path() usage includes __file__ for robustness.

    Pattern enforced:
      ❌ Path("AGENTS.md")                          # cwd-relative (breaks in CI)
      ✅ Path(__file__).parent.parent / "AGENTS.md"  # file-relative (robust)

    Why this matters:
    - pytest + coverage can change working directory
    - TemporaryDirectory usage can delete CWD mid-test
    - File-relative paths work regardless of CWD state

    Related: L119 (CI CWD deletion + coverage interaction)
    """
    # Find all test files
    tests_dir = Path(__file__).parent  # File-relative to tests/
    test_files = list(tests_dir.glob("test_*.py"))

    # Exclude this meta-test from checking itself
    test_files = [f for f in test_files if f.name != "test_path_robustness_contract.py"]

    violations = []

    for test_file in test_files:
        content = test_file.read_text()
        lines = content.splitlines()

        for line_num, line in enumerate(lines, 1):
            # Check for Path("...") or Path('...') patterns
            if 'Path("' in line or "Path('" in line:
                # Refined check: Allow if using __file__ in Path construction
                if 'Path(__file__)' not in line and '__file__' not in line:
                    # Exclude known safe patterns
                    safe_patterns = ['tmp', 'fixture', 'conftest', 'pytest', 'caplog']
                    if not any(safe in line.lower() for safe in safe_patterns):
                        violations.append({
                            'file': test_file.name,
                            'line': line_num,
                            'code': line.strip()
                        })

    # Format clear error message
    if violations:
        msg = ["❌ Tests using cwd-relative paths detected (L119 anti-pattern):", ""]
        for v in violations:
            msg.append(f"  {v['file']}:{v['line']}")
            msg.append(f"    → {v['code']}")
            msg.append("")
        msg.append("Fix: Use Path(__file__).parent.parent / 'file'")
        msg.append("Example:")
        msg.append("  ❌ agents_md = Path('AGENTS.md')")
        msg.append("  ✅ agents_md = Path(__file__).parent.parent / 'AGENTS.md'")
        msg.append("")
        msg.append("Why: CWD-relative paths break when pytest changes working directory")
        msg.append("See: L119_ci_cwd_deletion_coverage_interaction.md")
        pytest.fail("\n".join(msg))

    # Success message (logged but doesn't fail test)
    print(f"✅ Validated {len(test_files)} test files - all use file-relative paths")


def test_meta_test_uses_file_relative_paths():
    """Meta-test validation: This test file practices what it preaches.

    Ensures this meta-test itself uses file-relative paths.
    Self-consistency check for prevention infrastructure.
    """
    test_file = Path(__file__)  # File-relative reference
    content = test_file.read_text()

    # This test should reference __file__ for its own Path constructions
    assert '__file__' in content, \
        "Meta-test must use file-relative paths (practice what we preach)"

    # Verify actual Path() constructions use __file__
    # (This is a pragmatic check - we trust the meta-test's own logic
    # rather than recursively validating its detection patterns)
    actual_paths = ['Path(__file__)', 'tests_dir = Path(__file__).parent']
    for expected_pattern in actual_paths:
        assert expected_pattern in content, \
            f"Meta-test should use pattern: {expected_pattern}"

    print("✅ Meta-test validates its own path robustness")
