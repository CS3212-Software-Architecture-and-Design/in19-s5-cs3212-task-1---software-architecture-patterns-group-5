from AbstractEvent import AbstractEvent


class Post(AbstractEvent):
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def onEvent(self,subscriberName):
        print(subscriberName+" "+"likes on "+ self.title)
