from operator import imod
from fastapi import FastAPI
from models import Base
from database import engine

from api import comment, movie, role, artist

app = FastAPI()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/", tags=["test"])
async def root():
    return {"message": "Hello World"}

app.include_router(role.router, prefix="/role", tags=["Role"])
app.include_router(artist.router, prefix="/artist", tags=["Artist"])
app.include_router(movie.router, prefix="/movie", tags=["Movie"])
app.include_router(comment.router, prefix="/comment", tags=["Comment"])
