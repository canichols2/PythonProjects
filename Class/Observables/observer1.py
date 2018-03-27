class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


class Publisher:
    def __init__(self, events):
        self.subscribers = {event: dict()
                            for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who):
        self.get_subscribers(event).add(who)

    def unregister(self, event, who):
        self.get_subscribers(event).discard(who)

    def dispatch(self, event, message):
        for subscriber in self.get_subscribers(event):
            subscriber.update(message)
