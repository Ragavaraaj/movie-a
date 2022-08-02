from enum import Enum
from typing import Union
from pydantic import BaseModel, Field

from schemas.role import GetRole


class Gender(str, Enum):
    Male = "M"
    Female = "F"


class ArtistBase(BaseModel):
    name: str = Field(example="Jonny dip")
    gender: Gender


class PostArtist(ArtistBase):
    role_id: Union[str, None]


class GetArtist(ArtistBase):
    id: str
    role: GetRole

    class Config:
        orm_mode = True
