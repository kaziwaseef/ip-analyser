# Product template

Copy this directory's contents into `products/<slug>/` through [Create a product](../../workflows/create-product.md). Replace `{{product_id}}`, `{{product_name}}`, and `{{created_date}}`. A product directory is working material, not a completed assessment.

Read `overview.md` first, then the linked product facts and intake questions. Keep the overview's current state and changelog updated as changes happen. Its changelog retains ten recent entries and a cumulative final Old change summary under [the common changelog rules](../../workflows/maintain-changelogs.md).

Store originals in `evidence/raw/`, transformations in `evidence/derived/`, and dated analysis runs in `markets/<market-id>/runs/`. The default market is `us`; initialize other markets only on instruction. Those directories can be created on first use.

Keep a stable lower-case product slug and explicit market keys, such as `us` and `uk`. Name the member states covered by an `eu` assessment. Handoffs live under `markets/<market-id>/search-briefs/<YYYY-MM-DD>-<sequence>/`; runs use the same date/sequence convention under `runs/`. Shared source records do not merge market conclusions.

Markdown is the default working and report format. Create exports when requested and keep the underlying records. Resume applicable saved work, refresh affected stages after material changes, and do not imply a background watch has been configured.

Use `unknown`, `not supplied`, and `not assessed` explicitly. Do not fill blank tables with plausible examples. Keep stable IDs when an entry changes.
