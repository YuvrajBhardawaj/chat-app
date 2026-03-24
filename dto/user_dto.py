from pydantic import BaseModel

# Request body for register
class UserCreate(BaseModel):
    email: str
    password: str

# Request body for login
class UserLogin(BaseModel):
    email: str
    password: str

# Response model (optional but good practice)
class UserResponse(BaseModel):
    id: str
    email: str

    class Config:
        from_attributes = True  # allows returning ORM object directly