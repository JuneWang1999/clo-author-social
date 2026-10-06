# ==============================================================================
# build_manuscript.R -- Build the APA 7 Word manuscript from the drafts
# ==============================================================================
# Usage (from the project root):
#   Rscript paper/build_manuscript.R            # -> paper/drafts/manuscript_draft.docx
#   Rscript paper/build_manuscript.R --handoff  # -> paper/manuscript.docx (MASTER)
#
# Draft builds overwrite only paper/drafts/manuscript_draft.docx.
# --handoff creates the master copy once. It refuses to run if
# paper/manuscript.docx already exists: after handoff the Word file is the
# source of truth and is never overwritten by the pipeline.
#
# Inputs: paper/manuscript.Rmd, paper/sections/*.md, paper/displays.csv,
#         paper/tables/*.rds, paper/figures/*.png, Bibliography_base.bib
# Requires: rmarkdown, knitr, flextable, officer; pandoc on PATH
# ==============================================================================

library(rmarkdown)
library(officer)

args <- commandArgs(trailingOnly = FALSE)
script <- sub("^--file=", "", args[grep("^--file=", args)])
paper_dir <- if (length(script)) dirname(normalizePath(script)) else normalizePath("paper")
handoff <- "--handoff" %in% commandArgs(trailingOnly = TRUE)

master <- file.path(paper_dir, "manuscript.docx")
drafts_dir <- file.path(paper_dir, "drafts")
draft <- file.path(drafts_dir, "manuscript_draft.docx")

if (handoff && file.exists(master)) {
  stop("paper/manuscript.docx already exists -- it is the master copy and will not be ",
       "overwritten. Rename or move it yourself if you really want a fresh handoff.",
       call. = FALSE)
}

dir.create(drafts_dir, showWarnings = FALSE)
rmarkdown::render(
  input = file.path(paper_dir, "manuscript.Rmd"),
  output_file = basename(draft),
  output_dir = drafts_dir,
  knit_root_dir = paper_dir,
  intermediates_dir = tempdir(),
  quiet = TRUE
)

# Running head: replace the header placeholder with the short title (all caps)
meta <- rmarkdown::yaml_front_matter(file.path(paper_dir, "manuscript.Rmd"))
shorttitle <- toupper(meta$params$shorttitle %||% "")
if (nzchar(shorttitle) && !grepl("^\\[", shorttitle)) {
  if (nchar(shorttitle) > 50) warning("Running head exceeds 50 characters (APA 7).", call. = FALSE)
  doc <- officer::read_docx(draft)
  doc <- officer::headers_replace_all_text(doc, "RUNNING HEAD", shorttitle, fixed = TRUE)
  print(doc, target = draft)
}

if (handoff) {
  file.copy(draft, master, overwrite = FALSE)
  message("Master copy created: paper/manuscript.docx -- edit it in Word from now on.")
} else {
  message("Draft built: paper/drafts/manuscript_draft.docx")
}
