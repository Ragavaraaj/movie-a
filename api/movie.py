from typing import List, Union
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import crud.movie as crud

from schemas.movie import PostMovie, GetMovie

router = APIRouter()


@router.post("")
async def post_a_new_movie(new_movie: PostMovie, db: Session = Depends(get_db)):
    return crud.create_movie(db, new_movie)


@router.get("/{movie_id}", response_model=GetMovie)
def get_a_single_movie(movie_id: str, db: Session = Depends(get_db)):
    return crud.get_movie(db, movie_id)


@router.delete("/{movie_id}")
def delete_movie(movie_id: str, db: Session = Depends(get_db)):
    return crud.delete_movie(db, movie_id)


@router.get("", response_model=List[GetMovie])
def get_all_movies(db: Session = Depends(get_db)):
    return crud.get_movies(db)
