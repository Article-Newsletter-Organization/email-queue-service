from abc import ABC
from datetime import datetime


class CustomError(ABC):
    __time__ = datetime.now().isoformat()

    def __init__(self, message, trace="", name=None):
        self.message = message
        self.trace = trace
        self.name = name or self.__class__.__name__

    def __dict__(self):
        return {
            "message": self.message,
            "trace": self.trace,
            "name": self.name,
            "timestamp": self.__time__,
        }

    def __str__(self):
        return f"[{self.__time__}] ERROR {self.name}: {self.message}"
