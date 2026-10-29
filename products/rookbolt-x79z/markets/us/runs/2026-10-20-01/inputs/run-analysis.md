# Run an analysis

Use this procedure for a saved, reproducible sequence of LLM tasks. A run is not a legal clearance certificate.

Save working outputs and reports as Markdown by default. Create PDF, Word, or other exports when requested without replacing the underlying source records. Accept a natural-language request for a full scoped run, focused workstream, new market, or changed-product review.

1. Read the product's intake and evidence inventory. Confirm the user's explicit objective and agreed scope; ask first if unclear. Identify the workstreams that apply to that objective and the ones excluded with reasons. If the task includes patent research, link the external search brief and any returned evidence, distinguishing awaited results from verified inputs.
2. Create `products/<slug>/markets/<market-id>/runs/<YYYY-MM-DD>-<sequence>/` from `templates/run/`. Default `<market-id>` to `us`. Add another market only on instruction. Use a new sequence when a date already has a run within that market. Never overwrite a completed run or another market's assessment.
3. Complete `manifest.md`. Snapshot the product revision, relevant feature and rights tables, source versions, legal references, and actual prompts under `inputs/`. Record the model and available tool details. Use `not exposed` where a system does not reveal a version or parameter.
4. Run [Scope and evidence check](../../../../../../../prompts/01-scope-and-evidence.md). Mark missing evidence and affected workstreams before comparison.
5. Run the applicable separate prompts for [utility patents](../../../../../../../prompts/02-patent-claims.md), [designs](../../../../../../../prompts/03-designs.md), [trademarks](../../../../../../../prompts/04-trademarks.md), and [copyright and adjacent rights](../../../../../../../prompts/05-copyright-and-adjacent.md). Save outputs under `outputs/` and complete the corresponding analysis templates.
6. Link each finding in `risk-register.md` to its feature, right, exact source locators, jurisdiction, activity, and analysis output. Apply [the risk-concern rubric](../../../../../../../workflows/rate-risk.md), with 1–5/U concern, separate business impact, evidence confidence, coverage, and uncertainty. Record current concern and any reassessed residual concern after completed, evidenced mitigation.
7. Use `challenge-plan.md` to select multiple relevant ways to test the assessment, documenting why any approach is excluded or unavailable. Run [Challenge the assessment](../../../../../../../prompts/06-challenge.md), preferably with a fresh context. For a blind retrieval check, supply the product facts and scope before showing prior conclusions. For an evidence audit, supply the actual evidence and results. Save outputs, objections, corrections, and limitations for each pass. Do not call these passes independent legal review or infer independence merely from a different model or role.
8. Resolve factual corrections and rerun affected comparisons. Preserve the earlier output and correction history.
9. Run [Prepare the review package](../../../../../../../prompts/07-report.md). Complete `report.md` and `review.md` under [the assurance and decision policy](../../../../../../../workflows/assurance-and-decisions.md). Escalate levels 4–5, decisive unknowns within required scope, stale evidence, and substantive interpretation disputes. Recommend appropriate review. Record actual legal review and the user's selling/launch decision only when received, without changing evidence completeness or concern scores merely because business risk was accepted.
10. Update the product's `decision-log.md` with the run path and actual decisions. Keep `overview.md` and its changelog current as run status, findings, blockers, and next actions change. Follow [the common changelog rules](../../../../../../../workflows/maintain-changelogs.md). Record refresh triggers. Keep any completed older reports and mark their applicability correctly.

## Required review gates

| Gate | Pass evidence | If it does not pass |
| --- | --- | --- |
| Scope | Product snapshot, relevant territories, activities, dates, and exclusions recorded | Exploratory screen only |
| Product evidence | Material features have inspected evidence | Affected comparisons unresolved |
| Rights evidence | Correct claims or representations and material records obtained | Affected comparisons unresolved |
| Status and territory | Dated verification appropriate to the right and intended activity | Status remains unknown |
| Traceability | Material conclusions cite product evidence and rights or legal sources | Correct or withdraw conclusion |
| Coverage | Agreed search scope completed or gaps made explicit | Incomplete coverage cannot imply clearance |
| Challenge | Adverse evidence and reviewer objections addressed or retained | Show unresolved concerns |
| Approval record | Any claimed legal review or business acceptance has an actual record | Do not claim approval |

A report may be useful while incomplete. Its status must remain incomplete where missing evidence prevents a material conclusion. `No material concerns identified within scope` requires the relevant evidence gates to pass and does not override excluded or unsearched areas.

## Trigger a new run

Start a new run for a material product change, new brand or market, changed launch or activity, new relevant right, status change, material legal change, corrected evidence, or a scheduled review date chosen for that product. Assess whether the event affects earlier findings. Do not apply one arbitrary expiration period to every product.

## Request, resume, and rerun scoped work

Support a full scoped assessment, a focused workstream, a new-market assessment, or a product-change review according to the user's actual objective. Do not silently expand a focused request into a full FTO assignment.

For unfinished work, resume from the saved manifest and stage state. Record which inputs and outputs remain applicable. When an input changes, rerun its affected downstream stages and explain what was carried forward. For completed runs, preserve their original inputs and reports and create a new run or dated addendum where relevant. Reusing unchanged source material does not automatically make earlier status, legal interpretation, or market conclusions current.
