# `_scripts/` — bundled engine tooling

Optional helper scripts that ship with LifeLong-Learning. **Nothing here is required for core study** (sessions, Units, synthesis, Socratic quizzing all work with zero runtime). These exist so operators who opt into certain integrations don't need to build or install anything themselves.

All scripts are **Python 3 standard-library only** — no `pip install`, no network beyond localhost.

## `anki_sync.py` — built-in Anki live sync

The AnkiConnect client for the OV's Anki integration. Lets any AI running LLL (or you, by hand) push flashcards straight into Anki and pull review performance back — **without any external "skill."** Full contract and workflow in `../_meta/SR-CONVENTIONS.md § "Anki integration"`.

**Requires** (only if you chose Anki as your SR backend): Anki desktop running + the free AnkiConnect add-on (Tools → Add-ons → Get Add-ons → code `2055492159` → restart). If you don't have those, or your AI has no shell, use the dependency-free **TSV import** path instead — same cards, manual File → Import.

**Commands** (run from the OV root):

```bash
# 1. Check the connection
python3 _teaching-engine/_scripts/anki_sync.py verify

# 2. Push a subject's cards (idempotent — re-running updates, never duplicates)
python3 _teaching-engine/_scripts/anki_sync.py push --tsv "<Subject>/SR-Cards/anki-export.tsv"

# 3. Pull review performance as JSON (the assistant then writes it into the SR-Log)
python3 _teaching-engine/_scripts/anki_sync.py pull --deck "LLL::<Subject>"
```

`push` only mutates Anki; `pull` only reads (it prints JSON — it never writes to your vault, so the assistant stays in control of SR-Log formatting and `_state.md` reconciliation). AnkiWeb has no write API; cards reach your phone/browser via Anki's own Sync.
