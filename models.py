from collections import UserList
from email.policy import default
from enum import unique
from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from database import Base


class Movie(Base):
    __tablename__ = "movie"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    release_date = Column(String)

    # comments = relationship("Comment")

    director_person_id = Column(String, ForeignKey("artist.id"))
    director_person = relationship(
        "Artist",
        back_populates="movies",
        foreign_keys=[director_person_id],
        uselist=False
    )

    actor_person_id = Column(String, ForeignKey("artist.id"))
    actor_person = relationship(
        "Artist",
        back_populates="movies",
        foreign_keys=[actor_person_id],
        uselist=False
    )

    actress_person_id = Column(String, ForeignKey("artist.id"))
    actress_person = relationship(
        "Artist",
        back_populates="movies",
        foreign_keys=[actress_person_id],
        uselist=False
    )


class Artist(Base):
    __tablename__ = "artist"

    id = Column(String, primary_key=True, index=True)
    gender = Column(String)
    name = Column(String)

    role_id = Column(String, ForeignKey("role.id"))
    role = relationship("Role", back_populates="artists", uselist=False)

    movies = relationship(
        "Movie",
        primaryjoin="or_(Movie.director_person_id==Artist.id, Movie.actress_person_id==Artist.id, Movie.actor_person_id==Artist.id)"
    )


class Role(Base):
    __tablename__ = "role"

    id = Column(String, primary_key=True, index=True)
    desc = Column(String)

    artists = relationship("Artist", back_populates="role")


# class Comment(Base):
#     __tablename__ = "comment"

#     id = Column(String, primary_key=True, index=True)
#     desc = Column(String)
#     rating = Column(Float)

#     movie_id = Column(String, ForeignKey("movie.id"))
#     movie = relationship("Movie", back_populates="comments")


# class User(Base):
#     __tablename__ = "user"

#     id = Column(String, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)
