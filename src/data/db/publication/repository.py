from psycopg2 import DatabaseError
from data.db.database_repository import DatabaseRepository


class PublicationRepository(DatabaseRepository):
    def __init__(self):
        super().__init__()

    def getPublication(self, id: str):
        try:
            query = "SELECT * FROM publications WHERE id = %s"
            vars = id
            self.cursor.execute(query, vars)
            publication = self.cursor.fetchone()

            self.logger.info(
                "Publication finded",
                metadata={"query": query, "vars": vars},
            )

            return publication
        except Exception as e:
            error = DatabaseError(
                message="Ocorreu um erro ao tentar capturar a publicação da mensagem no banco de dados",
                traceback=str(e),
            )

            self.logger.error(
                error.message,
                error,
                metadata={"query": query, "vars": vars},
            )

            raise error

    def updateStatus(self, id: str, status: str):
        try:
            query = "UPDATE publications SET status = %s WHERE id = %s"
            vars = (status, id)
            self.cursor.execute(query, vars)
            self.conn.commit()

            self.logger.info(
                "Publication status changed",
                metadata={"query": query, "vars": vars},
            )
        except Exception as e:
            error = DatabaseError(
                message="Ocorreu um erro ao tentar capturar a publicação da mensagem no banco de dados",
                traceback=str(e),
            )
            self.logger.error(
                error.message,
                error,
                metadata={"query": query, "vars": vars},
            )
