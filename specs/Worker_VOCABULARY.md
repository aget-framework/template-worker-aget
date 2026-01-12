# Worker Domain Vocabulary

**Version**: 1.1.0
**Status**: Active
**Owner**: template-worker-aget
**Created**: 2026-01-10
**Updated**: 2026-01-11
**Scope**: Template vocabulary (DRIVES instance behavior per L481)
**Archetype**: Worker
**Template**: VOCABULARY_TEMPLATE_v3.3

---

## Meta

```yaml
vocabulary:
  meta:
    domain: "execution"
    version: "1.0.0"
    owner: "template-worker-aget"
    created: "2026-01-10"
    theoretical_basis:
      - "L481: Ontology-Driven Agent Creation"
      - "L482: Executable Ontology - SKOS+EARS Grounding"
    archetype: "Worker"
```

---

## Concept Scheme

```yaml
Worker_Vocabulary:
  skos:prefLabel: "Worker Vocabulary"
  skos:definition: "Vocabulary for worker domain agents"
  skos:hasTopConcept:
    - Worker_Core_Concepts
  rdf:type: skos:ConceptScheme
```

---

## Core Concepts

### Task

```yaml
Task:
  skos:prefLabel: "Task"
  skos:definition: "A discrete unit of work to be completed"
  skos:broader: Worker_Core_Concepts
  skos:inScheme: Worker_Vocabulary
```

### Execution

```yaml
Execution:
  skos:prefLabel: "Execution"
  skos:definition: "Performance of assigned work"
  skos:broader: Worker_Core_Concepts
  skos:inScheme: Worker_Vocabulary
```

### Completion_Criteria

```yaml
Completion_Criteria:
  skos:prefLabel: "Completion Criteria"
  skos:definition: "Conditions that define task success"
  skos:broader: Worker_Core_Concepts
  skos:inScheme: Worker_Vocabulary
```

### Handoff

```yaml
Handoff:
  skos:prefLabel: "Handoff"
  skos:definition: "Transfer of work or context to another agent"
  skos:broader: Worker_Core_Concepts
  skos:inScheme: Worker_Vocabulary
```

### Status_Report

```yaml
Status_Report:
  skos:prefLabel: "Status Report"
  skos:definition: "Communication of progress and blockers"
  skos:broader: Worker_Core_Concepts
  skos:inScheme: Worker_Vocabulary
```

---

## Concept Relationships

```yaml
relationships:
  hierarchical:
    - parent: Worker_Core_Concepts
      children: [Task, Execution, Completion_Criteria, Handoff, Status_Report]

  associative:
    - subject: Task
      predicate: skos:related
      object: Execution
    - subject: Execution
      predicate: skos:related
      object: Completion_Criteria
```

---

## EKO Cross-References

Per AGET_EXECUTABLE_KNOWLEDGE_SPEC.md:

| Vocabulary Term | EKO Term | Relationship |
|-----------------|----------|--------------|
| Task | EKO:Work_Unit | skos:exactMatch |
| Execution | EKO:Process_Execution | skos:closeMatch |
| Handoff | EKO:Context_Transfer | skos:broadMatch |

---

## Extension Points

Instances extending this template vocabulary should:
1. Add domain-specific terms under appropriate broader concepts
2. Maintain SKOS compliance (prefLabel, definition, broader/narrower)
3. Reference foundation L-docs where applicable
4. Use `research_status` for terms under investigation

---

## References

- L481: Ontology-Driven Agent Creation
- L482: Executable Ontology - SKOS+EARS Grounding
- R-REL-015: Template Ontology Conformance
- AGET_VOCABULARY_SPEC.md

---

*Worker_VOCABULARY.md v1.0.0 — SKOS-compliant template vocabulary*
*Generated: 2026-01-10*
