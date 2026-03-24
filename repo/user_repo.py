from sqlalchemy.orm import Session
from models.user import User


# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# Create new user
def create_user(db: Session, email: str, password: str):
    user = User(email=email, password=password)

    db.add(user)
    db.commit()  # save to DB
    db.refresh(user)  # get updated object (with ID)

    return user