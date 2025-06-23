from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, name: str, email: str, age: int):
    db_user = User(name=name, email=email, age=age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()