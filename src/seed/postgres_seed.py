from sqlalchemy import insert
import json
import os

from errors.database.database_error import DatabaseError
from infra.postgres.sqlalchemy_connect import SQLAlchemySession
from infra.postgres.sqlalchemy_models.subscribers import SubscriberAlchemyModel
from infra.postgres.sqlalchemy_models.publications import PublicationAlchemyModel

current_path = os.path.dirname(os.path.abspath(__file__))

subscribers_data_file_path = os.path.join(current_path, "data/subscribers_data.json")

publications_data_file_path = os.path.join(current_path, "data/publications_data.json")

def uploadSubscribers():
    print("Uploading the publications dummy data for test")
    try:
        with open(subscribers_data_file_path, "r+", encoding="utf-8") as file:
            subscribers_data = json.load(file)

            session = SQLAlchemySession()

            session.execute(insert(SubscriberAlchemyModel), subscribers_data)

            session.commit()
    except Exception as e:
        error = DatabaseError(
            message="An error occurred while trying to insert data into the database",
            traceback=str(e),
        )

        raise error


def uploadPublications():
    try:
        print("Uploading the publications dummy data for test")
        with open(publications_data_file_path, "r+", encoding="utf-8") as file:
            publications_data = json.load(file)

            session = SQLAlchemySession()

            session.execute(insert(PublicationAlchemyModel), publications_data)

            session.commit()
    except Exception as e:
        error = DatabaseError(
            message="An error occurred while trying to insert data into the database",
            traceback=str(e),
        )

        raise error
