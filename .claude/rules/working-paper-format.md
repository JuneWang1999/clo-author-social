# Manuscript Format Standard (APA 7)

All LaTeX papers generated or reviewed by this system must conform to the **APA 7 professional manuscript** format used for journal submission in psychology and education. The paper is built with the `apa7` document class in manuscript mode (`man`) and `biblatex` with `style=apa` (biblatex-apa) on `biber`. This rule applies to the writer, writer-critic, and verifier agents.

The filename is kept as `working-paper-format.md` because other files point here; the standard itself is APA 7 (*Publication Manual of the American Psychological Association*, 7th ed., 2020).

**Template:** `templates/latex/apa7-main.tex` — copy to `paper/main.tex` to start a new paper.

## Document Class and Layout

- `\documentclass[man,floatsintext]{apa7}` — `man` produces the professional manuscript: double spacing throughout, 1-inch margins, running head and page numbers in the header, title page, abstract page, title repeated on the first page of text.
- **Let the class do the layout.** Do NOT load `geometry`, `setspace`, `fancyhdr`, or `titlesec`, and do not call `\doublespacing`. They fight the class and break APA layout.
- `floatsintext` places tables and figures after first mention. Remove it when the target journal wants tables and figures after the references (APA permits either; check the journal profile).
- `mask` — add for masked (blind) review. It suppresses author names, affiliations, and the author note.
- `stu` (student paper) and `jou` (typeset-journal look) modes are not used for submissions.
- Fonts: keep the class default. APA 7 accepts any legible font (e.g., 12-pt Times New Roman, 11-pt Calibri/Arial/Georgia, 10-pt Computer Modern), so no font package is needed.

## Reference Preamble

The following preamble is the project standard. The writer-critic checks against it.

```latex
\documentclass[man,floatsintext]{apa7}
% Options: add `mask` for masked review; drop `floatsintext` if the journal
% wants tables/figures after the references.

% ====== Language and Quotation (required by biblatex-apa) ======
\usepackage[american]{babel}
\usepackage{csquotes}

% ====== Encoding and Typography ======
\usepackage[T1]{fontenc}
\usepackage{microtype}

% ====== Math ======
\usepackage{amsmath, amssymb, mathtools}
\usepackage{bm}                      % bold Greek for vectors/matrices

% ====== Tables and Figures ======
\usepackage{booktabs}
\usepackage{threeparttable}
\usepackage{array, makecell, multirow}
\usepackage{siunitx}
\usepackage{graphicx}
\usepackage{pdflscape}               % landscape pages for wide tables

% ====== Lists ======
\usepackage{enumitem}

% ====== Bibliography (biblatex-apa + biber) ======
\usepackage[style=apa, sortcites=true, sorting=nyt, backend=biber]{biblatex}
\DeclareLanguageMapping{american}{american-apa}
\addbibresource{../Bibliography_base.bib}

% ====== Hyperref (loaded second-to-last; no options -> no option clash) ======
\usepackage{hyperref}
\hypersetup{hidelinks, breaklinks=true}

% ====== Cleveref (loaded immediately after hyperref) ======
\usepackage[capitalise, noabbrev, nameinlink]{cleveref}
```

## Key Design Decisions

**Required** items are blocking — the writer-critic deducts points for violations. **Recommended** items improve output quality but are not publication blockers.

| Choice | Standard | Rationale |
|--------|----------|-----------|
| `apa7` class, `man` mode | Required | Produces APA 7 professional manuscript layout without manual tweaks |
| No `geometry` / `setspace` / `fancyhdr` / `titlesec` | Required | The class controls margins, spacing, running head, and heading levels |
| `biblatex` with `style=apa` + `biber` | Required | biblatex-apa implements APA 7 reference and citation rules (et al. rules, DOIs as URLs, sentence-case titles) |
| `babel` (american) + `csquotes` | Required | biblatex-apa depends on both for localization strings and quotation marks |
| `\textcite{}` / `\parencite{}` | Required | Native biblatex-apa commands; produce "Smith (2024)" and "(Smith, 2024)" |
| `booktabs` + `threeparttable` | Required | APA tables: horizontal rules only, notes under the table |
| `hyperref` loaded second-to-last, without options | Required | Avoids conflicts; `\hypersetup` sets options safely |
| `cleveref` loaded after `hyperref` | Required | `\Cref{tab:x}` → "Table 1"; `capitalise,noabbrev` matches APA ("Table 1", never "Tab. 1") |
| `microtype` | Required | Better spacing and line breaking |
| `floatsintext` | Recommended | Easier review; drop for journals that want floats at the end |
| `tabularray` (`tblr`/`talltblr`) | Not recommended | Its own caption machinery bypasses apa7 caption formatting |

## Title Page Format

```latex
\title{Effects of Retrieval Practice on Middle School Science Achievement}
\shorttitle{RETRIEVAL PRACTICE AND SCIENCE ACHIEVEMENT}   % running head, <= 50 characters

\authorsnames[1,2,1]{Author One, Author Two, Author Three}
\authorsaffiliations{
  {Department of Psychology, University One},
  {School of Education, University Two}}

\authornote{
  \addORCIDlink{Author One}{0000-0000-0000-0000}

  This study was preregistered at [registry URL]. Data, materials, and analysis
  code are available at [repository URL]. We have no known conflicts of interest
  to disclose. This research was supported by [funder, grant number].

  Correspondence concerning this article should be addressed to Author One,
  [address]. Email: author.one@university.edu}
```

Rules:
- Title in title case, bold and centered by the class — do NOT wrap it in `\textbf{}`. Aim for a focused title (about 12 words or fewer is typical); no abbreviations.
- `\shorttitle{}` is the running head: all caps, 50 characters or fewer including spaces.
- Single author: `\author{}` + `\affiliation{}`. Multiple authors: `\authorsnames[...]{...}` + `\authorsaffiliations{...}`. Do NOT use `\and` or `\thanks{}`.
- No degrees or titles after author names.
- Author note (APA 7 §2.7) paragraphs in order: ORCID iDs; changes of affiliation; disclosures and acknowledgments (preregistration, data/materials/code availability, conflicts of interest, funding, prior presentation); correspondence.
- Do not put author names or identifying information anywhere in the body for masked review — `mask` handles the title page; the text must avoid self-identifying statements ("in our previous study (Smith, 2023)" → "in a previous study (Smith, 2023)").

## Abstract and Keywords

```latex
\abstract{Abstract text, one paragraph, no indentation, 250 words or fewer
(or the target journal's limit, whichever is smaller).}

\keywords{retrieval practice, science achievement, cluster-randomized trial}
```

- Defined in the preamble, printed by `\maketitle` on its own page.
- 250 words or fewer by default (APA 7); many journals set 150–250 — the journal profile governs (INV-5).
- Structure: problem, participants/sample (with key characteristics), method/design, main findings with effect sizes and CIs, conclusions/implications.
- 3–5 keywords; lowercase except proper nouns (INV-6). No JEL codes.
- Journals that require a public significance or impact statement: the text goes in the submission system and in `quality_reports/` — see the journal profile.

## Section Structure

APA quantitative empirical article (JARS-Quant; Appelbaum et al., 2018):

1. **Introduction** — *no heading*. The class repeats the paper title at the top of the first text page. Problem, literature, hypotheses/research questions.
2. **Method** — Level 1 heading. Subsections (Level 2) such as: Transparency and Openness, Participants (or Sample), Sampling Procedures / Power Analysis, Measures (or Materials), Procedure, Design, Data Analysis.
3. **Results** — Level 1 heading. Preliminary analyses (missing data, assumptions, measurement models), then confirmatory hypotheses in preregistered order, then exploratory analyses (labeled as such).
4. **Discussion** — Level 1 heading. Support for hypotheses, interpretation, limitations, constraints on generality, implications for theory and practice.
5. **References** — `\printbibliography`.
6. **Tables and figures** (only if `floatsintext` is off), then **Appendices**.

**Multi-study papers:** Introduction → `\section{Study 1}` (Level 1) with `\subsection{Method}`, `\subsection{Results}`, `\subsection{Discussion}` (Level 2) → Study 2 … → `\section{General Discussion}`.

**Heading levels** (the class formats them; never style headings manually):

| LaTeX command | APA level | Appearance |
|---------------|-----------|------------|
| `\section{}` | Level 1 | Centered, bold, title case |
| `\subsection{}` | Level 2 | Flush left, bold, title case |
| `\subsubsection{}` | Level 3 | Flush left, bold italic, title case |
| `\paragraph{}` | Level 4 | Indented, bold, title case, ends with period, text runs in |
| `\subparagraph{}` | Level 5 | Indented, bold italic, title case, ends with period, text runs in |

- APA sections are not numbered. Give sections `\label{sec:...}` for internal bookkeeping but refer to them by name in prose ("see the Data Analysis section"), not by number.
- Do not skip levels. Do not use a heading for the introduction.

## Tables and Figures

APA 7 (§7.1–7.36): number (bold) and title (italic, title case) **above** the table or figure; notes **below**. The `apa7` class formats captions automatically; put `\caption{}` first.

```latex
\begin{table}[tbp]
\begin{threeparttable}
\caption{Means, Standard Deviations, and Correlations Among Study Variables}
\label{tab:descriptives}
\input{tables/descriptive/sumstats_correlations.tex}
\begin{tablenotes}[para, flushleft]
{\small
\textit{Note.} $N = 412$ students in 24 classrooms. Coefficient omega reliabilities
appear on the diagonal. Data are from the fall 2025 wave.
}
\end{tablenotes}
\end{threeparttable}
\end{table}
```

```latex
\begin{figure}[tbp]
\caption{Posttest Science Achievement by Condition and Prior Achievement}
\label{fig:interaction}
\includegraphics[width=\linewidth]{figures/fig2_condition_by_prior.pdf}
\figurenote{Error bars represent 95\% confidence intervals. Prior achievement is
grand-mean centered. Data are from the spring 2026 posttest.}
\end{figure}
```

- Generated `.tex` table files contain bare `tabular` only — no `\begin{table}`, `\caption`, or notes (INV-13).
- `booktabs` rules only (`\toprule`, `\midrule`, `\bottomrule`, `\cmidrule`) — never `\hline`, never vertical rules (INV-3).
- Notes in order: general note (*Note.*), specific notes (superscript lowercase letters), probability note (asterisks, only when used).
- Refer to every table and figure in the text by number before it appears: `\Cref{tab:descriptives}` → "Table 1".
- Wide tables: wrap in `landscape` (pdflscape) rather than shrinking below `\small`.

## Citations and References

- Narrative: `\textcite{smith2024}` → Smith (2024). Parenthetical: `\parencite{smith2024}` → (Smith, 2024). Multiple: `\parencite{a2020,b2021}` — biblatex-apa sorts them (`sortcites=true`).
- Page-specific: `\parencite[p.~12]{smith2024}`; direct quotations always carry a page or paragraph number.
- Do not hand-type "et al." or years — biblatex-apa applies the APA 7 rule (three or more authors → first author et al. from the first citation).
- `.bib` entries need DOIs (`doi = {10.xxxx/...}`, no `https://doi.org/` prefix) whenever one exists; titles in sentence case are produced by the style.
- References: `\printbibliography` after the Discussion. Do NOT shrink the font or switch to single spacing — APA manuscripts double-space references with hanging indents (the style does this).

## Compilation

```bash
# Preferred: latexmk handles pdfLaTeX + biber passes automatically
cd paper && latexmk main.tex

# Manual fallback:
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

`paper/latexmkrc` configures pdfLaTeX, TEXINPUTS, and BIBINPUTS. apa7 and biblatex-apa are developed and tested on pdfLaTeX; XeLaTeX/LuaLaTeX also work if you need system fonts. On Overleaf, set the compiler to pdfLaTeX via Menu > Compiler. Required TeX Live packages: `apa7`, `biblatex`, `biblatex-apa`, `biber`, `threeparttable`, `scalerel` (apa7 ORCID icon), `csquotes`, `babel-english`.

## What the Writer-Critic Checks

**Required (blocking deductions):**
- Not `apa7` class, or not `man` mode (-5)
- Loads `geometry`, `setspace`, `fancyhdr`, or `titlesec`, or calls `\doublespacing` manually (-3)
- Missing or over-long `\shorttitle{}` running head (> 50 characters) (-2)
- `\textbf{}` wrapping `\title{}` (-3)
- `\and` or `\thanks{}` for authors instead of `\authorsnames`/`\authorsaffiliations` (-3)
- Missing author note elements required for the target journal (ORCID, disclosures, correspondence) (-2)
- Missing keywords, or JEL codes present instead (INV-6) (-5)
- Abstract over 250 words or over the journal limit (INV-5) (-3)
- Introduction carries a heading, or Method/Results/Discussion headings missing (-3)
- Manual heading styling or skipped heading levels (-2)
- `natbib`, `apacite`, or `bibtex` instead of biblatex-apa + biber (INV-9) (-3)
- `\citet`/`\citep`/hand-typed citations instead of `\textcite`/`\parencite` (-1 per, max -5)
- `\hline` or vertical rules (INV-3) (-3)
- Missing table notes or figure notes (INV-1, INV-2) (-5 per, max -15)
- Caption placed below a table or figure (APA puts number and title above) (-2 per, max -6)
- Statistics not reported per APA (INV-4) (-2 per, max -10)
- Method section missing JARS elements (INV-23) (-5 per element, max -15)
- `hyperref` not loaded second-to-last, or loaded with options that clash (INV-10) (-2)
- Missing `cleveref` after `hyperref` (INV-10) (-2)
- Manual `Table~\ref{}` instead of `\Cref{}` (-1 per, max -5)
- Missing `microtype` (-2)
- Biased or imprecise language about people (INV-24) (-2 per, max -6)

**Recommended (advisory — reported but not deducted):**
- `floatsintext` matches the journal's float placement preference
- `mask` option on for masked-review journals
- DOIs present for every reference that has one
- `hidelinks` in `\hypersetup`
