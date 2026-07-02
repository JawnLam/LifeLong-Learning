---
type: teaching-engine
role: lesson-artifact-authoring
scope: subject-agnostic
updated: 2026-07-02
---

# 05 — LESSONS (optional beautiful artifacts)

> **Optional modality.** LLL teaches primarily through live Socratic sessions, and its durable knowledge lives in Units. A **lesson** is an *optional* extra: a short, self-contained artifact the learner can return to. Produce one when a tangible, revisitable artifact would help — never as a substitute for dialogue.

## What a lesson is

An `LLL_Lesson` is a **markdown note** in `<Subject>/Lessons/` (`0001-slug.md`, incrementing) — the source of truth, Obsidian-native, works on any substrate. From it you may render an *optional* beautiful `0001-slug.html` (below). If you can't render, the markdown lesson stands alone; set `lll_Rendered: false`. This is the same degrade-safe posture as the bundled Anki tool.

A lesson is **not** a Unit. The Unit is the durable knowledge; the lesson is a short teaching *event* tied to the mission and the learner's zone of proximal development. Lessons are rarely revisited; Units and `_glossary.md` are. Don't duplicate a Unit into a lesson.

## The rules of a good lesson

- **One tangible win.** Each lesson delivers a single, ZPD-sized thing the learner can now do. Name it up front (`## The one win`).
- **Fit working memory.** Short. Difficulty is the enemy during acquisition — strip everything not required for the win.
- **Tied to the mission.** If it doesn't serve the reason they're studying (`_subject.md`), don't teach it yet.
- **Cited, never parametric.** Every claim links a Source (`02-PEDAGOGY.md` § "Ground every claim"). Recommend one **primary source** to read next (`lll_Primary_Source`).
- **Ends in retrieval.** Close with an effortful `## Try it` — produce/apply from memory, not "does that make sense?" This is where storage strength is built.
- **Anti-cueing** applies to any in-lesson quiz (`_meta/SR-CONVENTIONS.md`).
- **Invites follow-up.** End reminding the learner their teacher (the AI) can clarify anything.

## Rendering the optional HTML artifact

When the environment supports it (you can write files and the learner can open a browser):

1. Author the markdown lesson first — it is the source of truth.
2. Render a **self-contained** `0001-slug.html` that links the bundled stylesheet: `<link rel="stylesheet" href="../../_teaching-engine/_assets/lesson.css">` (or inline the CSS for a fully portable single file). Use the classes `lesson-win`, `lesson-try`, `cite`, `lesson-foot`.
3. Anchor-link to related lessons and reference docs.
4. Set `lll_Rendered: true`. Optionally open it for the learner with a CLI command.

**Reuse the component library.** Before authoring, read `_assets/` and build from what's there; when you need something new and reusable, add it there — never re-inline what a future lesson would duplicate (`_assets/README.md`).

## When NOT to make a lesson

- When a live Socratic exchange would teach it better (the default).
- When it would just re-render a Unit.
- When no renderer/browser exists — then the markdown lesson is the whole deliverable, and that's fine.
