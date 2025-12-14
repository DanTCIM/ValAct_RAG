import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from fredapi import Fred
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_openai import ChatOpenAI

# from langchain_community.chat_models import ChatOpenAI
import os
import tabulate


@st.cache_data(ttl=86400)  # Cache result for 1 day (86400 seconds)
def load_fred_data():
    fred = Fred(api_key=st.secrets["FRED_API_KEY"])
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
        # series = fred.get_series(code)
        # df_list.append(series.rename(label).to_frame())
        try:
            series = fred.get_series(code)
            df_list.append(series.rename(label).to_frame())
        except Exception as e:
            st.warning(f"Failed to fetch series '{label}' ({code}): {e}")

    combined_df = pd.concat(df_list, axis=1)
    combined_df.index.name = "Date"
    combined_df = combined_df.dropna(how="all").reset_index()

    combined_df["Date"] = pd.to_datetime(combined_df["Date"])
    todays_date = combined_df["Date"].max().strftime("%Y-%m-%d")

    # Create a copy so we don't mutate the main DataFrame
    month_end_df = combined_df.copy()
    month_end_df = month_end_df.sort_values("Date")
    month_end_df["YearMonth"] = month_end_df["Date"].dt.to_period("M")
    month_end_data = month_end_df.groupby("YearMonth").last().reset_index(drop=True)
    month_end_data = month_end_data[month_end_data["Date"] >= "2022-01-01"]
    month_end_data = month_end_data.set_index("Date")
    month_end_data.index = month_end_data.index.strftime("%Y-%m-%d")

    return combined_df, list(series_ids.keys()), todays_date, month_end_data


def main():
    st.set_page_config(page_title="Yield Data", page_icon="📈")
    st.title("FRED Yield Data")

    combined_df, output_list, todays_date, month_end_data = load_fred_data()

    # Prepare data for chart
    melted_df = combined_df.melt(id_vars="Date", var_name="Ticker", value_name="Yield")
    melted_df.dropna(subset=["Yield"], inplace=True)
    melted_df = melted_df[melted_df["Date"] >= "2022-09-01"]

    # Y-axis bounds
    y_start = np.floor(melted_df["Yield"].min() * 2) / 2
    y_end = np.ceil(melted_df["Yield"].max() * 2) / 2

    # Dropdown for filtering
    input_dropdown = alt.binding_radio(
        options=output_list + [None],
        labels=[label + " " for label in output_list] + ["All"],
        name="Ticker: ",
    )
    selection = alt.selection_point(fields=["Ticker"], bind=input_dropdown)

    # Base chart
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

    # Add vertical interaction line
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

    # Quarter lines
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

    # Combine all charts
    final_chart = alt.layer(base_chart, rule, text, quarter_lines)

    # Show chart
    st.altair_chart(final_chart, theme=None, use_container_width=True)

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

    # LLM section
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

    if "messages" not in st.session_state or st.sidebar.button(
        "Clear conversation history"
    ):
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "Welcome to Fred Treasury Yield and Corp Spread Tracker!",
            }
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(
        placeholder="Ask questions on the interest rate and spread data."
    ):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        llm = ChatOpenAI(
            model="gpt-5.2", streaming=True
        )  # removed "temperature=0," from the argument
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
            # response = pandas_df_agent.run(st.session_state.messages, callbacks=[st_cb]) # updated the code as per the following recommendation: Feed the prompt, not the message list, to the agent
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)


if __name__ == "__main__":
    main()
