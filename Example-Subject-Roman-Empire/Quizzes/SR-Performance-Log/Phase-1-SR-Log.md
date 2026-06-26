---
Item_ID: "roman-empire-phase-1-sr-log"
type: LLL_SR_Log
timestamp: "2026-06-01T00:00:00Z"
title: "Roman Empire — Phase 1 SR Performance Log"
lll_Subject: Roman-Empire
lll_Phase: 1
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
---

# Phase 1 SR Performance Log

*Append-only. Every SR quizzing session adds rows. No cards yet — Units must reach mastery 2 before SR cards are generated.*

| Date | Unit | Card | Result | Streak | Session |
|------|------|------|--------|--------|---------|

## Rules

- Result values: `again` | `hard` | `good` | `easy`
- Streak counts consecutive non-`again` results
- Any Unit with two or more `again` results in its last three reviews gets flagged `lll_Status: weak` in `_state.md`
- No SR quizzing for Units below mastery level 2
