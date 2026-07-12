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


def login_page():

    st.markdown("""
    <div class="login-box">
    <h2>💰Employee Salary Predictor</h2>
    <p>Welcome Back 👋</p>
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )

    st.write("")

    if st.button(
        "🚀 Login",
        use_container_width=True
    ):

        if not email or not password:

            st.warning("Please fill all fields")

            return

        with st.spinner("Logging in..."):

            response = login(
                email,
                password
            )

        if response.status_code == 200:

            st.success("Welcome Back!")

            st.balloons()

            st.rerun()

        else:

            try:

                st.error(
                    response.json()["detail"]
                )

            except:

                st.error(response.text)

    st.markdown(
        "<center>New user? Click the Signup tab above.</center>",
        unsafe_allow_html=True
    )