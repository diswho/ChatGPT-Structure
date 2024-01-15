# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL_SOURCE = settings.database_url_source
DATABASE_URL_DESTINATION = settings.database_url_destination

engine_source = create_engine(DATABASE_URL_SOURCE)
engine_destination = create_engine(DATABASE_URL_DESTINATION)

SessionLocalSource = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_source)
SessionLocalDestination = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_destination)

Base = declarative_base()


def get_db():
    db = SessionLocalDestination()
    try:
        yield db
    finally:
        db.close()
