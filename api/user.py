from typing import List, Union
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import crud.user as crud

from schemas.user import PostUser, GetUser

router = APIRouter()


@router.post("")
async def post_a_new_user(new_user: PostUser, db: Session = Depends(get_db)):
    return crud.create_user(db, new_user)


@router.get("/{user_id}", response_model=GetUser)
def get_a_single_user(user_id: str, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@router.delete("/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)


@router.get("", response_model=List[GetUser])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
