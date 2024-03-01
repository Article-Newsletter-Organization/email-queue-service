from data.db.database_repository import DatabaseRepository
from errors.database.database_error import DatabaseError
from infra.postgres.sqlalchemy_connect import SQLAlchemySession
from infra.postgres.sqlalchemy_models.subscribers import SubscriberAlchemyModel


class SubscriberRepository(DatabaseRepository):
    def __init__(self):
        super().__init__()

    def getSubscribers(self):
        try:
            self.logger.info("Getting a list of subscribers.")

            session = SQLAlchemySession()

            query = session.query(SubscriberAlchemyModel).filter(
                SubscriberAlchemyModel.verificate == True
            )

            return query.all()
        except Exception as e:
            error = DatabaseError(
                message="Ocorreu um erro ao tentar tentar listar os inscritos no banco de dados",
                traceback=str(e),
                metadata={"query": query.statement},
            )

            raise error
