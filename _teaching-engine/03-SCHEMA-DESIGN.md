---
type: teaching-engine
role: schema-design-protocol
scope: subject-agnostic
updated: 2026-05-31
---

# 03 — SCHEMA DESIGN

> **This document defines how each subject's Units are designed. Different subjects have different structural shapes. This teaching engine does not impose a single Unit taxonomy on all subjects; it provides the protocol by which each subject's cartridge defines its own.**

## What is an Unit

An Unit is the smallest testable, quizzable, linkable unit of knowledge in a subject. The word replaces "concept" (which is too narrow for subjects like cuisine or languages) and generalizes across all domain shapes.

Examples across domains:

| Subject | Types |
|---------|-----------|
| History (e.g., Roman Empire) | Concept, Thinker, Period, Event |
| Cybernetics | Concept, Thinker, Reading |
| Linear Algebra | Theorem, Definition, Proof-Technique, Problem-Set |
| Southeast Asian Cuisine | Technique, Ingredient, Regional-Tradition, Dish, Equipment |
| Music Theory | Interval, Chord, Progression, Form, Composer, Work |
| Japanese Language | Kanji, Grammar-Pattern, Vocabulary-Set, Expression |
| Macroeconomics | Concept, Model, School-of-Thought, Indicator, Historical-Episode |
| Medicine | Condition, Mechanism, Drug-Class, Procedure, Case |

## Universal (cross-subject) Types

Every cartridge inherits these from the teaching engine, fully defined in `_teaching-engine/_templates/`:

- **session** — one per study session
- **quiz** — one per Socratic/conceptual quiz event
- **sr-log** — rolling performance log for SR cards
- **synthesis** — weekly journals, monthly essays, phase-end translations, quarterly drafts
- **source** — any external material consumed (book, paper, video, lecture, class, etc.)

These universal types use `source` rather than `reading` because not every subject is book-based — a cuisine cartridge's sources might be YouTube cooking demonstrations, a chef's recipe book, a market visit, a class. A language cartridge might use podcasts, textbooks, apps. The source template accommodates all of these.

## Subject-specific Types

Each cartridge defines its own Types in `<Subject>/_schema.md`, following the protocol below.

### Protocol for designing subject-specific Units

When cartridging a new subject, answer the following questions in `<Subject>/_schema.md` before creating any Units:

**Q1: What kind of knowledge does this subject consist of?** Choose all that apply, and note the relative weights:
- [ ] Formal/propositional (theorems, definitions, rules)
- [ ] Conceptual (ideas, frameworks, theories)
- [ ] Procedural (techniques, skills, methods)
- [ ] Declarative/factual (vocabulary, names, dates, data)
- [ ] Experiential (embodied, tacit, practiced)
- [ ] Creative/interpretive (works, performances, compositions)

**Q2: Who or what is a canonical authority in this subject?** Some subjects have thinkers (philosophy, economics), some have traditions or regions (cuisine, music), some have no authorities at all (logic, mathematics at the textbook level). Name what plays the authority role, if anything.

**Q3: What is the smallest unit a quiz question would test?** That's the discrete unit. Anything smaller is a fragment; anything larger should decompose.

**Q4: What relationships exist between Units?** Hierarchy, composition, similarity, contrast, cause-effect, historical sequence, prerequisite structure? These relationships become the `Related_Concepts:` fields in Unit frontmatter and the `[[wiki-links]]` in note bodies.

**Q5: Does the subject have a natural progression?** Some subjects have a strict prerequisite order (math, most sciences). Some are mostly lateral with a few entry points (cuisine, most humanities). This shapes the curriculum structure.

**Q6: What does mastery look like?** Mastery in music theory means hearing intervals, not reciting definitions. Mastery in cuisine means cooking a dish from scratch with sensory judgment, not listing ingredients. Mastery in cybernetics means applying concepts to novel organizational problems. Define the mastery endpoint concretely.

**Q7: What subject-specific session activities, if any, does this subject need?** Beyond the seven universal activities, does the subject need custom activity types (COOK-ALONG, SPEAK, PROVE, COMPOSE, PERFORM)? Each custom activity needs its trigger conditions specified.

**Q8: What's the right mastery scale?** The default is the 0–5 scale in the universal schema. Some subjects may need modified scales (language proficiency might use CEFR A1–C2; a skill-based subject might use novice-apprentice-journeyman-master). If you change the scale, document it.

### Required sections of `<Subject>/_schema.md`

Every cartridge's schema file must contain:

1. **Subject identity** — name, shape (which Q1 categories), domain summary
2. **Answers to Q1–Q8** — the analytical answers that justify the Unit choices
3. **Type definitions** — for each subject-specific Type:
   - Name and plural
   - One-sentence description
   - Required YAML frontmatter fields
   - Required body sections (in order)
   - Naming convention for files
   - Example (at least one)
4. **Relationship vocabulary** — the named relations that link Units (e.g., `prerequisite-of`, `variation-of`, `student-of`, `contains`)
5. **Mastery scale** — inherited 0–5 default or the subject's custom scale
6. **Custom session activities** — any activities beyond the universal seven, with trigger conditions
7. **Folder structure** — how Units are organized in subfolders within the cartridge

## Universal schema elements (inherited by all cartridges)

All cartridges inherit these without needing to redefine them:

### `_state.md` frontmatter (required fields)

```yaml
type: LLL_State
lll_Subject: <subject-name>
lll_Current_Phase: <int>
lll_Current_Phase_Name: <string>
lll_Pace_Mode: variable
lll_Sessions_Completed: <int>
lll_Total_Study_Hours: <float>
lll_Last_Session_Date: <YYYY-MM-DD | null>
lll_Next_Session_Default_Activity: <activity-code>
```

### `_subject.md` frontmatter (required fields)

```yaml
type: LLL_Subject_Manifest
lll_Subject: <subject-name>
lll_Subject_Slug: <lowercase-hyphenated>
lll_Domain_Shape: <list of Q1 categories>
lll_User_Goals: <summary string>
lll_User_Prior_Knowledge: <summary string>
lll_Math_Stance: <minimize | conceptual | full>
lll_Primary_Unit_Types: <list>
lll_Custom_Session_Activities: <list>
lll_Mastery_Scale: <default | custom-scale-name>
lll_SR_Enabled: <true | false>   # does this subject use spaced repetition? (BOOTSTRAP Q10; backend chosen globally in _USER.md)
lll_Bootstrapped: <YYYY-MM-DD>
```

### Session log frontmatter

Inherited from `_teaching-engine/_templates/TEMPLATE-Session.md`. Universal across subjects. The `lll_Units_Engaged` field is subject-agnostic — it just lists Unit slugs, regardless of their type.

### Quiz and SR-log frontmatter

Inherited. Universal.

### Synthesis frontmatter

Inherited. Universal — weekly, monthly, phase-end, quarterly variants.

## Conventions across all cartridges

- **Links:** Always `[[wiki-style]]` for internal links
- **Dates:** ISO format `YYYY-MM-DD`
- **Slugs:** lowercase-hyphenated, matching filename minus extension
- **Tags:** minimal, rely on frontmatter fields for queryable metadata
- **File edits:** Unit notes grow as mastery increases; session logs are append-only once written; `_state.md` is overwritten; quiz and SR-log files are append-only

## How the teaching engine uses `_schema.md`

When the assistant reads a cartridge, `_schema.md` tells it:

1. What Units exist in this subject (so it knows what types of notes to create)
2. What each Unit's required structure is (so it conforms to the schema)
3. What relationships can connect Units (so it links correctly)
4. What mastery means for this subject (so it calibrates probing and quizzing)
5. Whether custom session activities exist (so it can propose them)

Without a well-formed `_schema.md`, the cartridge is not ready for study.
