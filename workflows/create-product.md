# Create a product

Create a product directory as soon as the user supplies a usable product name. Do not wait for a complete technical dossier.

First identify the current objective. If the user has not explicitly stated what they want to accomplish, ask before setting the work scope or doing dependent research. Creating the directory and organizing already supplied material can proceed. Record the objective, requested deliverable, relevant workstreams, market and activities, and exclusions in `intake.md`. Use existing explicit instructions rather than asking the same question again.

1. Read the root `AGENTS.md` and `templates/product/README.md`.
2. Derive a lower-case slug containing letters, digits, and hyphens. Check `products/` for a collision. Do not overwrite an existing product. Clarify whether an apparent match is an update or a new product.
3. Copy the contents of `templates/product/` to `products/<slug>/`, including `overview.md` and `AGENTS.md`. Replace `{{product_id}}`, `{{product_name}}`, and `{{created_date}}` with actual values throughout the copied text. Use ISO dates. Leave other unknowns explicitly unknown.
4. Set US as the initial assessment market. Record Amazon and the user's ecommerce website as the usual sales channels and manufacturing partners in China as the usual supply-chain context, with product-specific confirmation still needed. Add a market assessment only on instruction, under `markets/<market-id>/runs/`. Record supplied facts and their sources in `product.md`. Record files in `evidence/index.md`. Link existing material rather than inventing a duplicate source.
5. Give each relevant technical, visual, brand, and content feature a stable ID in `features.md`. Distinguish the product as supplied from planned modifications.
6. Ask for the missing information below in short rounds. Show the current known facts first and ask only for the next useful answers.
7. Save the next actions and blockers in `intake.md`. Begin searches that are meaningful with the information available. Keep blocked conclusions unresolved.
8. Populate `overview.md` with the known state, market scope, evidence links, blockers, and next actions. Add the actual creation entry to its changelog. Follow [Maintain overviews and changelogs](maintain-changelogs.md) from this point onward, updating the overview and changelog as changes happen.
9. For patent-related work, prepare the detailed external-AI prompt and attachment checklist through [Prepare and import an external patent search](external-patent-search.md). Record the handoff state and any missing facts. Do not mark a search executed merely because its prompt is ready.

## Intake rounds

Start with intended use, product identity, commercial scope, and evidence. Go deeper only where the product calls for it.

| Round | Information to request | Why it matters |
| --- | --- | --- |
| Identity | Name, product type, sourcing model, variants, revision, links, supplier, competitors | Defines what is being compared |
| Activity | Countries of manufacture, assembly, import, sale, use, and online targeting; launch dates | Defines territorial and time scope |
| Function | Mechanism, components, materials, dimensions, workflows, technical drawings, software behavior | Supports technical feature and claim mapping |
| Appearance | Photos or renders of all views, CAD where available, packaging, surface decoration, UI states | Supports design and trade dress review |
| Brand and content | Names, logos, slogans, goods and services, target users, channels, artwork, text, fonts, audio | Supports trademark and copyright review |
| Provenance | Who designed each part, supplier documents, licenses, contracts, source code dependencies, prior disclosures | Tests ownership, permission, and copying questions |
| Commercial choices | Planned design changes, risk tolerance, deadlines, review owner, tools and data permissions | Defines the review and decision process |

Support existing supplier products, private-label modifications, and custom designs. Record sourcing and product-specific evidence during intake. China is manufacturing context only; never add it as a sales market. Open a China-specific manufacturing IP assessment only when separately requested, and record it as unassessed when excluded.

Accept a short description first. Keep a text description of an unseen image distinct from having inspected that image. Do not request a complete software bill of materials for a product that has no software.

For EU work, ask for actual member states when the user is ready to scope an assessment. "EU" may remain a discovery scope while the target-state decision is open. Do not turn that discovery scope into a territory-wide clearance conclusion.

## Minimum gate for a scoped analysis

Record at least a product revision or dated snapshot, enough evidence to compare the relevant features, intended activities, target territories, and an as-of date. If a requirement is missing, run only an exploratory screen and mark its affected workstreams incomplete.

No intake answer is an authorization to purchase a subscription, contact a third party, or publish confidential information.
