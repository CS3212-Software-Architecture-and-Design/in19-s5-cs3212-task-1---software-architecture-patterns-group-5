from abc import ABC, abstractmethod

from event_bus import AbstractEvent


class AbstractSubscriber(ABC):

    @abstractmethod
    def handleEvent(self, event: AbstractEvent):
        pass
