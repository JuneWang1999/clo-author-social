# Talk Skill -- Gotchas

Known failure points and edge cases for presentation creation.

- Notation in talks must match the paper exactly (INV-20). Different subscripts or variable names will confuse the audience.
- Every claim on a slide must appear in the manuscript (INV-21). No orphan results.
- pandoc moves any text that follows an image onto a new slide. Use the two-column block (`:::::: {.columns}`) for figure + interpretation.
- Don't style slides in the Markdown (colors, fonts). Everything visual comes from `paper/talks/reference.pptx`; restyle there.
- Once the user edits `paper/talks/<name>.pptx`, rebuilding from Markdown would destroy their work. The build script refuses `--handoff` over an existing deck; never work around it.
- The job market talk is the most important format. Allocate time for iteration.
- Talk scoring is advisory (non-blocking) -- a low score won't stop the pipeline, but it should prompt revision.
- Images are looked up in `paper/talks/`, `paper/figures/`, and `paper/`. A missing image becomes a placeholder description, not an error — check the build output for `Could not fetch resource`.
- The default `reference.pptx` is 16:9. For 4:3 venues, change the slide size in the reference deck (Design › Slide Size), not in the Markdown.
