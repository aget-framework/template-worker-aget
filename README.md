# CLI Agent Template

A reference implementation of the [CLI Agent Template Framework](https://www.aget-framework.com/RKB/CLI_Agent_Template_Framework) - transform any codebase into a CLI coding agent-ready collaborative environment through conversational command patterns.

## What This Is

This repository provides a [workflow automation framework](https://www.aget-framework.com/RKB/CLI_Agent_Template_Framework) with reusable patterns and templates that enable natural language workflows for CLI coding agents like Claude Code, Cursor, Aider, and Windsurf. It implements conversational command patterns that allow AI coding assistants to execute development workflows through natural language interfaces.

## Quick Start

```bash
# Method 1: Install in existing project (now with self-verifying installer)
curl -sSL https://raw.githubusercontent.com/aget-framework/cli-agent-template/main/install.sh | bash

# Method 2: Clone and customize
git clone https://github.com/aget-framework/cli-agent-template
cd your-project
python3 ../cli-agent-template/installer/install.py . --template standard
```

## Why Universal Standards?

### The Configuration Fragmentation Problem

The current landscape of AI coding assistants has created a significant maintenance burden for development teams. Each tool requires its own configuration format:

- **Claude Code**: Reads `CLAUDE.md` for agent-specific instructions
- **Cursor**: Requires `.cursorrules` for behavior configuration
- **Windsurf**: Uses `.windsurfrules` for custom patterns
- **Aider**: Expects `.aider.conf.yml` for settings
- **GitHub Copilot**: Uses `.github/copilot-instructions.md`

This fragmentation forces teams to maintain multiple configuration files with largely duplicated content. A typical multi-tool setup requires developers to synchronize changes across 3-5 different configuration formats, increasing the risk of inconsistencies and configuration drift.

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

### Minimal (5 patterns)
Basic setup with session management only. Perfect for small projects.

```bash
curl -sSL https://raw.githubusercontent.com/aget-framework/cli-agent-template/main/install.sh | bash -s . minimal
```

### Standard (15+ patterns) - Recommended
Full conversational interface with housekeeping and documentation checks.

```bash
curl -sSL https://raw.githubusercontent.com/aget-framework/cli-agent-template/main/install.sh | bash
```

### Advanced (25+ patterns)
Everything including CI/CD integration, advanced testing, and compliance checks.

```bash
curl -sSL https://raw.githubusercontent.com/aget-framework/cli-agent-template/main/install.sh | bash -s . advanced
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
├── AGENTS.md                 # Universal agent configuration (AGENTS.md specification)
├── CLAUDE.md                 # Symlink to AGENT.md (backward compatibility)
├── scripts/
│   ├── session_protocol.py   # Wake up, wind down, sign off
│   ├── housekeeping_protocol.py  # Cleaning and organization
│   └── recovery_protocol.py  # Emergency diagnostics
├── patterns/                 # Reusable workflow patterns
│   ├── session/             # Session management patterns
│   ├── housekeeping/        # Maintenance patterns
│   └── documentation/       # Documentation patterns
└── .session_state.json      # Session persistence
```

## How It Works

1. **Agent reads AGENTS.md** - Discovers available conversational command patterns
2. **Pattern discovery** - Agent automatically identifies workflow patterns from configuration
3. **Natural language triggers** - You say "wake up", agent executes the corresponding pattern
4. **Safe-by-default** - Dry-run previews, rollback support, confirmation prompts
5. **Session persistence** - Context preservation across agent restarts

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

## Documentation

- [Quick Start Guide](docs/QUICK_START.md) - Get running in 30 seconds
- [Understanding Patterns](docs/PATTERNS_EXPLAINED.md) - Learn how patterns work
- [Why This Matters](docs/WHY_THIS_MATTERS.md) - The value proposition
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions
- [Framework Concept](https://www.aget-framework.com/RKB/CLI_Agent_Template_Framework) - Academic reference

## Contributing

This repository implements [dogfooding practices](https://www.aget-framework.com/RKB/CLI_Agent_Template_Framework) - it uses its own patterns for self-maintenance. To contribute:

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