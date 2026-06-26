# LifeLong Learning — Operator Guide

This guide is for the human running LifeLong Learning day-to-day: how sessions actually work, common failure modes, how to recover, and how to keep your cartridges healthy over months and years of study.

If you're setting up for the first time, read [`INSTALL.md`](INSTALL.md) first.

---

## 1. How a session actually works

A session has nine phases. The AI runs through all of them; you only experience the parts where you talk.

1. **READ** — AI reads the teaching engine, your `_USER.md` (if present), and the active subject's `_subject.md`, `_schema.md`, `_state.md`, recent session logs, and weak Units.
2. **DIAGNOSE** — AI inspects state for hard overrides, weak Units, cadence rhythms.
3. **PROPOSE** — AI proposes an activity (TEACH / QUIZ-SR / QUIZ-SOCRATIC / REVIEW-WEAK / SYNTHESIZE / INTEGRATE) with rationale.
4. **WAIT** — AI waits for your confirmation or override.
5. **EXECUTE** — the actual conversation happens here.
6. **CAPTURE** — AI records Unit mastery changes, quiz results, synthesis artifacts.
7. **WRITE session log** — new file in `<Subject>/Sessions/`.
8. **UPDATE `_state.md`** — overwritten with new state.
9. **END with Open Threads** — explicit seed for the next session.

If a session ends without phases 6–9, the session is incomplete. Tell the AI to finish.

## 2. Reading the state file

`<Subject>/_state.md` is the single source of truth. Useful sections:

- **Current Position** — which phase you're in and where you are inside it
- **Unit Mastery Snapshot** — every Unit's mastery level (0–5)
- **Weak Units** — Units flagged for re-teaching
- **Recent Sessions** — pointers to recent session logs
- **Phase Exit Checklist** — what you need to demonstrate to leave the current phase
- **Open Threads** — what next session is supposed to address

If you ever want to know "where am I in this subject?", read this file. The AI reads it at the start of every session.

## 3. Common failure modes and how to fix them

### The AI starts teaching without reading the engine

**Symptom:** the AI's first response is a long explanation, a generic greeting, or jumps straight into content without acknowledging your state.

**Fix:** stop the session and say *"Read `AI-BOOTSTRAP.md` in full before responding."* Restart.

### The AI invents books, thinkers, or facts

**Symptom:** you notice a citation that looks suspicious — a book title that doesn't quite ring true, a date that seems off, a thinker you've never heard of.

**Fix:** verify the citation against a real source. If it's fabricated, tell the AI: *"That citation is wrong. Remove it from the Unit and the source list. From now on, if you're not sure something is real, say so."* The fabrication discipline is in `_teaching-engine/02-PEDAGOGY.md` and `BOOTSTRAP-NEW-SUBJECT.md` — refresh the AI on it if it keeps happening.

**Prevention:** when cartridging a new subject, ask the AI to flag any source it isn't 100% sure exists. Verify the first few before trusting the rest.

### The AI dumps a multi-bullet questionnaire

**Symptom:** during cartridging, the AI sends a single message with eight or nine questions in a list. You answer them all, the AI builds something that doesn't quite fit, and you realize halfway through it didn't really hear you.

**Fix:** stop. Say *"Ask me one question at a time, conversationally. Probe my answers. The protocol is conversation, not assignment."* Then start the cartridging over.

**Prevention:** the protocol in `BOOTSTRAP-NEW-SUBJECT.md` already says this, but some models default to bulk-questioning anyway. Watch for it on the first message.

### `_state.md` is corrupted, missing, or contradictory

**Symptom:** the AI says it can't read your state, or it reads state that contradicts the session logs.

**Fix:**
1. Open the most recent session log in `<Subject>/Sessions/`.
2. Look at the "Units Updated," "Open Threads for Next Session," and other concrete sections.
3. Reconstruct `_state.md` from the session log using `_teaching-engine/_templates/TEMPLATE-State.md`.
4. If multiple sessions back are unrecoverable, you may need to manually walk through Unit files and check `lll_Mastery` to rebuild the snapshot.

Unit files themselves are usually the more durable record, since they accumulate over time. The state file is a rollup.

### The AI mixes subjects mid-session

**Symptom:** you started a session on one subject, then started talking about another, and the AI followed without closing out the first session properly.

**Fix:** ask the AI to close out the original session (write its log, update state) before starting the new one. The protocol forbids mid-session subject switching for this reason.

### Sessions stop producing files

**Symptom:** the AI seems engaged but nothing is appearing in the `Sessions/` folder.

**Fix:** check whether your environment is read-only (some sandboxes, web-only AI environments). If yes, the AI should declare sandbox mode and tell you state is inline. If no, the AI is failing to follow the protocol — remind it: *"Write the session log to disk now. Then update `_state.md`."*

### Units drift away from their schema

**Symptom:** Units you wrote weeks ago have different frontmatter than newer ones, or sections are missing.

**Fix:** ask the AI: *"Audit the cartridge against `_schema.md`. List any Units with non-conforming frontmatter or missing sections."* Then ask it to fix them one at a time, with your approval.

## 4. Cartridge health over time

A cartridge can degrade silently over months. Periodic check:

- **Every ~10 sessions:** ask the AI to do an INTEGRATE session — cross-Unit connection mapping. This surfaces Units that have drifted apart from each other.
- **Every phase exit:** the AI runs the phase-exit protocol (demonstrate each criterion in your own words). This is the gate.
- **Every ~25 sessions:** ask the AI to audit the cartridge against its schema.
- **Every quarter:** produce a quarterly draft synthesis (`SYNTHESIZE` activity, quarterly kind). Writing for an external reader exposes thinness.

## 5. Sharing or transporting a cartridge

A cartridge is a self-contained folder. To share or move:

- **Zip the `<Subject>/` folder.** That's it.
- The recipient drops it into their own `LifeLong Learning/` directory.
- Cartridges are user-specific (the `lll_User_Goals` and `lll_User_Prior_Knowledge` fields encode the original learner's situation). The recipient should edit `_subject.md` to reflect their own goals before studying, or treat it as a curriculum reference rather than a personal cartridge.

## 6. Multiple subjects in parallel

There's no limit. You can have ten subjects in your `LifeLong Learning/` folder; each has its own state, sessions, Units, and pacing. When starting a session, name the subject in your first message so the AI knows which cartridge to load.

If you're studying multiple related subjects (e.g., Roman Empire + Late Antiquity + Byzantine Empire), consider whether they should be one cartridge with multi-phase scope or separate cartridges with cross-links. The bootstrap protocol's Q1 ("subject name, stated precisely") helps decide.

## 7. When something breaks and you can't fix it

- Open `CONTRIBUTING.md` and see if your case is a bug worth reporting upstream.
- If it's a one-off (your cartridge is wedged, your state file is broken): copy the cartridge folder, delete the broken pieces, restore from session logs as described in §3.
- Worst case: archive the cartridge as `99-Archive-<Subject>/`, bootstrap a fresh one with the AI, and import any Units worth keeping by hand.

## 8. Versioning your study work

Decisions to make at install time:

- **Version control?** The canonical install pattern is a `git clone` with push disabled (see `INSTALL.md § 1`). The shipped `.gitignore` excludes session/quiz/state files by default (so you can share the engine without leaking personal study). If you want to track your own study history privately, edit `.gitignore` to remove those exclusions before your first commit.
- **Cloud sync?** Dropbox / iCloud / OneDrive / Google Drive all work. Sync gives you cross-device continuity at the cost of some conflict risk if you start the same session on two machines.
- **Backups?** Treat your `LifeLong Learning/` folder as you'd treat any irreplaceable personal work. Years of study history live in those markdown files.

## 9. Engine vs your work — the four content zones (OVE Convention 8)

Your installed LLL folder has four content zones. Knowing which is which prevents the operator-pulls-and-loses-work failure mode.

### Engine Zone — release-owned; updated by `git pull`

The files that LLL's release ships:

- Front-door docs: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md`
- `_teaching-engine/` — engine chapters, templates, meta
- `_types/` — LLL's own Prototype definitions
- `_USER.md.template` — the template, not the populated `_USER.md`
- `.gitignore` — engine-zone file

**Do not edit Engine Zone files directly.** Updates from `git pull` overwrite them. Customizations belong in Operator-Extension Zone cartridges or in per-subject configuration (`_schema.md`, `_curriculum.md`, `_subject.md`).

### Operator-Private Zone — gitignored; never tracked

The `.gitignore` excludes:

- Your operator profile (`_USER.md`)
- Per-subject state (`<Subject>/_state.md`), identity (`<Subject>/_subject.md`)
- Session logs (`<Subject>/Sessions/*.md`), Socratic-conceptual quizzes
- SR performance logs (`<Subject>/Quizzes/SR-Performance-Log/*.md`)
- Synthesis drafts (weekly journals, monthly essays, phase-end translations, quarterly drafts)
- SR-card files

These never get pushed and never get touched by `git pull`. The `!Example-Subject-*/...` overrides re-include the worked example's bootstrap session log and `_state.md` (Shipped Examples Zone).

### Operator-Extension Zone — your subject cartridges; survives `git pull`

This is where your work lives. Every subject you bootstrap through LLL becomes a folder at the LLL root.

`<Subject>/` folders that aren't named `Example-Subject-*` are not in LLL's release, so `git pull` never touches them. They're yours.

### Shipped Examples Zone — release-owned; updated by `git pull`

The one worked-example subject that demonstrates LLL:

- `Example-Subject-Roman-Empire/` — "The Rise and Fall of the Roman Empire"

**Do not edit Shipped Examples directly.** If you want to riff on the example, copy it into an Extension Zone cartridge (`cp -r Example-Subject-Roman-Empire My-Roman-Study`) and customize there.

## 10. Updates and troubleshooting

The canonical update workflow lives in `INSTALL.md § 8`. Common scenarios:

### Clean fast-forward (no local engine modifications)

```bash
cd ~/Operating-Volumes/LifeLong-Learning-v<your-major>.<minor>
git fetch origin
git log --oneline HEAD..origin/main          # what's incoming
git pull --ff-only origin main
```

### Fast-forward fails because you have local engine modifications

```bash
git status                                    # see what's modified
git stash push --include-untracked -m "pre-update state"
git pull --ff-only origin main
git stash pop                                 # may produce conflicts on engine files you edited
```

If `git stash pop` reports conflicts, the conflict is between *your local edit* of an engine file and *the upstream release's version*. You almost always want the upstream version (engine evolution generally improves what's there):

```bash
git checkout --theirs <conflicting-file>
git add <conflicting-file>
# OR — abandon your local edits entirely:
git checkout origin/main -- <conflicting-file>
```

If your local edit was load-bearing, copy it to a side file before checkout, then reconcile.

### Update lost a file you cared about

`git pull` only updates tracked paths. If a file disappeared, either: (a) the release explicitly removed it (the `CHANGELOG.md` will say so), or (b) it was a gitignored file you forgot was ignored. For (a), the file is recoverable via `git log --all --oneline -- <path>`. For (b), check whether the file matched a `.gitignore` pattern.

### Major.minor folder transition

When the release notes say to rename your folder:

```bash
cd ~/Operating-Volumes/
mv LifeLong-Learning-v<old> LifeLong-Learning-v<new>
cd LifeLong-Learning-v<new>
git status   # should show clean
```

The folder rename doesn't affect git; the rename is for your filesystem clarity.

### Contributing back upstream

To contribute back (open a PR against the upstream LLL), re-enable push to *your own fork* (never to upstream):

```bash
# Replace with your fork's URL
git remote set-url --push origin https://github.com/<your-username>/LifeLong-Learning.git

# Make a branch, commit, push to your fork, open a PR on GitHub
git checkout -b my-contribution
# ... your changes ...
git commit -m "..."
git push origin my-contribution
```

When you're done contributing, re-disable push to protect your private study work going forward:

```bash
git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK
```

## Version

This operator guide ships with LifeLong Learning v1.3.0. See `VERSION.md`.
