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


def signup_page():

    st.markdown("""
    <div class="login-box">
    <h2>Create Account</h2>
    <p>Start Predicting Salaries 🚀</p>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input(
        "Username",
        placeholder="Username"
    )

    email = st.text_input(
        "Email",
        placeholder="Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm = st.text_input(
        "Confirm Password",
        type="password"
    )

    st.write("")

    if st.button(
        "Create Account",
        use_container_width=True
    ):

        if not username or not email or not password:

            st.warning("Fill all fields")

            return

        if password != confirm:

            st.error("Passwords do not match")

            return

        with st.spinner("Creating account..."):

            response = signup(
                username,
                email,
                password
            )

        if response.status_code == 200:

            st.success("Account Created Successfully 🎉")

        else:

            try:

                st.error(
                    response.json()["detail"]
                )

            except:

                st.error(response.text)

    st.markdown(
        "<center>Already have an account? Click Login tab.</center>",
        unsafe_allow_html=True
    )