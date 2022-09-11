import unittest

from event_bus.EventBus import EventBus
from event_bus.Post import Post
from event_bus.SubscriberImp1 import SubscriberImp1


class TestEventBus(unittest.TestCase):
    def test_subscribe_process(self):
        subscriber2 = SubscriberImp1('Nimal')
        eventbus = EventBus()
        eventbus.subscribe(subscriber2)
        self.assertEqual(eventbus.getLenghthofQueue(), 1)


    def test_remove_sub_process(self):
        subscriber1 = SubscriberImp1('sumeela')
        subscriber2 = SubscriberImp1('dinuka')
        eventbus=  EventBus()
        eventbus.subscribe(subscriber1)
        eventbus.subscribe(subscriber2)
        eventbus.remove_sub(subscriber1)
        self.assertEqual(eventbus.getLenghthofQueue(), 1)


    def test_post_process(self):
        post = Post("Asia cup", "Asia cup final SL vs PAK")
        self.assertEqual(post.getTitle(), "Asia cup")
        self.assertEqual(post.getDescription(), "Asia cup final SL vs PAK")

    def test_psubscriber(self):
        subscriber = SubscriberImp1("Kasun")
        self.assertEqual(subscriber.getName(), "Kasun")



if __name__ == '__main__':
    unittest.main()
