import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🧠 AI Insights & Advanced Analytics")

df = st.session_state.get(
    "df",
    None
)

if df is not None:

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

    # =========================
    # BASIC AI INSIGHTS
    # =========================

    st.subheader(
        "📊 Smart Insights"
    )

    for col in numeric[:4]:

        avg = df[col].mean()

        maximum = df[col].max()

        minimum = df[col].min()

        st.success(
            f"""
{col}

Average: {avg:,.2f}

Highest: {maximum:,.2f}

Lowest: {minimum:,.2f}
"""
        )

    # =========================
    # BEST CATEGORY
    # =========================

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

        st.info(
            f"""
🏆 Best {category[0]}:

{top.index[0]}

Value:

{top.iloc[0]:,.2f}
"""
        )

    st.markdown("---")

    # =========================
    # CORRELATION HEATMAP
    # =========================

    if len(numeric)>1:

        st.subheader(
            "🔥 Correlation Heatmap"
        )

        corr = df[numeric].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu",
            title="Feature Relationships"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    st.markdown("---")

    # =========================
    # ANOMALY DETECTION
    # =========================

    st.subheader(
        "⚠ Anomaly Detection"
    )

    target = st.selectbox(
        "Select Column",
        numeric
    )

    mean = df[target].mean()

    std = df[target].std()

    anomalies = df[
        abs(
            df[target]-mean
        ) > 2*std
    ]

    st.metric(
        "Anomalies Found",
        len(anomalies)
    )

    if len(anomalies)>0:

        fig2 = px.scatter(
            df,
            y=target,
            title=f"Anomalies in {target}"
        )

        st.plotly_chart(
            fig2,
            width="stretch"
        )

        st.dataframe(
            anomalies.head(10)
        )

else:

    st.info(
        "Upload dataset from sidebar"
    )