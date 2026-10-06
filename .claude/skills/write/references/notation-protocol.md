# Notation Protocol -- Standard Conventions (Potential Outcomes, Multilevel, Latent Variable)

Notation conventions for consistency across all sections of the paper.

---

## Core Variables

| Symbol | Meaning | Usage |
|--------|---------|-------|
| $Y_{it}$ | Outcome variable | Unit $i$, time $t$ |
| $D_{it}$ | Treatment indicator | Binary or continuous treatment |
| $X_{it}$ | Control variables | Covariate vector |
| $\gamma_i$ | Unit fixed effect | Absorbs time-invariant unit heterogeneity |
| $\delta_t$ | Time fixed effect | Absorbs common time shocks |
| $\varepsilon_{it}$ | Error term | Idiosyncratic shock |

---

## Rules

- **Consistent throughout** -- the same symbol never means two things across sections
- **Define every symbol at first use** -- no implicit notation
- **Match the strategy memo** -- if the coder's naming map uses specific notation, the paper must match
- **Subscripts matter** -- $i$ for units, $t$ for time, $g$ for groups, $j$ for secondary units (firms, markets)
- **Hats for estimates** -- $\hat{\beta}$ for estimated coefficients, $\beta$ for population parameters
- **Bold for vectors/matrices** -- $\mathbf{X}$ for the control matrix, $X_{it}$ for a single observation's controls

---

## Common Estimands

| Estimand | Symbol | Definition |
|----------|--------|------------|
| Average Treatment Effect | $\text{ATE}$ | $E[Y_i(1) - Y_i(0)]$ |
| Average Treatment Effect on the Treated | $\text{ATT}$ | $E[Y_i(1) - Y_i(0) \mid D_i = 1]$ |
| Local Average Treatment Effect | $\text{LATE}$ | $E[Y_i(1) - Y_i(0) \mid \text{compliers}]$ |
| Group-time ATT | $\text{ATT}(g,t)$ | Callaway-Sant'Anna notation |

---

## Multilevel Models (students $i$ in classrooms/schools $j$)

Raudenbush & Bryk (2002) notation; use the level-specific form or the combined form, not both inconsistently.

| Symbol | Meaning |
|--------|---------|
| $Y_{ij}$ | Outcome for student $i$ in cluster $j$ |
| $\beta_{0j}$, $\beta_{1j}$ | Level-1 intercept and slope for cluster $j$ |
| $\gamma_{00}$, $\gamma_{01}$, $\gamma_{10}$ | Fixed effects (grand intercept, level-2 predictor, level-1 slope) |
| $u_{0j}$, $u_{1j}$ | Level-2 random effects, variances $\tau_{00}$, $\tau_{11}$ |
| $r_{ij}$ | Level-1 residual, variance $\sigma^2$ |
| $\rho = \tau_{00} / (\tau_{00} + \sigma^2)$ | Intraclass correlation (ICC) |

- State centering for every level-1 predictor (grand-mean vs. cluster-mean) at first use.
- Three-level models add $k$ (students $i$ in classrooms $j$ in schools $k$).

## Latent Variable / SEM

| Symbol | Meaning |
|--------|---------|
| $\eta$ | Latent factor (endogenous); $\xi$ for exogenous factors when the distinction matters |
| $\lambda$ | Factor loading; $\tau$ item intercept; $\theta$ residual variance |
| $\omega$ | McDonald's omega reliability |
| $a$, $b$, $c'$, $ab$ | Mediation paths: X→M, M→Y, direct effect, indirect effect |

## Effect Sizes

| Symbol | Meaning |
|--------|---------|
| $d$ | Cohen's *d* (state which SD standardizes it) |
| $g$ | Hedges' *g* (small-sample corrected) |
| $\eta^2_p$, $\omega^2$ | Partial eta squared, omega squared |
| $r$, $R^2$ | Correlation, variance explained (marginal/conditional $R^2$ for multilevel models) |

In APA prose, statistical symbols are italicized (*M*, *SD*, *t*, *p*, *d*, *r*); Greek letters are not.
