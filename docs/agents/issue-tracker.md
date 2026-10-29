# Local Markdown issue tracker

Wayfinder lives in `wayfinder/<effort>/`, as requested by the user. This adapts the upstream local Markdown tracker, whose default directory is `.scratch/`. There is no configured remote tracker.

## Wayfinding operations

- Store the canonical map at `wayfinder/<effort>/map.md` with label `wayfinder:map`.
- Store each child ticket at `wayfinder/<effort>/issues/NN-<slug>.md`. An issue's `ID` is unique within its parent map.
- Give each issue `Parent`, `Labels`, `Type`, `Mode`, `Status`, `Assignee`, and `Blocked by` fields.
- Use `open`, `claimed`, or `resolved` as status. An open issue with `Assignee: unassigned` is unclaimed.
- Create issues first. Add dependencies in a second pass using `Blocked by: NN, NN`. Local Markdown has no native dependency UI, so this is the fallback relationship.
- The frontier contains open, unassigned issues whose dependencies are all resolved. Read ticket metadata to find it, then sort by ID. A missing dependency is a blocker, not a resolved ticket.
- Claim before doing work. Set `Status: claimed` and `Assignee` to the session or agent name. Confirm nobody else has claimed it.
- Keep the original question. Append dated conversation and resolution comments under `## Comments`. Link assets rather than pasting their full contents.
- On resolution, set `Status: resolved`, preserve the assignee, and append a linked gist to the map's Decisions so far.
- On a scope closure, record the reason on the ticket and put the link in the map's Out of scope section, not Decisions so far.
- Refer to tickets by their linked titles in user-facing prose. Bare IDs are metadata, not readable names.

Follow the invoked Wayfinder skill's session and research rules. An unanswered human decision remains open even if a provisional template uses a recommended default.

## Setup provenance

The user supplied the Wayfinder skill. Its required companion skills and the local tracker reference were read from [mattpocock/skills](https://github.com/mattpocock/skills) on 2026-10-19. They are not installed by this workspace.

For a full installation of that skill suite and its tracker configuration, run `/setup-matt-pocock-skills`. This local tracker lets the requested repository work continue without changing global skill installations.
