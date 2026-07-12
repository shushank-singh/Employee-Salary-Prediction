import streamlit as st

import os
import sys
from pathlib import Path

css_path = Path(__file__).parent / "assets" / "style.css"

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from auth.login import login_page
from auth.signup import signup_page

from pages.dashboard import dashboard_page
from pages.history import history_page
from pages.profile import profile_page  

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Employee Salary Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION ---------------- #

if "token" not in st.session_state:
    st.session_state.token = None

# ---------------- CSS ---------------- #

with open(css_path, "r", encoding="utf-8") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True,
    )

# ---------------- HIDE STREAMLIT ---------------- #

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}


</style>
""", unsafe_allow_html=True)

# ====================================================
# LOGIN SCREEN
# ====================================================

if st.session_state.token is None:

    left, center, right = st.columns([1,2,1])

    with center:

        tab1, tab2 = st.tabs(
            [
                "🔐 Login",
                "📝 Signup"
            ]
        )

        with tab1:
            login_page()

        with tab2:
            signup_page()

    st.stop()

# ====================================================
# SIDEBAR
# ====================================================

with st.sidebar:

    st.markdown("# 💰 Salary AI")

    st.write("")

    menu = st.radio(

        "",

        [
            "🏠 Dashboard",
            "📜 History",
            "👤 Profile"
        ]

    )

    st.write("---")

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.token = None

        if "salary" in st.session_state:
            del st.session_state.salary

        st.rerun()

# ====================================================
# PAGE ROUTING
# ====================================================

if menu == "🏠 Dashboard":

    dashboard_page()

elif menu == "📜 History":

    history_page()

elif menu == "👤 Profile":

    profile_page()