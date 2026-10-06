# Plan: Replace LaTeX with a Word (.docx) / PowerPoint Workflow

**Status:** COMPLETED (2026-10-06) — not yet committed
**Supersedes:** the LaTeX parts of `2026-10-06_apa7-psych-education-adaptation.md` (APA 7 and psych/ed calibration stay)

## User decisions
1. **Word file is the master copy.** Claude drafts once in Markdown, builds `paper/manuscript.docx`; after that the user edits in Word and agents never overwrite it. They propose changes as a change list or as a revised copy the user compares in Word (Review > Compare).
2. **Zotero for references.** Zotero exports `Bibliography_base.bib` (Better BibTeX auto-export recommended); pandoc + `apa.csl` (copied from the user's Zotero styles folder) formats APA citations and references in the first build.
3. **Replace LaTeX/Beamer** with Word/PowerPoint. Remove LaTeX format rules, templates, and build files.

## Architecture

```
paper/
├── sections/*.md            # Draft phase only: Pandoc Markdown, [@key] citations
├── tables/*.rds (+ .docx)   # flextable objects from R (bare: no number/title/note)
├── figures/*.png            # 300 dpi PNG, no titles inside
├── manuscript.Rmd           # Assembles title page + sections + tables/figures
├── build_manuscript.R       # Renders → manuscript.docx; never overwrites an existing master
├── manuscript.docx          # MASTER after first build (user edits in Word)
├── word/                    # apa7-reference.docx, apa.csl, apa_helpers.R
└── talks/<name>.md → <name>.pptx (pandoc, reference.pptx)
.claude/scripts/
├── make_reference_docx.py   # Regenerates APA styles in the reference .docx
├── docx_snapshot.sh         # Master .docx → Markdown snapshot for critics (incl. tracked changes, comments)
├── check_docx_format.py     # APA format checks on the .docx (margins, font, spacing, headings, styles)
└── pptx_text.py             # Slide text extraction for the storyteller-critic
```

Agents read the master via `docx_snapshot.sh` and write proposals to `quality_reports/revisions/`.

## Files
- **Build infrastructure (new, tested end to end):** everything above.
- **Rules:** working-paper-format.md (APA 7 in Word), content-invariants.md (INV-1/2/3/9/10/12/13 re-specified for Word; numbers kept), content-standards.md (flextable tables, PNG figures), permissions.md, agents.md, workflow.md, meta-governance.md.
- **Agents:** writer, writer-critic, coder, data-engineer, verifier, storyteller, storyteller-critic, theorist (Markdown + math outputs).
- **Skills:** write, review, analyze (+ table/figure standards, gotchas, R template, results summary), talk (Beamer/Quarto → PowerPoint), revise (response letter .md → .docx), submit (cover letter, audit, checklist), tools (compile → build), strategize (theory outputs), new-project quality gates.
- **Remove:** `paper/latexmkrc`, `paper/talks/latexmkrc`, `paper/preambles/`, `paper/quarto/`, `templates/latex/`, `talk/templates/beamer-scaffold.tex`, `talk/templates/quarto-scaffold.qmd`, `revise/templates/response-letter.tex`, `submit/templates/cover-letter.tex`.
- **CLAUDE.md, .gitignore, WORKFLOW_QUICK_REF.md.**
- **Out of scope:** `guide/` documentation site (Quarto, describes the upstream template).

## Verification
- Build a sample manuscript from the template with a table, a figure, and citations; open-check with `check_docx_format.py` and `docx_snapshot.sh`.
- Build a sample talk .pptx and extract it with `pptx_text.py`.
- Confirm the build refuses to overwrite an existing `manuscript.docx`.
- Grep for leftover LaTeX requirements.
