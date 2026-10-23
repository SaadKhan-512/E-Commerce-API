from fastapi import FastAPI
from routes.crud import router
from database import models
from database.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)