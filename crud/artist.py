from uuid import uuid1
from sqlalchemy import and_
from sqlalchemy.orm import Session
from models import Artist, Movie, Role
from schemas.artist import PostArtist


def get_artist(db: Session, artist_id: int):
    return db.query(Artist).filter(Artist.id == artist_id).first()


# def get_artist_id(db: Session, artist_desc: str):
#     return db.query(Artist).filter(Artist.desc == artist_desc).first()


def get_specific_artists(db: Session, type: str):
    if(type != None):
        if(type == "directors"):
            return db.query(Artist).join(Role).join(
                Movie,
                and_(Movie.director_person_id == Artist.id)
            ).all()
        if(type == "actors"):
            return db.query(Artist).join(Role).join(
                Movie,
                and_(Movie.actor_person_id == Artist.id)
            ).all()
        if(type == "actresses"):
            return db.query(Artist).join(Role).join(
                Movie,
                and_(Movie.actress_person_id == Artist.id)
            ).all()
    return db.query(Artist).all()


def create_artist(db: Session, data: PostArtist):
    gId = str(uuid1())
    db_user = Artist(
        id=gId,
        name=data.name,
        gender=data.gender,
        role_id=data.role_id
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_artist(db: Session, p_id: int):
    data = db.query(Artist).filter(Artist.id == p_id).delete()
    db.commit()
    return data
