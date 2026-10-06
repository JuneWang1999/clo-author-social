# CLAUDE.MD -- Empirical Psychology & Education Research with Claude Code

<!-- HOW TO USE: Replace [BRACKETED PLACEHOLDERS] with your project info.
     Keep this file under ~150 lines — Claude loads it every session.
     See the guide at https://hugosantanna.github.io/clo-author/ for full documentation. -->

**Project:** [YOUR PROJECT NAME]
**Institution:** [YOUR INSTITUTION]
**Field:** [YOUR FIELD — Psychology / Education by default (APA 7). Narrow it in `.claude/references/domain-profile.md`; journal calibration in `.claude/references/journal-profiles.md`.]
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile and confirm output at the end of every task
- **Single source of truth** -- the paper is authoritative; talks and supplements derive from it. Drafts live in `paper/sections/*.md` until handoff; after that `paper/manuscript.docx` (edited by you in Word) is the master and agents never overwrite it — they propose changes
- **Quality gates** -- weighted aggregate score; nothing ships below 80/100; see `quality.md`
- **Worker-critic pairs** -- every creator has a paired critic; critics never edit files
- **Auto-memory** -- corrections and preferences are saved automatically via Claude Code's built-in memory system

---

## Getting Started

1. Fill in the `[BRACKETED PLACEHOLDERS]` in this file
2. Run `/discover interview [topic]` to build your research specification
3. Or run `/new-project [topic]` for the full orchestrated pipeline

---

## Folder Structure

```
[YOUR-PROJECT]/
├── CLAUDE.MD                    # This file
├── .claude/                     # Rules, skills, agents, hooks
├── Bibliography_base.bib        # Centralized bibliography
├── paper/                       # Manuscript (APA 7, Microsoft Word)
│   ├── manuscript.docx          # MASTER after handoff — you edit it in Word
│   ├── manuscript.Rmd           # Draft assembly: title page, abstract, section order
│   ├── build_manuscript.R       # Draft build (+ --handoff, once)
│   ├── displays.csv             # Table/figure numbers, titles, notes
│   ├── sections/                # Draft sections (.md) — before handoff only
│   ├── drafts/                  # Draft builds (overwritten freely)
│   ├── revisions/               # Revised copies to merge via Word's Review › Compare
│   ├── word/                    # APA reference .docx, apa.csl, R helpers
│   ├── figures/                 # Generated figures (.png, 300 dpi)
│   ├── tables/                  # Generated tables (.rds/.csv + .docx previews)
│   ├── talks/                   # PowerPoint talks (.md source → .pptx)
│   ├── supplementary/           # Online supplement
│   └── replication/             # Replication package for deposit
├── data/                        # Project data
│   ├── raw/                     # Original untouched data (often gitignored)
│   └── cleaned/                 # Processed datasets ready for analysis
├── scripts/                     # Analysis code (R, Python, Julia)
├── quality_reports/             # Plans, session logs, reviews, scores
├── explorations/                # Research sandbox (see rules)
├── templates/                   # Session log, quality report templates
└── master_supporting_docs/      # Reference papers and data docs
```

---

## Commands

```bash
# Manuscript draft (before handoff): Markdown sections -> APA Word file
Rscript paper/build_manuscript.R              # -> paper/drafts/manuscript_draft.docx
Rscript paper/build_manuscript.R --handoff    # once: create paper/manuscript.docx (master)

# Read / check the Word master (read-only)
.claude/scripts/docx_snapshot.sh paper/manuscript.docx
python3 .claude/scripts/check_docx_format.py paper/manuscript.docx

# Talks: Markdown slides -> PowerPoint
paper/talks/build_talk.sh <name>              # -> paper/talks/drafts/<name>_draft.pptx
paper/talks/build_talk.sh <name> --handoff    # once: create paper/talks/<name>.pptx
```

> **Note:** Papers are APA 7 manuscripts in Word — see `.claude/rules/working-paper-format.md`.
> Needs R (`rmarkdown`, `knitr`, `flextable`, `officer`) and pandoc; no LaTeX.
> References: export your Zotero collection to `Bibliography_base.bib` (Better BibTeX › Keep updated recommended).
> After handoff, agents send proposed edits as change lists in `quality_reports/revisions/`; apply them in Word with Track Changes on.

---

## Quality Thresholds

| Score | Gate | Applies To |
|-------|------|------------|
| 80 | Commit | Weighted aggregate (blocking) |
| 90 | PR | Weighted aggregate (blocking) |
| 95 | Submission | Aggregate + all components >= 80 |
| -- | Advisory | Talks (reported, non-blocking) |

See `quality.md` for weighted aggregation formula.

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/new-project [topic]` | Full pipeline: idea → paper (orchestrated) |
| `/discover [mode] [topic]` | Discovery: interview, literature, data, ideation |
| `/strategize [mode] [question]` | Identification strategy, pre-analysis plan, or formal theory section (`theory` mode) |
| `/analyze [dataset]` | End-to-end data analysis |
| `/write [section]` | Draft paper sections + humanizer pass (`style-guide` mode extracts voice from prior papers) |
| `/review [file/--flag]` | Quality reviews (routes by target: paper, code, peer) |
| `/revise [report]` | R&R cycle: classify + route referee comments |
| `/talk [mode] [format]` | Create, audit, or build PowerPoint presentations |
| `/submit [mode]` | Journal targeting → package → audit → final gate |
| `/tools [subcommand]` | Utilities: commit, compile, validate-bib, journal, etc. |
| `/checkpoint [--flag]` | Session handoff: memory + SESSION_REPORT + research journal (+ Obsidian if configured) |

---

## Talk Design

Slide design (fonts, colors, layouts) comes from `paper/talks/reference.pptx`. Replace it with your institution's template — keep the layout names — to restyle every talk.

---

## Output Organization

<!-- Options: by-script (default) or by-purpose -->
Output organization: by-script

<!-- by-script:  paper/figures/main_regression/figure1.png, paper/tables/main_regression/table1.rds -->
<!-- by-purpose: paper/figures/estimation/coefplot_main.png, paper/tables/robustness/alt_controls.rds -->

---

## Current Project State

| Component | File | Status | Description |
|-----------|------|--------|-------------|
| Paper | `paper/manuscript.docx` (master) or `paper/sections/` (draft) | [draft/handed off/submitted/R&R] | [Brief description] |
| Data | `scripts/R/` | [complete/in-progress] | [Analysis description] |
| Replication | `paper/replication/` | [not started/ready] | [Deposit status] |
| Job Market Talk | `paper/talks/job_market_talk.pptx` | -- | [Status] |
