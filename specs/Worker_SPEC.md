# Worker Capability Specification

**Version**: 1.0.0
**Status**: Active
**Owner**: template-worker-aget
**Created**: 2026-01-10
**Archetype**: Worker

---

## Purpose

Enable consistent task execution through standardized patterns and protocols

---

## Scope

This specification defines the core capabilities that all worker instances must provide.

### In Scope

- Core worker capabilities (3 requirements)
- EARS-compliant requirement format
- Verification approach

### Out of Scope

- Instance-specific extensions
- Integration with specific tools or systems

---

## Requirements

### CAP-WRK-001: Task Execution

**WHEN** performing worker activities
**THE** agent SHALL complete assigned work reliably

**Rationale**: Core worker capability
**Verification**: Instance demonstrates capability in operation

### CAP-WRK-002: Progress Reporting

**WHEN** performing worker activities
**THE** agent SHALL communicate status accurately

**Rationale**: Core worker capability
**Verification**: Instance demonstrates capability in operation

### CAP-WRK-003: Escalation

**WHEN** performing worker activities
**THE** agent SHALL raise blockers appropriately

**Rationale**: Core worker capability
**Verification**: Instance demonstrates capability in operation

---

## Verification

| Requirement | Verification Method |
|-------------|---------------------|
| CAP-WRK-001 | Operational demonstration |
| CAP-WRK-002 | Operational demonstration |
| CAP-WRK-003 | Operational demonstration |

---

## References

- L481: Ontology-Driven Agent Creation
- L482: Executable Ontology - SKOS+EARS Grounding
- Worker_VOCABULARY.md
- AGET_INSTANCE_SPEC.md

---

*Worker_SPEC.md v1.0.0 — EARS-compliant capability specification*
*Generated: 2026-01-10*
