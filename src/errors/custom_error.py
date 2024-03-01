from abc import ABC
from datetime import datetime


class CustomError(ABC, BaseException):
    __time__ = datetime.now().isoformat()

    def __init__(
        self,
        message,
        traceback="",
        name: str = None,
        issues: list[dict | str] = [],
        metadata: dict[str, str] = None,
    ):
        self.message = message
        self.issues = issues
        self.traceback = traceback
        self.name = name or self.__class__.__name__
        self.metadata = metadata

    def __dict__(self):
        return {
            "timestamp": self.__time__,
            "message": self.message,
            "name": self.name,
            "traceback": self.traceback,
            "issues": self.issues,
            "metadata": self.metadata,
        }

    def __json__(self):
        return self.__dict__()

    def __str__(self):
        return f"[{self.__time__}] ERROR {self.name}: {self.message}"
