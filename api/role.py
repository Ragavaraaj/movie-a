from typing import List, Union
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import crud.role as crud

from schemas.role import PostRole, GetRole

router = APIRouter()


@router.post("")
async def post_a_new_role(new_role: PostRole, db: Session = Depends(get_db)):
    return crud.create_role(db, new_role.desc)


@router.get("/{role_id}", response_model=GetRole)
def get_a_single_role(role_id: str, db: Session = Depends(get_db)):
    return crud.get_role(db, role_id)


@router.delete("/{role_id}")
def delete_role(role_id: str, db: Session = Depends(get_db)):
    return crud.delete_role(db, role_id)


@router.get("", response_model=List[GetRole])
def get_all_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db)
