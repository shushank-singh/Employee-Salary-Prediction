from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd

from app.schema.model_validator import Employee
from app.database.database import get_db
from app.database.models import Prediction, User
from app.dependencies.dependencies import get_current_user
from src.predict import predict_data

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.post("/predict")
def salary_predict(
    employee_data: Employee,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:

        data_info = pd.DataFrame(
            [employee_data.model_dump()]
        )

        prediction = predict_data(data_info)

        predicted_salary = round(
            float(prediction[0]), 2
        )

        new_prediction = Prediction(
            user_id=current_user.id,
            job_title=employee_data.job_title,
            experience_years=employee_data.experience_years,
            education_level=employee_data.education_level,
            skills_count=employee_data.skills_count,
            industry=employee_data.industry,
            company_size=employee_data.company_size,
            location=employee_data.location,
            remote_work=employee_data.remote_work,
            certifications=employee_data.certifications,
            predicted_salary=predicted_salary
        )

        db.add(new_prediction)
        db.commit()
        db.refresh(new_prediction)

        return {
            "message": "Prediction Saved Successfully",
            "predicted_salary": predicted_salary
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )