from sqlalchemy import Column, String, DateTime

from infra.postgres.sqlalchemy_connect import SQLAlchemyBase


class PublicationAlchemyModel(SQLAlchemyBase):
    __tablename__ = "publications"

    id = Column(String, primary_key=True, name="id_publication")
    articleId = Column(String)
    authorId = Column(String)
    status = Column(String)
    createdAt = Column(DateTime)
    publishedAt = Column(DateTime)
