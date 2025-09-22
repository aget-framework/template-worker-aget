# {{PROJECT_NAME}} - Universal Agent Configuration

## Agent Compatibility
This configuration follows the AGENTS.md open-source standard for universal agent configuration.
Works with Claude Code, Cursor, Aider, Windsurf, and other CLI coding agents.
**Note**: CLAUDE.md is a symlink to this file for backward compatibility.

## Project Context
This project uses CLI Agent Template for conversational development workflows.

## Session Management Commands

### Wake Up
When user says "wake up", immediately execute:
- Read AGENTS.md (this file)
- Run: `python3 scripts/session_protocol.py wake`
- Report project status
- End with "Ready for tasks."

### Wind Down
When user says "wind down", execute:
- Run: `python3 scripts/session_protocol.py wind-down`
- Commit changes and save session state
- Report "Session preserved."

### Sign Off
When user says "sign off", execute:
- Run: `python3 scripts/session_protocol.py sign-off`
- Quick commit and push
- Report "Signed off."

## Project Information
- **Name**: {{PROJECT_NAME}}
- **Type**: {{PROJECT_TYPE}}
- **Path**: {{PROJECT_PATH}}

## Important Notes
- Always run commands exactly as specified
- Maintain conversation context across commands
- Report command outputs clearly