# Changelog

All notable changes to LifeLong Learning are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.1] — 2026-06-07

Patch release adding `UPDATE-PROMPT.md` at the LLL root — the fourth required artifact under OVE Convention 7 (added in OVE v1.2.1).

### Added — `UPDATE-PROMPT.md`

Copy-pasteable AI prompt that asks any AI assistant (Claude, ChatGPT, Gemini, Cursor, Claude Code) to walk the operator through updating LLL to the latest release. The prompt instructs the AI to:

1. Read `INSTALL.md § "Updating"` and `OPERATOR-GUIDE.md § "Updates and troubleshooting"` so it knows LLL's update protocol.
2. Run `git fetch origin` and report incoming commits + the new CHANGELOG entry.
3. Check `git status` and propose a stash strategy if local engine modifications exist.
4. Walk through `git pull --ff-only origin main` step by step, stopping to confirm before running.
5. Surface migration recipes, major.minor folder renames, breaking-change notes from the new CHANGELOG entry.
6. Verify the operator's subject cartridges (Operator-Extension Zone) and operator-private files (`_USER.md`, per-subject `_state.md`/`_subject.md`, session logs, Socratic-conceptual quizzes, SR performance logs, synthesis drafts) are intact and untouched after the pull.

The prompt enforces discipline:

- Do not modify Operator-Extension or Operator-Private Zone content.
- Do not run destructive commands without explicit operator confirmation.
- Stop and ask if anything is unclear or unexpected.

### Why two update paths

OVE Convention 7 supports both a **manual path** (operator reads `INSTALL.md § Updating` and `OPERATOR-GUIDE.md § Updates`, runs git commands themselves) and an **AI-assisted path** (operator opens `UPDATE-PROMPT.md`, copies the prompt, pastes to an AI, approves each step). Manual path is recommended for major-version transitions and any release with a non-trivial migration recipe; AI-assisted path is recommended for routine releases (patches and small minors).

### Notes

Patch release — purely additive. No engine prose modified; no schema change; no Prototype content moved.

Coordinated multi-OV release with OVE v1.2.1 (codifies the artifact + adds validator C10), LFW v1.7.2, SOLVE-eX v2.1.3.

## [1.3.0] — 2026-06-06

Adopts OVE Conventions 7 (install-and-update pattern) and 8 (engine vs operator-content boundary). Documents the install/update workflow and the four-zone content boundary in front-door docs.

### Added — OVE Convention 7 (install-and-update pattern)

`INSTALL.md` rewritten with:

- **§ 1** — canonical git-clone-with-push-disabled install snippet. Concrete URL: `https://github.com/JawnLam/LifeLong-Learning.git`. Folder convention: `LifeLong-Learning-v<major>.<minor>`.
- **§ 1a** — alternative no-git install (download ZIP, manual copy).
- **§ 8 — Updating** — `git fetch` + `git log --oneline HEAD..origin/main` + `git pull --ff-only`, with stash-pop fallback for when local engine edits would conflict.
- Major.minor folder transition snippet (`mv LifeLong-Learning-v1.3 LifeLong-Learning-v1.4`).

`OPERATOR-GUIDE.md` gains:

- **§ 10 — Updates and troubleshooting** — clean fast-forward, stash-pop conflict resolution (`git checkout --theirs`), recovery for lost files, major.minor folder transitions, contributing back upstream (re-enable push to your fork; never to upstream).

### Added — OVE Convention 8 (engine vs operator-content boundary)

`CONTRIBUTING.md` gains:

- **§ 6 — Content zones** — declares the four zones with concrete path patterns:
  - **Engine Zone** — front-door docs, `_teaching-engine/`, `_Prototypes/`, `_USER.md.template`, `.gitignore`
  - **Operator-Private Zone** — `_USER.md`, per-subject `_state.md`/`_subject.md`, session logs, Socratic-conceptual quizzes, SR-performance logs, synthesis drafts (weekly/monthly/phase-end/quarterly), SR-card files
  - **Operator-Extension Zone** — operator's own subject cartridges parallel to `Example-Subject-*`
  - **Shipped Examples Zone** — `Example-Subject-Roman-Empire/`

`OPERATOR-GUIDE.md` gains:

- **§ 9 — Engine vs your work** — plain-English explanation of the four-zone boundary, with concrete file/folder examples per zone.

### Notes

This is a minor release. No engine prose changed beyond the documentation additions; no schema change; no Prototype changes. The `.gitignore` already had the right Operator-Private patterns from v1.0; v1.3.0 just documents them in CONTRIBUTING.

The minor bump (rather than patch) reflects that the install/update story now has first-class documentation and the four-zone boundary is now a documented contract operators can rely on.

This release is part of an OVE-coordinated multi-OV cycle: OVE v1.2.0 codifies Conventions 7 and 8; LFW v1.7.1, SOLVE-eX v2.1.2, and this release retrofit them across the OV ecosystem.

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
