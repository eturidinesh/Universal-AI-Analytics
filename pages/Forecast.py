import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(layout="wide")

st.title("🔮 Forecast Analytics")

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

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    if len(numeric_cols)==0:

        st.error(
            "No numeric columns found"
        )

    else:

        target = st.selectbox(
            "Select Column For Prediction",
            numeric_cols
        )

        temp=df.copy()

        temp["Index"]=range(
            len(temp)
        )

        X=temp[["Index"]]

        y=temp[target]

        model=LinearRegression()

        model.fit(
            X,
            y
        )

        future=pd.DataFrame({

            "Index":
            range(
                len(temp),
                len(temp)+30
            )

        })

        predictions=model.predict(
            future
        )

        forecast_df=pd.DataFrame({

            "Day":
            range(
                1,
                31
            ),

            "Prediction":
            predictions
        })

        st.subheader(
            "Forecast Result"
        )

        fig=px.line(

            forecast_df,

            x="Day",

            y="Prediction",

            title=f"30 Day Forecast of {target}",

            template="plotly_dark"

        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        st.metric(
            "Predicted Average",
            f"{predictions.mean():,.2f}"
        )

else:

    st.info(
        "Upload dataset from sidebar"
    )