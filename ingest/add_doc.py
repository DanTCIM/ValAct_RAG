from __future__ import annotations

import argparse
import shutil
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from valact.settings import (
    ADD_DOC_STATE_PATH,
    BASE_MD_PATH,
    BASE_PDF_PATH,
    COLLECTIONS,
    INBOX_MANIFEST_PATH,
    PINECONE_INDEX,
)

from ingest import classify, manifest, md_review, pdf2md, summarize
from ingest.inbox import (
    STAGES,
    ManifestRow,
    inbox_dir,
    is_done,
    load_manifest,
    mark_done,
    merge_with_existing,
    save_manifest,
    scan_inbox,
    state_dir,
)
from ingest.run import ensure_index, ingest_file


@dataclass
class RowResult:
    pdf: str
    ok: bool
    stages_run: list[str]
    error: str = ""


# --- scaffold ---------------------------------------------------------------


def _prompt_choice(suggestion: classify.Suggestion) -> str:
    while True:
        choice = input("    [a]ccept / [c]hange / [s]kip / [q]uit  → ").strip().lower()
        if choice in {"a", "c", "s", "q"}:
            break
        print("    please enter a, c, s, or q")
    if choice == "a":
        return suggestion.collection
    if choice == "s":
        return ""
    if choice == "q":
        raise KeyboardInterrupt
    # choice == "c"
    print("    Pick a collection:")
    for i, c in enumerate(COLLECTIONS, 1):
        print(f"      [{i:2d}] {c}")
    while True:
        raw = input("    number → ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(COLLECTIONS):
            return COLLECTIONS[int(raw) - 1]
        print("    invalid number")


def cmd_scaffold(args: argparse.Namespace) -> int:
    pdfs = scan_inbox()
    if not pdfs:
        print(f"No PDFs found in {inbox_dir()}. Drop files there and re-run.")
        return 0

    existing = load_manifest(args.manifest)
    rows = merge_with_existing(pdfs, existing)
    by_pdf = {r.pdf: r for r in rows}

    if args.suggest:
        new_rows = [r for r in rows if r.pdf in {p.name for p in pdfs} and not r.collection]
        total = len(new_rows)
        for i, row in enumerate(new_rows, 1):
            pdf_path = inbox_dir() / row.pdf
            print(f"\n[{i}/{total}] {row.pdf}")
            try:
                sugg = classify.suggest_collection(pdf_path)
            except Exception as exc:
                print(f"    classify failed: {exc}")
                continue
            print(f"    Suggested: {sugg.collection}   (confidence {sugg.confidence:.2f})")
            if sugg.reason:
                print(f"    Reason:    {sugg.reason}")

            if args.auto_accept_above and sugg.confidence >= args.auto_accept_above:
                print(f"    [auto-accept ≥ {args.auto_accept_above:.2f}]")
                by_pdf[row.pdf].collection = sugg.collection
                continue
            try:
                picked = _prompt_choice(sugg)
            except KeyboardInterrupt:
                print("\n  quit — saving manifest with progress so far")
                break
            by_pdf[row.pdf].collection = picked

    out = save_manifest(list(by_pdf.values()), args.manifest)
    print(f"\nWrote {out} ({len(by_pdf)} row(s)).")
    print("Next: fill in any blank `collection`/`url` columns, then run `python -m ingest.add_doc run`.")
    return 0


# --- per-row stage runners --------------------------------------------------


def _state_review_json(stem: str) -> Path:
    return Path(ADD_DOC_STATE_PATH) / f"{stem}_review.json"


def _state_review_diff(stem: str) -> Path:
    return Path(ADD_DOC_STATE_PATH) / f"{stem}_review.diff"


def _md_path_for(stem: str, collection: str) -> Path:
    return Path(BASE_MD_PATH) / collection / f"{stem}.md"


def _stage_convert(row: ManifestRow, pdf_src: Path, force: bool) -> Path:
    md_out = _md_path_for(row.stem, row.collection)
    if not force and md_out.exists() and is_done(row.stem, "convert"):
        print(f"  [convert] already done → {md_out}")
        return md_out
    md_path = pdf2md.convert_pdf(pdf_src, md_out.parent)
    mark_done(row.stem, "convert", md_path=str(md_path))
    return md_path


def _stage_review(
    row: ManifestRow,
    pdf_src: Path,
    md_path: Path,
    mode: str,
    force: bool,
) -> None:
    if mode == "skip":
        mark_done(row.stem, "review", skipped=True)
        print("  [review] skipped (mode=skip)")
        return
    if not force and is_done(row.stem, "review"):
        print("  [review] already done")
        return
    if mode == "manual":
        print(f"  [review] open and inspect: {md_path}")
        input("    press Enter to continue → ")
        mark_done(row.stem, "review", mode="manual")
        return

    print("  [review] linting with Claude...")
    issues = md_review.lint_md(md_path, pdf_src)
    md_review.save_report(issues, _state_review_json(row.stem))
    print(md_review.summarize_issues(issues))

    if mode in {"auto", "lint"} and issues:
        applied = md_review.apply_fixes(
            md_path,
            issues,
            mode="safe" if mode == "auto" else "safe",
            diff_path=_state_review_diff(row.stem),
        )
        if applied:
            print(f"    applied {applied} safe fix(es); diff at {_state_review_diff(row.stem)}")

    mark_done(row.stem, "review", mode=mode, n_issues=len(issues))


def _stage_summarize(row: ManifestRow, md_path: Path, force: bool) -> None:
    if not force and is_done(row.stem, "summarize"):
        print("  [summarize] already done")
        return
    print("  [summarize] generating with Claude...")
    entry = summarize.summarize_md(md_path, row.collection)
    summarize.upsert_summary(row.pdf_filename, entry)
    mark_done(row.stem, "summarize")


def _stage_manifest(row: ManifestRow, allow_missing_url: bool, force: bool) -> None:
    if not force and is_done(row.stem, "manifest"):
        print("  [manifest] already done")
        return
    if row.url:
        manifest.set_document_link(row.pdf_filename, row.url)
    elif not allow_missing_url:
        raise RuntimeError(
            f"empty url for {row.pdf_filename}; pass --allow-missing-urls to ignore"
        )
    # document_list rebuilds from data/pdf/, so we defer the final rebuild to
    # after place_pdf. Do an interim rebuild here too so warnings reflect state.
    manifest.rebuild_document_list()
    mark_done(row.stem, "manifest", url=row.url)


def _stage_embed(row: ManifestRow, md_path: Path, index_name: str, force: bool) -> None:
    if not force and is_done(row.stem, "embed"):
        print("  [embed] already done")
        return
    print("  [embed] chunk + embed + upsert...")
    n_chunks, n_parents = ingest_file(
        md_path, collection=row.collection, index_name=index_name, purged=False
    )
    mark_done(row.stem, "embed", chunks=n_chunks, parents=n_parents)


def _stage_place_pdf(row: ManifestRow, pdf_src: Path, force: bool) -> None:
    if not force and is_done(row.stem, "place_pdf"):
        print("  [place_pdf] already done")
        return
    dest_dir = Path(BASE_PDF_PATH) / row.collection
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / row.pdf_filename

    if pdf_src.parent == inbox_dir():
        shutil.move(str(pdf_src), str(dest))
        print(f"  [place_pdf] moved → {dest}")
    else:
        shutil.copy2(pdf_src, dest)
        print(f"  [place_pdf] copied → {dest}")

    manifest.rebuild_document_list()
    mark_done(row.stem, "place_pdf", dest=str(dest))


# --- per-row dispatcher -----------------------------------------------------


def _process_row(
    row: ManifestRow,
    *,
    pdf_src: Path,
    index_name: str,
    review_mode: str,
    allow_missing_url: bool,
    force: bool,
) -> RowResult:
    stages_run: list[str] = []
    try:
        if row.collection not in COLLECTIONS:
            raise RuntimeError(
                f"invalid collection {row.collection!r} (valid: {', '.join(COLLECTIONS)})"
            )
        md_path = _stage_convert(row, pdf_src, force)
        stages_run.append("convert")

        _stage_review(row, pdf_src, md_path, review_mode, force)
        stages_run.append("review")

        _stage_summarize(row, md_path, force)
        stages_run.append("summarize")

        _stage_manifest(row, allow_missing_url, force)
        stages_run.append("manifest")

        _stage_embed(row, md_path, index_name, force)
        stages_run.append("embed")

        _stage_place_pdf(row, pdf_src, force)
        stages_run.append("place_pdf")

        return RowResult(pdf=row.pdf_filename, ok=True, stages_run=stages_run)
    except Exception as exc:
        traceback.print_exc()
        return RowResult(
            pdf=row.pdf_filename,
            ok=False,
            stages_run=stages_run,
            error=f"{type(exc).__name__}: {exc}",
        )


# --- run --------------------------------------------------------------------


def _parse_row_range(spec: str, n: int) -> range:
    if not spec:
        return range(n)
    if "-" in spec:
        a, b = spec.split("-", 1)
        lo = int(a) - 1 if a else 0
        hi = int(b) if b else n
    else:
        lo = int(spec) - 1
        hi = lo + 1
    return range(max(0, lo), min(n, hi))


def cmd_run(args: argparse.Namespace) -> int:
    rows = load_manifest(args.manifest)
    if not rows:
        print(f"No rows in {args.manifest}. Run `scaffold` first.")
        return 1

    ensure_index(args.index)
    state_dir()  # touch

    indices = _parse_row_range(args.rows or "", len(rows))
    selected = [rows[i] for i in indices]

    results: list[RowResult] = []
    for i, row in enumerate(selected, 1):
        pdf_src = inbox_dir() / row.pdf
        if not pdf_src.exists():
            # likely already moved into data/pdf/{collection}/ by a prior run
            pdf_src_dest = Path(BASE_PDF_PATH) / row.collection / row.pdf_filename
            if pdf_src_dest.exists():
                pdf_src = pdf_src_dest
            else:
                results.append(
                    RowResult(
                        pdf=row.pdf_filename,
                        ok=False,
                        stages_run=[],
                        error=f"PDF not found: {pdf_src}",
                    )
                )
                continue
        print(f"\n=== [{i}/{len(selected)}] {row.pdf} → {row.collection or '(blank!)'} ===")
        if args.purge:
            from ingest.inbox import clear_state

            clear_state(row.stem)
        result = _process_row(
            row,
            pdf_src=pdf_src,
            index_name=args.index,
            review_mode=args.review_mode,
            allow_missing_url=args.allow_missing_urls,
            force=args.purge,
        )
        results.append(result)

    # final consistency check
    missing = manifest.check_consistency()
    if missing:
        print("\n[warn] document_list entries missing in document_link.json:")
        for m in missing[:20]:
            print(f"  - {m}")
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more")

    print("\n=== batch summary ===")
    for r in results:
        status = "OK" if r.ok else "FAIL"
        stages = ",".join(r.stages_run) if r.stages_run else "-"
        line = f"  [{status}] {r.pdf}   stages: {stages}"
        if r.error:
            line += f"   error: {r.error}"
        print(line)

    log_path = Path(INBOX_MANIFEST_PATH).parent / "last_run.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        "\n".join(
            f"{'OK' if r.ok else 'FAIL'}\t{r.pdf}\t{','.join(r.stages_run)}\t{r.error}"
            for r in results
        )
        + "\n",
        encoding="utf-8",
    )
    return 0 if all(r.ok for r in results) else 2


# --- one --------------------------------------------------------------------


def cmd_one(args: argparse.Namespace) -> int:
    pdf_path = Path(args.pdf).resolve()
    if not pdf_path.is_file():
        print(f"PDF not found: {pdf_path}")
        return 1
    if args.collection not in COLLECTIONS:
        print(f"Invalid collection {args.collection!r}. Valid: {', '.join(COLLECTIONS)}")
        return 1

    ensure_index(args.index)
    row = ManifestRow(pdf=pdf_path.name, collection=args.collection, url=args.url or "")
    result = _process_row(
        row,
        pdf_src=pdf_path,
        index_name=args.index,
        review_mode=args.review_mode,
        allow_missing_url=args.allow_missing_urls,
        force=args.purge,
    )
    if result.ok:
        print(f"\nOK — stages: {','.join(result.stages_run)}")
        return 0
    print(f"\nFAIL — {result.error}")
    return 2


# --- entry point ------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python -m ingest.add_doc",
        description=(
            "End-to-end document ingestion: PDF → MD (MathPix) → Claude review → "
            "summary → manifest JSONs → vector DB."
        ),
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("scaffold", help="Scan inbox and write/update manifest CSV")
    sp.add_argument("--manifest", default=INBOX_MANIFEST_PATH)
    sp.add_argument(
        "--suggest",
        action="store_true",
        help="Ask Claude to propose a collection per PDF; interactive a/c/s prompt",
    )
    sp.add_argument(
        "--auto-accept-above",
        type=float,
        default=0.0,
        help="With --suggest, auto-accept proposals at or above this confidence",
    )
    sp.set_defaults(func=cmd_scaffold)

    rp = sub.add_parser("run", help="Process every row in the manifest")
    rp.add_argument("--manifest", default=INBOX_MANIFEST_PATH)
    rp.add_argument("--rows", default="", help='Range like "1-3" or single index "2"')
    rp.add_argument("--index", default=PINECONE_INDEX)
    rp.add_argument(
        "--review-mode",
        choices=["auto", "lint", "manual", "skip"],
        default="auto",
        help="auto = lint+safe-fix (default); lint = lint only; manual = pause; skip = no review",
    )
    rp.add_argument("--allow-missing-urls", action="store_true")
    rp.add_argument(
        "--purge", action="store_true", help="Ignore checkpoints; re-run every stage"
    )
    rp.set_defaults(func=cmd_run)

    op = sub.add_parser("one", help="Process a single PDF without using the manifest CSV")
    op.add_argument("--pdf", required=True)
    op.add_argument("--collection", required=True)
    op.add_argument("--url", default="")
    op.add_argument("--index", default=PINECONE_INDEX)
    op.add_argument(
        "--review-mode",
        choices=["auto", "lint", "manual", "skip"],
        default="auto",
    )
    op.add_argument("--allow-missing-urls", action="store_true")
    op.add_argument("--purge", action="store_true")
    op.set_defaults(func=cmd_one)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

# When stages are listed:
__all__ = ["main", "STAGES"]
