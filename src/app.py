from log.custom_logger import CustomLogger
from data.db.publication.repository import PublicationRepository
from data.db.subscribers.repository import SubscriberRepository


class App():
    logger = CustomLogger()

    def __init__(self):
        self.subscriber_repo = SubscriberRepository()
        self.publication_repo = PublicationRepository()

    def run(self):
        self.logger.info("Application running!")
