# Ontology Quality Rubric v1.0

**Version**: 1.0.0
**Created**: 2026-03-23
**Author**: private-supervisor-AGET
**Extends**: ONTOLOGY_TIER_SPEC v1.0 (tier classification criteria)
**Implements**: L600 (Ontologies Are AGET Artifacts — rubric pillar)
**SOP**: SOP_ontology_management.md (Step 5: Verify Quality)
**Template**: ONTOLOGY_DOMAIN_TEMPLATE.yaml

---

## Purpose

Score ontology quality beyond tier classification. While ONTOLOGY_TIER_SPEC defines *what tier an agent is at*, this rubric scores *how good the ontology is* within that tier. Used during:
- G3 tier assessment (fleet_ontology_skills_deployment)
- Periodic ontology reviews (SOP Checklist C)
- Pre-promotion quality gates

---

## Scoring Dimensions

### Dimension 1: Coverage (30% weight)

**What it measures**: Number and breadth of domain-specific concepts defined.

| Score | Criteria | Evidence |
|:-----:|----------|----------|
| 0 | Template baseline only (7 concepts) | `ontology_concepts: 7` in FLEET_STATE |
| 1 | 8-24 concepts (above baseline, below Domain threshold) | Partial expansion, insufficient for Domain tier |
| 2 | 25-49 concepts (meets Domain tier minimum OT-003) | Passes `grep -c "prefLabel:" ontology/*.yaml >= 25` |
| 3 | 50-99 concepts (strong domain coverage) | Multiple concept clusters, top concepts well-decomposed |
| 4 | 100+ concepts (comprehensive domain vocabulary) | Approaching Operational depth |

**Minimum for Domain tier**: Score 2
**Minimum for Operational tier**: Score 3

### Dimension 2: SKOS Compliance (25% weight)

**What it measures**: Structural correctness of SKOS term definitions.

| Score | Criteria | Evidence |
|:-----:|----------|----------|
| 0 | No SKOS structure (plain text, ad-hoc format) | Missing apiVersion, conceptScheme, or concepts block |
| 1 | Partial SKOS (some terms missing required fields) | Terms lack id, prefLabel, or definition |
| 2 | All terms have id + prefLabel + definition | 100% structural compliance (OT-006 minimum) |
| 3 | Plus: extends reference resolves, broader/narrower typed correctly | OT-011 reference resolution passes |
| 4 | Plus: example and source fields populated for all terms | Full provenance traceability |

**Minimum for Domain tier**: Score 2
**Minimum for Operational tier**: Score 3

### Dimension 3: Interlinkage (20% weight)

**What it measures**: Semantic relationships between concepts (hierarchy + lateral links).

| Score | Criteria | Evidence |
|:-----:|----------|----------|
| 0 | Flat list — no broader/narrower/related links | All terms at same level |
| 1 | 1-2 broader/narrower relationships | Minimal hierarchy |
| 2 | 3-9 broader/narrower relationships | Basic taxonomy structure |
| 3 | 10+ broader/narrower + some related links | Rich taxonomy with lateral connections |
| 4 | Fully connected: every term has >= 1 relationship, related cross-links to framework vocabulary | Ontology functions as a navigable knowledge graph |

**Minimum for Domain tier**: Score 2
**Minimum for Operational tier**: Score 3

### Dimension 4: Domain Alignment (15% weight)

**What it measures**: How relevant the defined terms are to the agent's actual domain work.

| Score | Criteria | Evidence |
|:-----:|----------|----------|
| 0 | Terms are generic / framework concepts repackaged | Could apply to any agent |
| 1 | < 50% of terms are domain-specific | Mix of generic and domain terms |
| 2 | 50-79% of terms are domain-specific | Majority domain-relevant |
| 3 | 80-94% of terms are domain-specific | Strong domain focus (OT-003 intent) |
| 4 | 95%+ domain-specific, grounded in KB evidence (L-docs, sessions, specs) | Every term traceable to agent's work |

**Minimum for Domain tier**: Score 3
**Minimum for Operational tier**: Score 3

### Dimension 5: Freshness (10% weight)

**What it measures**: How recently the ontology was created or updated.

| Score | Criteria | Evidence |
|:-----:|----------|----------|
| 0 | Template baseline, never modified | Last commit is template migration |
| 1 | Modified > 90 days ago | `git log -1 -- ontology/` older than 90 days |
| 2 | Modified 31-90 days ago | Recent but not current |
| 3 | Modified within 30 days | Actively maintained |
| 4 | Modified this session + review scheduled | Current with forward maintenance plan |

**Minimum for Domain tier**: Score 2
**Minimum for Operational tier**: Score 3

---

## Composite Score Calculation

```
Composite = (Coverage × 0.30) + (SKOS × 0.25) + (Interlinkage × 0.20) + (Alignment × 0.15) + (Freshness × 0.10)
```

**Maximum**: 4.0

### Tier Qualification Thresholds

| Tier | Minimum Composite | Per-Dimension Minimums | Additional Requirements |
|------|:-----------------:|----------------------|------------------------|
| **Inherited** | N/A | N/A | OT-021 exemption — no scoring obligation |
| **Domain** | 2.0 | Coverage >=2, SKOS >=2, Interlinkage >=2, Alignment >=3, Freshness >=2 | OT-003: >=25 terms, zero framework collisions |
| **Operational** | 3.0 | Coverage >=3, SKOS >=3, Interlinkage >=3, Alignment >=3, Freshness >=3 | OT-007: consuming skills + lifecycle integration |

---

## Scoring Template

Use this table when assessing an agent's ontology:

```markdown
### Ontology Quality Assessment: {agent-name}

**Date**: {YYYY-MM-DD}
**Assessor**: {who}
**Current Tier**: {inherited|domain|operational}
**Target Tier**: {domain|operational|N/A}

| Dimension | Weight | Score (0-4) | Weighted | Evidence |
|-----------|:------:|:-----------:|:--------:|----------|
| Coverage | 0.30 | | | {concept count, source} |
| SKOS Compliance | 0.25 | | | {structural check result} |
| Interlinkage | 0.20 | | | {relationship count} |
| Domain Alignment | 0.15 | | | {% domain-specific, KB grounding} |
| Freshness | 0.10 | | | {last modified date} |
| **Composite** | **1.00** | | **{sum}** | |

**Tier Qualification**: {PASS/FAIL} for {target tier}
**Gaps**: {dimensions below minimum, with remediation path}
**Recommendation**: {PROMOTE / DEFER / REMEDIATE}
```

---

## Integration with OT-022 (Concept Surplus)

When `/aget-analyze-ontology` reports CONCEPT_SURPLUS (concept:requirement ratio > 3:1):
- Coverage score may be high (3-4) but consumption is low
- This is not a rubric failure but a **signal to investigate**
- Check: Are concepts being used in EARS requirements? In skills? In session work?
- If not: ontology may be decorative despite high coverage score

---

## Anti-Patterns

| Anti-Pattern | Rubric Impact | Detection |
|--------------|---------------|-----------|
| Score-gaming: adding 25 trivial terms to pass OT-003 | Low Alignment score (0-1) | Terms don't appear in agent's KB or sessions |
| Copy-paste from another agent | Low Alignment + potential collision | `cross_reference_vocabulary.py` flags; terms don't match domain_area |
| All top-level concepts, no hierarchy | Low Interlinkage score (0-1) | Zero broader/narrower in YAML |
| Stale ontology never updated | Low Freshness score (0-1) | `git log -1 -- ontology/` shows old date |

---

## References

- ONTOLOGY_TIER_SPEC v1.0: Tier definitions (OT-001 through OT-022)
- L600: Ontologies Are AGET Artifacts (governance triad requirement)
- L542: Ontology Maturity Tiers (five-question diagnostic)
- L564: Ontology Adoption Is Demand-Side (demand evidence required)
- SOP_ontology_management.md: Production process
- ONTOLOGY_DOMAIN_TEMPLATE.yaml: Content structure template

---

*ONTOLOGY_QUALITY_RUBRIC_v1.0.md — "Score ontology quality, not just tier classification"*
*Created: 2026-03-23*
*Owner: private-supervisor-AGET*
