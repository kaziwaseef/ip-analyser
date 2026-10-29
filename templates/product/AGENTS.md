# Instructions for {{product_name}}

Read the repository's root `AGENTS.md` and relevant workflows before working on this product. This file adds product-specific facts or instructions only when actually supplied.

- Product ID: {{product_id}}
- Created: {{created_date}}
- Product-specific scope and exceptions: not yet supplied
- Data-sharing permissions: not yet supplied
- Review owner and decision authority: not yet supplied

Ordinary product documents may be stored and versioned in the intended private GitHub repository. Do not impose a separate restricted-storage requirement. Keep credentials outside repository files and follow the actual external-service sharing grants recorded in `tool-register.md`, reusing covered permissions without repeated questions.

Read `overview.md` first. Use `product.md` for facts and `intake.md` for open questions. Record analysis in a new directory under `markets/<market-id>/runs/`. Default to `us` and add other markets only on instruction. Preserve earlier market assessments. Never turn a template default into a verified product fact or an accepted business risk.

Update `overview.md` and its changelog as each meaningful change happens, in the same work step. Keep current facts, market assessments, findings, blockers, next actions, and supporting links consistent with the underlying records.

Follow the root changelog rule and `../../workflows/maintain-changelogs.md` for every changelog. Keep at most ten individual entries, newest first. Fold older entries into the cumulative final `## Old change summary` section without losing the substance already summarized. Preserve the original supporting evidence and assessment records.
