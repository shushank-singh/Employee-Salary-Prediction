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


def dashboard_page():

    st.title("💰 Employee Salary Prediction")
    st.caption("Predict employee salaries using Machine Learning.")

    st.write("")

    left, right = st.columns([2, 1])

    # ================= LEFT ================= #

    with left:

        st.subheader("👨‍💼 Employee Information")

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
                "Cloud Engineer",
            ],
        )

        experience_years = st.slider(
            "📈 Experience (Years)",
            min_value=0,
            max_value=25,
            value=3,
        )

        education_level = st.selectbox(
            "🎓 Education",
            [
                "Bachelor",
                "High School",
                "Diploma",
                "Master",
                "PhD",
            ],
        )

        skills_count = st.slider(
            "🛠 Skills Count",
            min_value=1,
            max_value=20,
            value=8,
        )

        industry = st.selectbox(
            "🏢 Industry",
            [
                "Technology",
                "Finance",
                "Education",
                "Retail",
                "Manufacturing",
                "Consulting",
                "Government",
                "Media",
                "Telecom",
            ],
        )

        company_size = st.selectbox(
            "🏭 Company Size",
            [
                "Startup",
                "Small",
                "Medium",
                "Large",
                "Enterprise",
            ],
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
                "Remote",
            ],
        )

        remote_work = st.radio(
            "🏠 Remote Work",
            ["Yes", "No"],
            horizontal=True,
        )

        certifications = st.slider(
            "📜 Certifications",
            min_value=0,
            max_value=10,
            value=1,
        )

        st.write("")

        predict_btn = st.button(
            "🚀 Predict Salary",
            use_container_width=True,
        )

    # ================= RIGHT ================= #

    with right:

        st.subheader("📊 Prediction Result")

        if "salary" not in st.session_state:
            st.session_state.salary = None

        if st.session_state.salary is None:

            st.info("Prediction result will appear here.")

        else:

            st.success("Prediction Successful ✅")

            st.metric(
                label="Predicted Salary",
                value=f"₹ {st.session_state.salary:,.2f}",
            )

    # ================= PREDICTION ================= #

    if predict_btn:

        payload = {
            "job_title": job_title,
            "experience_years": experience_years,
            "education_level": education_level,
            "skills_count": skills_count,
            "industry": industry,
            "company_size": company_size,
            "location": location,
            "remote_work": remote_work,
            "certifications": certifications,
        }

        with st.spinner("🤖 AI is predicting salary..."):

            response = predict_salary(payload)

        if response.status_code == 200:

            result = response.json()

            st.session_state.salary = result["predicted_salary"]

            st.balloons()

            st.rerun()

        else:

            try:

                st.error(response.json()["detail"])

            except Exception:

                st.error(response.text)