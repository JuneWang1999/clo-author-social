# Manuscript Format Standard (APA 7, Microsoft Word)

All papers generated or reviewed by this system are **APA 7 professional manuscripts in Microsoft Word (.docx)** for journal submission in psychology and education (*Publication Manual of the American Psychological Association*, 7th ed., 2020). No LaTeX. This rule applies to the writer, writer-critic, coder, storyteller, and verifier agents.

The filename is kept as `working-paper-format.md` because other files point here.

---

## The Master-Copy Rule

The manuscript has two phases. Every agent must know which phase the project is in.

| Phase | How to tell | Source of truth | Agents may |
|-------|-------------|-----------------|-----------|
| **Draft** | `paper/manuscript.docx` does **not** exist | `paper/sections/*.md`, `paper/displays.csv`, `paper/manuscript.Rmd` | Edit the Markdown drafts; rebuild `paper/drafts/manuscript_draft.docx` |
| **Word master** | `paper/manuscript.docx` exists | `paper/manuscript.docx` — the user edits it in Word | Read it; propose changes. **Never write to, overwrite, rename, or regenerate it.** |

- **Handoff** happens once, when the user approves the draft: `Rscript paper/build_manuscript.R --handoff`. The script refuses to run if the master already exists.
- After handoff, `paper/sections/*.md` are historical. Do not edit them to change the paper and do not rebuild over the master.
- The same rule applies to talks (`paper/talks/<name>.pptx`) and to any other `.docx`/`.pptx` the user has edited.

### Reading the master

```bash
.claude/scripts/docx_snapshot.sh paper/manuscript.docx        # -> quality_reports/snapshots/manuscript_<date>.md
python3 .claude/scripts/check_docx_format.py paper/manuscript.docx --abstract-limit 250
```

The snapshot includes the user's tracked changes and comments. Always read a fresh snapshot — the user may have edited the file since the last one.

### Proposing changes to the master

1. **Change list (default).** Write `quality_reports/revisions/YYYY-MM-DD_<topic>.md` using `templates/change-list.md`: for each change, the location (section heading + paragraph's first words), the current text quoted exactly, the proposed text, and the reason. The user applies the changes in Word.
2. **Revised copy (large rewrites).** When the change list would exceed about 10 paragraphs, write a revised copy to `paper/revisions/manuscript_YYYY-MM-DD_<topic>.docx` (convert the snapshot, apply the changes, rebuild with the reference template) and tell the user to compare it with the master in Word: **Review › Compare › Compare Documents**, original = `manuscript.docx`, revised = the copy. Word shows every difference as a tracked change the user can accept or reject. Warn the user that paragraphs touched in the copy lose live Zotero citation fields, which they re-insert with the Zotero plugin.
3. **Tracked changes directly.** If the Claude environment provides a Word/docx skill that can add tracked changes, it may write them into a **copy** of the master (never the master itself).

---

## Build Infrastructure

| File | Purpose |
|------|---------|
| `paper/manuscript.Rmd` | Title page, abstract, keywords, section order, references, tables/figures. Metadata lives in its `params:` |
| `paper/build_manuscript.R` | Renders the draft (`paper/drafts/manuscript_draft.docx`); `--handoff` creates the master once |
| `paper/sections/*.md` | Draft text in Pandoc Markdown |
| `paper/displays.csv` | Table and figure manifest: `type, number, file, title, note` |
| `paper/word/apa7-reference.docx` | Word styles: Times New Roman 12, double spacing, 1-in margins, APA headings, running head + page number. Regenerate with `python3 .claude/scripts/make_reference_docx.py` |
| `paper/word/apa.csl` | APA 7 citation style (from Zotero's style repository, CC BY-SA 3.0) |
| `paper/word/apa_helpers.R` | `apa_flextable()`, `apa_spanner()`, `apa_save_table()`, `apa_num()`, `apa_p()`, `apa_ci()` |
| `Bibliography_base.bib` | Exported from Zotero (see Citations) |

Requirements: R with `rmarkdown`, `knitr`, `flextable`, `officer`; pandoc (bundled with RStudio or installed separately). No TeX.

---

## Page Layout (handled by the reference template)

- US Letter, 1-in margins on all sides
- Times New Roman 12 pt (APA 7 also accepts Calibri 11, Arial 11, Georgia 11, Lucida Sans Unicode 10 — change `FONT`/`SIZE` in `make_reference_docx.py`)
- Double spacing everywhere, including the title page, abstract, references, and table/figure notes; no extra space before or after paragraphs
- First-line indent 0.5 in for body paragraphs; left-aligned, ragged right (no justification)
- Header: running head (all caps, ≤ 50 characters) flush left, page number flush right, on every page including the title page
- **Use the styles, not direct formatting.** Body text uses *Body Text*; headings use *Heading 1–5*; references use *Bibliography*. Never fake a heading with bold body text — the critic and the format checker look for heading styles.

---

## Title Page (set in `paper/manuscript.Rmd` `params:`)

| Param | Content |
|-------|---------|
| `title` | Title case, bold, centered (the style does this); focused, about 12 words or fewer, no abbreviations |
| `shorttitle` | Running head, ≤ 50 characters; the build converts it to all caps |
| `authors` | Names with superscript affiliation numbers: `"Ana Ruiz^1^ and Lee Park^2^"` — no degrees or titles |
| `affiliations` | One entry per affiliation: `"^1^Department of Psychology, University One"` |
| `author_note` | Paragraphs in APA order: ORCID iDs; changes of affiliation; disclosures and acknowledgments (preregistration with link and deviations, data/materials/code availability, conflicts of interest, funding); correspondence |
| `masked` | `true` for masked review — drops authors, affiliations, and author note |

For masked review, the text must not identify the authors either ("in our previous study (Ruiz, 2023)" → "in a previous study (Ruiz, 2023)").

## Abstract and Keywords

- Own page after the title page; label "Abstract" centered bold; one paragraph, no indent
- 250 words or fewer by default (APA 7) or the journal limit if stricter (INV-5)
- Problem; participants and key characteristics; design and method; main findings with effect sizes and 95% CIs; conclusions and implications
- `Keywords:` (italic label, indented) followed by 3–5 lowercase keywords (INV-6). No JEL codes
- Public significance / impact statements required by some journals go into the submission system; draft them in `quality_reports/submission/`

## Section Structure

APA quantitative empirical article (JARS-Quant; Appelbaum et al., 2018):

1. **Title** repeated at the top of the first text page (bold, centered) — the build does this
2. **Introduction** — *no heading*. Problem, literature, gap, hypotheses / research questions
3. **Method** (Level 1) — Transparency and Openness, Participants, Sample Size Determination, Measures, Procedure, Data Analysis (Level 2)
4. **Results** (Level 1) — preliminary analyses, confirmatory tests in preregistered order, labeled exploratory analyses
5. **Discussion** (Level 1) — support for hypotheses, interpretation, limitations, constraints on generality, implications
6. **References** (new page)
7. **Tables**, then **Figures** — each on its own page after the references (APA-permitted placement and the default here; the user may move them into the text in Word if the journal prefers)
8. **Appendices**

**Multi-study papers:** Introduction → `# Study 1` with `## Method`, `## Results`, `## Discussion` → … → `# General Discussion`.

**Heading levels in Markdown drafts** (the reference template formats them):

| Markdown | APA level | Appearance |
|----------|-----------|------------|
| `# Heading` | Level 1 | Centered, bold, title case |
| `## Heading` | Level 2 | Flush left, bold, title case |
| `### Heading` | Level 3 | Flush left, bold italic, title case |
| `#### Heading.` | Level 4 | Indented, bold, title case, ends with a period |
| `##### Heading.` | Level 5 | Indented, bold italic, title case, ends with a period |

APA Levels 4–5 run into the paragraph; the Word styles approximate them as separate indented paragraphs — acceptable for submission, or the user can run them in by hand. Headings are not numbered. Do not skip levels.

## Tables and Figures

APA 7 (§7.1–7.36): **bold number** and *italic title* above; the table or image; *Note.* below. The build creates this from `paper/displays.csv`:

```csv
type,number,file,title,note
table,1,tables/sumstats_correlations.rds,"Means, Standard Deviations, and Correlations Among Study Variables","*N* = 412 students in 24 classrooms. Coefficient omega reliabilities appear on the diagonal."
figure,1,figures/fig1_condition_by_prior.png,Posttest Science Achievement by Condition and Prior Achievement,Error bars represent 95% confidence intervals.
```

- Tables are flextable objects saved by the analysis scripts (`apa_save_table()`): `.rds` for the build, `.docx` preview. They contain no number, title, or note (INV-13).
- Figures are PNG at 300 dpi or more (TIFF if the journal requires); no title inside the image (INV-12).
- Number tables and figures separately, in order of first mention; call out every one in the text ("Table 1", "Figure 2") before it appears (INV-10).
- Table rules: horizontal only — above and below the column heads, below the body; spanner rules under spanned columns. No vertical rules, shading, or cell borders (INV-3).
- Notes: general note (*Note.*), then specific notes (superscript lowercase letters), then probability note (asterisks, only if used).

## Citations and References (Zotero)

**Draft phase:**
- References live in Zotero. Export the project collection to `Bibliography_base.bib` (project root). Recommended: install the **Better BibTeX** plugin and use *Export Collection › Better BibTeX › Keep updated*, which rewrites the file whenever the library changes and gives stable citation keys. Without Better BibTeX, re-export by hand after adding references.
- In drafts, cite with Pandoc keys: narrative `@key` → Ruiz (2024); parenthetical `[@key]` → (Ruiz, 2024); multiple `[@a; @b]`; page `[@key, p. 12]`; suppress author `[-@key]`. Every key must exist in `Bibliography_base.bib`.
- pandoc + `apa.csl` formats in-text citations and the reference list (APA 7 et al. rules, DOIs as URLs, sentence-case titles). Never type a reference list by hand.

**Word-master phase:**
- In the master, citations and references are formatted text, not live Zotero fields. The user adds new citations with the **Zotero Word plugin** (Zotero tab › Add/Edit Citation) and either keeps the generated list or rebuilds the bibliography with the plugin.
- Agents propose new citations in change lists as `(Author, Year)` plus the citation key and full reference, and check that every in-text citation appears in the References section and vice versa.
- Optional: convert the first build to live Zotero fields with Better BibTeX's pandoc filter (`zotero.lua`, see the Better BibTeX documentation) so all citations stay editable through the Zotero plugin.

## Equations

Write math in drafts as `$...$` / `$$...$$` (LaTeX math syntax). pandoc converts it to native Word equations, which the user edits with Word's equation editor. Number display equations at the right margin in parentheses when they are referred to.

## Building

```bash
Rscript paper/build_manuscript.R            # draft -> paper/drafts/manuscript_draft.docx
Rscript paper/build_manuscript.R --handoff  # once: create paper/manuscript.docx (master)
```

## What the Writer-Critic Checks

Run `python3 .claude/scripts/check_docx_format.py <file.docx>` first; it checks page setup, font, spacing, running head, headings, abstract length, keywords, hanging indents, table/figure numbering and callouts, vertical rules, and common statistics errors. Then read the snapshot.

**Required (blocking deductions):**
- Margins, font/size, or double spacing not APA (-5)
- Missing running head or page number (-2); running head > 50 characters or not all caps (-1)
- Headings typed as bold body text instead of heading styles, skipped levels, or numbered headings (-2)
- Introduction carries a heading, or Method/Results/Discussion missing (-3)
- Title page missing elements (title, authors, affiliations, author note) for a non-masked submission (-3); identifying information in a masked submission (-5)
- Missing keywords, or JEL codes present (INV-6) (-5)
- Abstract over 250 words or the journal limit (INV-5) (-3)
- Reference list typed by hand, or citations missing from / extra in the reference list (INV-9) (-3, plus -1 per mismatch, max -5)
- Vertical rules or full grid borders in tables (INV-3) (-3)
- Missing table notes or figure notes (INV-1, INV-2) (-5 per, max -15)
- Number/title placed below a table or figure, or title inside a figure image (-2 per, max -6)
- Table or figure not called out in the text, or numbered out of order (INV-10) (-2 per, max -6)
- Statistics not reported per APA (INV-4) (-2 per, max -10)
- Method missing JARS elements (INV-23) (-5 per element, max -15)
- Biased or imprecise language about people (INV-24) (-2 per, max -6)
- Draft-phase only: build fails (-20)

**Recommended (advisory):**
- Tables/figures placed as the journal prefers (after references vs. in text)
- DOIs present for every reference that has one
- Live Zotero fields in the master (eases later citation edits)
