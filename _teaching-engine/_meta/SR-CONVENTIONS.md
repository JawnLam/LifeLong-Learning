---
type: teaching-engine
role: sr-plugin-conventions
scope: subject-agnostic
updated: 2026-05-31
---

# SR Card Conventions

Every cartridge can use spaced repetition. The assistant generates cards embedded in atom notes (or in dedicated SR-card files), the user's SR tool handles all scheduling, and the assistant logs performance in a per-phase SR log.

Supported SR tools include the Obsidian **Spaced Repetition** plugin, Anki (with `apkg` export or via plugins), Mochi, RemNote, or any other SR tool the user prefers. The card syntax below targets the Obsidian SR plugin; for other tools, adapt the syntax to match.

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

Each atom note has a `## Quiz Bank` section. When the assistant promotes a quiz-bank question into an SR card, it moves the question into an embedded cards section at the bottom of the note. The plugin picks up all cards in any note in the vault.

Optionally, all SR cards can live in a dedicated file per atom in `<Subject>/SR-Cards/`, but embedding in the atom is preferred — keeps context next to the card.

## Card generation rules

- **No cards for atoms at mastery 0 or 1.** Premature cards train recall of words, not understanding. Wait until mastery 2.
- **Create 2–5 cards per atom**, varying in form:
  - One definitional (recall)
  - One application (transfer)
  - One counter-example / boundary (sharpen)
  - Optional: one connection
  - Metacognitive questions are poor SR cards — keep them for Socratic quizzes
- **Update `lll_SR_Cards_Created` in atom frontmatter** whenever cards are added.

## Card quality standards

- Answerable in one to three sentences
- Answers unambiguous
- Test understanding, not trivia (dates, page numbers, biographical minutiae)
- If a card has failed (`again`) twice in its last three reviews, the atom gets flagged `lll_Status: weak` in `_state.md`

## Performance logging

After SR quizzing, the assistant appends rows to `<Subject>/Quizzes/SR-Performance-Log/Phase-<N>-SR-Log.md`. Separate from the plugin's own records so performance can be queried across atoms and sessions without plugin-specific tooling.

## Subject-specific card forms

Some subjects benefit from non-standard card formats:

- **Language subjects:** image-to-word, audio-to-word cards (if the user's SR tool supports audio; otherwise note audio-associated terms in card text)
- **Music theory:** notation or interval cards — may use image attachments
- **Cuisine:** ingredient identification, dish component recall
- **Math:** proof-step cards, definition cards
- **History:** chronology cards, cause-effect cards, "what changed?" cards

If a subject needs non-text cards, document the approach in `<Subject>/_schema.md` under "SR adaptations."

## If the user is not using an SR tool

SR is optional. If the user doesn't have an SR tool configured, fall back to Socratic quizzing only. The QUIZ-SR activity is skipped in the session protocol; the QUIZ-SOCRATIC activity continues to apply.
