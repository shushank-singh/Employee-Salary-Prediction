import streamlit as st

st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "token" not in st.session_state:
    st.session_state.token = None


st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background:linear-gradient(135deg,#0F172A,#1E293B);
}

[data-testid="stSidebar"]{
background:#111827;
}

h1,h2,h3{
color:white;
}

p{
color:white;
}

</style>
""", unsafe_allow_html=True)


st.title("💰 Employee Salary Prediction")

st.markdown("---")

st.markdown(
"""
## 👋 Welcome

This application predicts employee salaries using Machine Learning.

### Features

- 🔐 JWT Authentication
- 📈 Salary Prediction
- 💾 Save Prediction History
- 👤 User Profile
- 📊 Dashboard

---

### 👈 Use the Sidebar to Navigate.
"""
)

st.success("Backend Connected Successfully ✅")