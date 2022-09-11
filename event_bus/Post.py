from event_bus.AbstractEvent import AbstractEvent


class Post(AbstractEvent):
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def onEvent(self,subscriberName):
        print(subscriberName+" "+"likes on "+ self.title)
    def getTitle(self):
         return self.title

    def getDescription(self):
        return self.description