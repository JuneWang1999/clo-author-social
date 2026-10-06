---
name: talk
description: Create and audit PowerPoint presentations from the paper. Combines talk creation, visual audit, and building. Replaces /create-talk, /visual-audit.
argument-hint: "[mode: create | audit | build | handoff] [format: job-market | seminar | short | lightning] [talk name or .pptx path]"
allowed-tools: Read,Grep,Glob,Write,Edit,Task,Bash
---

# Talk

Create, audit, or build PowerPoint (.pptx) presentations from the paper.

**Input:** `$ARGUMENTS` — mode and format/path.

**How it works:** the Storyteller writes slides as Markdown (`paper/talks/<name>.md`); pandoc turns them into PowerPoint using `paper/talks/reference.pptx` for the design. Once the user starts editing the `.pptx` in PowerPoint, that file is the master and the pipeline never overwrites it (INV-25) — same rule as the manuscript.

---

## Modes

### `/talk create [format]` — Create a PowerPoint Talk

Generate a presentation from the paper.

**Agents:** Storyteller (creator) → storyteller-critic (reviewer)

#### Format Constraints

| Format | Slides | Duration | Content Scope |
|--------|--------|----------|---------------|
| job-market | 40-50 | 45-60 min | Full story, all results, mechanism, robustness |
| seminar | 25-35 | 30-45 min | Motivation, main result, 2 robustness, conclusion |
| short | 10-15 | 12-20 min (conference symposium) | Question, method, key result, implication |
| lightning | 3-5 | 5 min | Hook, one result, so-what |

#### Workflow

**Step 1: Parse Arguments**

- **Format** (required): `job-market` | `seminar` | `short` | `lightning`
- **Paper:** `paper/manuscript.docx` if it exists (read through `.claude/scripts/docx_snapshot.sh`), otherwise the current draft (`paper/sections/*.md`)
- **Talk name:** defaults to `[format]_talk`
- If no format specified, ask the user.
- If `paper/talks/<name>.pptx` already exists, the user owns it: switch to **revision mode** (Step 2b).

**Step 2a: Dispatch Storyteller (new talk)**

Read the paper and extract: research question, design, main result, secondary results, robustness checks, key figures/tables, setting. Design the narrative arc for the format. Write `paper/talks/<name>.md` from `talk/templates/pptx-scaffold.md`, then build:

```bash
paper/talks/build_talk.sh <name>     # -> paper/talks/drafts/<name>_draft.pptx
```

Design principles:
- **One idea per slide** — never cram two concepts onto one slide
- **Figures over tables; tables in backup** — reuse the paper's PNGs from `paper/figures/`
- **Build tension** — motivation → question → method → findings → implications
- **Section divider slides** between major parts
- **All claims must appear in the paper** — the manuscript is the single source of truth

**Step 2b: Revision mode (user-edited .pptx exists)**

Extract the deck with `python3 .claude/scripts/pptx_text.py paper/talks/<name>.pptx`, then write a slide-by-slide change list to `quality_reports/revisions/YYYY-MM-DD_<name>_slides.md` (slide number, current text, proposed text, reason). New slides can be built as a separate draft deck (`paper/talks/drafts/<name>_additions.pptx`) for the user to copy in. Never overwrite the user's `.pptx`.

**Step 3: Dispatch Storyteller-Critic**

Review across 6 categories (`review/templates/talk-review-6-categories.md`):

| Category | What It Checks |
|----------|---------------|
| **Narrative flow** | Clear arc from motivation through results to implications; smooth transitions |
| **Visual quality** | Text overflow, font size (≥ 18 pt body text on projected slides), figure sizing, consistent layouts |
| **Content fidelity** | Every claim and number traceable to the paper |
| **Scope for format** | Right amount of content for the duration |
| **Build integrity** | `build_talk.sh` succeeds; every image found; no placeholder text |
| **Coherence** | Notation and terminology match the paper |

Score as advisory (non-blocking). Save report to `quality_reports/[format]_talk_review.md`.

**Step 4: Fix Critical Issues**

If the storyteller-critic finds Critical issues (build failures, content not in paper):
1. Re-dispatch Storyteller with specific fixes (max 3 rounds per three-strikes rule) — draft deck only
2. Re-run storyteller-critic to verify

**Step 5: Present Results**

Report to the user:
1. Draft deck path (`paper/talks/drafts/<name>_draft.pptx`) — open it in PowerPoint
2. Slide count and format compliance
3. Storyteller-critic score (advisory)
4. TODO items (missing figures, results not yet in the paper)
5. Ask whether to hand off (Step 6)

**Step 6: Handoff**

On the user's clear yes: `paper/talks/build_talk.sh <name> --handoff` → `paper/talks/<name>.pptx`. From then on the user edits it in PowerPoint.

---

### `/talk audit [file]` — Visual Audit

For a `.pptx`: `python3 .claude/scripts/pptx_text.py <file>`, then check:
- Slides with more than ~6 bullet lines or ~40 words (likely overflow at projection size)
- Slides with both a dense table and a figure
- Missing slide titles
- Numbers that don't match the paper
- Speaker notes present on content slides

Visual properties the text extract cannot show (actual font size, image cropping) are flagged as "check in PowerPoint" items.

---

### `/talk build [name]` — Build a Draft Deck

```bash
paper/talks/build_talk.sh <name>
```

### `/talk handoff [name]` — Create the PowerPoint Master

```bash
paper/talks/build_talk.sh <name> --handoff
```

Refuses if `paper/talks/<name>.pptx` already exists.

---

## Changing the Slide Design

`paper/talks/reference.pptx` controls fonts, colors, and layouts for every built deck. To use an institutional template: open `reference.pptx` in PowerPoint, apply the template's theme in **View › Slide Master** while keeping the layout names (Title Slide, Title and Content, Section Header, Two Content, Comparison, Content with Caption, Blank), save, and rebuild.

---

## Bundled Resources

| Resource | Path | What It Contains |
|----------|------|-----------------|
| Narrative arcs | `talk/templates/narrative-arcs.md` | Paper-type-specific story structures with pacing and audience calibration |
| Format constraints | `talk/templates/format-constraints.md` | Slide counts, durations, per-format rules |
| PowerPoint scaffold | `talk/templates/pptx-scaffold.md` | Slide Markdown skeleton: title, sections, figure+text columns, notes, backup |
| Slide design | `talk/references/slide-design-principles.md` | Visual design principles: font sizes, colors, builds, rhythm |
| Gotchas | `talk/gotchas.md` | Known failure points and edge cases |

---

## Principles

- **Paper is authoritative.** Every claim must appear in the paper.
- **The user's .pptx is never overwritten.** Drafts go to `paper/talks/drafts/`; changes to an edited deck are proposals.
- **Figures over tables.** Put regression tables in backup slides for Q&A.
- **Less is more.** Especially for short and lightning formats.
- **One idea per slide.**
- **Audience calibration.** Job talk = rigor and command of the literature. Seminar = the interesting result. Conference symposium = method and key finding. Lightning = the idea in one breath.
- **Advisory scoring.** Talk scores don't block commits.
