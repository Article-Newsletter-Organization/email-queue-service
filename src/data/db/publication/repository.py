from data.db.database_repository import DatabaseRepository
from errors.database.database_error import DatabaseError
from infra.postgres.sqlalchemy_connect import SQLAlchemySession
from infra.postgres.sqlalchemy_models.publications import PublicationAlchemyModel


class PublicationRepository(DatabaseRepository):
    session = SQLAlchemySession()

    def __init__(self):
        super().__init__()

    def getPublication(self, id: str):
        try:
            self.logger.info(f"Trying get the publication with id: {id}.")

            query = self.session.query(PublicationAlchemyModel).filter(
                PublicationAlchemyModel.id == id
            )

            return query.first()
        except Exception as e:
            error = DatabaseError(
                message="Ocorreu um erro ao tentar capturar a publicação da mensagem no banco de dados",
                traceback=str(e),
                metadata={"query": query.statement},
            )

            raise error

    def updateStatus(self, id: str, status: str):
        try:
            publication_query = self.session.query(PublicationAlchemyModel).filter(
                PublicationAlchemyModel.id == id
            )
            publication = publication_query.first()
            publication.status = status

            self.session.commit()

        except Exception as e:
            update_statement = publication_query.statement.compile(
                compile_kwargs={"literal_binds": True}
            )
            error = DatabaseError(
                message="Ocorreu um erro ao tentar capturar a publicação da mensagem no banco de dados",
                traceback=str(e),
                metadata={"query": str(update_statement)},
            )

            raise error
