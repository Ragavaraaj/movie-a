from uuid import uuid1
from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import Comment
from schemas.comment import PostComment


def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()


# def get_comment_id(db: Session, comment_desc: str):
#     return db.query(Comment).filter(Comment.desc == comment_desc).first()


def get_comments(db: Session):
    return db.query(Comment).all()


def create_comment(db: Session, data: PostComment):
    gId = str(uuid1())
    db_comment = Comment(
        id=gId,
        desc=data.desc,
        rating=data.rating,
        movie_id=data.movie_id,
        user_id=data.user_id
    )

    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, p_id: int):
    data = db.query(Comment).filter(Comment.id == p_id).delete()
    db.commit()
    return data
