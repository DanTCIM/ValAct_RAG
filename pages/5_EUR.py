import io
import urllib.request

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from valact.yield_chat import render_chat_panel


PARQUET_URL = "https://pub-bedeea83f4c04f0abb342c6e246f8db5.r2.dev/eur/rates.parquet"
RATE_COLUMNS = ["EUR €STR", "GBP SONIA"]
FX_COLUMNS = ["EUR/USD", "GBP/USD"]


@st.cache_data(ttl=86400, show_spinner=False)
def load_eur_data():
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
    melted = chart_df[["Date"] + RATE_COLUMNS].melt(id_vars="Date", var_name="Ticker", value_name="Rate")
    melted["Rate"] = pd.to_numeric(melted["Rate"], errors="coerce")
    melted = melted.dropna(subset=["Rate"])
    melted = melted[melted["Date"] >= "2022-09-01"]

    y_start = np.floor(melted["Rate"].min() * 2) / 2
    y_end = np.ceil(melted["Rate"].max() * 2) / 2

    radio = alt.binding_radio(
        options=RATE_COLUMNS + [None],
        labels=[label + " " for label in RATE_COLUMNS] + ["All"],
        name="Ticker: ",
    )
    selection = alt.selection_point(fields=["Ticker"], bind=radio)

    base = (
        alt.Chart(melted)
        .mark_line()
        .encode(
            x="Date:T",
            y=alt.Y("Rate:Q", scale=alt.Scale(domain=[y_start, y_end]),
                    axis=alt.Axis(title="Rate (%)")),
            color=alt.Color("Ticker:N", sort=RATE_COLUMNS),
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
        .encode(text=alt.condition(hover, "Rate:Q", alt.value(" "), format=".2f"))
        .transform_filter(hover)
    )

    quarter_ends = pd.DataFrame(
        {"Date": pd.date_range(start=melted["Date"].min(), end=melted["Date"].max(), freq="QE")}
    )
    quarter_lines = alt.Chart(quarter_ends).mark_rule(color="gray", strokeWidth=1).encode(x="Date:T")

    st.altair_chart(alt.layer(base, rule, text, quarter_lines), theme=None, use_container_width=True)

    # Combined EUR/USD + GBP/USD chart below the rate chart.
    available_fx = [col for col in FX_COLUMNS if col in chart_df.columns]
    if available_fx:
        fx_melted = (
            chart_df[["Date"] + available_fx]
            .melt(id_vars="Date", var_name="Pair", value_name="FX")
            .dropna(subset=["FX"])
        )
        fx_melted = fx_melted[fx_melted["Date"] >= "2022-09-01"]
        fx_min = np.floor(fx_melted["FX"].min() / 0.05) * 0.05
        fx_max = np.ceil(fx_melted["FX"].max() / 0.05) * 0.05

        fx_chart = (
            alt.Chart(fx_melted)
            .mark_line()
            .encode(
                x=alt.X("Date:T", axis=alt.Axis(title="")),
                y=alt.Y("FX:Q", scale=alt.Scale(domain=[fx_min, fx_max]),
                        axis=alt.Axis(title="FX Rate (USD)", format=".2f")),
                color=alt.Color("Pair:N", sort=available_fx),
            )
            .properties(height=180)
        )
        st.subheader("EUR/USD & GBP/USD (FRED)")
        st.altair_chart(fx_chart, theme=None, use_container_width=True)


def main():
    st.set_page_config(page_title="EUR/GBP Rates", page_icon="📈")
    st.title("EUR/GBP Rates")

    combined_df, chart_df, todays_date, month_end_data = load_eur_data()
    _render_chart(chart_df)

    display_cols = [c for c in RATE_COLUMNS + FX_COLUMNS if c in month_end_data.columns]
    with st.sidebar:
        st.subheader("Month-End Data Table")
        st.dataframe(month_end_data[display_cols])
        st.write(f"Data source: FRED as of {todays_date}")
        st.markdown(
            "[ECB €STR](https://fred.stlouisfed.org/series/ECBESTRVOLWGTTRMDMNRT) / "
            "[SONIA](https://fred.stlouisfed.org/series/IUDSOIA) / "
            "[EUR/USD](https://fred.stlouisfed.org/series/DEXUSEU) / "
            "[GBP/USD](https://fred.stlouisfed.org/series/DEXUSUK)"
        )

    render_chat_panel(
        df=combined_df,
        series_columns=RATE_COLUMNS + FX_COLUMNS,
        label="EUR/GBP short-term rates (EURIBOR, SONIA) and exchange rates (FRED)",
        latest_date=todays_date,
        welcome="Welcome to EUR/GBP Rate Tracker!",
        placeholder="Ask questions on the EUR/GBP rate data.",
        state_key="eur_messages",
    )


if __name__ == "__main__":
    main()
