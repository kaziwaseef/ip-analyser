# Evidence-model proposal

Review aid, 2026-10-19. The initial choices were accepted by the user; the parent ticket records the canonical resolution and added changelog requirements. Parent ticket: [What evidence and provenance are necessary for a reproducible product assessment?](../issues/04-evidence-model.md).

## Proposed evidence lifecycle

| Moment | Agent action | Preserved evidence or outcome |
| --- | --- | --- |
| Product first supplied | Accept a name and available description, listing, or images; ask focused follow-up questions | Supplied facts and explicit unknowns |
| Research | Capture permitted originals, source identifiers, URLs, retrieval dates, and exact relevant locators | Original files separate from OCR, translations, and summaries |
| Product comparison | Link each material feature to inspected product evidence | Stable feature and source IDs assigned by the agent |
| Run starts | Freeze a dated product revision and the evidence actually used | A market-specific input snapshot and manifest |
| Another market is requested | Reuse applicable product evidence and independently check market-specific rights, status, rules, and dates | Separate analysis and conclusions without overwriting the first market |
| Material evidence is missing | Continue useful exploratory work, keeping affected findings unresolved | Explicit gaps rather than a favorable final conclusion |

The existing `templates/product/` and `templates/run/` files illustrate these records. The agent maintains the bookkeeping; the user supplies facts and documents they have.

## Initial discussion choices

1. Allow exploratory analysis while material evidence is missing, keeping affected conclusions incomplete.
2. Preserve permitted originals with source links, dates, and exact locators; keep summaries, OCR, and translations as derivatives.
3. Freeze the product revision and evidence set used by each market run, reusing only applicable shared product evidence across markets.

The user accepted all three. The parent ticket holds the decision details and the user's additional overview/changelog requirements.

## Cases checked against the accepted rules

- Another application in a relevant patent family is found. Does it receive its own record and scope/status checks instead of inheriting another member's result?
- Relevant unregistered-right evidence is a competitor's dated product page. How is it captured and how is ownership or copying uncertainty retained?
- An official register is inaccessible. Does the run preserve the candidate and unknown status while continuing unaffected analysis?
- An image is missing or an OCR/translation passage is uncertain. Which conclusions stay incomplete and which derivative checks are needed?

Confidential-data service choices remain with the tool/data-policy ticket. This evidence discussion can identify handling requirements without preapproving external disclosure.
