# Changelog

All notable changes to LifeLong Learning are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-06-01

### Added — initial public release

- **Teaching engine** (`_teaching-engine/`):
  - `00-START-HERE.md` — assistant entry point and mandatory read order
  - `01-SESSION-PROTOCOL.md` — six universal session activities and the decision algorithm that selects between them
  - `02-PEDAGOGY.md` — andragogy reference (Knowles), Socratic ladder, desirable difficulty, 70/30 rule
  - `03-SCHEMA-DESIGN.md` — Q1–Q8 protocol for designing per-subject atom schemas
  - `04-SYNTHESIS-CADENCE.md` — weekly / monthly / phase-end / quarterly synthesis kinds
  - `BOOTSTRAP-NEW-SUBJECT.md` — end-to-end cartridging prompt for setting up a brand-new subject
- **Templates** (`_teaching-engine/_templates/`):
  - `TEMPLATE-Atom-Generic.md`, `TEMPLATE-Session.md`, `TEMPLATE-State.md`, `TEMPLATE-Source.md`, `TEMPLATE-Quiz.md`, `TEMPLATE-SR-Log.md`
  - Four synthesis templates: `TEMPLATE-Weekly-Journal.md`, `TEMPLATE-Monthly-Essay.md`, `TEMPLATE-Phase-End.md`, `TEMPLATE-Quarterly-Draft.md`
- **Meta** (`_teaching-engine/_meta/`):
  - `SCHEMA-OF-SCHEMAS.md` — three-layer ontology (engine / cartridge / instance)
  - `SR-CONVENTIONS.md` — spaced-repetition card conventions and quality standards
- **Root docs**: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md` (CC-BY 4.0), `VERSION.md`, this file, `_USER.md.template`, `.gitignore`
- **Example cartridge**: `Example-Subject-Roman-Empire/` — a worked-out cartridge for studying "The Rise and Fall of the Roman Empire," demonstrating the Concept + Thinker + Period + Event atom shape with seed atoms, a six-phase curriculum, primary and secondary sources, and a bootstrap session log

### Notes

LifeLong Learning v1.0.0 derives from an internal AI-assisted study system that has been in private use since 2026-04. The public release scrubs all personal references, generalizes the teaching engine to be subject-agnostic, adds front-door documentation, and ships with a worked example cartridge in place of any personal subject folders.
