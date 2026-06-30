from sqlalchemy import Column, Integer, String, DateTime,ForeignKey,Numeric
from sqlalchemy.sql import func

from app.database.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    job_title = Column(String(100), nullable=False)

    experience_years = Column(Integer, nullable=False)

    education_level = Column(String(50), nullable=False)

    skills_count = Column(Integer, nullable=False)

    industry = Column(String(50), nullable=False)

    company_size = Column(String(30), nullable=False)

    location = Column(String(50), nullable=False)

    remote_work = Column(String(20), nullable=False)

    certifications = Column(Integer, nullable=False)

    predicted_salary = Column(Numeric(12, 2), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())