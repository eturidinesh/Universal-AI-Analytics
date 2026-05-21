import streamlit as st
import pandas as pd
import numpy as np
import io
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib import styles

st.set_page_config(
    page_title="Reports",
    layout="wide"
)

st.title("📄 Reports")

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

    st.subheader(
        "📊 Summary Metrics"
    )

    if len(numeric)>0:

        cols = st.columns(
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
                f"{df[col].mean():,.2f}"
            )

    st.markdown("---")

    # ==========================
    # CSV DOWNLOAD
    # ==========================

    csv = df.to_csv(
        index=False
    )

    st.download_button(
        "⬇ Download CSV",
        csv,
        "dataset.csv",
        "text/csv"
    )

    # ==========================
    # PDF REPORT
    # ==========================

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer
    )

    style = (
        styles.getSampleStyleSheet()
    )

    content = []

    content.append(
        Paragraph(
            "Universal AI Analytics Report",
            style["Title"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    for col in numeric[:5]:

        content.append(

            Paragraph(
                f"{col} Average: {df[col].mean():,.2f}",
                style["Normal"]
            )

        )

    doc.build(
        content
    )

    pdf = buffer.getvalue()

    st.download_button(
        "📄 Download PDF Report",
        pdf,
        "analytics_report.pdf",
        "application/pdf"
    )

    st.markdown("---")

    st.subheader(
        "📋 Data Preview"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

else:

    st.info(
        "📂 Upload dataset from sidebar"
    )