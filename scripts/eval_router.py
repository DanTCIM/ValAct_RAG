"""Evaluate Jev collection routing against labeled queries.

Reads scripts/queries.txt (collection|document|query, shared with bench.py) and
scripts/router_queries.txt (collection|query) and reports how often the labeled
collection lands top-1, in the top 3, and above the pre-check threshold.

    python scripts/eval_router.py [--threshold 0.5]
"""

from __future__ import annotations

import argparse
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from valact.router import _rank_impl
from valact.settings import AUTO_PRECHECK_THRESHOLD

QUERIES_PATH = Path(__file__).resolve().parent / "queries.txt"
ROUTER_QUERIES_PATH = Path(__file__).resolve().parent / "router_queries.txt"


def _load() -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for path, query_index in ((QUERIES_PATH, 2), (ROUTER_QUERIES_PATH, 1)):
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|", query_index)
            if len(parts) != query_index + 1:
                continue
            out.append((parts[0].strip(), parts[query_index].strip()))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=AUTO_PRECHECK_THRESHOLD)
    args = ap.parse_args()

    cases = _load()
    if not cases:
        print("no queries found")
        return 1

    top1 = top3 = prechecked = 0
    latencies: list[float] = []
    precheck_counts: list[int] = []
    misses: list[str] = []

    for expected, query in cases:
        t0 = time.perf_counter()
        ranking = _rank_impl(query)
        latencies.append((time.perf_counter() - t0) * 1000)
        if ranking is None:
            print(f"FAILED  {query[:60]}")
            continue

        order = [c for c, _ in ranking]
        scores = dict(ranking)
        above = [c for c, p in ranking if p >= args.threshold] or order[:1]

        top1 += order[0] == expected
        top3 += expected in order[:3]
        prechecked += expected in above
        precheck_counts.append(len(above))

        if order[0] != expected:
            misses.append(
                f"  want {expected:<12} got {order[0]:<12} "
                f"(p_expected={scores.get(expected, 0):.2f}, rank "
                f"{order.index(expected) + 1}) :: {query[:58]}"
            )

    n = len(cases)
    print(f"\nqueries: {n}  threshold: {args.threshold}")
    print(f"top-1 accuracy:      {top1}/{n} ({top1 / n:.0%})")
    print(f"top-3 recall:        {top3}/{n} ({top3 / n:.0%})")
    print(f"pre-checked:         {prechecked}/{n} ({prechecked / n:.0%})")
    print(f"domains pre-checked: mean {statistics.mean(precheck_counts):.1f}, "
          f"max {max(precheck_counts)}")
    print(f"latency ms:          mean {statistics.mean(latencies):.0f}, "
          f"p95 {sorted(latencies)[int(len(latencies) * 0.95) - 1]:.0f}")
    if misses:
        print("\ntop-1 misses:")
        print("\n".join(misses))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
