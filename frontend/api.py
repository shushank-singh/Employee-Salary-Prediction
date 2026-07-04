import requests
import streamlit as st

BASE_URL = "https://employee-salary-prediction-frzc.onrender.com"


# ---------------- SIGNUP ---------------- #

def signup(username, email, password):

    response = requests.post(
        f"{BASE_URL}/auth/signup",
        json={
            "username": username,
            "email": email,
            "password": password
        }
    )

    return response


# ---------------- LOGIN ---------------- #

def login(email, password):

    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    if response.status_code == 200:

        data = response.json()

        st.session_state.token = data["access_token"]

    return response


# ---------------- PROFILE ---------------- #

def get_profile():

    headers = {
        "Authorization":
        f"Bearer {st.session_state.token}"
    }

    return requests.get(
        f"{BASE_URL}/auth/me",
        headers=headers
    )


# ---------------- LOGOUT ---------------- #

def logout():

    st.session_state.token = None

    if "salary" in st.session_state:
        del st.session_state.salary

    st.success("Logged Out Successfully")


# ---------------- PREDICTION ---------------- #

def predict_salary(data):

    headers = {
        "Authorization":
        f"Bearer {st.session_state.token}"
    }

    return requests.post(
        f"{BASE_URL}/prediction/predict",
        json=data,
        headers=headers
    )


# ---------------- HISTORY ---------------- #

def prediction_history():

    headers = {
        "Authorization":
        f"Bearer {st.session_state.token}"
    }

    return requests.get(
        f"{BASE_URL}/prediction/history",
        headers=headers
    )