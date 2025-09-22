# CLI Agent Template

Transform any codebase into a CLI coding agent-ready collaborative environment.

## What This Is

Reusable patterns and templates that enable natural language workflows for CLI coding agents like Claude Code, Cursor, Aider, and Windsurf.

## Quick Start

```bash
# Method 1: Install in existing project
curl -sSL https://raw.githubusercontent.com/aget-framework/cli-agent-template/main/install.sh | bash

# Method 2: Clone and customize
git clone https://github.com/aget-framework/cli-agent-template
cd your-project
python ../cli-agent-template/installer/install.py . --template standard
```

## What You Get

After installation, your CLI agent can understand commands like:

- **`wake up`** - Initialize session with project status
- **`housekeeping`** - Clean temporary files and caches
- **`spring clean`** - Deep cleanup with archiving
- **`documentation check`** - Analyze documentation quality
- **`sanity check`** - Emergency diagnostics when something's wrong
- **`wind down`** - Save session state and commit changes
- **`sign off`** - Quick commit and push

## Features

✅ **Natural Language Commands** - Conversational interface for common tasks
✅ **Progressive Safety** - Dry-run → Modify → Reorganize
✅ **Session Management** - Context preservation across conversations
✅ **Emergency Recovery** - Diagnostic and recovery protocols
✅ **Documentation as Code** - Quality checks and auto-fixes
✅ **Git Integration** - Smart commits, checkpoints, and rollbacks

## Templates

### Minimal
Basic setup with session management only. Perfect for small projects.

```bash
python installer/install.py . --template minimal
```

### Standard (Recommended)
Full conversational interface with housekeeping and documentation checks.

```bash
python installer/install.py . --template standard
```

### Advanced
Everything including CI/CD integration, advanced testing, and compliance checks.

```bash
python installer/install.py . --template advanced
```

## Supported CLI Agents

- [Claude Code](https://claude.ai/code) (Primary target)
- [Cursor](https://cursor.sh)
- [Aider](https://aider.chat)
- [Windsurf](https://codeium.com/windsurf)
- [Mentat](https://github.com/AbanteAI/mentat)
- Any CLI-based AI coding assistant

## Project Structure

```
your-project/
├── AGENT.md                  # Universal agent configuration
├── CLAUDE.md                 # Symlink to AGENT.md (backward compatibility)
├── Makefile                  # Common tasks as make targets
├── scripts/
│   ├── session_protocol.py   # Wake up, wind down, sign off
│   ├── housekeeping_protocol.py  # Cleaning and organization
│   └── sanity_check.py      # Emergency diagnostics
└── .cli-agent.yaml          # Template configuration
```

## How It Works

1. **Agent reads AGENT.md** - Understands available commands and project context
2. **Natural language triggers** - You say "wake up", agent runs the protocol
3. **Progressive automation** - Safe operations first, destructive only with confirmation
4. **Context preservation** - Session state maintained across conversations

## Examples

### Starting a Session
```
You: wake up
Agent: Running wake protocol...
       ✓ Working directory: /Users/you/project
       ✓ Git status: 3 uncommitted changes
       ✓ Tests: 47 passing
       ✓ Documentation: Grade B
       Ready for tasks.
```

### Cleaning Up
```
You: spring clean
Agent: Running spring clean protocol (dry-run)...
       Would archive 5 old session notes
       Would remove 127 __pycache__ files
       Would clean 3.2MB temp files
       Run without --dry-run to execute.
```

### Emergency Recovery
```
You: sanity check
Agent: Running emergency diagnostics...
       ✓ Python 3.11.0
       ✓ Git repository OK
       ✓ Critical files present
       ✓ Imports working
       System Status: OK
```

## Contributing

This repository dogfoods its own patterns. To contribute:

1. Fork and clone
2. Say "wake up" to your CLI agent
3. Make changes following existing patterns
4. Say "test templates" to run tests
5. Say "wind down" to save your session
6. Submit a pull request

## Pattern Development

To add a new pattern:

1. Create in `patterns/<category>/<pattern_name>.py`
2. Add tests in `tests/test_<pattern_name>.py`
3. Document in `patterns/<category>/README.md`
4. Update the installer to include it

## Versioning

This project uses semantic versioning. Each pattern has its own version number, allowing selective updates.

## License

MIT - See [LICENSE](LICENSE) file

## Acknowledgments

Patterns evolved from real-world usage in production codebases, especially the RKB content enhancement project.

---

*Making CLI coding agents better collaborators, one pattern at a time.*