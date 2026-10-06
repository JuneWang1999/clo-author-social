# Verifier Submission-Mode Audit: 10 Checks

The verifier runs in two modes. Standard mode (checks 1-4) runs between phase transitions. Submission mode (checks 1-10) runs before journal submission. All checks are pass/fail.

## Standard Checks (Always Run)

### 1. Manuscript Format (Word)
- `python3 .claude/scripts/check_docx_format.py paper/manuscript.docx --abstract-limit <journal limit>` reports no FAIL
- Every in-text citation has a reference entry and vice versa (read the snapshot)
- No unresolved comments or pending tracked changes in the file to be submitted (report; the user resolves them)
- A PDF export from Word (File › Save As › PDF) opens and shows every table and figure, if the journal wants a PDF too

### 2. Script Execution
- All scripts run without errors
- Output files created
- File sizes > 0

### 3. File Integrity
- Every `\input{}` and `\include{}` resolves to an existing file
- Every referenced table in `paper/tables/` exists
- Every referenced figure in `paper/figures/` exists

### 4. Output Freshness
- Output file timestamps match latest script run
- No stale outputs (generated before latest code change)

## Submission Checks (Additional)

### 5. Package Inventory
- All scripts present and numbered sequentially
- Master script exists (runs everything in order)
- No orphan scripts (scripts not called by master)

### 6. Dependency Verification
- R: `renv.lock` or `sessionInfo()` output exists
- Python: `requirements.txt` or `pyproject.toml` exists
- Non-standard packages documented with install instructions

### 7. Data Provenance
- Every dataset has a documented source
- Access instructions for restricted data
- No hardcoded paths
- Data availability statement present

### 8. Execution Verification
- Run master script end-to-end
- Capture all output and errors
- Report runtime

### 9. Output Cross-Reference
- Every table and figure in the paper traced to a specific script
- No orphan outputs (generated but not referenced)
- No missing outputs (referenced but not generated)

### 10. README Completeness (AEA Format)
- Data availability statement
- Computational requirements (software, packages, hardware, runtime)
- Description of programs (numbered, with inputs/outputs)
- Instructions for replication
- List of tables and figures with generating scripts

## Content Invariants Checked

The verifier also enforces these invariants (any violation is FAIL):
- INV-9: references from Zotero/.bib via APA CSL or the Zotero plugin; citations and reference list match
- INV-10: tables/figures numbered in order of first mention and all called out
- INV-25: the pipeline never modified `paper/manuscript.docx`
- INV-14: `set.seed()` exactly once at top if stochastic
- INV-15: All packages loaded at top
- INV-16: No absolute paths
- INV-19: No prohibited functions (`setwd()`, `rm(list = ls())`, `install.packages()`, `attach()`)

## Scoring

Pass/fail per check. Binary for aggregation: 0 (any failure) or 100 (all pass). Contributes 5% to weighted overall score.
