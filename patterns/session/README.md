# Session Management Patterns

Patterns for managing development sessions across CLI agent conversations.

## Available Patterns

### wake_up
**Trigger**: "wake up"
**Purpose**: Initialize a new development session
**Actions**:
- Display working directory and git status
- Show recent session history
- List available patterns
- Report test status
- Check documentation grade

### wind_down
**Trigger**: "wind down"
**Purpose**: Gracefully end a development session
**Actions**:
- Commit all changes with descriptive message
- Create session notes with summary
- Run test suite
- Update session metrics
- Archive old session notes (>30 days)

### sign_off
**Trigger**: "sign off"
**Purpose**: Quick save and push
**Actions**:
- Fast commit with timestamp
- Push to remote repository
- Update session state
- No tests or extensive checks

## Usage Examples

```bash
# Start your day
You: wake up
Agent: [Shows project status, recent changes, ready for work]

# Take a break
You: wind down
Agent: [Commits changes, saves notes, runs tests]

# End of day
You: sign off
Agent: [Quick commit and push]
```

## State Management

Session state is persisted in `.session_state.json`:
```json
{
  "session_count": 42,
  "total_commits": 156,
  "last_session_time": "2025-09-21T10:30:00",
  "last_session_end": "2025-09-21T18:45:00",
  "project_created": "2025-09-01T08:00:00"
}
```

## Session Notes

Session notes are organized by date:
```
SESSION_NOTES/
├── 2025-09-21/
│   ├── session_1030.md
│   └── session_1845.md
└── archive/
    └── 2025-08-15/
```

## Customization

Edit `scripts/session_protocol.py` to:
- Add custom status checks
- Modify commit message format
- Change session note template
- Add project-specific commands

## Integration Points

- **Git**: Automatic commits and pushes
- **Testing**: Runs test suite on wind-down
- **Documentation**: Checks documentation quality
- **Metrics**: Tracks session duration and productivity