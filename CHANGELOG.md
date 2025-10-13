# Changelog

All notable changes to AGET will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.7.0] - 2025-10-13 - "Portfolio Governance"

### Added
- **Portfolio Governance System**:
  - `.aget/portfolios/` directory for portfolio manifests
  - Portfolio field in version.json for organizational grouping
  - Classification levels (very_personal, confidential, private, public)
  - Portfolio-aware operations and security boundaries

- **Organizational Memory Patterns**:
  - Enhanced learning document structure (L51)
  - Standardized session metadata (v1.0)
  - Cross-agent knowledge sharing protocols

- **Learning Discovery Framework**:
  - Systematic learning capture and validation
  - Learning reference validation tools
  - Evolution document templates

### Changed
- Enhanced wake protocol with portfolio awareness
- Updated identity protocol to include portfolio field
- Improved session documentation requirements

### Documentation
- Portfolio manifests guide
- Learning document standard (v1.0)
- Session metadata standard (v1.0)

### Compatibility
- Backward compatible with v2.6
- New portfolio field optional (defaults to null)
- Existing agents work without portfolio assignment

## [2.6.0] - 2025-10-11 - "Configuration Management"

### Added
- **Configuration Size Management**:
  - 40,000 character limit for AGENTS.md (L146)
  - Size monitoring tools and warnings
  - Content extraction strategies for large configs

- **Framework Positioning**:
  - Clarified AGET vs autonomous agent frameworks
  - Updated positioning documentation
  - Landscape analysis (L143)

- **Contract Test Validation**:
  - Enhanced contract test suite
  - Validation for configuration compliance
  - Automated testing improvements

### Documentation
- Configuration size management guide
- Framework positioning analysis
- Best practices for large configurations

### Compatibility
- Fully backward compatible with v2.5
- No breaking changes

## [2.5.0] - 2025-10-06 - "Validation"

### Added
- **Contract Testing Framework**:
  - 7 core contract tests for wake/identity protocols
  - Automated validation of agent configuration
  - Test suite in tests/ directory

- **Identity Protocol**:
  - Standardized agent_name field (must match directory)
  - Instance type declaration (AGET vs aget)
  - Domain field for specialization

- **Validation Framework**:
  - Version compliance checking
  - Configuration consistency validation
  - Deployment verification standards (L93)

### Documentation
- Testing guide (tests/README.md)
- Contract test documentation
- Identity protocol standards

### Compatibility
- Backward compatible with v2.4
- All new agents must pass contract tests (v2.5.0 version floor)

## [2.4.0] - 2025-10-03 - "Naming Conventions"

### Added
- **Naming Convention Standard**:
  - Suffix-based capability signaling (-AGET vs -aget)
  - Visual warning for action-taking agents
  - Template naming convention (template-{role}-aget)

- **Organizational Grouping**:
  - aget_group field in version.json
  - Organization migration to aget-framework
  - Repository standardization

### Changed
- Repository names follow template-{role}-aget pattern
- Template organization moved to aget-framework
- Detection logic supports case-insensitive suffix (L47)

### Documentation
- Naming convention guide (L35)
- Organization structure documentation
- Migration guide from v2.3

### Compatibility
- Backward compatible with v2.3
- Old repository URLs redirect automatically

## [2.3.0] - 2025-10-02 - "Collaboration"

### Added
- **Pattern Versioning System**:
  - `.aget/patterns/versions.yaml` - Semantic versioning for all 24 patterns
  - `.aget/tools/bump_pattern.py` - Version bump automation
  - `.aget/tools/check_pattern_compatibility.py` - Compatibility validation
  - `docs/PATTERN_VERSIONING.md` - Complete versioning guide

- **Session Metadata System**:
  - `.aget/schemas/session_metadata_v1.0.yaml` - YAML schema for session frontmatter
  - `.aget/schemas/session_metadata_v1.0.json` - JSON schema for validation
  - `.aget/tools/generate_session_metadata.py` - Metadata generation tool
  - `.aget/tools/validate_session_metadata.py` - Schema validation tool
  - `docs/SESSION_METADATA_MIGRATION_GUIDE.md` - Migration instructions

- **Specification Framework**:
  - `.aget/docs/SPEC_FORMAT_v1.1.md` - EARS-based specification format
  - Support for formal capability documentation with aerospace patterns
  - Four maturity levels: bootstrapping, minimal, standard, exemplary

### Changed
- Session pattern upgraded to v1.1.0 (session metadata support)
- Version file now tracks collaboration features

### Documentation
- Complete guides for all v2.3 features
- Migration path from v2.2 to v2.3
- Pattern versioning best practices

### Compatibility
- Not backward compatible with v2.2 (breaking changes)
- Requires pattern versioning system
- Requires session metadata schema v1.0
- AGETs must update to v2.3 for ecosystem compatibility

## [2.1.0] - 2025-09-28

### Added
- **Clear File Ownership Standard**:
  - Framework scripts now use `aget_` prefix for clear identification
  - Added `.aget/OWNERSHIP.md` guide for developers
  - Migration script `aget_v21_migration.py` for upgrading existing projects

- **Release Quality Tools**:
  - `aget_check_permissions.py` - Comprehensive file permission validator
  - `aget_pre_release.sh` - Pre-release checklist automation
  - Both tools ensure template quality before releases

### Changed
- Renamed framework scripts with `aget_` prefix:
  - `check_file_permissions.py` → `aget_check_permissions.py`
  - `pre-release.sh` → `aget_pre_release.sh`
  - Existing `housekeeping_protocol.py` and `session_protocol.py` already use prefix

### Documentation
- Added ownership standard documentation
- Created migration guide for v2.0 → v2.1
- Updated installer to respect new naming convention

### Compatibility
- Maintains backward compatibility with v2.0
- Symlinks preserved for legacy script names
- Non-breaking changes for existing agents

## [2.0.0-beta.1] - 2025-09-24

### Gate 3: Migration Tools - Scaffolding System

#### Added
- **Template-based Scaffolding System**:
  - Five templates: `minimal`, `standard` (default), `agent`, `tool`, `hybrid`
  - `aget init --template <type>` creates appropriate directory structure
  - Auto-generates README.md files in key directories
  - Template-specific .gitignore patterns
  - Version tracking includes template information

- **Directory Structure Improvements**:
  - Renamed `outputs/` → `workspace/` (private exploration)
  - Renamed `Outputs/` → `products/` (public products)
  - Fixes case-sensitivity issues on macOS/Windows
  - Clear vocabulary distinction between private and public

- **Template Features**:
  - **Minimal**: Basic .aget/ and AGENTS.md only
  - **Standard**: Adds workspace/ and data/ directories
  - **Agent**: Full structure with checkpoints, src, tests, docs
  - **Tool**: Focused on products/ without workspace/
  - **Hybrid**: Combines agent and tool with examples/

#### Testing
- 13 new scaffolding tests covering all templates
- Validates directory creation, README generation, and configuration

#### Documentation
- Added comprehensive [SCAFFOLDING.md](docs/SCAFFOLDING.md)
- Updated vocabulary throughout codebase
- Clear migration path from v1 naming conventions

## [2.0.0-alpha.2] - 2025-09-24

### Gate 2: Pattern Library Complete

#### Added
- **Pattern Library Foundation** with PatternRegistry for discovery and loading
- **8 Reusable Patterns**:
  - `session/wake` - Wake up protocol with git status and pattern detection
  - `session/wind_down` - Save work with commits, notes, and tests
  - `session/sign_off` - Quick save and exit without prompts
  - `housekeeping/cleanup` - Remove temp files, caches, build artifacts
  - `housekeeping/doc_check` - Assess documentation quality (A-F grades)
  - `bridge/extract_output` - Transform agent outputs to public products
  - `housekeeping/migration_cleanup` - Clean migration artifacts (existing)
  - `meta/project_scanner` - Scan projects for AGET readiness (existing)

#### Enhanced
- `aget init` now creates:
  - `outputs/` directory for agent workspace
  - `data/` directory for persistent storage
  - `.aget/evolution/` for tracking insights
  - Updated AGENTS.md template with vocabulary reference

- `aget apply` command:
  - Lists all available patterns
  - Applies patterns to projects
  - Provides helpful error messages
  - Performance <2 second requirement met

#### Testing
- Comprehensive test suites for all patterns
- 54 tests passing
- Test-first development approach
- Performance validation (<2s requirement)

## [2.0.0-alpha.1] - 2025-09-24

### Gate 1: Core CLI Foundation

#### Added
- `aget init` command with three-tier degradation (gh/git/filesystem)
- `aget rollback` command for safe configuration rollback
- Base command architecture for future expansion
- Test theater with quality agent architecture

#### Changed
- Unified v2 vision combining CLI tool with framework concepts
- Vocabulary distinction: outputs (private) vs Outputs (public)
- Naming convention: aget-* (framework), *-aget (agents)

## [1.0.0] - 2025-09-22

### Initial Release

#### Added
- Universal agent configuration via AGENTS.md
- Session management protocols (wake, wind down, sign off)
- Housekeeping protocols (cleanup, documentation check)
- Template installer with three tiers (minimal, standard, advanced)
- Support for multiple AI coding assistants
- Cross-platform compatibility (Mac, Linux, Windows)

---

*For detailed migration instructions from v1 to v2, see [UPGRADING.md](docs/UPGRADING.md)*