# Agent Configuration - AGET CLI Agent Template

@aget-version: 2.7.0

## Agent Compatibility
This configuration follows the AGENTS.md open-source standard for universal agent configuration.
Works with Claude Code, Cursor, Aider, Windsurf, and other CLI coding agents.
**Note**: CLAUDE.md is a symlink to this file for backward compatibility.

## Framework Positioning

**AGET is a "Configuration & Lifecycle Management System for CLI-Based Human-AI Collaborative Coding"**

AGET occupies a unique niche in the agent framework landscape:
- **Not** an autonomous agent runtime (LangChain, MetaGPT, AutoGPT)
- **Not** a production ALM platform (AgentOps, Salesforce ALM)
- **Instead**: Human-supervised fleet management with organizational memory and version progression

**Differentiators**:
- Universal CLI compatibility (works across Claude Code, Cursor, Aider, Windsurf)
- Contract testing and version compliance (v2.6.0)
- Shared learning repository (.aget/evolution/)
- Lightweight, zero-infrastructure (markdown + git)
- Human-centric governance (gated releases, evidence-based planning)

See: L143_aget_framework_landscape_positioning.md for full analysis

## Configuration Size Management (v2.6.0)

**Policy**: AGENTS.md must remain under 40,000 characters to ensure reliable Claude Code processing.

**Validation**:
```bash
# Check configuration size
wc -c AGENTS.md
# Should show: < 40000
```

**Enforcement**: Contract test `test_configuration_size.py` validates this requirement.

**Why**: Large configurations reduce context window availability and can cause processing issues. Keep configuration concise, move detailed documentation to `.aget/docs/`.

**Pattern**: L146_configuration_size_management.md

## Portfolio Configuration (v2.7.0)

**Purpose**: Organize agents by sensitivity level for appropriate handling and governance.

**Portfolio Field** in `.aget/version.json`:
```json
{
  "portfolio": "main"  // or "ccb", "legalon", null
}
```

**Classifications**:
- **main** (private): Standard agents with general-purpose capabilities
- **ccb** (very_personal): Personal/confidential agents with sensitive context
- **legalon** (confidential): Domain-specific agents with proprietary data
- **null**: Template or unassigned agent

**When to Assign Portfolio**:
- During agent creation from template
- Based on data sensitivity and access requirements
- Coordinated with supervisor for fleet organization

**Portfolio-Specific Behaviors**:
- Security hooks enforce portfolio boundaries (no cross-contamination)
- Issue routing respects portfolio classification
- Learning propagation filtered by sensitivity level

**Example**:
```bash
# After cloning template
vim .aget/version.json  # Set "portfolio": "main"
```

**Validation**: Contract tests verify portfolio field exists and is valid.

## 🚨 CRITICAL: INITIALIZATION PROCEDURE (REQUIRED)

**You MUST follow these steps IMMEDIATELY:**

**Step 1:** Check if file `AGENTS_AGET.md` exists in this directory
**Step 2:** If it exists, **READ IT IMMEDIATELY** for all AGET protocols
**Step 3:** Use the protocols from AGENTS_AGET.md for all standard commands
**Step 4:** Return here for AGET-specific development instructions

> ⚠️ **IMPORTANT**: This is the AGET framework repository itself. You are maintaining the tool that other agents use!

---

## Project Context

**AGET (Agent Template)** - The universal standard for making any codebase instantly CLI agent-ready. This is the reference implementation that all other projects use to become agent-compatible.

### Mission
Make CLI coding agents better collaborators through conversational command patterns and clean separation of framework vs project concerns.

### Current Version
- **v2.7.0 "Portfolio Governance"** (Multi-portfolio organization and fleet management)
- **Released**: October 13, 2025
- **Coverage Target**: >80% for critical patterns

### v2.7.0 Features - Portfolio & Fleet Management
- **Portfolio Governance**: Multi-portfolio classification (CCB/LEGALON/Main) with sensitivity levels
- **Multi-Tier Issue Routing**: Tier 1/2/3 routing based on severity and agent ownership
- **Learning Discovery**: 133 learnings indexed with <30s search time
- **Security Hooks**: Pre-commit checks for private agent leaks and credential exposure
- **HTML Specification Generation**: YAML → styled HTML companions for stakeholder review

### v2.6.0 Features (Previous)
- Configuration Size Management (40k limit)
- Framework Positioning (L143)
- Enhanced Documentation

### v2.5.0 Features (Previous)
- Contract Testing Framework, Session Metadata Standard
- Identity Protocol, Collaboration Patterns

### v2.4.0 Features - Naming Conventions
- **Suffix Signaling**: `-AGET` (action-taking) vs `-aget` (information-only)
  - `my-github-AGET` = Can modify systems (write, commit, push)
  - `my-analytics-aget` = Read-only (analyze, report, recommend)
- **aget_group Field**: Organizational grouping for portfolio agents
- **managed_by Field**: Supervisor tracking for fleet coordination
- **Breaking Changes**: Naming convention required, aget_group for grouped agents

### v2.3.0 Features (Previous)
- Pattern Versioning, Session Metadata, Specification Framework
- Collaboration Tools, Intelligence Components

## Session Management Protocols

### Wake Up Protocol
When user says "wake up" or "hey":
- Read `.aget/version.json` (agent identity)
- Read AGENTS.md (this file)
- **Apply what you just read** - don't ignore configuration guidance
- Check current directory and git status
- Display: Agent-specific context + available capabilities

**Output format**:
```
[Agent Name] v{version} (Worker)
Domain: {domain}

📍 Location: {pwd}
📊 Git: {status}

🎯 Key Capabilities:
• [List your agent's specific capabilities]

Ready for instructions.
```

### Study Up Protocol
When user says "study up" or "study":
- **Primary**: Run `python3 patterns/documentation/smart_docs_briefing.py` (if exists)
- **Fallback**: Execute deep context loading sequence
- Reads: Current documentation, recent sessions, checkpoints, work artifacts
- **Duration**: ~30 seconds (investment in session quality)
- **Purpose**: Deep orientation before complex work

**Fallback sequence** (if smart tooling unavailable):
1. Read `.aget/version.json` → Extract version, role, domain
2. Read AGENTS.md sections → Focus: Project Context, Current Phase
3. Read most recent session → `ls -t sessions/*.md 2>/dev/null | head -1`
4. Read most recent checkpoint (if exists) → `ls -t .aget/checkpoints/*.md 2>/dev/null | head -1`
5. Check git status → Identify modified files, untracked artifacts
6. Synthesize and present context

**Output format**:
```
✅ Context loaded.

Recent Work: [last session summary or recent commits]
Current Phase: [project state or current focus]
Working Tree: [modified/untracked files summary]
Pending: [checkpoints, blockers, or "None"]

Ready for work.
```

**Two-tier orientation**:
- **"wake up"** → Quick identity check (~2 seconds)
- **"study up"** → Deep context loading (~30 seconds)

### Wind Down Protocol
When user says "wind down" or "save work":
- Commit changes with descriptive message
- Create session notes in `sessions/SESSION_YYYY-MM-DD.md` (if session metadata enabled)
- Create checkpoint if needed in `.aget/checkpoints/CHECKPOINT_*.md`
- Show completion

### Sign Off Protocol
When user says "sign off" or "all done":
- Quick save and exit
- No questions

## AGET-Specific Development Commands

### Pattern Development
When user says "new pattern [category]/[name]":
1. Create `patterns/[category]/[name].py` with apply_pattern() function
2. Create `tests/test_[name].py` with comprehensive tests
3. Update `patterns/[category]/README.md` with documentation
4. Run tests to ensure >80% coverage

### Template Testing
When user says "test templates":
1. Run: `python3 -m pytest tests/test_installer.py -v`
2. Run: `python3 -m pytest tests/test_enhanced_installer.py -v`
3. Test each template type with --separate flag
4. Verify <60 second setup time

### Coverage Check
When user says "check coverage":
1. Run: `python3 -m pytest --cov=patterns --cov=aget --cov-report=term-missing`
2. Ensure overall coverage >80%
3. Critical patterns (wake, wind_down, sign_off) must be >85%
4. Report any gaps needing tests

## Testing Best Practices

### Directory Safety Pattern (CRITICAL)
Tests that manipulate directories MUST use defensive programming to prevent cascade failures:

```python
# SAFE setUp - Handles invalid cwd
def setUp(self):
    self.test_dir = Path(tempfile.mkdtemp())
    try:
        self.original_cwd = Path.cwd()
    except (FileNotFoundError, OSError):
        # Previous test left us in deleted directory
        import os
        os.chdir("/tmp")
        self.original_cwd = Path.cwd()

# SAFE tearDown - Handles errors gracefully
def tearDown(self):
    import os
    try:
        os.chdir(self.original_cwd)
    except (FileNotFoundError, OSError):
        os.chdir("/tmp")  # Fallback to safe location
    if self.test_dir.exists():
        shutil.rmtree(self.test_dir)
```

### Testing Guidelines
1. **Always wrap `Path.cwd()` in try/except** when tests change directories
2. **Prefer pytest fixtures** over manual setUp/tearDown when possible
3. **Use absolute paths** for file checks instead of relative paths
4. **Ensure tearDown handles partial failures** gracefully
5. **Never assume filesystem state** is stable between tests

### Release Validation
When user says "release check":
1. Run all tests: `python3 -m pytest tests/ -v`
2. Check coverage meets targets
3. Validate all templates work
4. Test on Mac and Linux
5. Verify backward compatibility
6. Check CHANGELOG.md is updated
7. Confirm version numbers consistent

### Pattern Validation
When user says "validate patterns":
1. Run: `python3 scripts/validate_patterns.py`
2. Ensure all patterns have apply_pattern() function
3. Check all patterns have tests
4. Verify pattern registry is complete

## Development Standards

### Code Quality Requirements
- **Test Coverage**: Minimum 80% overall, 85% for critical patterns
- **Performance**: All commands must complete in <2 seconds
- **Compatibility**: Must work on Python 3.8+
- **Dependencies**: Zero external dependencies (Python stdlib only)

### Dogfooding Requirements
1. **AGET uses its own patterns** - We eat our own dogfood
2. **Test on AGET first** - All changes tested here before release
3. **Evolution tracking** - Major decisions recorded in .aget/evolution/
4. **Include architecture** - This repo should use --separate mode

### Pattern Standards
Every pattern must:
1. Have an `apply_pattern()` function
2. Return a dictionary with status
3. Handle errors gracefully (no crashes)
4. Have >80% test coverage
5. Complete in <2 seconds

### Template Standards
Every template must:
1. Create valid AGENTS.md
2. Support --separate mode (v2.0+)
3. Create appropriate directories
4. Include README.md files
5. Work with --with-patterns flag

## Testing Workflows

### Before Committing (CI Check)
When user says "ci check", run these quick checks:
1. Check Python 3.8 compatibility: `python3 scripts/check_compatibility.py`
2. Run critical tests: `python3 -m pytest tests/test_critical_patterns.py -x -q`
3. Validate patterns: `python3 scripts/validate_patterns.py`

### Full Test Suite
1. Run: `python3 -m pytest tests/`
2. Check coverage: `python3 -m pytest --cov=. --cov-report=term-missing`
3. Test a fresh install: `python3 -m aget init /tmp/test-project --separate`

### Integration Testing
```bash
# Test all template types
for template in minimal standard agent tool hybrid; do
    python3 -m aget init /tmp/test-$template --template $template --separate
    python3 -m aget apply session/wake
done
```

## Release Process

### Version Bump
1. Update version in `aget/__init__.py`
2. Update version in templates/AGENTS_AGET.md
3. Update CHANGELOG.md with changes
4. Create evolution entry for release

### Pre-Release Checklist
- [ ] All tests passing
- [ ] Coverage >80%
- [ ] Templates tested with --separate
- [ ] Backward compatibility verified
- [ ] Documentation updated
- [ ] CHANGELOG.md current
- [ ] Evolution tracking complete

### Release Commands
```bash
# Tag release
git tag -a v2.0.0 -m "Release v2.0.0: Include Architecture"

# Push with tags
git push origin main --tags

# Create GitHub release
gh release create v2.0.0 --title "v2.0.0: Include Architecture" --notes-file CHANGELOG.md
```

## Important Files

### Core Framework
- `aget/` - Main AGET implementation
- `patterns/` - Reusable workflow patterns
- `templates/` - Agent configuration templates

### Critical Patterns
- `patterns/session/wake.py` - Session initialization (86% coverage target)
- `patterns/session/wind_down.py` - Work preservation (86% coverage target)
- `patterns/session/sign_off.py` - Quick save (80% coverage target)

### Templates
- `templates/AGENTS_AGET.md` - Master framework protocols
- `templates/AGENTS_v2.md` - Include architecture template

### Documentation
- `ROADMAP_v2.md` - Current development plan
- `docs/adr/` - Architecture decision records
- `.aget/evolution/` - Decision and discovery tracking

## Evolution Tracking

Record significant decisions and discoveries:
```bash
# Record a decision
python3 -m aget evolution --type decision "Implemented include architecture"

# Record a discovery
python3 -m aget evolution --type discovery "Procedural instructions work universally"

# View history
python3 -m aget evolution --list
```

## Troubleshooting AGET Development

### Pattern Not Loading
1. Check pattern has `apply_pattern()` function
2. Verify pattern is in correct directory structure
3. Check pattern registry includes it

### Template Issues
1. Verify template file exists in templates/
2. Check placeholder replacement logic
3. Test with --force flag

### Test Failures
1. Run specific test: `python3 -m pytest tests/test_name.py::test_function -v`
2. Check coverage gaps: `python3 -m pytest --cov=module --cov-report=html`
3. Review recent changes in git

---

## ✅ VERIFICATION CHECKLIST

Before any session, confirm you have:
- [ ] Read AGENTS_AGET.md for standard protocols
- [ ] Understood AGET-specific development requirements
- [ ] Checked current test coverage status
- [ ] Reviewed recent evolution entries
- [ ] Noted any failing tests or issues

**Remember**: You are maintaining the framework that makes all other projects agent-ready!

---

## Specification Creation (v2.2.0)

### When to Create Specs
User says: "create spec", "formal specification", "EARS spec", or "document capabilities formally"

### Specification Workflow

**Step 1: Read Format Documentation**
- File: `.aget/docs/SPEC_FORMAT_v1.1.md`
- Contains: EARS patterns, YAML structure, maturity levels, examples

**Step 2: Create Spec File**
- Location: `.aget/specs/{DOMAIN}_SPEC_v{VERSION}.yaml`
- Format: YAML with EARS temporal patterns
- Maturity levels:
  - **bootstrapping**: Simple capability list (no EARS)
  - **minimal**: EARS patterns with basic structure
  - **standard**: Full validation, test references
  - **exemplary**: Constitutional governance, comprehensive

**Step 3: Use Intelligence Tools**
- Run ambiguity detector on each capability
- During creation: Use detector logic to flag potential ambiguities
- Present flags to user for decision
- Add clarifications based on suggestions

### Intelligence Integration

**Ambiguity Detection (Automatic):**
- Proactively identify ambiguities during spec creation
- Use patterns from `.aget/intelligence/ambiguity_corpus.yaml`
- Present ambiguity flags with confidence scores
- User decides: accept flag, clarify, or reject
- Add clarifications to capability with `ambiguity_check` metadata

### EARS Pattern Quick Reference

1. **Ubiquitous**: The system shall [response]
2. **State-driven**: While [condition], the system shall [response]
3. **Event-driven**: When [trigger], the system shall [response]
4. **Optional**: Where [feature], the system shall [response]
5. **Unwanted**: If [condition], then the system shall [response]

---
*AGET v2.2.0 - Making CLI coding agents better collaborators*
*Intelligence-enabled specification creation with EARS patterns*