from fastapi import FastAPI
from models import Base
from database import engine
from fastapi.staticfiles import StaticFiles
import pages

from api import movie, role, artist

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(pages.router, tags=["Pages"])
app.include_router(role.router, prefix="/role", tags=["Role"])
app.include_router(artist.router, prefix="/artist", tags=["Artist"])
app.include_router(movie.router, prefix="/movie", tags=["Movie"])
