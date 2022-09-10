from event_bus.EventBus import EventBus
from event_bus.Post import Post
from event_bus.SubscriberImp1 import SubscriberImp1


class Demo:
    eventbus = EventBus();
    subscriber1 = SubscriberImp1('Sumeela')
    subscriber1 = SubscriberImp1('Nuwan')
    subscriber2 = SubscriberImp1('Dinuka')
    subscriber3 = SubscriberImp1('Nisanya')
    eventbus.subscribe(subscriber1)
    eventbus.subscribe(subscriber2)
    eventbus.subscribe(subscriber3)
    post = Post("Asia cup", "Final SL vs PAK")
    eventbus.dispatch(post)
