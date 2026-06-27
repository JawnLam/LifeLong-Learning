---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: type-lll-source
title: "LLL_Source Type"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LLL_Source` — Type Definition

> **What this file is.** The canonical definition of the `LLL_Source` Type for the LifeLong-Learning Operating Volume. Items in any subject cartridge that declare `type: LLL_Source` conform to the contract described below.

## Purpose

A Source is **any external material a learner engages with** in the course of studying a subject: book, paper, article, video series, podcast, lecture course, cooking class, recipe collection, language app, dataset, museum, etc. Sources are how a subject cartridge connects to the broader world of knowledge it is drawing on. Each Source Item tracks its role in the curriculum (primary, supplementary, reference, deep-dive, media), its kind, the learner's progress through it, the Units it introduces or deepens, and a post-engagement synthesis written when the learner finishes. Genre scope: every LLL subject cartridge. Created when the learner adds a new study source; never automatically.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LLL_Source` |
| `Item_ID` | string | yes | Lowercase kebab slug |
| `Title` | string | yes | Source title |
| `Date_Added` | date | yes | When the Source was added |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lll_Subject` | string | yes | Subject slug (e.g., `cybernetics`, `git-for-vibe-coding`, `roman-empire`) |
| `lll_Phase` | string | optional | Which curriculum phase the source belongs to |
| `lll_Source_Role` | enum | yes | `primary` \| `supplementary` \| `reference` \| `deep-dive` \| `media` |
| `lll_Source_Kind` | enum | yes | `book` \| `paper` \| `article` \| `video` \| `podcast` \| `course` \| `other` |
| `lll_Progress_Pct` | integer | yes | 0–100 |
| `lll_Estimated_Hours` | number | optional | Initial estimate of engagement time |
| `lll_Actual_Hours` | number | yes | Cumulative actual time engaged |
| `Author` | list[string] | optional | Author names (for books/papers/articles) |
| `Year` | integer | optional | Publication year |
| `URL` | string | optional | For online materials |
| `ISBN` | string | optional | For books |

## Body structure

```markdown
# <Title>

## What this source is
*Book? Paper? Video series? Podcast? Recipe collection? Language course? State it plainly.*

## Why it matters here
*Where in the curriculum. What Units it introduces or deepens.*

## Approach notes
*Pace, depth, selective vs full engagement, known hard sections, pairings with other sources.*

## Progress log
*Dated entries as the user engages.*

### <YYYY-MM-DD>

## Highlights & Notes
*Paraphrased or cited excerpts, marginalia, section-level distillations.*

## Units Introduced or Deepened
- [[Unit-Name]] — how this source relates to it

## Questions for Assistant
- [ ]

## Post-Engagement Synthesis
*Completed when the user finishes engaging with the source. 300–500 words.*
```

## Naming

- **Filename pattern:** `<Author-Title-Year>.md` for books/papers; `<Title-Year>.md` for media; `<Source-Slug>.md` for less-formal sources
- **Location:** `<Subject-Cartridge>/Sources/`
- **Wikilink target:** the filename

## Example Item

```markdown
---
Item_ID: beard-spqr
type: LLL_Source
timestamp: "2026-06-04T00:00:00Z"
title: "SPQR: A History of Ancient Rome"
lll_Subject: roman-empire
lll_Phase: 1
lll_Source_Role: primary
lll_Source_Kind: book
lll_Progress_Pct: 35
lll_Estimated_Hours: 22
lll_Actual_Hours: 9.5
Author:
  - "Mary Beard"
Year: 2015
ISBN: "978-1631491252"
Date_Added: 2026-04-25
Date_Modified: 2026-06-04
Needs_Processing: false
---

# SPQR: A History of Ancient Rome

## What this source is
A single-volume history of Rome from the founding through the early imperial period, by Mary Beard (Cambridge classicist). Aimed at a general-reader audience but with substantial scholarly apparatus in the notes. The book's spine is a long argument about how Rome thought about itself — and how its own historians shaped what we can know.

## Why it matters here
Primary text for Phase 1 (Republic). Introduces: the founding-mythology distinction between Romulus narratives and archaeological evidence; the cursus honorum and political career structure; the Patrician-Plebeian distinction; mos maiorum. Companion to Polybius (primary source) and Livy (primary source).

## Approach notes
- Read end-to-end, not selectively. Beard's argumentative spine is the value.
- Pair with [[Polybius-Histories]] — read Beard's chapter on the early Republic alongside Polybius Book 6 on the mixed constitution.
- Beard's notes are dense; skim on first read, return on second.
- Note: Beard's positions on the historicity of the early Republic differ from Livy's claims. Hold both versions during Phase 1; pick after Phase 2's Punic War material lands.

## Progress log

### 2026-04-25
Started. Read introduction and Chapter 1 (The First Romans). The skepticism about Romulus is sharper than I expected.

### 2026-05-02
Through Chapter 3 (The Kings of Rome). The argument that we know more about how Romans thought about their kings than about the actual kings is operative throughout.

### 2026-05-14
Chapter 4 (Rome's Great Leap Forward). The Twelve Tables. The patrician-plebeian distinction starts to take its mature shape.

### 2026-06-04
Through Chapter 5. Mid-book; pacing slowing because Phase 1 quizzes are coming due.

## Highlights & Notes

> "Rome was not built in a day, nor by a Romulus." — Beard, Ch 1
> *(Beard's opening pivot: the founding-story is a Roman cultural product, not a chronicle.)*

The cursus honorum is Beard's example of an institution that *constrained* Roman politics and made certain kinds of conflict structurally unavoidable. The constraint is what makes the institution analytically interesting.

## Units Introduced or Deepened

- [[Founding-Of-Rome]] — Beard's treatment is the principal source
- [[Cursus-Honorum]] — Beard Chapters 4–5
- [[Patrician-Plebeian-Distinction]] — Beard Chapter 4
- [[Mos-Maiorum]] — touched throughout; central to Beard's argument about Roman self-understanding
- [[Mixed-Constitution]] — Beard's brief treatment is preface to Polybius's deeper one

## Questions for Assistant

- [ ] After Phase 1 close: how does Beard's skepticism about early Republic chronology compare to current archaeological consensus? Get a citation pointer.
- [ ] Pair-reading question: Beard treats Polybius's mixed-constitution analysis as analytical category; Polybius treats it as constitutional theory. Both are doing different things with the same evidence. Worth a SOCRATIC-QUIZ.

## Post-Engagement Synthesis

*(To be completed when the book is finished, target Phase 2 close — late July 2026.)*
```

## Relationships

- `LLL_Unit` — Sources introduce or deepen Units; each Unit may cite Sources via `Sources` body section. The bidirectional relation is operational during Synthesis and Quiz activities.
- `LLL_Subject_Manifest` — Every Source declares its parent subject via `lll_Subject`.
- `LLL_Curriculum` — Sources are typically tied to a phase via `lll_Phase`; the Curriculum's per-phase Source list references back.
- `LLL_Session` — Sessions of `READ` activity reference the Source being engaged.
- `LLL_Synthesis` — Synthesis Items (weekly/monthly/phase-end) draw on Sources; the per-Synthesis Source list documents which Sources fed which Synthesis.

## Notes

- **Sources are not Units.** A Source is the *material* (the book); the Units it introduces are the *knowledge* (the concepts, techniques, facts the book contains). Engaging a Source typically produces or deepens multiple Units.
- **`lll_Source_Role` taxonomy:**
  - `primary` — central to the subject's curriculum; the spine of a phase
  - `supplementary` — adds depth or alternative perspective; not load-bearing
  - `reference` — used for lookup; not engaged end-to-end
  - `deep-dive` — engaged when a particular Unit needs more weight
  - `media` — video/podcast/film as study material (sometimes substitutes for reading; sometimes complements)
- **`lll_Progress_Pct` is approximate.** Useful for quick visual tracking of where the learner is in a long Source; don't obsess about precision. 25%, 50%, 75% bands are usually fine.
- **`lll_Actual_Hours` is for self-knowledge.** Tracking actual time vs estimated helps the learner calibrate future estimates and notice when a Source has consumed more attention than expected (a useful signal — either the Source is more valuable than expected, or the engagement is procrastinating around a Unit that's resisting mastery).
- **Post-Engagement Synthesis is the discipline.** Completing a Source without a synthesis is a missed opportunity for consolidation; the synthesis is 300–500 words written after finishing, before moving on. Per the LLL synthesis cadence (chapter 04).
- **Optional bibliographic fields** (`Author`, `Year`, `URL`, `ISBN`) are recommended for books, papers, articles, podcasts — they make the Source citation-ready when Synthesis pieces reference it.
