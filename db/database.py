from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite DB (easy for beginners)
DATABASE_URL = "sqlite:///./test.db"

# engine = connection to DB
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite
)

# SessionLocal = factory to create DB sessions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class → all models will inherit this
Base = declarative_base()