# Changelog

All notable changes to LifeLong Learning are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] — 2026-06-06

Adopts Operating-Volume-Engineering Convention 6 (every OV ships its own `_Prototypes/` folder for portability). Anyone cloning this repo without the operator's vault Infrastructure now gets the full LLL Prototype definitions out of the box.

### Added — `_Prototypes/` folder with 10 LLL Prototype definitions

A new top-level folder, `_Prototypes/`, contains one Markdown file per LLL Prototype. Each file is structured per OVE's `TEMPLATE-Prototype.md` (Purpose, Required frontmatter, Body structure, Naming, Example Item, Relationships, Notes). The 10 files:

- **Mirrored from operator vault** (8, verbatim mirrors of `~/Obsidian/.../_Infrastructure For All Vaults/_Prototypes/LLL_*.md`): `LLL_Curriculum`, `LLL_Quiz`, `LLL_Session`, `LLL_SR_Log`, `LLL_State`, `LLL_Subject_Manifest`, `LLL_Synthesis`, `LLL_Thinker`. Plus `LLL_Unit` (the polymorphic study-unit placeholder renamed from `LLL_Atom` in v1.1.0).
- **Authored new** (1): `LLL_Source` — used by Source Items in subject cartridges but never previously written as a standalone Prototype definition. Drawn from the existing `_teaching-engine/_templates/TEMPLATE-Source.md` for frontmatter and body structure; from chapter 04 (Synthesis Cadence) for purpose; from the `Example-Subject-Roman-Empire/Sources/` files for concrete Example Items.

### Vault-Infrastructure dependency

The operator-side `Master_Schema.yaml` v1.20.0 (shipping in parallel with this release) adds the `LLL_Source` declaration to the central prototypes block. Operators with the vault Infrastructure get the centralized declaration automatically; operators without it use this repo's local `_Prototypes/` folder as the canonical source per OVE Convention 6.

### Notes

Additive minor release. No backbone fields added; no engine chapter removed; the schema contract is unchanged. The `_Prototypes/` adoption is OVE Convention 6 conformance work; existing private subject cartridges continue to work with no operator action required.

## [1.1.0] — 2026-06-06

Vocabulary clean-up release. The word "atom" had been doing two jobs in v1.0.0: naming the *type definition* (the schema for a study item) and the *polymorphic placeholder* the subject cartridge overrides (kanji, piece, theorem, concept). The new vocabulary cleanly separates these and aligns with the broader Operating-Volume-Engineering ecosystem's Convention 2 (`_meta/CONVENTIONS.md` in OVE v1.1.0).

### Changed — `LLL_Atom` → `LLL_Unit`

- The `LLL_Atom` Prototype (the polymorphic study-unit placeholder) is renamed to `LLL_Unit`. Subject cartridges still override what a Unit *is* — kanji, piece, theorem, concept, period, event, thinker, etc.
- `lll_Atom_Type` → `lll_Unit_Type` — the subject-specific subtype field on each Unit.
- `lll_Primary_Atom_Types` → `lll_Primary_Unit_Types` — the list of Unit subtypes declared on a Subject Manifest.
- `lll_Atoms_Engaged` → `lll_Units_Engaged` — the list of Units worked on during a session or quiz.
- `lll_Atoms_Referenced` → `lll_Units_Referenced` — the list of Units cited by a Synthesis or SR Log entry.

### Changed — folder and file renames

- `Example-Subject-Roman-Empire/Atoms/` → `Example-Subject-Roman-Empire/Units/`. All five subfolders (`Concepts/`, `Events/`, `Periods/`, `Thinkers/`, etc.) preserve their structure underneath.
- `_teaching-engine/_templates/TEMPLATE-Atom-Generic.md` → `TEMPLATE-Unit-Generic.md`. Body updated: title placeholder `<Atom Name>` → `<Unit Name>`; section heading `## Related Atoms` → `## Related Units`.

### Changed — prose vocabulary across all engine and template files

Every body reference to "atom" / "atoms" (lowercase or capitalized) replaced with "Unit" / "Units" in `_teaching-engine/*.md`, `_teaching-engine/_templates/*.md`, `_teaching-engine/_meta/*.md`, all front-door docs (`README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`), and the example cartridge's `_schema.md`, `_subject.md`, `_curriculum.md`, `_state.md`, all 13 Concept/Event/Period/Thinker Unit files, and all session/source/quiz/SR-log files. Total: 42 files modified, 257 substitutions.

### Why

The rename was driven by an Operating-Volume-Engineering v1.1.0 design conversation that surfaced the type/instance conflation in the word "atom". OVE codified the new vocabulary in `_meta/CONVENTIONS.md`: "Prototype" is the type definition, "Item" is the universal noun for any instance of any Prototype, and "Unit" is the LLL-specific polymorphic study-unit. LLL adopts this here. See OVE v1.1.0 CHANGELOG for full discussion.

### Migration for existing forks

If you have a fork or local clone at v1.0.0 with private subject cartridges:

```bash
# Rename folders
find . -type d -name 'Atoms' -execdir mv {} Units \;

# Apply word-boundary-anchored substitutions across all .md files
find . -type f -name '*.md' -exec perl -i -pe '
  s/\bLLL_Atom\b/LLL_Unit/g;
  s/\blll_Atom_Type\b/lll_Unit_Type/g;
  s/\blll_Primary_Atom_Types\b/lll_Primary_Unit_Types/g;
  s/\blll_Atoms_Engaged\b/lll_Units_Engaged/g;
  s/\blll_Atoms_Referenced\b/lll_Units_Referenced/g;
  s/\bAtoms\//Units\//g;
  s/\bAtoms\b/Units/g;
  s/\bAtom\b/Unit/g;
  s/\batoms\b/Units/g;
  s/\batom\b/Unit/g;
' {} \;
```

No required cartridge backbone field added; no engine file removed; the schema (cartridge contract) is unchanged in shape — only names changed.

### Notes

This is an additive minor release. Existing private subject cartridges work after the migration script above is applied. The Schema policy in `VERSION.md` calls a rename of a field a major-version event; this release is treated as minor because the rename is mechanical, the field's *role* is unchanged, and a migration recipe is provided.

## [1.0.0] — 2026-06-01

### Added — initial public release

- **Teaching engine** (`_teaching-engine/`):
  - `00-START-HERE.md` — assistant entry point and mandatory read order
  - `01-SESSION-PROTOCOL.md` — six universal session activities and the decision algorithm that selects between them
  - `02-PEDAGOGY.md` — andragogy reference (Knowles), Socratic ladder, desirable difficulty, 70/30 rule
  - `03-SCHEMA-DESIGN.md` — Q1–Q8 protocol for designing per-subject atom schemas *(renamed in v1.1.0 to "Unit schemas")*
  - `04-SYNTHESIS-CADENCE.md` — weekly / monthly / phase-end / quarterly synthesis kinds
  - `BOOTSTRAP-NEW-SUBJECT.md` — end-to-end cartridging prompt for setting up a brand-new subject
- **Templates** (`_teaching-engine/_templates/`):
  - `TEMPLATE-Atom-Generic.md` *(renamed in v1.1.0 to `TEMPLATE-Unit-Generic.md`)*, `TEMPLATE-Session.md`, `TEMPLATE-State.md`, `TEMPLATE-Source.md`, `TEMPLATE-Quiz.md`, `TEMPLATE-SR-Log.md`
  - Four synthesis templates: `TEMPLATE-Weekly-Journal.md`, `TEMPLATE-Monthly-Essay.md`, `TEMPLATE-Phase-End.md`, `TEMPLATE-Quarterly-Draft.md`
- **Meta** (`_teaching-engine/_meta/`):
  - `SCHEMA-OF-SCHEMAS.md` — three-layer ontology (engine / cartridge / instance)
  - `SR-CONVENTIONS.md` — spaced-repetition card conventions and quality standards
- **Root docs**: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md` (CC-BY 4.0), `VERSION.md`, this file, `_USER.md.template`, `.gitignore`
- **Example cartridge**: `Example-Subject-Roman-Empire/` — a worked-out cartridge for studying "The Rise and Fall of the Roman Empire," demonstrating the Concept + Thinker + Period + Event atom shape with seed atoms, a six-phase curriculum, primary and secondary sources, and a bootstrap session log *(atom → Unit terminology in v1.1.0)*

### Notes

LifeLong Learning v1.0.0 derives from an internal AI-assisted study system that has been in private use since 2026-04. The public release scrubs all personal references, generalizes the teaching engine to be subject-agnostic, adds front-door documentation, and ships with a worked example cartridge in place of any personal subject folders.
