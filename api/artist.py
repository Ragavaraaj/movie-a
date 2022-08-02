from typing import List, Union
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import crud.artist as crud

from schemas.artist import PostArtist, GetArtist

router = APIRouter()


@router.post("")
async def post_a_new_artist(new_artist: PostArtist, db: Session = Depends(get_db)):
    return crud.create_artist(db, new_artist)


@router.get("/{artist_id}", response_model=GetArtist)
def get_a_single_artist(artist_id: str, db: Session = Depends(get_db)):
    return crud.get_artist(db, artist_id)


@router.delete("/{artist_id}")
def delete_artist(artist_id: str, db: Session = Depends(get_db)):
    return crud.delete_artist(db, artist_id)


@router.get("", response_model=List[GetArtist])
def get_all_artists(db: Session = Depends(get_db)):
    return crud.get_artists(db)
