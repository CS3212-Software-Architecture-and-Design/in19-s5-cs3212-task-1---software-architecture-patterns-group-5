

from AbstractSubscriber import AbstractSubscriber


class SubscriberImp1(AbstractSubscriber):
    def __init__(self, name):
        self.name = name
        self.subscribers_queue = set()
@abstractmethod
    def handle(self, event: AbstractEvent):
        pass