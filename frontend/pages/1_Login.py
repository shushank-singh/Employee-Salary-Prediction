import streamlit as st
import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from api import login

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# Redirect if already logged in
if st.session_state.get("token"):
    st.success("✅ You are already logged in.")
    st.stop()

# ---------- Custom CSS ----------
st.markdown("""
<style>

/* Main background */
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg,#0F172A,#1E293B);
}

/* Login Card */
.login-card{
    background:white;
    padding:35px;
    border-radius:18px;
    box-shadow:0px 8px 30px rgba(0,0,0,.25);
}

/* Title */
.title{
    text-align:center;
    font-size:34px;
    font-weight:bold;
    color:#2563EB;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#666;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown(
    "<div class='title'>💰 Employee Salary Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Login to continue</div>",
    unsafe_allow_html=True
)

# ---------- Login Form ----------
with st.container():

    email = st.text_input(
        "📧 Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "🔑 Password",
        type="password",
        placeholder="Enter your password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        if email == "" or password == "":
            st.warning("Please fill all fields.")
            st.stop()

        with st.spinner("Logging in..."):

            response = login(email, password)

        if response.status_code == 200:

            st.success("🎉 Login Successful!")

            st.balloons()

            st.session_state.logged_in = True

            st.rerun()

        else:

            try:
                message = response.json()
            except Exception:
                message = response.text

            st.error(message)

st.markdown("---")

st.info(
    "Don't have an account? Go to the Signup page from the sidebar."
)