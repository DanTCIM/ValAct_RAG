"""Evaluate the Jev follow-up and on-topic decisions against labeled cases.

Reads scripts/gate_cases.txt, plus the collection-labeled queries in
scripts/queries.txt and scripts/router_queries.txt as on-topic positives, and
reports accuracy at the configured thresholds with the probability spread per
label so the thresholds can be retuned.

    python scripts/eval_gates.py
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from valact.router import _followup_impl, _route_impl
from valact.settings import AUTO_OFFTOPIC_THRESHOLD, FOLLOWUP_THRESHOLD

HERE = Path(__file__).resolve().parent


def _lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [
        ln.strip()
        for ln in path.read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.lstrip().startswith("#")
    ]


def _load():
    followup: list[tuple[bool, str, str]] = []
    ontopic: list[tuple[bool, str]] = []
    for line in _lines(HERE / "gate_cases.txt"):
        parts = line.split("|")
        if parts[0] == "followup" and len(parts) == 4:
            followup.append((parts[1] == "yes", parts[2], parts[3]))
        elif parts[0] == "ontopic" and len(parts) == 3:
            ontopic.append((parts[1] == "yes", parts[2]))
    for path, n in ((HERE / "queries.txt", 3), (HERE / "router_queries.txt", 2)):
        for line in _lines(path):
            parts = line.split("|", n - 1)
            if len(parts) == n:
                ontopic.append((True, parts[-1].strip()))
    return followup, ontopic


def _spread(probs: list[float]) -> str:
    if not probs:
        return "n/a"
    return f"min {min(probs):.2f}  median {statistics.median(probs):.2f}  max {max(probs):.2f}"


def _report(name: str, rows: list[tuple[bool, float | None, str]], predict) -> None:
    failed = [text for _, p, text in rows if p is None]
    scored = [(label, p, text) for label, p, text in rows if p is not None]
    correct = sum(predict(p) == label for label, p, _ in scored)
    print(f"\n== {name} ==")
    print(f"accuracy: {correct}/{len(scored)}" + (f"  ({len(failed)} failed calls)" if failed else ""))
    print(f"label yes: {_spread([p for label, p, _ in scored if label])}")
    print(f"label no:  {_spread([p for label, p, _ in scored if not label])}")
    for label, p, text in scored:
        if predict(p) != label:
            print(f"  WRONG want {'yes' if label else 'no ':<3} p={p:.2f} :: {text[:90]}")


def main() -> int:
    followup, ontopic = _load()

    rows = [(label, _followup_impl(prev, cur), f"{prev} -> {cur}") for label, prev, cur in followup]
    _report(f"follow-up (yes if p >= {FOLLOWUP_THRESHOLD})", rows, lambda p: p >= FOLLOWUP_THRESHOLD)

    rows = []
    for label, query in ontopic:
        r = _route_impl(query)
        rows.append((label, None if r is None else r.on_topic, query))
    _report(
        f"on-topic (off-topic if p < {AUTO_OFFTOPIC_THRESHOLD})",
        rows,
        lambda p: p >= AUTO_OFFTOPIC_THRESHOLD,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
