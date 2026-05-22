import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from fredapi import Fred

from valact.settings import get_secrets
from valact.yield_chat import render_chat_panel


@st.cache_data(ttl=86400, show_spinner=False)
def load_fred_data():
    fred = Fred(api_key=get_secrets().fred)
    series_ids = {
        "3 Month": "DGS3MO",
        "5 Year": "DGS5",
        "10 Year": "DGS10",
        "30 Year": "DGS30",
        "A Spread": "BAMLC0A3CA",
        "BBB Spread": "BAMLC0A4CBBB",
    }

    df_list = []
    for label, code in series_ids.items():
        try:
            series = fred.get_series(code)
            df_list.append(series.rename(label).to_frame())
        except Exception as exc:
            st.warning(f"Failed to fetch series '{label}' ({code}): {exc}")

    combined_df = pd.concat(df_list, axis=1)
    combined_df.index.name = "Date"
    combined_df = combined_df.dropna(how="all").reset_index()
    combined_df["Date"] = pd.to_datetime(combined_df["Date"])
    todays_date = combined_df["Date"].max().strftime("%Y-%m-%d")

    month_end_df = combined_df.sort_values("Date").copy()
    month_end_df["YearMonth"] = month_end_df["Date"].dt.to_period("M")
    month_end_data = month_end_df.groupby("YearMonth").last().reset_index(drop=True)
    month_end_data = month_end_data[month_end_data["Date"] >= "2022-01-01"]
    month_end_data = month_end_data.set_index("Date")
    month_end_data.index = month_end_data.index.strftime("%Y-%m-%d")

    return combined_df, list(series_ids.keys()), todays_date, month_end_data


def _render_chart(combined_df: pd.DataFrame, output_list: list[str]):
    melted = combined_df.melt(id_vars="Date", var_name="Ticker", value_name="Yield")
    melted = melted.dropna(subset=["Yield"])
    melted = melted[melted["Date"] >= "2022-09-01"]

    y_start = np.floor(melted["Yield"].min() * 2) / 2
    y_end = np.ceil(melted["Yield"].max() * 2) / 2

    radio = alt.binding_radio(
        options=output_list + [None],
        labels=[label + " " for label in output_list] + ["All"],
        name="Ticker: ",
    )
    selection = alt.selection_point(fields=["Ticker"], bind=radio)

    base = (
        alt.Chart(melted)
        .mark_line()
        .encode(
            x="Date:T",
            y=alt.Y("Yield:Q", scale=alt.Scale(domain=[y_start, y_end])),
            color=alt.Color("Ticker:N", sort=output_list),
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
        {"Date": pd.date_range(start=melted["Date"].min(), end=melted["Date"].max(), freq="Q")}
    )
    quarter_lines = alt.Chart(quarter_ends).mark_rule(color="gray", strokeWidth=1).encode(x="Date:T")

    st.altair_chart(alt.layer(base, rule, text, quarter_lines), theme=None, use_container_width=True)


def main():
    st.set_page_config(page_title="Yield Data", page_icon="📈")
    st.title("FRED Yield Data")

    combined_df, output_list, todays_date, month_end_data = load_fred_data()
    _render_chart(combined_df, output_list)

    with st.sidebar:
        st.subheader("Month-End Data Table")
        st.dataframe(month_end_data[output_list])
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
        series_columns=output_list,
        label="US Treasury yields and IG corporate spreads (FRED)",
        latest_date=todays_date,
        welcome="Welcome to FRED Treasury Yield and Corporate Spread Tracker!",
        placeholder="Ask questions on the interest rate and spread data.",
        state_key="fred_messages",
    )


if __name__ == "__main__":
    main()
