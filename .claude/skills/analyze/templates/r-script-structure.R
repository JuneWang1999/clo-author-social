# ==============================================================================
# [NN]_[script_name].R
# [Purpose: one sentence]
# Project: [Project Name]
# Paper: [Author (Year)], Section [X]
# Inputs: [data/cleaned/analysis_sample.rds]
# Outputs: [paper/tables/reg_main.rds (+ .docx preview), paper/figures/fig1_main.png]
# ==============================================================================

# --- Packages ----------------------------------------------------------------
library(here)
library(data.table)
library(fixest)
library(modelsummary)
library(flextable)
library(ggplot2)
# [add project-specific packages]

# --- Seed --------------------------------------------------------------------
# Single seed per script. SEED defined in 01_setup.R; override here only if
# this script needs an independent stream (document why).
set.seed(12345L)

# --- Paths -------------------------------------------------------------------
# All paths relative via here(). No setwd(), no absolute paths.
dir.create(here("paper", "tables"), recursive = TRUE, showWarnings = FALSE)
dir.create(here("paper", "figures"), recursive = TRUE, showWarnings = FALSE)
source(here("paper", "word", "apa_helpers.R"))   # apa_flextable(), apa_save_table(), apa_p(), ...

# --- Paper-to-Code Naming Map -----------------------------------------------
# (Include in 01_setup.R; reference here for quick lookup)
# Paper Symbol       | Code Name        | Description
# $Y_{it}$           | outcome          | [outcome variable]
# $D_{it}$           | treatment        | [treatment indicator]
# $X_{it}$           | controls         | [control vector]
# $\hat{\beta}$      | beta_hat         | [main coefficient]

# --- Data --------------------------------------------------------------------
df <- readRDS(here("data", "cleaned", "analysis_data.rds"))

# Document dimensions
message("Observations: ", nrow(df))
message("Variables: ", ncol(df))

# --- Analysis ----------------------------------------------------------------
# [Main analysis code here]
# Use fixest::feols() for panel regressions
# Use modelsummary(output = "data.frame") / broom::tidy() to get estimates
# Use ggplot2 for figures

# --- Save Intermediate Objects -----------------------------------------------
# saveRDS() for ALL computed objects (models, data frames, statistics)
# saveRDS(model_fit, here("scripts", "R", "output", "model_fit.rds"))
# saveRDS(main_results, here("scripts", "R", "output", "main_results.rds"))

# --- Export Tables -----------------------------------------------------------
# APA flextable, no number/title/note -- INV-13 (those go in paper/displays.csv)
# ft <- apa_flextable(tab_df)
# apa_save_table(ft, "reg_main", dir = here("paper", "tables"))

# --- Export Figures ----------------------------------------------------------
# No titles inside ggplot -- INV-12. Titles go in paper/displays.csv
# ggsave(here("paper", "figures", "fig1_main.png"), width = 6.5, height = 4.5, dpi = 300, bg = "white")

message("Script complete: [NN]_[script_name].R")
