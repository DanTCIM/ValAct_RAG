from __future__ import annotations

import base64
import difflib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from valact.clients import get_anthropic_client
from valact.settings import ANTHROPIC_MODEL

REVIEW_MAX_TOKENS = 4096


@dataclass
class ReviewIssue:
    line: int
    severity: str  # high|med|low
    category: str  # header_hierarchy|broken_table|joined_paragraph|ocr_artifact|...
    message: str
    before: str
    after: str
    auto_safe: bool


_SAFE_CATEGORIES = {"header_hierarchy", "ocr_artifact", "image_link", "joined_paragraph"}

_LINT_INSTRUCTION = """You are reviewing a Markdown file that was OCR'd from a PDF (via MathPix).
The PDF is provided as ground truth. Find places where the Markdown structure or text diverges from the PDF in ways that would degrade RAG retrieval quality.

Focus on these categories ONLY:
- header_hierarchy: H1/H2/H3 levels are wrong or skipped vs. the PDF's visible hierarchy
- broken_table: a table in the PDF was parsed into prose, or columns/rows are wrong
- joined_paragraph: two distinct paragraphs in the PDF were concatenated without a blank line
- ocr_artifact: stray ligatures (e.g., 'fi', 'fl'), mojibake, or repeated junk characters
- image_link: a markdown image link `![](url)` slipped through (should be <img> tag)
- missing_section: a whole section visible in the PDF is absent from the MD
- math_garbled: math expressions clearly corrupted vs. the PDF

Return a JSON object with a single key "issues" whose value is an array. Each issue must have:
- line: int (1-based line number in the Markdown)
- severity: "high" | "med" | "low"
- category: one of the categories above
- message: short human-readable description
- before: the EXACT current text in the MD that needs changing (must match verbatim, including whitespace)
- after: the corrected text. Empty string means "delete the `before` text".
- auto_safe: boolean. True ONLY if applying `before -> after` is a clearly safe, local edit that cannot break surrounding content. Header level fixes, ligature replacements, single blank-line insertions, and <img> tag conversions are auto_safe. Table reconstruction and large rewrites are NOT auto_safe.

Use empty array if the MD looks faithful to the PDF. Do not invent issues. Prefer fewer, high-confidence issues over many speculative ones.
Return ONLY the JSON object, no prose."""


def _pdf_block(pdf_path: Path) -> dict:
    data = base64.standard_b64encode(pdf_path.read_bytes()).decode("utf-8")
    return {
        "type": "document",
        "source": {"type": "base64", "media_type": "application/pdf", "data": data},
        "cache_control": {"type": "ephemeral"},
    }


def _md_block(md_text: str) -> dict:
    numbered = "\n".join(f"{i + 1:5d}\t{line}" for i, line in enumerate(md_text.splitlines()))
    return {
        "type": "text",
        "text": f"# Markdown to review (with line numbers)\n\n{numbered}",
        "cache_control": {"type": "ephemeral"},
    }


def _strip_code_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z0-9]*\n", "", text, count=1)
        text = re.sub(r"\n?```\s*$", "", text)
    return text


def lint_md(md_path: Path, pdf_path: Path) -> list[ReviewIssue]:
    md_text = Path(md_path).read_text(encoding="utf-8")
    client = get_anthropic_client()

    resp = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=REVIEW_MAX_TOKENS,
        messages=[
            {
                "role": "user",
                "content": [
                    _pdf_block(Path(pdf_path)),
                    _md_block(md_text),
                    {"type": "text", "text": _LINT_INSTRUCTION},
                ],
            }
        ],
    )

    raw = "".join(block.text for block in resp.content if getattr(block, "type", None) == "text")
    raw = _strip_code_fence(raw)
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"lint_md: model returned non-JSON: {exc}\n---\n{raw[:1000]}") from exc

    issues_raw = payload.get("issues", []) if isinstance(payload, dict) else payload
    issues: list[ReviewIssue] = []
    for item in issues_raw:
        try:
            issues.append(
                ReviewIssue(
                    line=int(item.get("line", 0)),
                    severity=str(item.get("severity", "low")),
                    category=str(item.get("category", "")),
                    message=str(item.get("message", "")),
                    before=str(item.get("before", "")),
                    after=str(item.get("after", "")),
                    auto_safe=bool(item.get("auto_safe", False))
                    and str(item.get("category", "")) in _SAFE_CATEGORIES,
                )
            )
        except (TypeError, ValueError):
            continue
    return issues


def save_report(issues: list[ReviewIssue], path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"issues": [asdict(i) for i in issues]}
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def apply_fixes(
    md_path: Path,
    issues: list[ReviewIssue],
    *,
    mode: str = "safe",
    diff_path: Path | None = None,
) -> int:
    md_path = Path(md_path)
    original = md_path.read_text(encoding="utf-8")
    updated = original
    applied = 0

    to_apply = [i for i in issues if (mode == "all") or i.auto_safe]
    # Apply longest `before` first so we never partially overlap a longer fix with a shorter one.
    to_apply.sort(key=lambda i: len(i.before), reverse=True)

    for issue in to_apply:
        if not issue.before or issue.before not in updated:
            continue
        updated = updated.replace(issue.before, issue.after, 1)
        applied += 1

    if applied and updated != original:
        md_path.write_text(updated, encoding="utf-8")
        if diff_path is not None:
            diff = difflib.unified_diff(
                original.splitlines(keepends=True),
                updated.splitlines(keepends=True),
                fromfile=str(md_path) + " (before)",
                tofile=str(md_path) + " (after)",
            )
            Path(diff_path).parent.mkdir(parents=True, exist_ok=True)
            Path(diff_path).write_text("".join(diff), encoding="utf-8")
    return applied


def summarize_issues(issues: list[ReviewIssue]) -> str:
    if not issues:
        return "  no lint issues found"
    by_sev: dict[str, int] = {}
    for i in issues:
        by_sev[i.severity] = by_sev.get(i.severity, 0) + 1
    parts = [f"{c} {s}" for s, c in sorted(by_sev.items())]
    return f"  {len(issues)} issue(s): " + ", ".join(parts)
