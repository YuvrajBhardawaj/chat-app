from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.deps import get_current_user
from dto.user_dto import UserCreate, UserLogin
from services import auth_service
from db.database import SessionLocal
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter()


# Dependency → gives new DB session per request
def get_db():
    db = SessionLocal()  # create new session
    try:
        yield db  # send it to route
    finally:
        db.close()  # close after request


# REGISTER API
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = auth_service.register_user(db, user.email, user.password)

    if not new_user:
        raise HTTPException(status_code=400, detail="User already exists")

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


# LOGIN API
@router.post("/login_swagger")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # NOTE: username field will contain email
    token = auth_service.login_user(
        db,
        form_data.username,
        form_data.password
    )

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    token = auth_service.login_user(db, user.email, user.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/profile")
def get_me(current_user = Depends(get_current_user)):
    return {
        "user_id": current_user.id,
        "email": current_user.email
    }