
from event_bus.EventBus import EventBus
from event_bus.Post import Post
from event_bus.SubscriberImp1 import SubscriberImp1
# import sys
#
# sys.path.append('H:\\CSE_5_sem\\SAD\\Task1\\in19-s5-cs3212-task-1---software-architecture-patterns-group-5')

def test_demo():
    eventbus = EventBus()
    subscriber1 = SubscriberImp1('Sumeela')
    subscriber4 = SubscriberImp1('Nuwan')
    subscriber2 = SubscriberImp1('Dinuka')
    subscriber3 = SubscriberImp1('Nisanya')
    eventbus.subscribe(subscriber1)
    eventbus.subscribe(subscriber2)
    eventbus.subscribe(subscriber3)
    post = Post("Asia cup", "Final SL vs PAK")
    sub_count=eventbus.dispatch(post)
    assert sub_count == 3

