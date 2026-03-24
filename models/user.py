import uuid
from sqlalchemy import Column, String
from db.database import Base

class User(Base):
    __tablename__ = "users"

    # UUID as primary key
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    email = Column(String, unique=True, index=True)
    password = Column(String)