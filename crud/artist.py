from uuid import uuid1
from sqlalchemy.orm import Session
from models import Artist, Role
from schemas.artist import PostArtist


def get_artist(db: Session, artist_id: int):
    return db.query(Artist).filter(Artist.id == artist_id).first()


def get_specific_artists(db: Session, type: str):
    if(type == None):
        return db.query(Artist).all()
    else:
        print(db.query(Artist).join(Role).filter(Role.desc == "Actor"))
        return db.query(Artist).join(Role).filter(Role.desc == "Actor").all()


def create_artist(db: Session, data: PostArtist):
    gId = str(uuid1())
    db_artist = Artist(
        id=gId,
        name=data.name,
        gender=data.gender,
        role_id=data.role_id
    )

    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist


def delete_artist(db: Session, p_id: int):
    data = db.query(Artist).filter(Artist.id == p_id).delete()
    db.commit()
    return data
