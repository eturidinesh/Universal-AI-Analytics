import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Forecast",
    layout="wide"
)

st.title("🔮 Forecast Analysis")

# ==========================
# GET SHARED DATA
# ==========================

df = st.session_state.get("df", None)

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

    if len(numeric) > 0:

        st.subheader(
            "Select data for prediction"
        )

        target = st.selectbox(
            "Target Column",
            numeric
        )

        temp = (
            df[target]
            .dropna()
            .reset_index(drop=True)
        )

        if len(temp) > 5:

            x = np.arange(
                len(temp)
            ).reshape(-1,1)

            y = temp.values

            model = LinearRegression()

            model.fit(
                x,
                y
            )

            future_days = st.slider(
                "Forecast Days",
                1,
                30,
                7
            )

            future_x = np.arange(
                len(temp),
                len(temp)+future_days
            ).reshape(-1,1)

            prediction = model.predict(
                future_x
            )

            result = pd.DataFrame({

                "Day":
                np.arange(
                    len(temp)+1,
                    len(temp)+future_days+1
                ),

                "Prediction":
                prediction
            })

            st.subheader(
                "📈 Forecast Result"
            )

            fig = px.line(
                result,
                x="Day",
                y="Prediction",
                markers=True,
                template="plotly_dark"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.dataframe(
                result,
                use_container_width=True
            )

        else:

            st.warning(
                "Not enough data available"
            )

    else:

        st.warning(
            "No numeric columns found"
        )

else:

    st.info(
        "📂 Upload dataset from sidebar"
    )