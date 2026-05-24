# Ingest runbook

Quick reference for adding new PDFs to the RAG vector DB.

## TL;DR

```bash
# 1. Drop PDF(s) here in data/inbox/

# 2. Scaffold the manifest (Claude proposes categories; you confirm)
/Users/dan153/anaconda3/envs/ValAct_RAG/bin/python -m ingest.add_doc scaffold --suggest

# 3. Open data/inbox/manifest.csv and fill in the `url` column

# 4. Run the full pipeline
/Users/dan153/anaconda3/envs/ValAct_RAG/bin/python -m ingest.add_doc run
```

That's it. Six stages run per PDF: MathPix convert → Claude lint+safe-fix → Claude summary → JSON manifests → embed+upsert → move PDF to `data/pdf/{collection}/`.

## Variations

**Skip Claude's category suggestion** — fill `collection` yourself:
```bash
python -m ingest.add_doc scaffold     # blank collection column
```

**Auto-accept high-confidence suggestions**:
```bash
python -m ingest.add_doc scaffold --suggest --auto-accept-above 0.85
```

**Single PDF outside the inbox flow**:
```bash
python -m ingest.add_doc one \
  --pdf /path/X.pdf --collection SAP --url "https://..."
```

**Skip the URL** (consistency check will warn):
```bash
python -m ingest.add_doc run --allow-missing-urls
```

**Re-run a PDF from scratch** (ignores checkpoints):
```bash
python -m ingest.add_doc one --pdf data/pdf/{collection}/X.pdf \
  --collection {collection} --url "..." --purge
```

## What to spot-check after a run

1. **Batch summary** at end of `run` output — every row should say `[OK]`.
2. **Lint report** at `.add_doc_state/{stem}_review.json` — Claude flags MD/PDF discrepancies. The `auto_safe: true` ones were applied automatically (see `_review.diff` for what changed). The `auto_safe: false` ones need your eyes — typically broken tables, wrong numbers, OCR misreads. Fix in `data/md/{collection}/{stem}.md`, then re-run with `--purge`.
3. **summary.json** — confirm the entry for the new PDF looks right.
4. **Streamlit query** — `streamlit run Valuation_search.py`, filter to the new collection, ask a question the doc would answer.

## File layout

- `data/inbox/` — drop zone (this folder). PDFs are moved out after success.
- `data/inbox/manifest.csv` — per-PDF row: `pdf,collection,url`.
- `data/inbox/last_run.log` — per-row status from the last `run`.
- `data/md/{collection}/` — converted Markdown (source of truth for embeddings).
- `data/pdf/{collection}/` — final PDF home.
- `data/summary.json` — per-doc Claude summaries (Title/Publisher/Purpose/Key Points/Implications).
- `data/document_list.json` — per-collection file listing, rebuilt from `data/pdf/` each run.
- `data/document_link.json` — `{pdf_filename: source_url}` for the UI.
- `data/parents/{collection}.jsonl` — sidecar parent blocks for context expansion.
- `.add_doc_state/{stem}.json` — per-PDF checkpoint; safe to `rm` to force a full re-run.

## Code map (when something needs changing)

- `ingest/add_doc.py` — CLI orchestrator. The six `_stage_*` functions are the pipeline stages.
- `ingest/pdf2md.py` — MathPix wrapper (`MATHPIX_APP_ID` + `MATHPIX_APP_KEY` in `.streamlit/secrets.toml`).
- `ingest/md_review.py` — Claude lint + safe-fix.
- `ingest/summarize.py` — Claude summary generator.
- `ingest/classify.py` — optional category suggester (uses Anthropic PDF input).
- `ingest/manifest.py` — `document_list.json` + `document_link.json` updaters.
- `ingest/inbox.py` — manifest CSV IO + per-PDF checkpoint state.
- `ingest/run.py` — the underlying chunk/embed/upsert pipeline (reused, not re-implemented).
- `valact/settings.py` — collections list, model names, paths, Pinecone index.

## Common gotchas

- **MathPix credentials live in `.streamlit/secrets.toml`** (not `.env`). Both `MATHPIX_APP_ID` and `MATHPIX_APP_KEY` are required.
- **Collection must be one of the 12** in `valact/settings.py` `COLLECTIONS`. Typos will be rejected at run time.
- **`run` won't process a row with empty `collection`** — fill it in the CSV.
- **URLs aren't auto-detected.** If you don't supply one, pass `--allow-missing-urls`.
- **Lint can have false positives** — review the report before trusting it. Claude flags issues it *thinks* exist; verify against the PDF.
