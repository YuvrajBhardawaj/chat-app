from passlib.context import CryptContext
from repo import user_repo
from services.jwt_service import create_access_token
# bcrypt hashing (same as Node bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hash password before saving
def hash_password(password: str):
    return pwd_context.hash(password)

# verify password during login
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# Register logic
def register_user(db, email, password):
    # check if user exists
    existing = user_repo.get_user_by_email(db, email)
    if existing:
        return None  # user already exists

    hashed = hash_password(password)
    return user_repo.create_user(db, email, hashed)

# Login logic
def login_user(db, email, password):
    user = user_repo.get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_access_token({"sub": user.id})

    return token