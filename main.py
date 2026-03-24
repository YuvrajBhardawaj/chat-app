from fastapi import FastAPI
from routes import auth
from db.database import engine, Base

# Create DB tables ONCE at startup (Code First)
Base.metadata.create_all(bind=engine)
app = FastAPI()

# Register routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])


@app.get("/")
def home():
    return {"message": "FastAPI running 🚀"}