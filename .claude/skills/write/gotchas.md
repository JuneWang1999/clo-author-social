# Write Skill -- Gotchas

Known failure points and edge cases for paper drafting.

- Writer produces generic academic voice if `personal-style-guide.md` hasn't been extracted first. Run `/write style-guide` before drafting.
- Writer will draft results from strategy memo predictions if tables don't exist yet -- the hard gate catches this, but watch for it in partial drafts.
- Citation commands are biblatex-apa's `\textcite` ("Author (Year)" in prose) and `\parencite` ("(Author, Year)"). The writer slips into economics habits (`\citet`/`\citep`) — the writer-critic deducts for them.
- Writer sometimes invents citation keys not in `Bibliography_base.bib`. Always verify generated `\cite{}` keys against the actual bib file.
- The cleanup pass catches AI patterns but can over-correct domain-specific hedging that's actually appropriate (e.g., "may" in describing potential mechanisms is fine).
- Section ordering varies by paper type. Don't force reduced-form structure on structural papers.
- Abstract word count (250 max per INV-5, or the journal's stricter limit) is a hard constraint -- check the journal profile; some APA-style journals cap at 150--200 words.
- The writer tends to add an "Introduction" heading out of habit. APA introductions have no heading; `\maketitle` repeats the title instead.
- Method sections drift toward econometrics prose and skip JARS items (power analysis, reliability in this sample, exclusions, transparency statement). Check INV-23 before presenting.
- Leading zeros: *r* = .45 and *p* = .031, but *d* = 0.45 and *b* = 0.21 (those can exceed 1).
- Cross-sectional mediation written as "X affects Y through M" violates INV-8 -- describe indirect associations instead.
