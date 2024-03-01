from sqlalchemy import Column, String, DateTime, Boolean

from infra.postgres.sqlalchemy_connect import SQLAlchemyBase


class SubscriberAlchemyModel(SQLAlchemyBase):
    __tablename__ = "subscribers"

    id = Column(String, primary_key=True, name="id_subscriber")
    name = Column(String)
    email = Column(String)
    verificate = Column(Boolean)
    createAt = Column(DateTime)
