---
lll_version: "1.8.0"
schema_version: "1.5"
schema_status: "STABLE"
release_date: 2026-07-02
release_phase: "Minor release — the Anki live-sync tool is now BUILT INTO the OV (_teaching-engine/_scripts/anki_sync.py, stdlib-only). Any AI running LLL with shell access can push/pull cards with no external skill. No schema change (v1.5 retained)"
---

# LifeLong Learning — Version

This is LifeLong Learning **v1.8.0** — Anki live-sync is now a **built-in OV feature**. The AnkiConnect push/pull tool ships with the engine at `_teaching-engine/_scripts/anki_sync.py` (Python 3 standard library only — nothing to install), so **any** operator who chooses Anki gets one-command live sync without building or knowing about "skills." The dependency-free TSV-import path remains for AIs with no shell. This reverses v1.6.0's choice to keep the automation in an external skill — most operators won't have one, so the capability belongs in the OV. No schema change (v1.5 retained).

Prior releases: **v1.7.0** — spaced repetition made opt-in at bootstrap (`lll_SR_Enabled`). **v1.6.0** — first-class Anki integration (export contract + TSV + AnkiConnect). **v1.5.0** — the capture layer (`LLL_Note`, `_Inbox/`/`Captures/`, TRIAGE).

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.8.0        | Built-in Anki live-sync tool (`_scripts/anki_sync.py`); no external skill needed (v1.7.0: SR opt-in; v1.6.0: Anki integration; v1.5.0: capture layer)   |
| **Schema**              | v1.5          | STABLE — added `lll_SR_Enabled` (boolean) to `LLL_Subject_Manifest`; additive |
| **Teaching engine**     | v1.8.0        | Five core operating files (`00`–`04`) + `BOOTSTRAP-NEW-SUBJECT.md` (SR Q10); seven universal activities; SR-CONVENTIONS backend-onboarding + Anki contract; new optional `_scripts/` (bundled `anki_sync.py`) |
| **Note templates**      | v1.7.0        | Eleven templates (unchanged since v1.5.0)                              |
| **Example cartridge**   | v1.7.0        | `Example-Subject-Roman-Empire/` — `Captures/` (v1.5.0); Anki export regenerated on demand, not shipped |
| **Release date**        | 2026-07-01    |                                                                        |

## Schema policy

The universal note types (`LLL_State`, `LLL_Subject_Manifest`, `LLL_Session`, `LLL_Quiz`, `LLL_SR_Log`, `LLL_Synthesis`, `LLL_Source`, `LLL_Unit`, `LLL_Note`) are stable. Any change that:

- Adds a required field
- Renames a field
- Removes a field
- Changes a field's type

requires a major version bump (v2.0). Additive changes (a new optional type such as `LLL_Note`, new optional fields, new template variants within an existing type) are minor version bumps (v1.x). See `CONTRIBUTING.md` for the contribution workflow.

## What is in this version

- Subject-agnostic teaching engine in `_teaching-engine/`:
  - Five core operating files (`00`–`04`) plus `BOOTSTRAP-NEW-SUBJECT.md`; the session protocol now defines **seven** universal activities (TEACH, QUIZ-SR, QUIZ-SOCRATIC, REVIEW-WEAK, SYNTHESIZE, INTEGRATE, **TRIAGE**)
  - Eleven note templates in `_templates/` (Unit, session, state, source, quiz, SR-log, four synthesis kinds, **Note**)
  - Schema-of-schemas + SR conventions in `_meta/` — `SR-CONVENTIONS.md` now carries the **Anki integration contract** (deck/tag/deterministic-key/notetype mapping; TSV import path; AnkiConnect two-way procedure)
- **Spaced-repetition opt-in (v1.7.0):** bootstrap Q10 asks whether the user wants SR and which backend, then guides one-time setup (SR-CONVENTIONS "Choosing and setting up an SR backend"). Backend recorded once in `_USER.md`; per-subject `lll_SR_Enabled` toggle on the manifest; QUIZ-SR is guarded on it. Fixes a stale `Item_Prototype` key in `_USER.md.template`.
- **Anki integration (v1.6.0):** first-class Anki SR backend. Dependency-free TSV import for any AI substrate; optional live AnkiConnect push + two-way review-stat sync (desktop + add-on); AnkiWeb review via Anki's own sync. No schema change. A companion Claude Code skill (operator-private, outside this repo) packages the AnkiConnect automation.
- **Capture layer (v1.5.0):**
  - `_types/LLL_Note.md` — the fleeting-note type (`lll_Note_Kind`, `lll_Note_Status`, `lll_Promoted_To`, `lll_Captured_During`; `Needs_Processing: true` on birth)
  - OV-root `_Inbox/` (with its own `README.md`) — un-homed captures, `lll_Subject` empty
  - Per-subject `<Subject>/Captures/` — subject-homed captures awaiting triage
- Front-door docs at the root: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `UPDATE-PROMPT.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md`
- Optional user profile template: `_USER.md.template`
- One worked example cartridge: `Example-Subject-Roman-Empire/` (now with a `Captures/` folder)
- `.gitignore` that keeps a user's private study work — including capture pens — out of source control by default

## Compatibility

- **AI:** any capable assistant that can read markdown and parse YAML frontmatter (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS:** Mac, Windows, Linux
- **Editor:** Obsidian recommended (Spaced Repetition + Bases plugins enable the full experience; Bases can filter the capture pens by `lll_Note_Status`); also works in VS Code, Cursor, Windsurf, Zed, JetBrains, or any text editor that gives an AI read/write access to the folder
- **SR tool:** optional; Obsidian SR plugin, Anki, Mochi, RemNote, or none
- **Python / network / runtime dependencies:** none for core study. *Optional:* the bundled Anki live-sync helper (`_teaching-engine/_scripts/anki_sync.py`) needs Python 3 (standard library only — no pip) and talks solely to Anki on `localhost`; skip it and use TSV import if you prefer zero scripts.

## License

See `LICENSE.md`. Released under CC-BY 4.0.
