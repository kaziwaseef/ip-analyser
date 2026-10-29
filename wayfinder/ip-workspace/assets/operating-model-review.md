# Operating-model review

Review aid for [Does the repository structure and agent contract support the intended work?](../issues/08-operating-model.md), 2026-10-19. The existing files are the document prototype. The user accepted the layout, Markdown/report defaults, and event-driven resumption/refresh conventions. The parent ticket records the canonical resolution. Earlier decisions remain in force.

## Product workspace layout

```text
products/<product-slug>/
  overview.md                 Current state, market links, blockers, rolling changelog
  AGENTS.md                   Product-specific instructions and accepted defaults
  product.md                  Product facts, revisions, sourcing, activities
  intake.md                   Explicit objective, scope, questions, next actions
  features.md                 Stable feature IDs and supporting evidence
  rights.md                   Candidate rights across identified territories
  search-log.md               Queries and results with explicit market scope
  tool-register.md            Actual tools, reusable grants, access and source limits
  decision-log.md             Supporting decision records and assessment history
  evidence/
    index.md                  Source provenance, locators, derivatives
    raw/                      Permitted originals, including ordinary private documents
    derived/                  OCR, translations, crops, and summaries
  markets/<market-id>/
    search-briefs/<date>-<sequence>/
      prompt.md               Self-contained external patent-search instructions
      manifest.md             Scope, attachment, disclosure and return references
    runs/<date>-<sequence>/
      manifest.md             Frozen inputs, prompt/model/tool records, stage state
      inputs/                 Actual input snapshots
      outputs/                Stage results and challenge outputs
      ...                     Comparisons, challenge plan, risk register, report, review
```

Folders are created when useful; the outline does not require empty folders or invented evidence. No sample product is being treated as real work.

## Accepted conventions

1. Keep one stable lower-case product slug. Use `us` for the default market, `uk` when requested, and another explicit market key when needed. An `eu` assessment must identify its member-state coverage; changing that scope needs an explicit new assessment/run rather than silently expanding an old report. Preserve each market's analysis history.
2. Use ISO dates and a unique sequence for handoffs and runs. Shared product evidence and candidate indexes remain linked to their territories; they do not merge market conclusions.
3. Use `overview.md` as the starting point and navigation summary. Product facts, source records, saved comparisons, and decisions remain in their canonical files. Agents keep the overview and rolling changelog consistent as changes happen.
4. Keep Markdown as the default working and report format. Create PDF, Word, spreadsheet, or other exports when requested, without replacing the underlying evidence and assessment records.
5. Accept natural-language instructions such as create a product, prepare its search prompt, import these results, run a scoped assessment, add a market, or reassess this revision. Ask only when objective or necessary facts are unclear; resume applicable saved work.
6. Refresh on material product, market, evidence, right-status, or legal changes, and when a product-specific review date is set. Check current information when it matters to a consequential decision. No automatic background monitoring is implied; configure it only as a separate explicit task.

## Already settled, not reopened here

Physical products only; Amazon/ecommerce sales; China manufacturing context; US-first separate market assessments; scoped external-search handoffs; preserved originals and frozen runs; multiple challenge approaches; 1–5/U concern with separate exposure/evidence/coverage; user release authority; ten-entry changelogs with cumulative older summaries; public/existing tools first; reusable external-sharing grants; normal document storage in the intended private GitHub repository with credentials outside repository files.

## Review outcome

The user accepted the recommended layout, Markdown defaults, and event-driven refresh/resumption. The pilot-selection and acceptance-criteria decision remains open. No prototype or template is a real product assessment.
