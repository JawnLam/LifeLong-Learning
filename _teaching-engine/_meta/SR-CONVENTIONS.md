---
type: teaching-engine
role: sr-plugin-conventions
scope: subject-agnostic
updated: 2026-05-31
---

# SR Card Conventions

Every cartridge can use spaced repetition. The assistant generates cards embedded in Unit notes (or in dedicated SR-card files), the user's SR tool handles all scheduling, and the assistant logs performance in a per-phase SR log.

Supported SR tools include the Obsidian **Spaced Repetition** plugin, **Anki** (first-class — see "Anki integration" below), Mochi, RemNote, or any other SR tool the user prefers. The card syntax immediately below targets the Obsidian SR plugin; for other tools, adapt the syntax to match. **Anki has a dedicated, dependency-free integration contract documented in its own section further down** — a plain-text import path that works from any AI substrate, plus an optional live AnkiConnect path for two-way sync.

## Choosing and setting up an SR backend

**SR is opt-in and is chosen once, then toggled per subject.** The very first subject bootstrap asks the user whether they want spaced repetition and which backend (BOOTSTRAP-NEW-SUBJECT Q10); the answer is recorded globally in `{ROOT}/_USER.md` (Learning preferences) so later subjects inherit it. Each subject then carries `lll_SR_Enabled: true|false` in its `_subject.md`. If no backend is recorded and none is chosen, skip SR entirely and fall back to Socratic quizzing (see the last section).

When the user picks a backend they haven't installed, **guide them through the one-time setup before continuing the bootstrap.** Walk it step by step; stop and confirm at each step; don't assume anything is already in place.

### Option 1 — Anki (recommended)

Best if the user wants review on phone/web as well as desktop, and the tightest automation (one-command push + two-way stat sync). Full contract in "Anki integration" below. One-time setup:

1. **Install Anki desktop** (macOS: `brew install --cask anki`, or download from `https://apps.ankiweb.net/`). Launch it once to create the profile.
2. **Install the AnkiConnect add-on** (only needed for the live/two-way path): in Anki → Tools → Add-ons → Get Add-ons → paste `2055492159` → OK → **restart Anki**. Verify with the OV's built-in tool: `python3 _teaching-engine/_scripts/anki_sync.py verify`.
3. **AnkiWeb sync** (for phone/browser review): click Sync, create/log into a free AnkiWeb account. Cards pushed to desktop reach every device after a sync.

If the environment can't run a local API (no shell, or Anki not on this machine), the user can still use the **dependency-free TSV path**: the assistant writes `anki-export.tsv` and the user does File → Import. No add-on required.

### Option 2 — Obsidian Spaced Repetition plugin

Best if the user lives in Obsidian and wants cards in-vault with no extra app. One-time setup:

1. In Obsidian → Settings → **Community plugins** → **Browse** → search "**Spaced Repetition**" → **Install** → **Enable**.
2. (Optional) In the plugin settings, set the review tag/folder scope; the defaults pick up all cards in the vault.
3. Cards use the `::` / `:::` / multi-line syntax documented immediately below, embedded in Unit notes.

### Option 3 — Another tool (Mochi, RemNote, etc.)

Record the tool in `_USER.md`. Generate cards in the tool's import format (most accept the Anki-style TSV or a simple Q/A text). The assistant adapts the card syntax; scheduling and review happen in that tool.

### Option 4 — None

Fully valid. Set `lll_SR_Enabled: false`; the QUIZ-SR activity is skipped and QUIZ-SOCRATIC carries the review load. The user can turn SR on later by choosing a backend and flipping `lll_SR_Enabled`.

## Card syntax (Obsidian SR plugin)

### One-line (basic)

```
What is requisite variety::Only variety can destroy variety — a regulator must have at least as much variety as the disturbance it regulates.
```

### Multi-line (longer answer)

```
Longer question here
?
Longer answer here, possibly spanning multiple sentences and paragraphs.
```

### Reversed (bidirectional)

```
Good Regulator Theorem:::Every good regulator of a system must be a model of that system.
```

Three colons `:::` creates a bidirectional card.

## Where cards live

Each Unit note has a `## Quiz Bank` section. When the assistant promotes a quiz-bank question into an SR card, it moves the question into an embedded cards section at the bottom of the note. The plugin picks up all cards in any note in the vault.

Optionally, all SR cards can live in a dedicated file per Unit in `<Subject>/SR-Cards/`, but embedding in the Unit is preferred — keeps context next to the card.

## Card generation rules

- **No cards for Units at mastery 0 or 1.** Premature cards train recall of words, not understanding. Wait until mastery 2.
- **Create 2–5 cards per Unit**, varying in form:
  - One definitional (recall)
  - One application (transfer)
  - One counter-example / boundary (sharpen)
  - Optional: one connection
  - Metacognitive questions are poor SR cards — keep them for Socratic quizzes
- **Update `lll_SR_Cards_Created` in Unit frontmatter** whenever cards are added.

## Card quality standards

- Answerable in one to three sentences
- Answers unambiguous
- Test understanding, not trivia (dates, page numbers, biographical minutiae)
- If a card has failed (`again`) twice in its last three reviews, the Unit gets flagged `lll_Status: weak` in `_state.md`

## Performance logging

After SR quizzing, the assistant appends rows to `<Subject>/Quizzes/SR-Performance-Log/Phase-<N>-SR-Log.md`. Separate from the plugin's own records so performance can be queried across Units and sessions without plugin-specific tooling.

## Subject-specific card forms

Some subjects benefit from non-standard card formats:

- **Language subjects:** image-to-word, audio-to-word cards (if the user's SR tool supports audio; otherwise note audio-associated terms in card text)
- **Music theory:** notation or interval cards — may use image attachments
- **Cuisine:** ingredient identification, dish component recall
- **Math:** proof-step cards, definition cards
- **History:** chronology cards, cause-effect cards, "what changed?" cards

If a subject needs non-text cards, document the approach in `<Subject>/_schema.md` under "SR adaptations."

## Anki integration (desktop + AnkiConnect + AnkiWeb)

Anki is a first-class SR backend. There is **no public write API for AnkiWeb** — you never push to ankiweb.net directly. The flow is always: get cards into an Anki client → the client syncs to AnkiWeb → review anywhere (desktop, mobile, browser). LLL therefore defines a stable *export contract* (how a Unit's cards map to Anki), and offers two ways to move cards across that contract.

### The two paths

- **Path A — plain-text (TSV) import.** Zero-dependency and substrate-agnostic: the assistant writes a tab-separated file with Anki's header directives; the user does **File → Import** once, and every later import updates in place. Works from any AI (Claude, ChatGPT, Gemini) because it is just a text file. This is the portable default and the fallback whenever a live connection isn't available.
- **Path B — AnkiConnect (live, two-way).** With Anki desktop running and the [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on installed (code `2055492159`), cards are pushed directly and review performance pulled back — the low-friction path, and the only one that supports two-way sync. **This is built into the OV**: the bundled `_teaching-engine/_scripts/anki_sync.py` (Python 3 stdlib, nothing to install) does it. Any assistant running LLL with shell access can invoke it; **no separate "skill" or special setup is required.** If the AI has no shell, or AnkiConnect isn't installed, fall back to Path A.

Both paths use the **same identity, deck, tag, and notetype contract** below, so a subject can move between them freely.

### The contract

**Card identity (idempotency key) — deterministic, so re-export updates instead of duplicating:**

```
lll-id::<subject-slug>::<unit-id>::<card-index>
```

`<card-index>` is the card's 1-based position within its Unit's `## Quiz Bank` / embedded cards, in file order. The key is derived from stable inputs, so nothing needs to be stored — regenerating a subject's cards always yields the same keys. Carried as the Anki note **GUID** in Path A (`#guid column:`) and as an Anki **tag** in Path B (`findNotes` matches it to decide add-vs-update). One string, two carriers.

**Deck:** `LLL::<Subject>` (Anki `::` = subdeck). One deck per subject; phases are tags, not subdecks, so cards don't migrate decks as phases advance. A subject may override its deck name in `_subject.md` (documented convention; no schema field needed).

**Notetypes:** built-in only — **Basic** (Front/Back) for one-line and multi-line cards; **Basic (and reversed card)** for bidirectional (`:::`) cards. Nothing to install.

**Tags (organizational, hierarchical):**

```
lll::subject::<subject-slug>
lll::phase::<n>
lll::unit::<unit-slug>
lll::kind::<recall|application|boundary|connection>
```

plus the identity tag `lll-id::<subject-slug>::<unit-id>::<card-index>` — **always included in the tags column**, so a single exported file serves both paths (Path A also copies it into the guid column; Path B matches on it).

### Path A — TSV file format

Regenerate to `<Subject>/SR-Cards/anki-export.tsv` (operator-private; gitignored). Column order: 1 notetype, 2 deck, 3 Front, 4 Back, 5 tags (space-separated), 6 guid.

```
#separator:tab
#html:true
#notetype column:1
#deck column:2
#tags column:5
#guid column:6
Basic	LLL::Roman Empire	What did the cursus honorum constrain?	The sequence and minimum ages of Roman magistracies — structuring political careers and making certain conflicts unavoidable.	lll::subject::roman-empire lll::phase::1 lll::unit::cursus-honorum lll::kind::recall lll-id::roman-empire::cursus-honorum::1	lll-id::roman-empire::cursus-honorum::1
```

Import: **File → Import → select the file → "Notes" match by guid → Import**. Because guids are stable, re-importing an updated file edits the existing notes rather than adding duplicates. Then click **Sync** to push to AnkiWeb.

### Path B — AnkiConnect procedure (two-way)

**The OV ships a tool that does all of this — you normally just run it**, from the OV root:

```bash
python3 _teaching-engine/_scripts/anki_sync.py verify                                  # check the connection
python3 _teaching-engine/_scripts/anki_sync.py push --tsv "<Subject>/SR-Cards/anki-export.tsv"
python3 _teaching-engine/_scripts/anki_sync.py pull --deck "LLL::<Subject>"            # prints per-Unit stats as JSON
```

`push` is idempotent (re-running updates, never duplicates); `pull` prints JSON and does **not** write to the vault — the assistant takes that JSON and writes the SR-Log + reconciles `_state.md`. The mechanics the tool implements, for reference (or for a substrate re-implementing it): AnkiConnect listens on `http://127.0.0.1:8765`; every call is `POST {"action": ..., "version": 6, "params": {...}}`.

- **Push (add-or-update, idempotent):** for each card, `findNotes` with query `tag:lll-id::<key>`. If a note is returned → `updateNoteFields` (and reconcile tags). If not → `createDeck` (if needed) then `addNote` with the deck, notetype, Front/Back, and all tags including the identity tag. Never rely on `allowDuplicate`; the identity tag is the dedup mechanism.
- **Pull (review performance → SR-Log):** `findCards` with query `deck:"LLL::<Subject>"` (or `tag:lll::subject::<slug>`); `cardsInfo` for `interval`/`reps`/`lapses`/`factor`/`queue`/`due`; `getReviewsOfCards` for the recent per-review `ease` values (1 = again). Parse each note's `lll-id` tag to map back to its Unit, then:
  - append dated rows to `<Subject>/Quizzes/SR-Performance-Log/Phase-<N>-SR-Log.md`, and
  - apply the weak-Unit rule (an `again` twice in the last three reviews → set `lll_Status: weak` on the Unit and add it to Weak Units in `_state.md`).

This makes Anki the scheduling system of record while LLL stays the source of truth for *what* is learned and *which Units are weak* — the two-way loop keeps REVIEW-WEAK driven by real Anki data.

### How QUIZ-SR behaves when the tool is Anki

The QUIZ-SR activity (see `01-SESSION-PROTOCOL.md`) becomes: (1) **push** any new/changed cards for the active subject; (2) the user **reviews in Anki / AnkiWeb / mobile** (not inside the LLL session); (3) **pull** the results back into the SR-Log and reconcile weak-Unit flags. On Path A, steps 1 and 3 are the operator running an import/export; on Path B they are one `anki_sync.py` command each (`push`, then later `pull`).

## If the user is not using an SR tool

SR is optional and opt-in. If the subject has `lll_SR_Enabled: false` (or no SR backend is recorded in `_USER.md`), fall back to Socratic quizzing only: the QUIZ-SR activity is skipped in the session protocol; the QUIZ-SOCRATIC activity continues to apply. Never generate SR cards or an SR log for a subject that hasn't opted in.
