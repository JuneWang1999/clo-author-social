# Manuscript Review: 8 Check Categories

Extracted from `writer-critic.md`. Used by the writer-critic agent for manuscript review.

---

## Prerequisite Checks

**Before running categories:**

- Read `.claude/rules/content-invariants.md` -- enforce INV-1 through INV-13, INV-22, INV-23 (JARS), and INV-24 (bias-free language). Cite invariant numbers (e.g., "violates INV-3") in report alongside deductions.
- Read `.claude/rules/working-paper-format.md` -- APA 7 manuscript standard; enforce all Required items listed in the deduction table.
- Read the target journal's profile in `.claude/references/journal-profiles.md` -- abstract limit, float placement, asterisk policy, required statements.
- Identify the paper type (reduced-form, structural, theory+empirics, descriptive) from the strategy memo or the manuscript itself. This determines which checks apply.

---

## 1. Structure and Flow

- Does the paper follow APA structure: untitled Introduction → Method → Results → Discussion → References (or Study 1…k → General Discussion for multi-study papers)?
- Does the introduction end with numbered hypotheses or research questions that match the preregistration (if any)?
- Are confirmatory and exploratory analyses clearly separated in Results?
- Does the Discussion address limitations and constraints on generality specifically?
- Does each paragraph have a single identifiable argument move (motivation, result statement, mechanism, qualification, etc.)?
- Are transitions between sections coherent?
- Does the introduction state the gap and the present study's contribution before the hypotheses?
- No economics-style roadmap paragraph ("The rest of the paper is organized as follows") -- APA papers do not use one (-2)
- Does the Discussion restate each main finding with its effect size?

**Paper-type-specific** (argument moves inside the APA introduction; APA introductions end with hypotheses and usually do not preview numerical results):

**Reduced-form:** Introduction follows: motivation -> question -> stakes -> identification preview -> result -> literature positioning?

**Structural:** Introduction includes model preview -> estimation/counterfactual preview -> key counterfactual result -> literature?

**Theory + empirics:** Introduction includes theory preview -> empirical preview -> literature positioning?

**Descriptive:** Introduction includes data/measurement innovation -> key fact -> why it matters -> literature?

---

## 2. Claims and Evidence

- Every empirical claim is supported by a table, figure, or citation
- No orphan claims (assertions without evidence)
- Numbers in text match the tables and figures exactly (INV-11)
- Effect sizes stated with units or standardized metrics and 95% CIs ("*d* = 0.32, 95% CI [0.10, 0.54]", not "the effect was significant") (INV-4)
- Statistics formatted per APA: exact *p*, italicized symbols with *df*, no leading zeros on bounded statistics (INV-4) -- -2 per, max -10
- Null results not described as "no effect" without an equivalence test, Bayes factor, or CI-based argument -- -3 per
- Comparisons to prior literature include specific magnitudes from cited papers
- No stale numbers (values that don't match current output files)

**Claim-source map verification (INV-22):**
- Does `quality_reports/claim_source_map_{project}.md` exist? If not: -15
- Every numerical claim in the manuscript has a map entry? -5 per missing
- Map entries point to files that exist? -10 per broken link
- Numbers in the map match the manuscript? -5 per mismatch

---

## 3. Identification Fidelity

- Does the empirical strategy section accurately describe the strategy memo's design?
- No overclaiming: causal language only in papers with causal designs (INV-8)
- Assumptions named and stated formally (parallel trends, exclusion restriction, continuity, etc.)
- Threats acknowledged -- no "our results are robust to all concerns"
- Estimand clearly stated (ATE, ITT vs. treatment-on-the-treated/CACE, conditional indirect effect, or equivalent)
- Method meets JARS (INV-23): sample-size justification, exclusions/attrition/missing data, reliability in this sample, randomization level, transparency statement -- -5 per missing element, max -15
- Nested data (students in classrooms/schools) analyzed with multilevel models or cluster-robust inference -- -10 if ignored
- Mediation/longitudinal claims match the design: no causal mediation language from cross-sectional data (INV-8)

**Paper-type-specific:**

**Reduced-form:** Design-specific elements present (pre-trends for DiD, first stage for IV, bandwidth for RDD, event definition for ES)?

**Structural:** Identification argument maps data moments to parameters? Estimation method justified?

**Theory + empirics:** Testable predictions numbered and linked to evidence?

**Descriptive:** No causal language. Patterns described as correlations or associations.

**Experiment / RCT:** Randomization level and method, manipulation checks, attrition (overall and differential), and intention-to-treat analysis described?

**Measurement / psychometric:** Factor structure, reliability, and measurement invariance reported before group comparisons?

---

## 4. Writing Quality

Run the 24-pattern AI detection check from the Writer's cleanup pass:

**Content patterns:**
- Significance inflation ("pivotal moment", "transformative impact", "groundbreaking") -- -3 per, max -9
- Promotional language -- -3 per, max -9
- Superficial -ing analyses ("highlighting...", "underscoring...") -- -2 per, max -6
- Vague attributions ("experts argue", "scholars have noted") -- -3 per, max -9

**Language patterns:**
- AI vocabulary (additionally, delve, foster, garner, interplay, tapestry, underscore, landscape) -- -2 per, max -10
- Copula avoidance ("serves as" instead of "is") -- -1 per, max -5
- Negative parallelisms ("not X but Y" overuse) -- -2 per, max -6
- Excessive hedging beyond field norms -- -3

**Style patterns:**
- Em dash overuse (>2 per page) -- -3
- Rule of three everywhere -- -3
- Uniform sentence length (no variation) -- -5

**Communication patterns:**
- Filler phrases ("It's important to note that...", "It is worth mentioning...") -- -2 per, max -6
- Announcements ("In the next section, we will discuss...") -- -2 per, max -6

**Bias-free language (INV-24):**
- "Subjects" for human participants, non-specific group labels, gendered defaults, "the elderly" -- -2 per, max -6

---

## 5. APA Format (Word)

Run `python3 .claude/scripts/check_docx_format.py <file.docx> --abstract-limit <journal limit>` and fold its FAIL/WARN lines into this category. Then enforce the remaining Required items from `.claude/rules/working-paper-format.md` by reading the snapshot:

| Issue | Deduction |
|-------|-----------|
| Margins, font/size, or double spacing not APA | -5 |
| Missing running head or page number | -2 |
| Running head > 50 characters or not all caps | -1 |
| Headings typed as bold body text (no heading style), numbered headings, or skipped levels | -2 |
| Introduction has a heading; Method/Results/Discussion headings missing | -3 |
| Title page missing title, authors, affiliations, or author note (non-masked) | -3 |
| Identifying information in a masked submission | -5 |
| Author note missing elements the journal requires (ORCID, disclosures, correspondence) | -2 |
| Missing keywords, or JEL codes present (INV-6) | -5 |
| Abstract exceeds 250 words or the journal limit (INV-5) | -3 |
| Hand-typed reference list, or citation/reference mismatches (INV-9) | -3, plus -1 per mismatch (max -5) |
| Vertical rules, full grid, or shading in tables (INV-3) | -3 |
| Missing table notes beginning with *Note.* (INV-1) | -5 per table, max -15 |
| Missing figure notes (INV-2) | -5 per figure, max -15 |
| Number/title below a table or figure instead of above | -2 per, max -6 |
| Table or figure not called out in text, or numbered out of order (INV-10) | -2 per, max -6 |
| Asterisks without a probability note, or asterisks the journal profile disallows (INV-4) | -3 |
| Table pasted as an image, or title inside a figure image (INV-12, INV-13) | -3 per, max -9 |
| References not double-spaced or without hanging indents | -2 |

---

## 6. Build Integrity

- **Draft phase:** `Rscript paper/build_manuscript.R` succeeds? If not: -20
- Placeholders in the output (`[Missing file: …]`, `[Section not drafted yet: …]`, `[Author One]`-style template text)? -5 per, max -15
- pandoc citation warnings (`Citeproc: citation … not found`)? -3 per missing key
- Every file listed in `displays.csv` exists in `paper/tables/` / `paper/figures/`? -5 per missing
- **Word-master phase:** `paper/manuscript.docx` modified by the pipeline instead of the user (INV-25)? -20 and flag to the Orchestrator
- Unresolved comments or tracked changes left in a file labeled for submission? -2 (report, do not resolve)

---

## 7. Voice Fidelity

**Only scored when `.claude/references/personal-style-guide.md` contains real content (not the template).**

Compare the draft against the style guide:

| Issue | Deduction |
|-------|-----------|
| Uses 3+ words from "author avoids" list | -5 per word, max -15 |
| Sentence length median off by >5 words from guide | -5 |
| Paragraph openings don't match documented patterns | -3 per, max -9 |
| Tone mismatch (e.g., bombastic when author is dry) | -10 |
| Hedging frequency doesn't match documented pattern | -3 |
| Em dash rate deviates significantly from guide | -2 |

If the style guide is still a template, report: "Voice fidelity not scored -- style guide not yet extracted. Run `/write style-guide [paper-dir]` to enable."

---

## 8. Notation Consistency

- Same symbol means the same thing everywhere (INV-7)
- Every symbol defined at first use
- Notation matches the strategy memo
- Subscript conventions consistent ($i$ for individual, $t$ for time, $g$ for group -- or whatever the paper uses, but consistent)
- Notation in tables matches notation in text

---

## Standalone Mode

When invoked via `/review [file.docx]` or `/review --proofread`, run categories **4, 5, 6, 8 only** (writing quality + APA/Word format + build integrity + notation). No strategy alignment -- just prose and format quality.

When invoked via `/review --all` or `/review --peer`, run all 8 categories.

---

## Report Format

```markdown
# Manuscript Review -- [Project Name]
**Date:** [YYYY-MM-DD]
**Reviewer:** writer-critic
**Paper type:** [Reduced-form / Structural / Theory+Empirics / Descriptive]
**Design:** [Experiment / Cluster RCT / Quasi-experiment / Correlational / Longitudinal / Psychometric / Meta-analysis]
**Target journal:** [from journal profile, or "generic APA"]
**Score:** [XX/100]
**Mode:** [Full / Standalone (prose quality only)]

## Structure and Flow: [COHERENT/ISSUES/MAJOR ISSUES]
## Claims and Evidence: [SUPPORTED/GAPS/UNSUPPORTED]
## Identification Fidelity: [FAITHFUL/OVERCLAIMED/MISREPRESENTED]
## Writing Quality: [CLEAN/AI PATTERNS FOUND/NEEDS REWRITE]
## APA Format (Word): [COMPLIANT/ISSUES/NON-COMPLIANT]
## JARS Completeness (INV-23): [COMPLETE/GAPS]
## Build Integrity: [PASS/WARNINGS/FAIL]
## Voice Fidelity: [MATCH/DRIFT/NOT SCORED]
## Notation Consistency: [CONSISTENT/INCONSISTENCIES]

## Score Breakdown
- Starting: 100
- [Deductions with invariant citations]
- **Final: XX/100**

## Claim-Source Map Status
- Map exists: [YES/NO]
- Claims mapped: [X/Y]
- Broken links: [list]

## Escalation Status: [None / Strike N of 3]
```
