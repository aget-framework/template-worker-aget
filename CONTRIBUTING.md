# Contributing to CLI Agent Template

Thank you for your interest in contributing to CLI Agent Template! This project aims to make CLI coding agents better collaborators.

## How to Contribute

### Reporting Issues
- Check if the issue already exists
- Provide clear description and steps to reproduce
- Include your environment details (OS, Python version, CLI agent used)

### Submitting Pull Requests

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/cli-agent-template
   cd cli-agent-template
   ```

2. **Use the Patterns** (dogfooding!)
   ```bash
   # Tell your CLI agent to wake up
   # The repository uses its own patterns
   ```

3. **Make Changes**
   - Follow existing code style
   - Add tests for new patterns
   - Update documentation

4. **Test Your Changes**
   ```bash
   python3 scripts/housekeeping_protocol.py sanity-check
   python3 scripts/housekeeping_protocol.py documentation-check
   ```

5. **Submit PR**
   - Clear description of changes
   - Reference any related issues
   - Ensure all tests pass

## Pattern Development Guidelines

### Creating New Patterns

1. **Location**: Place in `patterns/<category>/<pattern_name>.py`
2. **Documentation**: Include `README.md` in pattern directory
3. **Safety**: Always implement dry-run mode
4. **Testing**: Add tests in `tests/test_<pattern_name>.py`

### Pattern Requirements

- Must work standalone and integrated
- Include natural language triggers
- Implement progressive safety levels
- Maintain backward compatibility

## Code Style

- Python 3.8+ compatible
- Follow PEP 8
- Use type hints where appropriate
- Clear docstrings for public functions

## Testing

Run tests before submitting:
```bash
python3 -m pytest tests/ -v
```

## Documentation

- Update README.md for user-facing changes
- Update pattern README files
- Keep CLAUDE.md in sync with available commands

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue for discussion before implementing major changes.