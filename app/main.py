from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.prediction import router as prediction_router
from app.database.database import Base, engine
from app.database.models import User, Prediction

app = FastAPI(
    title="Employee Salary Prediction",
    description="Predict Employee Salary using Machine Learning"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

app.include_router(prediction_router)


@app.get("/")
def root():
    return {
        "message": "Employee Salary Prediction API"
    }


