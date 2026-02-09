import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_openai import ChatOpenAI

import os


JGB_ALL_CSV = (
    "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/historical/jgbcme_all.csv"
)
JGB_REMOTE_CSV = (
    "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv"
)


@st.cache_data(ttl=86400)  # Cache result for 1 day (86400 seconds)
def load_jgb_data():
    output_list = ["1Y", "10Y", "30Y", "40Y"]

    all_df = pd.read_csv(JGB_ALL_CSV, header=1, encoding="cp932")
    all_df["Date"] = pd.to_datetime(all_df["Date"], errors="coerce")

    remote_df = None
    try:
        remote_df = pd.read_csv(JGB_REMOTE_CSV, header=1, encoding="cp932")
        remote_df["Date"] = pd.to_datetime(remote_df["Date"], errors="coerce")
    except Exception as e:
        st.warning(f"Failed to fetch JGB web CSV: {e}")

    if remote_df is not None:
        combined_df = pd.concat([all_df, remote_df], axis=0, ignore_index=True)
    else:
        combined_df = all_df.copy()

    combined_df = combined_df.sort_values("Date").drop_duplicates(subset=["Date"])
    combined_df = combined_df[["Date"] + output_list]

    todays_date = combined_df["Date"].max().strftime("%Y-%m-%d")

    month_end_df = combined_df.copy()
    month_end_df = month_end_df.sort_values("Date")
    month_end_df["YearMonth"] = month_end_df["Date"].dt.to_period("M")
    month_end_data = month_end_df.groupby("YearMonth").last().reset_index(drop=True)
    month_end_data = month_end_data[month_end_data["Date"] >= "2022-01-01"]
    month_end_data = month_end_data.set_index("Date")
    month_end_data.index = month_end_data.index.strftime("%Y-%m-%d")

    return combined_df, output_list, todays_date, month_end_data


def main():
    st.set_page_config(page_title="JGB Yield Data", page_icon="📈")
    st.title("JGB Yield Data")

    combined_df, output_list, todays_date, month_end_data = load_jgb_data()

    melted_df = combined_df.melt(id_vars="Date", var_name="Ticker", value_name="Yield")
    melted_df["Yield"] = pd.to_numeric(melted_df["Yield"], errors="coerce")
    melted_df.dropna(subset=["Yield"], inplace=True)
    melted_df = melted_df[melted_df["Date"] >= "2022-09-01"]

    y_start = np.floor(melted_df["Yield"].min() * 2) / 2
    y_end = np.ceil(melted_df["Yield"].max() * 2) / 2

    input_dropdown = alt.binding_radio(
        options=output_list + [None],
        labels=[label + " " for label in output_list] + ["All"],
        name="Ticker: ",
    )
    selection = alt.selection_point(fields=["Ticker"], bind=input_dropdown)

    base_chart = (
        alt.Chart(melted_df)
        .mark_line()
        .encode(
            x="Date:T",
            y=alt.Y("Yield:Q", scale=alt.Scale(domain=[y_start, y_end])),
            color=alt.Color("Ticker:N", sort=output_list),
        )
        .add_params(selection)
        .transform_filter(selection)
    )

    selector = alt.selection_point(
        encodings=["x"], on="mouseover", nearest=True, empty=False
    )
    rule = (
        alt.Chart(melted_df)
        .mark_rule()
        .encode(
            x="Date:T",
            opacity=alt.condition(selector, alt.value(1), alt.value(0)),
            color=alt.value("gray"),
        )
        .add_params(selector)
    )
    text = (
        base_chart.mark_text(align="left", dx=5, dy=-10, fontWeight="bold", fontSize=15)
        .encode(text=alt.condition(selector, "Yield:Q", alt.value(" "), format=".2f"))
        .transform_filter(selector)
    )

    start_date = melted_df["Date"].min()
    end_date = melted_df["Date"].max()
    quarter_ends_df = pd.DataFrame(
        {"Date": pd.date_range(start=start_date, end=end_date, freq="Q")}
    )

    quarter_lines = (
        alt.Chart(quarter_ends_df)
        .mark_rule(color="gray", strokeWidth=1)
        .encode(x="Date:T")
    )

    final_chart = alt.layer(base_chart, rule, text, quarter_lines)

    st.altair_chart(final_chart, theme=None, use_container_width=True)

    with st.sidebar:
        st.subheader("Month-End Data Table")
        st.dataframe(month_end_data[output_list])

        st.write(f"Data source: MOF JGB as of {todays_date}")
        st.markdown(
            "[JGB Interest Rate - MOF](https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/)"
        )

    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

    if "messages" not in st.session_state or st.sidebar.button(
        "Clear conversation history"
    ):
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "Welcome to JGB Yield Tracker!",
            }
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="Ask questions on the JGB yield data."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        llm = ChatOpenAI(model="gpt-5.2", streaming=True)
        pandas_df_agent = create_pandas_dataframe_agent(
            llm,
            combined_df,
            verbose=True,
            agent_type="openai-tools",
            allow_dangerous_code=True,
        )

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = pandas_df_agent.run(prompt, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)


if __name__ == "__main__":
    main()
