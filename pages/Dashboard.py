import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("📊 Universal Analytics Dashboard")

# ==========================
# GET DATA
# ==========================

df = st.session_state.get("df", None)

if df is not None:

    # optimize performance
    if len(df) > 5000:
        df = df.sample(
            n=5000,
            random_state=42
        )

    # clean columns
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

    # ==========================
    # KPI CARDS
    # ==========================

    st.subheader("📈 Key Metrics")

    if len(numeric)>0:

        cols = st.columns(
            min(4,len(numeric))
        )

        for i,col in enumerate(
            numeric[:4]
        ):

            value = round(
                df[col].mean(),
                2
            )

            cols[i].metric(
                label=col,
                value=f"{value:,}"
            )

    st.markdown("---")

    # ==========================
    # VISUAL ANALYTICS
    # ==========================

    if len(category)>0 and len(numeric)>0:

        st.subheader(
            "📊 Visual Analytics"
        )

        left,right = st.columns(2)

        grouped = (
            df.groupby(
                category[0]
            )[numeric[0]]
            .mean()
            .sort_values(
                ascending=False
            )
            .head(10)
            .reset_index()
        )

        fig1 = px.bar(
            grouped,
            x=category[0],
            y=numeric[0],
            title=f"{numeric[0]} by {category[0]}",
            template="plotly_dark"
        )

        left.plotly_chart(
            fig1,
            use_container_width=True
        )

        fig2 = px.pie(
            grouped,
            names=category[0],
            values=numeric[0],
            hole=0.5,
            template="plotly_dark"
        )

        right.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================
    # TOP PERFORMERS
    # ==========================

    if len(category)>0 and len(numeric)>0:

        st.subheader(
            "🏆 Top Analysis"
        )

        selected_category=st.selectbox(
            "Choose Category",
            category
        )

        selected_metric=st.selectbox(
            "Choose Metric",
            numeric
        )

        top=(
            df.groupby(
                selected_category
            )[selected_metric]
            .mean()
            .sort_values(
                ascending=False
            )
            .head(10)
            .reset_index()
        )

        fig3=px.bar(
            top,
            x=selected_metric,
            y=selected_category,
            orientation="h",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================
    # MAP ANALYSIS
    # ==========================

    st.subheader(
        "🗺 Geographic Analysis"
    )

    lat=None
    lon=None

    for c in df.columns:

        name=c.lower()

        if "lat" in name:
            lat=c

        if "lon" in name or "long" in name:
            lon=c

    if lat and lon:

        map_df=(
            df[[lat,lon]]
            .dropna()
            .rename(
                columns={
                    lat:"lat",
                    lon:"lon"
                }
            )
        )

        st.map(
            map_df
        )

    else:

        st.info(
            "No latitude/longitude columns found"
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
        "📂 Upload a dataset from sidebar"
    )