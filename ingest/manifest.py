from __future__ import annotations

import json
from pathlib import Path

from valact.settings import (
    BASE_PDF_PATH,
    DOCUMENT_LINK_PATH,
    DOCUMENT_LIST_PATH,
)


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _save_json(data: dict, path: Path, *, indent: int | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=indent, ensure_ascii=False), encoding="utf-8"
    )


def rebuild_document_list(
    base_pdf_path: str | Path = BASE_PDF_PATH,
    *,
    out_path: str | Path = DOCUMENT_LIST_PATH,
) -> dict:
    base = Path(base_pdf_path)
    folders: dict[str, list[str]] = {}
    if base.exists():
        for entry in sorted(base.iterdir()):
            if not entry.is_dir():
                continue
            files = ["All"]
            for f in entry.iterdir():
                if f.name == ".DS_Store" or not f.is_file():
                    continue
                files.append(f.name)
            files[1:] = sorted(files[1:])
            folders[entry.name] = files
    _save_json(folders, Path(out_path))  # compact, matches existing style
    return folders


def set_document_link(
    filename: str,
    url: str | None,
    *,
    path: str | Path = DOCUMENT_LINK_PATH,
) -> Path:
    p = Path(path)
    data = _load_json(p)
    if url:
        data[filename] = url
    _save_json(data, p, indent=4)  # indented, matches existing style
    return p


def check_consistency(
    *,
    list_path: str | Path = DOCUMENT_LIST_PATH,
    link_path: str | Path = DOCUMENT_LINK_PATH,
) -> list[str]:
    list_data = _load_json(Path(list_path))
    link_data = _load_json(Path(link_path))
    missing: list[str] = []
    for collection, items in list_data.items():
        for item in items:
            if item == "All":
                continue
            if item not in link_data:
                missing.append(f"{collection}/{item}")
    return missing
