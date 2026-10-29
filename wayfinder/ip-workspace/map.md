# Build a product IP research and analysis workspace

ID: ip-workspace
Labels: wayfinder:map
Status: open

## Destination

Establish a document-first work repository for product-specific, evidence-backed IP research and repeatable LLM analysis, primarily for the United States and also for the United Kingdom and specified EU member states. The workspace must guide intake, document discovery, infringement-risk screening, and a scoped FTO review package.

## Notes

- The user requested a work repository, external research tools, one directory per product, comprehensive legal foundations, analysis prompts, risk reporting, and separate Wayfinder tickets.
- Execution override: build the requested reversible Markdown foundation during charting. Do not treat its provisional defaults as resolved human decisions. No product clearance or legal certification is authorized by this foundation.
- Consult the wayfinder, grilling, domain-modeling, research, technical-writing, and unslop skills. The local wayfinder skill is `/Users/kaziwaseef/.agents/skills/wayfinder/SKILL.md`. Companion skill sources were retrieved from the upstream mattpocock/skills repository because they are not installed locally.
- Use the local Markdown tracker described in `../../docs/agents/issue-tracker.md`. The user requested `wayfinder/` instead of `.scratch/`.
- Research tickets may resolve in parallel. Charting does not resolve human decision tickets. Claim tickets before work; preserve questions and append resolution comments.
- Follow the resolved product-scope, evidence, pipeline, assurance, and tool/data tickets for standing decisions. The operating model is also resolved; define pilot validation next. Do not reopen accepted choices without a new reason or user instruction.
- "Patterns" is provisionally interpreted as patents and product design rights. Software design patterns alone are not treated as registered IP rights.

## Decisions so far

- [Which primary legal sources and jurisdiction distinctions must govern the workspace?](issues/01-legal-foundations.md): Dated primary-source foundations establish separate legal and territorial analysis requirements.
- [Which public and optional commercial systems can support reliable IP discovery and verification?](issues/02-research-systems.md): A sourced system survey separates discovery, official verification, access requirements, and optional tools.

- [Which products and commercial activities must the first workflow support?](issues/03-product-scope.md): Physical-product scope and separate market assessments agreed, with manufacturing review boundaries recorded.

- [What evidence and provenance are necessary for a reproducible product assessment?](issues/04-evidence-model.md): Evidence handling, frozen inputs, product overviews, and a common changelog retention rule agreed.

- [Which challenge methods and risk dimensions should inform the assessment?](issues/10-challenge-risk-methods.md): Sourced challenge methods and risk-model alternatives researched for the subsequent pipeline decision.

- [What separate analysis stages and review gates make the LLM pipeline defensible?](issues/05-analysis-pipeline.md): Scoped stages, external-search handoffs, multiple challenge methods, and the concern rubric agreed.

- [What may the FTO result state, and who may approve its use?](issues/06-fto-assurance.md): Internal report purpose, user decision authority, and explicit escalation rules agreed.

- [Which external tools and data handling rules should be adopted?](issues/07-tool-data-policy.md): Tool/spending defaults, reusable sharing grants, and simplified private-repository storage agreed.

- [Does the repository structure and agent contract support the intended work?](issues/08-operating-model.md): Product/market layout, Markdown defaults, and saved-stage resumption/refresh agreed.

## Not yet specified

- Specialist analysis branches will depend on the first actual products, their technology, assets, supply chains, and countries of activity.
- A meaningful search stopping rule and representative pilot evidence depend on the chosen product and available sources.
- Connector implementation details depend on access, export rights, provider terms, volume, and confidentiality requirements.

## Out of scope

- Issuing an automated legal FTO certificate or promising that all relevant rights have been found.
- Performing an actual product analysis before a product and scope are supplied.
- Building an application, autonomous scraper, or production integration as part of this foundation.
- Purchasing subscriptions, contacting rights holders, filing applications, or sending confidential material to external services without task-specific authorization.
