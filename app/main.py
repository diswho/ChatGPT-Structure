from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import endpoints
from app.core.database import engine_internal, engine_external, SessionLocalInternal, SessionLocalExternal,Base

from app.core.config import settings
from app.crud.user import create_user
from app.schemas.user import UserCreate


# Initialize the database
def init_db():
    db = SessionLocalInternal()
    Base.metadata.create_all(bind=engine_internal)

    # Create the first superuser
    superuser = create_user(
        db,
        UserCreate(email=settings.FIRST_SUPERUSER,
                   password=settings.FIRST_SUPERUSER_PASSWORD),
    )

    db.close()


# init_db()

app = FastAPI()

# Set CORS origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for internal database


def get_db_internal():
    db = SessionLocalInternal()
    try:
        yield db
    finally:
        db.close()

# Dependency for external database


def get_db_external():
    db = SessionLocalExternal()
    try:
        yield db
    finally:
        db.close()


app.include_router(endpoints.router, prefix=settings.API_V1_STR)
