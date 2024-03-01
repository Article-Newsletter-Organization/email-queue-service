"""
Postgres Module:

Responsável pela conexão e gerenciamento da integração do banco de dados com o script.
"""

import logging
import uuid

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.env import getEnvParams


SQLAlchemyBase = declarative_base()


def get_database_url() -> str:
    data = getEnvParams()["postgres"]

    return data["database_url"]


SQLAlchemyEngine = create_engine(url=get_database_url())

SQLAlchemySession = sessionmaker(bind=SQLAlchemyEngine)

SQLAlchemyBase.metadata.create_all(SQLAlchemyEngine)

def get_uuid():
    return str(uuid.uuid4())


def initialize():
    logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)
    SQLAlchemyBase.metadata.create_all(SQLAlchemyEngine)
