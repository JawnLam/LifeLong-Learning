---
type: teaching-engine
role: session-activity-decision-algorithm
scope: subject-agnostic
updated: 2026-05-31
---

# 01 — SESSION PROTOCOL

> **Defines how you decide what to do in a session. Default posture is hybrid autonomy: you propose a default; the user overrides freely. Show your reasoning.**

## Session lifecycle

```
1. READ teaching engine + subject mandatory files (see 00-START-HERE.md)
2. DIAGNOSE current state
3. PROPOSE a session activity with rationale
4. WAIT for user confirmation or override
5. EXECUTE the activity
6. CAPTURE results (Unit updates, quiz logs, SR cards, synthesis artifacts); drop any stray, off-topic thought raised mid-session into the root `_Inbox/` as an `LLL_Note`; and when a trigger fires (below), write an `LLL_Insight` to `<Subject>/Insights/`
7. WRITE the session log
8. UPDATE _state.md
9. END with one explicit "next-session seed" in Open Threads
```

Steps 1, 6, 7, 8, 9 are non-negotiable. Step 5 varies by activity.

## The seven universal session activity types

These apply to all subjects. Individual cartridges may define their own subject-specific activities in addition (documented in `<Subject>/_schema.md`).

| Code | Activity | When it's the right default |
|------|----------|------------------------------|
| **TEACH** | Introduce new material via Socratic dialogue; user engages with source material before or during | Active source material in progress and no major weak Units pending; user has momentum |
| **QUIZ-SR** | Drive SR card recall and log performance | Subject has `lll_SR_Enabled: true` AND cards are due AND ≥ 72 hours since last session of this type. If `lll_SR_Enabled: false`, this activity never fires — SR is opt-in (see SR-CONVENTIONS). |
| **QUIZ-SOCRATIC** | Conceptual/application questions — probe explanation and transfer, not pure recall. Interleave Units and keep any candidate answers equal-length (anti-cueing) — see `02-PEDAGOGY.md` / `_meta/SR-CONVENTIONS.md`. | ≥ 2 Units at mastery level 2 and user hasn't been Socratically quizzed in ≥ 7 days |
| **REVIEW-WEAK** | Revisit Units flagged `weak` in state with targeted re-teaching | Any Unit is flagged weak OR SR performance on an Unit is failing |
| **SYNTHESIZE** | Produce a synthesis artifact (weekly journal, monthly essay, phase-end piece, quarterly draft) | Synthesis cadence due OR user explicitly wants to write |
| **INTEGRATE** | Cross-Unit connection-mapping session; end-of-phase checks also live here | ≥ 5 Units introduced since last INTEGRATE, OR at phase boundary |
| **TRIAGE** | Process the capture inbox: for each pending `LLL_Note`, decide its disposition — **promote** to a new Unit/Source, **merge** into an existing Unit, or **discard** (kept, not deleted) — assigning a subject and moving un-homed root-`_Inbox/` notes into `<Subject>/Captures/` along the way. Drains the pen toward zero. | The root `_Inbox/` holds ≥ 5 untriaged captures, OR any capture with `Needs_Processing: true` is older than 14 days |

**The capture layer, in one paragraph.** Fleeting notes live in two places: the root `_Inbox/` (un-homed — subject unknown or cross-cutting; `lll_Subject` empty) and `<Subject>/Captures/` (subject known, not yet processed into a Unit). A capture is *only* for the un-homed / pre-processed — a thought about a known Unit belongs in that Unit's Open Questions, a reading note on a known Source in that Source's Highlights, a session recap in the session log. TRIAGE is what keeps the inbox from becoming a dumping ground. The single move in the system is homing (root `_Inbox/` → `<Subject>/Captures/` when a subject is assigned); after that, disposition is status-only (`lll_Note_Status`), preserving provenance. See `_types/LLL_Note.md`.

## Decision algorithm

Evaluate in order. First condition that fires determines the default proposal. Before evaluating, read the subject's recent `Insights/` (below) — they set the **zone of proximal development**: the mastery floors, corrected misconceptions to preempt, and disclosed prior knowledge that determine where "just past what they can already do" actually is.

### Step 1 — Hard overrides (highest priority)

- **If** user has entered a new phase within the last 2 sessions and has not completed an orientation to the phase → propose **TEACH** with an orientation framing
- **If** a phase exit checklist has ≥ 80% items checked but not 100% → propose **INTEGRATE** as a phase-exit check
- **If** ≥ 3 sessions have passed since any SYNTHESIZE → propose **SYNTHESIZE** (weekly journal at minimum)
- **If** the root `_Inbox/` holds ≥ 5 untriaged captures OR any capture with `Needs_Processing: true` is older than 14 days → propose **TRIAGE** (drain the capture inbox before it silts up)

Regardless of what fires: at session start, if the capture inbox (`_Inbox/` + the active subject's `Captures/`) is non-empty, name the pending count in your proposal even when TRIAGE is not the default — so the user always knows the pen has something waiting.

### Step 2 — Weak-Unit priority

- **If** `_state.md` lists any Unit under "Weak Units" → propose **REVIEW-WEAK** on the most recently flagged
- **If** SR performance log shows any Unit failing its most recent review → add to Weak Units and propose **REVIEW-WEAK**

### Step 3 — Cadence rhythms

- **If** ≥ 7 days since last QUIZ-SOCRATIC AND ≥ 2 Units at mastery level 2 → propose **QUIZ-SOCRATIC**
- **If** the subject has `lll_SR_Enabled: true` AND SR cards are due AND last QUIZ-SR was ≥ 72 hours ago → propose **QUIZ-SR** (skip entirely when SR is off)

### Step 4 — Default forward motion

- **If** none of the above fires → propose **TEACH** on the next Unit in the phase's curriculum order at mastery level 0

### Step 5 — Subject-specific activities

Check `<Subject>/_schema.md` for any custom activities this subject defines (for example, a cuisine cartridge might define a **COOK-ALONG** activity; a language cartridge might define a **SPEAK** activity). If a custom activity's trigger condition is satisfied, propose it with equal priority to the universal activities.

### Step 6 — Post-proposal

Present the proposal to the user:

```
Proposed activity: <CODE> — <plain-English description>
Rationale: <which conditions fired>
Alternative activities available: <the other valid options>
Your call.
```

Wait. Do not begin until confirmation or override.

## Learning records — the Insight ledger

`<Subject>/Insights/` holds `LLL_Insight` items: decision-grade records of what's now *known about the learner*, ADR-style, numbered `0001-slug.md`. They are **not** a session journal (that's the session log) — they are the small set of facts that change what to teach next, and they are the primary input to the zone-of-proximal-development judgment above.

**Write an Insight when — and only when — one of these fires:**

1. **A misconception was corrected.** The learner held a wrong belief and now sees why. Highest value: a corrected misconception predicts related future stumbles, so the engine can preempt them. (`lll_Insight_Kind: misconception-corrected`)
2. **Prior knowledge was disclosed.** "I already know X" — record it, and the claimed depth, so future sessions don't re-teach it. (`prior-knowledge`)
3. **A mastery floor was set.** The learner demonstrated genuine, evidenced understanding of something non-trivial — raising where to start next time. Not mere exposure; evidence required. (`mastery-floor`)
4. **The mission shifted.** The learner discovered they care about something different. Cross-link and update `_subject.md`; confirm with the learner before re-pointing the cartridge. (`mission-shift`)

**Do not** write one for material merely covered (coverage is not learning — wait for evidence), for anything already captured tersely in `_glossary.md`, or as a per-session activity log.

**Supersession:** when a later insight corrects an earlier one, mark the old `lll_Insight_Status: superseded` and link it from the new one via `lll_Supersedes`. Keep the superseded record — how understanding evolved is itself signal.

## Writing the session log

At the end of every session, create a new file in `<Subject>/Sessions/` named:

```
YYYY-MM-DD_NNN_<activity-code>.md
```

`NNN` is a zero-padded sequential session number. Use `_teaching-engine/_templates/TEMPLATE-Session.md`.

## Updating `_state.md`

After every session, update:

- `lll_Sessions_Completed` (increment by 1)
- `lll_Last_Session_Date`
- `lll_Total_Study_Hours` (add the session duration)
- Phase hours logged
- Unit mastery table (any Units touched this session)
- Recent Sessions (prepend new session)
- Weak Units (add or remove as appropriate)
- Open Threads (close any addressed, add new ones for next session)
- `lll_Next_Session_Default_Activity` (your prediction — a hint, not a commitment)

## Phase exit protocol

When the user approaches phase exit (≥ 80% checklist complete):

1. Propose **INTEGRATE** as the next session's activity
2. Ask the user to demonstrate each unchecked exit criterion **in their own words with their own examples**
3. Identify any thin spots. Add to Weak Units with specific remediation.
4. When all demonstrated, update `_state.md`:
   - Mark the phase complete
   - Increment `lll_Current_Phase`
   - Update `lll_Current_Phase_Name`
   - Reset Phase Exit Checklist to new phase's criteria
5. Create a Phase-End Translation piece in `Synthesis/Phase-End-Translations/`

## Quality gates

Before ending any session, confirm:

- [ ] At least one concrete learning moment captured
- [ ] Mastery levels updated for any Units engaged
- [ ] Session log written
- [ ] `_state.md` updated
- [ ] Explicit Open Thread left for next session
- [ ] Quiz results logged (if a quiz happened)
- [ ] Synthesis artifact saved (if a synthesis was produced)

If any is no, the session is not complete. Do the missing work.
