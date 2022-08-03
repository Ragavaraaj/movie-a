from uuid import uuid1
from sqlalchemy.orm import Session
from models import Role


def get_role(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()


# def get_role_id(db: Session, role_desc: str):
#     return db.query(Role).filter(Role.desc == role_desc).first()


def get_roles(db: Session):
    return db.query(Role).all()


def create_role(db: Session, desc: str):
    gId = str(uuid1())
    db_role = Role(
        id=gId,
        desc=desc
    )

    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def delete_role(db: Session, p_id: int):
    data = db.query(Role).filter(Role.id == p_id).delete()
    db.commit()
    return data
