from AbstractSubscriber import AbstractSubscriber
from AbstractEvent import AbstractEvent
from collections import defaultdict


class AbstractEventBus:

    def __init__(self):
        self.subscribers_queue = set()

    def subscribe(self, subscriber: AbstractSubscriber):
        self.subscribers_queue.add(subscriber)

    def dispatch(self, event: AbstractEvent):
        pass

    def getSubscribers(self):
        pass
