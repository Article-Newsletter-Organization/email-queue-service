from datetime import datetime
from errors.custom_error import CustomError
from models.metric_model import Metrics
import logging


class LogModel:
    def __init__(
        self,
        name: str,
        message: str,
        level="INFO",
        error: CustomError = None,
        metrics: Metrics = None,
        metadata: dict = None,
    ):
        self.name = name
        self.message = message
        self.level = level
        self.error = error
        self.metrics = metrics
        self.metadata = metadata
        self.timestamp = datetime.now().isoformat()

    def __dict__(self):
        return dict(
            {
                "timestamp": self.timestamp,
                "level": self.level,
                "name": self.name,
                "message": self.message,
                "error": self.error.__dict__() if self.error else None,
                "metrics": self.metrics.__dict__() if self.metrics else None,
                "metadata": self.metadata,
            }
        )

    def __json__(self):
        return self.__dict__()
