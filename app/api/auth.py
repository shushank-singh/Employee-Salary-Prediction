from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import User
from app.schema.auth_schema import UserSignup,UserLogin
from app.utils.hash import hash_password,verify_password
from app.utils.jwt import create_access_token
from app.dependencies.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        return {"message": "Email already exists"}   
    
    print("Password:", user.password)
    print("Type:", type(user.password))
    print("Length:", len(user.password))
    
    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message":"User Created Successfully"
    }


@router.post("/login")
def login(user: UserLogin,
          db: Session = Depends(get_db)):
    
    db_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not db_user:
        return {
            "message": "Invalid Email or Password"
        }
    
    if not verify_password(user.password , db_user.password):
        return {
            "message": "Invalid Email or Password"
        }
    
    access_token = create_access_token(
        {
            "sub": str(db_user.id)
        }
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"

    }


@router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }