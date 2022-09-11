from event_bus import AbstractSubscriber, AbstractEvent


class EventBus:

    def __init__(self):
        self.subscribers_queue = set()

    def subscribe(self, subscriber: AbstractSubscriber):
        self.subscribers_queue.add(subscriber)

    def dispatch(self, event: AbstractEvent):
        return self.notifySubscribers(event);

    def notifySubscribers(self, event: AbstractEvent):
        count = 0
        for ele in self.subscribers_queue:
            count += 1
            ele.handleEvent(event)
        return count

    def getLenghthofQueue(self):
        return len(self.subscribers_queue)

    def remove_sub(self, sub: AbstractSubscriber):
        self.subscribers_queue.remove(sub)
