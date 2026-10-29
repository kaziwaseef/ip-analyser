# Product workspaces

Each product gets its own directory, created from [the product template](../templates/product/README.md) through [Create a product](../workflows/create-product.md).

Start in that product's `overview.md` for its current state, market assessments, blockers, and changelog. Agents update it as changes happen. Every changelog follows [the common ten-entry and older-summary rule](../workflows/maintain-changelogs.md).

## Products

- [ROOKBOLT X79Z](rookbolt-x79z/overview.md): first US assessment delivered on 2026-10-20; incomplete with material follow-up concerns and decisive unknowns.

A product workspace, template, or research note does not constitute a completed assessment.

Keep each product's market-specific runs under `markets/<market-id>/runs/`, with `us` as the default. A later market assessment preserves the earlier market's work. Product facts and original sources can be shared, while conclusions and applicability checks stay market-specific.

Use stable lower-case slugs such as `folding-phone-stand`. Keep variants together only when their evidence and differences can be tracked explicitly. Create separate products when scope or ownership warrants separate records.

Use explicit market keys such as `us` and `uk`. An `eu` assessment names its covered member states. Keep uniquely dated/sequenced search briefs and runs under their market. Markdown is the default report format; exports are created when requested. Start from the saved overview and stage state when resuming work.
