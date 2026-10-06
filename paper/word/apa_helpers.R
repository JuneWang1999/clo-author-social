# ==============================================================================
# apa_helpers.R -- APA 7 tables, numbers, and display blocks for Word output
# ==============================================================================
# Used by analysis scripts (to build and save tables) and by
# paper/manuscript.Rmd (to place tables and figures in the Word manuscript).
#
#   source(here::here("paper", "word", "apa_helpers.R"))   # in analysis scripts
#
# Requires: flextable, officer
# ==============================================================================

# ---- Tables -------------------------------------------------------------------

#' Apply APA 7 table styling to a data frame or flextable.
#' Horizontal rules only: above and below the column heads and below the body.
#' The table carries NO number, title, or note -- those are added by the
#' manuscript (INV-1, INV-13).
apa_flextable <- function(x, font = "Times New Roman", size = 12,
                          first_col_align = "left") {
  stopifnot(is.data.frame(x) || inherits(x, "flextable"))
  ft <- if (inherits(x, "flextable")) x else flextable::flextable(x)
  rule <- officer::fp_border(color = "black", width = 1)
  ft <- flextable::border_remove(ft)
  ft <- flextable::hline_top(ft, border = rule, part = "header")
  ft <- flextable::hline_bottom(ft, border = rule, part = "header")
  ft <- flextable::hline_bottom(ft, border = rule, part = "body")
  ft <- flextable::font(ft, fontname = font, part = "all")
  ft <- flextable::fontsize(ft, size = size, part = "all")
  ft <- flextable::align(ft, align = "center", part = "all")
  ft <- flextable::align(ft, j = 1, align = first_col_align, part = "all")
  ft <- flextable::line_spacing(ft, space = 1, part = "all")
  # Side padding 0: flextable writes padding as paragraph indents, which pandoc
  # reads as block quotes. Column spacing comes from the widths below instead.
  ft <- flextable::padding(ft, padding.top = 2, padding.bottom = 2,
                           padding.left = 0, padding.right = 0, part = "all")
  # Fixed layout with computed widths: "autofit" layout writes no column grid,
  # and pandoc (snapshots, revised copies) silently drops grid-less tables.
  ft <- flextable::set_table_properties(ft, layout = "fixed")
  ft <- flextable::autofit(ft, add_w = 0, add_h = 0)
  flextable::width(ft, width = flextable::dim_pretty(ft)$widths + 0.2)
}

#' Add a spanner row above the column heads, e.g.
#' apa_spanner(ft, c("", "Treatment", "Comparison"), c(1, 2, 2))
apa_spanner <- function(ft, labels, widths) {
  stopifnot(inherits(ft, "flextable"), length(labels) == length(widths))
  rule <- officer::fp_border(color = "black", width = 1)
  ft <- flextable::add_header_row(ft, values = labels, colwidths = widths)
  ft <- apa_flextable(ft)
  starts <- cumsum(c(1, utils::head(widths, -1)))
  for (k in seq_along(labels)) {
    if (nzchar(labels[k])) {
      cols <- starts[k]:(starts[k] + widths[k] - 1)
      ft <- flextable::hline(ft, i = 1, j = cols, border = rule, part = "header")
    }
  }
  ft
}

#' Save a table for the manuscript: <dir>/<name>.rds (used by the build) and
#' <dir>/<name>.docx (preview you can open in Word).
apa_save_table <- function(ft, name, dir = file.path("paper", "tables")) {
  stopifnot(inherits(ft, "flextable"), nzchar(name))
  dir.create(dir, recursive = TRUE, showWarnings = FALSE)
  saveRDS(ft, file.path(dir, paste0(name, ".rds")))
  flextable::save_as_docx(ft, path = file.path(dir, paste0(name, ".docx")))
  invisible(file.path(dir, paste0(name, ".rds")))
}

# ---- Numbers (INV-4) ------------------------------------------------------------

#' Format numbers APA-style. leading_zero = FALSE for statistics that cannot
#' exceed 1 (p, r, R^2, alpha, omega, proportions).
apa_num <- function(x, digits = 2, leading_zero = TRUE) {
  out <- formatC(x, format = "f", digits = digits)
  if (!leading_zero) out <- sub("^(-?)0\\.", "\\1.", out)
  out[is.na(x)] <- ""
  out
}

#' Exact p values: ".031", "< .001"; never ".000".
apa_p <- function(p, digits = 3) {
  stopifnot(all(is.na(p) | (p >= 0 & p <= 1)))
  out <- ifelse(p < 0.001, "< .001", apa_num(p, digits, leading_zero = FALSE))
  out[is.na(p)] <- ""
  out
}

#' Confidence interval in brackets: "[0.12, 0.45]".
apa_ci <- function(lower, upper, digits = 2, leading_zero = TRUE) {
  sprintf("[%s, %s]", apa_num(lower, digits, leading_zero),
          apa_num(upper, digits, leading_zero))
}

# ---- Manuscript display blocks (used by paper/manuscript.Rmd) -------------------

.apa_div <- function(style, text) {
  cat(sprintf('\n::: {custom-style="%s"}\n%s\n:::\n\n', style, text))
}

#' Write every table and figure listed in the manifest (displays.csv), each on
#' its own page after the references, in APA format: bold number, italic title,
#' the table or image, then the note. Call inside a chunk with results = "asis".
apa_displays <- function(manifest = "displays.csv", fig_width = "6.5in") {
  if (!file.exists(manifest)) return(invisible(NULL))
  d <- utils::read.csv(manifest, stringsAsFactors = FALSE, na.strings = "")
  stopifnot(all(c("type", "number", "file", "title", "note") %in% names(d)))
  d <- d[order(match(d$type, c("table", "figure")), d$number), ]
  for (k in seq_len(nrow(d))) {
    row <- d[k, ]
    is_table <- row$type == "table"
    label <- if (is_table) "Table" else "Figure"
    .apa_div(paste(label, "Number"), sprintf("%s %d", label, row$number))
    .apa_div(paste(label, "Title"), row$title)
    if (!file.exists(row$file)) {
      .apa_div("Body Text", sprintf("**[Missing file: %s]**", row$file))
    } else if (is_table) {
      # .rds = flextable from R; .csv = pre-formatted table from Python/Julia
      ft <- if (grepl("\\.csv$", row$file, ignore.case = TRUE)) {
        apa_flextable(utils::read.csv(row$file, check.names = FALSE,
                                      colClasses = "character", na.strings = character(0)))
      } else {
        readRDS(row$file)
      }
      flextable::flextable_to_rmd(ft)
    } else {
      # absolute path: pandoc runs from a temporary directory
      .apa_div("Figure", sprintf("![](%s){width=%s}", normalizePath(row$file), fig_width))
    }
    if (!is.na(row$note) && nzchar(row$note)) {
      .apa_div(paste(label, "Note"), paste0("*Note.* ", row$note))
    }
  }
  invisible(d)
}

#' Insert one Markdown section file (paper/sections/<name>.md) verbatim.
apa_section <- function(name, dir = "sections") {
  f <- file.path(dir, paste0(name, ".md"))
  if (!file.exists(f)) {
    cat(sprintf("\n**[Section not drafted yet: %s]**\n\n", f))
    return(invisible(NULL))
  }
  cat(readLines(f, warn = FALSE, encoding = "UTF-8"), sep = "\n")
  cat("\n\n")
}

#' Hard page break in the Word output.
apa_page_break <- function() {
  cat('\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n')
}
