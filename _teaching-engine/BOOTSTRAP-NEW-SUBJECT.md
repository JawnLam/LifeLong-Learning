---
type: teaching-engine
role: cartridge-bootstrapping-prompt
scope: subject-agnostic
updated: 2026-05-31
---

# BOOTSTRAP A NEW SUBJECT

> **You are an AI assistant (Claude, Gemini, ChatGPT, or other capable model). The user has asked you to cartridge a new subject into their LifeLong Learning system — i.e., set up a brand-new topic they want to learn. This document is your complete execution plan. Follow it end-to-end. Ask clarifying questions before building.**

## What you're producing

A complete subject folder inside the `LifeLong Learning/` directory that is ready for the user to begin studying. A successful cartridge includes:

1. `_subject.md` — manifest answering who/why/shape
2. `_schema.md` — Prototype definitions specific to this subject
3. `_curriculum.md` — phase roadmap
4. `_state.md` — initial state
5. Populated Unit folders — enough seed Units for the first 2–4 sessions
6. Populated `Sources/` folder — the books/media/references the user will engage
7. Empty-but-ready subfolders for `Sessions/`, `Quizzes/`, `Synthesis/`, `SR-Cards/`
8. A bootstrap session log (Session 000) documenting what you created

## Before you start

Read these files in order:

1. `_teaching-engine/00-START-HERE.md`
2. `_teaching-engine/01-SESSION-PROTOCOL.md`
3. `_teaching-engine/02-PEDAGOGY.md`
4. `_teaching-engine/03-SCHEMA-DESIGN.md`
5. `_teaching-engine/04-SYNTHESIS-CADENCE.md`
6. All files in `_teaching-engine/_templates/`
7. The shipped example cartridge (`Example-Subject-Roman-Empire/`) as a reference implementation

Do not proceed without reading these. Cartridges that ignore the teaching engine break the system.

## Clarifying questions you must ask the user

Before creating any files, ask the user the following. **One question at a time, in conversation — never as a bulk questionnaire.** Wait for each answer, probe if it's thin, then ask the next.

**Q1: Subject name.** What is the subject, stated precisely? ("Linear algebra" vs "linear algebra through eigendecomposition and SVD" — these are different cartridges.)

**Q2: Why this subject?** What is the user's reason for studying it? (Intellectual curiosity, professional application, personal interest, specific goal?)

**Q3: Prior knowledge.** What does the user already know in this subject? What adjacent subjects do they know well? (This is Knowles's "experience" principle — you cannot teach well without it.)

**Q4: Goals.** What does mastery look like for *this user* in *this subject*? Concretely. ("I want to be able to cook a credible pho from memory" is different from "I want to understand the history of Vietnamese cuisine.")

**Q5: Time commitment and horizon.** How many hours per week, over what period? This shapes the phase count and depth.

**Q6: Depth.** Full rigor (exercises, proofs, all primary sources) vs. conceptual (understand the landscape, skim formalisms) vs. applied (minimize theory, maximize practice)?

**Q7: Scope boundaries.** Is there anything explicitly out of scope? (E.g., "I want macroeconomics but not the math beyond basic calculus." Or "I want music theory but not ear training.")

**Q8: Learning modality preferences.** Books, papers, videos, lectures, podcasts, apps, hands-on practice? Weight them.

**Q9: Communication preferences.** Default is peer register, direct, substantive critique, minimal hedging. Confirm or modify.

Once you have answers, proceed.

## Step-by-step execution

### Step 1 — Create the subject subfolder

Use a human-readable folder name matching the subject. Examples: `Linear-Algebra`, `SE-Asian-Cuisine`, `Music-Theory`, `Japanese-Language`, `Macroeconomics`, `Roman-Empire`. Avoid spaces, avoid abbreviations the user wouldn't recognize.

### Step 2 — Design the schema

Work through the protocol in `_teaching-engine/03-SCHEMA-DESIGN.md`. Specifically answer Q1–Q8 from that document (these are different from the clarifying questions above — they are about the subject's structural shape, not the user's preferences).

Output: `<Subject>/_schema.md` following the required sections laid out in `03-SCHEMA-DESIGN.md`.

This is the most important creative act in cartridging. Take time with it. A poorly-designed schema forces bad Units and a stilted learning experience.

### Step 3 — Write the subject manifest

Output: `<Subject>/_subject.md` using the frontmatter spec in `03-SCHEMA-DESIGN.md`. Include:

- Everything the user told you in Q1–Q9
- A clear summary of the user's goals, prior knowledge, constraints, and communication preferences
- Anything a fresh AI session would need to calibrate teaching correctly on first read

### Step 4 — Design the curriculum

Based on the schema and the user's answers, design a phase structure. Typical phases for a 200–600-hour study are 4–6; shorter studies may have 2–4. Each phase has:

- Core question the phase answers
- Reading/source order (or technique/topic order for skill-based subjects)
- Entry criteria and exit criteria
- Estimated hours (core + deep-dive)
- Subject-specific Units to introduce in this phase

Output: `<Subject>/_curriculum.md`

### Step 5 — Initialize state

Output: `<Subject>/_state.md` using the frontmatter spec and the `_teaching-engine/_templates/TEMPLATE-State.md` template. Populate:

- `lll_Current_Phase: 1`
- Phase 1 Unit list with all mastery levels at 0
- Phase 1 exit checklist
- An "Open Threads for Next Session" section that primes Session 001 to be an orientation

### Step 6 — Seed Units

Create Unit notes for the first phase only. Each Unit note is a seed (frontmatter + skeleton sections + a few genuine questions the user will engage with). Do not fabricate depth — leave sections as `*To be developed*` where appropriate. The user fills them through study.

How many seed Units: enough to run the first 2–4 sessions. For a canonical-thinker subject, typically 5–10 seed Units. For a skill-based subject, typically 8–15 Units since skill Units are smaller. Use your judgment.

Output: files in `<Subject>/Units/` organized per the schema's folder structure.

### Step 7 — Seed sources

Create source notes for the user's active source(s) in Phase 1. Each source note has a progress log, an Unit-mapping section, and a place for highlights/notes. Don't try to populate content — the user generates content as they engage.

Output: files in `<Subject>/Sources/`.

### Step 8 — Create empty-but-ready subfolders

Create `<Subject>/Sessions/`, `<Subject>/Quizzes/Socratic-Conceptual/`, `<Subject>/Quizzes/SR-Performance-Log/`, `<Subject>/Synthesis/Weekly-Journals/`, `<Subject>/Synthesis/Monthly-Essays/`, `<Subject>/Synthesis/Phase-End-Translations/`, `<Subject>/Synthesis/Quarterly-Drafts/`, `<Subject>/SR-Cards/`. Add `.gitkeep` files so they survive transport.

Also create `<Subject>/Quizzes/SR-Performance-Log/Phase-1-SR-Log.md` using `TEMPLATE-SR-Log.md`.

### Step 9 — Write the bootstrap session log

Create `<Subject>/Sessions/YYYY-MM-DD_000_BOOTSTRAP.md` documenting what you created, with a set of open threads for Session 001. The bootstrap session's default next activity is **ORIENTATION** — the real first session walks the user through the cartridge, confirms the cartridging got the user's situation right, and begins the first source material.

### Step 10 — Show the user what you built

Summarize, succinctly:

- Subject name
- Units defined (types and counts)
- Phases (count and names)
- Hours estimate
- What's in Phase 1 specifically
- How to start Session 001

Then stop. The user reviews and approves before study begins.

## Quality gates for a complete cartridge

Before you consider bootstrapping finished, confirm:

- [ ] Clarifying Q1–Q9 asked and answered
- [ ] `_subject.md` exists with all required frontmatter
- [ ] `_schema.md` exists with all required sections and genuine answers to schema Q1–Q8
- [ ] `_curriculum.md` exists with phases, criteria, hours
- [ ] `_state.md` exists and is internally consistent
- [ ] At least 5 seed Units created (more for skill-based subjects)
- [ ] At least 1 active source seeded
- [ ] Empty subfolders created with `.gitkeep`
- [ ] Phase 1 SR log initialized
- [ ] Bootstrap session log written
- [ ] Summary shown to user

## Common failure modes to avoid

1. **Inventing thinkers, authorities, or sources.** If you are not certain a book or figure is real in this subject, say so and ask the user or decline to name it. Fabricated citations poison the cartridge.
2. **Over-seeding Units.** Don't write 50 Units. The user creates most Units through study; you provide scaffolding for the first sessions.
3. **Imposing a canonical-thinker schema on a non-canonical subject.** Cuisine does not have "thinkers." Mathematics usually doesn't have "readings" the same way philosophy does. Design the schema around the subject's actual shape.
4. **Skipping the `_schema.md` schema-design questions.** The questions exist because good schemas come from answered questions. Skipping them produces generic schemas that fit nothing well.
5. **Loading Phase 1 with too many Units or hours.** Phase 1 should be tractable — the user must be able to reach exit criteria within a reasonable time at the stated pace.
6. **Writing teaching content for the Units.** You don't know yet how the user learns best in this subject. Seed Units are scaffolds, not lessons. The real teaching happens in sessions.
7. **Ignoring user preferences already established.** Honor the defaults in `02-PEDAGOGY.md` and any overrides the user gave in Q9. Your communication during cartridging should match the system's overall tone.
8. **Not checking the example cartridge.** When in doubt about file structure or frontmatter style, consult `Example-Subject-Roman-Empire/`.
9. **Bulk-dumping the clarifying questions.** Ask one at a time, conversationally. A multi-bullet "please send me Q1–Q9" message is a failure mode, not the protocol.

## A note on the user

The user is an adult, self-directed learner who chose this system because they want something more rigorous than passive consumption. They do not need hand-holding. They need a well-built system and the occasional push. Cartridging well is primarily technical work; do it carefully, show them what you built, and let them take it from there.
