# Maintain overviews and changelogs

This rule applies to every changelog in the repository, including a changelog embedded in an overview. Agents update logs as changes happen, before handing work back to the user.

## Update the relevant records

1. For a product change, update `products/<slug>/overview.md` and its changelog in the same work step. Set Last updated to the actual change date. Keep its current state, market-assessment links, blockers, and next actions consistent with the underlying files.
2. For workspace-wide instruction, template, workflow, or knowledge changes, update the root `CHANGELOG.md`. A change affecting a real product also requires that product's overview update.
3. Record each completed meaningful change. Include the date, what changed, why, affected product revision or market where applicable, and links to supporting records.
4. Group related file edits that implement one change into one entry. A later independent change gets a new entry. Do not wait until a project or analysis is finished to record changes.
5. Do not create a changelog entry solely for updating the changelog or for a read-only check that changes nothing.

Examples of meaningful changes include intake facts, product revisions, new markets, material new evidence, findings, decisions, scope, instructions, assessment status, blockers, and review outcomes. Keep query-by-query detail in the search log and document detail in the evidence register; link them from a concise change entry when their update is material.

## Keep the newest ten changes

1. Put the newest entry first under `## Recent changes`.
2. Keep at most ten individual entries there. Each `###` heading is one entry; grouped details beneath it do not count as separate changes.
3. When an eleventh entry arrives, move the oldest entry's substance into the final `## Old change summary` section and remove that individual entry from Recent changes.
4. Update the existing old-change summary cumulatively. Preserve its earlier substance when folding in another entry. Include the covered date range, important changes and decisions, affected revisions or markets, unresolved issues, and useful links.
5. Keep Old change summary as the final section. With no rolled-up history, write `No changes have been rolled into this summary yet.` Do not fill the summary with invented history.

Use actual change dates and keep their order distinguishable when several changes happen on one date. Do not pad a new log with ten entries or relabel old work as new.

## Preserve supporting records

Changelog compaction summarizes navigation history. It does not remove original evidence, search records, decision records, ticket discussions, frozen run inputs, or completed reports. Keep references needed to understand earlier assessments.

The product overview's current-state sections may change as work advances. Completed run artifacts remain tied to their original inputs. Record a corrected assessment in a new run or dated addendum and link it from the overview.
