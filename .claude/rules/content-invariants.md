# Content Invariants

These are non-negotiable. Every agent checks against them. Violations are deductions, not suggestions. Critics cite invariant numbers (e.g., "violates INV-3") in their reports.

---

## Paper

**INV-1.** Every table follows APA 7: bold number and italic title above, and a note below beginning with *Note.* that explains abbreviations, the sample (*N*, and clusters if nested), the data source, and what is in parentheses or brackets. In drafts these come from `paper/displays.csv`; in the Word master they are paragraphs in the *Table Number*, *Table Title*, and *Table Note* styles.

**INV-2.** Every figure has a bold number and italic title above the image and a note below explaining what is shown, how to read it (e.g., what error bars represent), and the data source. In drafts these come from `paper/displays.csv`; in the Word master they use the *Figure Number*, *Figure Title*, and *Figure Note* styles.

**INV-3.** Tables use horizontal rules only — above and below the column heads, below the body, and under spanner heads. No vertical rules, full grid borders, or shading (`apa_flextable()` enforces this).

**INV-4.** Statistics are reported in APA style. Exact *p* values to two or three decimals (*p* = .031; *p* < .001 below that), never "*p* = .000" or "n.s." alone. Every primary result reports an effect size (e.g., *d*, *g*, $\eta^2_p$, $\omega^2$, *r*, standardized $\beta$, odds ratio) with a 95% confidence (or credible) interval in brackets: 95% CI [0.12, 0.45]. Test statistics are italicized with degrees of freedom: *t*(48) = 2.31, *F*(2, 117) = 4.56, $\chi^2$(3, *N* = 412) = 9.80. No leading zero for statistics that cannot exceed 1 (*p*, *r*, $\alpha$, $\omega$, $R^2$, proportions). Significance asterisks appear only if the journal profile allows them, and then only with a probability note defining every threshold.

**INV-5.** Abstract is 250 words or fewer (APA 7 default), or the target journal's limit if stricter.

**INV-6.** 3–5 keywords present on a `Keywords:` line after the abstract (lowercase except proper nouns). No JEL codes. When the target journal requires a public significance or impact statement, it exists (see the journal profile).

**INV-7.** Notation is consistent across all sections — the same symbol means the same thing everywhere. Different concepts get different symbols.

**INV-8.** Every causal claim has a corresponding design justification (randomization, or a named quasi-experimental design with its assumptions defended). No causal language ("effect of," "leads to," "improves," "reduces") for correlational, cross-sectional, or longitudinal-observational findings — use "is associated with," "predicts," or "covaries with." Mediation estimated from non-experimental or single-time-point data is not described as a causal mechanism.

**INV-9.** References come from Zotero via `Bibliography_base.bib` and are formatted by pandoc with `paper/word/apa.csl` (draft phase) or the Zotero Word plugin (Word-master phase). No hand-typed reference lists. Every in-text citation appears in the References section and every reference is cited.

**INV-10.** Tables and figures are numbered separately in order of first mention, and each is called out in the text ("Table 1", "Figure 2") before it appears.

**INV-11.** Numbers in text match the tables and figures exactly. No rounding discrepancies, no stale values.

**INV-12.** No titles inside ggplot/matplotlib figures. The number and title go above the image in the manuscript. Panel labels ("Panel A: ...") inside multi-panel figures are fine.

**INV-13.** R/Python/Julia scripts export tables as styled flextable objects (`apa_save_table()` → `paper/tables/<name>.rds` + `.docx` preview) with no number, title, or note, and figures as PNG (≥ 300 dpi) with no title. The manuscript adds numbers, titles, and notes.

## Code

**INV-14.** `set.seed()` (or language equivalent) called exactly once, at the top of the main script, if any stochastic element exists.

**INV-15.** All packages/libraries loaded at the top of the script, before any data loading or computation.

**INV-16.** No absolute paths. All paths relative to project root via `here()` (R), `pathlib.Path` (Python), or `joinpath(@__DIR__, ...)` (Julia).

**INV-17.** No growing vectors/lists in loops. Pre-allocate result containers or use vectorized operations.

**INV-18.** Output files go to the path specified by the Output Organization setting in `CLAUDE.md`.

**INV-19.** No prohibited functions: `setwd()` / `os.chdir()` / `cd()`, `rm(list = ls())`, `install.packages()` in scripts, `attach()` / `detach()`.

## Talk

**INV-20.** Notation in talk matches paper exactly — same symbols, same subscripts, same definitions.

**INV-21.** Every claim on a slide is traceable to the paper. No orphan results or numbers that don't appear in the manuscript.

## Traceability

**INV-22.** Every numerical claim in the manuscript must have an entry in the claim-source map (`quality_reports/claim_source_map_{project}.md`) traceable to a specific script line and output file.

## Reporting Standards (APA 7)

**INV-23.** The Method section meets the APA Journal Article Reporting Standards (JARS-Quant; Appelbaum et al., 2018; JARS-Qual or JARS-Mixed when applicable). Required elements: (a) participant characteristics and recruitment/sampling procedures; (b) sample-size determination (a priori power analysis or other justification, with the assumed effect size and its source); (c) exclusions, attrition, and missing data with the handling method; (d) every measure with its source, scoring, and reliability estimate in this sample (prefer $\omega$ to $\alpha$ when assumptions differ); (e) design and procedure, including assignment method and level of randomization; (f) the analysis plan, distinguishing confirmatory from exploratory analyses; (g) a transparency statement — preregistration (with registry link and any deviations), and availability of data, materials, and code; (h) ethics approval (IRB) and consent/assent procedures.

**INV-24.** Language about people is bias-free and specific (APA 7 Chapter 5): "participants" or the specific role (students, teachers), not "subjects"; person-first or identity-first wording as preferred by the community described; specific racial/ethnic labels, capitalized (Black, White, Latinx/Hispanic as reported by participants); singular "they" for unspecified gender; age groups described specifically ("adults aged 65–80 years") rather than "the elderly"; report how demographic categories were collected.

**INV-25.** The Word master is never overwritten. Once `paper/manuscript.docx` exists (or a talk's `.pptx`), agents read it through a snapshot and propose changes as a change list or a separate revised copy (see `working-paper-format.md`, The Master-Copy Rule).

---

## How Agents Use This File

| Agent | Checks | Action on Violation |
|-------|--------|-------------------|
| **writer-critic** | INV-1 through INV-13, INV-22 through INV-25 | Deduct per scoring rubric |
| **coder-critic** | INV-13 through INV-19 | Deduct per scoring rubric |
| **storyteller-critic** | INV-20, INV-21, INV-25 | Deduct per scoring rubric |
| **verifier** | INV-9, INV-10, INV-14, INV-15, INV-16, INV-19, INV-25 | FAIL if present |
| **lint hook** | INV-14, INV-15, INV-16, INV-19 | Advisory warning |
