from fastapi import FastAPI
from models import Base
from database import engine
from fastapi.staticfiles import StaticFiles
import pages

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(pages.router, tags=["Pages"])
