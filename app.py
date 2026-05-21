import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Universal AI Analytics",
    page_icon="🚀",
    layout="wide"
)

# ======================
# SIDEBAR
# ======================

st.sidebar.image(
    "assets/logo.png",
    width=170
)

st.sidebar.markdown("""
# 🚀 Universal AI Analytics

Smart AI-powered data analysis platform
""")

st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload CSV Dataset",
    type=["csv"]
)

# Save dataframe once
if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        # Save globally for all pages
        st.session_state["df"] = df

        st.sidebar.success(
            "Dataset uploaded successfully"
        )

    except Exception as e:

        st.sidebar.error(
            f"Error loading file: {e}"
        )

st.sidebar.markdown("---")

st.sidebar.info("""
Supported:

✅ E-commerce  
✅ Finance  
✅ Employee  
✅ Hospital  
✅ Student  
✅ Any CSV
""")

# ======================
# HOME PAGE
# ======================

st.markdown("""
<style>

.hero{
padding:35px;
border-radius:20px;
background:linear-gradient(
90deg,
#0f172a,
#4c1d95,
#7e22ce
);

text-align:center;
margin-bottom:30px;
}

.big{
font-size:55px;
font-weight:bold;
color:white;
}

.small{
font-size:22px;
color:#d1d5db;
}

.card{
padding:25px;
border-radius:15px;
background:#111827;
border:1px solid #374151;
text-align:center;
height:150px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<div class="big">
🚀 Universal AI Analytics
</div>

<div class="small">
AI Powered Analytics Platform
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("## Features")

c1,c2,c3=st.columns(3)

with c1:

    st.markdown("""
<div class="card">
<h3>📊 Dashboard</h3>
KPI Metrics and Charts
</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="card">
<h3>🔮 Forecast</h3>
Machine Learning Predictions
</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="card">
<h3>🧠 AI Insights</h3>
Smart Analytics
</div>
""", unsafe_allow_html=True)

c4,c5,c6=st.columns(3)

with c4:

    st.markdown("""
<div class="card">
<h3>💬 Chat</h3>
Chat with Data
</div>
""", unsafe_allow_html=True)

with c5:

    st.markdown("""
<div class="card">
<h3>📄 Reports</h3>
PDF Reports
</div>
""", unsafe_allow_html=True)

with c6:

    st.markdown("""
<div class="card">
<h3>🗺 Maps</h3>
Geographic Analysis
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.success(
"""
Upload your dataset from the sidebar and explore:

📊 Dashboard  
🔮 Forecast  
🧠 Insights  
💬 Chat with Data  
📄 Reports
"""
)