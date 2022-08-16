from fastapi import FastAPI
from models import Base
from database import engine
import pages

app = FastAPI()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(pages.router, tags=["Pages"])
