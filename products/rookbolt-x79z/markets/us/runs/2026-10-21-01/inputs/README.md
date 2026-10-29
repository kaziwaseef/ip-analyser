# IP analysis workspace

This is a work repository for researching physical products, collecting IP evidence, and running repeatable analysis through an LLM and external research tools. Each product defaults to a US assessment. Additional markets are added on instruction, with a separate assessment history for each market.

Start a product by saying, for example:

> Create a product called Acme folding stand. I have these photographs and a supplier listing. Start with US sales and help me complete the intake.

The agent follows [Create a product](workflows/create-product.md), creates a directory, and asks for the missing information in manageable rounds. A product can start with incomplete information. An assessment cannot silently treat missing information as favorable evidence.

If your intended task is unclear, the agent asks what you want to accomplish before setting the work scope. For patent research, intake also produces a detailed, copy-ready prompt for your dedicated patent-search AI. You can bring results from that AI or other external tools back here for evidence import, verification, and analysis. See [the external search workflow](workflows/external-patent-search.md).

## What lives here

| Path | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Instructions for agents working in this repository |
| [GLOSSARY.md](GLOSSARY.md) | Terms that distinguish products, documents, rights, findings, and decisions |
| [CHANGELOG.md](CHANGELOG.md) | Recent workspace changes and cumulative older-change summary |
| [knowledge/](knowledge/README.md) | Dated legal foundations and research-system references |
| [workflows/](workflows/README.md) | Intake, research, analysis, and maintenance procedures |
| [prompts/](prompts/README.md) | Prompts for the separate analysis stages |
| [templates/product/](templates/product/README.md) | Files to copy when creating a product |
| [templates/run/](templates/run/README.md) | Files to copy for each analysis run |
| [products/](products/README.md) | A separate directory and evidence history for each product |
| [wayfinder/](wayfinder/README.md) | Decision maps and tickets, separate from product work |

No application, dependency installation, or coding pipeline is required. An analysis pipeline here is a sequence of documented LLM tasks with saved inputs, outputs, and review gates. APIs and other automation can be added after their access and data rules are chosen.

## How a product moves through the workspace

1. Describe the product, its variants, relevant commercial activities, countries, and dates.
2. Break the product into evidenced technical, visual, brand, and content features.
3. Search broadly and preserve search queries, exclusions, and coverage gaps.
4. Obtain the relevant documents and verify territorial status against appropriate official records.
5. Run the patent, design, trademark, copyright, or specialist analyses included in the agreed work scope.
6. Challenge the findings, record remaining risks, and prepare a scoped review package.
7. Refresh the assessment when the product, rights, law, or intended activities change.

The output is a dated risk assessment tied to a product version, countries, activities, and evidence. It includes claim charts where relevant, source locators, unresolved questions, and actions. Any legal FTO opinion and business release decision are recorded separately. An LLM run does not issue a legal clearance seal.

Each product has an `overview.md` with its current state, separate market assessments, blockers, and changelog. Agents update it as changes happen. All changelogs keep the newest ten individual changes and fold older changes into a cumulative final Old change summary, following [the common changelog rules](workflows/maintain-changelogs.md).

## Current planning state

The [Build a product IP research and analysis workspace map](wayfinder/ip-workspace/map.md) tracks decisions that remain open. Product scope, evidence handling, overviews/changelogs, scoped pipelines, external-search handoffs, concern scoring, assurance, and tool/data policy are agreed. The user accepts ordinary document storage in the intended private GitHub repository; credentials remain outside repository files. The operating model is also agreed. Pilot selection and acceptance criteria are the final open decision.

Research references identify useful sources and systems. They do not mean an account, API connection, subscription, or automated monitoring job is configured.

The [foundation validation record](docs/foundation-validation.md) describes the checks performed on this initial structure and what remains untested.
