from log.custom_logger import CustomLogger
from infra.postgres.sqlalchemy_connect import initialize as sqlalchemy_init
from domain.services.database_service import DatabaseService
from errors.custom_error import CustomError
from errors.unexpected_error import UnexpectedError


class App:
    logger = CustomLogger("Application")
    database_service = DatabaseService()

    def __init__(self):
        sqlalchemy_init()

    def queueCallback(self):
        subscribers = self.database_service.getSubscribers()

    def exceptionHandler(self, error: CustomError):
        self.logger.error(error.message, error, metadata=error.metadata)

    def run(self):
        try:
            self.logger.info("Application running!")
            self.queueCallback()
        except CustomError as error:
            self.exceptionHandler(error)
        except Exception as e:
            custom_error = UnexpectedError(traceback=str(e))

            self.logger.error(custom_error.message, custom_error)
