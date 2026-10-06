# Figure Standards (APA 7, Word)

Publication-quality figures for APA manuscripts in Word. Every figure is a PNG (300 dpi or more) that the manuscript build inserts at 6.5 in wide, with the bold number and italic title above it and a note below — all taken from `paper/displays.csv`.

Mirror of `.claude/rules/content-standards.md` Section 2, with code. If the two ever differ, `content-standards.md` wins.

---

## Core Rules

- **Never add titles or subtitles inside ggplot** — `labs(title = NULL, subtitle = NULL)` (INV-12)
- **Figure information goes in two places:**
  1. **File name** — descriptive, e.g., `fig2_condition_by_prior_achievement.png`
  2. **`paper/displays.csv`** — the APA title and note (or the *Figure Title* / *Figure Note* paragraphs once the Word master exists)
- **Panel labels are the exception** — "Panel A: Grade 6" inside multi-panel figures (`patchwork`, `cowplot`) is fine
- **Axis labels publication-quality, title case, with units or scale** — "Self-Efficacy (1–5)" not `se_mean`
- **Sans serif text inside the figure** (APA recommends sans serif, 8–14 pt at final size)
- **Show uncertainty** — 95% CIs or ±1 *SE*, stated in the note

---

## Font and Theme

```r
theme_apa <- theme_minimal(base_family = "sans", base_size = 12) +
  theme(
    panel.grid.minor = element_blank(),
    legend.position  = "bottom",
    plot.title       = element_blank(),   # No titles -- INV-12
    plot.subtitle    = element_blank(),
    axis.line        = element_line(color = "black")
  )

theme_set(theme_apa)
```

Python (matplotlib):
```python
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 12,
                     "axes.spines.top": False, "axes.spines.right": False})
```

---

## Axis Labels

- **Show all waves / years** on the x-axis when there are about 20 ticks or fewer: `scale_x_continuous(breaks = min_wave:max_wave)`
- **Human-readable labels with units:** "Posttest Score (Scale Score)", "Proportion Correct", "Weeks Since Baseline"

---

## Color

- **Colorblind-friendly palettes** — Okabe–Ito, viridis, `scale_color_brewer(palette = "Set2")`; never red/green contrast alone
- **Grayscale-readable** — combine color with `shape` and `linetype`

```r
okabe_ito <- c("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000")
scale_color_manual(values = okabe_ito)
scale_color_viridis_d(end = 0.85)
```

---

## Common Figure Types (psychology / education)

### Means by Condition with Raw Data
```r
ggplot(df, aes(condition, score)) +
  geom_jitter(width = 0.15, alpha = 0.25) +
  stat_summary(fun.data = mean_cl_normal, geom = "errorbar", width = 0.1) +
  stat_summary(fun = mean, geom = "point", size = 3) +
  labs(x = "Condition", y = "Posttest Score")
```

### Interaction / Simple Slopes
```r
ggplot(pred, aes(prior, fit, color = condition, linetype = condition)) +
  geom_ribbon(aes(ymin = lower, ymax = upper, fill = condition), alpha = 0.15, color = NA) +
  geom_line() +
  labs(x = "Prior Achievement (Centered)", y = "Predicted Posttest Score",
       color = "Condition", linetype = "Condition", fill = "Condition")
```

### Growth Trajectories
```r
ggplot(traj, aes(wave, estimate, group = group, color = group, shape = group)) +
  geom_line() + geom_point(size = 2) +
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.1) +
  labs(x = "Wave", y = "Reading Score")
```

### Coefficient / Forest Plot (incl. meta-analysis)
```r
ggplot(coefs, aes(estimate, reorder(term, estimate))) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "gray50") +
  geom_errorbarh(aes(xmin = lower, xmax = upper), height = 0.2) +
  geom_point() +
  labs(x = "Standardized Effect (95% CI)", y = NULL)
```

### Event Study / RDD
Event-study and RD plots follow the same rules: zero reference line, CIs on every point, treatment onset or cutoff marked, axis labels in words.

---

## Export

```r
ggsave(
  here("paper", "figures", "fig1_condition_means.png"),
  plot = p, width = 6.5, height = 4.5, dpi = 300, bg = "white"
)
```

- PNG, 300 dpi minimum (600 dpi for line art if the journal asks); white background
- Keep a vector copy (`.pdf` or `.svg`) only if the journal requests production files
- Add the figure to `paper/displays.csv` (writer fills in title and note)

---

## File Naming

```
figures/
├── fig1_condition_means.png
├── fig2_condition_by_prior_achievement.png
└── figS1_attrition_flow.png        # supplementary
```

Pattern: `fig{N}_{description}.png` — the number in the file name is provisional; `displays.csv` holds the final number.

---

## Prohibited Patterns

| Pattern | Reason |
|---------|--------|
| `ggtitle()` or `labs(title = "...")` | Titles go above the image in the manuscript (INV-12) |
| Screenshots of console output or of tables | Tables must be editable Word tables (INV-13) |
| JPEG for charts | Lossy compression blurs lines and text; use PNG |
| Low resolution (< 300 dpi) | Journals reject; Word upscaling blurs |
| Red/green only distinctions | Not colorblind-safe |
| Unlabeled error bars | The note must say what they represent (INV-2) |
