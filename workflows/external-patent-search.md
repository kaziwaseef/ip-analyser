# Prepare and import an external patent search

Use this workflow after product intake when the agreed objective includes patent research. The user may search with their dedicated patent-search AI, another external tool, or both. This workflow creates a portable prompt and records the returned evidence; it does not send a message, connect an account, or execute the external search.

## Establish the task

1. Read the product overview, current instructions, supplied facts, and intake. If the current objective is not explicit, ask the user what they want to accomplish before drafting a search scope or doing dependent research.
2. Record the objective, product revision, requested market, relevant activities, rights in scope, exclusions, expected output, and known gaps. Distinguish FTO candidate discovery, patentability/prior-art research, a patent landscape, design-patent discovery, and focused follow-up searches.
3. Use US as the default market unless the user requests another. China is manufacturing context; Chinese manufacturing-rights review is separately requested. Do not silently expand the search to every right type or country.
4. Prepare a feature brief with stable feature IDs, mechanism, components, use cases, visual features where relevant, synonyms, known competitors, and source references. Preserve unknowns and distinguish observed product facts from proposed changes.

## Produce the handoff

1. Create `products/<slug>/markets/<market-id>/search-briefs/<YYYY-MM-DD>-<sequence>/` with a unique sequence.
2. Instantiate [the external patent-search prompt](../prompts/external-patent-search.md) into `prompt.md`. Replace template fields with the actual scoped brief. The generated prompt must be self-contained; the external AI cannot read repository paths or unstated conversation history.
3. Copy [the handoff manifest](../templates/search-handoff/manifest.md) into `manifest.md` and complete it with the exact prompt version, sources, attachments, product revision, scope, disclosure limits, and intended tool if known.
4. Produce the shareable prompt using permitted public material or information covered by an actual service/product/data sharing grant. Reuse existing grants for covered disclosures. Identify attachment names and what each contains. Record material withheld or redacted and resulting search limitations. Ordinary local storage in the intended private repository does not by itself grant external-sharing permission.
5. Include search strategies, family and territory follow-up, source verification requirements, a structured result format, exclusions and uncertainty reporting, and follow-up queries. Do not fill in search results before they exist.
6. Give the user the actual copy-ready prompt or its local file link and an attachment checklist. Mark the handoff `prepared` or `awaiting-external-results`. Update the product overview and changelog in the same work step.

If material intake is missing, create a clearly limited exploratory brief or ask the specific questions needed for a useful search. Do not invent technical features to make the prompt appear complete. Do not require a provider-specific format until that provider and its requirements are actually known.

## Import returned work

1. Preserve the exact returned report and any permitted attachments as raw evidence, recording their source, tool or model if exposed, date, handoff ID, and associated queries. Keep it distinguishable from the underlying patent documents.
2. Record which searches were reportedly executed and which have direct execution evidence. Do not upgrade an unsupported claimed query into a verified database search.
3. Normalize identifiers, kind codes, application/publication/grant relationships, families, jurisdictions, and source URLs into `rights.md` and `search-log.md`. Keep material territorial rights and claim versions separate.
4. Open and verify material patent documents, operative claims or design representations, and official status records. Flag fabricated identifiers, mismatched claims, unsupported status, missing sources, and unavailable images. An external AI summary is a discovery lead, not authoritative rights evidence.
5. Keep the returned candidate ranking and the repository's verified findings distinguishable. Preserve adverse candidates and uncertain exclusions.
6. Record gaps and further searches. Feed the verified evidence into the appropriate market run. Update the handoff manifest, product overview, and changelog as changes happen.

Repeat the cycle with a new brief version when feature knowledge, scope, or search leads change. Preserve earlier prompts and responses so another reviewer can see how the search developed.
