# Pre-Submission Checklist

## Quality Gates
- [ ] Overall score >= 95
- [ ] All component scores >= 80
- [ ] Verifier pass (0 or 100)

## Manuscript
- [ ] Abstract <= 250 words or the journal limit (INV-5)
- [ ] 3–5 keywords present; public significance / impact statement prepared if the journal requires one (INV-6)
- [ ] All tables have notes (INV-1)
- [ ] All figures have notes (INV-2)
- [ ] No `\hline` -- booktabs only (INV-3)
- [ ] Notation consistent throughout (INV-7)
- [ ] Numbers in text match tables (INV-11)
- [ ] Compiles cleanly with no warnings
- [ ] biblatex-apa (`style=apa`) + `biber`, not `natbib`/`apacite` (INV-9)
- [ ] `hyperref` second-to-last, `cleveref` after (INV-10)
- [ ] No `Figure~\ref{}` -- use `\cref{}` throughout

## Replication Package
- [ ] README follows AEA template
- [ ] All scripts run from clean state
- [ ] Data dictionary included
- [ ] Computational requirements documented
- [ ] License specified
- [ ] Master script exists and runs end-to-end

## Submission Materials
- [ ] Cover letter drafted
- [ ] Target journal selected (from journal profiles)
- [ ] Formatting matches journal requirements
- [ ] Author information complete
- [ ] Statistics in APA form; asterisks only if the journal allows them (INV-4)
- [ ] Method meets JARS, incl. transparency statement (INV-23)
- [ ] `mask` option on and text free of self-identification (masked-review journals)
- [ ] Float placement matches the journal (`floatsintext` on or off)
