import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from valact.yield_chat import render_chat_panel


JGB_ALL_CSV = (
    "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/historical/jgbcme_all.csv"
)
JGB_REMOTE_CSV = (
    "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv"
)


@st.cache_data(ttl=86400, show_spinner=False)
def load_jgb_data():
    output_list = ["1Y", "10Y", "30Y", "40Y"]

    all_df = pd.read_csv(JGB_ALL_CSV, header=1, encoding="cp932")
    all_df["Date"] = pd.to_datetime(all_df["Date"], errors="coerce")

    remote_df = None
    try:
        remote_df = pd.read_csv(JGB_REMOTE_CSV, header=1, encoding="cp932")
        remote_df["Date"] = pd.to_datetime(remote_df["Date"], errors="coerce")
    except Exception as exc:
        st.warning(f"Failed to fetch JGB web CSV: {exc}")

    combined_df = pd.concat([all_df, remote_df], axis=0, ignore_index=True) if remote_df is not None else all_df.copy()
    combined_df = combined_df.sort_values("Date").drop_duplicates(subset=["Date"])
    combined_df = combined_df[["Date"] + output_list]

    for c in output_list:
        combined_df[c] = pd.to_numeric(combined_df[c], errors="coerce")

    todays_date = combined_df["Date"].max().strftime("%Y-%m-%d")

    month_end_df = combined_df.sort_values("Date").copy()
    month_end_df["YearMonth"] = month_end_df["Date"].dt.to_period("M")
    month_end_data = month_end_df.groupby("YearMonth").last().reset_index(drop=True)
    month_end_data = month_end_data[month_end_data["Date"] >= "2022-01-01"]
    month_end_data = month_end_data.set_index("Date")
    month_end_data.index = month_end_data.index.strftime("%Y-%m-%d")

    return combined_df, output_list, todays_date, month_end_data


def _render_chart(combined_df: pd.DataFrame, output_list: list[str]):
    melted = combined_df.melt(id_vars="Date", var_name="Ticker", value_name="Yield")
    melted["Yield"] = pd.to_numeric(melted["Yield"], errors="coerce")
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
        {"Date": pd.date_range(start=melted["Date"].min(), end=melted["Date"].max(), freq="QE")}
    )
    quarter_lines = alt.Chart(quarter_ends).mark_rule(color="gray", strokeWidth=1).encode(x="Date:T")

    st.altair_chart(alt.layer(base, rule, text, quarter_lines), theme=None, use_container_width=True)


def main():
    st.set_page_config(page_title="JGB Yield Data", page_icon="📈")
    st.title("JGB Yield Data")

    combined_df, output_list, todays_date, month_end_data = load_jgb_data()
    _render_chart(combined_df, output_list)

    with st.sidebar:
        st.subheader("Month-End Data Table")
        st.dataframe(month_end_data[output_list])
        st.write(f"Data source: MOF JGB as of {todays_date}")
        st.markdown(
            "[JGB Interest Rate - MOF](https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/)"
        )

    render_chat_panel(
        df=combined_df,
        series_columns=output_list,
        label="Japanese Government Bond yields (JGB, MOF)",
        latest_date=todays_date,
        welcome="Welcome to JGB Yield Tracker!",
        placeholder="Ask questions on the JGB yield data.",
        state_key="jgb_messages",
    )


if __name__ == "__main__":
    main()
