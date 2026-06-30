from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import User
from app.schema.auth_schema import UserSignup
from app.utils.hash import hash_password

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

    