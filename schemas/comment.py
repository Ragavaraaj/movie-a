from enum import Enum
from pydantic import BaseModel, Field


class CommentBase(BaseModel):
    desc: str = Field(example="very good movie")
    rating: float = Field(example=5.0)


class PostComment(CommentBase):
    movie_id: str
    pass


class GetComment(CommentBase):
    id: str

    class Config:
        orm_mode = True
