import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("📊 Universal Analytics Dashboard")

uploaded = st.sidebar.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded:

    # ==========================
    # LOAD DATA
    # ==========================

    with st.spinner(
        "Analyzing dataset..."
    ):

        df = pd.read_csv(
            uploaded
        )

    df.columns=(
        df.columns
        .str.strip()
        .str.replace(
            " ",
            "_"
        )
    )

    numeric=df.select_dtypes(
        include=np.number
    ).columns.tolist()

    category=df.select_dtypes(
        include=["object","string"]
    ).columns.tolist()

    # ==========================
    # KPI SECTION
    # ==========================

    st.subheader(
        "📈 Key Metrics"
    )

    cols=st.columns(
        min(
            len(numeric),
            4
        )
    )

    for i,col in enumerate(
        numeric[:4]
    ):

        cols[i].metric(
            col,
            f"{df[col].sum():,.2f}"
        )

    st.markdown("---")

    # ==========================
    # FILTERS
    # ==========================

    st.sidebar.subheader(
        "Filters"
    )

    if category:

        selected=st.sidebar.selectbox(
            "Select Category",
            category
        )

    # ==========================
    # VISUAL ANALYTICS
    # ==========================

    if category and numeric:

        st.subheader(
            "📊 Visual Analytics"
        )

        left,right=st.columns(
            2
        )

        chart=(
            df.groupby(
                category[0]
            )[numeric[0]]
            .sum()
            .reset_index()
        )

        fig1=px.bar(
            chart,
            x=category[0],
            y=numeric[0],
            title=f"{numeric[0]} by {category[0]}",
            template="plotly_dark"
        )

        left.plotly_chart(
            fig1,
            width="stretch"
        )

        fig2=px.pie(
            chart,
            names=category[0],
            values=numeric[0],
            hole=.5,
            template="plotly_dark"
        )

        right.plotly_chart(
            fig2,
            width="stretch"
        )

    st.markdown("---")

    # ==========================
    # MAP SECTION
    # ==========================

    st.subheader(
        "🗺 Geographic Analysis"
    )

    lat_col=None
    lon_col=None

    for c in df.columns:

        name=c.lower()

        if "lat" in name:

            lat_col=c

        elif "lon" in name or "long" in name:

            lon_col=c

    if lat_col and lon_col:

        map_df=(
            df[
                [lat_col,lon_col]
            ]
            .dropna()
            .rename(
                columns={
                    lat_col:"lat",
                    lon_col:"lon"
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

    # ==========================
    # TOP PERFORMERS
    # ==========================

    st.subheader(
        "🏆 Top Performers"
    )

    if category and numeric:

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
            .sum()
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
            title=f"Top {selected_category}",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig3,
            width="stretch"
        )

    st.markdown("---")

    # ==========================
    # DATA PREVIEW
    # ==========================

    st.subheader(
        "📋 Dataset Preview"
    )

    st.dataframe(
        df.head(
            20
        ),
        width="stretch"
    )

else:

    st.info(
        "Upload dataset from sidebar"
    )