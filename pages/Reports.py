import streamlit as st
import pandas as pd
import numpy as np
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib import styles
import io

st.set_page_config(layout="wide")

st.title("📄 Analytics Reports")

uploaded = st.sidebar.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded:

    df = pd.read_csv(uploaded)

    df.columns=(
        df.columns
        .str.strip()
        .str.replace(" ","_")
    )

    numeric=df.select_dtypes(
        include=np.number
    ).columns.tolist()

    st.subheader(
        "Summary Report"
    )

    for col in numeric[:4]:

        st.metric(
            col,
            f"{df[col].sum():,.2f}"
        )

    # CSV download

    csv=df.to_csv(
        index=False
    )

    st.download_button(
        "⬇ Download CSV",
        csv,
        "report.csv",
        "text/csv"
    )

    # PDF generation

    buffer=io.BytesIO()

    doc=SimpleDocTemplate(
        buffer
    )

    style=styles.getSampleStyleSheet()

    content=[]

    content.append(
        Paragraph(
            "Analytics Report",
            style["Title"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    for col in numeric[:4]:

        content.append(

            Paragraph(
                f"{col}: {df[col].sum():,.2f}",
                style["Normal"]
            )

        )

    doc.build(
        content
    )

    pdf=buffer.getvalue()

    st.download_button(
        "📄 Download PDF",
        pdf,
        "analytics_report.pdf",
        "application/pdf"
    )

else:

    st.info(
        "Upload dataset from sidebar"
    )