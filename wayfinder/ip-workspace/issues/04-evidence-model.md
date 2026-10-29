# What evidence and provenance are necessary for a reproducible product assessment?

ID: 04
Parent: ../map.md
Labels: wayfinder:prototype
Type: prototype
Mode: HITL
Status: resolved
Assignee: codex-root
Blocked by: 01, 03

## Question

Review the provisional product template with the user. Decide product versioning, feature IDs, right and family IDs, source capture, date and territorial scope, exact claim and image locators, authoritative status checks, translations, missing-data treatment, confidentiality, and reproducible run manifests. Stress-test a continuation, an unregistered right, and an inaccessible register.

## Comments

- 2026-10-19: Created during charting. No decision has been recorded.

- 2026-10-19: Claimed by codex-root after the product-scope decision was resolved. Starting the user-requested next interactive discussion. The existing product and run templates are working drafts, not an accepted evidence policy.
- The upstream prototype skill was read. Its code/UI examples are adapted to a document prototype because the user requested a work repository and no application is needed. Review asset: [Evidence-model proposal](../assets/evidence-model-proposal.md). No evidence-model decisions are resolved yet.

### Resolution comment, 2026-10-19

The user accepted all three evidence recommendations and added an explicit repository-wide changelog requirement.

- A description, listing link, or photos can start exploratory research. Missing material evidence leaves affected conclusions incomplete, while useful unblocked work continues.
- Preserve permitted original documents with source URLs, retrieval dates, and exact claim, page, or image references. Keep summaries, OCR, translations, and other derivatives separate from originals, with uncertainties visible.
- Freeze the product revision and evidence actually reviewed by each market run. Later material changes trigger a new run where relevant. Reuse applicable shared product evidence while retaining separate market assessments.
- The agent maintains stable source, feature, right, search, and finding IDs and the run manifest. Do not merge related territorial rights or different claim versions into one verified result.
- Every product has an `overview.md` covering current state, market-assessment links, evidence and decision references, blockers, next actions, and an embedded changelog. Its product `AGENTS.md` requires updates as meaningful changes happen.
- All changelogs, standalone or embedded, retain the newest ten individual entries, newest first. Overflow is folded into a cumulative final Old change summary section. Preserve the substance and useful source links already summarized. Supporting evidence, decision records, search history, frozen inputs, and completed reports remain intact.

Acceptance evidence: the user answered "Yes" to exploratory research and source preservation, "Yes" to frozen assessment inputs, and expressly requested a per-product overview plus the common ten-change/old-summary rule.

Applied consequences of the accepted incomplete-evidence rule, checked by the agent against the discussion cases:

| Case | Required record and handling |
| --- | --- |
| Another application in a patent family | Its own relevant identifier, claim version, territorial/status checks, and source links; no inherited clearance from a related member |
| Unregistered-right candidate on a product page | Preserve permitted dated page/image evidence and its provenance; retain unknown ownership, dates, and copying facts |
| Official register inaccessible | Record the attempted check, candidate, and unknown status; affected conclusions remain incomplete while other work continues |
| Missing images or uncertain OCR/translation | Preserve originals and uncertainty; affected visual or text-dependent comparisons remain incomplete |

These are applications of accepted rules, not completed product assessments. Confidential-data service permissions remain on the tool/data-policy ticket. No third-party sharing was approved.

Implementation: root `AGENTS.md`, `CHANGELOG.md`, `workflows/maintain-changelogs.md`, the product overview and agent templates, and the intake/research/analysis/maintenance workflows. The [evidence-model review asset](../assets/evidence-model-proposal.md) preserves the discussion context.
