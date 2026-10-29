# Which products and commercial activities must the first workflow support?

ID: 03
Parent: ../map.md
Labels: wayfinder:grilling
Type: grilling
Mode: HITL
Status: resolved
Assignee: codex-root
Blocked by: none

## Question

Confirm initial product families, technical depth, goods and services, target countries, launch dates, manufacturing, import, distribution and sales activities, variants, and available evidence. The user has specified the US as primary, plus UK and EU. Ask only for missing choices, not facts the agent can retrieve. General consumer products are a provisional default, not a human answer.

## Comments

- 2026-10-19: Created during charting. No decision has been recorded.

- 2026-10-19: Claimed by codex-root for the user-requested interactive walkthrough. Product categories, scope defaults, commercial activities, and initial input expectations remain unsettled. No resolution recorded.

### Discussion round one, 2026-10-19

The user confirmed:

- Physical products only.
- Sales will mostly be through Amazon and the user's ecommerce website. Manufacturing will be done by partners in China.
- The US is the default assessment market. Additional markets are added only on instruction.
- Each market's analysis must be separate. An existing product can receive a later assessment for another market without replacing its earlier market analysis.

These are confirmed scope decisions within this ticket. The ticket remains claimed while discussing the treatment of China-specific manufacturing analysis and whether both supplier/private-label and custom-design sourcing routes are required. No inference about ownership, licenses, importer of record, or Chinese legal clearance has been made.

### Discussion round two, 2026-10-19

- The user stated that the business will never sell in China. China is a manufacturing location, not an intended sales market.
- The user asked why sourcing models matter; no sourcing restriction was chosen. Explain their role as product-specific provenance and evidence context, rather than requiring separate repository workflows.
- Do not infer that absence of China sales means manufacturing is legally cleared. CNIPA's reference translation of Patent Law Article 11 separately includes manufacturing among restricted acts: https://english.cnipa.gov.cn/art/2022/10/13/art_3068_179273.html, checked 2026-10-19.
- Proposed boundary, awaiting the user's answer: support all physical-product sourcing models, capture provenance per product, and keep any China-specific manufacturing-rights assessment optional and separate from the default US assessment.

### Resolution comment, 2026-10-19

The user accepted the recommended scope after the two discussion rounds above.

- Support physical products only, including existing supplier products, private-label modifications, and custom designs. Record the sourcing model and relevant provenance during product intake.
- Usual sales channels are Amazon and the user's ecommerce website. Manufacturing is performed by partners in China. Record actual product-specific suppliers, roles, variants, dates, and available evidence during intake rather than inventing those facts or imposing global launch dates.
- Default each product to a US assessment. Add another sales market only on instruction. Each market has separate analysis runs, findings, and reports; a later market assessment preserves the earlier market's work.
- Shared product evidence may be reused when applicable. Market-specific law, rights, status, dates, and conclusions require their own checks.
- China is never an intended sales market. China-specific manufacturing IP review is optional and separately scoped. If excluded, state that Chinese manufacturing rights have not been assessed. Do not interpret this exclusion as manufacturing clearance.

Acceptance evidence: the user replied "Accept recommended" to the proposed scope covering all sourcing models, US-first separate market assessments, and optional separate China manufacturing-IP review.

Applied to the root agent instructions, product-intake workflow, product template, and scope-exclusion reporting instructions. Evidence-model and workflow assurance choices remain on their own tickets.
