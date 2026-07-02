---
type: teaching-engine
role: schema-of-schemas
scope: subject-agnostic
updated: 2026-05-31
---

# Schema of Schemas — The Meta-Ontology

> **This document is for humans and AI that want to understand, audit, or extend the LifeLong Learning system's meta-architecture. Most session work does not require reading this. Cartridging does.**

## Three layers of schema

The LifeLong Learning system uses three nested layers of schema:

### Layer 1 — Teaching engine universals (this layer)

The teaching engine (`_teaching-engine/`) defines all universal types (`LLL_State`, `LLL_Subject_Manifest`, `LLL_Session`, `LLL_Quiz`, `LLL_SR_Log`, `LLL_Synthesis`, `LLL_Source`, `LLL_Note`, `LLL_Insight`, `LLL_Community`) and the protocols that govern their use: decision algorithms, pedagogy, synthesis cadence, SR conventions. Applies to every cartridge. Cannot be overridden per subject.

### Layer 2 — Cartridge schema (per subject)

Defined by `<Subject>/_schema.md`. Applies only to that cartridge. Designed during bootstrapping.

- Subject-specific Types (concept, technique, theorem, kanji, period, event, etc.)
- Relationship vocabulary
- Mastery scale (default 0–5 or subject-custom)
- Custom session activities (beyond the universal eight)
- Folder structure within the cartridge

### Layer 3 — Instance (per note)

Defined by each note's YAML frontmatter. Applies to that single note. Every instance declares its type via `type:` and uses `lll_`-prefixed keys for all LLL-specific properties.

- Values for required fields (using `lll_` prefixed property names)
- Optional fields the note chooses to populate

## What universal (Layer 1) note types provide

```
LLL_Session          → one per study session
LLL_Quiz             → one per Socratic/conceptual quiz event
LLL_SR_Log           → rolling performance log per phase
LLL_Synthesis        → weekly-journal | monthly-essay | phase-end | quarterly-draft
LLL_Source           → any external material (book, paper, video, class, etc.)
LLL_State            → single source of truth for subject
LLL_Subject_Manifest → subject's identity document (_subject.md)
LLL_Unit             → generic Unit type; specialized per cartridge
LLL_Note             → fleeting-capture note; lives in root _Inbox/ (un-homed) or <Subject>/Captures/, drained by TRIAGE
LLL_Insight          → decision-grade learning record (ADR-style); lives in <Subject>/Insights/; steers ZPD / what-to-teach-next
LLL_Community        → a vetted place to test skills in the real world (the wisdom axis); lives in <Subject>/Communities/; used by the FIELD-TEST activity
```

These are fully templated in `_teaching-engine/_templates/` and inherited by every cartridge.

## What Layer 2 must provide

Per `_teaching-engine/03-SCHEMA-DESIGN.md`, every `<Subject>/_schema.md` must answer:

- Q1–Q8 analytical questions (knowledge shape, authorities, discrete unit, relationships, progression, mastery endpoint, custom activities, mastery scale)
- Type definitions (one per subject-specific type)
- Relationship vocabulary
- Mastery scale
- Custom activities (if any)
- Folder structure

## Cross-layer rules

1. **Layer 1 never mentions a specific subject.** If the teaching engine names a particular subject anywhere (other than illustrative examples in tables), it's a bug.
2. **Layer 2 never redefines Layer 1 types.** A cartridge cannot redefine what `LLL_Session` is. It can only add to what Layer 1 provides.
3. **Layer 3 must conform to Layer 2 where Layer 2 applies, and Layer 1 where Layer 1 applies.** An Unit note must match its `type` definition in Layer 2. A session note must match the Layer 1 `LLL_Session` definition.
4. **Forward compatibility.** Adding a new subject-specific Type does not break any other cartridge or the teaching engine. Adding a new Layer 1 type requires a teaching engine update and, by extension, a migration of existing cartridges.

## Auditing a cartridge

A well-formed cartridge satisfies:

- [ ] Has all required Layer 1 files (`_state.md`, `_subject.md`, `_schema.md`, `_curriculum.md`)
- [ ] `_schema.md` answers Q1–Q8 and defines all Types used in the cartridge
- [ ] Every Unit note has valid frontmatter with correct `type:` and `lll_`-prefixed properties per its type's definition
- [ ] Every session log conforms to the Layer 1 `LLL_Session` type template
- [ ] `_state.md` references Units that actually exist
- [ ] No dangling `[[wiki-links]]` in Units introduced in this cartridge's phases
- [ ] Phase exit criteria are demonstrable, not vague
- [ ] SR log exists for the current phase

If a cartridge fails audit, it's not ready for study. Fix before continuing.

## Evolution of the teaching engine

If the teaching engine itself needs to change — new universal Type, revised session protocol, modified pedagogy — the change must be:

1. Documented in the relevant `_teaching-engine/` file with a version note
2. Audited against every existing cartridge for compatibility
3. If breaking, a migration path provided for each existing cartridge
4. Logged in the root `CHANGELOG.md`
