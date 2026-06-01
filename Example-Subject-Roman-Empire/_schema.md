---
# This is a cartridge reference document, not a learning note.
# It defines atom types for the Roman-Empire cartridge.
# See _teaching-engine/03-SCHEMA-DESIGN.md for the protocol.
lll_Subject: Roman-Empire
updated: 2026-06-01
---

# _schema — The Rise and Fall of the Roman Empire

> **Subject-specific atom definitions. Follows the protocol in `_teaching-engine/03-SCHEMA-DESIGN.md`.**

## Subject identity

- **Name:** The Rise and Fall of the Roman Empire
- **Shape:** Historical narrative + conceptual / institutional + declarative
- **Domain summary:** Roman political history from the traditional founding (753 BC) through the fall of the Western Empire (476 AD), with closing attention to the Byzantine continuation and the historiographical "why did Rome fall?" debate. Studied as institutions, mechanisms, and pressures rather than as a chronicle of emperors and battles.

## Answers to schema-design Q1–Q8

**Q1 — Kinds of knowledge.** Primarily conceptual (institutions, mechanisms: cursus honorum, imperium, Principate vs Dominate, variety of governance forms) and declarative (names, dates, sequences). Some interpretive (competing theses of decline). Minimally procedural — there is no skill to practice; this is comprehension and synthesis.

**Q2 — Canonical authority.** Yes, on two levels. Primary sources (Polybius, Livy, Tacitus, Suetonius, Cassius Dio, Ammianus Marcellinus, Procopius, Augustine, etc.) and major modern historians (Gibbon as the canonical decline-thesis voice; Peter Brown for late antiquity; Mary Beard, Adrian Goldsworthy, Bryan Ward-Perkins, Peter Heather as contemporary interpreters). Both categories matter; the **thinker** atom type accommodates both.

**Q3 — Smallest quizzable unit.** A concept (e.g., *cursus honorum*), a thinker (e.g., *Tacitus*), a period (e.g., *Severan dynasty*), or an event (e.g., *Battle of Adrianople, 378 AD*). These are the four atom types.

**Q4 — Relationships between atoms.**
- `precedes` / `follows` — period→period or event→event chronological
- `contains` — period contains events
- `caused-by` / `causes` — event→event causal
- `prefigures` — event or period anticipates a later development
- `parallels` — institutional or historical parallel between non-adjacent atoms
- `analyzed-by` — event or period analyzed by a particular thinker
- `student-of` / `teacher-of` — thinker-to-thinker (less common in history, used for historiographical lineage)
- `influenced-by` / `influences` — thinker-to-thinker, weaker form
- `instantiates` — event instantiates a concept (e.g., *Battle of Cannae* instantiates *imperium delegated to a dictator*)
- `contrasts-with` — for sharpening conceptual boundaries (e.g., *Principate* contrasts with *Dominate*)

**Q5 — Natural progression.** Strong chronological progression. Phase 1 (early Rome, kings to mid-Republic) must precede Phase 2 (Late Republic to Augustus). Within phases, lateral movement between atoms is fine. The historiographical thread (Q2 thinkers and the "why did Rome fall?" debate) runs alongside the chronology and is mostly back-loaded to phases 5–6.

**Q6 — Mastery endpoint.** The user can:
1. Narrate the arc of Roman history from founding to fall in a single sitting, with the load-bearing inflection points and institutional shifts
2. Explain at least three competing theses of decline and articulate which they find most persuasive, with reasoning
3. Read a piece of Roman primary-source text in translation and place it politically and historically
4. Apply Roman institutional concepts (imperium, principate, cursus honorum) to compare/contrast with other systems they know

**Q7 — Custom session activities.** None beyond the universal six. History is well-served by TEACH (Socratic walk-through of new period/concept), QUIZ-SOCRATIC (apply concepts, place events), REVIEW-WEAK, SYNTHESIZE, INTEGRATE (chronology mapping and cross-thesis comparison).

**Q8 — Mastery scale.** Default 0–5.

## Atom type definitions

### concept

- **Description:** An institution, idea, distinction, or mechanism — abstract enough to apply across multiple periods. The atomic unit of *understanding* in this subject.
- **Required frontmatter:**
  ```yaml
  Item_Prototype: LLL_Atom
  Item_ID: "<slug>"
  Title: "<Concept Name>"
  lll_Subject: Roman-Empire
  Date_Added: <YYYY-MM-DD>
  Date_Modified: <YYYY-MM-DD>
  Needs_Processing: false
  lll_Atom_Type: concept
  lll_Phase: <1-6>
  lll_Status: <seed | active | weak | mastered>
  lll_Mastery: <0-5>
  Related_Concepts: <list of wikilinks>
  lll_First_Encountered: <YYYY-MM-DD | null>
  lll_Last_Practiced: <YYYY-MM-DD | null>
  lll_SR_Cards_Created: <int>
  lll_Confidence: <1-5 | null>
  lll_Graduated_To: []
  Opposing_Concepts: []
  Discipline: Roman-History
  ```
- **Required sections (in order):**
  1. `# <Concept Name>`
  2. `## One-Sentence Statement`
  3. `## Precursor / Problem`
  4. `## Full Exposition`
  5. `## Analogies`
  6. `## Counter-Examples / Boundaries`
  7. `## Applications` (cite events, periods, or thinkers where this concept does work)
  8. `## Related Atoms`
  9. `## Sources`
  10. `## Quiz Bank`
  11. `## Open Questions`
- **Naming:** `Concept-Name.md` in PascalCase-With-Hyphens (e.g., `Cursus-Honorum.md`, `Mos-Maiorum.md`)
- **Location:** `Atoms/Concepts/`

### thinker

- **Description:** A historian, statesman, or commentator whose work or example matters for understanding the period. Includes both ancient (Polybius, Tacitus) and modern (Gibbon, Beard) historians.
- **Required frontmatter:**
  ```yaml
  Item_Prototype: LLL_Atom
  Item_ID: "<slug>"
  Title: "<Full Name>"
  lll_Subject: Roman-Empire
  Date_Added: <YYYY-MM-DD>
  Date_Modified: <YYYY-MM-DD>
  Needs_Processing: false
  lll_Atom_Type: thinker
  lll_Phase: <primary phase number>
  lll_Status: <seed | active | weak | mastered>
  lll_Mastery: <0-5>
  lll_First_Encountered: <YYYY-MM-DD | null>
  lll_Last_Practiced: <YYYY-MM-DD | null>
  lll_Thinker_Era: <ancient | medieval | modern | contemporary>
  lll_Thinker_Lifespan: "<approx. years, e.g., c. 200–118 BC>"
  lll_Primary_Works: <list of strings>
  ```
- **Required sections (in order):**
  1. `# <Full Name>`
  2. `## Sketch` (1–2 paragraphs: who they were, when, why they matter here)
  3. `## Method / Stance` (how they approach the subject; their bias, their genre, their reliability)
  4. `## Key Works`
  5. `## Contributions` (which concepts or events they're the primary source/interpreter for)
  6. `## Related Atoms`
  7. `## Quotes Worth Keeping`
  8. `## Quiz Bank`
  9. `## Open Questions`
- **Naming:** `Last-Name.md` or `Last-Name-First.md` if disambiguation needed (e.g., `Polybius.md`, `Livy.md`, `Gibbon.md`)
- **Location:** `Atoms/Thinkers/`

### period

- **Description:** A bounded span of Roman history with a coherent character — political, institutional, or cultural. Period atoms are containers for the events and concepts that belong to them.
- **Required frontmatter:**
  ```yaml
  Item_Prototype: LLL_Atom
  Item_ID: "<slug>"
  Title: "<Period Name>"
  lll_Subject: Roman-Empire
  Date_Added: <YYYY-MM-DD>
  Date_Modified: <YYYY-MM-DD>
  Needs_Processing: false
  lll_Atom_Type: period
  lll_Phase: <1-6>
  lll_Status: <seed | active | weak | mastered>
  lll_Mastery: <0-5>
  lll_Period_Start: "<year, e.g., -509 (Republic) or 27 BC>"
  lll_Period_End: "<year>"
  lll_Period_Order: <int>     # 1 = earliest
  Related_Concepts: <list>
  ```
- **Required sections (in order):**
  1. `# <Period Name> (<dates>)`
  2. `## Character` (what defines this period)
  3. `## Key Institutions in Force`
  4. `## Major Events Within` (links to event atoms)
  5. `## Inflection Out` (what ends this period and starts the next)
  6. `## Concepts Operative in This Period`
  7. `## Thinkers / Sources for This Period`
  8. `## Quiz Bank`
  9. `## Open Questions`
- **Naming:** `Period-Name.md` (e.g., `Early-Republic.md`, `Crisis-of-the-Third-Century.md`)
- **Location:** `Atoms/Periods/`

### event

- **Description:** A bounded, dated occurrence with consequences. Battles, deaths, accessions, reforms, treaties, edicts. Event atoms are the load-bearing inflection points the user needs to be able to place and explain.
- **Required frontmatter:**
  ```yaml
  Item_Prototype: LLL_Atom
  Item_ID: "<slug>"
  Title: "<Event Name>"
  lll_Subject: Roman-Empire
  Date_Added: <YYYY-MM-DD>
  Date_Modified: <YYYY-MM-DD>
  Needs_Processing: false
  lll_Atom_Type: event
  lll_Phase: <1-6>
  lll_Status: <seed | active | weak | mastered>
  lll_Mastery: <0-5>
  lll_Event_Date: "<year or range, e.g., 218–201 BC>"
  lll_Event_Kind: <battle | accession | reform | treaty | death | edict | other>
  lll_Containing_Period: "[[Period-Name]]"
  Related_Concepts: <list>
  ```
- **Required sections (in order):**
  1. `# <Event Name> (<date>)`
  2. `## What Happened` (factual narrative, 1–3 paragraphs)
  3. `## Why It Mattered` (consequences, what it changed)
  4. `## Causes`
  5. `## Sources / Disputes` (where the historical record is solid, where it's contested)
  6. `## Concepts This Instantiates`
  7. `## Related Atoms`
  8. `## Quiz Bank`
  9. `## Open Questions`
- **Naming:** `Event-Name.md` (e.g., `Founding-Of-Rome.md`, `Battle-Of-Adrianople.md`)
- **Location:** `Atoms/Events/`

## Relationship vocabulary

Used in atom frontmatter and body links:

| Relation | Used between | Where it appears |
|----------|--------------|------------------|
| precedes / follows | period↔period, event↔event | Body, chronology sections |
| contains | period→event, period→concept-in-force | Body of period atom |
| caused-by / causes | event↔event | Body, "Causes" / "Why It Mattered" sections |
| prefigures | event→event, period→period | Body |
| parallels | any↔any | Body, "Related Atoms" |
| analyzed-by | event→thinker, period→thinker | Body, "Sources / Disputes" |
| influenced-by / influences | thinker↔thinker | Body |
| instantiates | event→concept | Body, "Concepts This Instantiates" |
| contrasts-with | any↔any | Body, sharpening boundaries |

## Mastery scale

Default 0–5 per teaching engine convention. See `_state.md` for definitions.

## Synthesis adaptations

History benefits from one optional synthesis form beyond the universal four:

- **Causation map** — a non-prose synthesis: a structured diagram or table linking events / periods / concepts via the relationship vocabulary above. Useful for INTEGRATE sessions. Store in `Synthesis/Causation-Maps/` if the user opts to produce these. Not required.

Otherwise standard cadence (weekly, monthly, phase-end, quarterly) applies directly.

## SR adaptations

Standard text-based cards. For history, two card forms are especially useful:

- **Chronology cards** — *"What did Rome become in 27 BC?"* → *"The Principate, under Augustus."*
- **Cause cards** — *"Why did the Crisis of the Third Century end?"* → *"Diocletian's reforms (Tetrarchy, administrative reorganization, currency reform) restored stability ~284–305 AD."*

See `_teaching-engine/_meta/SR-CONVENTIONS.md` for card syntax.

## Folder structure within cartridge

```
Example-Subject-Roman-Empire/
├── _subject.md
├── _schema.md                       ← this file
├── _curriculum.md
├── _state.md
├── Atoms/
│   ├── Concepts/                    ← concept atoms
│   ├── Thinkers/                    ← thinker atoms (ancient + modern)
│   ├── Periods/                     ← period atoms
│   └── Events/                      ← event atoms
├── Sources/                         ← books, papers, videos, podcasts
├── Sessions/
├── Quizzes/
│   ├── Socratic-Conceptual/
│   └── SR-Performance-Log/
├── Synthesis/
│   ├── Weekly-Journals/
│   ├── Monthly-Essays/
│   ├── Phase-End-Translations/
│   └── Quarterly-Drafts/
└── SR-Cards/
```
