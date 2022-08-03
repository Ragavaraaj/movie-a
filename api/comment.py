from typing import List, Union
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import crud.comment as crud

from schemas.comment import PostComment, GetComment

router = APIRouter()


@router.post("")
async def post_a_new_comment(new_comment: PostComment, db: Session = Depends(get_db)):
    return crud.create_comment(db, new_comment)


@router.get("/{comment_id}", response_model=GetComment)
def get_a_single_comment(comment_id: str, db: Session = Depends(get_db)):
    return crud.get_comment(db, comment_id)


@router.delete("/{comment_id}")
def delete_comment(comment_id: str, db: Session = Depends(get_db)):
    return crud.delete_comment(db, comment_id)


@router.get("", response_model=List[GetComment])
def get_all_comments(db: Session = Depends(get_db)):
    return crud.get_comments(db)
