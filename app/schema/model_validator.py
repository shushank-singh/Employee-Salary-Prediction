from pydantic import BaseModel,Field,model_validator,ConfigDict
from typing import Annotated
from enum import Enum


class JobTitle(str,Enum):
    AI_Engineer = "AI Engineer"
    Data_Analyst = "Data Analyst"
    Frontend_Developer = "Frontend Developer"
    Product_Manager = "Product Manager"
    Business_Analyst = "Business Analyst"
    Backend_Developer = "Backend Developer"
    Machine_Learning_Engineer = "Machine Learning Engineer"
    DevOps_Engineer = "DevOps Engineer"
    Software_Engineer = "Software Engineer"
    Cybersecurity_Analyst = "Cybersecurity Analyst"
    Data_Scientist = "Data Scientist"
    Cloud_Engineer = "Cloud Engineer"

class EducationLevel(str,Enum):
    Bachelor = "Bachelor"
    PhD = "PhD"
    High_School = "High School"
    Diploma = "Diploma"
    Master = "Master"

class Industry(str,Enum):
    Industry = "Industry"
    Telecom = "Telecom"
    Media = "Media"
    Retail = "Retail"
    Manufacturing = "Manufacturing"
    Education = "Education"
    Finance = "Finance"
    Technology = "Technology"
    Consulting = "Consulting"
    Government = "Government"

class CompanySize(str,Enum):
    Medium = "Medium"
    Small = "Small"
    Large = "Large"
    Enterprise = "Enterprise"
    Startup = "Startup"

class Location(str,Enum):
    India = "India"
    Australia = "Australia"
    Singapore = "Singapore"
    Canada = "Canada"
    Sweden = "Sweden"
    USA = "USA"
    Netherlands = "Netherlands"
    Remote = "Remote"
    Germany = "Germany"
    UK = "UK"

class RemoteWork(str,Enum):
    Hybrid = "Hybrid"
    No = "No"
    Yes = "Yes"

class Employee(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )

    job_title: JobTitle
    experience_years : Annotated[int,Field(le=25,ge=0,description="Years of Professional Experience")]
    education_level : EducationLevel
    skills_count : Annotated[int,Field(le=20,ge=1,description="How Many Skills You Have")]
    industry : Industry
    company_size : CompanySize
    location : Location
    remote_work : RemoteWork
    certifications : Annotated[int,Field(le=5,ge=0,description="How Many Certificate You Have")]


    @model_validator(mode="after")
    @classmethod
    def validation(cls,value):
        if value.experience_years == 0 and value.certifications > 2:
            raise ValueError(
                "A fresher cannot have more than 2 certifications."
            )

        
        if value.experience_years >= 10 and value.skills_count < 5:
            raise ValueError(
                "Employees with 10+ years of experience should have at least 5 skills."
            )

        if value.remote_work == RemoteWork.Yes and value.location == Location.Remote:
            raise ValueError(
                "Select your actual country instead of 'Remote'."
            )
        
        if (
            value.job_title == JobTitle.AI_Engineer
            and value.education_level == EducationLevel.High_School
        ):
            raise ValueError(
                "AI Engineers must have at least a Bachelor's degree."
            )
        
        if (
            value.experience_years >= 15
            and value.skills_count < 8
        ):
            raise ValueError(
                "Senior employees should have at least 8 skills."
            )
        
        return value

    