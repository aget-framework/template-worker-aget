# Housekeeping Pattern

Provides cleanup and organization commands for maintaining healthy codebases.

## Commands

- `housekeeping` - Light cleanup (temp files, caches)
- `spring-clean` - Deep cleanup with archiving
- `documentation-check` - Analyze documentation quality
- `sanity-check` - Emergency diagnostics

## Usage

```python
# Always run with --dry-run first
python3 scripts/housekeeping_protocol.py housekeeping --dry-run
python3 scripts/housekeeping_protocol.py spring-clean --dry-run

# Then execute if satisfied
python3 scripts/housekeeping_protocol.py housekeeping --no-dry-run
```

## Safety Features

- Dry-run mode by default
- Progressive intervention levels
- Git status checks before major operations