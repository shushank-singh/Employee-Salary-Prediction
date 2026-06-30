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

from api import predict_salary

st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💰",
    layout="wide"
)

# ---------- Login Check ----------

if "token" not in st.session_state or st.session_state.token is None:
    st.warning("🔒 Please login first.")
    st.stop()

# ---------- CSS ----------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background:linear-gradient(135deg,#0F172A,#1E293B);
}

.big-title{
font-size:40px;
font-weight:bold;
color:white;
}

.card{
padding:20px;
border-radius:15px;
background:#1E293B;
border:1px solid #334155;
}

.salary-card{
padding:30px;
border-radius:20px;
background:linear-gradient(90deg,#2563EB,#06B6D4);
text-align:center;
color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<div class="big-title">
💰 Employee Salary Prediction
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------- Layout ----------

left,right = st.columns([2,1])

# ================= LEFT ===================

with left:

    st.subheader("Employee Information")

    job_title = st.selectbox(
        "💼 Job Title",
        [
            "AI Engineer",
            "Data Analyst",
            "Frontend Developer",
            "Product Manager",
            "Business Analyst",
            "Backend Developer",
            "Machine Learning Engineer",
            "DevOps Engineer",
            "Software Engineer",
            "Cybersecurity Analyst",
            "Data Scientist",
            "Cloud Engineer"
        ]
    )

    experience_years = st.slider(
        "💼 Experience (Years)",
        0,
        25,
        3
    )

    education_level = st.selectbox(
        "🎓 Education",
        [
            "Bachelor",
            "Master",
            "PhD",
            "Diploma",
            "High School"
        ]
    )

    skills_count = st.slider(
        "🛠 Skills Count",
        1,
        20,
        8
    )

    industry = st.selectbox(
        "🏢 Industry",
        [
            "Industry",
            "Finance",
            "Education",
            "Healthcare",
            "Retail",
            "Manufacturing",
            "Consulting",
            "Government",
            "Media",
            "Telecom"
        ]
    )

    company_size = st.selectbox(
        "🏭 Company Size",
        [
            "Startup",
            "Small",
            "Medium",
            "Large",
            "Enterprise"
        ]
    )

    location = st.selectbox(
        "🌍 Country",
        [
            "India",
            "USA",
            "Canada",
            "Australia",
            "Germany",
            "UK",
            "Singapore",
            "Netherlands",
            "Sweden",
            "Remote"
        ]
    )

    remote_work = st.radio(
        "🏠 Remote Work",
        [
            "Yes",
            "No"
        ],
        horizontal=True
    )

    certifications = st.slider(
        "📜 Certifications",
        0,
        10,
        1
    )

    predict_btn = st.button(
        "🚀 Predict Salary",
        use_container_width=True
    )

# ================= RIGHT ===================

with right:

    st.markdown("""
    <div class="salary-card">
        <h2>Predicted Salary</h2>
    """, unsafe_allow_html=True)

    if "salary" in st.session_state:

        st.metric(
            label="💰 Salary",
            value=f"₹{st.session_state.salary:,.2f}"
        )

    else:

        st.info("Prediction will appear here.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Prediction ----------

if predict_btn:

    data = {

        "job_title": job_title,

        "experience_years": experience_years,

        "education_level": education_level,

        "skills_count": skills_count,

        "industry": industry,

        "company_size": company_size,

        "location": location,

        "remote_work": remote_work,

        "certifications": certifications

    }

    with st.spinner("🤖 AI is Predicting Salary..."):

        response = predict_salary(data)

    if response.status_code == 200:

        salary = response.json()["predicted_salary"]

        st.session_state.salary = salary

        st.success("Prediction Successful 🎉")

        st.balloons()

        st.rerun()

    else:

        st.error(response.json())