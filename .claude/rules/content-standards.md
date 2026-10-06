---
paths:
  - "**/*.R"
  - "**/*.py"
  - "**/*.jl"
  - "**/*.do"
  - "**/*.tex"
  - "paper/tables/**"
  - "paper/figures/**"
  - "master_supporting_docs/**"
  - "explorations/**"
---

# Content Standards: Tables, Figures, PDFs, and Explorations

---

## 1. Table Standards

**Target:** APA 7 tables (*Publication Manual*, §7.8–7.21): horizontal booktabs rules only, number and title above, notes below. The paper uses `tabular` + `booktabs` + `threeparttable` inside the `apa7` class, which formats the caption (bold "Table 1", italic title on the next line) automatically.

Journal-specific conventions (asterisks, float placement) adapt to the target journal — see journal-profiles.md. Statistical reporting rules are in INV-4.

### No In-Table Titles or Notes

- **Never** embed titles inside the table body or as a table header row
- **Never** embed notes, sources, or footnotes inside the table itself
- Number and title come from `\caption{}` (placed first); notes from `\begin{tablenotes}` below the tabular
- The file name and folder identify what the table contains

### APA Table Layout

Exactly three horizontal rules plus optional `\cmidrule` spanners, and **zero vertical lines**:

```latex
\begin{table}[tbp]
\begin{threeparttable}
\caption{Multilevel Model Predicting Posttest Science Achievement}
\label{tab:main}
\input{tables/estimation/reg_main_specification.tex}
\begin{tablenotes}[para, flushleft]
{\small
\textit{Note.} $N = 1{,}204$ students in 48 classrooms. Estimates are unstandardized
fixed effects from a two-level random-intercept model; standardized estimates
($\beta$) use the pooled posttest standard deviation. CI = confidence interval.
}
\end{tablenotes}
\end{threeparttable}
\end{table}
```

- `\toprule` above column headers, `\midrule` below them, `\bottomrule` at the end
- `\cmidrule(lr){2-4}` for spanners over column groups
- Note order: general note (`\textit{Note.}`), then specific notes (superscript lowercase letters, `\textsuperscript{a}`), then probability note
- **Never** `\hline`, `|` in column specs, shading, or cell borders

### Statistical Reporting in Tables

| Element | APA convention |
|---------|----------------|
| Column heads | Italicized statistical symbols: *M*, *SD*, *n*, *b*, *SE*, $\beta$, *t*, *p*, *d*, *r*, *F*, $\eta^2_p$ |
| Confidence intervals | Brackets, lower and upper limits: [0.12, 0.45]; or separate *LL* / *UL* columns under a "95% CI" spanner |
| Decimals | Two decimals by default; three for *p* values; consistent within a column |
| Leading zeros | Omit for values that cannot exceed 1 (*p*, *r*, $R^2$, $\alpha$, $\omega$, proportions): .45, not 0.45 |
| *p* values | Exact (.031); "< .001" below .001; never .000 |
| Asterisks | Only if the journal profile permits. Then define every symbol in a probability note: `\textsuperscript{*}$p < .05$. \textsuperscript{**}$p < .01$. \textsuperscript{***}$p < .001$.` Prefer an exact *p* column. |
| Nested data | State levels and counts in the note (students, classrooms, schools); report variance components / ICC |
| Sample size | In the note, and per column if *n* varies |

Example rows (unstandardized estimate, SE, CI, standardized estimate, exact *p*):
```
Treatment          & 0.21 & 0.07 & [0.07, 0.35] & .18 & .004 \\
Pretest            & 0.62 & 0.04 & [0.54, 0.70] & .59 & < .001 \\
```

### Column and Row Structure

- **Variable names** human-readable, not raw code names: `Pretest science score` not `pre_sci_z`; `Female` not `sex_2`
- **Numeric columns** decimal-aligned (`siunitx` `S` columns) or centered
- Model-fit rows at the bottom: *N* (and clusters), $R^2$ or marginal/conditional $R^2$, ICC, AIC/BIC, or $\chi^2$, CFI, TLI, RMSEA [90% CI], SRMR for latent variable models
- Panel labels (`\multicolumn{k}{l}{\textit{Panel A: Grade 6}}`) are fine for multi-outcome tables

### Preferred R Packages

**Model tables: `modelsummary`** (bare tabular, no stars by default)

```r
library(modelsummary)

modelsummary(
  models,
  output    = "latex_tabular",            # bare tabular, no wrapper
  statistic = c("std.error", "conf.int"),
  conf_level = 0.95,
  stars     = FALSE,                      # APA default; set per journal profile
  fmt       = 2,
  coef_rename = c("treatment" = "Treatment", "pretest" = "Pretest"),
  gof_map   = c("nobs", "r2.marginal", "r2.conditional", "icc"),
  escape    = FALSE
)
```

**In-text statistics strings: `papaja::apa_print()`** — produces APA-formatted strings (*t*(48) = 2.31, *p* = .025, *d* = 0.66, 95% CI [0.08, 1.23]) from model objects. Write them to `quality_reports/results_summary.md` so the writer copies numbers rather than retyping them (INV-11, INV-22).

**Effect sizes: `effectsize`** (Cohen's *d*, Hedges' *g*, $\eta^2_p$, $\omega^2$ with CIs). **Descriptives/correlation matrices:** `apaTables` or `modelsummary::datasummary_correlation()`. **Latent variable models:** `lavaan` + `semTools` (fit indices, invariance tests, $\omega$ reliability).

**Descriptive tables: `kableExtra`**

```r
library(kableExtra)

kbl(df, format = "latex", booktabs = TRUE, escape = FALSE,
    align = c("l", rep("c", ncol(df) - 1)))
```

### Typography

- Body font inherits from the class — no extra commands
- `\small` acceptable inside tables when needed; use `landscape` for wide tables rather than going below `\small`
- Statistical symbols italic (Greek letters upright as typeset in math mode)
- Never bold table body content

### Export

```r
# Write .tex fragment (no \begin{table} wrapper -- added in main.tex)
writeLines(tex_output, file.path("paper/tables", "reg_main_specification.tex"))
```

- Output a **bare `tabular` environment** (no `\begin{table}` float, caption, or notes)
- `main.tex` wraps it with `\begin{table}`, `\caption{}`, `threeparttable`, and notes
- Write to `paper/tables/`

### File Naming

```
tables/
├── descriptive/
│   ├── sumstats_correlations.tex
│   └── balance_baseline_equivalence.tex
├── measurement/
│   ├── cfa_fit_indices.tex
│   └── invariance_by_grade.tex
├── estimation/
│   ├── reg_main_specification.tex
│   └── mlm_moderation_prior_achievement.tex
└── robustness/
    └── reg_alternative_missing_data.tex
```

Pattern: `{table_type}_{content_description}.tex`

- `sumstats_` descriptives and correlations; `balance_` baseline equivalence; `cfa_` / `invariance_` measurement models
- `reg_` / `mlm_` / `sem_` model output; `anova_` ANOVA tables; `meta_` meta-analytic summaries

### Prohibited Patterns

| Pattern | Reason |
|---------|--------|
| Title row inside the table | Titles go in `\caption{}` |
| Notes embedded in table body | Notes go below via `tablenotes` |
| Caption after the tabular | APA places number and title above |
| `\hline` / vertical rules | booktabs horizontal rules only |
| "*p* = .000" or "n.s." without statistics | Report exact *p* (or < .001) and the statistic |
| Leading zero on bounded statistics (0.45 for *r*) | APA 7 §6.36 |
| Asterisks without a probability note | Every symbol must be defined |
| `stargazer` | Deprecated workflow; use `modelsummary` |
| Raw variable names in labels | Human-readable labels required |
| `\begin{table}` in R output | Float wrapper lives in `main.tex` (INV-13) |

### Table Type Templates

Adapt columns to the paper's needs.

**Descriptive Statistics and Correlations** (the standard first table in psychology/education):
```
\toprule
Variable                 & \textit{M} & \textit{SD} & 1     & 2     & 3     \\
\midrule
1. Pretest achievement   & 48.2 & 9.6  & (.91) &       &       \\
2. Self-efficacy         & 3.42 & 0.71 & .38   & (.87) &       \\
3. Posttest achievement  & 52.7 & 10.1 & .64   & .41   & (.92) \\
\bottomrule
```
- Reliabilities ($\omega$ or $\alpha$, say which) in parentheses on the diagonal, explained in the note
- Correlations without leading zeros; state *N* and how missing data were handled in the note
- Binary variables: percentage in the *M* column, *SD* blank, noted

**Regression / Multilevel Model Results:**
```
\toprule
                 &      &       &                & \multicolumn{2}{c}{Standardized} \\
\cmidrule(lr){5-6}
Predictor        & \textit{b} & \textit{SE} & 95\% CI       & $\beta$ & \textit{p} \\
\midrule
\multicolumn{6}{l}{\textit{Fixed effects}} \\
Intercept        & 50.12 & 0.88 & [48.39, 51.85] &        & < .001 \\
Treatment        & 1.94  & 0.65 & [0.67, 3.21]   & .19    & .003   \\
Pretest          & 0.61  & 0.04 & [0.53, 0.69]   & .58    & < .001 \\
\midrule
\multicolumn{6}{l}{\textit{Random effects}} \\
Classroom intercept variance & 4.21 & & & & \\
Residual variance            & 52.80 & & & & \\
\midrule
ICC              & .07 & & & & \\
\bottomrule
```

**ANOVA:**
```
\toprule
Source               & \textit{df} & \textit{F} & \textit{p} & $\eta^2_p$ & 95\% CI     \\
\midrule
Condition            & 2, 117 & 4.56 & .012 & .07 & [.01, .15] \\
Time                 & 1, 117 & 21.40 & < .001 & .15 & [.06, .26] \\
Condition $\times$ Time & 2, 117 & 3.12 & .048 & .05 & [.00, .12] \\
\bottomrule
```

**Baseline Equivalence** (randomized and quasi-experimental studies; WWC convention):
```
\toprule
Variable           & \multicolumn{2}{c}{Treatment} & \multicolumn{2}{c}{Comparison} & \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}
                   & \textit{M} & \textit{SD} & \textit{M} & \textit{SD} & Hedges' \textit{g} \\
\midrule
Pretest            & 48.6 & 9.4 & 47.9 & 9.8 & 0.07 \\
Free/reduced lunch (\%) & 41.2 & & 43.5 & & -0.05 \\
\bottomrule
```
- Report standardized differences; |*g*| > 0.25 fails WWC baseline equivalence, 0.05–0.25 requires statistical adjustment

**Measurement Model Fit / Invariance:**
```
\toprule
Model        & $\chi^2$ & \textit{df} & CFI & TLI & RMSEA [90\% CI]  & SRMR & $\Delta$CFI \\
\midrule
Configural   & 312.4 & 164 & .962 & .956 & .047 [.039, .055] & .041 & --    \\
Metric       & 330.9 & 176 & .960 & .957 & .046 [.038, .054] & .049 & -.002 \\
Scalar       & 371.2 & 188 & .952 & .951 & .049 [.042, .057] & .053 & -.008 \\
\bottomrule
```

---

## 2. Figure Standards

APA 7 (§7.22–7.36): figure number (bold) and title (italic, title case) **above** the image; a note below. In `apa7`, write `\caption{}` before `\includegraphics` and the note with `\figurenote{}`.

- **Never add titles or subtitles inside ggplot** — use `labs(title = NULL, subtitle = NULL)`
- **Figure information goes in two places:**
  1. **File name** — descriptive, e.g., `fig2_condition_by_prior_achievement.pdf`
  2. **LaTeX `\caption{}`** — the authoritative title, numbered and editable without re-running R
- **Panel labels are the exception** — "Panel A: Grade 6" inside multi-panel figures is fine
- **Axis labels publication-quality and in title case** — "Posttest Score" not "post_sci"; include units or scale ("Self-Efficacy (1–5)")
- **Legends inside the figure image**, positioned so they do not obscure data
- **Show uncertainty** — error bars or ribbons for every estimate, with what they represent (95% CI, ±1 *SE*) stated in the figure note. Prefer showing raw data distributions (jittered points, violins, raincloud plots) alongside means for experimental data.
- **Sans serif fonts inside the figure** — APA recommends a sans serif font (8–14 pt at final size) for figure text: `theme_minimal(base_family = "sans")` or `"Arial"`
- **Show all years / waves on the x-axis** when there are about 20 ticks or fewer
- **Output PDF for figures** — vector graphics. PNG only for raster content (photos, brain images).
- **Colorblind-friendly palettes** — `viridis`, `scale_color_brewer(palette = "Set2")`, or Okabe–Ito. Never rely on red/green contrast alone.
- **Grayscale-readable** — combine color with shape and linetype
- **Figure width** — single panel `width=\linewidth`; side-by-side panels `0.48\linewidth` each
- **Path diagrams (SEM/mediation)** — draw with TikZ or export from `semPlot`/`lavaanPlot`; label paths with standardized estimates and CIs or SEs; define the notation in the figure note

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
