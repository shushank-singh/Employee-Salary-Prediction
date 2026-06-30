from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.prediction import router as prediction_router

app = FastAPI(
    title="Employee Salary Prediction",
    description="Predict Employee Salary using Machine Learning"
)

app.include_router(auth_router)

app.include_router(prediction_router)


@app.get("/")
def root():
    return {
        "message": "Employee Salary Prediction API"
    }


