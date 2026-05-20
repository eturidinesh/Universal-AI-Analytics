import streamlit as st

st.set_page_config(
    page_title="Universal AI Analytics",
    page_icon="🚀",
    layout="wide"
)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.image(
    "assets/logo.png",
    width=180
)

st.sidebar.markdown(
    """
    # 🚀 Universal AI Analytics
    
    Smart AI-powered data analysis platform
    """
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Upload datasets and explore insights"
)

# ==========================
# HOME PAGE
# ==========================

st.markdown(
"""
<style>

.hero{
padding:35px;
border-radius:25px;
background:linear-gradient(
90deg,
#0f172a,
#4c1d95,
#7e22ce
);
text-align:center;
margin-bottom:25px;
box-shadow:0px 0px 30px rgba(139,92,246,.5);
}

.big{
font-size:50px;
font-weight:bold;
color:white;
}

.small{
font-size:22px;
color:#d1d5db;
}

.card{
padding:25px;
border-radius:20px;
background:#111827;
border:1px solid #374151;
text-align:center;
}

</style>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="hero">

<div class="big">
🚀 Universal AI Analytics
</div>

<div class="small">
AI Powered Analytics Platform
</div>

</div>
""",
unsafe_allow_html=True
)

st.markdown("## Features")

c1,c2,c3=st.columns(3)

with c1:

    st.markdown(
    """
<div class="card">
<h3>📊 Dashboard</h3>
Dynamic KPI charts and metrics
</div>
""",
unsafe_allow_html=True
)

with c2:

    st.markdown(
    """
<div class="card">
<h3>🔮 Forecasting</h3>
ML-based prediction engine
</div>
""",
unsafe_allow_html=True
)

with c3:

    st.markdown(
    """
<div class="card">
<h3>🧠 AI Insights</h3>
Smart recommendations
</div>
""",
unsafe_allow_html=True
)

st.markdown("---")

c4,c5,c6=st.columns(3)

with c4:

    st.markdown(
    """
<div class="card">
<h3>💬 Chat with Data</h3>
Ask questions naturally
</div>
""",
unsafe_allow_html=True
)

with c5:

    st.markdown(
    """
<div class="card">
<h3>📄 Reports</h3>
Generate PDF reports
</div>
""",
unsafe_allow_html=True
)

with c6:

    st.markdown(
    """
<div class="card">
<h3>🗺 Maps</h3>
Interactive geographic analysis
</div>
""",
unsafe_allow_html=True
)

st.markdown("---")

st.success(
"""
✅ Upload a CSV from the sidebar and navigate using:

📊 Dashboard  
🔮 Forecast  
🧠 Insights  
💬 Chat  
📄 Reports
"""
)