# Proposed challenge and residual-risk rubric

Review aid, 2026-10-19. The user accepted the challenge approach and 1–5/U concern metric. The adopted operational rule is `../../../workflows/rate-risk.md`. This internal prioritization rubric is not a validated legal risk scale, measured infringement probability, or product assessment. Parent decision: [What separate analysis stages and review gates make the LLM pipeline defensible?](../issues/05-analysis-pipeline.md). Primary-source methodology research: [Which challenge methods and risk dimensions should inform the assessment?](../issues/10-challenge-risk-methods.md).

## Use several different challenges

Choose the methods relevant to the agreed objective and record actual execution and limits in the run's challenge plan.

| Method | What it tests | Example of an objection to preserve |
| --- | --- | --- |
| Source and evidence audit | Whether the report accurately represents its sources and the product | The chart quotes a pending claim instead of the granted claim |
| Blind second search | Whether different query routes find candidates missed by the first search | Classification and citation searches identify a family absent from the keyword search |
| Rights-holder argument | The strongest plausible adverse interpretation supported by evidence | A claimed relationship may be present even though the component has a different marketing name |
| Sensitivity analysis | Whether uncertain product facts or interpretations control the conclusion | A different answer about the internal mechanism changes a limitation mapping |
| Family, market, and time check | Whether related rights, territorial effects, status, or revisions were missed | A different family member or product revision needs a separate comparison |
| Workstream-specific countercheck | Whether visual, marketplace, provenance, or permission evidence was overlooked | A missing design view or license restriction changes the analysis |

A practical default is a source audit, an adverse argument, and sensitivity checks, plus a different-route retrieval check for an FTO research assignment. Use family/territory/date checks where patent records matter and visual or provenance checks when those workstreams are in scope. Record why a selected pass was unavailable. Do not pretend one model using several role labels is several independent experts.

## Proposed IP risk-concern score

Apply this only to a scoped risk assessment with actual comparisons. A search-only report may rank candidates for review without asserting an assessed product-risk score.

| Score | Meaning | Evidence condition |
| --- | --- | --- |
| 1 | Lowest assessed concern; residual risk remains | No material concern found within completed agreed scope, with decisive facts and source checks sufficient; record search and interpretation limits |
| 2 | Limited concern | A specific supported issue warrants follow-up or a limited mitigation, with the basis and remaining uncertainty stated |
| 3 | Material unresolved concern | Plausible overlap, permission restriction, or interpretive dispute requires substantive follow-up |
| 4 | High concern | Strong adverse evidence or a substantial unresolved conflict warrants urgent mitigation or qualified review |
| 5 | Critical concern | The supported issue requires immediate decision-maker attention because the scoped activity has a serious unresolved IP obstacle; do not equate this label with a court finding |
| U | Unassessable | A decisive fact, claim/view, source, status, or scope check is missing or unreliable |

No score of zero exists. Level 1 is not risk-free. Use U for a decisive unknown rather than making incomplete evidence look like a favorable score. These bands are qualitative ordinal judgments, not calibrated likelihoods, percentages, equal-sized intervals, or universal legal thresholds. Every rating needs scenario, evidence, and reasoning.

## Show dimensions separately

- Business impact: describe the actual scenario, affected channels, inventory, redesign and delay exposure when known. Keep missing inputs explicit and do not invent revenue or damages. The accepted concern scale does not imply a separately calibrated numerical impact scale.
- Evidence confidence: low, medium, or high, with the reason and remaining source or interpretation problems.
- Search coverage: limited, expanded, or completed for the agreed scope, supported by the search log, follow-up, exclusions, and inaccessible areas. Completed scope is not an exhaustive-search claim.
- Current and residual concern: distinguish risk before a completed mitigation from what remains afterward. A proposed redesign, future search, or hoped-for license is not a completed mitigation.
- Residual-risk explanation: include relevant possibility of missed documents, later publication or status change, unregistered-right evidence limits, unsettled interpretation, and errors in product facts or model analysis. Say which uncertainty actually applies.

Do not multiply concern and impact into an infringement probability or average findings into clearance. The product summary retains the highest material known concern plus unresolved/U areas, rather than hiding them in a mean. Consider cumulative scenarios when supported. A required incomplete workstream stays incomplete even if every completed finding is low concern.

## Proposed review rules for discussion

1. Use a documented mix of challenge approaches, with a source audit for material findings and scope-appropriate alternate retrieval, adverse argument, and sensitivity checks.
2. Use the 1–5/U concern scale with separate impact, evidence confidence, coverage, and residual-risk reasons.
3. Keep final status wording, decision authority, accepted thresholds, and any requirement for qualified legal review on the separate FTO-assurance ticket.

The user accepted the recommended challenge approach and 1–5/U concern metric. The parent pipeline ticket records the resolution. The FTO-assurance ticket now records the accepted report, release-authority, and escalation policy; follow `workflows/assurance-and-decisions.md` for its operational rules.
