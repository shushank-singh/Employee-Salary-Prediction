from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,Session

DATABASE_URL = "postgresql://postgres:SHUshu8400@localhost:5432/employee_salary_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()