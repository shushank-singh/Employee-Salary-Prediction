from pydantic import BaseModel, EmailStr, Field


class UserSignup(BaseModel):

    username: str = Field(min_length=3, max_length=100)

    email: EmailStr

    password: str = Field(min_length=8, max_length=50)


class UserLogin(BaseModel):

    email: EmailStr

    password: str