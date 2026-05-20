import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("💬 Chat With Data")

uploaded = st.sidebar.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded:

    df = pd.read_csv(uploaded)

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ","_")
    )

    numeric = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    category = df.select_dtypes(
        include=["object","string"]
    ).columns.tolist()

    question = st.text_input(
        "Ask about your data"
    )

    if question:

        q = question.lower()

        # total
        if "total" in q:

            for col in numeric:

                if col.lower() in q:

                    st.success(
                        f"Total {col}: {df[col].sum():,.2f}"
                    )

        # average
        elif "average" in q:

            for col in numeric:

                if col.lower() in q:

                    st.success(
                        f"Average {col}: {df[col].mean():,.2f}"
                    )

        # highest
        elif "highest" in q:

            if len(category)>0 and len(numeric)>0:

                top = (
                    df.groupby(
                        category[0]
                    )[numeric[0]]
                    .sum()
                    .sort_values(
                        ascending=False
                    )
                )

                st.success(
                    f"""
Top {category[0]}:

{top.index[0]}

Value:
{top.iloc[0]:,.2f}
"""
                )

        else:

            st.warning(
                "Question not understood"
            )

else:

    st.info(
        "Upload dataset from sidebar"
    )