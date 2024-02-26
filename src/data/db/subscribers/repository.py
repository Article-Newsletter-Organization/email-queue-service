from data.db.database_repository import DatabaseRepository
from errors.database.database_error import DatabaseError


class SubscriberRepository(DatabaseRepository):
    def __init__(self):
        super().__init__()

    def getSubscribers(self):
        try:
            query = "SELECT * FROM subscribers WHERE verificate = true"
            vars = ()
            self.cursor.execute(query, vars)
            subscribers = self.cursor.fetchall()

            self.logger.info(
                "Subscribers listed successfully.",
                metadata={"query": query, "vars": vars},
            )

            return subscribers
        except Exception as e:
            error = DatabaseError(
                message="Ocorreu um erro ao tentar tentar listar os inscritos no banco de dados",
                traceback=str(e),
            )
            self.logger.error(
                error.message,
                error,
                metadata={"query": query, "vars": vars},
            )
