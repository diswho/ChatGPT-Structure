# app/db/copy.py
from sqlalchemy import select
from app.db.session import SessionLocalSource, SessionLocalDestination
from app.api.v1.models import SourceModel, DestinationModel


def copy_data():
    with SessionLocalSource() as source_db:
        source_data = source_db.execute(select(SourceModel)).fetchall()

    with SessionLocalDestination() as destination_db:
        for row in source_data:
            destination_row = DestinationModel(**row)
            destination_db.execute(
                DestinationModel.__table__.insert().values(destination_row))
