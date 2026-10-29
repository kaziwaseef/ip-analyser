# Which external tools and data handling rules should be adopted?

ID: 07
Parent: ../map.md
Labels: wayfinder:grilling
Type: grilling
Mode: HITL
Status: resolved
Assignee: codex-root
Blocked by: 02

## Question

Choose the public-source baseline, optional paid tools, manual versus API acquisition, budget, accounts, data export and retention, and which product data may leave the workspace. Public-first and no unapproved confidential uploads are provisional defaults. No external connection is configured by a research note.

## Comments

- 2026-10-19: Created during charting. No decision has been recorded.

- 2026-10-19: Claimed by codex-root for the next sequential discussion after assurance was resolved. The user already requires support for external tools and a copy-ready patent-search-AI handoff; do not re-ask whether that capability is wanted. Discuss tool/access and spending defaults, scoped data-sharing permissions, and retention/storage rules. No provider account, new subscription, API connection, or confidential disclosure has been authorized by this claim.

### Resolution comment, 2026-10-19

The user accepted the recommended tool and sharing policy, with an explicit simpler storage preference.

- Use official public sources and the user's existing tools first. Support copy/paste prompts, permitted exports, and available authorized connectors. New subscriptions, purchases, or custom integrations require the user's instruction; no spending cap or paid account is invented.
- Use permitted public material for scoped research. Confidential disclosures must stay within actual permissions granted for the service, product, and data. Record and reuse standing grants rather than asking again on every covered query. Ask only for disclosures outside the existing grant.
- The user accepts the intended private GitHub repository as ordinary document storage. Product evidence, supplier contracts, and design files may be stored and versioned in normal workspace paths where retention is permitted. Do not impose a separate restricted store, routine untracked document copies, or extra storage approvals.
- Keep credentials and access tokens outside repository files, as in the accepted recommendation. Storage acceptance does not extend permission to disclose confidential material to external services.
- Retain source and export constraints, provenance, prompt/response records, and verification history. Track proposed, available, used, or unavailable tool state accurately. An unnamed dedicated patent-search AI can use the portable handoff; provider-specific details can be added when supplied.

Acceptance evidence: the user replied "Accept recommended" and clarified that storage need not be strict because an intended private GitHub repository is sufficient. This supersedes the earlier recommendation to keep ordinary confidential design/contract files out of Git by default.

Applied to root and product agent instructions, `workflows/external-tools.md`, handoff rules, the tool-register template, and `.gitignore`. Removed generic restricted-document ignore rules while retaining credential/environment ignores. No remote was created, repository visibility changed, third-party upload performed, subscription bought, or integration configured.
