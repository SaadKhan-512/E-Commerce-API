from fastapi import FastAPI, Request
from routes.crud import router
from database import models
from database.database import Base, engine
import oauth2


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
app.include_router(oauth2.router)