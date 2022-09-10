from abc import ABC, abstractmethod
from AbstractEvent import AbstractEvent;


class AbstractSubscriber(ABC):

    @abstractmethod
    def handle(self, event: AbstractEvent):
        pass
