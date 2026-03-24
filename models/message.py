from sqlalchemy import Column, String, DateTime

from db.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True)
    sender_id = Column(String)
    room_id = Column(String)
    content = Column(String)
    created_at = Column(DateTime)