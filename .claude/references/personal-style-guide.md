# Personal Style Guide — MODEL VOICE

<!--
HOW TO USE: The writer agent auto-loads this file and calibrates drafting to it.

THIS IS A MODEL VOICE, NOT THE USER'S OWN VOICE. It was extracted from three
published papers by other researchers in the user's field (preschool expulsion /
early childhood teacher well-being), chosen by the user as the target style.
Patterns are described in our own words; quoted fragments are short phrases only.
When the user has their own writing (thesis chapter, drafts, published papers),
re-run `/write style-guide [dir]` on it and replace this file.

Precedence: APA 7 rules (`.claude/rules/working-paper-format.md`) and content
invariants INV-1..25 override anything here. Where the model papers break APA
or invariant rules, this guide says so and the rule wins.
-->

## Source Corpus

**Extracted on:** 2026-10-06
**Type:** Model voice (papers by other authors, selected by the user as the target style)
**Papers analyzed:** 3
**Paths (outside the repository, not tracked in git):**
- `/Users/juanwang/Documents/My papers/Loomis et al. - 2023 - Teachers' emotion regulation strategies and preschool expulsion risk Suppression and reappraisal.pdf` — *Journal of Applied Developmental Psychology*; quantitative, multilevel moderation
- `/Users/juanwang/Documents/My papers/Zinsser et al. - 2019 - Utilizing social-emotional learning supports to address teacher stress and preschool expulsion.pdf` — *Journal of Applied Developmental Psychology*; mixed methods, mediation + qualitative matrix
- `/Users/juanwang/Documents/My papers/Shenberger and Zinsser - 2026 - An evaluation of "preventing expulsion in preschool" A cognitive-behavioral, strengths-based teache.pdf` — *Infant Mental Health Journal*; pre/post training evaluation, mixed effects models

**Extraction note:** The Shenberger and Zinsser PDF extracts with missing word spaces in parts, so its sentence statistics are unreliable; it informed structure and lexicon only. Sentence statistics below come from Loomis et al. and Zinsser et al.

---

## Sentence Patterns

| Metric | Value | Notes |
|--------|-------|-------|
| Median sentence length (words) | 26–33 | Long, clause-rich sentences; literature sentences carry a parenthetical citation list that adds length |
| Range (10th–90th pct) | 12–55 | Short sentences appear mainly when stating a gap or a hypothesis |
| Passive voice frequency | Moderate — about 23–35% of sentences | Concentrated in Method ("were recruited", "were eligible", "was used to") and in describing prior findings |
| First-person plural ("we", "our") | Sparse to moderate — 0.2–3.4 per 1,000 words | Used for aims and hypotheses ("we hypothesize", "we sought to"); the default subject is **"the current study" / "the present study" / "this study"** |
| Em dashes | Rare — about 0–1 per 1,000 words | Used once to attach a name or definition to a program; otherwise commas and parentheses |
| Semicolons | About 4 per 1,000 words | Mostly separating citations inside parentheses; occasionally joining two related clauses |
| Parentheses | Heavy | Citations, abbreviations at first use (ECE, SEL), percentages, and "e.g.," examples |

---

## Paragraph Architecture

**Typical paragraph structure:**
Claim or fact about the problem → supporting evidence with a parenthetical citation cluster → consequence or implication for children, families, or teachers. Literature paragraphs build cumulatively; each adds one link in the argument chain (problem → disparities → harms → teacher-level mechanism → gap).

**Opening moves:**
- A concrete prevalence figure about the problem, with a report or national-data citation (e.g., how many children are suspended or expelled each day)
- A topic claim naming the construct the paragraph is about (expulsion, teacher stress, emotion regulation, SEL supports)
- In the Discussion, a restatement of what the study did before what it found ("In this study, …", "The present study evaluated …")

**Closing moves:**
- Link the evidence back to young children's outcomes or to teachers' decision-making
- Point to an intervention target ("could be an important target of intervention" type of close)
- In Discussion paragraphs, connect the finding to prior work and then to an opportunity for intervention

**Openings these papers avoid:**
- Generic scene-setting ("In recent years, there has been growing interest …") — when attention to the topic is mentioned, it is tied to a specific figure or policy
- Announcing the paper's structure ("This paper is organized as follows")

---

## Section Architecture

### Introduction
- Opens with the scale of the problem — a specific number on preschool suspension/expulsion — then disparities by gender, race, and disability status in the next sentence or two
- Moves to consequences for children and families, then to the teacher-level mechanism (teacher stress, emotions, perceptions of behavior), usually anchored in a named theoretical model (e.g., the Prosocial Classroom model)
- Previews the present study at the end of the first section, then develops the literature under Level 2 headings named for constructs (child expulsion, teacher stress, emotion regulation, existing interventions)
- Policy and local context get their own short subsection when relevant (a state law or a city policy that limits expulsion)
- Ends with a **"Current Study" / "Present Study"** subsection: the need, the aim stated as "examines the extent to which …", then directional hypotheses, one sentence each

### Method
- First sentence gives the sample: number of teachers, role breakdown in percentages, number and type of programs, region, and school year
- Eligibility criteria and recruitment follow; consent and survey platform named
- Measures subsections named by construct; nested child-within-teacher reports explained plainly (e.g., teachers rated randomly selected children in their classroom)

### Results
- Opens with descriptives and correlations, pointing to the table ("presented in Table 3", "shown in Table 2")
- Each sentence states the relation in words, then the statistic in parentheses after the claim
- Non-significant comparisons reported in the same flat style ("did not significantly differ")
- Qualitative results (mixed-methods papers) are organized by code and by group (e.g., teachers who requested expulsions vs. those who did not), with counts of teachers or references

### Discussion
- First paragraph: restate the design and aims (sometimes as a numbered list of aims), then summarize the headline findings in 3–5 sentences
- Subsections titled with the finding as a short declarative phrase (the style of "Use matters over access" — the finding, not the topic)
- Each finding is placed "in light of prior research" and tied to an intervention or practice implication
- **Limitations and Future Directions** combined: opens with a one-sentence acknowledgment, then specific limitations (self-selected sample, correlational or single time point data, no control group, English-only training), each paired with a concrete future design
- **Implications** subsection for practice and policy (teacher training, program supports, policymakers)

### Conclusion
- Short (one paragraph): restate the problem in one or two sentences, the key finding, and a forward call (systems of support for teachers; more work needed on cultural and contextual factors)

---

## Lexicon

### Words and phrases the model voice uses

Domain terms (use consistently, define at first use): exclusionary discipline, expulsion risk, suspension and expulsion, "soft expulsion", early care and education (ECE), early educators, community-based programs, social-emotional learning (SEL), SEL supports, teacher stress, job-related stress, emotion regulation strategies (reappraisal, suppression), inhibitory control, student-teacher conflict, trauma-informed attitudes, developmentally typical / developmentally appropriate behavior, classroom management, intervention target, expulsion prevention

Framing words: disproportionately, disparities, persist, harmful, alarming (for prevalence only), buffer / exacerbate (for moderation), above and beyond

Transitions: However, (frequent), Therefore, Additionally, Furthermore, Importantly, In other words,

People: children of color, Black children, boys, children with disabilities, Latine/Latino children, teachers of color, lead and assistant teachers

### Words the model voice avoids

Not found in any of the three papers: delve, landscape, pivotal, underscore(s), tapestry, groundbreaking, transformative, game-changing.

Used but rare — keep rare: "nuanced" (one paper only), "leveraging" (once, for data), "crucial", "foster".

### Hedging pattern

- **"may"** is the main hedge — frequent when summarizing literature and when interpreting mechanisms ("may offer", "may indicate", "may be related to")
- "likely" for plausible explanations; "suggests" occasionally after a result
- Associations stated as **"related to"** or **"associated with"**; moderation as "buffered" / "exacerbated" the association
- Results themselves are stated flatly; hedging is reserved for interpretation and mechanism

### Comparison pattern

- Positions findings against prior work in prose: a result "expands on prior findings" or was "surprising" given the authors' or others' earlier results, with the prior study cited parenthetically
- Prior work is compared by direction and pattern more than by effect-size magnitude

---

## Citation Conventions

- **Overwhelmingly parenthetical**, often 2–4 sources in one parenthesis separated by semicolons, placed at the end of the claim
- Narrative citations are rare — used for theoretical models (e.g., Jennings and Greenberg's model) and for programs of research ("Gilliam and colleagues")
- National reports and government data (Office for Civil Rights, federal and state agencies) are cited for prevalence and disparities
- Citations commonly supply examples inside parentheses: "(e.g., crying, inattention; Author, Year)"

---

## Tone Markers

- **Urgent but grounded framing.** The problem is presented as serious and inequitable, always with a number or a source attached
- **Equity is central, not an aside.** Disparities by race, gender, and disability appear in the first paragraph and return in the Discussion
- **Practice-facing.** Every major finding is connected to what teachers, programs, or policymakers could do
- **Measured in results.** Findings are reported plainly; enthusiasm is limited to the implications
- **Candid limitations.** Limitations are specific and paired with what a better study would do

---

## Anti-patterns to Avoid (including habits of the model papers that APA rules override)

- **"p = ns"** (one model paper) → report the exact *p* value (INV-4)
- **Leading zeros on bounded statistics** such as *r* = 0.04 (model papers) → *r* = .04 (INV-4)
- **Significance asterisks** in tables (model papers) → exact *p* columns unless the journal profile allows asterisks (INV-4)
- **Results reported with only *p*** → add an effect size and 95% CI for every primary result (INV-4)
- **Causal words for correlational or cross-sectional mediation results** ("impact", "reduce") → "is associated with", "predicts" (INV-8); one model paper itself notes its data are correlational
- **"Additionally," at the start of consecutive sentences** → the model papers use it often, and it is also on the cleanup list of AI-pattern words; use at most once per section, and prefer integrating the point
- **"In order to"** → "To"
- **"The present study was not without limitations"** style double negatives → state the limitation directly

---

## Notes for the Writer Agent

- Default subject for aims and design: "the current study" / "the present study"; reserve "we" for hypotheses and for describing decisions
- Open the Introduction with a specific prevalence figure and its source, followed by disparities; never with a generic "growing interest" sentence
- End the Introduction with a "Current Study" Level 2 subsection containing directional hypotheses
- Title Discussion subsections with the finding, stated as a short declarative phrase
- Pair every limitation with a specific future design
- Keep sentences long-ish (median about 25–30 words) but break up any sentence with more than one citation cluster
- Person-first or community-preferred, specific group labels (INV-24) — the model papers already do this well
- Re-run `/write style-guide` on the user's own writing when available; this model voice is a starting point
