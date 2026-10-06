---
paths:
  - "**/*.R"
  - "**/*.py"
  - "**/*.jl"
  - "**/*.do"
  - "paper/**"
  - "paper/tables/**"
  - "paper/figures/**"
  - "master_supporting_docs/**"
  - "explorations/**"
---

# Content Standards: Tables, Figures, PDFs, and Explorations

---

## 1. Table Standards

**Target:** APA 7 tables in Word (*Publication Manual*, §7.8–7.21): bold number and italic title above, horizontal rules only, notes below. Analysis scripts build each table as a **flextable** styled with `apa_flextable()` (`paper/word/apa_helpers.R`) and save it with `apa_save_table()`. The manuscript build adds the number, title, and note from `paper/displays.csv`.

Journal-specific conventions (asterisks, table placement) adapt to the target journal — see journal-profiles.md. Statistical reporting rules are in INV-4.

### No In-Table Titles or Notes

- **Never** put the title in the table body or as a header row
- **Never** put notes, sources, or footnotes inside the table
- Number, title, and note live in `paper/displays.csv` (draft) or in the *Table Number* / *Table Title* / *Table Note* paragraphs (Word master)
- The file name identifies what the table contains

### Building a Table in R

```r
source(here::here("paper", "word", "apa_helpers.R"))

tab <- data.frame(
  Predictor = c("Intercept", "Treatment", "Pretest"),
  b         = apa_num(c(50.12, 1.94, 0.61)),
  SE        = apa_num(c(0.88, 0.65, 0.04)),
  CI        = apa_ci(c(48.39, 0.67, 0.53), c(51.85, 3.21, 0.69)),
  beta      = c("", apa_num(c(.19, .58), leading_zero = FALSE)),
  p         = apa_p(c(1e-6, .003, 1e-6))
)

ft <- apa_flextable(tab)
ft <- flextable::set_header_labels(ft, b = "b", SE = "SE", CI = "95% CI", beta = "β", p = "p")
ft <- flextable::italic(ft, j = c("b", "SE", "p"), part = "header")   # statistical symbols italic
apa_save_table(ft, "reg_main_specification", dir = here::here("paper", "tables"))
```

- `apa_flextable()` sets Times New Roman 12, single-spaced cells, centered numeric columns with a left-aligned first column, and the three APA rules
- `apa_spanner(ft, labels, widths)` adds a spanner row with rules under the spanned columns (e.g., "Treatment" over *M* and *SD*)
- `apa_save_table()` writes `paper/tables/<name>.rds` (used by the build) and `<name>.docx` (a preview you can open in Word)
- Model output: build the data frame from `broom::tidy()`, `parameters::model_parameters()`, or `modelsummary(..., output = "data.frame")`, then format with `apa_num()` / `apa_p()` / `apa_ci()` before `apa_flextable()`

### APA Table Layout

- Rules: above the column heads, below the column heads, below the body; under spanner heads only across the spanned columns
- **Never** vertical rules, full grid borders, shading, or bold body text
- Note order below the table: general note (*Note.*), specific notes (superscript lowercase letters), probability note
- Wide tables: landscape page in Word (Layout › Orientation on a section) rather than shrinking the font below 10 pt

### Statistical Reporting in Tables

| Element | APA convention |
|---------|----------------|
| Column heads | Italicized statistical symbols: *M*, *SD*, *n*, *b*, *SE*, β, *t*, *p*, *d*, *r*, *F*, η²p |
| Confidence intervals | Brackets, lower and upper limits: [0.12, 0.45] (`apa_ci()`); or separate *LL* / *UL* columns under a "95% CI" spanner |
| Decimals | Two decimals by default; three for *p* values; consistent within a column |
| Leading zeros | Omit for values that cannot exceed 1 (*p*, *r*, *R*², α, ω, proportions): .45, not 0.45 (`apa_num(x, leading_zero = FALSE)`) |
| *p* values | Exact (.031); "< .001" below .001; never .000 (`apa_p()`) |
| Asterisks | Only if the journal profile permits; define every symbol in a probability note. Prefer an exact *p* column |
| Nested data | State levels and counts in the note (students, classrooms, schools); report variance components / ICC |
| Sample size | In the note, and per column if *n* varies |

### Column and Row Structure

- **Variable names** human-readable, not code names: "Pretest science score" not `pre_sci_z`
- Model-fit rows at the bottom: *N* (and clusters), *R*² or marginal/conditional *R*², ICC, AIC/BIC, or χ², CFI, TLI, RMSEA [90% CI], SRMR for latent variable models
- Panel labels ("Panel A: Grade 6") as italic rows spanning all columns are fine

### Preferred R Packages

| Purpose | Package |
|---------|---------|
| Table objects for Word | `flextable` (+ `officer`) with `apa_flextable()` |
| Tidy model output | `broom`, `broom.mixed`, `parameters`, `modelsummary(output = "data.frame")` |
| Effect sizes with CIs | `effectsize` (Cohen's *d*, Hedges' *g*, η²p, ω²) |
| APA in-text strings | `papaja::apa_print()` — copy its strings into `quality_reports/results_summary.md` so the writer never retypes numbers (INV-11, INV-22) |
| Descriptives / correlations | `apaTables`, `modelsummary::datasummary_correlation(output = "data.frame")` |
| APA-styled flextables in one call | `rempsyc::nice_table()` (acceptable alternative to `apa_flextable()`) |
| Latent variable models | `lavaan` + `semTools` (fit indices, invariance tests, ω) |

### File Naming

```
tables/
├── sumstats_correlations.rds / .docx
├── balance_baseline_equivalence.rds / .docx
├── cfa_fit_indices.rds / .docx
├── reg_main_specification.rds / .docx
└── reg_alternative_missing_data.rds / .docx
```

Pattern: `{table_type}_{content_description}`. Prefixes: `sumstats_`, `balance_`, `cfa_` / `invariance_`, `reg_` / `mlm_` / `sem_`, `anova_`, `meta_`. Subfolders (descriptive/, estimation/, robustness/) are fine; record the path in `displays.csv`.

### Prohibited Patterns

| Pattern | Reason |
|---------|--------|
| Title or note inside the table | They belong in `displays.csv` / the manuscript |
| Number and title below the table | APA places them above |
| Vertical rules or full grid | Horizontal rules only (INV-3) |
| Tables pasted as images | Journals and reviewers need editable tables |
| Tables typed by hand in Word from console output | Breaks traceability (INV-11, INV-22); generate them from code |
| "*p* = .000" or "n.s." without statistics | Report exact *p* (or < .001) and the statistic |
| Leading zero on bounded statistics (0.45 for *r*) | APA 7 §6.36 |
| Asterisks without a probability note | Every symbol must be defined |
| Raw variable names in labels | Human-readable labels required |

### Table Type Templates

Adapt columns to the paper's needs. Layouts shown as rows (columns separated by `|`).

**Descriptive Statistics and Correlations** (the standard first table in psychology/education):

| Variable | *M* | *SD* | 1 | 2 | 3 |
|----------|-----|------|---|---|---|
| 1. Pretest achievement | 48.2 | 9.6 | (.91) | | |
| 2. Self-efficacy | 3.42 | 0.71 | .38 | (.87) | |
| 3. Posttest achievement | 52.7 | 10.1 | .64 | .41 | (.92) |

- Reliabilities (ω or α — say which) in parentheses on the diagonal, explained in the note
- Correlations without leading zeros; state *N* and missing-data handling in the note

**Regression / Multilevel Model Results:** Predictor | *b* | *SE* | 95% CI | β | *p*, with italic panel rows "Fixed effects" and "Random effects" (classroom intercept variance, residual variance) and an ICC row.

**ANOVA:** Source | *df* | *F* | *p* | η²p | 95% CI.

**Baseline Equivalence** (WWC convention): Variable | Treatment *M* | *SD* | Comparison *M* | *SD* | Hedges' *g*, with spanners "Treatment" and "Comparison". |*g*| > 0.25 fails WWC baseline equivalence; 0.05–0.25 requires statistical adjustment.

**Measurement Model Fit / Invariance:** Model | χ² | *df* | CFI | TLI | RMSEA [90% CI] | SRMR | ΔCFI, rows Configural / Metric / Scalar.

---

## 2. Figure Standards

APA 7 (§7.22–7.36): bold figure number and italic title **above** the image; a note below. The build places them from `paper/displays.csv`.

- **Never add titles or subtitles inside ggplot** — `labs(title = NULL, subtitle = NULL)`
- **Figure information goes in two places:** the file name (`fig2_condition_by_prior_achievement.png`) and the `title` column of `displays.csv` (or the *Figure Title* paragraph in the Word master)
- **Panel labels are the exception** — "Panel A: Grade 6" inside multi-panel figures is fine
- **Axis labels publication-quality, title case, with units or scale** — "Self-Efficacy (1–5)" not `se_mean`
- **Legends inside the image**, not obscuring data
- **Show uncertainty** — error bars or ribbons for every estimate, with what they represent (95% CI, ±1 *SE*) stated in the note; show raw data distributions (jittered points, violins) alongside means for experimental data
- **Sans serif fonts inside the figure** (8–14 pt at final size): `theme_minimal(base_family = "sans")`
- **Output PNG at 300 dpi or more** for Word: `ggsave(here::here("paper", "figures", "fig1_main.png"), width = 6.5, height = 4, dpi = 300)`. Keep a PDF or TIFF copy too if the journal asks for production files
- **Width** — 6.5 in fills the text block; the build inserts figures at 6.5 in
- **Colorblind-friendly palettes** — viridis, Okabe–Ito, `scale_color_brewer(palette = "Set2")`; never red/green contrast alone
- **Grayscale-readable** — combine color with shape and linetype
- **Path diagrams (SEM/mediation)** — `semPlot`/`lavaanPlot` exported to PNG, or drawn in PowerPoint and exported; label paths with standardized estimates and CIs or SEs; define the notation in the note

---

## 3. PDF Processing

### The Safe Processing Workflow

**Step 1: Receive PDF Upload**
- User uploads PDF to `master_supporting_docs/supporting_papers/` or `supporting_slides/`
- Claude DOES NOT attempt to read it directly

**Step 2: Check PDF Properties**
```bash
pdfinfo paper_name.pdf | grep "Pages:"
ls -lh paper_name.pdf
```

**Step 3: Create Subfolder and Split**
```bash
mkdir -p paper_name/

for i in {0..9}; do
  start=$((i*5 + 1))
  end=$(((i+1)*5))
  gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
     -dFirstPage=$start -dLastPage=$end \
     -sOutputFile="paper_name/paper_name_p$(printf '%03d' $start)-$(printf '%03d' $end).pdf" \
     paper_name.pdf 2>/dev/null
done
```

**Step 4: Process Chunks Intelligently**
- Read chunks ONE AT A TIME using the Read tool
- Extract key information from each chunk
- Build understanding progressively
- Don't try to hold all chunks in working memory

**Step 5: Selective Deep Reading**
- After scanning all chunks, identify the most relevant sections
- Only read those sections in detail for slide development
- Skip appendices, references, or less relevant sections unless needed

### Error Handling Protocol

**If a chunk fails to process:**
1. Note the problematic chunk (e.g., "Chunk p021-025 failed")
2. Try splitting into 1-2 page pieces
3. If still failing, skip and document the gap

**If splitting fails:**
1. Check if Ghostscript is installed: `gs --version`
2. Try alternative: `pdftk paper.pdf burst output paper_%03d.pdf`
3. If all else fails, ask user to upload specific page ranges manually

**If memory/token issues persist:**
1. Process only 2-3 chunks per session
2. Focus on specific sections user identifies as most important

---

## 4. Exploration Folder Protocol

**All experimental work goes into `explorations/` first.** Never directly into production folders.

### Folder Structure

```
explorations/
├── ACTIVE_PROJECTS.md
├── [project]/
│   ├── README.md          # Goal, status, findings
│   ├── R/                 # Code (use _v1, _v2 for iterations)
│   ├── scripts/           # Test scripts
│   ├── output/            # Results
│   └── SESSION_LOG.md     # Progress notes
└── ARCHIVE/
    ├── completed_[project]/
    └── abandoned_[project]/
```

### Lifecycle

1. **Create** — `mkdir -p explorations/[name]/{R,scripts,output}` + README from `templates/exploration-readme.md`
2. **Develop** — work entirely within the exploration folder
3. **Decide:**

   - **Graduate to production** — copy to `R/`, `scripts/`; requires quality >= 80, tests pass, code clear. Move to `ARCHIVE/completed_[project]/`
   - **Keep exploring** — document next steps in README
   - **Abandon** — move to `ARCHIVE/abandoned_[project]/` with explanation (use `templates/archive-readme.md`)

### Graduate Checklist

- [ ] Quality score >= 80
- [ ] All tests pass
- [ ] Results replicate within tolerance
- [ ] Code is clear without deep context
- [ ] README explains approach and findings

---

## 5. Exploration Fast-Track

**Lightweight workflow for experimental work.** Quality threshold: 60/100 (vs 80 for production). No planning needed.

### Steps

1. **Research value check** — Does this improve the project? If NO, don't build it.
2. **Create folder** — `mkdir -p explorations/[name]/{R,scripts,output}` + README + SESSION_LOG.md
3. **Code immediately** — no plan needed. Must-haves: code runs, results correct, goal documented. Not needed: Roxygen docs, full tests, perfect style.
4. **Log progress** — append 2-3 lines to SESSION_LOG.md as you work
5. **Decision point** — keep exploring, graduate to production (upgrade to 80/100), or archive with brief explanation

### When to Stop (Kill Switch)

At any point: stop, archive with note ("Attempted X, hit blocker Y"), move on. No guilt — exploration is inherently uncertain.
