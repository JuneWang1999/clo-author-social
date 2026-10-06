# Tools Skill -- Gotchas

- `build_manuscript.R` and `build_talk.sh` write only to `drafts/`. If a master exists, never delete or rename it to force a rebuild — that is the user's call.
- Zotero exports: if Better BibTeX "Keep updated" is on, the .bib is rewritten automatically; hand edits to it are lost.
- `validate-bib` checks for common issues but doesn't verify that citation keys match the .bib file.
- Journal selection (`/tools journal`) reads journal-profiles.md -- if the target field isn't profiled, results will be generic.
- Commit skill runs quality checks before committing. Score < 80 blocks the commit.
- The lint subcommand is advisory (exit 0 always). It catches grep-able violations; the coder-critic handles judgment calls.
- `upgrade` deletes and replaces `.claude/` entirely -- it preserves domain-profile.md and settings but nothing else custom in that directory.
- Never stage `.env`, credentials, or `.claude/state/` files in commits.
