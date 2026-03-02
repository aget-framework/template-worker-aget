# Template: Worker Agent

> Execute tasks reliably with progress tracking and deliverable production

**Version**: v3.7.0 | **Archetype**: Worker | **Skills**: 2 specialized + 15 universal

---

## Why Worker?

The Worker archetype is the **foundation of task execution** in AGET. While every agent can do work, worker agents excel at:

- **Structured execution** — Break tasks into steps, track progress, produce deliverables
- **Visibility** — Report completion status, blockers, and handoff context
- **Reliability** — Never claim completion without evidence, never skip steps silently

**For evaluators**: If you need an AI that executes defined work items with clear tracking and accountability, the Worker archetype provides the discipline of task management without heavyweight tooling.

**Domain knowledge that compounds**: Worker agents build persistent understanding of your task patterns — common blockers, resolution strategies, and handoff conventions. Unlike tools that start fresh each session, your agent accumulates execution context that makes each task more efficient and each handoff more complete.

---

## Skills

Worker agents come with **2 archetype-specific skills** plus the universal AGET skills.

### Archetype Skills

| Skill | Description |
|-------|-------------|
| **aget-execute-task** | Execute defined tasks with step-by-step progress tracking. Validates prerequisites, produces deliverables, handles blockers with human escalation. |
| **aget-report-progress** | Report work status including completion percentage, blockers, and risks. Supports handoff documentation for session continuity. |

### Universal Skills

All AGET agents include session management, knowledge capture, and health monitoring:

- `aget-wake-up` / `aget-wind-down` — Session lifecycle
- `aget-create-project` / `aget-review-project` — Project management
- `aget-record-lesson` / `aget-capture-observation` — Learning capture
- `aget-check-health` / `aget-check-kb` / `aget-check-evolution` — Health monitoring
- `aget-propose-skill` / `aget-create-skill` — Skill development
- `aget-save-state` / `aget-file-issue` — State and issue management

---

## Ontology

Worker agents use a **formal vocabulary** of 7 concepts organized into 2 clusters:

| Cluster | Concepts |
|---------|----------|
| **Task Management** | Task, Task_Status, Progress, Blocker |
| **Deliverable Production** | Deliverable, Handoff, Completion |

This vocabulary enables precise communication about work execution and progress.

See: [`ontology/ONTOLOGY_worker.yaml`](ontology/ONTOLOGY_worker.yaml)

---

## Quick Start

```bash
# 1. Clone the template
git clone https://github.com/aget-framework/template-worker-aget.git my-worker-agent
cd my-worker-agent

# 2. Configure identity
# Edit .aget/version.json:
#   "agent_name": "my-worker-agent"
#   "domain": "your-domain"

# 3. Verify setup
python3 -m pytest tests/ -v
# Expected: All tests passing
```

### Try the Skills

```bash
# In Claude Code CLI
/aget-execute-task       # Execute a defined task
/aget-report-progress    # Report on current work status
```

---

## What Makes Worker Different

| Aspect | Generic AI Assistant | Worker Agent |
|--------|---------------------|--------------|
| **Task execution** | Ad-hoc completion | Step tracking with deliverables |
| **Progress reporting** | Manual updates | Structured reports with percentages |
| **Blockers** | Silent failures | Explicit escalation with impact |
| **Handoffs** | Context lost | Documented state for continuation |
| **Domain memory** | Starts fresh each session | Accumulates task execution expertise over time |

---

## Framework Specification

| Attribute | Value |
|-----------|-------|
| **Framework** | [AGET v3.7.0](https://github.com/aget-framework/aget) |
| **Archetype** | Worker |
| **Skills** | 17 total (2 archetype + 15 universal) |
| **Ontology** | 7 concepts, 2 clusters |
| **License** | Apache 2.0 |

---

## Learn More

- **[AGET Framework](https://github.com/aget-framework/aget)** — Core framework documentation
- **[Archetype Guide](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — All 12 archetypes explained
- **[Getting Started](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — Full onboarding guide

---

## Related Archetypes

| Archetype | Best For |
|-----------|----------|
| **[Developer](https://github.com/aget-framework/template-developer-aget)** | Code building, testing, review |
| **[Supervisor](https://github.com/aget-framework/template-supervisor-aget)** | Fleet coordination and oversight |
| **[Operator](https://github.com/aget-framework/template-operator-aget)** | Incident handling and playbooks |

---

**AGET Framework** | Apache 2.0 | [Issues](https://github.com/aget-framework/template-worker-aget/issues)
