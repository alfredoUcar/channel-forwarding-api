from abc import ABC, abstractmethod


class Channel(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
