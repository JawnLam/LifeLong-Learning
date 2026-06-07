---
lll_version: "1.3.1"
schema_version: "1.3"
schema_status: "STABLE"
release_date: 2026-06-07
release_phase: "Patch release — adds UPDATE-PROMPT.md (OVE Convention 7's fourth required artifact); copy-pasteable AI prompt that walks the operator through routine updates"
---

# LifeLong Learning — Version

This is LifeLong Learning **v1.2.0** — Convention 6 (portability) adoption release.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.1.0        | atom → Unit vocabulary clean-up (`LLL_Atom` → `LLL_Unit`)              |
| **Schema**              | v1.1          | STABLE — universal `LLL_*` prototypes locked; `LLL_Atom` renamed to `LLL_Unit` |
| **Teaching engine**     | v1.1          | Subject-agnostic operating manual                                      |
| **Note templates**      | v1.1          | Shipped in `_teaching-engine/_templates/`                              |
| **Example cartridge**   | v1.1          | `Example-Subject-Roman-Empire/`                                        |
| **Release date**        | 2026-06-06    |                                                                        |

## Schema policy

The universal note prototypes (`LLL_State`, `LLL_Subject_Manifest`, `LLL_Session`, `LLL_Quiz`, `LLL_SR_Log`, `LLL_Synthesis`, `LLL_Source`, `LLL_Unit`) are stable at v1.0. Any change that:

- Adds a required field
- Renames a field
- Removes a field
- Changes a field's type

requires a major version bump (v2.0). Additive changes (new optional fields, new template variants within an existing prototype) are minor version bumps (v1.x). See `CONTRIBUTING.md` for the contribution workflow.

## What is in this version

- Subject-agnostic teaching engine in `_teaching-engine/`:
  - Five core operating files (`00`–`04`) plus `BOOTSTRAP-NEW-SUBJECT.md`
  - Ten note templates in `_templates/` (Unit, session, state, source, quiz, SR-log, four synthesis kinds)
  - Schema-of-schemas + SR conventions in `_meta/`
- Front-door docs at the root: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md`
- Optional user profile template: `_USER.md.template`
- One worked example cartridge: `Example-Subject-Roman-Empire/`
- `.gitignore` that keeps a user's private study work out of source control by default

## Compatibility

- **AI:** any capable assistant that can read markdown and parse YAML frontmatter (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS:** Mac, Windows, Linux
- **Editor:** Obsidian recommended (Spaced Repetition + Bases plugins enable the full experience); also works in VS Code, Cursor, Windsurf, Zed, JetBrains, or any text editor that gives an AI read/write access to the folder
- **SR tool:** optional; Obsidian SR plugin, Anki, Mochi, RemNote, or none
- **Python / network / runtime dependencies:** none

## License

See `LICENSE.md`. Released under CC-BY 4.0.
