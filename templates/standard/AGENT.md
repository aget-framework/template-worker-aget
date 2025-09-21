# {{PROJECT_NAME}} - Universal Agent Configuration

## Agent Compatibility
This configuration works with Claude Code, Cursor, Aider, Windsurf, and other CLI coding agents.
**Note**: CLAUDE.md is a symlink to this file for backward compatibility.

## Project Context
This project uses CLI Agent Template (Standard) for comprehensive development workflows.

## Session Management Commands

### Wake Up
When user says "wake up", immediately execute:
- Read AGENT.md (this file)
- Run: `python3 scripts/session_protocol.py wake`
- Report project status with git, tests, and documentation info
- End with "Ready for tasks."

### Wind Down
When user says "wind down", execute:
- Run: `python3 scripts/session_protocol.py wind-down`
- Commit changes, save session state, run tests
- Report "Session preserved."

### Sign Off
When user says "sign off", execute:
- Run: `python3 scripts/session_protocol.py sign-off`
- Quick commit and push to remote
- Report "Signed off."

## Housekeeping Commands

### Documentation Check
When user says "documentation check", execute:
- Run: `python3 scripts/housekeeping_protocol.py documentation-check`
- Analyze documentation quality (line counts, staleness, missing files)
- Report grade (A-F) and specific issues

### Housekeeping
When user says "housekeeping", execute:
- Run: `python3 scripts/housekeeping_protocol.py housekeeping --dry-run`
- Clean temporary files, caches, Python artifacts
- Show what would be removed, then ask for confirmation

### Spring Clean
When user says "spring clean", execute:
- Run: `python3 scripts/housekeeping_protocol.py spring-clean --dry-run`
- Deep cleanup: archive old files, remove duplicates, organize
- Always dry-run first, require explicit confirmation for actual execution

### Sanity Check
When user says "sanity check", execute:
- Run: `python3 scripts/housekeeping_protocol.py sanity-check`
- Emergency diagnostics: Python version, git status, dependencies
- Report system status: OK/DEGRADED/CRITICAL

## Project Information
- **Name**: {{PROJECT_NAME}}
- **Type**: {{PROJECT_TYPE}}
- **Path**: {{PROJECT_PATH}}
- **Test Command**: {{TEST_COMMAND}}

## Development Workflow

### Before Committing
1. Run tests: `{{TEST_COMMAND}}`
2. Check documentation: Say "documentation check"
3. Clean workspace: Say "housekeeping"

### When Something's Wrong
1. Say "sanity check" for diagnostics
2. Review the reported issues
3. Follow suggested fixes

## Important Notes
- All housekeeping commands default to dry-run for safety
- Session state is preserved in SESSION_NOTES/ directory
- Git commits follow conventional format: type: description
- Always maintain clean git history