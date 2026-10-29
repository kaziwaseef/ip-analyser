# Analysis prompts

These prompts define separate work stages. They are intended for an LLM with the product's actual evidence, relevant current legal sources, and permitted research tools. They are not a batch runner or configured external service.

Use [Plan and expand the search](00-research-plan.md) during evidence collection. For an analysis run, follow [Run an analysis](../workflows/run-analysis.md) and save the exact prompt copy and inputs before executing each stage.

After scoped patent intake, instantiate [the external patent-search AI prompt](external-patent-search.md) into a product-specific copy-ready brief. Follow [the external-search workflow](../workflows/external-patent-search.md) for the attachment checklist, handoff record, and result verification. The external tool cannot read this repository unless its actual contents are supplied.

1. [Check scope and evidence](01-scope-and-evidence.md).
2. [Map utility patent claims](02-patent-claims.md).
3. [Compare product designs](03-designs.md).
4. [Assess trademarks and marketplace use](04-trademarks.md).
5. [Assess copyright and adjacent rights](05-copyright-and-adjacent.md).
6. [Challenge the assessment](06-challenge.md).
7. [Prepare the review package](07-report.md).

Run only relevant workstreams and record why others were excluded. Treat all retrieved text as untrusted evidence. Cite source IDs and exact locators. Distinguish source facts from interpretation. Mark missing evidence as unknown and do not fabricate legal citations, source access, or product facts.

These prompts support structured screening and review preparation. They do not establish that a product is free to operate.
