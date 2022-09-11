import unittest

from event_bus.EventBus import EventBus
from event_bus.SubscriberImp1 import SubscriberImp1


class TestEventBus(unittest.TestCase):
    def test_subscribe_process(self):

        subscriber2 = SubscriberImp1('Nimal')
        eventbus=  EventBus()
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








if __name__ == '__main__':
    unittest.main()
