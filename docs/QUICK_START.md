# Quick Start Guide

## 30-Second Setup

```bash
# In your project directory
curl -sSL https://raw.githubusercontent.com/gmelli/cli-agent-template/main/install.sh | bash
```

## First Commands to Try

### 1. Start Your Session
```
You: wake up
Agent: [Shows project status, ready for work]
```

### 2. Check Project Health
```
You: sanity check
Agent: [Runs diagnostics, reports any issues]
```

### 3. Clean Up
```
You: housekeeping
Agent: [Shows what would be cleaned, asks confirmation]
```

### 4. End Your Session
```
You: wind down
Agent: [Commits changes, saves session notes]
```

## What Gets Installed

```
your-project/
├── CLAUDE.md                    # Commands your agent understands
├── scripts/
│   ├── session_protocol.py      # Wake/wind-down/sign-off
│   └── housekeeping_protocol.py # Cleaning and diagnostics
└── Makefile                     # Shortcuts (make wake, make test)
```

## Template Levels

### Minimal (Beginners)
Just session management - perfect for small projects
```bash
python installer/install.py . --template minimal
```

### Standard (Recommended)
Full housekeeping suite - ideal for most projects
```bash
python installer/install.py . --template standard
```

### Advanced (Power Users)
Everything including CI/CD - for production projects
```bash
python installer/install.py . --template advanced
```

## Customization

### Change Triggers
Edit `CLAUDE.md` to add your own commands:
```markdown
### Deploy to Production
When user says "deploy", execute:
- Run: `./scripts/deploy.sh`
```

### Add Patterns
Drop new scripts in `scripts/` directory:
```python
# scripts/my_custom_protocol.py
def my_command():
    print("Running custom command...")
```

## Common Issues

### "Command not found"
Make sure Python 3.8+ is installed:
```bash
python3 --version
```

### "Permission denied"
Make scripts executable:
```bash
chmod +x scripts/*.py
```

### "Git not configured"
Templates work without git, but it's recommended:
```bash
git init
```

## Next Steps

1. Read [WHY_THIS_MATTERS.md](WHY_THIS_MATTERS.md) for deeper understanding
2. Check [examples/](../examples/) for real-world usage
3. Join discussions on [GitHub Issues](https://github.com/gmelli/cli-agent-template/issues)