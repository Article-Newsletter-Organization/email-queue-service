from typing import Callable

from log.custom_logger import CustomLogger
from infra.postgres.sqlalchemy_connect import initialize as sqlalchemy_init
from domain.services.database_service import DatabaseService
from errors.custom_error import CustomError
from errors.unexpected_error import UnexpectedError
from errors.email_send_error import EmailSendError
from data.queue.message_body import MessageBody
from domain.services.email_service import EmailService
from domain.services.queue_consumer import QueueConsumer


class App:
    logger = CustomLogger("Application")
    database_service = DatabaseService()
    email_service = EmailService()
    _email_list: list[str] | None = None
    _queue_consumer = QueueConsumer()

    def __init__(self):
        sqlalchemy_init()

    def _queueCallback(self, body: MessageBody, result_handler: Callable[[bool], None]):
        self.logger.info("Queue consumining...")

        self._message_body_target = body
        self._publication_target = self.database_service.getPublication(
            body.publicationId
        )

        if self._publication_target is None:
            result_handler(False)
            raise UnexpectedError("Publication not found")

        self._email_list = list(
            map(
                lambda subscriber: subscriber.email,
                self.database_service.getSubscribers(),
            )
        )
        self._emailHandler()

        result_handler(True)

    def _emailHandler(self):
        self.logger.info(f"Trying to send {len(self._email_list)} email(s)")

        emailsCount = 0
        for email in self._email_list:
            try:
                self.email_service.sendEmail(
                    email,
                    self._message_body_target.body,
                    self._message_body_target.subject,
                )
                emailsCount += 1

            except Exception as e:
                custom_error = EmailSendError(
                    traceback=str(e), metadata={"email": email}
                )
                self.logger.error(custom_error.message, custom_error)

        self.logger.info(f"Emails sent successfully: {emailsCount}")

    def _exceptionHandler(self, error: CustomError):
        self.logger.error(error.message, error, metadata=error.metadata)

    def run(self):
        try:
            self.logger.info("Application running!")
            self._queue_consumer.consume(self._queueCallback)
            while True:
                """"""
        except CustomError as error:
            self._exceptionHandler(error)
        except Exception as e:
            custom_error = UnexpectedError(traceback=str(e))

            self.logger.error(custom_error.message, custom_error)
        finally:
            self.logger.info("Closing application...")
            self.logger.info("Application closed!")
