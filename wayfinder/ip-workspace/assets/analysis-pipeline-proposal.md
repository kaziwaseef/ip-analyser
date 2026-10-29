# Analysis-pipeline proposal

Review aid, 2026-10-19. The user has accepted the pipeline requirements, challenge approach, and 1–5/U concern metric. Parent decision: [What separate analysis stages and review gates make the LLM pipeline defensible?](../issues/05-analysis-pipeline.md). The parent ticket records the canonical decision and the workflows implement it. This document is not evidence that an external integration or actual product assessment has run.

## Proposed stages and evidence contracts

| Stage | Inputs | Saved output | Missing-input behavior |
| --- | --- | --- | --- |
| Scope and intake | Product revision, requested market, commercial activities, supplied evidence | Scope statement, feature inventory, questions and gaps | Exploratory work only for affected questions |
| Discovery | Product features, owner/competitor leads, available permitted tools | Exact queries, coverage record, candidates, exclusions and follow-ups | Record unavailable searches and limited coverage |
| Retrieve and verify | Candidate identifiers, source access, original documents | Operative claims/representations, provenance, dated territorial/status checks | Retain unknown facts and affected incomplete findings |
| Separate comparisons | Verified relevant rights, product evidence, applicable legal sources | Patent claim charts, visual design comparisons, trademark and copyright/provenance findings as applicable | Never infer favorable outcomes from absent evidence |
| Challenge | Inputs, saved comparisons, sources, gaps and findings | Separate critique, corrections, unresolved disagreements and rerun needs | Record whether the challenge was possible and its limits |
| Review package | Findings, coverage, challenge and actual human decisions | Market-specific report, risk register, actions and refresh needs | Keep unknowns and incomplete results explicit |

Each stage links its actual inputs, prompt, model/session information, tool use, and outputs in the run manifest. The agent updates the product overview and changelog as meaningful work changes, following the accepted retention rule.

## Choices for the first discussion round

1. Adopt the staged pipeline above, with saved outputs and explicit gaps at each step.
2. Cover all applicable core rights workstreams; document why a workstream is excluded rather than silently skipping it.
3. Require a separate LLM challenge pass before treating an assessment as fully reviewed; prefer a fresh context and record actual review limitations. A preliminary result can still be useful while awaiting that pass.

## User responses and current review aid

The user accepted separate stages and required objective-first scoping, an external patent-search-AI handoff after intake, multiple ways to challenge findings, and a metric preserving residual risk. The scope must follow the explicit task rather than automatically including every IP workstream. The repository now provides the handoff workflow, standalone search-prompt template, import checks, and a multi-approach challenge plan.

Research: [Challenge methods and residual-risk metrics](../../../knowledge/challenge-and-risk-methods.md).

Next review aid: [Proposed challenge and residual-risk rubric](risk-rubric-proposal.md). The challenge approach and 1–5/U concern scale are accepted; `workflows/rate-risk.md` is the adopted operational rubric. The separate FTO-assurance ticket records the now-accepted report purpose, authority, and escalation rules.

## How the agreed pipeline handles follow-up work

- The explicit user objective selects a full scoped run, one workstream, a new-market assessment, or a product-change review.
- Saved manifests and stage outputs support resumption. Carry forward only applicable evidence; changed inputs trigger the affected downstream stages and market-specific checks.
- Completed inputs and reports remain preserved. Current status, product revision, source versions, review limits, and remaining risk are recorded separately.
- The separate FTO-assurance decision is resolved and implemented in `workflows/assurance-and-decisions.md`. The tool/data policy is also resolved on its own ticket, including the user's private-repository storage preference.
- Search stopping rules and pilot-specific search depth depend on a concrete product; no arbitrary universal search-completeness promise is made.
