from abc import ABC, abstractmethod


class Metrics(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def __dict__(self):
        return {"name": self.name}

    @abstractmethod
    def toJSON(self):
        return self.__dict__()
