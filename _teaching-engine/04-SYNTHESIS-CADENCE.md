---
type: teaching-engine
role: synthesis-cadence
scope: subject-agnostic
updated: 2026-05-31
---

# 04 — SYNTHESIS CADENCE

> **Synthesis converts intake into knowledge the user can act from. This cadence applies across all subjects. Individual cartridges may add subject-specific synthesis kinds (e.g., a cuisine cartridge might include a "menu-design" synthesis; a language cartridge might include a "translation-attempt"), documented in `<Subject>/_schema.md`.**

## Four universal synthesis kinds

| Kind | Trigger | Target length |
|------|---------|---------------|
| **Weekly journal** | Every 3–5 sessions | 30–45 min, 200–500 words |
| **Monthly essay** | Every 12–18 sessions OR on request | 1,500–2,500 words |
| **Phase-end translation** | At phase exit | 2,000–3,000 words |
| **Quarterly public-facing draft** | Every ~40 sessions OR on request | Variable, public-ready |

## Why this cadence

**Weekly journals** catch learning the moment it happens. Three prompts: *What did I understand this week that I didn't last week? What am I still uncertain about? Where in my current work does this show up?*

**Monthly essays** force consolidation. Pick a concept or tension from the month and write through it. These are first drafts of future public work regardless of whether the user ever publishes.

**Phase-end translations** translate theory into the user's own practice at each phase boundary. Across a multi-phase study, these accumulate into the backbone of any eventual synthesis output.

**Quarterly public-facing drafts** force writing for an external reader, which exposes thinness that self-directed journaling protects.

## Assistant's role

- Propose SYNTHESIZE activity per the triggers in `01-SESSION-PROTOCOL.md`
- When the user brings a completed synthesis piece for review, critique substantively — where the argument is thin, where citations don't do the work, where a domain expert would push back
- Store artifacts in `<Subject>/Synthesis/<Kind>/` using the templates in `_teaching-engine/_templates/`
- Track synthesis count in `_state.md`

## Adaptations per subject shape

Not every subject has the same synthesis pattern:

- **Canonical-thinker subjects** (philosophy, cybernetics, intellectual history): journals and essays work naturally; translations connect theory to practice
- **Formal subjects** (math, logic): synthesis may take the form of worked-example collections, proof-technique summaries, or connection-maps rather than essays
- **Skill-based subjects** (languages, instruments, cooking): synthesis may be performances, recordings, completed dishes, translation attempts, compositions — the "artifact" is the skill's output, and the writing is reflection on it
- **Empirical / historical subjects** (medicine, history, political science): synthesis may be case analyses, review syntheses across multiple sources, or mechanism/causation maps

If the subject's shape requires a modified synthesis approach, document it in `<Subject>/_schema.md` under "Synthesis adaptations."

## Synthesis output goals

The default posture is: produce synthesis continuously at all four cadence levels so that raw material accumulates regardless of eventual output form. Whether the user's final output is a framework, a book, a teaching curriculum, a playlist, a cookbook, or a portfolio of compositions, the weekly and monthly artifacts feed it.

If the user has a specific output target in mind (a book, a course, a public Substack, a portfolio), record it in `<Subject>/_subject.md` under `lll_User_Goals` so synthesis can be aimed accordingly. Otherwise let it emerge.
