# Changelog

All notable changes to AGET (CLI Agent Template) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Self-verifying `install.sh` script with rollback support
- Comprehensive pattern documentation in `patterns/*/README.md`
- `PATTERNS_EXPLAINED.md` guide explaining pattern architecture
- `CONTRIBUTING.md` with development guidelines
- Pattern categories: session, housekeeping, documentation, recovery
- Reference to academic [CLI Agent Template Framework](https://www.gabormelli.com/RKB/CLI_Agent_Template_Framework) concept

### Changed
- Updated all documentation to use consistent AGENTS.md naming
- Replaced arbitrary "30 minutes saved" claims with measurable benefits
- Improved installation commands across all documentation
- Enhanced README with framework references and proper structure

### Fixed
- Inconsistent AGENT.md vs AGENTS.md references
- Non-existent curl installer URL in documentation
- Missing pattern context in documentation
- Incorrect Python command variations (python vs python3)

## [1.0.0] - 2025-09-21

### Added
- Initial release of CLI Agent Template Framework
- Core patterns: wake up, wind down, sign off
- Housekeeping protocols: housekeeping, spring clean, sanity check
- Documentation quality checker with A-F grading
- Session state persistence with `.session_state.json`
- Session notes organization in `SESSION_NOTES/` directory
- Universal AGENTS.md configuration standard
- Backward compatibility with CLAUDE.md via symlink
- Three template levels: minimal (5 patterns), standard (15+), advanced (25+)
- Python-based installer with template selection
- Comprehensive test suite
- Documentation suite: Quick Start, Why This Matters, Troubleshooting

### Framework Features
- Conversational command patterns for natural language interfaces
- Pattern discovery mechanism for automatic command detection
- Safe-by-default operations with dry-run previews
- Self-documenting patterns with inline explanations
- Cross-tool compatibility (Claude Code, Cursor, Aider, Windsurf)
- Dogfooding practices - framework uses its own patterns

## [0.9.0] - 2025-09-15 (Pre-release)

### Added
- Initial proof of concept
- Basic session management
- Simple housekeeping functions
- Git integration

## Version History

- **1.0.0** - First stable release with complete pattern library
- **0.9.0** - Beta testing with early adopters
- **0.5.0** - Alpha version with core functionality
- **0.1.0** - Initial prototype

## Upgrade Guide

### From 0.9.x to 1.0.0

1. Update CLAUDE.md references to AGENTS.md
2. Run new installer for additional patterns
3. Review new pattern categories in `patterns/`
4. Update any custom patterns to follow new structure

### From manual setup to 1.0.0

1. Backup existing configuration
2. Run installer with desired template level
3. Migrate custom commands to pattern format
4. Test all workflows with new patterns

## Contributors

- Gabor Melli ([@gabormelli](https://github.com/gabormelli)) - Creator and maintainer
- Community contributors via GitHub

## Support

For issues and feature requests, please use [GitHub Issues](https://github.com/gabormelli/cli-agent-template/issues).

For documentation, see [docs/](docs/) directory.

---

[Unreleased]: https://github.com/gabormelli/cli-agent-template/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/gabormelli/cli-agent-template/releases/tag/v1.0.0
[0.9.0]: https://github.com/gabormelli/cli-agent-template/releases/tag/v0.9.0