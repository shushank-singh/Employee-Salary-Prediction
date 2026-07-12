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

from api import get_profile, logout


def profile_page():

    st.title("👤 My Profile")
    st.caption("Your account information")

    response = get_profile()

    if response.status_code != 200:

        st.error("Unable to load profile.")
        return

    user = response.json()

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("### 👤 User Information")

        st.info(f"**Username:** {user['username']}")

        st.info(f"**Email:** {user['email']}")

        st.info(f"**User ID:** {user['id']}")

        st.info(f"**Joined:** {user['created_at']}")

    with col2:

        st.metric(
            label="Account Status",
            value="🟢 Active"
        )

        st.metric(
            label="Authentication",
            value="✅ Logged In"
        )

        if "salary" in st.session_state and st.session_state.salary is not None:

            st.metric(
                label="Last Prediction",
                value=f"₹ {st.session_state.salary:,.2f}"
            )

        else:

            st.metric(
                label="Last Prediction",
                value="N/A"
            )