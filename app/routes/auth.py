from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from passlib.context import CryptContext
from app.core.db import db

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegisterRequest(BaseModel):
    role: str
    userId: str          # Farmer ID / GST ID / phone number, depending on role
    contact: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str

class LoginRequest(BaseModel):
    role: str
    userId: str
    password: str

@router.post("/register")
async def register(user: RegisterRequest):
    existing = await db.users.find_one({"role": user.role, "userId": user.userId})
    if existing:
        raise HTTPException(status_code=400, detail="This ID is already registered for this role")

    hashed_password = pwd_context.hash(user.password)
    new_user = {
        "role": user.role,
        "userId": user.userId,
        "contact": user.contact,
        "email": user.email,
        "password": hashed_password,
    }
    result = await db.users.insert_one(new_user)
    return {"message": "Registered successfully", "id": str(result.inserted_id)}

@router.post("/login")
async def login(credentials: LoginRequest):
    user = await db.users.find_one({"role": credentials.role, "userId": credentials.userId})
    if not user or not pwd_context.verify(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "role": user["role"]}