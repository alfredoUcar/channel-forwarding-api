from abc import ABC, abstractmethod


class BaseChannel(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
