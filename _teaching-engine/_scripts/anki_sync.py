#!/usr/bin/env python3
"""
anki_sync.py — LifeLong-Learning's built-in Anki live-sync tool.

Ships WITH the OV (you do not need any external "skill" to use this). Any AI
assistant running LLL that has shell access — or you, by hand — can run it.
Zero third-party dependencies (Python 3 stdlib urllib only; nothing to pip-install).
Talks to the AnkiConnect add-on on http://127.0.0.1:8765. If there's no shell or
no AnkiConnect, use the no-tool TSV import path instead (SR-CONVENTIONS Path A).

Implements the LLL export contract:

  card identity key : lll-id::<subject-slug>::<unit-id>::<card-index>
  deck              : LLL::<Subject>
  tags              : lll::subject::<slug>  lll::phase::<n>
                      lll::unit::<unit-slug>  lll::kind::<kind>  + the lll-id:: key tag
  notetypes         : "Basic" and "Basic (and reversed card)"

Subcommands:
  verify                     Check the connection; print Anki + AnkiConnect status.
  push   --tsv <file>        Add-or-update notes from an LLL anki-export.tsv (idempotent
                             via the lll-id:: key tag). Creates decks as needed.
  pull   --deck "<deck>"     Read review performance for a deck and emit JSON
         [--subject <slug>]  (per-Unit reps/lapses/recent-ease + weak flags), for the
                             assistant to write into the SR-Log and reconcile _state.md.

Design note: `pull` never writes to the vault. It emits JSON on stdout; the assistant
applies LLL formatting to the SR-Log and _state.md. `push` is the only mutating call,
and it mutates Anki, not the vault.
"""

import sys
import json
import argparse
import urllib.request
import urllib.error

ANKICONNECT_URL = "http://127.0.0.1:8765"


def invoke(action, **params):
    """POST a single AnkiConnect action; return its result or raise RuntimeError."""
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT_URL, data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(
            "Cannot reach AnkiConnect at %s — is Anki desktop running with the "
            "AnkiConnect add-on installed (code 2055492159)? Underlying error: %s"
            % (ANKICONNECT_URL, e)
        )
    if body.get("error") is not None:
        raise RuntimeError("AnkiConnect error on '%s': %s" % (action, body["error"]))
    return body.get("result")


# ---------------------------------------------------------------- verify

def cmd_verify(_args):
    version = invoke("version")
    decks = invoke("deckNames")
    lll_decks = sorted(d for d in decks if d == "LLL" or d.startswith("LLL::"))
    print("AnkiConnect reachable. API version: %s" % version)
    print("Total decks: %d" % len(decks))
    if lll_decks:
        print("LLL decks present:")
        for d in lll_decks:
            print("  - %s" % d)
    else:
        print("No LLL:: decks yet (nothing pushed).")
    return 0


# ---------------------------------------------------------------- push

def parse_tsv(path):
    """Parse an LLL anki-export.tsv into (columns_map, rows).

    Honors the header directives:
      #separator:tab  #html:true
      #notetype column:N  #deck column:N  #tags column:N  #guid column:N
    Remaining columns are the notetype fields in order (Front, Back).
    """
    sep = "\t"
    cols = {}  # role -> 0-based index
    data_rows = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line:
                continue
            if line.startswith("#"):
                low = line[1:].strip().lower()
                if low.startswith("separator:"):
                    val = low.split(":", 1)[1].strip()
                    sep = "\t" if val in ("tab", "\\t") else val
                elif low.startswith("html:"):
                    pass
                else:
                    # e.g. "notetype column:1"
                    for role in ("notetype", "deck", "tags", "guid"):
                        if low.startswith(role + " column:"):
                            cols[role] = int(low.split(":", 1)[1].strip()) - 1
                continue
            data_rows.append(line.split(sep))
    return cols, data_rows


def field_indices(cols, ncols):
    """Columns not claimed by notetype/deck/tags/guid, in order = Front, Back, ..."""
    claimed = set(cols.values())
    return [i for i in range(ncols) if i not in claimed]


def cmd_push(args):
    cols, rows = parse_tsv(args.tsv)
    if "notetype" not in cols or "deck" not in cols:
        raise RuntimeError("TSV missing '#notetype column:' or '#deck column:' header directives.")
    added = updated = failed = 0
    ensured_decks = set()
    for r in rows:
        try:
            notetype = r[cols["notetype"]]
            deck = r[cols["deck"]]
            tags = r[cols["tags"]].split() if "tags" in cols and len(r) > cols["tags"] else []
            fidx = field_indices(cols, len(r))
            front = r[fidx[0]] if len(fidx) > 0 else ""
            back = r[fidx[1]] if len(fidx) > 1 else ""
            key_tags = [t for t in tags if t.startswith("lll-id::")]
            if not key_tags:
                raise RuntimeError("row has no lll-id:: identity tag: %r" % r)
            key = key_tags[0]

            if deck not in ensured_decks:
                invoke("createDeck", deck=deck)
                ensured_decks.add(deck)

            existing = invoke("findNotes", query='tag:%s' % key)
            if existing:
                invoke("updateNoteFields",
                       note={"id": existing[0], "fields": {"Front": front, "Back": back}})
                updated += 1
            else:
                invoke("addNote", note={
                    "deckName": deck,
                    "modelName": notetype,
                    "fields": {"Front": front, "Back": back},
                    "tags": tags,
                    "options": {"allowDuplicate": False},
                })
                added += 1
        except Exception as e:  # noqa: BLE001 - report per-row, keep going
            failed += 1
            sys.stderr.write("push row failed: %s\n" % e)
    print(json.dumps({"added": added, "updated": updated, "failed": failed,
                      "decks_ensured": sorted(ensured_decks)}, indent=2))
    return 0 if failed == 0 else 1


# ---------------------------------------------------------------- pull

def parse_key_tag(tags):
    """Return (subject, unit_id, card_index) from a note's lll-id:: tag, or (None,None,None)."""
    for t in tags:
        if t.startswith("lll-id::"):
            parts = t.split("::")
            if len(parts) == 4:
                return parts[1], parts[2], parts[3]
    return None, None, None


def cmd_pull(args):
    if args.deck:
        query = 'deck:"%s"' % args.deck
    elif args.subject:
        query = "tag:lll::subject::%s" % args.subject
    else:
        raise RuntimeError("pull needs --deck or --subject")

    card_ids = invoke("findCards", query=query)
    if not card_ids:
        print(json.dumps({"query": query, "cards": 0, "units": {}}, indent=2))
        return 0

    cards = invoke("cardsInfo", cards=card_ids)
    # Tags live on the NOTE, not the card — fetch notesInfo to map each card's note to its tags.
    note_ids = sorted({c["note"] for c in cards if c.get("note")})
    note_tags = {}
    if note_ids:
        for n in invoke("notesInfo", notes=note_ids):
            note_tags[n.get("noteId", n.get("note"))] = n.get("tags", [])
    # Per-review ease history (1=again). Degrade gracefully if the action is unavailable.
    reviews = {}
    try:
        reviews = invoke("getReviewsOfCards", cards=card_ids)
    except RuntimeError as e:
        sys.stderr.write("getReviewsOfCards unavailable (%s); using lapses only.\n" % e)

    units = {}
    for c in cards:
        subject, unit_id, _idx = parse_key_tag(note_tags.get(c.get("note"), []))
        unit_id = unit_id or "(unmapped)"
        u = units.setdefault(unit_id, {
            "subject": subject, "cards": 0, "reps": 0, "lapses": 0,
            "failing_cards": 0, "weak": False,
        })
        u["cards"] += 1
        u["reps"] += c.get("reps", 0)
        u["lapses"] += c.get("lapses", 0)
        cid = str(c.get("cardId", c.get("id")))
        rlist = reviews.get(cid) or reviews.get(int(cid), []) if reviews else []
        if rlist:
            last3 = sorted(rlist, key=lambda x: x.get("id", 0))[-3:]
            agains = sum(1 for rv in last3 if rv.get("ease") == 1)
            if agains >= 2:
                u["failing_cards"] += 1
        elif c.get("lapses", 0) >= 2:
            u["failing_cards"] += 1
    for u in units.values():
        u["weak"] = u["failing_cards"] > 0

    print(json.dumps({
        "query": query,
        "cards": len(card_ids),
        "weak_units": sorted(k for k, v in units.items() if v["weak"]),
        "units": units,
    }, indent=2))
    return 0


def main():
    p = argparse.ArgumentParser(description="AnkiConnect client for LifeLong-Learning.")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("verify", help="check the AnkiConnect connection")

    pp = sub.add_parser("push", help="add-or-update notes from an LLL anki-export.tsv")
    pp.add_argument("--tsv", required=True, help="path to anki-export.tsv")

    pl = sub.add_parser("pull", help="emit per-Unit review performance as JSON")
    pl.add_argument("--deck", help='deck name, e.g. "LLL::Roman Empire"')
    pl.add_argument("--subject", help="subject slug, e.g. roman-empire")

    args = p.parse_args()
    handler = {"verify": cmd_verify, "push": cmd_push, "pull": cmd_pull}[args.cmd]
    try:
        sys.exit(handler(args))
    except RuntimeError as e:
        sys.stderr.write("ERROR: %s\n" % e)
        sys.exit(2)


if __name__ == "__main__":
    main()
