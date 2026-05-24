from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path

from valact.settings import (
    ADD_DOC_STATE_PATH,
    COLLECTIONS,
    INBOX_MANIFEST_PATH,
    INBOX_PATH,
)

CSV_FIELDS = ["pdf", "collection", "url"]
CSV_HEADER_COMMENT = (
    "# ValAct_RAG inbox manifest. Edit `collection` and `url` for each row, then run "
    "`python -m ingest.add_doc run`.\n"
    f"# Valid collections: {', '.join(COLLECTIONS)}\n"
)


@dataclass
class ManifestRow:
    pdf: str
    collection: str = ""
    url: str = ""
    extra: dict = field(default_factory=dict)

    @property
    def stem(self) -> str:
        return Path(self.pdf).stem

    @property
    def pdf_filename(self) -> str:
        return Path(self.pdf).name


def inbox_dir() -> Path:
    p = Path(INBOX_PATH)
    p.mkdir(parents=True, exist_ok=True)
    return p


def scan_inbox() -> list[Path]:
    return sorted(p for p in inbox_dir().glob("*.pdf") if p.is_file())


def load_manifest(path: str | Path = INBOX_MANIFEST_PATH) -> list[ManifestRow]:
    path = Path(path)
    if not path.exists():
        return []
    rows: list[ManifestRow] = []
    with path.open("r", encoding="utf-8", newline="") as fh:
        lines = [ln for ln in fh if not ln.lstrip().startswith("#")]
    if not lines:
        return []
    reader = csv.DictReader(lines)
    for r in reader:
        if not r.get("pdf"):
            continue
        rows.append(
            ManifestRow(
                pdf=r["pdf"].strip(),
                collection=(r.get("collection") or "").strip(),
                url=(r.get("url") or "").strip(),
            )
        )
    return rows


def save_manifest(
    rows: list[ManifestRow], path: str | Path = INBOX_MANIFEST_PATH
) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        fh.write(CSV_HEADER_COMMENT)
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for r in rows:
            writer.writerow({"pdf": r.pdf, "collection": r.collection, "url": r.url})
    return path


def merge_with_existing(
    pdfs: list[Path],
    existing: list[ManifestRow],
) -> list[ManifestRow]:
    by_pdf = {r.pdf_filename: r for r in existing}
    out: list[ManifestRow] = list(existing)
    for p in pdfs:
        if p.name not in by_pdf:
            out.append(ManifestRow(pdf=p.name))
    return out


# --- per-PDF checkpoint state -----------------------------------------------

STAGES = ["convert", "review", "summarize", "manifest", "embed", "place_pdf"]


def state_dir() -> Path:
    p = Path(ADD_DOC_STATE_PATH)
    p.mkdir(parents=True, exist_ok=True)
    return p


def state_path(stem: str) -> Path:
    return state_dir() / f"{stem}.json"


def load_state(stem: str) -> dict:
    p = state_path(stem)
    if not p.exists():
        return {"stem": stem, "done": []}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"stem": stem, "done": []}


def save_state(state: dict) -> None:
    p = state_path(state["stem"])
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def mark_done(stem: str, stage: str, **info) -> dict:
    state = load_state(stem)
    if stage not in state.get("done", []):
        state.setdefault("done", []).append(stage)
    state[stage] = info or True
    save_state(state)
    return state


def is_done(stem: str, stage: str) -> bool:
    state = load_state(stem)
    return stage in state.get("done", [])


def clear_state(stem: str) -> None:
    p = state_path(stem)
    if p.exists():
        p.unlink()
