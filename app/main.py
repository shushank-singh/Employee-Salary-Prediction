from fastapi import FastAPI,HTTPException
from app.schema.model_validator import Employee
from src.predict import predict_data
import pandas as pd


app = FastAPI(title="Employee Salary Prediction",description="Predict what the salary of each employee")

@app.get("/")
def root():
    return {"message":"Employee Salary"}


@app.post("/predict")
def salary_predict(employee_data:Employee):
    try:
        data_info = pd.DataFrame([employee_data.model_dump()])
        prediction = predict_data(data_info)

        return {
            "predicted_salary": round(float(prediction[0]),2)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,detail=str(e)
        )



