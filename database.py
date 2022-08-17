from os import environ
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = "postgresql://{username}:{password}@{host}:{port}/{db_name}".format(
    username=environ.get('DB_USERNAME', "postgres"),
    password=environ.get('DB_PASSWORD', "root"),
    host=environ.get('DB_HOST_NAME', "localhost"),
    port=environ.get('PORT', "5432"),
    db_name=environ.get('DB_NAME', "test")
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
