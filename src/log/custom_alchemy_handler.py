import logging

from log.custom_logger import CustomLogger
from errors.database.database_error import DatabaseError
from sqlalchemy.engine.base import ExceptionContextImpl


class CustomSQLAlchemyHandler(logging.Handler):
    logger = CustomLogger("SQLAlchemy")

    def emit(self, record):
        if record.levelno == logging.ERROR:
            print(vars(record))
            error = DatabaseError()

            self.logger.error(error)
