# What separate analysis stages and review gates make the LLM pipeline defensible?

ID: 05
Parent: ../map.md
Labels: wayfinder:prototype
Type: prototype
Mode: HITL
Status: resolved
Assignee: codex-root
Blocked by: 01, 04, 10

## Question

Decide intake gates, broad discovery, family and territory verification, utility claim mapping, visual design comparison, trademark confusion review, copyright and provenance review, independent challenge, consolidation, and refresh. Agree on input/output contracts, evidence citations, uncertainty, invalidation triggers, and how a human can rerun the work through prompts and external tools.

## Comments

- 2026-10-19: Created during charting. No decision has been recorded.

- 2026-10-19: Claimed by codex-root for the next sequential interactive discussion after the evidence-model decision was resolved. Review asset: [Analysis-pipeline proposal](../assets/analysis-pipeline-proposal.md). This is a document prototype matching the requested work repository; no application or automatic external integration is being built. Pipeline choices remain open.

### Discussion round one, 2026-10-19

- The user accepted the separate-stage pipeline with saved inputs, outputs, and explicit gaps.
- The user requires the agent to ask for the objective at the start when it is not explicit, and set the scope before dependent work. Do not default every task to all IP workstreams.
- The user will also search with external tools and requires a detailed, product-specific prompt for their dedicated patent-search AI after intake. Support manual handoff and result import without assuming an integration or sending anything automatically.
- The user requests multiple approaches to challenge the assessment and a risk metric reflecting residual risk even where findings appear clear. Research methods and a proposed rubric are being prepared; no numeric scale, thresholds, or clearance wording has been accepted.
- Related research: [Which challenge methods and risk dimensions should inform the assessment?](10-challenge-risk-methods.md). Continue the independently authorized intake/handoff work while that research runs.

### Research and implementation update, 2026-10-19

[Challenge-method and residual-risk research](10-challenge-risk-methods.md) is resolved and indexed on the map. No human scoring-policy decision was inferred from the research.

The accepted requirements are implemented in objective-first scope instructions, `workflows/external-patent-search.md`, the self-contained external-AI prompt template, the handoff manifest and result-import controls, and a multi-approach challenge plan. The user need not use a particular external provider, and no search or integration was executed.

Review aid: [Proposed challenge and residual-risk rubric](../assets/risk-rubric-proposal.md), supported by [the dated research note](../../../knowledge/challenge-and-risk-methods.md). Discuss whether to adopt a scope-appropriate default mix of review methods and the ordinal 1–5/U concern scale with separate impact, confidence, coverage and residual risk. The pipeline ticket remains claimed while these choices are discussed.

### Resolution comment, 2026-10-19

The user accepted the recommended challenge approach and 1–5/U concern metric after reviewing the sourced methods and the proposed scale. Together with the previous discussion, this settles the pipeline design.

- Establish the user's actual objective first, asking when it is not explicit. Set the work scope and deliverable from that objective rather than automatically including every IP workstream.
- Use separate stages for scoped intake, discovery, document/status verification, relevant comparisons, multiple challenges, and a review package. Save inputs, outputs, prompts, execution limits, and gaps in the market run's manifest.
- After patent-related intake, prepare the detailed self-contained prompt for the user's dedicated patent-search AI. Accept evidence from that AI and other external tools, preserve provenance, and verify material original sources before relying on returned analysis. No submission, account connection, or successful search is inferred from a prepared prompt.
- Use a documented scope-appropriate mix of blind alternate retrieval, strongest supported rights-holder argument, decisive-source audit, feature/interpretation sensitivity, family/market/date checks, and visual/provenance counterchecks. Record actual execution, omissions, disagreements, and necessary reruns. Model agreement is not statistical independence or legal review.
- Adopt concern levels 1 low identified concern with residual risk, 2 limited, 3 material, 4 high, 5 critical, and U unassessable. There is no zero. Preserve known adverse evidence and decisive unknowns. Scores are ordinal judgments, not probabilities.
- Keep business impact, evidence confidence, coverage, and remaining uncertainty separate. Show the highest known material concern plus unresolved areas rather than an averaged clearance score. Compare current concern with residual concern only after completed, evidenced mitigation. The user did not separately choose a numerical business-impact scale; report actual exposure and scenarios.
- Support full scoped assessments, focused workstreams, new-market assessments, product-change reviews, and resumption from saved stage state. Carry forward only applicable evidence, rerun affected stages after changed inputs, and preserve completed reports.
- Keep product-specific search stopping rules tied to the actual product and agreed scope. Final assurance wording, escalation/release policy, and tool/data permissions remain on their respective tickets.

Acceptance evidence: the user's "Accept recommended" reply accepted the listed challenge approaches and 1–5/U concern metric with separate impact/evidence measures. The earlier "1. Yes" accepted the separate-stage pipeline, and the user's explicit additions required objective-first scoping and the patent-search-AI handoff.

Implementation: [Risk-concern workflow](../../../workflows/rate-risk.md), [external search workflow](../../../workflows/external-patent-search.md), [analysis workflow](../../../workflows/run-analysis.md), corresponding prompts, run templates, and root agent instructions. [The review aid](../assets/risk-rubric-proposal.md) records the discussion context. No product risk rating or release approval was issued.
