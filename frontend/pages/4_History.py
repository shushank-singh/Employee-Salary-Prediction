import streamlit as st
import pandas as pd
import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from api import prediction_history

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)

if "token" not in st.session_state:
    st.warning("Please Login First")
    st.stop()

st.title("📜 Prediction History")

response = prediction_history()

if response.status_code == 200:

    data = response.json()

    if len(data) == 0:

        st.info("No Predictions Yet")

    else:

        df = pd.DataFrame(data)

        columns = [
            "job_title",
            "experience_years",
            "education_level",
            "skills_count",
            "industry",
            "company_size",
            "location",
            "remote_work",
            "certifications",
            "predicted_salary",
            "created_at"
        ]

        st.dataframe(
            df[columns],
            use_container_width=True
        )

else:

    st.error(response.text)