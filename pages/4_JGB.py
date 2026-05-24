import io
import urllib.request

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from valact.yield_chat import render_chat_panel


PARQUET_URL = "https://pub-bedeea83f4c04f0abb342c6e246f8db5.r2.dev/jgb/yields.parquet"
OUTPUT_TENORS = ["1Y", "10Y", "30Y", "40Y"]
FX_COLUMN = "JPY/USD"


@st.cache_data(ttl=86400, show_spinner=False)
def load_jgb_data():
    # Cloudflare R2 public URLs reject the default Python-urllib UA with 403.
    req = urllib.request.Request(PARQUET_URL, headers={"User-Agent": "ValAct-RAG/1.0"})
    with urllib.request.urlopen(req) as resp:
        combined_df = pd.read_parquet(io.BytesIO(resp.read()))

    todays_date = combined_df["Date"].max().strftime("%Y-%m-%d")

    # Weekly resample for the long-range chart only (perf).
    chart_df = (
        combined_df.set_index("Date")
        .resample("W-FRI")
        .last()
        .reset_index()
    )

    month_end_df = combined_df.copy()
    month_end_df["YearMonth"] = month_end_df["Date"].dt.to_period("M")
    month_end_data = month_end_df.groupby("YearMonth").last().reset_index(drop=True)
    month_end_data = month_end_data[month_end_data["Date"] >= "2022-01-01"]
    month_end_data = month_end_data.set_index("Date")
    month_end_data.index = month_end_data.index.strftime("%Y-%m-%d")

    return combined_df, chart_df, todays_date, month_end_data


def _render_chart(chart_df: pd.DataFrame):
    melted = chart_df[["Date"] + OUTPUT_TENORS].melt(id_vars="Date", var_name="Ticker", value_name="Yield")
    melted["Yield"] = pd.to_numeric(melted["Yield"], errors="coerce")
    melted = melted.dropna(subset=["Yield"])
    melted = melted[melted["Date"] >= "2022-09-01"]

    y_start = np.floor(melted["Yield"].min() * 2) / 2
    y_end = np.ceil(melted["Yield"].max() * 2) / 2

    radio = alt.binding_radio(
        options=OUTPUT_TENORS + [None],
        labels=[label + " " for label in OUTPUT_TENORS] + ["All"],
        name="Ticker: ",
    )
    selection = alt.selection_point(fields=["Ticker"], bind=radio)

    base = (
        alt.Chart(melted)
        .mark_line()
        .encode(
            x="Date:T",
            y=alt.Y("Yield:Q", scale=alt.Scale(domain=[y_start, y_end])),
            color=alt.Color("Ticker:N", sort=OUTPUT_TENORS),
        )
        .add_params(selection)
        .transform_filter(selection)
    )

    hover = alt.selection_point(encodings=["x"], on="mouseover", nearest=True, empty=False)
    rule = (
        alt.Chart(melted)
        .mark_rule()
        .encode(
            x="Date:T",
            opacity=alt.condition(hover, alt.value(1), alt.value(0)),
            color=alt.value("gray"),
        )
        .add_params(hover)
    )
    text = (
        base.mark_text(align="left", dx=5, dy=-10, fontWeight="bold", fontSize=15)
        .encode(text=alt.condition(hover, "Yield:Q", alt.value(" "), format=".2f"))
        .transform_filter(hover)
    )

    quarter_ends = pd.DataFrame(
        {"Date": pd.date_range(start=melted["Date"].min(), end=melted["Date"].max(), freq="QE")}
    )
    quarter_lines = alt.Chart(quarter_ends).mark_rule(color="gray", strokeWidth=1).encode(x="Date:T")

    st.altair_chart(alt.layer(base, rule, text, quarter_lines), theme=None, use_container_width=True)

    # JPY/USD chart below the yield chart, same x-axis range.
    fx_df = chart_df[["Date", FX_COLUMN]].dropna(subset=[FX_COLUMN])
    fx_df = fx_df[fx_df["Date"] >= "2022-09-01"]
    fx_min = np.floor(fx_df[FX_COLUMN].min() / 5) * 5
    fx_max = np.ceil(fx_df[FX_COLUMN].max() / 5) * 5

    fx_chart = (
        alt.Chart(fx_df)
        .mark_line(color="#FFA500")
        .encode(
            x=alt.X("Date:T", axis=alt.Axis(title="")),
            y=alt.Y(f"{FX_COLUMN}:Q", scale=alt.Scale(domain=[fx_min, fx_max]),
                    axis=alt.Axis(title="JPY/USD")),
        )
        .properties(height=180)
    )
    st.subheader("JPY/USD Exchange Rate (FRED DEXJPUS)")
    st.altair_chart(fx_chart, theme=None, use_container_width=True)


def main():
    st.set_page_config(page_title="JGB Yield Data", page_icon="📈")
    st.title("JGB Yield Data")

    combined_df, chart_df, todays_date, month_end_data = load_jgb_data()
    _render_chart(chart_df)

    with st.sidebar:
        st.subheader("Month-End Data Table")
        st.dataframe(month_end_data[OUTPUT_TENORS + [FX_COLUMN]])
        st.write(f"Data source: MOF JGB / FRED DEXJPUS as of {todays_date}")
        st.markdown(
            "[JGB Interest Rate - MOF](https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/) / "
            "[FRED DEXJPUS](https://fred.stlouisfed.org/series/DEXJPUS)"
        )

    render_chat_panel(
        df=combined_df,
        series_columns=OUTPUT_TENORS + [FX_COLUMN],
        label="Japanese Government Bond yields (JGB, MOF) and JPY/USD exchange rate (FRED)",
        latest_date=todays_date,
        welcome="Welcome to JGB Yield Tracker!",
        placeholder="Ask questions on the JGB yield data.",
        state_key="jgb_messages",
    )


if __name__ == "__main__":
    main()
