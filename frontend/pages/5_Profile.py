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

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)

# ---------------- Login Check ---------------- #

if "token" not in st.session_state or st.session_state.token is None:

    st.warning("🔒 Please login first.")

    st.stop()

# ---------------- CSS ---------------- #

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background:linear-gradient(135deg,#0F172A,#1E293B);
}

.profile-card{

background:#1E293B;

padding:30px;

border-radius:20px;

border:1px solid #334155;

color:white;

}

</style>
""", unsafe_allow_html=True)

# ---------------- Profile ---------------- #

response = get_profile()

if response.status_code != 200:

    st.error("Unable to Load Profile")

    st.stop()

user = response.json()

st.title("👤 My Profile")

st.write("")

col1,col2 = st.columns([2,1])

with col1:

    st.markdown(
    f"""
    <div class="profile-card">

    <h2>{user['username']}</h2>

    <hr>

    <h4>📧 {user['email']}</h4>

    <h4>🆔 User ID : {user['id']}</h4>

    <h4>📅 Joined : {user['created_at']}</h4>

    </div>
    """,
    unsafe_allow_html=True
    )

with col2:

    st.metric(
        "Login Status",
        "✅ Active"
    )

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        logout()

        st.rerun()