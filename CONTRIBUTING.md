# Contributing to LifeLong Learning

LifeLong Learning ships at v1.0.0 with a stable schema (`LLL_*` types locked) and a subject-agnostic teaching engine. This document describes when a contribution is in-scope at v1.x, when it requires a major version bump, and how to propose either kind.

For day-to-day operation, see `OPERATOR-GUIDE.md`. For release history, see `CHANGELOG.md`.

---

## 1. What is in-scope at v1.x

The following kinds of contributions do **not** require a major version bump:

| Contribution                                                                | Where it lives                                                                 |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| New example cartridge for a different subject                               | `Example-Subject-<Name>/` at the root                                          |
| New template variant within an existing type                            | `_teaching-engine/_templates/TEMPLATE-<Name>.md`                                |
| Clarification or correction in any teaching engine file                      | Edit in place; bump teaching-engine patch version                              |
| Documentation fixes (README, INSTALL, OPERATOR-GUIDE, this file)             | Edit in place                                                                  |
| New optional field on a `LLL_*` type, backward-compatible               | Update `_meta/SCHEMA-OF-SCHEMAS.md` + the relevant template + minor version bump |
| New tip, failure-mode, or troubleshooting entry in `OPERATOR-GUIDE.md`       | Edit in place                                                                  |
| SR adaptation notes for a new editor/tool                                    | `_teaching-engine/_meta/SR-CONVENTIONS.md`                                     |

---

## 2. What requires a major version bump (v2.0)

Any change to the schema that breaks existing cartridges:

- Adding a **required** field to a `LLL_*` type
- Renaming a field
- Removing a field
- Changing a field's type
- Restructuring `_teaching-engine/` such that existing cartridges can no longer be read by the new engine
- Changing the universal session activity set (the six in `01-SESSION-PROTOCOL.md`) such that existing cartridges' custom activities collide
- Changing what `_state.md` is the source of truth for

These changes require:

1. A documented migration path from v1.x to v2.0
2. A scripted or manual migration users can run on existing cartridges
3. A clear note in `CHANGELOG.md` flagging the break

Don't propose a major break unless the v1 schema demonstrably fails in real use.

---

## 3. What is explicitly out of scope

- **Hardcoded references to a specific subject in `_teaching-engine/`.** The engine is subject-agnostic. If you need a feature that only makes sense for one subject, it belongs in that cartridge's `_schema.md`, not in the engine.
- **Personal data in shipped files.** No real names, emails, paths, or project references in anything that ships. Use placeholders.
- **AI-tool-specific code.** The system is markdown only. If you want Claude Code slash commands or ChatGPT Custom GPT configs, ship them in a separate `integrations/` directory clearly marked as optional.
- **Renaming `LLL_*` types.** The prefix and names are stable. New types can be added; existing ones cannot be renamed without a major version bump (§2).

---

## 4. How to propose a change

### In-scope contribution (no version bump)

1. **Locate the right path** per §1.
2. **Conform to existing conventions.** Read 2–3 existing files in the target folder first to match voice, structure, and metadata format.
3. **Test your change against the example cartridge.** If you changed a template or engine file, verify that `Example-Subject-Roman-Empire/` still parses cleanly with a fresh AI bootstrap session.
4. **Open a pull request** (if hosted on GitHub/GitLab) or share the changeset by other means.

### Major version bump (v2.0)

1. **Draft the schema change** as a markdown spec — what changes, why, what breaks, what the migration looks like.
2. **Author the migration path.** A migration script (if mechanizable) or step-by-step instructions (if not) that converts a v1 cartridge to v2.
3. **Test against at least three example cartridges** of different shapes (canonical-thinker, skill-based, formal/proof-based).
4. **Update `CHANGELOG.md`** with the breaking change clearly flagged.
5. **Update `VERSION.md`** with the new major version.

---

## 5. Voice and tone conventions

When authoring content for the engine (`_teaching-engine/` and its subfolders):

- **Subject-agnostic.** Never name a specific subject except in illustrative tables.
- **Peer register.** Adult learner, direct, substantive. Match the tone of existing files.
- **No flattery, no filler.** "Great question," "interesting," etc. are forbidden.
- **No emojis.** Plain prose.
- **Markdown only.** No HTML, no special syntax that breaks in non-Obsidian editors.

When authoring docs at the root (README, INSTALL, OPERATOR-GUIDE, this file):

- More relaxed — explanatory prose is fine.
- Still no emojis, still no flattery.
- Audience is a human reading the file once, not an AI consuming it every session.

---

## 6. Content zones (OVE Convention 8)

Every file in this repo belongs to one of four zones. Knowing which zone a file is in tells you whether the release owns it (the engine) or the operator owns it.

### Engine Zone — release-owned; updated by `git pull`

| Path pattern | Notes |
|--------------|-------|
| `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md` | Front-door docs |
| `_teaching-engine/**` | Engine chapters, templates, meta |
| `_types/**` | OVE Convention 6 — LLL's own Type definitions |
| `_USER.md.template` | Template only; the populated `_USER.md` is operator-private |
| `.gitignore` | Engine-zone file; its patterns define the Operator-Private patterns below |

**Engine Zone files do not get hand-edited by operators.** Customizations belong in the Operator-Extension Zone (your own subject cartridges) or in per-subject configuration (`_schema.md`, `_curriculum.md`, `_subject.md`).

### Operator-Private Zone — gitignored; never tracked

| Pattern | Why |
|---------|-----|
| `_USER.md` | Operator profile; identity, communication preferences, personal context (F3) |
| `<Subject>/_state.md` | Per-subject state; operator's live working state |
| `<Subject>/_subject.md` | Per-subject identity card (your goals, prior knowledge, cadence) |
| `<Subject>/Sessions/*.md` | Per-subject session logs; verbatim AI/operator conversation |
| `<Subject>/Quizzes/SR-Performance-Log/*.md` | Per-subject SR logs (your retention performance) |
| `<Subject>/Synthesis/**/*.md` | Per-subject synthesis drafts (weekly/monthly/phase-end/quarterly) |
| `_Inbox/*.md` | OV-root un-homed capture pen (`README.md` + `.gitkeep` kept) |
| `<Subject>/Captures/*.md` | Per-subject fleeting-note pen; `LLL_Note` captures awaiting triage |
| `.DS_Store`, `.obsidian/`, IDE caches | Filesystem-noise |

These patterns are in `.gitignore`. The `!Example-Subject-*/**` override re-includes the worked-example subject so it remains tracked (Shipped Examples Zone).

If you want to track your own subject despite the default ignore, edit `.gitignore` to remove the cartridge-content exclusions before your first commit on your own work.

### Operator-Extension Zone — operator-created; survives `git pull`

The OV is designed to be extended at the OV root by adding new subject cartridge folders parallel to the shipped example.

| Pattern | Notes |
|---------|-------|
| `<Subject>/` at the LLL root (anything other than `Example-Subject-*`) | Your own subject cartridges; not in the release; untracked unless you `git add -f` (or remove the cartridge-content `.gitignore` exclusions before commit) |

`git pull` never touches Operator-Extension folders because they aren't in the release tree.

### Shipped Examples Zone — release-owned; updated by `git pull`

| Path | Notes |
|------|-------|
| `Example-Subject-Roman-Empire/` | Worked example: "The Rise and Fall of the Roman Empire" |

**Shipped Examples are reference implementations.** If you want to riff on the example, copy it into an Operator-Extension Zone cartridge (`cp -r Example-Subject-Roman-Empire My-Roman-Study`) and customize there.

## 7. Sharing cartridges

A cartridge is a complete `<Subject>/` folder. Sharing patterns:

- **As an example in this repo:** rename to `Example-Subject-<Name>/`, scrub all personal references (user goals, prior knowledge), and submit as a PR. Useful for demonstrating the system's range.
- **As a personal share:** zip and send. The recipient drops it into their own `LifeLong Learning/` folder and edits `_subject.md` to reflect their own goals and prior knowledge.
- **As a curriculum reference:** strip the user-specific fields from `_subject.md` and ship just the `_schema.md` + `_curriculum.md` + seed Units. Useful for teaching the system itself.

---

## Version

This contribution guide ships with LifeLong Learning v1.0.0. See `VERSION.md` and `CHANGELOG.md`.
