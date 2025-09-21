#!/usr/bin/env python3
"""
Session Protocol for CLI Agent Template
This repository uses its own patterns (dogfooding)
"""

import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

# ANSI color codes
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'


def run_command(cmd, check=False):
    """Run command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def wake():
    """Wake up protocol - Initialize session"""
    print(f"{BOLD}{BLUE}## Wake Up - {datetime.now():%Y-%m-%d %H:%M}{RESET}")

    # Show current directory
    cwd = Path.cwd()
    print(f"📍 {cwd}")

    # Check git status
    git_status = run_command("git status --short")
    if git_status:
        change_count = len(git_status.split('\n'))
        print(f"🔄 {change_count} uncommitted changes")
    else:
        print(f"{GREEN}✓ Git repository clean{RESET}")

    # Check pattern status
    pattern_dirs = ['session', 'housekeeping', 'documentation', 'recovery']
    patterns_found = []
    for pattern in pattern_dirs:
        pattern_path = cwd / 'patterns' / pattern
        if pattern_path.exists() and any(pattern_path.glob('*.py')):
            patterns_found.append(pattern)

    print(f"📦 Patterns available: {', '.join(patterns_found)}")

    # Check templates
    template_dirs = ['minimal', 'standard', 'advanced']
    templates_found = []
    for template in template_dirs:
        template_path = cwd / 'templates' / template
        if template_path.exists():
            templates_found.append(template)

    print(f"📄 Templates: {', '.join(templates_found)}")

    # Check if tests exist
    test_count = len(list((cwd / 'tests').glob('test_*.py'))) if (cwd / 'tests').exists() else 0
    if test_count > 0:
        print(f"🧪 Tests: {test_count} test files found")

    print(f"{GREEN}✅ Ready for tasks.{RESET}")


def wind_down():
    """Wind down protocol - Save session state"""
    print(f"{BOLD}{BLUE}## Wind Down - {datetime.now():%Y-%m-%d %H:%M}{RESET}")

    # Check for uncommitted changes
    git_status = run_command("git status --short")

    if git_status:
        print("📝 Committing changes...")
        run_command("git add -A")

        # Create commit message
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        commit_msg = f"session: Wind down at {timestamp}"

        run_command(f'git commit -m "{commit_msg}"')
        print(f"{GREEN}✓ Changes committed{RESET}")
    else:
        print("✓ No changes to commit")

    # Run tests if they exist
    if Path('tests').exists():
        print("🧪 Running tests...")
        result = run_command("python -m pytest tests/ -q")
        if result:
            print(f"{GREEN}✓ Tests passed{RESET}")
        else:
            print(f"{YELLOW}⚠ Some tests may have failed{RESET}")

    # Create session note
    session_dir = Path('SESSION_NOTES')
    session_dir.mkdir(exist_ok=True)

    session_file = session_dir / f"session_{datetime.now():%Y%m%d_%H%M}.md"
    with open(session_file, 'w') as f:
        f.write(f"# Session Notes - {datetime.now():%Y-%m-%d %H:%M}\n\n")
        f.write(f"## Status\n")
        f.write(f"- Working directory: {Path.cwd()}\n")
        f.write(f"- Git status: {'Clean' if not git_status else 'Changes committed'}\n")
        f.write(f"- Patterns: {len(list(Path('patterns').glob('*/*.py'))) if Path('patterns').exists() else 0} files\n")
        f.write(f"- Tests: {len(list(Path('tests').glob('test_*.py'))) if Path('tests').exists() else 0} files\n")

    print(f"📝 Session note: {session_file.name}")
    print(f"{GREEN}✅ Session preserved.{RESET}")


def sign_off():
    """Sign off protocol - Quick commit and push"""
    print(f"{BOLD}{BLUE}## Sign Off - {datetime.now():%Y-%m-%d %H:%M}{RESET}")

    # Quick commit
    git_status = run_command("git status --short")

    if git_status:
        run_command("git add -A")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        run_command(f'git commit -m "chore: Quick sign off at {timestamp}"')
        print(f"{GREEN}✓ Changes committed{RESET}")

    # Check if we have a remote
    remote = run_command("git remote -v")
    if remote and 'origin' in remote:
        print("📤 Pushing to remote...")
        result = run_command("git push origin main 2>&1")
        if result and 'error' not in result.lower():
            print(f"{GREEN}✓ Pushed to origin/main{RESET}")
        else:
            # Try master branch
            result = run_command("git push origin master 2>&1")
            if result and 'error' not in result.lower():
                print(f"{GREEN}✓ Pushed to origin/master{RESET}")
            else:
                print(f"{YELLOW}⚠ Push skipped (no remote configured or branch not set){RESET}")
    else:
        print("ℹ No remote configured")

    print(f"{GREEN}✅ Signed off.{RESET}")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [wake|wind-down|sign-off]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'wake':
        wake()
    elif command == 'wind-down':
        wind_down()
    elif command == 'sign-off':
        sign_off()
    else:
        print(f"{RED}Unknown command: {command}{RESET}")
        print("Valid commands: wake, wind-down, sign-off")
        sys.exit(1)


if __name__ == '__main__':
    main()