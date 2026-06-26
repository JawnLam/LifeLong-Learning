---
Item_ID: "UUID-OR-SLUG"
type: LLL_SR_Log
title: ""
lll_Subject: ""
lll_Phase: 
Date_Added: 
Date_Modified: 
Needs_Processing: false
---

# Phase <N> SR Performance Log

*Append-only. Every SR quizzing session adds rows.*

| Date | Unit | Card | Result | Streak | Session |
|------|------|------|--------|--------|---------|

## Rules

- Result values: `again` | `hard` | `good` | `easy`
- Streak counts consecutive non-`again` results
- Any Unit with two or more `again` results in its last three reviews gets flagged `lll_Status: weak` in `_state.md`
- No SR quizzing for Units below mastery level 2
