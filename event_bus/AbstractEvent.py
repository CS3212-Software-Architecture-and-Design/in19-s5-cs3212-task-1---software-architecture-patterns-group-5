from abc import ABC, abstractmethod


class AbstractEvent(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def onEvent(self):
        pass
