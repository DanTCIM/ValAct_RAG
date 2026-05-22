import io
import urllib.request

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from valact.yield_chat import render_chat_panel


PARQUET_URL = "https://pub-bedeea83f4c04f0abb342c6e246f8db5.r2.dev/fred/yields.parquet"
OUTPUT_LIST = ["3 Month", "5 Year", "10 Year", "30 Year", "A Spread", "BBB Spread"]


@st.cache_data(ttl=86400, show_spinner=False)
def load_fred_data():
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

    month_end_df = combined_df.sort_values("Date").copy()
    month_end_df["YearMonth"] = month_end_df["Date"].dt.to_period("M")
    month_end_data = month_end_df.groupby("YearMonth").last().reset_index(drop=True)
    month_end_data = month_end_data[month_end_data["Date"] >= "2022-01-01"]
    month_end_data = month_end_data.set_index("Date")
    month_end_data.index = month_end_data.index.strftime("%Y-%m-%d")

    return combined_df, chart_df, todays_date, month_end_data


def _render_chart(chart_df: pd.DataFrame):
    melted = chart_df.melt(id_vars="Date", var_name="Ticker", value_name="Yield")
    melted = melted.dropna(subset=["Yield"])
    melted = melted[melted["Date"] >= "2022-09-01"]

    y_start = np.floor(melted["Yield"].min() * 2) / 2
    y_end = np.ceil(melted["Yield"].max() * 2) / 2

    radio = alt.binding_radio(
        options=OUTPUT_LIST + [None],
        labels=[label + " " for label in OUTPUT_LIST] + ["All"],
        name="Ticker: ",
    )
    selection = alt.selection_point(fields=["Ticker"], bind=radio)

    base = (
        alt.Chart(melted)
        .mark_line()
        .encode(
            x="Date:T",
            y=alt.Y("Yield:Q", scale=alt.Scale(domain=[y_start, y_end])),
            color=alt.Color("Ticker:N", sort=OUTPUT_LIST),
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


def main():
    st.set_page_config(page_title="Yield Data", page_icon="📈")
    st.title("FRED Yield Data")

    combined_df, chart_df, todays_date, month_end_data = load_fred_data()
    _render_chart(chart_df)

    with st.sidebar:
        st.subheader("Month-End Data Table")
        st.dataframe(month_end_data[OUTPUT_LIST])
        st.write(f"Data source: FRED as of {todays_date}")
        st.markdown(
            "[Constant Maturity Treasury (CMT) Rates](https://fred.stlouisfed.org/categories/115)"
        )
        st.markdown(
            "[ICE BofA Single-A US Corporate Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLC0A3CA)"
        )
        st.markdown(
            "[ICE BofA BBB US Corporate Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLC0A4CBBB)"
        )

    render_chat_panel(
        df=combined_df,
        series_columns=OUTPUT_LIST,
        label="US Treasury yields and IG corporate spreads (FRED)",
        latest_date=todays_date,
        welcome="Welcome to FRED Treasury Yield and Corporate Spread Tracker!",
        placeholder="Ask questions on the interest rate and spread data.",
        state_key="fred_messages",
    )


if __name__ == "__main__":
    main()
