# Challenge methods and residual-risk metrics

Research and primary-source verification date: 2026-10-19.

This research supports [Which challenge methods and risk dimensions should inform the assessment?](../wayfinder/ip-workspace/issues/10-challenge-risk-methods.md). It proposes methods for a physical-product, US-first workspace with separate market assessments. The user has requested several ways to challenge an assessment and a metric that preserves residual risk. The methods, scoring anchors, and escalation policy below remain proposals for the human pipeline and assurance decisions. No product has been assessed.

## Why one review pass is insufficient

Different checks find different failures. A second reader cannot audit a right that the search never retrieved. A perfect citation does not prove that the cited claim governs the product. A product photograph does not establish an internal mechanism. The proposed process therefore tests retrieval, evidence, interpretation, scope, and changes separately.

WIPO organizes informal FTO around the invention, countries, and time frame. Its guide separates search, claim comparison, legal status, and reporting. Module V describes errors in product understanding, retrieval, translation, data, and interpretation, and explains why these risks cannot be eliminated. [WIPO, *Identifying inventions in the public domain*, 2020, Modules I and IV–V, printed pages 24–26 and 65–98](https://www.wipo.int/edocs/pubdocs/en/wipo_pub_1062.pdf).

The following challenge methods are this workspace's proposed implementation. They are not WIPO certification criteria or a validated recipe for clearance.

## Different ways to challenge an assessment

### Blind second retrieval

Give another search session the frozen product description, feature evidence, market, activities, dates, and scope. Withhold the first search's candidates and conclusions until that session saves its own strategy and results. Then reconcile the two searches.

The second search should vary the route: component and mechanism terms, functional synonyms, CPC or IPC classes, competitors, inventor and assignee names, citations, or image searches as applicable. Record which routes actually differed. A second interface backed by the same database and query may provide little added coverage.

The reconciliation records new candidates, missed feature groups, repeated exclusions, and why results differ. Overlap does not establish completeness. The USPTO's preliminary search guidance combines descriptive terms, verified classifications, document review, and broader sources. That guidance concerns preliminary prior-art searching, so it supports search diversity rather than a product FTO conclusion. [USPTO, *Applying for patents*, “Search for patents and prior art,” six-step strategy](https://www.uspto.gov/patents/basics/apply).

### Strongest adverse-party case

For each close right, ask a reviewer to construct the strongest evidence-supported argument that the relevant activity falls within that right. The reviewer identifies the exact claim, image, sign, or expression and the product facts needed for the argument.

Then require the assessment author to answer that argument with cited evidence. Keep both arguments, including unresolved disagreements. A reviewer must not invent hidden features, ownership, copying, or legal rules to make the case stronger. Label hypothetical facts and identify the evidence that would test them.

This pass tests whether the original assessment relied on a convenient interpretation or ignored adverse evidence. It is an internal challenge exercise, not a prediction of an actual claimant's conduct.

### Evidence and citation audit

A reviewer opens the original evidence behind every decisive favorable or adverse finding. The audit checks the document identifier, country, claim version, dependent-claim inheritance, quoted wording, figure or page, translation, status date, and matching product revision.

Classify defects as unsupported, mismatched, incomplete, outdated, or corrected. A broken link remains a problem until the underlying source is obtained and checked. Saving a document is different from verifying what it says.

Require verification of decisive assertions before closing the review. Sampling less consequential supporting material is a separate efficiency choice. Preserve the audit list so an apparently favorable finding remains reviewable.

### Feature and interpretation sensitivity

List the facts and interpretations on which a conclusion depends. Change one assumption at a time: a hidden latch, a material, an included accessory, an alternative assembly, a broader plausible claim reading, or the identity of the party importing the product.

Show which findings change and which do not. For an unknown physical feature, use explicitly conditional scenarios until a sample, drawing, measurement, or supplier answer establishes it. Plausible claim-construction or equivalence disputes need jurisdiction-specific legal review.

The useful output is a sensitivity table with the baseline assumption, alternative, affected finding, possible consequence, and next evidence request. A redesign that changes the result requires a new product revision and a new assessment of that revision. A suggested change is not an implemented mitigation.

### Visual design challenge

Use the complete protected representations and matching product views. Ask one reviewer to describe the strongest overall visual similarity and another to explain the most important differences, with precise image references. Check whether perspective, scale, lighting, missing views, or disclaimed matter distort the comparison.

In US design-patent work, the ordinary-observer inquiry concerns the overall claimed design in its prior-art context. A count of matching details or an image-similarity percentage does not apply that test. [Federal Circuit, *Lanard Toys Ltd. v. Dolgencorp LLC*, 14 May 2020, discussion of design-patent infringement, opinion pages 7–13](https://www.cafc.uscourts.gov/opinions-orders/19-1781.opinion.5-14-2020_1587770.pdf).

Missing usable images keep the affected finding unresolved. UK and EU design work needs its own legal test and territorial evidence.

### Family, territory, status, and date review

A separate pass checks that the assessment has not substituted one family member, foreign outcome, database badge, or old claim set for the right actually relevant to the market. Each candidate gets its own territorial and status record.

Revisit close excluded candidates, related live or pending members, and the claims actually used in comparison. Review material changes between search date and intended activity. Record what changed, what did not, and what could not be checked. An expired parent is not a reason to discard every related candidate.

This pass produces a dated delta list. A new market needs a separate assessment even if it reuses product evidence. WIPO's legal-status and reporting sections explain why territorial status and later amendments can change the assessment. [WIPO guide, Module IV, printed pages 84–92, and Module V, pages 96–98](https://www.wipo.int/edocs/pubdocs/en/wipo_pub_1062.pdf).

### Cross-right and provenance challenge

Ask what the patent-focused analysis missed: a brand, packaging presentation, surface artwork, product shape, copied supplier photography, or another relevant right. Keep excluded workstreams visible, with reasons and scope consequences.

A negative patent search does not answer those questions. The USPTO warns that a dead federal trademark record may still correspond to use supporting common-law rights. The Copyright Office explains that absence from its records does not establish that a work is unprotected. [USPTO, *Federal trademark searching*, “Live and dead trademarks”](https://www.uspto.gov/trademarks/search/federal-trademark-searching), [Copyright Office Circular 22, “Searches not always conclusive,” printed pages 4–5](https://www.copyright.gov/circs/circ22.pdf).

Supplier assurances are evidence to examine. Record the actual license or agreement, covered product and territory, source of design, and gaps. Do not turn a supplier statement into an inferred license.

### Disagreement review and expert escalation

The final reviewer lists unresolved disputes instead of voting on a preferred answer. Each dispute needs competing positions, evidence, why the difference matters, and a proposed resolution route. A technical issue may need a product sample or engineer. Claim interpretation, equivalents, ownership, and other legal issues may need a qualified professional for that jurisdiction.

A fresh conversation reduces exposure to the initial narrative. A different model can offer another view. Neither proves statistical independence. NIST identifies correlated failures associated with repeated model use and warns that generated reasoning and citations can be false. Its suggested actions include independent evaluations, source verification, and avoidance of broad capability claims from narrow tests. [NIST AI 600-1, July 2024, sections 2.2 and 2.6, introduction footnote 3, GV-3.2-001, and MS-2.5-001/003](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).

Model agreement is supporting process information, not a probability of correctness. These IP review proposals adapt broader evaluation principles. NIST does not validate their IP accuracy.

## A proposed metric without invented probabilities

Use an ordinal concern level for each finding. Keep concern separate from the report's assessment state and the user's decision. The anchors below are proposed internal screening categories. No study or cited authority calibrates these levels to infringement probability, litigation outcome, or launch safety.

| Level | Proposed meaning | Evidence needed for assignment |
| --- | --- | --- |
| U | Unassessable | A decisive product fact, document, legal status, or interpretation is missing. State the missing item and the possible adverse outcome. |
| 1 | Low identified concern | Completed scoped comparison and review find no material concern. Explain the favorable basis and remaining limitations. This never means zero risk. |
| 2 | Limited concern | A specific issue remains, but the reviewed evidence supports a bounded concern. Describe the condition and action rather than relying on the label. |
| 3 | Material concern | A plausible adverse case or unresolved substantive dispute warrants further investigation or mitigation. |
| 4 | High concern | Substantial evidence supports a close conflict requiring focused legal or technical review and a documented response. |
| 5 | Critical concern | The reviewed record shows an acute conflict or unresolved adverse event requiring urgent decision-maker attention. An assertion alone does not prove infringement. |

U is not a number. It cannot lower an average or become level 1 because the search found few candidates. Where a known concern and a decisive unknown coexist, record both. For example, “concern 3, unresolved mechanism evidence” is more informative than replacing the whole finding with a reassuring number.

A run summary should display the highest identified concern, all material unknowns, and the distribution of findings. Do not average away one serious right with many low-concern results. “Highest concern 1; coverage partial” must remain visibly incomplete where a required coverage gap prevents a scoped conclusion.

Every finding should retain separate fields:

- Business impact and exposure. Record affected SKUs, channels, inventory, commitments, expected sales, territory, substitution cost, redesign time, and possible disruption scenarios. Use supplied figures and clearly stated assumptions. A legal concern and the cost of responding to it are different questions.
- Evidence confidence. Use low, medium, or high with reasons about authenticity, specificity, consistency, completeness, and directness. High confidence can support an adverse finding.
- Search coverage. Report completed and missing work by feature, right type, source, territory, dates, and method. A denominator such as “all eight planned mechanism searches completed” describes process completion. It does not measure the percentage of relevant rights found.
- Uncertainty and residual risk. Name unknown rights, missing evidence, interpretation disputes, search blind spots, future amendments, and freshness limits. Identify the next useful action or explain why the uncertainty remains.
- Response and review. Record proposed action, owner, due trigger, evidence of completion, remaining concern after the action, and who actually reviewed it. Keep business acceptance separate.

## Alternatives and trade-offs

A likelihood-by-impact matrix can help prioritize business scenarios if the event and time horizon are explicit. “An infringement finding,” “a complaint,” and “a platform disruption” are different events. The workspace has no calibrated data for their likelihoods. Multiplying guessed likelihood and impact numbers would conceal uncertainty rather than resolve it.

FMEA-style occurrence, severity, and detectability scores can organize failure scenarios. For this workspace, detectability would overlap with coverage and missing evidence. Multiplying ordinal scores could also give a serious issue the same total as several modest ones. That is a reason to keep the dimensions separate here, not a finding that FMEA is universally unsuitable.

A single traffic light is easy to scan but loses the basis, uncertainty, and response. A numerical probability would need a defined event, representative outcome data, calibration, and validation that this workflow currently lacks.

NIST SP 800-30 permits qualitative and quantitative approaches, calls for explicit uncertainty and assumptions, and treats its scales as starting points for tailoring. It does not validate this proposed IP rubric. [NIST SP 800-30 Revision 1, September 2012, sections 2.3.1–2.3.2, task 2-6, and Appendix I](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-30r1.pdf).

The recommended discussion choice is therefore an ordinal concern scale plus separate exposure, evidence, coverage, and uncertainty. The human still needs to choose mandatory challenge passes, escalation triggers, and the authority for release decisions.

## Residual risk in an apparently clear result

A favorable scoped result should explain why concern is low and what remains. US publication exceptions leave some patent applications unavailable to ordinary public searching. [USPTO, *Helpful hints regarding publication of patent applications*, nonpublication-request guidance](https://www.uspto.gov/patents/laws/american-inventors-protection-act-1999/helpful-hints-regarding).

Other residual risks include an undiscovered right, an incomplete product description, an unregistered right, a disputed interpretation, or a change after the assessment date. Record these as concrete limitations with refresh triggers. “No material concerns identified within scope” can coexist with level 1 concern and nonzero residual uncertainty. It cannot promise that every relevant right was found, issue a legal clearance seal, or backfill legal review or business acceptance.
