# Domain Profile

<!--
HOW TO USE: This profile is pre-filled for quantitative psychology and education research
(APA 7 manuscripts). Narrow it to your subfield (e.g., delete the education rows for a
social-psychology project) or let /discover (interactive interview) refine it.
All agents read this file to calibrate their field-specific behavior.
-->

## Field

**Primary:** Psychology and Education — quantitative empirical research (educational psychology, developmental, cognitive, social/personality, learning sciences, education policy and program evaluation)
**Adjacent subfields:** Quantitative psychology/psychometrics, prevention science, school psychology, economics of education, sociology of education, public health (child and adolescent development)

**Manuscript format:** APA 7 (`.claude/rules/working-paper-format.md`). **Reporting standard:** APA JARS-Quant (JARS-Qual / JARS-Mixed when applicable); CONSORT for randomized trials; PRISMA 2020 for systematic reviews and meta-analyses.

---

## Target Journals (ranked by tier)

<!-- The Orchestrator uses this for journal selection. The Librarian prioritizes these in searches.
     Profiles for most of these are in journal-profiles.md (Psychology and Education sections). -->

| Tier | Psychology | Education |
|------|-----------|-----------|
| Top general | Psychological Science; Nature Human Behaviour; Perspectives on Psychological Science; Psychological Bulletin, Psychological Review (reviews/theory) | American Educational Research Journal (AERJ); Educational Researcher; Review of Educational Research (reviews) |
| Top field | Journal of Personality and Social Psychology; Journal of Experimental Psychology: General; Developmental Psychology; Child Development; Psychological Methods (methods) | Journal of Educational Psychology; Educational Evaluation and Policy Analysis (EEPA); Journal of Research on Educational Effectiveness (JREE); Sociology of Education |
| Strong field | Developmental Science; Journal of Experimental Child Psychology; Personality and Social Psychology Bulletin; Advances in Methods and Practices in Psychological Science (AMPPS); Collabra: Psychology | Contemporary Educational Psychology; Learning and Instruction; Educational Psychologist (reviews/theory); AERA Open; Journal of Policy Analysis and Management (education policy) |
| Specialty | Journal of Applied Developmental Psychology; Cognitive Research: Principles and Implications; Behavior Research Methods; Multivariate Behavioral Research; Structural Equation Modeling | Early Childhood Research Quarterly; Journal of School Psychology; Journal of Teacher Education; Reading Research Quarterly; Journal for Research in Mathematics Education; Educational and Psychological Measurement; Journal of Educational Measurement |

---

## Common Data Sources

<!-- The Explorer prioritizes these. The explorer-critic knows their quirks. -->

| Dataset | Type | Access | Notes |
|---------|------|--------|-------|
| ECLS-K:2011 / ECLS-B (NCES) | Longitudinal child cohort | Public-use + restricted license | Nationally representative K–5 cohort; direct assessments + parent/teacher reports; use sampling weights and design variables; IRT theta scores vs. scale scores differ across waves |
| ELS:2002 / HSLS:09 (NCES) | Longitudinal secondary cohort | Public-use + restricted | High school to postsecondary transitions; school-level clustering; nonresponse adjustments required |
| NAEP | Repeated cross-section assessment | Restricted (secure data) / NAEP Data Explorer | Plausible values — never average them; analyze each and combine (Rubin's rules); jackknife replicate weights |
| PISA / TIMSS / PIRLS | International assessments | Public | Plausible values + replicate weights; cross-national measurement invariance is a live concern |
| State longitudinal data systems (SLDS) | Administrative student/teacher records | Restricted (data-use agreement) | Population coverage; test-score scale changes across years and states; FERPA constraints; small-cell suppression |
| Add Health | Longitudinal adolescent cohort | Public-use + restricted | School-based sampling; network data; complex survey design |
| NLSY79 Child and Young Adult / NLSY97 | Longitudinal panel | Public | Long follow-up; sibling designs possible; assessment changes with age |
| PSID Child Development Supplement | Longitudinal family panel | Public + restricted | Time diaries; intergenerational links |
| ABCD Study | Longitudinal neurodevelopment cohort | Controlled access (NDA) | ~11,800 youth; imaging + cognition; site clustering and family nesting |
| NICHD SECCYD | Longitudinal child cohort | Controlled access (ICPSR) | Child-care quality and development; birth to 15 years |
| MIDUS / HRS | Adult panels | Public | Well-being, aging, cognition; biomarker subsamples |
| ManyLabs / Psychological Science Accelerator / OSF repositories | Multi-site replications, open data | Public | Large-N heterogeneity estimates; check codebooks for site-level exclusions |
| Online panels (Prolific, CloudResearch/MTurk) | Primary data collection | Paid | Attention checks, bot/duplicate screening, non-naiveté; preregister exclusion rules |
| What Works Clearinghouse (WWC) study reviews | Evidence syntheses | Public | Effect sizes and ratings by intervention; useful for priors and power analysis |

---

## Common Identification Strategies

<!-- The Strategist considers these first. The strategist-critic knows field-specific threats. -->

| Strategy | Typical Application | Key Assumption to Defend |
|----------|-------------------|------------------------|
| Between-subjects lab/online experiment | Manipulations of instruction, feedback, framing, stereotype threat | Successful randomization; manipulation works (manipulation check) and isolates the construct; no demand characteristics; preregistered exclusions |
| Within-subjects / factorial / crossover experiment | Cognitive and learning tasks | No carryover; counterbalancing; correct error terms (participants and items as random effects) |
| Individually randomized field trial | Tutoring, mindset, mentoring interventions | Randomization integrity; low/non-differential attrition (WWC standards); ITT analysis; business-as-usual control described |
| Cluster-randomized trial (classrooms/schools) | Curriculum, professional development, school-wide programs | Randomization at the cluster level; analysis at the level of assignment (multilevel); adequate number of clusters (MDES with ICC); no joiner bias |
| Regression discontinuity on test-score or age cutoffs | Gifted placement, remediation, grade retention, school-entry age | No manipulation of the running variable (density test); continuity of covariates; bandwidth sensitivity; local estimand |
| Comparative interrupted time series / DiD | District or state policy changes, program rollouts | Parallel pre-trends between adopting and comparison units; no coincident shocks; staggered-adoption estimators when timing varies |
| Admission lotteries | Charter schools, magnet schools, voucher programs | Lottery integrity; lottery-cohort fixed effects; differential attrition; compliance (ITT vs. TOT/CACE) |
| Matching / propensity score / weighting | Program participation without randomization | Selection on observables incl. pretest; WWC baseline equivalence (|g| ≤ 0.25, adjust if > 0.05); sensitivity to unobserved confounding |
| Longitudinal panel models (RI-CLPM, growth curves, within-person fixed effects) | Reciprocal relations (motivation ↔ achievement), developmental trajectories | Separation of within- from between-person variance; correct lag; time-invariant confounding only (for FE); measurement invariance across waves — associational unless a design adds identification |
| Mediation and moderation | Mechanisms of interventions; for whom effects hold | Sequential ignorability for causal mediation; temporal ordering of X, M, Y; moderators measured pre-treatment; probing (simple slopes / Johnson–Neyman) |
| Psychometric / measurement studies (CFA, IRT, invariance) | Scale development and validation | Model fit; invariance (configural → metric → scalar) before group comparisons; validity evidence per the *Standards for Educational and Psychological Testing* |
| Meta-analysis | Evidence synthesis | Random-effects model; dependent effect sizes (RVE / multilevel); heterogeneity (τ, prediction intervals); publication bias (selection models, PET-PEESE, funnel asymmetry) |

---

## Field Conventions

<!-- The Coder and Writer follow these. The writer-critic checks for them. -->

- APA 7 statistical reporting: exact *p* values, effect sizes with 95% CIs for every primary result (INV-4)
- Preregistration (OSF, AsPredicted) for confirmatory hypotheses; Registered Reports where available; report deviations explicitly
- A priori power analysis or sample-size justification (Lakens, 2022); for nested designs, MDES with ICCs (e.g., PowerUp!, Optimal Design) using empirical ICC benchmarks (Hedges & Hedberg, 2007)
- Nested data (students in classrooms in schools; trials in participants) → multilevel models or cluster-robust SEs at the level of assignment; report ICCs
- Crossed random effects for participants and items in experimental psycholinguistic/cognitive tasks
- Reliability in the current sample; prefer McDonald's ω over Cronbach's α when tau-equivalence is doubtful (McNeish, 2018)
- Test measurement invariance before comparing latent means or relations across groups or waves
- Missing data: FIML or multiple imputation under MAR, with auxiliary variables; listwise deletion only with justification; report attrition overall and by condition
- Education effect sizes interpreted against empirical benchmarks for interventions (Kraft, 2020), not Cohen's (1988) small/medium/large alone; standardize on the population SD and say which SD
- Researcher-developed outcome measures inflate effects relative to standardized tests (Cheung & Slavin, 2016) — report both when possible
- Multiple-comparison control (Holm, Benjamini–Hochberg) for families of confirmatory tests; label exploratory analyses
- Claims of "no effect" require equivalence tests (TOST), Bayes factors, or CI-based arguments
- Open science: data, materials, and code shared (or a stated reason not to); TOP Guidelines and journal badges
- Bias-free language and specific demographic reporting (APA 7 Chapter 5; INV-24)

---

## Notation Conventions

<!-- The Writer and writer-critic enforce these. Full protocol: .claude/skills/write/references/notation-protocol.md -->

| Symbol | Meaning | Anti-pattern |
|--------|---------|-------------|
| $Y_{ij}$ | Outcome for person $i$ in cluster $j$ (add $t$ for occasion: $Y_{tij}$) | Don't drop the cluster subscript in multilevel models |
| $\gamma_{00}, \gamma_{10}$ | Fixed effects (Raudenbush & Bryk notation) | Don't mix with $\beta$ for the same parameter across sections |
| $u_{0j}$, $\tau_{00}$; $r_{ij}$, $\sigma^2$ | Random effect and its variance; level-1 residual and its variance | Don't call random-effect variances "standard errors" |
| $\rho$ (ICC) | Intraclass correlation $\tau_{00} / (\tau_{00} + \sigma^2)$ | Don't use $r$ for the ICC |
| $\eta$, $\lambda$, $\omega$ | Latent factor, loading, omega reliability | Don't use $\alpha$ for reliability without saying "Cronbach's" |
| $a$, $b$, $c'$, $ab$ | Mediation paths and indirect effect | Don't report $ab$ without a bootstrap or Monte Carlo CI |
| $d$, $g$ | Cohen's *d*, Hedges' *g* (state the standardizer) | Don't report *d* without saying which SD |
| $Y_i(1), Y_i(0)$ | Potential outcomes under treatment/control | Don't use causal notation for correlational designs |

---

## Seminal References

<!-- The Librarian ensures these are cited when relevant. The strategist-critic knows their methods. -->

| Paper | Why It Matters |
|-------|---------------|
| Shadish, Cook, & Campbell (2002) | Experimental and quasi-experimental designs; validity typology (internal, external, construct, statistical conclusion) |
| Cronbach & Meehl (1955) | Construct validity |
| AERA, APA, & NCME (2014), *Standards for Educational and Psychological Testing* | Sources of validity evidence; fairness in testing |
| Appelbaum et al. (2018) | JARS-Quant — what an APA Method/Results section must report |
| Simmons, Nelson, & Simonsohn (2011) | Researcher degrees of freedom; motivates preregistration |
| Open Science Collaboration (2015) | Reproducibility Project: Psychology — replication rates |
| Cohen (1988) | Statistical power analysis and effect size conventions |
| Lakens (2022) | Sample size justification |
| Raudenbush & Bryk (2002) | Hierarchical linear models |
| Hedges & Hedberg (2007) | Empirical ICCs for planning cluster-randomized trials in education |
| Kraft (2020) | Interpreting effect sizes of education interventions |
| Cheung & Slavin (2016) | Methodological features (sample size, researcher-made measures) inflate education effect sizes |
| Hamaker, Kuiper, & Grasman (2015) | Critique of the cross-lagged panel model; RI-CLPM |
| Imai, Keele, & Tingley (2010) | Causal mediation analysis and sequential ignorability |
| Rohrer (2018) | Causal inference with observational data in psychology |
| Flake & Fried (2020) | Questionable measurement practices |
| McNeish (2018) | Alternatives to coefficient alpha |
| Henrich, Heine, & Norenzayan (2010) | WEIRD samples and generalizability |
| What Works Clearinghouse (2022), *Procedures and Standards Handbook* (v5.0) | Attrition, baseline equivalence, and evidence tiers for education studies |

---

## Theoretical Foundational References

<!-- The Theorist and theorist-critic default to these anchors when building or reviewing a theory section.
     Only needed if the paper has a formal methods/theory section. -->

| Topic | Anchor references |
|-------|------------------|
| Classical and modern test theory | Lord & Novick (1968); McDonald (1999); Embretson & Reise (2000) |
| Structural equation modeling | Bollen (1989); Kline (2023) |
| Measurement invariance | Meredith (1993); Putnick & Bornstein (2016) |
| Multilevel modeling | Raudenbush & Bryk (2002); Snijders & Bosker (2012) |
| Causal inference / potential outcomes | Rubin (1974); Holland (1986); Imbens & Rubin (2015) |
| Causal mediation | Imai, Keele, & Tingley (2010); VanderWeele (2015) |
| Missing data | Little & Rubin (2019); Enders (2022) |
| Meta-analysis | Borenstein et al. (2009); Hedges, Tipton, & Johnson (2010) (robust variance estimation) |
| Bayesian inference | Gelman et al. (2013); Kruschke (2015) |

---

## Paper Author Team

<!-- Used by the theorist-critic and strategist-critic to calibrate respect. If the authors are themselves
     among the reference literature on a topic, critics avoid lecturing them on their own contributions.
     List author surnames + the topics they are foundational on. -->

| Author | Foundational on |
|--------|----------------|
| [Surname] | [Topic] |

---

## Field-Specific Referee Concerns

<!-- The domain-referee and methods-referee watch for these. -->

- **Power and sample size** — "Was the study powered for the effect you report, or for a realistic one?" Small samples with large effects invite skepticism
- **Researcher degrees of freedom** — undisclosed flexibility in exclusions, covariates, outcomes, or stopping rules; deviations from preregistration
- **Measurement validity** — Does the instrument measure the construct? Reliability in this sample? Measurement invariance across groups/waves before comparisons?
- **Common-method variance** — all constructs self-reported by the same informant at one time point
- **Causal language from correlational designs** — "predicts" ≠ "causes"; cross-sectional mediation is not a mechanism
- **Nesting ignored** — students treated as independent when assignment was by classroom or school
- **Attrition** — overall and differential attrition against WWC thresholds; who left and why
- **Control condition** — What did the business-as-usual group receive? Active vs. passive control; expectancy effects
- **Implementation fidelity and dosage** — Was the intervention delivered as designed? Treatment contrast?
- **Effect-size interpretation** — benchmarks for education interventions (Kraft, 2020); researcher-made vs. standardized outcomes; practical significance
- **Generalizability (WEIRD samples)** — convenience samples, single sites, online panels; constraints-on-generality statement
- **Manipulation checks and demand characteristics** in experiments; attention checks and bot screening in online samples
- **Replication** — single-study findings with *p* just under .05; is there a direct or conceptual replication?
- **Floor/ceiling effects and regression to the mean** — especially when selecting on low pretest scores
- **Equity and heterogeneity** — Do effects differ by student subgroup? Are subgroup analyses preregistered and adequately powered?

---

## Quality Tolerance Thresholds

<!-- Customize for your domain's standards. Used by quality.md. -->

| Quantity | Tolerance | Rationale |
|----------|-----------|-----------|
| Point estimates (replication) | 1e-6 | Numerical precision across reruns |
| Standard errors | 1e-4 | Optimizer / bootstrap variability |
| Bootstrap CIs (indirect effects) | ± 0.01 at ≥ 5,000 resamples | Monte Carlo error |
| Reported statistics vs. output | Exact at reported precision | INV-11; *p* to three decimals, other statistics to two |
| Fit indices (CFI, TLI, RMSEA, SRMR) | ± 0.001 | Estimator / software defaults |
| Multiple-imputation estimates | ± 0.01 with *m* ≥ 20 imputations | Between-imputation variability |
| Coverage rates (simulation studies) | ± 0.01 | Simulation with B reps |
