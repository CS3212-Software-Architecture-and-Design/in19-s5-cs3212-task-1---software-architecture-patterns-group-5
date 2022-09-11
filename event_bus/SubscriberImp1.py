
from event_bus.AbstractEvent import AbstractEvent
from event_bus.AbstractSubscriber import AbstractSubscriber
from event_bus.EventBus import EventBus


class SubscriberImp1(AbstractSubscriber):
    def __init__(self, name):
        self.name = name

    def handleEvent(self, event: AbstractEvent):
        event.onEvent(self.name)


