from enum import Enum
from pydantic import BaseModel, Field


class RoleBase(BaseModel):
    desc: str = Field(example="Actor")


class PostRole(RoleBase):
    pass


class GetRole(RoleBase):
    id: str

    class Config:
        orm_mode = True
