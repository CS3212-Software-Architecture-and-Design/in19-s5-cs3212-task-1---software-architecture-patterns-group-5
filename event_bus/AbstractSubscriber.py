from abc import ABC, abstractmethod
from AbstractEvent import AbstractEvent;


class AbstractSubscriber(ABC):

    @abstractmethod
    def handleEvent(self, event: AbstractEvent):
        pass
