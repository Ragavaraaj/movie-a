from typing import List, Union
from fastapi import APIRouter, Depends, Request
from database import get_db
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from crud import movie, artist

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root(request: Request,  db: Session = Depends(get_db)):
    movieList = movie.get_movies(db)
    return templates.TemplateResponse("index.html", {"request": request, "movies": movieList})


@router.get("/directors", response_class=HTMLResponse)
async def root(request: Request,  db: Session = Depends(get_db)):
    movieList = movie.get_movies(db)
    return templates.TemplateResponse("directors.html", {"request": request, "movies": movieList})
