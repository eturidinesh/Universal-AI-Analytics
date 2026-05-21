import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Insights",
    layout="wide"
)

st.title("🧠 AI Insights")

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
        .str.replace(" ","_")
    )

    numeric = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    category = df.select_dtypes(
        include=["object","string"]
    ).columns.tolist()

    st.subheader(
        "📊 Smart Insights"
    )

    if len(numeric) > 0:

        cols = st.columns(
            min(
                len(numeric),
                4
            )
        )

        for i,col in enumerate(
            numeric[:4]
        ):

            avg = round(
                df[col].mean(),
                2
            )

            maxv = round(
                df[col].max(),
                2
            )

            cols[i].metric(
                col,
                avg,
                f"Max: {maxv}"
            )

    st.markdown("---")

    # ==========================
    # CORRELATION HEATMAP
    # ==========================

    if len(numeric) > 1:

        st.subheader(
            "🔥 Correlation Heatmap"
        )

        corr = df[
            numeric
        ].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================
    # OUTLIER DETECTION
    # ==========================

    if len(numeric)>0:

        st.subheader(
            "⚠ Outlier Detection"
        )

        selected = st.selectbox(
            "Select Numeric Column",
            numeric
        )

        fig2 = px.box(
            df,
            y=selected,
            template="plotly_dark"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.markdown("---")

    st.subheader(
        "📋 Dataset Preview"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

else:

    st.info(
        "📂 Upload dataset from sidebar"
    )