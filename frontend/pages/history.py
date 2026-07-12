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


def history_page():

    st.title("📜 Prediction History")
    st.caption("View all your previous salary predictions.")

    response = prediction_history()

    if response.status_code != 200:

        st.error(response.text)
        return

    data = response.json()

    if len(data) == 0:

        st.info("No prediction history available.")
        return

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
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="📥 Download History as CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="salary_prediction_history.csv",
        mime="text/csv",
        use_container_width=True
    )