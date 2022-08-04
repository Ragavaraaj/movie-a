import email
from uuid import uuid1
from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import User
from schemas.user import PostUser


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# def get_user_id(db: Session, user_desc: str):
#     return db.query(User).filter(User.desc == user_desc).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, data: PostUser):
    gId = str(uuid1())
    db_user = User(
        id=gId,
        name=data.name,
        email=data.email,
        password=data.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, p_id: int):
    data = db.query(User).filter(User.id == p_id).delete()
    db.commit()
    return data
