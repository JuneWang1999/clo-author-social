---
name: write
description: Draft APA 7 manuscript sections (Introduction, Method, Results, Discussion) using paragraph-level argument moves. Cleanup pass strips AI patterns after drafting. Replaces /draft-paper and /humanizer.
argument-hint: "[section or mode: intro | method | results | discussion | abstract | full | humanize | style-guide] [file path (optional)]"
allowed-tools: Read,Grep,Glob,Write,Edit,Task
---

# Write

Draft paper sections, apply a cleanup pass, or extract a personal style guide from prior papers by dispatching the **Writer** agent.

**Input:** `$ARGUMENTS` — section name or mode, optionally followed by file path.

---

## Modes

### `/write [section]` — Draft Paper Section
Draft a specific section of an APA 7 manuscript: `intro`, `method`, `results`, `discussion`, `abstract`, or `full`. Legacy aliases: `strategy` → `method` (Design and Data Analysis subsections), `conclusion` → `discussion`, `data` → `method` (Participants and Measures subsections).

**Agent:** Writer
**Output (draft phase):** Markdown section file in `paper/sections/`, updated `paper/manuscript.Rmd` params and `paper/displays.csv`, rebuilt `paper/drafts/manuscript_draft.docx`
**Output (Word-master phase, `paper/manuscript.docx` exists):** change list in `quality_reports/revisions/` (or a revised copy in `paper/revisions/`) — never edits the master (INV-25)
**Format:** `.claude/rules/working-paper-format.md` (APA 7 in Microsoft Word)

Workflow:

#### 1. Context Gathering

Before drafting, read all available context:
0. **Phase check:** does `paper/manuscript.docx` exist? If yes, take a fresh snapshot (`.claude/scripts/docx_snapshot.sh`) and work in Word-master mode — the snapshot is your view of the paper; proposals go to a change list
1. Read the existing draft (`paper/sections/*.md`) or the snapshot
2. Read `master_supporting_docs/` for notes, outlines, research specs
3. Read most recent `quality_reports/research_spec_*.md` or `quality_reports/lit_review_*.md`
4. Read `.claude/references/domain-profile.md` for field conventions and `.claude/references/journal-profiles.md` for the target journal (abstract limit, required statements, float placement)
5. Check `Bibliography_base.bib` for available citations
6. Scan `paper/tables/` and `paper/figures/` for generated output
7. Read `quality_reports/results_summary.md` if it exists (from Coder)

#### 2. Paper Type Detection

Before routing, identify the paper type from the strategy memo or existing draft:
- **Reduced-form** — DiD, IV, RDD, event study
- **Structural** — Model estimation, counterfactual simulations
- **Theory + empirics** — Propositions tested with data
- **Descriptive / measurement** — New data, new measure, stylized facts

This determines which section templates the Writer uses.

#### 3. Section Routing

Based on `$ARGUMENTS`:
- **`full`**: Draft all sections in sequence, pausing between major sections for user feedback
- **`intro`**: Draft the introduction (no heading) ending in numbered hypotheses or research questions
- **`method`**: Draft the Method section with JARS subsections (INV-23): Transparency and Openness, Participants, Sample Size Determination, Measures, Procedure, Data Analysis. Design-specific content (randomization, quasi-experimental assumptions, measurement models) goes in Procedure/Design and Data Analysis.
- **`results`**: Draft results — preliminary analyses, confirmatory tests in preregistered order, then labeled exploratory analyses; APA statistics (INV-4)
- **`discussion`**: Draft the Discussion — support per hypothesis, interpretation, limitations, constraints on generality, implications for theory and practice
- **`abstract`**: Draft abstract (must have other sections first); ≤ 250 words or journal limit; plus 3–5 keywords
- **`model`**: Draft a formal model or measurement-model subsection (theory+empirics or psychometric papers)
- **Multi-study papers:** `/write method study2` etc. drafts within `\section{Study 2}`; `/write discussion general` drafts the General Discussion
- **No argument**: Ask user which section to draft

#### 4. Dispatch Writer

Dispatch Writer with paper type and argument-move templates for the target section. The writer drafts using paragraph types (motivation, result statement, mechanism, etc.), applies design-specific moves, then runs the cleanup pass. Draft phase: save to `paper/sections/[section].md` and rebuild the draft. Word-master phase: write a change list instead (never edit `paper/manuscript.docx`).

#### 5. Quality Self-Check

Before presenting the draft:
- [ ] Paper type identified and correct template used
- [ ] Every paragraph has an identifiable purpose (argument move type)
- [ ] Findings lead sentences — not buried after setup
- [ ] Design-specific elements present (see writer.md for checklists per design)
- [ ] APA structure: no Introduction heading; Method / Results / Discussion as Level 1 headings; headings not numbered or styled by hand
- [ ] Method contains every JARS element (INV-23): sample-size justification, exclusions/missing data, reliability in this sample, transparency statement
- [ ] Statistics in APA form (INV-4): exact *p*, effect size + 95% CI, *df*, no leading zero on bounded statistics
- [ ] Bias-free, specific language about participants (INV-24)
- [ ] Every displayed equation is numbered (`\label{eq:...}`)
- [ ] All `@key` / `[@key]` citation keys exist in `Bibliography_base.bib` (exported from Zotero)
- [ ] `displays.csv` lists every table/figure with number, title, and note; numbers follow order of first mention
- [ ] Draft builds: `Rscript paper/build_manuscript.R`, then `python3 .claude/scripts/check_docx_format.py paper/drafts/manuscript_draft.docx` has no FAIL
- [ ] Word-master phase: nothing written to `paper/manuscript.docx`; every change is in the change list with exact current text
- [ ] Introduction contribution paragraph names specific papers
- [ ] Effect sizes stated with units or as standardized effects interpreted against field benchmarks
- [ ] No banned hedging phrases
- [ ] Notation consistent throughout
- [ ] All tables/figures referenced actually exist in `paper/tables/` or `paper/figures/`
- [ ] Results narrated correctly for output type (tables, event study figures, counterfactuals)
- [ ] Personal style guide loaded (not template) — or user prompted to run `/write style-guide`
- [ ] Claim-source map produced for all numerical claims (`quality_reports/claim_source_map_{project}.md`)
- [ ] Results/Conclusion only drafted after verifying actual output files exist

#### 6. Present to User

Present sections through drafting gates, pausing for approval at each:

**GATE 1:** Introduction (literature positioning + hypotheses) → present, wait for approval
**GATE 2:** Method (participants, measures, procedure, design, data analysis) → present, wait for approval
**GATE 3:** Results + Discussion + Abstract → present, wait for approval

For single-section drafts, present the section directly. For `full`, use all three gates.

Flag items that need attention:
- **BLOCKED items:** Results/Conclusion cannot be drafted without output files
- **VERIFY items:** Citations that need user confirmation
- **VOICE items:** Style guide not yet extracted (drafting blocked until resolved)

### `/write style-guide [paper-dir]` — Extract Personal Voice

One-shot extraction of the user's writing voice from their published or drafted papers. Produces `.claude/references/personal-style-guide.md`, which the writer auto-loads on every subsequent invocation.

**When to run:**
- Once at the start of a project, after pointing at a directory of the user's prior papers
- After publishing a new paper that shifts voice (re-run to refresh the profile)

**Input:** `$ARGUMENTS` — path to a directory containing prior papers (.docx or .pdf; .tex also accepted). If omitted, defaults to `master_supporting_docs/` and scans for .docx/.pdf files. Read .docx files with `pandoc <file> -t plain`.

**Agent:** Writer (style-extraction mode)
**Output:** `.claude/references/personal-style-guide.md`

Workflow:
1. **Discover corpus.** List .docx and .pdf files in the target directory. If fewer than 2 papers found, flag and ask before proceeding (style extraction on a single paper overfits).
2. **Sample strategically.** For each paper, extract:
   - The full introduction
   - The first two paragraphs of each major section
   - The abstract and conclusion
   - A random sample of 5–10 results-section paragraphs
   This keeps context usage bounded while capturing voice variation across sections.
3. **Extract patterns.** The Writer (in style-extraction mode) produces quantitative and qualitative patterns:
   - Sentence-length distribution (median, 10th–90th pct)
   - Passive-voice frequency, first-person-plural frequency, em dash rate
   - Paragraph opening and closing moves
   - Section-architecture patterns (how introductions open, how results lead)
   - Lexicon: words used repeatedly, words demonstrably avoided
   - Hedging and comparison patterns
   - Citation conventions (textual vs. parenthetical split; papers-per-claim)
   - Tone markers and anti-patterns already stripped
4. **Write to `.claude/references/personal-style-guide.md`.** Fill every template section with quoted examples from the corpus. Never invent patterns — if a section has no evidence, write "[insufficient corpus evidence]".
5. **Present summary.** One-paragraph recap of the voice profile: sentence length, passive rate, signature lexicon, distinguishing tone markers. User confirms before the guide takes effect on subsequent `/write` calls.

Principles for the extraction:
- **Ground every claim in the corpus.** Each pattern must have at least one quoted example.
- **Extract, don't prescribe.** The guide records the author's observed behavior, not what the Writer thinks is good style.
- **Don't duplicate `domain-profile.md`.** The style guide is about voice; the domain profile is about field conventions.
- **Don't override the APA format or content invariants.** Voice doesn't trump INV-1..24 or `working-paper-format.md`.

### `/write humanize [file]` — Cleanup Pass Only
Strip AI writing patterns from existing text without rewriting content.

**Agent:** Writer (cleanup mode)
**Output:** Edited file with AI patterns removed

Strips 24 patterns across 4 categories:
- Structural: forced narrative arcs, artificial progression
- Lexical: "delve, leverage, nuanced, robust"
- Rhetorical: rule-of-three, negative parallelisms, em dash overuse
- Formatting: excessive bullet points, promotional language

---

## Section Standards

**APA 7 empirical article (JARS-Quant). Word counts are defaults — the journal profile's limits govern.**

| Section | Length | Experiment / RCT | Quasi-experimental | Correlational / longitudinal | Measurement / psychometric |
|---------|--------|------------------|--------------------|------------------------------|---------------------------|
| Introduction (no heading) | 1000-2000 | Theory → gap → hypotheses about manipulation | Policy/practice problem → gap → design preview → RQs | Theory → gap → predicted associations | Construct → why existing measures fall short → validity questions |
| Method | 1000-2000 | Participants, power, conditions, randomization, fidelity, manipulation checks | Sample, assignment mechanism, assumptions, baseline equivalence | Sample, waves, attrition, measures, model | Item development, sample(s), validity evidence plan |
| Results | 1000-2000 | Preliminary → confirmatory (preregistered order) → exploratory | Main estimate → assumption checks → sensitivity | Measurement model → structural/growth model → robustness | Factor structure → reliability → invariance → validity evidence |
| Discussion | 1000-1500 | Support per hypothesis, theory, limitations, generality | Practice/policy implications, generality | Limits of causal inference, future designs | Recommended uses and misuses |
| Abstract | ≤ 250 | Problem, participants, design, effect size + CI, implication | Same | Same | Same |

---

## Markdown and Word Conventions (draft phase)

- Section files: `paper/sections/<name>.md`, Pandoc Markdown; headings `#` (Level 1) to `#####` (Level 5); the introduction has no heading
- Narrative citation `@key` → Smith (2024); parenthetical `[@key]` → (Smith, 2024); several `[@a; @b]`; with page `[@key, p. 12]`; year only `[-@key]`
- Call out tables and figures as plain text "Table 1", "Figure 2" — numbers must match `displays.csv`; refer to sections by name
- Statistics with Markdown italics: `*t*(118) = 2.45, *p* = .016, *d* = 0.45, 95% CI [0.08, 0.81]`
- Math: `$Y_{ij} = \gamma_{00} + u_{0j} + r_{ij}$` becomes a native Word equation
- Footnotes: `text^[Footnote text.]` (use sparingly; APA prefers integrating content into the text)
- Notation protocol: `references/notation-protocol.md`

## Word-Master Conventions (after handoff)

- Read: `.claude/scripts/docx_snapshot.sh paper/manuscript.docx` (fresh each time; shows the user's tracked changes and comments)
- Propose: `quality_reports/revisions/YYYY-MM-DD_<topic>.md` from `templates/change-list.md` — exact current text, proposed text, reason, citations to insert with Zotero
- Large rewrites: edit a copy of the snapshot, then `.claude/scripts/revised_copy.sh <edited.md> <topic>` → `paper/revisions/…docx`; the user merges with Word's Review › Compare
- Never write to `paper/manuscript.docx` (INV-25)

---

## Bundled Resources (Level 3)

Loaded on demand by the writer agent:

| Resource | Path | When |
|----------|------|------|
| Section templates | `templates/section-templates.md` | Always -- defines section structure |
| Paragraph moves | `templates/paragraph-moves.md` | Always -- defines argument types |
| Cleanup patterns | `templates/cleanup-patterns.md` | After drafting -- cleanup pass |
| Style extraction | `templates/style-extraction-protocol.md` | `/write style-guide` mode |
| Drafting gates | `templates/drafting-gates.md` | Full draft mode |
| Claim-source map | `templates/claim-source-map.md` | After results section |
| Notation protocol | `references/notation-protocol.md` | Strategy + results sections |

See also: `gotchas.md` for known failure points and edge cases.

---

## Principles
- **This is the user's paper, not Claude's.** Match their voice and style.
- **Never fabricate results.** Use TBD placeholders.
- **Citations must be verifiable.** Only cite confirmed papers.
- **Argument moves first, cleanup second.** Draft with structure, then strip AI patterns.
