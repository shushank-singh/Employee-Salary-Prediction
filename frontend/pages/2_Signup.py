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

from api import signup

st.set_page_config(
    page_title="Signup",
    page_icon="📝",
    layout="centered"
)

# ---------- CSS ----------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background:linear-gradient(135deg,#0F172A,#1E293B);
}

.title{
    text-align:center;
    font-size:34px;
    font-weight:bold;
    color:#2563EB;
}

.subtitle{
    text-align:center;
    color:#B0B0B0;
    margin-bottom:20px;
}

.stButton>button{
    width:100%;
    height:50px;
    font-size:18px;
    border-radius:10px;
    background:#2563EB;
    color:white;
    border:none;
}

.stButton>button:hover{
    background:#1D4ED8;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------

st.markdown(
    "<div class='title'>📝 Create Account</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Signup to start predicting salaries</div>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- Form ----------

username = st.text_input(
    "👤 Username",
    placeholder="Enter username"
)

email = st.text_input(
    "📧 Email",
    placeholder="Enter email"
)

password = st.text_input(
    "🔒 Password",
    type="password",
    placeholder="Minimum 8 characters"
)

confirm_password = st.text_input(
    "🔒 Confirm Password",
    type="password"
)

# ---------- Password Strength ----------

if password:

    if len(password) < 8:
        st.error("Weak Password ❌")

    elif len(password) < 12:
        st.warning("Medium Password ⚠️")

    else:
        st.success("Strong Password ✅")

# ---------- Signup ----------

if st.button("Create Account"):

    if not username or not email or not password:

        st.warning("Please fill all fields.")

        st.stop()

    if password != confirm_password:

        st.error("Passwords do not match.")

        st.stop()

    with st.spinner("Creating Account..."):

        response = signup(
            username,
            email,
            password
        )

    if response.status_code == 200:

        st.success("🎉 Account Created Successfully!")

        st.balloons()

    else:

        try:
            st.error(
                response.json()
            )
        except:

            st.error(
                response.text
            )

st.markdown("---")

st.info(
    "Already have an account? Login from the sidebar."
)