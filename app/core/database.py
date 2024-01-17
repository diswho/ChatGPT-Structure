from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL_INTERNAL = "sqlite:///destination.db"
SQLALCHEMY_DATABASE_URL_EXTERNAL = r"sqlite:///C:\\Users\\vieng\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"

engine_internal = create_engine(SQLALCHEMY_DATABASE_URL_INTERNAL)
engine_external = create_engine(SQLALCHEMY_DATABASE_URL_EXTERNAL)

SessionLocalInternal = sessionmaker(autocommit=False, autoflush=False, bind=engine_internal)
SessionLocalExternal = sessionmaker(autocommit=False, autoflush=False, bind=engine_external)

Base = declarative_base()
