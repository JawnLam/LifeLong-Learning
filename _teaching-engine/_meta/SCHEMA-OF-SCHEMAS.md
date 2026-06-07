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

The teaching engine (`_teaching-engine/`) defines all universal prototypes (`LLL_State`, `LLL_Subject_Manifest`, `LLL_Session`, `LLL_Quiz`, `LLL_SR_Log`, `LLL_Synthesis`, `LLL_Source`) and the protocols that govern their use: decision algorithms, pedagogy, synthesis cadence, SR conventions. Applies to every cartridge. Cannot be overridden per subject.

### Layer 2 — Cartridge schema (per subject)

Defined by `<Subject>/_schema.md`. Applies only to that cartridge. Designed during bootstrapping.

- Subject-specific Prototypes (concept, technique, theorem, kanji, period, event, etc.)
- Relationship vocabulary
- Mastery scale (default 0–5 or subject-custom)
- Custom session activities (beyond universal six)
- Folder structure within the cartridge

### Layer 3 — Instance (per note)

Defined by each note's YAML frontmatter. Applies to that single note. Every instance declares its prototype via `Item_Prototype:` and uses `lll_`-prefixed keys for all LLL-specific properties.

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
LLL_Unit             → generic Unit prototype; specialized per cartridge
```

These are fully templated in `_teaching-engine/_templates/` and inherited by every cartridge.

## What Layer 2 must provide

Per `_teaching-engine/03-SCHEMA-DESIGN.md`, every `<Subject>/_schema.md` must answer:

- Q1–Q8 analytical questions (knowledge shape, authorities, discrete unit, relationships, progression, mastery endpoint, custom activities, mastery scale)
- Prototype definitions (one per subject-specific type)
- Relationship vocabulary
- Mastery scale
- Custom activities (if any)
- Folder structure

## Cross-layer rules

1. **Layer 1 never mentions a specific subject.** If the teaching engine names a particular subject anywhere (other than illustrative examples in tables), it's a bug.
2. **Layer 2 never redefines Layer 1 prototypes.** A cartridge cannot redefine what `LLL_Session` is. It can only add to what Layer 1 provides.
3. **Layer 3 must conform to Layer 2 where Layer 2 applies, and Layer 1 where Layer 1 applies.** An Unit note must match its `Item_Prototype` definition in Layer 2. A session note must match the Layer 1 `LLL_Session` definition.
4. **Forward compatibility.** Adding a new subject-specific Prototype does not break any other cartridge or the teaching engine. Adding a new Layer 1 prototype requires a teaching engine update and, by extension, a migration of existing cartridges.

## Auditing a cartridge

A well-formed cartridge satisfies:

- [ ] Has all required Layer 1 files (`_state.md`, `_subject.md`, `_schema.md`, `_curriculum.md`)
- [ ] `_schema.md` answers Q1–Q8 and defines all Prototypes used in the cartridge
- [ ] Every Unit note has valid frontmatter with correct `Item_Prototype:` and `lll_`-prefixed properties per its type's definition
- [ ] Every session log conforms to the Layer 1 `LLL_Session` prototype template
- [ ] `_state.md` references Units that actually exist
- [ ] No dangling `[[wiki-links]]` in Units introduced in this cartridge's phases
- [ ] Phase exit criteria are demonstrable, not vague
- [ ] SR log exists for the current phase

If a cartridge fails audit, it's not ready for study. Fix before continuing.

## Evolution of the teaching engine

If the teaching engine itself needs to change — new universal Prototype, revised session protocol, modified pedagogy — the change must be:

1. Documented in the relevant `_teaching-engine/` file with a version note
2. Audited against every existing cartridge for compatibility
3. If breaking, a migration path provided for each existing cartridge
4. Logged in the root `CHANGELOG.md`
