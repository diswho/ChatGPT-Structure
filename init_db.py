# init_db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.api.v1.models.user import UserModel
from app.core.config import settings
from app.core.security import get_password_hash

# DATABASE_URL = settings.database_url_source
DATABASE_URL = settings.database_url_destination

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        # Check if the default user already exists
        existing_user = db.query(UserModel).filter(
            UserModel.username == settings.admin_username).first()
        if existing_user:
            print(
                f"User '{settings.admin_username}' already exists in the database. Skipping initialization.")
            return

        # Create the default user
        hashed_password = get_password_hash(settings.admin_password)
        new_user = UserModel(username=settings.admin_username,
                             hashed_password=hashed_password, email=settings.admin_username + "@example.com")
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(
            f"User '{settings.admin_username}' successfully created in the database.")


if __name__ == "__main__":
    init_db()
