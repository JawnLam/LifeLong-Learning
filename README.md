# LifeLong Learning

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](VERSION.md)

LifeLong Learning is an **[operating volume](https://github.com/JawnLam/Operating-Volume-Engineering)** for AI-orchestrated self-directed deep study. Pick a topic you've always wanted to learn. Point any capable AI at this folder, tell it to read `AI-BOOTSTRAP.md`, and it will set up the topic, design a curriculum, and run sessions with you over weeks, months, or years — keeping all state in plain markdown files so you own your work and never depend on a service that can disappear.

> **What's an operating volume?** A self-contained markdown corpus an AI loads to orchestrate a particular kind of long-running, stateful work — the slot in the AI lexicon between a Custom GPT / Project and an AI harness. Substrate-agnostic (Claude, GPT, Gemini, etc.), stateful (files on disk are the memory), forkable. See **[Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering)** for the discipline and a worked-example design walkthrough. LifeLong Learning is one of three operating volumes by the same author, alongside **[SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)** and **Operating-Volume-Engineering** itself.

---

## What this is

LifeLong Learning is a teaching engine plus a per-subject "cartridge" system. The teaching engine is the AI's operating manual: how to set up a new topic, how to run a session, how to decide what activity comes next, how to quiz, how to provoke synthesis. Cartridges are subject folders — one per topic you're studying — that the engine plugs into.

You don't need to learn the system. The AI does. You point it at the folder and start a conversation.

The default tone is peer-level, direct, substantive critique. The system treats you as an adult learner who wants to actually master something, not a student who needs encouragement.

## What it can help with

- **Any subject with depth.** History, philosophy, science, math, languages, music, cooking, a craft, a body of literature, a religious tradition, a professional discipline you want to take seriously.
- **Self-paced rigor.** You set the hours per week and the depth. The AI adapts the curriculum to fit.
- **Long-horizon study.** Designed for weeks, months, or multi-year arcs — not a single sitting.
- **Synthesis output.** Weekly journals, monthly essays, phase-end translations, quarterly drafts accumulate as you go. If you eventually want to publish, teach, or build something from what you learn, the raw material is already on disk.

## What it is not

- **Not a course catalog.** There is no pre-built syllabus for any subject. The AI designs one with you, based on your goals.
- **Not a chatbot tutor.** It is a stateful, file-based system. Every session writes to disk. Your progress is your own, in plain markdown, forever.
- **Not opinionated about your editor.** Works well in Obsidian (with the Spaced Repetition and Bases plugins) but also in VS Code, Cursor, Windsurf, Claude Desktop, Claude.ai with file access, ChatGPT Projects, Gemini, or anything else that lets an AI read local markdown files.

## Quick start

You just got this folder (cloned the repo, downloaded a zip, or someone shared it with you). Here is how to use it.

### 1. Open the folder in your AI environment

The folder is plain markdown. Any environment where your AI assistant can read local files works:

- **Claude Code** (CLI) — `cd` into the folder and start a session
- **Claude Desktop** — drag the folder into a project
- **ChatGPT / Gemini / other web UIs** — upload the folder or its files to a project
- **VS Code / Cursor / Windsurf / Zed** — open the folder; use the AI side-panel
- **Obsidian** — open the folder as a vault; install the Spaced Repetition and Bases plugins for the full experience

### 2. Tell the AI to bootstrap

In your first message, say something like:

> **"Read `AI-BOOTSTRAP.md` and help me set up a new subject I want to learn."**

Or, if you already have a subject set up:

> **"Read `AI-BOOTSTRAP.md` and let's continue my [subject] study."**

The AI reads the bootstrap file, then the rest of the teaching engine, then either walks you through setting up a brand-new subject (the "cartridging" flow) or picks up your existing study where you left off.

### 3. Have a conversation

Plain language. As specific or vague as you want to be. The AI asks the questions it needs to design your curriculum, runs the first session, and writes everything to disk.

You do not need to learn the system. `AI-BOOTSTRAP.md` is the AI's reading list, not yours.

For environment setup details, see [`INSTALL.md`](INSTALL.md).

## System requirements

- **AI assistant** — any model capable of reading markdown and parsing YAML frontmatter (Claude Sonnet/Opus class, GPT-4 class and above)
- **OS** — Mac, Windows, or Linux
- **Editor / environment** — anything that gives an AI read/write access to a local folder. Obsidian recommended but not required.
- **Spaced repetition tool** — optional. **Anki** has a first-class, dependency-free integration (plain-text import that works from any AI, plus optional live two-way sync via the AnkiConnect add-on; review anywhere it syncs to via AnkiWeb) — see `_teaching-engine/_meta/SR-CONVENTIONS.md § "Anki integration"`. Also supported: Obsidian SR plugin, Mochi, RemNote, or none at all (the system falls back to Socratic-only quizzing).
- **Python** — not needed for core study (sessions, Units, synthesis, Socratic quizzing are pure markdown). *Optional:* if you choose **Anki** for spaced repetition and want one-command live sync, the OV bundles a Python 3 **standard-library-only** helper (`_teaching-engine/_scripts/anki_sync.py`) — nothing to `pip install`, and there's a no-script TSV-import fallback if you'd rather not run it.
- **Network** — none for core study; nothing is fetched at runtime. The optional Anki live-sync helper talks only to Anki running on your own machine (`localhost`).

## Which file do I read?

There are eight top-level files in this folder. Each has a distinct audience:

- **You want to use the system:** read this `README.md`, then [`INSTALL.md`](INSTALL.md) for setup. After that, point any AI at the folder and say *"read `AI-BOOTSTRAP.md` and help me set up a new subject."*
- **You want to operate the system day-to-day:** read [`OPERATOR-GUIDE.md`](OPERATOR-GUIDE.md) — common failure modes, how to fix a corrupted state file, how to migrate cartridges between machines.
- **You want to extend or modify the engine:** read [`CONTRIBUTING.md`](CONTRIBUTING.md) — what changes are in-scope vs. require a version bump.
- **You need version info:** [`VERSION.md`](VERSION.md) and [`CHANGELOG.md`](CHANGELOG.md).
- **You're the AI on session boot:** [`AI-BOOTSTRAP.md`](AI-BOOTSTRAP.md).
- **License:** [`LICENSE.md`](LICENSE.md) — CC-BY 4.0.

Optional: copy `_USER.md.template` to `_USER.md` and fill it in if you want global personalization (name, communication preferences) the AI applies across every subject.

## Folder structure

| Folder / file                       | Contents                                                                  |
|-------------------------------------|---------------------------------------------------------------------------|
| `AI-BOOTSTRAP.md`                   | AI entry point — the file the AI reads first                              |
| `README.md`                         | This file                                                                 |
| `INSTALL.md`                        | Setup instructions                                                        |
| `OPERATOR-GUIDE.md`                 | Day-to-day operation and troubleshooting                                  |
| `CONTRIBUTING.md`                   | How to extend the engine or share improvements back                       |
| `VERSION.md` / `CHANGELOG.md`       | Release metadata and history                                              |
| `LICENSE.md`                        | CC-BY 4.0                                                                 |
| `_USER.md.template`                 | Optional user-profile template (copy to `_USER.md` and fill in)           |
| `_teaching-engine/`                 | Subject-agnostic AI operating manual                                      |
| `_teaching-engine/_templates/`      | Note templates inherited by every cartridge                               |
| `_teaching-engine/_meta/`           | Schema-of-schemas + SR conventions                                        |
| `_Inbox/`                           | Un-homed capture pen — fleeting notes not yet tied to a subject (see its README) |
| `<Subject>/`                        | A cartridge — one folder per topic you're studying                        |
| `Example-Subject-Roman-Empire/`     | A worked example cartridge for "The Rise and Fall of the Roman Empire"    |

Each cartridge contains: `_subject.md`, `_schema.md`, `_curriculum.md`, `_state.md`, `Units/`, `Sources/`, `Sessions/`, `Quizzes/`, `Synthesis/`, `SR-Cards/`, `Captures/`. Fleeting notes are captured as `LLL_Note` items — subject-homed ones in the cartridge's `Captures/`, un-homed or cross-cutting ones in the OV-root `_Inbox/` — and drained into Units by the TRIAGE session activity.

## Where to go for what

| If you want to…                                          | Read…                                                              |
|----------------------------------------------------------|--------------------------------------------------------------------|
| Set up a brand new topic                                 | Tell the AI: *"Read `AI-BOOTSTRAP.md` and set up a new subject."*  |
| Continue an existing subject                             | Tell the AI: *"Read `AI-BOOTSTRAP.md` and continue my [X] study."* |
| Understand how the AI runs a session                     | `_teaching-engine/01-SESSION-PROTOCOL.md`                          |
| Understand the pedagogy                                  | `_teaching-engine/02-PEDAGOGY.md`                                  |
| Understand how cartridges are designed                   | `_teaching-engine/03-SCHEMA-DESIGN.md`                             |
| See a worked-out cartridge                               | `Example-Subject-Roman-Empire/`                                    |
| Troubleshoot a stuck session or corrupted state          | `OPERATOR-GUIDE.md`                                                |
| Propose improvements                                     | `CONTRIBUTING.md`                                                  |

## Versioning

- **Software version** — see [`VERSION.md`](VERSION.md) and [`CHANGELOG.md`](CHANGELOG.md). Initial public release is v1.0.0.
- **Schema** — the `LLL_*` types defined in `_teaching-engine/_meta/SCHEMA-OF-SCHEMAS.md` are the contract every cartridge conforms to. Breaking changes require a major version bump.
- **Cartridges you create** are yours and travel with you across versions. Future versions will provide migration notes if cartridge format changes.

## License

LifeLong Learning is released under the **Creative Commons Attribution 4.0 International License (CC-BY 4.0)**. You are free to share, adapt, and build upon this material for any purpose — including commercially — provided you give appropriate attribution.

See [`LICENSE.md`](LICENSE.md) for the full license text. Attribution format:

> Built on **LifeLong Learning v1.0** by Jawn Lam — https://github.com/JawnLam/LifeLong-Learning
> Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Version

See [`VERSION.md`](VERSION.md). This is the **v1.0.0 initial public release**.
