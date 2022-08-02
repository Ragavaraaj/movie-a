from uuid import uuid1
from sqlalchemy.orm import Session
from models import Artist
from schemas.artist import PostArtist


def get_artist(db: Session, artist_id: int):
    return db.query(Artist).filter(Artist.id == artist_id).first()


# def get_artist_id(db: Session, artist_desc: str):
#     return db.query(Artist).filter(Artist.desc == artist_desc).first()


def get_artists(db: Session):
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
