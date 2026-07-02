# Changelog

All notable changes to LifeLong Learning are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.8.0] — 2026-07-02

Minor — **the Anki live-sync tool is now built into the OV.** Reverses v1.6.0's decision to keep the AnkiConnect automation in an external Claude Code skill. Rationale: most operators won't have that skill (or know skills exist), yet a large majority who pick Anki will want live sync — so the capability belongs in the OV, where the default assumption is "no skill." No schema change (v1.5 retained).

### Added — `_teaching-engine/_scripts/anki_sync.py` (+ `_scripts/README.md`)

The bundled AnkiConnect client: `verify` / `push --tsv <file>` / `pull --deck <deck>`. **Python 3 standard-library only — nothing to `pip install`**, talks only to Anki on `localhost:8765`. Any AI running LLL with shell access (or the operator by hand) runs it directly:

```bash
python3 _teaching-engine/_scripts/anki_sync.py push --tsv "<Subject>/SR-Cards/anki-export.tsv"
```

`push` is idempotent via the `lll-id::` identity tag (re-running updates, never duplicates); `pull` prints per-Unit stats as JSON and never writes to the vault (the assistant applies them to the SR-Log + `_state.md`). This is the same, corrected implementation validated live in v1.6.0 (including the card-vs-note tag fix).

### Changed

- `_meta/SR-CONVENTIONS.md` — the Anki setup, "Path B" procedure, and QUIZ-SR sections now point at the bundled script with exact commands; the earlier "see the operator's Anki skill" references are gone. Explicit: **no external skill is required.** TSV import (Path A) remains the fallback for AIs without shell access.
- `README.md` — the "Python: not used / no scripts" line is corrected: core study is still script-free, but the optional Anki live-sync helper is a bundled stdlib-only script (localhost-only). `AI-BOOTSTRAP.md` folder tree adds `_scripts/`.
- `VERSION.md` → v1.8.0.
- The operator-side `/anki` Claude Code skill is demoted to a thin convenience that delegates to the bundled OV script (single source of truth; no code duplication).

### Note

Core LLL remains dependency-free and substrate-agnostic. The bundled script is **optional** and only relevant to operators who chose Anki *and* run AnkiConnect; everyone else is unaffected, and the no-script TSV path still works everywhere.

## [1.7.0] — 2026-07-01

Minor — **spaced repetition is now opt-in, asked and set up at bootstrap.** Previously SR was silently assumed (the bootstrap never asked, yet the engine expected an SR tool and unconditionally initialized a Phase-1 SR log). Now the AI asks and guides setup. Additive schema growth (1.4 → 1.5).

### Added — the SR question + guided setup

- `BOOTSTRAP-NEW-SUBJECT.md` gains **Q10**, in two parts: (1) a **global, ask-once** question — do you want SR, and with which backend (**Anki** recommended / **Obsidian Spaced Repetition plugin** / **other** / **none**) — recorded in `_USER.md`, with **one-time setup guided** when the chosen tool isn't installed; (2) a **per-subject** on/off toggle. Plus an execution step, a quality-gate change (SR log initialized *only* if enabled), and a new failure mode ("assuming spaced repetition").
- `_meta/SR-CONVENTIONS.md` gains a **"Choosing and setting up an SR backend"** section with step-by-step onboarding for Anki (desktop → AnkiConnect `2055492159` → AnkiWeb) and the Obsidian SR community plugin, plus "other" and "none" paths. The Socratic-fallback section is tied to the flag.

### Added — `lll_SR_Enabled` (schema 1.4 → 1.5)

New boolean on `LLL_Subject_Manifest` — whether a subject uses spaced repetition. `01-SESSION-PROTOCOL.md` guards the **QUIZ-SR** activity on it (never fires when `false`). Added to the manifest frontmatter spec in `03-SCHEMA-DESIGN.md` and the `_types/LLL_Subject_Manifest.md` definition. The SR *backend* itself lives once, globally, in `_USER.md` (not per-subject).

### Fixed

- `_USER.md.template` — stale `Item_Prototype:` frontmatter key corrected to `type:` (a leftover from the OKF `type`-discriminator rename). Added the global **Spaced-repetition backend** preference line.

### Coordinated vault-schema change

Vault `Master_Schema.yaml` v1.39.0 → v1.40.0: registered the `lll_SR_Enabled` property and added it to `LLL_Subject_Manifest.specific_keys`; mirrored the updated `_types/LLL_Subject_Manifest.md`. Purely additive.

## [1.6.0] — 2026-07-01

Minor — **first-class Anki integration.** Makes Anki a real SR backend instead of a vaguely-supported option. Additive engine capability; **no schema change** (schema stays v1.4 — the integration needs no new type or field).

### Added — the Anki export contract (`_meta/SR-CONVENTIONS.md`)

A stable mapping from a Unit's cards to Anki, used identically by both transport paths:

- **Identity:** a deterministic per-card key `lll-id::<subject-slug>::<unit-id>::<card-index>` — derived from stable inputs, so re-export *updates* rather than duplicates, with no stored state. Carried as the Anki note GUID (TSV path) or as a tag (AnkiConnect path).
- **Deck:** `LLL::<Subject>` (one deck per subject; phases are tags, so cards never migrate decks).
- **Tags:** `lll::subject::<slug>`, `lll::phase::<n>`, `lll::unit::<unit-slug>`, `lll::kind::<recall|application|boundary|connection>`.
- **Notetypes:** built-in **Basic** and **Basic (and reversed)** only — nothing to install.

### Added — two transport paths

- **Path A — TSV import (portable default).** The assistant writes `<Subject>/SR-Cards/anki-export.tsv` with Anki's header directives (`#separator:tab`, `#notetype/deck/tags/guid column:`); the operator does File → Import once and re-imports update in place. Zero dependency; works from any AI substrate. Gitignored as operator-private.
- **Path B — AnkiConnect (live, two-way).** With Anki desktop + the AnkiConnect add-on (code `2055492159`), an assistant with local HTTP access pushes cards (`findNotes` → `addNote`/`updateNoteFields`, idempotent via the identity tag) and **pulls review performance back** (`findCards`/`cardsInfo`/`getReviewsOfCards`) into `<Subject>/Quizzes/SR-Performance-Log/Phase-<N>-SR-Log.md`, reconciling `lll_Status: weak` flags in `_state.md`. Anki becomes the scheduling system of record; LLL stays authoritative on what's learned and which Units are weak.

### Changed

- `README.md` — SR-tool line promotes Anki to first-class with a pointer to the contract.
- `_meta/SR-CONVENTIONS.md` — intro updated; QUIZ-SR behavior documented for the Anki case (push → review in Anki/AnkiWeb → pull).
- `VERSION.md` — v1.6.0 (schema unchanged v1.4).

### Companion (outside this repo)

A Claude Code **Anki skill** (operator-private, parent-child structure) packages the Path-B automation — one-command push and stat-pull against AnkiConnect. It *reads* this export contract; it is not part of the portable OV, preserving LLL's no-dependency posture. AnkiWeb has no public write API, so all paths reach AnkiWeb only via Anki's own client sync.

## [1.5.0] — 2026-07-01

Minor — **the capture layer.** Adds the fleeting-note tier that was missing between raw thought and permanent Unit: a place to put an idea, question, quote, link, or cross-cutting connection *before* you know where it belongs. Additive schema growth — one new type, zero renames, zero removals, no breaking change. Schema v1.3 → v1.4.

### Added — `LLL_Note` type + `TEMPLATE-Note.md`

The fleeting-note type. Frontmatter: `lll_Subject` (**may be empty** — that is the point), `lll_Note_Kind` (idea | question | connection | quote | link | observation | source-lead), `lll_Note_Status` (`captured → triaged → promoted | merged | discarded`), `lll_Promoted_To` (backlink to the Unit/Source it became), `lll_Captured_During` (session provenance), and `Needs_Processing: true` on birth — which finally makes the long-dormant `Needs_Processing` flag load-bearing. Body sections: Capture / Origin / Possible homes / Triage disposition.

### Added — two capture pens

- **`_Inbox/`** (OV root, sibling to subjects) — the un-homed pen: captures whose subject is unknown or cross-cutting. Ships with a `README.md` explaining the layer. `lll_Subject` empty.
- **`<Subject>/Captures/`** — the subject-homed pen: captures you know belong to one subject but haven't processed into a Unit yet.

The one *move* in the system is homing: TRIAGE assigns a subject to a root-`_Inbox/` note and moves it into that subject's `Captures/`. After that, disposition is status-only, preserving provenance.

### Added — TRIAGE (7th universal session activity)

`01-SESSION-PROTOCOL.md`: the activity table grows from six to seven; TRIAGE processes the inbox (promote / merge / discard). Decision-algorithm hook (Step 1 hard override): proposed when `_Inbox/` holds ≥ 5 untriaged captures or any capture with `Needs_Processing: true` is older than 14 days; the pending count is surfaced at every session start. The CAPTURE lifecycle step (step 6) is extended: a stray mid-session thought is dropped into `_Inbox/` rather than lost.

### Changed

- `_teaching-engine/_meta/SCHEMA-OF-SCHEMAS.md` — `LLL_Note` registered in the Layer-1 universal type list; "universal six" → "universal seven".
- `BOOTSTRAP-NEW-SUBJECT.md` — new cartridges create `Captures/` (+ `.gitkeep`); quality gate updated; `_Inbox/` documented as the shared, do-not-recreate-per-cartridge root pen.
- `README.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `AI-BOOTSTRAP.md` — folder-structure tables, the four-zone boundary (capture pens are Operator-Private), and the session walkthrough updated.
- `.gitignore` — `_Inbox/*.md` and `**/Captures/*.md` excluded as operator-private (keeping `_Inbox/README.md` + `.gitkeep`); `!Example-Subject-*/Captures/*.md` keeps the worked examples tracked.
- `VERSION.md` — rewritten to v1.5.0 and made internally consistent (the previous file's frontmatter, body, and table disagreed).
- `Example-Subject-Roman-Empire/` — gained `Captures/` with two worked examples: one live `captured` note (anacyclosis ↔ mixed constitution) and one `merged` note (tribune sacrosanctity → folded into the Patrician-Plebeian Unit).

### Coordinated vault-schema change

Vault `Master_Schema.yaml` v1.38.0 → v1.39.0: registered the `LLL_Note` type, four `lll_` properties (`lll_Note_Kind`, `lll_Note_Status`, `lll_Promoted_To`, `lll_Captured_During`), two enums (`lll_note_kinds`, `lll_note_statuses`), and `TRIAGE` in `lll_activities`; mirrored `_types/LLL_Note.md` into the vault type registry. Without this, the vault `schema-validator.py` would flag every `LLL_Note` as an invalid type.

## [1.4.1] — 2026-06-27

Patch — **terminology retirement: "Prototype" → "Type".** The OVE engine concept formerly called a *Prototype* (the type-definition unit) is now uniformly called a **Type**, completing the OKF `type` vocabulary adopted in 1.4.0. Infrastructure surfaces only — `_teaching-engine/` docs, `SCHEMA-OF-SCHEMAS.md`, `03-SCHEMA-DESIGN.md`, `_types/LLL_Source.md`, and front-door docs. Domain/manuscript prose, historical CHANGELOG entries below, and Hugo are unchanged. No behavioral or content change.

## [1.4.0] — 2026-06-26

Google OKF v0.1 conformance (coordinated with vault Master_Schema v1.23.0 + OVE v2.4.0). Universal Core renamed to OKF field names (Item_Prototype→type, Title→title, Tags→tags; added timestamp from Date_Modified, optional description/resource). Convention-6 folder _Prototypes/ → _types/. Date_Modified kept, time-synced with timestamp. Hugo excluded.

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
  - **Engine Zone** — front-door docs, `_teaching-engine/`, `_types/`, `_USER.md.template`, `.gitignore`
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

Adopts Operating-Volume-Engineering Convention 6 (every OV ships its own `_types/` folder for portability). Anyone cloning this repo without the operator's vault Infrastructure now gets the full LLL Prototype definitions out of the box.

### Added — `_types/` folder with 10 LLL Prototype definitions

A new top-level folder, `_types/`, contains one Markdown file per LLL Prototype. Each file is structured per OVE's `TEMPLATE-Prototype.md` (Purpose, Required frontmatter, Body structure, Naming, Example Item, Relationships, Notes). The 10 files:

- **Mirrored from operator vault** (8, verbatim mirrors of `~/Obsidian/.../_Infrastructure For All Vaults/_types/LLL_*.md`): `LLL_Curriculum`, `LLL_Quiz`, `LLL_Session`, `LLL_SR_Log`, `LLL_State`, `LLL_Subject_Manifest`, `LLL_Synthesis`, `LLL_Thinker`. Plus `LLL_Unit` (the polymorphic study-unit placeholder renamed from `LLL_Atom` in v1.1.0).
- **Authored new** (1): `LLL_Source` — used by Source Items in subject cartridges but never previously written as a standalone Prototype definition. Drawn from the existing `_teaching-engine/_templates/TEMPLATE-Source.md` for frontmatter and body structure; from chapter 04 (Synthesis Cadence) for purpose; from the `Example-Subject-Roman-Empire/Sources/` files for concrete Example Items.

### Vault-Infrastructure dependency

The operator-side `Master_Schema.yaml` v1.20.0 (shipping in parallel with this release) adds the `LLL_Source` declaration to the central prototypes block. Operators with the vault Infrastructure get the centralized declaration automatically; operators without it use this repo's local `_types/` folder as the canonical source per OVE Convention 6.

### Notes

Additive minor release. No backbone fields added; no engine chapter removed; the schema contract is unchanged. The `_types/` adoption is OVE Convention 6 conformance work; existing private subject cartridges continue to work with no operator action required.

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
