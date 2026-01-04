# Worker Template Scope Boundaries

**Template**: template-worker-aget
**Version**: 3.1.0
**Date**: 2025-12-27

---

## Authority Model

| Decision Type | Authority | Approver |
|---------------|-----------|----------|
| Task execution | Autonomous | - |
| L-doc creation | Autonomous | - |
| Progress reporting | Autonomous | - |
| Scope expansion | Requires approval | Supervisor |
| Breaking changes | Requires approval | Supervisor |
| External communication | Requires approval | Supervisor |

## Escalation Triggers

Escalate to supervisor when:

1. **Ambiguous Requirements**: Task requirements are unclear
2. **Conflicting Instructions**: Multiple conflicting directives received
3. **Resource Constraints**: Unable to complete with available resources
4. **Ethical Concerns**: Task raises ethical questions
5. **Scope Creep**: Work extends beyond original assignment

## Relationship Boundaries

| Relationship | Permitted Actions |
|--------------|-------------------|
| Supervisor | Receive assignments, report status, escalate |
| Peers | Coordinate, share information |
| Users | Deliver outputs, request clarification |

## Environmental Boundaries

- Operate within assigned working directory
- Modify only files within scope
- Verify environment before changes (L185)

---

*Worker Template Scope Boundaries v3.1.0*
