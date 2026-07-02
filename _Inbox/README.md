# `_Inbox/` — the un-homed capture pen

This is the OV-root capture inbox: the one place a fleeting note can live **before you know which subject it belongs to**. Drop anything here — a stray idea, a question, a quote, a link, a connection between two subjects — as an `LLL_Note` with `lll_Subject` left empty.

It is the counterpart to each cartridge's `<Subject>/Captures/` folder:

| Folder | For | `lll_Subject` |
|--------|-----|---------------|
| `_Inbox/` (here) | Un-homed or cross-cutting captures — subject unknown | empty |
| `<Subject>/Captures/` | Captures you already know belong to one subject, not yet processed into a Unit | set |

## How it drains

The **TRIAGE** session activity processes this inbox. For each note the AI proposes a disposition:

- **Homed** — assign a subject; the note moves from here into that subject's `Captures/`. (This is the only file *move* in the capture system.)
- **Promoted** — it became a new Unit or Source; recorded in `lll_Promoted_To`, and the new Item carries an `Origin:` backlink.
- **Merged** — folded into an existing Unit (usually as an Open Question); `lll_Promoted_To` points to the target.
- **Discarded** — kept, not deleted (the not-useful journey is data); one line says why.

TRIAGE is proposed automatically once this inbox holds ≥ 5 untriaged captures, or any capture is more than 14 days old. A healthy inbox trends back toward empty.

## What does *not* go here

Capture is only for the un-homed / pre-processed. If a thought already has a home, put it there instead:

- A thought about a **known Unit** → that Unit's *Open Questions*.
- A reading note on a **known Source** → that Source's *Highlights & Notes*.
- A recap of **what happened this session** → the Session log.

See `_teaching-engine/01-SESSION-PROTOCOL.md` (the TRIAGE activity) and `_types/LLL_Note.md` (the type contract).
