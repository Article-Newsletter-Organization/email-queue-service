from data.db.publication.repository import PublicationRepository
from data.db.subscribers.repository import SubscriberRepository


class DatabaseService:
    def __init__(self):
        self.subscriber_repo = SubscriberRepository()
        self.publication_repo = PublicationRepository()

    def getSubscribers(self):
        subscribers = self.subscriber_repo.getSubscribers()

        return subscribers

    def getPublication(self, id: str):
        publication = self.publication_repo.getPublication(id)

        return publication

    def updatePublicationStatus(self, id: str, status: str):
        self.publication_repo.updateStatus(id, status)
