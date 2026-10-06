# Drafting Gates -- Approval Checkpoints

Draft sections in this order, pausing for user approval at each gate.

---

## GATE 1: Introduction (Literature Positioning + Hypotheses)

Present to user. Wait for approval before proceeding.

User may redirect:
- Framing
- Contribution positioning
- Literature emphasis
- Hypothesis wording (must match the preregistration, if any)

---

## GATE 2: Method (Participants, Measures, Procedure, Data Analysis)

Present to user. Wait for approval.

User may adjust:
- Sample restrictions and exclusion rules
- Measure descriptions and scoring
- Specification details and missing-data handling
- Transparency statement (preregistration, data/code availability)

---

## GATE 3: Results + Discussion + Abstract

**Hard prerequisite:** Requires actual output files (see Artifact Prerequisites in the agent).
- `paper/tables/` must contain at least one `.rds` table with actual numbers
- `paper/figures/` must contain at least one `.png` figure

Present to user. Wait for approval.

---

## HANDOFF: Word Master

After all three gates pass, build the full draft and ask the user: "Ready to hand off? From now on you edit `paper/manuscript.docx` in Word and I only propose changes." On a clear yes, run `Rscript paper/build_manuscript.R --handoff`. Never hand off without that yes.

---

## Application Rules

- **Single-section drafts:** The gate for that section applies.
- **Full drafts (`/write full`):** All three gates apply in sequence.
- **BLOCKED items:** Results/Discussion cannot be drafted without output files.
- **VERIFY items:** Citations that need user confirmation.
- **VOICE items:** Style guide not yet extracted (drafting blocked until resolved).
