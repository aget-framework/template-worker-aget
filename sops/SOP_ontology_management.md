# SOP: Ontology Management

**Implements**: OT-003, OT-006, OT-009 (ONTOLOGY_TIER_SPEC v1.0)
**Pain Point**: L600 (Ontologies Are AGET Artifacts — no production SOP existed)
**See**: ONTOLOGY_TIER_SPEC v1.0, L542 (Maturity Tiers), L481 (Ontology-Driven Creation)
**Pattern**: L323 (Artifact Format Verification Protocol)

---

**Version**: 1.0.0
**Created**: 2026-03-23
**Owner**: private-supervisor-AGET
**Category**: Governance
**Related**: L600, L542, L481, L564, L525, ONTOLOGY_TIER_SPEC v1.0, SKILL-014 (aget-analyze-ontology), SKILL-019 (aget-expand-ontology), ONTOLOGY_DOMAIN_TEMPLATE.yaml, ONTOLOGY_QUALITY_RUBRIC_v1.0.md

---

## Purpose

Canonical process for creating, expanding, reviewing, and promoting agent ontologies across the fleet. Ensures ontologies — as AGET artifacts — receive the same governance rigor as session logs, L-docs, and specifications.

**Problem Solved**: Without this SOP, agents with ontology skills (`aget-expand-ontology`, `aget-analyze-ontology`) have capability without direction. Fleet ontology capability scoring (2026-03-23) showed 28/32 agents at template-baseline 7 concepts with no process guidance for expansion.

---

## Scope

### When to Use This SOP

| Trigger | Example |
|---------|---------|
| Creating domain ontology for an agent | New agent at Domain tier, or inherited agent promoted to Domain |
| Expanding existing ontology | Agent needs domain-specific vocabulary beyond template baseline |
| Reviewing ontology quality | Pre-tier-promotion assessment, periodic health check |
| Tier promotion (inherited -> domain -> operational) | Agent meets tier criteria, supervisor initiates promotion |

### When NOT to Use This SOP

| Situation | Alternative |
|-----------|-------------|
| Agent correctly at Inherited tier with no domain pressure | No action needed (OT-021 exemption — L564) |
| Template ontology directory structure issues | Use SOP_fleet_upgrade.md for structural fixes |
| Framework vocabulary changes | Framework-AGET owns framework vocabulary; use L100 checkpoint |

---

## Prerequisites

- [ ] Agent has `ontology/` directory with template baseline (OT-005)
- [ ] Agent has `/aget-expand-ontology` skill installed (or will install during procedure)
- [ ] Agent has `/aget-analyze-ontology` skill installed (or will install during procedure)
- [ ] Domain area identified for agent (from FLEET_STATE.yaml `domain_area` field)

---

## Procedure

### Step 1: Assess Current State

Run `/aget-analyze-ontology` in the agent's session to establish baseline.

```bash
# In agent session:
/aget-analyze-ontology
```

Record: current tier, concept count, gap analysis output.

### Step 2: Determine Target Tier

Apply L542 five-question diagnostic:

| # | Question | Answer |
|---|----------|--------|
| Q1 | Does the agent's domain have distinct vocabulary not covered by framework terms? | Y/N |
| Q2 | Does the agent have skills that would benefit from ontology-grounded concepts? | Y/N |
| Q3 | Would behavioral triggers (OT-020) improve the agent's EARS requirements? | Y/N |
| Q4 | Has the agent demonstrated domain depth (>=10 sessions, domain-specific L-docs)? | Y/N |
| Q5 | Are there term collision risks with other agents in the same portfolio? | Y/N |

**Decision**:
- Q1=N → Stay Inherited (OT-021 exemption)
- Q1=Y, Q4=N → Defer (insufficient evidence of demand — L564)
- Q1=Y, Q4=Y → Proceed to Domain tier creation (Step 3)
- All Y → Consider Operational tier path (Step 3 + Step 5)

### Step 3: Create Domain Ontology (L481 Protocol)

Use the domain ontology template:

```bash
# Copy template to agent's ontology/ directory
cp .aget/templates/ONTOLOGY_DOMAIN_TEMPLATE.yaml ~/github/{agent}/ontology/ONTOLOGY_{domain}.yaml
```

Edit the template:
1. Replace all `{placeholders}` with agent-specific values
2. Define >= 25 domain-specific SKOS terms (OT-003 threshold)
3. Set `extends:` to reference framework vocabulary
4. Ensure zero collisions with framework terms

### Step 4: Expand via Skill

Run `/aget-expand-ontology` to bootstrap from the agent's knowledge base:

```bash
# In agent session:
/aget-expand-ontology
```

The skill will:
- Scan the agent's KB (L-docs, specs, session logs) for domain vocabulary
- Propose SKOS terms grounded in actual usage
- Add terms to the ontology YAML file

### Step 5: Verify Quality

Score the ontology using the quality rubric (`ONTOLOGY_QUALITY_RUBRIC_v1.0.md`):

| Dimension | Weight | Minimum for Domain | Minimum for Operational |
|-----------|:------:|:------------------:|:-----------------------:|
| Coverage | 30% | 25 terms | 50 terms |
| SKOS Compliance | 25% | 100% | 100% |
| Interlinkage | 20% | 3 broader/narrower | 10 broader/narrower |
| Domain Alignment | 15% | 80% domain-relevant | 90% domain-relevant |
| Freshness | 10% | Created this session | Updated within 30 days |

Run collision check:
```bash
python3 .aget/tools/cross_reference_vocabulary.py ~/github/{agent}/ontology/
```

### Step 6: Update Fleet State

After verification passes:

1. Update agent's `.aget/version.json`: `"ontology_tier": "domain"` (or `"operational"`)
2. Update `FLEET_STATE.yaml`: `ontology_tier: domain` and `ontology_concepts: {count}`
3. Commit: `ontology: promote to Domain tier — {N} SKOS terms materialized`

---

## Checklists

### Checklist A: Inherited -> Domain Promotion

Use when: Agent meets L542 Q1+Q4 criteria and has demand signal.

- [ ] Current tier confirmed as `inherited` via `/aget-analyze-ontology`
- [ ] Domain area identified in FLEET_STATE.yaml
- [ ] Template copied: `ONTOLOGY_DOMAIN_TEMPLATE.yaml` -> agent's `ontology/`
- [ ] >= 25 domain-specific SKOS terms defined
- [ ] Zero framework vocabulary collisions (`cross_reference_vocabulary.py`)
- [ ] Quality rubric score >= Domain minimum (all 5 dimensions)
- [ ] `version.json` updated with `ontology_tier: domain`
- [ ] `FLEET_STATE.yaml` updated with new tier + concept count
- [ ] Committed with message: `ontology: promote to Domain tier`

### Checklist B: Domain -> Operational Promotion

Use when: Agent has domain vocabulary AND ontology-consuming skills AND lifecycle integration.

- [ ] Domain tier requirements met (Checklist A complete)
- [ ] At least one skill reads/validates ontology content (OT-007)
- [ ] Ontology status visible in wake-up or health check output (OT-007)
- [ ] Quality rubric score >= Operational minimum (all 5 dimensions)
- [ ] `version.json` and `FLEET_STATE.yaml` updated to `operational`
- [ ] Committed with message: `ontology: promote to Operational tier`

### Checklist C: Periodic Ontology Review

Use when: Quarterly review or pre-assessment.

- [ ] Run `/aget-analyze-ontology` — check for CONCEPT_SURPLUS (OT-022)
- [ ] Verify `extends:` references resolve (OT-011)
- [ ] Check freshness: last ontology commit within 90 days
- [ ] Score against quality rubric — note any dimension degradation

---

## Anti-Patterns

| Anti-Pattern | Consequence | Prevention |
|--------------|-------------|------------|
| Uniform tier mandate | Agents create decorative ontology to pass checks (L564) | Respect OT-021 inherited exemption; require demand evidence |
| Expanding without demand signal | Concept surplus (OT-022): vocabulary grows but nothing consumes it | Apply L542 Q1-Q5 before expansion |
| Copying another agent's ontology | Cross-domain term pollution, false precision | Always start from ONTOLOGY_DOMAIN_TEMPLATE; ground in agent's own KB |
| Skipping collision check | Framework vocabulary collision creates ambiguity | Always run cross_reference_vocabulary.py before commit |

---

## Quick Reference

### Minimum Viable Execution

1. Run `/aget-analyze-ontology` to assess current state
2. Apply L542 diagnostic — determine if promotion is warranted
3. If yes: copy template, define >= 25 terms, verify, update fleet state

### Decision Tree

```
Agent needs ontology work?
    |
    +-- Is agent at inherited tier?
    |   |
    |   +-- Does domain have distinct vocabulary? (Q1)
    |   |   +-- NO --> Stay inherited (OT-021)
    |   |   +-- YES --> Has agent demonstrated depth? (Q4)
    |   |       +-- NO --> DEFER (L564)
    |   |       +-- YES --> Execute Domain promotion (Steps 3-6)
    |   |
    +-- Is agent at domain tier?
    |   |
    |   +-- Has consuming skills + lifecycle integration?
    |       +-- NO --> Stay domain
    |       +-- YES --> Execute Operational promotion (Checklist B)
    |
    +-- Is agent at operational tier?
        +-- Run periodic review (Checklist C)
```

---

## Integration

### Related Protocols

| Protocol | Relationship |
|----------|--------------|
| L481 (Ontology-Driven Agent Creation) | Vocabulary-first creation methodology — Step 3 follows this |
| L100 (Worker Coordination) | Used when framework vocabulary changes need supervisor review |
| ONTOLOGY_TIER_SPEC v1.0 | Source of truth for tier definitions, requirements, validation |

### Workflow Position

```
Agent Creation / Session Work
        |
    THIS SOP (Ontology Management)
        |
    /aget-analyze-ontology (Verification)
        |
    FLEET_STATE.yaml Update
```

---

## References

- L600: Ontologies Are AGET Artifacts (governance triad requirement)
- L542: Ontology Maturity Tiers (three-tier model, 5-question diagnostic)
- L481: Ontology-Driven Agent Creation (vocabulary-first protocol)
- L564: Ontology Adoption Is Demand-Side (demand signal required)
- ONTOLOGY_TIER_SPEC v1.0: Formal specification (OT-001 through OT-022)
- ONTOLOGY_DOMAIN_TEMPLATE.yaml: Content template for domain ontologies
- ONTOLOGY_QUALITY_RUBRIC_v1.0.md: Quality scoring rubric

---

## Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Fleet tier distribution | Count of agents per tier | >= 3 Domain, >= 2 Operational |
| Promotion success rate | Agents promoted that maintain tier at 30-day check | >= 80% |
| Concept surplus ratio | Agents with OT-022 CONCEPT_SURPLUS | < 20% of Domain+ agents |

---

*SOP_ontology_management.md v1.0.0 — "Govern ontologies as first-class AGET artifacts"*
*Created: 2026-03-23*
*Owner: private-supervisor-AGET*
