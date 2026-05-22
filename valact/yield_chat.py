from __future__ import annotations

import json
from typing import Iterator

import pandas as pd
import streamlit as st

from valact.clients import get_anthropic_client
from valact.settings import ANTHROPIC_MODEL


def _tool_specs(series_columns: list[str]) -> list[dict]:
    series_enum = list(series_columns)
    return [
        {
            "name": "filter_window",
            "description": (
                "Return a markdown table of selected series values over a date window. "
                "Use this when the user asks about a specific period or recent values."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "series": {
                        "type": "array",
                        "items": {"type": "string", "enum": series_enum},
                        "description": "Which series to include.",
                    },
                    "start_date": {"type": "string", "description": "YYYY-MM-DD"},
                    "end_date": {"type": "string", "description": "YYYY-MM-DD"},
                    "frequency": {
                        "type": "string",
                        "enum": ["daily", "monthly", "quarterly"],
                        "description": "Sampling frequency. Default: monthly.",
                    },
                },
                "required": ["series", "start_date", "end_date"],
            },
        },
        {
            "name": "summarize_window",
            "description": (
                "Return summary statistics (min, max, mean, latest, change) for selected "
                "series over a date window."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "series": {
                        "type": "array",
                        "items": {"type": "string", "enum": series_enum},
                    },
                    "start_date": {"type": "string", "description": "YYYY-MM-DD"},
                    "end_date": {"type": "string", "description": "YYYY-MM-DD"},
                },
                "required": ["series", "start_date", "end_date"],
            },
        },
        {
            "name": "value_on_date",
            "description": (
                "Return the value of one or more series on a specific date. "
                "If exact date is missing, returns the nearest prior trading day."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "series": {
                        "type": "array",
                        "items": {"type": "string", "enum": series_enum},
                    },
                    "date": {"type": "string", "description": "YYYY-MM-DD"},
                },
                "required": ["series", "date"],
            },
        },
    ]


def _safe_series(df: pd.DataFrame, cols: list[str]) -> list[str]:
    return [c for c in cols if c in df.columns]


def _slice(df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    mask = (df["Date"] >= pd.to_datetime(start)) & (df["Date"] <= pd.to_datetime(end))
    return df.loc[mask].copy()


def _resample(window: pd.DataFrame, frequency: str, cols: list[str]) -> pd.DataFrame:
    if frequency == "daily" or window.empty:
        return window[["Date", *cols]]
    rule = {"monthly": "M", "quarterly": "Q"}.get(frequency, "M")
    resampled = (
        window.set_index("Date")[cols]
        .resample(rule)
        .last()
        .dropna(how="all")
        .reset_index()
    )
    return resampled


def _exec_tool(name: str, args: dict, df: pd.DataFrame) -> str:
    try:
        if name == "filter_window":
            cols = _safe_series(df, args.get("series", []))
            window = _slice(df, args["start_date"], args["end_date"])
            window = _resample(window, args.get("frequency", "monthly"), cols)
            if window.empty:
                return "No data in the requested window."
            window = window.copy()
            window["Date"] = window["Date"].dt.strftime("%Y-%m-%d")
            return window.to_markdown(index=False, floatfmt=".3f")

        if name == "summarize_window":
            cols = _safe_series(df, args.get("series", []))
            window = _slice(df, args["start_date"], args["end_date"])[cols]
            if window.empty:
                return "No data in the requested window."
            rows = []
            for c in cols:
                s = pd.to_numeric(window[c], errors="coerce").dropna()
                if s.empty:
                    rows.append({"series": c, "n": 0})
                    continue
                rows.append(
                    {
                        "series": c,
                        "n": int(s.shape[0]),
                        "min": round(float(s.min()), 4),
                        "max": round(float(s.max()), 4),
                        "mean": round(float(s.mean()), 4),
                        "latest": round(float(s.iloc[-1]), 4),
                        "change": round(float(s.iloc[-1] - s.iloc[0]), 4),
                    }
                )
            return pd.DataFrame(rows).to_markdown(index=False)

        if name == "value_on_date":
            cols = _safe_series(df, args.get("series", []))
            d = pd.to_datetime(args["date"])
            sub = df[df["Date"] <= d].sort_values("Date")
            if sub.empty:
                return "No data on or before that date."
            row = sub.iloc[-1]
            actual = row["Date"].strftime("%Y-%m-%d")
            vals = {c: float(row[c]) if pd.notna(row[c]) else None for c in cols}
            return json.dumps({"date_used": actual, "values": vals}, default=str)

        return f"Unknown tool: {name}"
    except KeyError as exc:
        return f"Missing argument: {exc}"
    except Exception as exc:  # noqa: BLE001
        return f"Tool error: {exc}"


def _system_prompt(label: str, columns: list[str], latest_date: str) -> str:
    return (
        f"You are a fixed-income analyst answering questions about {label}. "
        f"Available series: {', '.join(columns)}. Most recent data point: {latest_date}. "
        "Use the provided tools to fetch precise values; do not guess numbers. "
        "Give concise, numerically grounded answers. State percentages with two decimals."
    )


def chat_about_yields(
    *,
    container,
    user_query: str,
    history: list[dict],
    df: pd.DataFrame,
    series_columns: list[str],
    label: str,
    latest_date: str,
) -> str:
    client = get_anthropic_client()
    tools = _tool_specs(series_columns)
    system = _system_prompt(label, series_columns, latest_date)

    messages = [
        {"role": m["role"], "content": m["content"]}
        for m in history
        if m.get("role") in ("user", "assistant")
    ]
    messages.append({"role": "user", "content": user_query})

    stream_box = container.empty()
    text_so_far = ""
    max_iters = 4

    for _ in range(max_iters):
        with client.messages.stream(
            model=ANTHROPIC_MODEL,
            system=system,
            tools=tools,
            messages=messages,
            max_tokens=1024,
        ) as stream:
            for delta in stream.text_stream:
                text_so_far += delta
                stream_box.markdown(text_so_far)
            final = stream.get_final_message()

        if final.stop_reason != "tool_use":
            return text_so_far

        tool_uses = [b for b in final.content if b.type == "tool_use"]
        messages.append({"role": "assistant", "content": final.content})

        results = []
        for tu in tool_uses:
            result = _exec_tool(tu.name, tu.input, df)
            results.append(
                {"type": "tool_result", "tool_use_id": tu.id, "content": result}
            )
        messages.append({"role": "user", "content": results})
        text_so_far += "\n\n"

    return text_so_far


def render_chat_panel(
    *,
    df: pd.DataFrame,
    series_columns: list[str],
    label: str,
    latest_date: str,
    welcome: str,
    placeholder: str,
    state_key: str = "messages",
):
    if state_key not in st.session_state or st.sidebar.button(
        "Clear conversation history", key=f"{state_key}_clear"
    ):
        st.session_state[state_key] = [{"role": "assistant", "content": welcome}]

    for msg in st.session_state[state_key]:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder=placeholder):
        st.session_state[state_key].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        with st.chat_message("assistant"):
            container = st.container()
            try:
                answer = chat_about_yields(
                    container=container,
                    user_query=prompt,
                    history=st.session_state[state_key][:-1],
                    df=df,
                    series_columns=series_columns,
                    label=label,
                    latest_date=latest_date,
                )
            except Exception as exc:  # noqa: BLE001
                answer = f"Model call failed: {exc}"
                st.error(answer)
        st.session_state[state_key].append({"role": "assistant", "content": answer})
