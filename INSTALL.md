# LifeLong Learning — Install Guide

This is the step-by-step setup for a fresh installation. Once setup is complete, you only ever need `README.md` + `AI-BOOTSTRAP.md` — the AI handles everything else at runtime.

## 1. Install (recommended: git clone with push disabled)

This is the **canonical install pattern per OVE Convention 7** — git-tracked so you can `git pull` future releases; push disabled so you can't accidentally upload your private study work.

```bash
# Choose a parent folder. Anything works — Dropbox-synced, iCloud-synced, Obsidian vault, etc.
mkdir -p ~/Operating-Volumes
cd ~/Operating-Volumes

# Clone into a folder named with the current major.minor.
# (Check VERSION.md or the GitHub releases page for the current version.)
git clone https://github.com/JawnLam/LifeLong-Learning.git \
  LifeLong-Learning-v1.3

# Disable push remote — protects your study work against accidental upload.
cd LifeLong-Learning-v1.3
git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK

# Verify
git remote -v
# Expect: origin fetch URL real; origin push URL = DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK
```

**Why the folder name has a version suffix.** The convention is `LifeLong-Learning-v<major>.<minor>`. When a new major.minor ships (e.g., v1.4), `OPERATOR-GUIDE.md § Updates` walks you through renaming the folder so old and new can briefly coexist during the transition.

**Why push is disabled.** Almost everything you do in this folder beyond reading the engine is private study work — your Units, your Quizzes, your Synthesis pieces, your SR Logs, your session histories. The push-disabled default prevents the worst-case operator-error: `git push` accidentally uploading your in-progress study to the public LLL repo. You can re-enable push to your own fork if you want to contribute back upstream (see `OPERATOR-GUIDE.md § Contributing back`).

## 1a. Alternative install (no git tracking)

If you don't want git tracking — you'd rather treat this as a snapshot reference, no updates — you can also just download the folder:

- **Plain copy:** Download a release ZIP from the GitHub releases page; unzip anywhere your AI assistant can read.
- **Cloud-synced folder** (Dropbox, iCloud, OneDrive, Google Drive) — convenient if you want the same vault available across devices.
- **Obsidian vault** — recommended for the full experience with Spaced Repetition cards and Bases queries.
- **Plain local folder** — works for any AI environment that supports file-attachment uploads.

The folder is fully self-contained. No network fetch happens at runtime; no paths are hard-coded. The trade-off versus the git-tracked install: you don't get `git pull` updates — you have to re-download each release.

## 2. (Optional) Configure your user profile

If you want consistent personalization across every subject you study, copy the template:

```
cp _USER.md.template _USER.md
```

Open `_USER.md` and fill in your name, your default communication preferences, and any global notes you want every AI session to know. This file is read at the start of every session. It's optional — without it, the system uses sensible defaults (peer register, direct, substantive critique, minimal hedging).

## 3. (Optional) Configure Obsidian plugins

If you're using Obsidian as your editor, two plugins make the experience richer:

- **Spaced Repetition** (community plugin) — picks up `:: ` and `:::` syntax in any note to drive spaced-repetition review.
- **Bases** (core plugin, v1.9+) — database-like views of notes via YAML frontmatter properties; useful for Unit dashboards.

Neither is required. The system works without them — Bases just gives you nicer browsing, and SR can be replaced with Anki, Mochi, RemNote, or skipped entirely (the AI falls back to Socratic quizzing).

## 4. (Optional) Initialize git

If you want version control on your study work (recommended):

```
cd "LifeLong Learning"
git init
git add .
git commit -m "Initial install of LifeLong Learning"
```

The shipped `.gitignore` excludes session-private files (sessions, quizzes, synthesis drafts, state files) by default so the repo can be shared without leaking personal study notes. If you want your own private study history version-controlled, edit `.gitignore` to remove those exclusions before your first commit.

## 5. First session walkthrough

1. **Open the folder in your AI environment.** Point Claude Code / Claude Desktop / ChatGPT / Cursor / Obsidian + Copilot / your IDE-integrated agent at the folder.

2. **Trigger the AI bootstrap.** Send the AI a single message:

   > Read `AI-BOOTSTRAP.md` and help me set up a new subject I want to learn.

   Or, if you already have a subject set up:

   > Read `AI-BOOTSTRAP.md` and let's continue my [subject] study.

3. **Wait for the readiness statement.** The AI's first response should be a short paragraph confirming it has read the teaching engine, plus either a clarifying question (if you're cartridging a new subject) or a proposed session activity (if you're continuing an existing one).

   If the AI responds with anything else — a long explanation of the system, an unrequested summary, a generic greeting — it has skipped Phase 0. Tell it explicitly: *"Read `AI-BOOTSTRAP.md` in full before responding."*

4. **Have the conversation.** From here the AI guides you. You don't need to know which file it's reading or which activity it picked; that's the AI's job.

## 6. Migrating between machines

A LifeLong Learning vault is just markdown files. To move it:

- **Sync folder (Dropbox/iCloud/etc.):** changes propagate automatically. You can start a session on one machine and finish it on another.
- **Manual:** copy the folder. Cartridges work identically on a new machine.
- **Git:** clone the repo. If you've kept your study work in git, your full session history travels with you.

## 7. Troubleshooting

| Symptom                                                | Likely cause / resolution                                                                                                                          |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| AI never produces a readiness statement                | It probably didn't read `AI-BOOTSTRAP.md`. Re-send the bootstrap message explicitly: *"Read `AI-BOOTSTRAP.md` in full before responding."*           |
| AI starts a session but doesn't write anything to disk | It may be in a sandbox / read-only environment. Tell it to write to the folder, or accept sandbox mode (state lives inline in the conversation).    |
| `_state.md` is missing or corrupted for a subject      | See `OPERATOR-GUIDE.md` — "Recovering a corrupted state file."                                                                                       |
| AI invents books or thinkers that don't exist          | Stop the session, correct the AI, regenerate the affected Units. See `OPERATOR-GUIDE.md` — "Detecting and removing fabrications."                  |
| Obsidian SR plugin not detecting cards                 | Confirm card syntax is `::` (one-line) or `?` on its own line (multi-line). See `_teaching-engine/_meta/SR-CONVENTIONS.md`.                          |
| Want to share a cartridge with someone                 | Zip the `<Subject>/` folder; recipient drops it into their own LifeLong Learning vault.                                                              |

For deeper operational guidance, see `OPERATOR-GUIDE.md`. To extend the system, see `CONTRIBUTING.md`.

## 8. Updating (when a new release ships)

When LLL ships a new release on GitHub (announced in `CHANGELOG.md`):

```bash
cd ~/Operating-Volumes/LifeLong-Learning-v<your-current-major>.<minor>

git fetch origin
git log --oneline HEAD..origin/main           # preview what's incoming

# If you have no local engine modifications: clean fast-forward
git pull --ff-only origin main

# If you have local engine modifications: stash → pull → pop
git stash push --include-untracked -m "pre-update state"
git pull --ff-only origin main
git stash pop                                  # resolve any conflicts
```

**When major.minor changes (e.g., v1.3 → v1.4 ships):**

```bash
cd ~/Operating-Volumes/
mv LifeLong-Learning-v1.3 LifeLong-Learning-v1.4
```

The CHANGELOG entry for the new major.minor will tell you whether folder rename is recommended or required. For pure-patch releases (e.g., v1.3.0 → v1.3.1), no folder rename is needed.

For troubleshooting common update issues (fast-forward conflicts, stash-pop merge conflicts, dirty working tree blocking pull), see `OPERATOR-GUIDE.md § Updates and troubleshooting`.

## Version

This install guide ships with LifeLong Learning v1.3.0. See `VERSION.md` for full release metadata.
