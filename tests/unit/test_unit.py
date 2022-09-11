import unittest

from event_bus.EventBus import EventBus
from event_bus.SubscriberImp1 import SubscriberImp1


class TestEventBus(unittest.TestCase):
    def test_subscribe_process(self):

        subscriber2 = SubscriberImp1('Nimal')
        eventbus=  EventBus()
        eventbus.subscribe(subscriber2)
        self.assertEqual(eventbus.getLenghthofQueue(), 1)



if __name__ == '__main__':
    unittest.main()
