from enum import Enum
from inspect import getcomments
from typing import List
from pydantic import BaseModel, Field

from schemas.comment import GetComment


class UserBase(BaseModel):
    name: str = Field(example="raj")
    email: str = Field(example="raj@example.com")


class PostUser(UserBase):
    password: str = Field(example="123")
    pass


class GetUser(UserBase):
    id: str
    comments: List[GetComment]

    class Config:
        orm_mode = True
