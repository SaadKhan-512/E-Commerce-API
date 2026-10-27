from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import User_Create, Login_credentials
from database import models
from database.database import get_db
import hashing

router = APIRouter(tags=["Authentication"])

# Creating new user
@router.post("/signup")
def create_user(user_credentials: User_Create, db: Session = Depends(get_db)):
    user_data = models.User(**user_credentials.dict())
    user_data.password = hashing.hash_password(user_data.password)

    db.add(user_data)
    db.commit()

    return user_credentials

#Login
@router.post("/signin")
def login(login_credentials: Login_credentials):
    return login_credentials