import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Chat with Data",
    layout="wide"
)

st.title("💬 Chat With Data")

# ==========================
# GET SHARED DATA
# ==========================

df = st.session_state.get(
    "df",
    None
)

if df is not None:

    if len(df) > 5000:

        df = df.sample(
            n=5000,
            random_state=42
        )

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(
            " ",
            "_"
        )
    )

    numeric = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    category = df.select_dtypes(
        include=["object","string"]
    ).columns.tolist()

    st.markdown("""
Ask things like:

- total sales
- average profit
- highest category
- number of rows
""")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        q = question.lower()

        answered = False

        # Total
        if "total" in q:

            for col in numeric:

                if col.lower() in q:

                    st.success(
                        f"Total {col}: {df[col].sum():,.2f}"
                    )

                    answered = True

        # Average
        elif "average" in q:

            for col in numeric:

                if col.lower() in q:

                    st.success(
                        f"Average {col}: {df[col].mean():,.2f}"
                    )

                    answered = True

        # Highest category
        elif "highest" in q:

            if category and numeric:

                top = (
                    df.groupby(
                        category[0]
                    )[numeric[0]]
                    .mean()
                    .sort_values(
                        ascending=False
                    )
                )

                st.success(
                    f"""
Highest {category[0]}:

{top.index[0]}

Value:

{top.iloc[0]:,.2f}
"""
                )

                answered = True

        # Rows
        elif "rows" in q:

            st.success(
                f"Dataset contains {len(df):,} rows"
            )

            answered = True

        if not answered:

            st.warning(
                "Question not recognized"
            )

else:

    st.info(
        "📂 Upload dataset from sidebar"
    )