from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from routes.crud import router
from database import models
from database.database import Base, engine
import oauth2


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
app.include_router(oauth2.router)