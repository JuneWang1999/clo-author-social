---
title: "[Talk Title]"
subtitle: "[Venue, Month Year]"
author: "[Presenter Name]"
---

<!--
Slide Markdown for pandoc -> PowerPoint (paper/talks/build_talk.sh <name>).
- Each "## Title" starts a new slide (slide level 2). "# Section" makes a section-divider slide.
- Images: file names are found in paper/figures/ automatically.
- Image + text on one slide: use the columns block below (otherwise pandoc
  moves the text to its own slide).
- Speaker notes: a "::: notes" block at the end of a slide.
- Tables: Markdown pipe tables, 4-5 columns max; detailed tables go in Backup.
- Math: $...$ becomes a native PowerPoint equation.
- Incremental bullets: wrap the list in "::: incremental".
-->

## The Puzzle

- [One-sentence fact or tension that motivates the study]
- [Why it matters for theory, practice, or policy]

::: notes
[What to say; 30-60 seconds per slide]
:::

## Research Question

[One sentence]

# Study Design

## Design and Sample

- [Design: e.g., cluster-randomized trial, 24 classrooms]
- [Participants: N, key characteristics]
- [Primary outcome and measure]

## Main Result

:::::: {.columns}
::: {.column width="60%"}
![](fig1_condition_means.png)
:::
::: {.column width="40%"}
- [Effect in words]
- *d* = [x], 95% CI [[a], [b]]
:::
::::::

::: notes
[Interpretation against field benchmarks]
:::

# Takeaways

## What We Learned

1. [Finding 1]
2. [Finding 2]
3. [Implication]

## Thank You

[email] · [preprint / OSF link]

# Backup

## Full Model Results

| Predictor | *b* | *SE* | 95% CI | *p* |
|-----------|-----|------|--------|-----|
| Treatment | [x] | [x] | [[a], [b]] | [x] |
