from __future__ import annotations

import argparse
import os
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

from valact.clients import get_anthropic_client
from valact.rag import StageTimings, run_retrieval
from valact.settings import ANTHROPIC_MODEL


def _load_queries(path: Path) -> list[tuple[str, str, str]]:
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("|", 2)
        if len(parts) != 3:
            continue
        out.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))
    return out


def _time_first_token(query: str, parents) -> tuple[float, int]:
    client = get_anthropic_client()
    from valact.rag import build_messages

    system, messages = build_messages(query, [], parents)
    t0 = time.perf_counter()
    first = None
    total_tokens = 0
    with client.messages.stream(
        model=ANTHROPIC_MODEL,
        system=system,
        messages=messages,
        max_tokens=256,
    ) as stream:
        for chunk in stream.text_stream:
            if first is None and chunk:
                first = time.perf_counter() - t0
            total_tokens += 1
    return first or 0.0, total_tokens


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--queries", default=str(Path(__file__).parent / "queries.txt"))
    ap.add_argument("--runs", type=int, default=2, help="Repeats per query (after warmup)")
    ap.add_argument("--no-llm", action="store_true", help="Skip LLM timing")
    ap.add_argument("--no-mmr", action="store_true")
    ap.add_argument("--top-k", type=int, default=40)
    ap.add_argument("--top-n", type=int, default=10)
    args = ap.parse_args()

    queries = _load_queries(Path(args.queries))
    if not queries:
        print("No queries loaded")
        return 1

    print(
        f"{'Q#':<3} {'embed':>8} {'pine':>8} {'rerank':>8} {'expand':>8} "
        f"{'retr':>8} {'first':>8} {'collection':<12} {'query':<50}"
    )
    print("-" * 130)

    agg = {"embed": [], "pine": [], "rerank": [], "expand": [], "retr": [], "first": []}

    for i, (collection, document, query) in enumerate(queries, start=1):
        run_retrieval(
            query,
            collection=collection,
            document=document if document != "All" else None,
            top_k=args.top_k,
            top_n=args.top_n,
            use_mmr=not args.no_mmr,
        )

        for _ in range(args.runs):
            timings = StageTimings()
            _docs, parents = run_retrieval(
                query,
                collection=collection,
                document=document if document != "All" else None,
                top_k=args.top_k,
                top_n=args.top_n,
                use_mmr=not args.no_mmr,
                timings=timings,
            )
            first_s = 0.0
            if not args.no_llm:
                try:
                    first_s, _ = _time_first_token(query, parents)
                except Exception as exc:
                    print(f"  LLM error: {exc}")

            agg["embed"].append(timings.embed_s)
            agg["pine"].append(timings.pinecone_s)
            agg["rerank"].append(timings.rerank_s)
            agg["expand"].append(timings.expand_s)
            agg["retr"].append(timings.total_s)
            agg["first"].append(first_s)

            print(
                f"{i:<3} {timings.embed_s:>8.3f} {timings.pinecone_s:>8.3f} "
                f"{timings.rerank_s:>8.3f} {timings.expand_s:>8.3f} "
                f"{timings.total_s:>8.3f} {first_s:>8.3f} {collection:<12} {query[:50]:<50}"
            )

    print("-" * 130)
    for k, vals in agg.items():
        if not vals:
            continue
        med = statistics.median(vals)
        p95 = sorted(vals)[int(0.95 * (len(vals) - 1))]
        print(f"  {k:<8} median={med:.3f}s  p95={p95:.3f}s  n={len(vals)}")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
