# Analyze Skill -- Gotchas

Known failure points and edge cases for data analysis.

## R Packages

- Don't export model tables with `fixest::etable()` / `modelsummary()` LaTeX output. Get a data frame (`modelsummary(..., output = "data.frame")`, `broom::tidy()`, `parameters::model_parameters()`), format it with `apa_num()`/`apa_p()`/`apa_ci()`, then `apa_flextable()`.
- `modelsummary` silently drops coefficients when `coef_rename` keys don't match variable names exactly. Always check output dimensions against model object.
- `flextable::save_as_docx()` previews are for humans; the manuscript build reads the `.rds`. Always save both with `apa_save_table()`.
- `apa_flextable()` resets borders. Apply it before adding custom rules (or use `apa_spanner()` for spanner heads).
- Clustering syntax differs between `fixest` and `lm` -- always use `fixest::feols()` for cluster-robust standard errors.
- R's `haven::read_dta()` preserves Stata value labels as attributes -- use `as_factor()` explicitly or they'll be invisible numeric codes.
- `did::att_gt()` requires the group variable to be the year of first treatment (0 for never-treated). Miscoding this produces silent wrong results.
- `rdrobust` returns an object where `$coef` is a matrix, not a vector. Access the point estimate with `$coef[1]` or `$Estimate[1]`.

## Data Handling

- Pre-Code Report blocks on strategic alignment if strategy memo doesn't exist. Run `/strategize` first, or proceed with user description and flag the gap.
- `saveRDS()` required for ALL computed objects, not just final outputs. Intermediate objects enable debugging and writer handoff.
- `here()` resolves from `.here` file or `.Rproj` file -- make sure one exists at project root.
- Never use `setwd()` -- it breaks reproducibility across machines (INV-19).
- When merging datasets, always check merge rates. A 60% merge rate is a red flag. Document non-merges.

## Numerical Issues

- Never compare floats with `==`. Use `all.equal()` or tolerance: `abs(a - b) < 1e-10`.
- `qnorm(0)` returns `-Inf` and `qnorm(1)` returns `Inf`. Guard inverse link functions with `pmin(pmax(p, eps), 1 - eps)`.
- `1:n` when `n == 0` produces `c(1, 0)`. Use `seq_len(n)` instead.
- `sapply()` returns a list when lengths differ and a matrix when they match. Use `vapply()` for type safety.

## Output

- Figures must not have titles inside ggplot (INV-12). Titles go in `paper/displays.csv`.
- Tables carry no number, title, or note (INV-13) — those live in `displays.csv`.
- PNG at 300 dpi is the required figure format for Word and PowerPoint. Set `bg = "white"` in `ggsave()` or transparent backgrounds turn black in some viewers.
- Never write to `paper/manuscript.docx`. After handoff, regenerated tables/figures are delivered as files the user copies in.
- `results_summary.md` is mandatory. Without it, the writer agent cannot draft the results section.

## Cross-Language (--dual mode)

- R and Python handle NA differently in groupby/aggregate operations. Explicit `na.rm = TRUE` in R; `dropna()` in pandas.
- Factor ordering in R defaults to alphabetical; pandas categoricals preserve insertion order. This affects dummy variable encoding.
- `fixest` and `pyfixest` may differ slightly in cluster-robust SEs due to small-sample corrections.
- Sample sizes must match exactly across languages. Any difference is a data handling bug.
