from uuid import uuid1
from sqlalchemy.orm import Session
from models import Movie
from schemas.movie import PostMovie


def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


# def get_movie_id(db: Session, movie_desc: str):
#     return db.query(Movie).filter(Movie.desc == movie_desc).first()


def get_movies(db: Session):
    return db.query(Movie).all()


def create_movie(db: Session, data: PostMovie):
    gId = str(uuid1())
    db_movie = Movie(
        id=gId,
        name=data.name,
        release_date=data.release_date,
        actor_person_id=data.actor_person_id,
        actress_person_id=data.actress_person_id,
        director_person_id=data.director_person_id
    )

    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, p_id: int):
    data = db.query(Movie).filter(Movie.id == p_id).delete()
    db.commit()
    return data
