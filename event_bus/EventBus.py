from AbstractSubscriber import AbstractSubscriber
from AbstractEvent import AbstractEvent


class EventBus:

    def __init__(self):
        self.subscribers_queue = set()

    def subscribe(self, subscriber: AbstractSubscriber):
        self.subscribers_queue.add(subscriber)

    def dispatch(self, event: AbstractEvent):
        self.notifySubscribers(event);

    def notifySubscribers(self, event: AbstractEvent):
        for ele in self.subscribers_queue:
            ele.handleEvent(event)
