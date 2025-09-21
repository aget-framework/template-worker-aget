# Session Management Pattern

Provides wake up, wind down, and sign off protocols for CLI agent sessions.

## Commands

- `wake` - Initialize session with project status
- `wind-down` - Save session state and commit changes
- `sign-off` - Quick commit and push

## Usage

```python
python3 scripts/session_protocol.py wake
python3 scripts/session_protocol.py wind-down
python3 scripts/session_protocol.py sign-off
```

## Customization

Edit `session_protocol.py` to add project-specific status checks.