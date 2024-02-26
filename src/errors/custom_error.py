from abc import ABC
from datetime import datetime


class CustomError(ABC):
    __time__ = datetime.now().isoformat()

    def __init__(
        self, message, traceback="", name: str = None, issues: list[dict | str] = []
    ):
        self.message = message
        self.issues = issues
        self.traceback = traceback
        self.name = name or self.__class__.__name__

    def __dict__(self):
        return {
            "timestamp": self.__time__,
            "message": self.message,
            "name": self.name,
            "traceback": self.traceback,
            "issues": self.issues,
        }

    def __json__(self):
        return self.__dict__()

    def __str__(self):
        return f"[{self.__time__}] ERROR {self.name}: {self.message}"
